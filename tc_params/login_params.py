import pytest

def second_tc_login_params():
    params_list = [
        ("user_test@test.com", "Formulaq1w2e3!"),
        pytest.param("random_username", "admin123",
                     marks=pytest.mark.xfail(reason="Non-existing username entered")),
        pytest.param(" ", " ",
                     marks=pytest.mark.xfail(reason="Empty credentials")),
        pytest.param("111@", "qwertyADMIN",
                     marks=pytest.mark.xfail(reason="Wrong credentials")),
        pytest.param(" ", "admin123",
                     marks=pytest.mark.xfail(reason="Empty username")),
        pytest.param("Admin", " ",
                     marks=pytest.mark.xfail(reason="Empty password"))
    ]

    return params_list
