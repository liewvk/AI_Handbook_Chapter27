pixels = [[0, 64, 128], [192, 255, 32]]
normalized = [[round(value / 255, 3)
               for value in row] for row in pixels]
print(normalized)

