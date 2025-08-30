import pytest

from rool.store import Store


def test_init_empty():
    store = Store()
    assert store.size() == 0


def test_init_populated():
    store = Store(a=1)
    assert store.size() == 1
    assert store.get("a") == 1


def test_add():
    store = Store()
    store.add("a", 1)
    assert store.size() == 1
    assert store.get("a") == 1


def test_remove():
    store = Store(a=1, b=2)
    assert store.size() == 2
    store.remove("a")
    assert store.size() == 1


@pytest.mark.xfail(raises=KeyError)
def test_get_xfail():
    store = Store()
    store.get("a")
