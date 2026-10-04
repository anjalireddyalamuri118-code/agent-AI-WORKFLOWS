def agent():
    max_iters = 10

    state = {
        "done": False,
        "steps": 0
    }

    while not state["done"] and state["steps"] < max_iters:
        # Update step count
        state["steps"] += 1

        print("Step:", state["steps"])
        print("State:", state)

        # Act
        print("Agent is working...")

        # Example success condition
        if state["steps"] == 5:
            state["done"] = True

    # Safety limit
    if not state["done"]:
        return "failure"

    return "success"


result = agent()
print("Result:", result)
print("Final State:", {
    "done": True if result == "success" else False,
    "steps": 5 if result == "success" else 10
})