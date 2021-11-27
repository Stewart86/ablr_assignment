import logging
from json import JSONDecodeError
from typing import Any, Final, Union
from urllib.parse import quote, urlencode

import requests
from requests.models import Response
from requests.sessions import Session

from ablr import settings

from .security import generate_authorization_header

log = logging.getLogger(__name__)


class MyInfoClient:
    """
    See API doc at https://public.cloud.myinfo.gov.sg/myinfo/api/myinfo-kyc-v3.1.1.html
    Test data: https://www.ndi-api.gov.sg/library/trusted-data/myinfo/resources-personas.

    >>> from myinfo.client import MyInfoClient
    >>> from myinfo.security import get_decoded_access_token, get_decrypted_person_data
    >>>
    >>> client = MyInfoClient()
    >>> client.get_authorise_url(state="blahblah")
    >>>
    >>> # Open up this SingPass Authorise URL and follow instructions
    >>> # After clicking on the green "I Agree" button, you'll be redirected back to
    >>> # http://localhost:3001/callback?code=25e3a9679bfc9baca7ef47bceadea43fcd6eb199&state=blahblah
    >>> # Then grab the code for the next API call
    >>>
    >>> # Getting access token with code
    >>>
    >>> code = "25e3a9679bfc9baca7ef47bceadea43fcd6eb199"
    >>> resp = client.get_access_token(code)
    >>> access_token = resp["access_token"]
    >>>
    >>> # Decoding access token
    >>> decoded_access_token = get_decoded_access_token(access_token)
    >>> uinfin = decoded_access_token["sub"]
    >>>
    >>> # Getting person data
    >>> resp = client.get_person(uinfin=uinfin, access_token=access_token)
    >>> decrypted = get_decrypted_person_data(resp)
    >>> print(decrypted)
    """

    API_TIMEOUT: Final = 30

    def __init__(self):
        """
        Initialize a request session to interface with remote API
        """
        self.session: Session = requests.Session()

    @staticmethod
    def get_authorise_url(state: str, callback_url: str = None) -> str:
        """
        Return a redirect URL to SingPass login page for user's authentication and consent.
        """
        # At the moment, only this URL is whitelisted as we're using key from MyInfo demo app
        # https://github.com/ndi-trusted-data/myinfo-demo-app
        # Otherwise, we would get this error:
        # `redirect_uri_mismatch The redirection URI provided does not match a pre-registered value.`
        if not callback_url:
            callback_url = "http://localhost:3001/callback"

        query: dict[str, str] = {
            "client_id": settings.MYINFO_CLIENT_ID,
            "attributes": settings.MYINFO_ATTRS,
            "purpose": "credit risk assessment",
            "state": state,
            "redirect_uri": callback_url,
        }
        querystring: str = urlencode(query, safe=",/:", quote_via=quote)
        authorise_url: str = f"{settings.MYINFO_ROOT}/authorise?{querystring}"
        return authorise_url

    def get_access_token(
        self, auth_code: str, callback_url: str = None
    ) -> Union[str, dict[str, Any]]:
        """
        Generate an access token when presented with a valid authcode obtained from the Authorise API.
        This token can then be used to request for the user's data that were consented.

        """
        # At the moment, only this URL is whitelisted as we're using key from MyInfo demo app
        # https://github.com/ndi-trusted-data/myinfo-demo-app
        # Otherwise, we would get this error:
        # `redirect_uri_mismatch The redirection URI provided does not match a pre-registered value.`
        if not callback_url:
            callback_url = "http://localhost:3001/callback"

        api_url: str = f"{settings.MYINFO_ROOT}/token"
        params: dict[str, str] = {
            "client_id": settings.MYINFO_CLIENT_ID,
            "client_secret": settings.MYINFO_SECRET,
            "code": auth_code,
            "grant_type": "authorization_code",
            "redirect_uri": callback_url,
        }
        auth_header: str = generate_authorization_header(
            url=api_url, params=params, method="POST", app_id=settings.MYINFO_CLIENT_ID
        )
        log.info("auth_header: %s", auth_header)

        return self.__request(
            api_url, method="POST", auth_header=auth_header, data=params
        )

    def get_person(self, uinfin: str, access_token: str) -> Union[str, dict[str, Any]]:
        """
        Return user's data from MyInfo when presented with a valid access token obtained from the Token API.
        """
        api_url: str = f"{settings.MYINFO_ROOT}/person/{uinfin}/"
        params: dict[str, str] = {
            "client_id": settings.MYINFO_CLIENT_ID,
            "attributes": settings.MYINFO_ATTRS,
        }
        auth_header: str = generate_authorization_header(
            url=api_url, params=params, method="GET", app_id=settings.MYINFO_CLIENT_ID
        )
        auth_header += f",Bearer {access_token}"
        log.info("auth_header: %s", auth_header)

        return self.__request(
            api_url, method="GET", auth_header=auth_header, params=params
        )

    def __request(
        self,
        api_url: str,
        method: str = "GET",
        auth_header: str = None,
        params: dict[str, Any] = None,
        data: Any = None,
    ) -> Union[str, dict[str, Any]]:
        """A private method to send request to MyInfo

        Raises:
            requests.RequestException
        """
        headers: dict[str, str] = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Cache-Control": "no-cache",
        }
        if auth_header:
            headers["Authorization"] = auth_header

        log.info("headers = %s", headers)
        response: Response = self.session.request(
            method,
            url=api_url,
            params=params,
            data=data,
            timeout=self.API_TIMEOUT,
            verify=settings.CERT_VERIFY,
            headers=headers,
        )

        response.raise_for_status()

        try:
            return response.json()
        except JSONDecodeError:
            return response.text
