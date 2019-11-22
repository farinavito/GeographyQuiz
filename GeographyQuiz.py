
while True:
    Europe = {"Slovenia": "Ljubljana",
             "Hungary": "Budimpesta",
             "Italy": "Rome",
             "Austria": "Vienna",
              }

    Africa = {"Algeria": "Algiers",
              "Angola": "Luanda",
              "Benin": "Portonovo",
              "Botswana": "Gaborone",
              }

    Asia = {"Afganistan": "Kabul",
              "Armenia": "Yerevan",
              "Azerbaijan": "Baku",
              "Bahrain": "Manama",
            }


    def query_cities(level):
        for country, capital_city in level.items():
            question = input("What is the capital city of " + str(country) + "? ")
            end_list = list(level)
            if country == end_list[-1]:
                return f"You have guessed all the questions for this continent!!!"
            correct_form_answer = question.capitalize()
            if correct_form_answer == f"{capital_city}":
                print("Congrats")
                continue
            return f"Wrong! The capital city of {country} is {capital_city}."


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



