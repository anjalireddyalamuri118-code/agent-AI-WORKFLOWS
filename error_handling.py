def handle_action(action):
    valid_actions = ["start", "stop", "pause"]

    if action not in valid_actions:
        return {
            "status": "error",
            "code": 400,
            "message": "Invalid action"
        }

    return {
        "status": "success",
        "code": 200,
        "message": f"Action '{action}' executed"
    }


print(handle_action("invalid"))