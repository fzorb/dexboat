import html
import json
import re
from datetime import datetime
from zoneinfo import ZoneInfo

import requests


def cuvantul_zilei(interaction: dict) -> dict:
    dexonline_req: dict = json.loads(requests.get(f"https://dexonline.ro/cuvantul-zilei/{datetime.now(ZoneInfo("Europe/Bucharest")).strftime('%Y/%d/%m')}/json").text)
    if dexonline_req["requested"] == None:
        return {
            "type": 4,
            "data": {"content": "Cuvântul zilei nu este valabil încă."},
        }


    cuvantul_zilei = dexonline_req["requested"]["record"]

    definitie = html.unescape(
        re.sub(r"[@#$]", "", cuvantul_zilei["definition"]["internalRep"])
    )
    definitie = definitie.replace("&039;", "") # Dumnezeu cu mila!

    definitie = re.sub(r"^([^,]+)", r"**\1**", definitie)

    text = f"**Cuvântul zilei {datetime.now(ZoneInfo("Europe/Bucharest")).strftime('%d/%m/%Y')} - {cuvantul_zilei["word"]}**\n\n{definitie}\n\n**Cheia alegerii:** {cuvantul_zilei["reason"]}\n{cuvantul_zilei["image"]}"

    return {
        "type": 4,
        "data": {"content": text},
    }
