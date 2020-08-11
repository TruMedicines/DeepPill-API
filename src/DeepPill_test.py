from . import DeepPill

def test_DeepPill():
    assert DeepPill.apply("Jane") == "hello Jane"
