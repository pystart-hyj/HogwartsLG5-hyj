import allure

def test_attach_txt():
    allure.attach("这是一个文本",attachment_type=allure.attachment_type.TEXT)

def test_attach_html():
   allure.attach("</body>这是一段html body块</body>","html测试块",attachment_type=allure.attachment_type.HTML)

def test_attach_photo():
   allure.attach.file("D:/PycharmProjects/HogwartsLG5/test_pytest/test_allure/测-办公助手.png",name="这是一个图片",
                 attachment_type=allure.attachment_type.PNG)
