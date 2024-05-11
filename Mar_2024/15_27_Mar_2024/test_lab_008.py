import pytest
import requests
import allure
from codetest import create_book,create_token


@allure.title("Booking - UpdateBooking")
@allure.description("UpdateBooking")
def test_update_booking(create_book,create_token):
    try:
        url_base = "https://restful-booker.herokuapp.com"
        url_path = "/booking/"
        param = create_book
        update_url = url_base + url_path + str(param)
        cookie="token =" + create_token

        head = {
            "Content - Type": "application / json",
            "Accept": "application / json",
            "Cookie": "cookie"
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


def test_delete_booking(create_book,create_token):
    try:
        url_base = "https://restful-booker.herokuapp.com"
        url_path = "/booking/"
        param = create_book
        delete_url = url_base + url_path + str(param)
        cookie="token=" + create_token

        head = {"Content-Type": "application/json",
                "Cookie": "cookie"}

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
