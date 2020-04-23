from main import strms2time


def test_strms2time():
    inputstr = "2 ms"
    result = strms2time(inputstr)
    assert result == 2
