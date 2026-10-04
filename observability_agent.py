def process():
    log = []

    log.append("Step 1: Process started")

    log.append("Step 2: Taking input")
    name = "Geeva"

    log.append("Step 3: Processing data")
    result = "Hello " + name

    log.append("Step 4: Process completed")

    return result, log


result, full_log = process()

print("Result:", result)
print("\nFull Log:")
for step in full_log:
    print(step)