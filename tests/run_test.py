
from run import division, informations

def test_division():
    func_division = division(6)
    
    assert isinstance(func_division, float)
    assert func_division == 3

def test_informations():
    dict_example = informations()
    
    assert isinstance(dict_example, dict)
    assert "name" in dict_example
    assert "height" not in dict_example
    assert "Gabriel" in dict_example["name"]
    assert dict_example["is_ok"]
