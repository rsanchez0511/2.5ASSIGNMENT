from ac_logic import AC_automation

def test_AC_automation_cool():
    assert AC_automation(28, 24) == "Cool air ON"

def test_AC_automation_heat():
    assert AC_automation(16, 21) == "Heat ON"

def test_AC_automation_stable():
    assert AC_automation(23, 24) == "Air stable"