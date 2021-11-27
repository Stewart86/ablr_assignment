import json
import logging
from typing import Any

from django.http import HttpRequest, HttpResponseRedirect
from django.http.response import (
    HttpResponseBadRequest,
    HttpResponseServerError,
    JsonResponse,
)
from requests.exceptions import HTTPError

from .myinfo_client import MyInfoClient
from .security import get_decoded_access_token, get_decrypted_person_data

log = logging.getLogger(__name__)


def login(request: HttpRequest):
    if request.method == "GET":
        return HttpResponseRedirect(MyInfoClient.get_authorise_url(state="demo"))
    return HttpResponseBadRequest()


def retrieve(request: HttpRequest):
    if request.method == "POST":
        try:
            code = json.loads(request.body.decode("utf-8"))["code"]
        except json.JSONDecodeError:
            return HttpResponseBadRequest("request body is not the accepted structure")
        client = MyInfoClient()

        print(code)

        access_token: str = ""
        try:
            resp = client.get_access_token(code)
            access_token = resp["access_token"]
        except HTTPError as err:
            log.error(err)
            return HttpResponseBadRequest(
                "Something when wrong when connection to MyInfo"
            )

        decoded_access_token: dict[str, Any] = get_decoded_access_token(access_token)
        uinfin: str = decoded_access_token["sub"]

        person: dict[str, Any]
        try:
            person = client.get_person(uinfin, access_token)
            if not isinstance(person, str):
                log.error("person should be string: %s", person)
                return HttpResponseServerError()
        except HTTPError as err:
            log.error(err)
            return HttpResponseBadRequest(
                "Something when wrong when connection to MyInfo"
            )

        decrypted = get_decrypted_person_data(person)
        return JsonResponse(decrypted)
    return HttpResponseBadRequest()
