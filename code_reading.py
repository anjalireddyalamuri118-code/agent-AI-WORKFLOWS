state = {"steps": 0, "done": False}

while state["steps"] < 2:
    print("Step:", state["steps"] + 1)

    state["steps"] += 1

    if state["steps"] == 2:
        state["done"] = True

print("Agent completed")
print("State:", state)