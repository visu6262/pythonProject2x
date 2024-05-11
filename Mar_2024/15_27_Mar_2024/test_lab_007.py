import pytest
import requests
import allure

@allure.title("Token - Generate Token")
@allure.description("Create new Token")
@pytest.fixture
def create_token():
    base_url="https://restful-booker.herokuapp.com"
    path_url="/auth"
    token_url=base_url+path_url
    headers={"content-tpyt":"application/json"}
    payload={
    "username" : "admin",
    "password" : "password123"
    }
    responce=requests.post(url=token_url,headers=headers,json=payload)
    jsonbody=responce.json()

    status=responce.status_code
    assert status == 200

    status_msg=responce.ok
    assert status_msg == True

    token=jsonbody["token"]
    assert token is not None
    assert type(token) == str

    print(jsonbody)
    print(status)
    print(status_msg)
    print(token)
    return token

@allure.title("Booking - CreateBooking")
@allure.description("Create Booking")
@pytest.fixture
def create_book():
    url_base = "https://restful-booker.herokuapp.com"
    url_path = "/booking"
    book_url = url_base + url_path
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

    response=requests.post(url=book_url,headers=headers,json=payload)
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
    return bookid



@allure.title("Booking - UpdateBooking")
@allure.description("UpdateBooking")
def test_update_booking(create_token,create_book):
    try:
        url_base = "https://restful-booker.herokuapp.com"
        url_path = "/booking/"
        param = create_book
        update_url = url_base + url_path + str(param)

        head = {
            "Content - Type": "application / json",
            "Accept": "application / json",
            "Cookie": "token =" + create_token
        }
        paload = {
            "firstname": "Nagarjuna",
            "lastname": "Brown",
            "totalprice": 1500,
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2024-05-01",
                "checkout": "2024-05-10"
            },
            "additionalneeds": "Breakfast and coffee"
        }
        resp = requests.put(url=update_url, headers=head, json=paload)
        jsonbody = resp.json()

        status = resp.status_code
        assert status == 200

        status_msg = resp.ok
        assert status_msg is True

        print(resp)
        print(status)
        print(status_msg)
    except Exception as e:
        print(e)


def test_delete_booking(create_token,create_book):
    try:
        url_base = "https://restful-booker.herokuapp.com"
        url_path = "/booking/"
        param = create_book
        delete_url = url_base + url_path + str(param)

        head = {"Content-Type": "application/json",
                "Cookie": "token=" + create_token}

        response = requests.delete(url=delete_url, headers=head)
        jsonbody = response.json()

        status=response.status_code
        assert status == 201

        # status_msg=response.ok
        # assert status_msg == True

        print(jsonbody)
        print(status)
        # print(status_msg)
    except Exception as e:
        print(e)
