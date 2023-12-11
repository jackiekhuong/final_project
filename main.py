import requests

def get_food_data(food_item):

    url = "https://edamam-food-and-grocery-database.p.rapidapi.com/api/food-database/v2/parser"

    querystring = {"ingr": food_item}
    headers = {
        'x-rapidapi-key': "bfa927fd68msh5051cad3d20bd0fp122eedjsn3a5717582c1e",
        'x-rapidapi-host': "edamam-food-and-grocery-database.p.rapidapi.com"
        }

    try:
        response = requests.get(url, headers=headers, params=querystring)
        response.raise_for_status()
        parsed_data = response.json().get("parsed")
        return parsed_data
    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")
        return None

def extract_protein_content(data):
    if data:
        try:
            protein_content = data[0]['food']['nutrients']['PROCNT']
            return protein_content
        except (KeyError, IndexError) as e:
            print(f"Error: {e}")
    return None

def categorize_protein(protein_content):
    if protein_content >= 15:
        return "Great Choice, you will be satisfied for a while!", "great_choice_image.jpg"
    elif protein_content >= 5:
        return "An alright snack, consider adding a handful of nuts or having some Greek yogurt to keep you full for longer!", "giphy-1.gif"
    else:
        return "Sounds yummy, but maybe consider adding some lean meats or chickpeas to have a complete meal!", "giphy-1.gif"

def main():
    while True:
        food_item = input("Enter a food item: ")

        if food_item.lower() == "quit":
            break

        food_data = get_food_data(food_item)
        protein_content = extract_protein_content(food_data)

        if protein_content:
            print(f"Protein content of the specified food: {protein_content} grams")
            category, image = categorize_protein(protein_content)
            print(category)
            print(f"Image: {image}")  # You'll use this image path in your HTML/CSS
        else:
            print("Sorry, could not get protein data for the specified food.")

if __name__ == "__main__":
    main()