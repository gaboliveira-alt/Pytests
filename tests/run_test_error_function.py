import pytest
from run import error_function

def test_error_function():
    try:
        error_function()
    except Exception as exception_raises:
        assert str(exception_raises) == "Meu erro estás aqui"

def test_error_function_with_pytest():
    with pytest.raises(Exception) as error_info:
        error_function()
    assert str(error_info.value) == "Meu erro estás aqui"