
while True:
    Europe = {"Slovenia": "Ljubljana",
             "Hungary": "Budapest",
             "Italy": "Rome",
             "Austria": "Vienna",
             "Germany": "Berlin",
              }

    Africa = {"Algeria": "Algiers",
              "Angola": "Luanda",
              "Benin": "Portonovo",
              "Botswana": "Gaborone",
              "Egipt": "Kairo"
              }

    Asia = {"Afganistan": "Kabul",
              "Armenia": "Yerevan",
              "Azerbaijan": "Baku",
              "Bahrain": "Manama",
                "Japan": "Tokyo"
            }


    def query_cities(level):
        for country, capital_city in level.items():
            question = input("What is the capital city of " + str(country) + "? ")
            end_list = list(level)
            if country == end_list[-1]:
                return f"You have guessed all the questions for this continent!!!"
            correct_form_answer = question.capitalize()
            if correct_form_answer == f"{capital_city}":
                # print("Congrats")
                if country == end_list[0]:
                    print(f"That was easy.")
                elif country == end_list[1]:
                    print(f"Not impressed yet.")
                elif country == end_list[2]:
                    print(f"Damn you're good.")
                elif country == end_list[3]:
                    print(f"You're on fire!")
                continue
            return f"Wrong! The capital city of {country} is {capital_city}."


    starter = input("Hello user! Please select the continent referring to quiz: [Europe, Asia, Africa] ")
    if starter.lstrip().capitalize() == "Europe":
        print(query_cities(Europe))
    elif starter.lstrip().capitalize() == "Africa":
        print(query_cities(Africa))
    elif starter.lstrip().capitalize() == "Asia":
        print(query_cities(Asia))
    else:
        end = input("Wrong input. Would you like to continue [y/n]? ")
        if end.lstrip().lower() == "n":
            print("Bye")
            break
        elif end.lstrip().lower() == "y":
            continue
        else:
            print("You have entered an invalid symbol. You will have to restart the program. Bye.")
    break



