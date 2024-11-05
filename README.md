## L7 Project

# Chocolate House Seasonal Flavor Management

This is a Flask application that manages seasonal flavor offerings, ingredients, and customer suggestions for a fictional chocolate house. The application allows users to add and delete flavors, ingredients, and suggestions, as well as view all records. The application uses Flask, SQLite, Docker, and HTML for the front end.

## Requirements

- **Packages Used**:
  - Flask
  - SQLite
  - Docker
  - HTML

## Getting Started

### Prerequisites

- Docker installed on your system.
- Basic knowledge of using Docker, Flask, and SQLite.

### Clone the Repository

```bash
git clone https://github.com/Avikumar2003/L7-project.git
cd chocolate-house
```

### Setup and Installation
1) Create the Database Schema:
The application automatically creates chocolate_house.db with the required tables (flavors, ingredients, suggestions) on the first run if they do not exist.

2) Build the Docker Image:

```bash
docker build -t chocolate_house_app .
```

3) Run the Docker Container:

```bash
docker run -d -p 5000:5000 chocolate_house_app
```

4) Access the Application:
Open your web browser and go to http://localhost:5000.

### Application Usage
## Features
- Home Page: Displays the main page of the application (index.html).
- Add Flavor: Adds a new seasonal flavor.
- Delete Flavor: Deletes an existing flavor by flavor_name and id.
- Add Ingredient: Adds a new ingredient with quantity details.
- Delete Ingredient: Deletes an existing ingredient by ingredient_name.
- Add Suggestion: Adds a customer suggestion with optional allergy concerns.
- Delete Suggestion: Deletes an existing suggestion by suggestion_id.
- View Records: Displays all records in flavors, ingredients, and suggestions.
- View All: Special view page (view_all.html) to display all records in detail.

### API Endpoints
- GET /: Home page of the application.
- POST /add_flavor: Adds a new flavor with flavor_name and description.
- POST /delete_flavor: Deletes a flavor by flavor_name and id.
- POST /add_ingredient: Adds a new ingredient with ingredient_name and quantity.
- POST /delete_ingredient: Deletes an ingredient by ingredient_name.
- POST /add_suggestion: Adds a customer suggestion with customer_name, suggestion, and optional allergy_concern.
- POST /delete_suggestion: Deletes a suggestion by suggestion_id.
- GET /view_records: View all records from flavors, ingredients, and suggestions.
- GET /view_all: Display all records in detail in view_all.html.

## Testing Steps
1) Add a Flavor: Go to the form in the home page to add a new seasonal flavor, providing flavor_name and description. Confirm that the success message appears.
2) Delete a Flavor: Use the delete form or API call to remove a flavor by providing its flavor_name and id.
3) Add an Ingredient: Add a new ingredient with ingredient_name and quantity, then confirm that it displays in the records view.
4) Delete an Ingredient: Delete an ingredient by its ingredient_name and verify that it no longer appears in the records.
5) Add a Suggestion: Enter a new customer suggestion and confirm it appears in the suggestions list.
6) Delete a Suggestion: Remove a suggestion by suggestion_id and confirm the deletion.
7) View All Records: Check the view_all page to see all records in detail.

PS:
I have created the delete routes for flavors, written code for others but have not integrated with frontend. Please go through the code to find Create, Read and Delete functionality for all routes.
