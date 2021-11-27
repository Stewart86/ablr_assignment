import logging
import time
from base64 import b64encode
from typing import Any, Optional, Tuple
from urllib.parse import quote, urlencode

import jwt
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.x509 import load_pem_x509_certificate
from cryptography.x509.base import Certificate
from django.utils.encoding import force_bytes, force_text
from jwcrypto import jwe, jwk

from ablr import settings

log = logging.getLogger(__name__)

myinfo_cert_obj: Certificate = load_pem_x509_certificate(
    settings.MYINFO_PUBLIC_CERT.encode()
)
public_key_str = myinfo_cert_obj.public_key()


def create_signature(
    raw_message: str, private_key_data: Optional[str] = settings.MYINFO_PRIVATE_KEY
) -> str:
    private_key = serialization.load_pem_private_key(
        force_bytes(private_key_data), password=None
    )
    signature = private_key.sign(
        force_bytes(raw_message), padding.PKCS1v15(), hashes.SHA256()  # type: ignore
    )
    return force_text(b64encode(signature))


def generate_authorization_header(
    url: str, params: dict[str, Any], method: str, app_id: str
) -> str:
    """
    See: https://www.ndi-api.gov.sg/assets/lib/trusted-data/myinfo/specs/myinfo-kyc-v2.1.1.yaml.html#section/Security/Request-Signing  # noqa: E501
    """
    # A) Construct the Authorisation Token Parameters
    timestamp: int = int(time.time() * 1000)
    nonce: int = timestamp * 100
    default_apex_headers: dict[str, Any] = {
        "app_id": settings.MYINFO_CLIENT_ID,
        "nonce": nonce,
        "signature_method": "RS256",
        "timestamp": timestamp,
    }

    # B) Forming the Base String
    # Base String is a representation of the entire request (ensures message integrity)
    base_params: dict[str, Any] = default_apex_headers.copy()
    base_params.update(params)
    query: list[Tuple[str, Any]] = sorted(base_params.items())
    base_params_str: str = urlencode(query, safe=",/:", quote_via=quote)

    base_string: str = f"{method.upper()}&{url}&{base_params_str}"

    # C) Signing Base String to get Digital Signature
    signature: str = create_signature(base_string)
    log.info("Signature: %s", signature)

    # D) Assembling the Authorization Header
    return (
        f"PKI_SIGN "
        f'app_id="{app_id}",'
        f'timestamp="{timestamp}",'
        f'nonce="{nonce}",'
        'signature_method="RS256",'
        f'signature="{signature}"'
    )


def get_decoded_access_token(access_token: str) -> dict[str, Any]:
    return jwt.decode(
        access_token,
        public_key_str,
        algorithms=["RS256"],
        options={"verify_aud": False},
    )


def get_decrypted_person_data(person_data: str) -> dict[str, Any]:
    jwetoken = jwe.JWE()
    private_key = jwk.JWK.from_pem(force_bytes(settings.MYINFO_PRIVATE_KEY))
    jwetoken.deserialize(person_data, key=private_key)
    decoded = force_text(jwetoken.payload)
    decoded = decoded.strip('"')
    log.debug("decoded = %s", decoded)
    return jwt.decode(decoded, public_key_str, algorithms=["RS256"])
