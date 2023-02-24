import requests

class Test_location():
    """work with new loc"""
    
    def test_create_loc(self):
        """new loc"""

        based_url = "https://rahulshettyacademy.com" #based url
        key = "?key=qaclick123" #herecter
        post_resours = "/maps/api/place/add/json" # resours

        post_url = based_url + post_resours + key
        print(post_url)


        json_create_loc = {
            "location": { 
            "lat": -38.383494, 
            "lng": 33.427362 
            }, "accuracy": 50, 
            "name": "Frontline house", 
            "phone_number": "(+91) 983 893 3937", 
            "address": "29, side layout, cohen 09", 
            "types": [
            "shoe park", 
            "shop"
            ],
            "website": "http://google.com", 
            "language": "French-IN"

        }

        result_post = requests.post(post_url, json= json_create_loc) 
        print(result_post.text)
        print("Status cod: " + str(result_post.status_code))
        assert 200 == result_post.status_code
        if result_post.status_code == 200:
            print("Secsessful!!")
        else:
            print("Error!!!")

        check_post = result_post.json()
        check_info_post = check_post.get("status")
        print("status cod : " + check_info_post)
        assert check_info_post == "OK"
        print("status accept")
        place_id = check_post.get("place_id")
        print("Olace_id :" + place_id)


        """Check new location"""

        get_resource = "/maps/api/place/get/json"
        get_url = based_url + get_resource + key + "&place_id" + place_id
        print(get_url)
        result_get = requests. get(get_url)
        print(result_get.text)
        print("status:" + str(result_get.status_code))
        assert 200 == result_get.status_code
        if result_get.status_code == 200:
            print("Correct!!!")
        else:
            print("Wrong")
        
        """Hange new location"""

        #  https://rahulshettyacademy.com,  /maps/api/place/update/json, key =qaclick123
        put_resource = " /maps/api/place/update/json"
        put_url = based_url + put_resource + key
        print(put_url)
        json_for_update_new_location = { 
            "place_id": place_id,
            "address": "100 Lenina street, RU", 
            "key": "qaclick123" 
        }
        result_put = requests.put(put_url, json = json_for_update_new_location)
        print(result_put.text)
        print("status:" + str(result_put.status_code))
        assert 200 == result_put.status_code
        if result_put.status_code == 200:
            print("Correct swich new location!!!")
        else:
            print("Wrong")
        check_put = result_put.json()
        check_put_info = check_put.get("msg")
        print("Message: " + check_put_info)
        assert check_put_info == "Address successfully updated"
        print("Message no avalible")
        
        """proverca"""

        check_adress = result_get.json()
        check_adress_info = check_adress.get("address")
        print("Message: " + check_put_info)
        assert check_adress_info == "100 Lenina street, RU"
        print("Message valible")

        """delete new location"""

        delete_resourse = "/maps/api/place/delete/json"
        delete_url = based_url + delete_resourse + key
        print(delete_url)
        json_for_delete_new_location = {"place_id":"928b51f64aed18713b0d164d9be8d67f"}
        result_delete = requests.delete(delete_url, json = json_for_delete_new_location)
        print(result_delete.text)




new_place = Test_location()
new_place.test_create_loc()