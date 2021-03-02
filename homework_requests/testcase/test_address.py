import pytest
from homework_requests.api.address import Address


class TestAddress():

    def setup(self):
        self.address = Address()

    @pytest.mark.parametrize("userid, mobile",[("userid001","13910000001"),
                                               ("userid002","13910000002"),
                                               ("userid003","13910000003")])
    def test_add_member(self,userid, mobile):
        name = "新建成员-0303"
        department = [1]
        r = self.address.delete_member(userid)
        r = self.address.add_member(userid=userid,mobile=mobile,name=name,department=department)
        assert r["errcode"] == 0
        r = self.address.get_member(userid)
        assert r["userid"] == userid