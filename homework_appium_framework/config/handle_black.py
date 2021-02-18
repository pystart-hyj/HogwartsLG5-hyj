from selenium.webdriver.common.by import By


def handle_black(fun):
    def run(*args, **kwargs):
        black_list = [(By.ID, "iv_close")]
        # instance 是指传入的self，BasePage中的find方法传入两个参数（self, locator），args[0]表示取第一个参数
        instance = args[0]
        try:
            # 如果元素找到，就返回
            return fun(*args, **kwargs)
        except Exception as e:
            # 遍历黑名单
            for black in black_list:
                # 如果发现黑名单中的元素存在
                eles = instance.driver.find_elements(*black)
                # 对黑名单元素进行处理
                if len(eles) > 0:
                    # 通过点击的方式，关闭弹窗
                    eles[0].click()
                    # 再次查找
                    return fun(*args, **kwargs)
            raise e

    return run