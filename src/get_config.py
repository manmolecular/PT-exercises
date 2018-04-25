import json

_json_config = None

def get_config():
    global _json_config
    if not _json_config:
        with open('config.json','r') as f:
            _json_config = json.load(f)
    return _json_config