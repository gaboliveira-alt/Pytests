from tests import run_01

def test_get_discount(mocker):
    mocker.patch("tests.run_01.fetch_discount_rate", return_value=0.50)
    
    response = run_01.get_discount(100)
    assert response == 50