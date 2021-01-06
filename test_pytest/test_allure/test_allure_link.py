import allure

@allure.link("https://www.baidu.com/",name="链接")
def test_allure_link():
    print("这是一条加了链接的测试")

test_case_link = "https://www.baidu.com/"
@allure.testcase(test_case_link,"登录用例")
def test_allure_testcaselink():
    print("这是一条测试用例的链接")

# --allure-link-pattern=issue:https://ceshiren.com/t/topic/8734/{}
@allure.link("https://www.baidu.com/",name="链接")
@allure.testcase(test_case_link,"登录用例")
@allure.issue("3","缺陷地址")
def test_issue_link():
    pass

@allure.severity(allure.severity_level.CRITICAL)
def test_allure_severity():
    pass