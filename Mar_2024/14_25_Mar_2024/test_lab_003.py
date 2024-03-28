import pytest,requests,allure

@allure.title("Geting single booking")
@allure.description("Get single book details")
def test_single_book():
    url_base="https://restful-booker.herokuapp.com"
    url_path="/booking/1"
    URl=url_base+url_path
    response=requests.get(url=URl)
    status=response.status_code
    assert status ==200
    jsonbody=response.json()
    print(jsonbody)
