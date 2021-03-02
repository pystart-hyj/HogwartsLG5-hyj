import requests
from homework_requests.api.base import Base


class Address(Base):

    def get_member(self,userid):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={self.token}&userid={userid}"
        return self.send("get", url)

    def update_member(self, userid ,name):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={self.token}"
        body = {
            "userid": userid,
            "name": name
        }
        return self.send("post", url, json=body)

    def add_member(self, userid, mobile, name, department):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={self.token}"
        body = {
            "userid": userid,
            "name": name,
            "mobile": mobile,
            "department": department
        }
        return self.send("post", url, json=body)

    def delete_member(self, userid):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={self.token}&userid={userid}"
        return self.send("get", url)