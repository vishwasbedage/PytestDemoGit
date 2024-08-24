import pytest


class Test002:
    @pytest.mark.group2
    def test_sum_005(self):
        a= 10
        b = 20
        sum = a+b
        print("Sum of a + b",str(sum))
        if sum == 30:
            assert True
        else:
            assert False

    @pytest.mark.group3
    def test_mul_006(self):
        a = 2
        b = 2
        mul = a * b
        print("Mul of a * b =" + str(mul))
        if mul == 5:
            assert True
        else:
            assert False

    @pytest.mark.group2
    def sub_007(self):
        a = 20
        b = 2
        sub = a - b
        print("sub of a - b =" + str(sub))
        if sub == 18:
            assert True
        else:
            assert False

    @pytest.mark.group3
    def test_sub_008(self):
        a = 20
        b = 2
        sub = a - b
        print("sub of a - b =" + str(sub))
        if sub == 18:
            assert True
        else:
            assert False

    @pytest.mark.group2
    def test_sum_009(self):
        a = 15
        b = 25
        sum = a + b
        print("Sum of a+b",str(sum))
        if sum == 40:
            assert True
        else:
            assert False











