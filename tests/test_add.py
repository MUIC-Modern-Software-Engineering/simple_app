import simple_app


def test_sanity():
    assert 1 + 1 == 2


def test_add():
    assert simple_app.add_numbers(1, 2) == 3
