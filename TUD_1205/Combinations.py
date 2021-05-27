values = [24, 50, 51, 56, 57, 58, 64, 83, 90, 91]

import time
st=time.time()
for a in range(1, 50):
    for b in range(1, 50):
        for c in range(1, 50):
            for d in range(1, 50):
                for e in range(1, 50):
                    comb = [(a + b), (a + c), (a + d), (a + e), (b + c), (b + d), (b + e), (c + d), (c + e), (d + e)]
                    comb.sort()
                    if comb == values:
                        break
                if comb == values:
                    break
            if comb == values:
                break
        if comb == values:
            break
    if comb == values:
        print(f"it took {st-time.time()}  seconds")
        break


print(a, b, c, d, e)
