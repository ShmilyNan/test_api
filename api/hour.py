import jsonpath
import pprint
#增加课时url调用的参数social/services/rest/course/V2/User/Period
from test_api.core.rest_client import RestClient

data_add = {"PeriodArgu":{"dataOper":"append","message":"","period":100,"userIds":[13308]}}

period = data_add["PeriodArgu"]["period"]

# print(period)
# 减少课时/course/V2/User/Period
data_reduce = {
  "PeriodArgu": {
    "dataOper": "reduce",
    "message": "-5",
    "period": 5,
    "userIds": [
      13308
    ]
  }
}
preiod_reduce = jsonpath.jsonpath(data_reduce,"$.PeriodArgu.period")
#获取操作记录的user_idsocial/services/rest/course/V2/Class/PeriodRecord/user_id
user_id = 13285
import pytest

userids = 13285, 13286


class APIs(RestClient):

    def login_student(self):
        self.session.headers.update(self.header)
        response = self.put("/center/services/rest/user/Login/{}/{}?server={}".format(self.dict["username"], self.dict["password"], self.dict["servername"]))
        return response

    def add_hour(self, data):
        #增加课时
        response = self.put("/social/services/rest/course/V2/User/Period", json=data)
        return response


    def reduce_hour(self, data):
        #减少课时
        response = self.put("/social/services/rest/course/V2/User/Period", json=data)
        code = response.json()["code"]
        return response

    def get_record(self, user_id):
        #获取用户机构中个人机构课时购、退课、消课记录
        response = self.get("/social/services/rest/course/V2/Class/PeriodRecord/{}".format(user_id))
        # print("获取个人机构课时购、退课、消课记录", response.json())
        return response

    def judge_hour(self, userids):
        #验证用户是否能移除 通过用户在机构内是否有剩余课时数判断
        response = self.put("/social/services/rest/course/V2/CheckPeriod/User/{}".format(userids))
        code = response.json()["code"]
        return response

    def List_organization_hours(self):
        #列出机构的课时列表
        response = self.get("/social/services/rest/course/V2/Inst/PeriodRecord")
        return response


api = APIs()




