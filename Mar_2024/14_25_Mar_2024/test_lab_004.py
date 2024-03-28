import pytest,requests,allure

@allure.title("Booking - CreateBooking")
@allure.description("Create Booking")
def test_create_book():
    url_base = "https://restful-booker.herokuapp.com"
    url_path = "/booking"
    URl = url_base + url_path
    headers = {"Content-Type": "application/json"}
    payload = {
        "firstname": "visu_visu",
        "lastname": "RRR",
        "totalprice": 999,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-04-22",
            "checkout": "2024-04-25"
        },
        "additionalneeds": "Breakfast"
    }

    response=requests.post(url=URl,headers=headers,json=payload)
    status_code=response.status_code
    assert status_code == 200
    status_msg=response.ok
    assert status_msg == True
    jsonbody=response.json()
    bookid=jsonbody["bookingid"]
    assert bookid is not None
    assert bookid > 0
    assert type(bookid) == int
    first_name=jsonbody["booking"]["firstname"]
    last_name=jsonbody["booking"]["lastname"]
    price=jsonbody["booking"]["totalprice"]
    deposit_paid=jsonbody["booking"]["depositpaid"]
    check_in=jsonbody["booking"]["bookingdates"]["checkin"]
    assert type(first_name)==str
    assert first_name == "visu_visu"
    assert type(last_name)==str
    assert last_name =="RRR"
    assert type(price)==int
    assert type(deposit_paid)==bool
    assert check_in== "2024-04-22"
    print(bookid)
    print(jsonbody)
    print(status_code)
    print(status_msg)
    print(first_name)
    print(bookid)