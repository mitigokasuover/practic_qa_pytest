import requests

class Test_new_joke():
    """create joke"""

    def __init__(self):
        pass

    # def test_create_new_joke(self):
    #     """create random joke"""
    #     url = "https://api.chucknorris.io/jokes/random"
    #     print(url)
    #     result = requests.get(url)
    #     print("Status cod: " + str(result.status_code))
    #     assert 200 == result.status_code
    #     if result.status_code == 200:
    #         print("Secsessful!!")
    #     else:
    #         print("Error!!!")

    #     result.encoding = "utf-8"
    #     print(result.text)
    #     check = result.json()
        # check_info = check.get("categories")
        # print(check_info)
        # assert check_info == []
        # # print("Categori version")
        # check_info_value = check.get("value")
        # print(check_info_value)
        # name = "Chuck"
        # if name in check_info_value:
        #     print("Chuck here")
        # else:
        #     print("Chuck not here")


    def test_create_new_random_joke(self):
        """create new/random/sport joke"""
        category = "sport"
        url = "https://api.chucknorris.io/jokes/random?category=" + category
        print(url)
        result = requests.get(url)
        print("Status cod: " + str(result.status_code))
        assert 200 == result.status_code
        if result.status_code == 200:
            print("Secsessful!!")
        else:
            print("Error!!!")

        result.encoding = "utf-8"
        print(result.text)
        check = result.json()
        check_info = check.get("category")
        print(check_info)
        assert check_info == ["sport"]
        print("Categori version")
        # check_info_value = check.get("value")
        # print(check_info_value)
        # name = "Chuck"
        # if name in check_info_value:
        #     print("Chuck here")
        # else:
        #     print("Chuck not here")

# random_joke = Test_new_joke()
# random_joke.test_create_new_joke()

sport_joke = Test_new_joke()
sport_joke.test_create_new_random_joke()