#!/usr/bin/python3
for i in range(100):
    if i % 10 != (i // 10) % 10 and i < 99:
        print(f"{i}, ", end='')
    else:
        print(i, end=' ')
