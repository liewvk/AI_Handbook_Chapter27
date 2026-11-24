results = {"Fractions": [1, 1, 0, 1, 0, 1, 0, 1],
           "Algebra": [1, 1, 1, 1, 1]}
for topic, attempts in results.items():
    accuracy = sum(attempts) / len(attempts)
    status = "Review" if accuracy < 0.8 else "Continue"
    print(f"{topic}: {accuracy:.1%} - {status}")

