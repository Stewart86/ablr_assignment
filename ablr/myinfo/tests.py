from django.test import Client, TestCase


class MyInfoTest(TestCase):
    def test_login(self):
        client = Client()
        resp = client.get("/api/myinfo/login/")
        self.assertEqual(resp.status_code, 302)
        self.assertEqual(
            resp.url,
            "https://test.api.myinfo.gov.sg/com/v3/authorise?client_id=STG2-MYINFO-SELF-TEST&attributes=uinfin,name,sex,race,nationality,dob,email,mobileno,regadd,housingtype,hdbtype,marital,edulevel,ownerprivate,cpfcontributions,cpfbalances,birthcountry,residentialstatus,aliasname,marriedname,passtype,employmentsector,noahistory&purpose=credit%20risk%20assessment&state=demo&redirect_uri=http://localhost:3001/callback",
        )

    def test_login_bad_request_when_not_using_get(self):
        client = Client()
        resp = client.post("/api/myinfo/login/")
        self.assertEqual(resp.status_code, 400)
        resp = client.put("/api/myinfo/login/")
        self.assertEqual(resp.status_code, 400)
        resp = client.delete("/api/myinfo/login/")
        self.assertEqual(resp.status_code, 400)

    def test_retrieve_should_give_bad_request_when_post_without_body(self):
        client = Client()
        resp = client.post("/api/myinfo/retrieve/")
        self.assertEqual(resp.status_code, 400)
        self.assertEqual(resp.content, b"request body is not the accepted structure")
