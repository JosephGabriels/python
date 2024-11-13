from hello import say_hello

def test_say_hello():
    from io import StringIO
    import sys

    captured_output=StringIO()
    sys.stdout=captured_output

    say_hello("Test")

    sys.stdout=sys.__stdout__
    assert captured_output.getvalue().strip() == "Hello, Test!"

