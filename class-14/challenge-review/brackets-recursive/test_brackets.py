from brackets import check_brackets

def test_check_brackets_exists():
    assert check_brackets

def test_one_open_curly():
    assert check_brackets('{') == False

def test_one_close_curly():
    assert check_brackets('}') == False

def test_two_parens():
    assert check_brackets('()') == True

def test_two_parens_reversed():
    assert check_brackets(')(') == False

def test_nested():
    assert check_brackets('([[]])')

def test_mulitples():
    assert check_brackets('()[]{}')

def test_nested_imbalanced():
    assert check_brackets('([[]])]') == False

def test_with_extras():
    assert check_brackets('[ for x in exes if y() ]')

def test_unmatched():
    assert check_brackets('[}') == False