import requests

from dexboat import config


def register(commands) -> bool:
    payload = []
    for command in commands:
        payload.append(command.get_json())

    request = requests.put(json=payload, headers={"Authorization": f"Bot {config.TOKEN}", "Content-Type": "application/json"}, url=f"https://discord.com/api/v10/applications/{config.APPLICATION_ID}/commands")
    if request.status_code != 200:
        raise Exception(f"Could not register commands! {request.content}") #noqa: TRY002
    print(payload)
    return True
