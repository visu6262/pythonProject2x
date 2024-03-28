import pytest
import requests

def test_single_request():
    responce=requests.get("https://restful-booker.herokuapp.com/booking/1")
    responce_status=responce.status_code
    assert responce_status==200

def test_status_ok():
    responce=requests.get("https://restful-booker.herokuapp.com/booking/1")
    responce_status=responce.status_code
    responce_msg=responce.ok
    assert responce_msg == True
    print(responce.url)
