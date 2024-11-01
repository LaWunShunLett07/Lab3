import Lab2.bmi as bmi

def test_bmi_normal_weight():
    result=bmi.calculate_bmi(weight=57,height=1.73)
    test_result=0
    assert(result==test_result)

def test_bmi_over_weight():
    result=bmi.calculate_bmi(weight=90,height=1.73)
    test_result=1
    assert(result==test_result)

def test_bmi_under_weight():
    result=bmi.calculate_bmi(weight=17,height=50)
    test_result=-1
    assert(result==test_result)