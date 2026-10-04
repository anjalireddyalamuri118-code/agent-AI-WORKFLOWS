def agent_loop():
    max_iters = 10

    for i in range(max_iters):
        print(f"Iteration {i + 1}")

        # Observe
        observation = input("Enter observation: ")

        # Decide
        if observation == "goal":
            print("Goal achieved!")
            return "success"

        # Act
        print("Taking action...")

    return "failure"


result = agent_loop()
print("Result:", result)