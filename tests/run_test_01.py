from tests import run_01

def test_get_discount(mocker):
    mocker.patch("tests.run_01.fetch_discount_rate", return_value=0.50)
    
    response = run_01.get_discount(100)
    assert response == 50

def test_get_discount_with_spy_integration(mocker):
    spy = mocker.spy(run_01, "fetch_discount_rate")
    response = run_01.get_discount(100)
    
    assert response == 91.0
    spy.assert_called_once()
    spy.assert_called_with(0.9)

def fake_discount_rate(initial_value: float):
    return 0.40

def test_get_discount_with_spy_and_custom_return(mocker):
    spy = mocker.patch("tests.run_01.fetch_discount_rate", side_effect=fake_discount_rate)
    
    result = run_01.get_discount(100)
    
    assert result == 60.0
    spy.assert_called_once()
    spy.assert_called_with(0.9)
