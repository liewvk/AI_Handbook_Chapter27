measurements = [4.1, 4.4, 4.3, 4.8, 5.0, 5.2, 5.4, 5.5]
split = int(0.75 * len(measurements))
train = measurements[:split]
test = measurements[split:]
print("Training:", train)
print("Testing:", test)

