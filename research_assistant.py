def summarize(values):
    if not values or any(type(x) not in (int, float) for x in values):
        raise ValueError("Provide a nonempty list of numbers")
    if any(x < 0 or x > 100 for x in values):
        raise ValueError("Measurements must be between 0 and 100")
    count = len(values)
    average = sum(values) / count
    return {"count": count, "mean": round(average, 2),
            "minimum": min(values), "maximum": max(values)}

sample = [42, 44, 46, 48]
report = summarize(sample)
print("Observations:", report["count"])
print("Mean:", f'{report["mean"]:.2f}')
print("Range:", report["minimum"], "to", report["maximum"])
print("Note: Descriptive summary only; no causal conclusion.")

