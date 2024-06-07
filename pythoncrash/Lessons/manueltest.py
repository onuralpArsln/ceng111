test_list=[
    (1, 2, 3),
    (0, 0, 0),
    (-1, 1, 0),
    (2, -2, 0),
    (2, -2, 2)
]


def add(a, b):
    return a + b



for i in test_list:
    try:
        assert add(i[0],i[1])==i[2]
    except:
        raise AssertionError(f" Error for input values {i[0]} , {i[1]}, Expected output {i[2]} ")
  