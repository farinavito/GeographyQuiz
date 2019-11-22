
while True:
    Europe = {"Slovenia": "Ljubljana",
             "Hungary": "Budimpesta",
             "Italy": "Rome",
             "Austria": "Vienna",
              "": ""}

    Africa = {"Algeria": "Algiers",
              "Angola": "Luanda",
              "Benin": "Portonovo",
              "Botswana": "Gaborone",
              "": ""}

    Asia = {"Afganistan": "Kabul",
              "Armenia": "Yerevan",
              "Azerbaijan": "Baku",
              "Bahrain": "Manama",
              "": ""}


    def query_cities(level):
        for country, capital_city in level.items():
            end = list(level)
            if country == end[-1]:
                print("You have guessed all the questions!!!")
                break
            question = input("What is the capital city of " + str(country) + "? ")
            correct_form_answer = question.capitalize()
            if correct_form_answer == f"{capital_city}":
                print("Congrats")
                continue
            else:
                print(f"Wrong! The capital city of {country} is {capital_city}.")
            break
        return

    starter = input("Hello user! Please select the continent referring to quiz: [Europe, Asia, Africa] ")
    if starter.capitalize() == "Europe":
        print(query_cities(Europe))
    elif starter.capitalize() == "Africa":
        print(query_cities(Africa))
    elif starter.capitalize() == "Asia":
        print(query_cities(Asia))
    else:
        end = input("Wrong input. Would you like to continue [y/n]? ")
        if end.lower() == "n":
            print("Bye")
            break
        elif end.lower() == "y":
            continue
        else:
            print("You have entered an invalid symbol. You will have to restart the program. Bye.")
    break



