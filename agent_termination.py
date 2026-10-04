def agent():
    max_iters = 10

    state = {
        "done": False,
        "steps": 0
    }

    while not state["done"] and state["steps"] < max_iters:
        state["steps"] += 1

        print(f"Step: {state['steps']}")

        # Agent action
        print("Agent is working...")

        # Success condition
        if state["steps"] == 5:
            state["done"] = True
            return "success"

    # Failure if safety limit is reached
    if state["steps"] >= max_iters:
        return "failure"


result = agent()
print("Result:", result)