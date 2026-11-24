from statistics import mean, pstdev
readings = [10, 11, 9, 10, 10, 20]
average = mean(readings)
spread = pstdev(readings)
for value in readings:
    z = (value - average) / spread
    if abs(z) > 2:
        print(f"Review {value}: z={z:.2f}")

