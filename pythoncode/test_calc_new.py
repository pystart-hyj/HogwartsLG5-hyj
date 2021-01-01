import pytest
import yaml

class TestCalc:

    # 测试add函数
    @pytest.mark.run(order=1)
    def test_add(self,get_calc,get_datas_add):
        result = None
        try:
            # 调用add函数,返回的结果保存在result里面
            result = get_calc.add(get_datas_add[0],get_datas_add[1])
            # 判断result结果是否等于期望的值
            if isinstance(result,float):
                result = round(result,2)
        except Exception as e:
            print(e)
        assert result == get_datas_add[2]

    @pytest.mark.run(order=4)
    def test_div(self,get_calc,get_datas_div):
        result_div = get_calc.div(get_datas_div[0],get_datas_div[1])
        assert result_div == get_datas_div[2]

    @pytest.mark.run(order=2)
    def test_sub(self,get_calc,get_datas_sub):
        result1 = get_calc.sub(get_datas_sub[0],get_datas_sub[1])
        assert result1 == get_datas_sub[2]

    @pytest.mark.run(order=3)
    def test_mul(self,get_calc,get_datas_mul):
        result2 = get_calc.mul(get_datas_mul[0],get_datas_mul[1])
        assert result2 == get_datas_mul[2]

