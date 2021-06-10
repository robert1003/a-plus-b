
for i in range(1, 3):
    a, b = list(map(int, open(f'samples/sample{i}.in', 'r').read().split()))
    c = int(open(f'samples/sample{i}.out', 'r').read())
    assert a + b == c

for i in range(1, 24):
    a, b = list(map(int, open(f'testcases/{i}.in', 'r').read().split()))
    c = int(open(f'testcases/{i}.out', 'r').read())
    assert a + b == c
