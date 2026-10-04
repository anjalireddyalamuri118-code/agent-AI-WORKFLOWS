for i in range(3):

    # Observe
    observation = input("Observe: ")

    # Decide
    if "hot" in observation.lower():
        action = "Turn ON the fan"
    elif "cold" in observation.lower():
        action = "Turn OFF the fan"
    else:
        action = "Do nothing"

    # Act
    print("Decision:", action)
    print("Action performed!")
    print("--------------------")