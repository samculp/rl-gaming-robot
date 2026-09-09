from hardware.experiments.controller_input_test.controller_input import get_button_action


def test_get_button_action():
    assert get_button_action(0) == "A"
    assert get_button_action(1) == "B"
    assert get_button_action(2) == "SELECT"
    assert get_button_action(3) == "START"