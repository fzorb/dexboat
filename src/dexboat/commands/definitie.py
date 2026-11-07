import html
import json
import re

import requests


def definitie(interaction: dict) -> dict:
    cuvant = interaction["options"][0]["value"]
    dexonline_req: dict = json.loads(requests.get(f"https://dexonline.ro/definitie/{cuvant}/json").text)
    if len(dexonline_req["definitions"]) <= 0:
        return {
            "type": 4,
            "data": {"content": "Cuvântul introdus nu există în DEX. L-ai scris corect?"},
        }

    text = html.unescape(
        re.sub(r"[@#$]", "", dexonline_req["definitions"][0]["internalRep"])
    )
    text = text.replace("&039;", "") # Dumnezeu cu mila!

    text = re.sub(r"^([^,]+)", r"**\1**", text)

    return {
        "type": 4,
        "data": {"content": text},
    }
