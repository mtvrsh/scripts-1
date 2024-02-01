import countdown

def test_parse_seconds_empty():
    assert countdown.parse_seconds("") == 0

def test_parse_seconds_no_unit():
    assert countdown.parse_seconds("5") == 5

def test_parse_seconds_no_value():
    assert countdown.parse_seconds("s") == 0

def test_parse_seconds_in_seconds():
    assert countdown.parse_seconds("5s") == 5

def test_parse_seconds_in_minutes():
    assert countdown.parse_seconds("5m") == 300

def test_parse_seconds_in_hours():
    assert countdown.parse_seconds("5h") == 18000
