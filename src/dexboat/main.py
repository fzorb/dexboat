import flask
import functions_framework
from flask.json import jsonify
from flask.typing import ResponseReturnValue

from dexboat.commands.commands import COMMANDS
from dexboat.crypto import verify_request

#register(COMMANDS)

@functions_framework.http
def bot(request: flask.Request) -> ResponseReturnValue:
    if (request.method == "POST"):
        signature = request.headers.get("X-Signature-Ed25519")
        timestamp_header = request.headers.get("X-Signature-Timestamp")

        if signature is None or timestamp_header is None:
            return "missing signature headers", 401, {"Content-Type": "text/plain"}

        try:
            timestamp = int(timestamp_header)
        except ValueError:
            return "invalid timestamp", 401, {"Content-Type": "text/plain"}

        if not verify_request(signature=signature, data=request.get_data(), timestamp=timestamp):
            return "invalid request signature", 401, {"Content-Type": "text/plain"}

        interaction_type = request.get_json()["type"]

        if interaction_type == 1:
            return jsonify({"type": 1})
        if interaction_type == 2:
            data = request.get_json()["data"]
            for command in COMMANDS:
                if command.name == data["name"]:
                    return command.execute(data)
            return jsonify({
                "type": 4,
                "data": {"content": "Unknown command."},
            })

        return "Unrecognized interaction type", 400, {"Content-Type": "text/plain"}

    return "Hello world!"
