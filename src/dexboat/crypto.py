import time

from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives.asymmetric import ed25519

from dexboat.config import ALLOWED_CLOCK_SKEW, DISCORD_PUBLIC_KEY


def verify_request(signature: str, data: bytes, timestamp: int) -> bool:
    if int(time.time()) - ALLOWED_CLOCK_SKEW > timestamp:
        return False
    public_key = ed25519.Ed25519PublicKey.from_public_bytes(bytes.fromhex(DISCORD_PUBLIC_KEY))
    try:
        public_key.verify(
            signature=bytes.fromhex(signature),
            data=str(timestamp).encode() + data,
        )
    except InvalidSignature:
        return False
    return True
