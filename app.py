from flask import Flask, render_template, request, redirect, session
import sqlite3 as sql

app = Flask(__name__)
app.secret_key = 'chocolate_house_secret_key'


# Home page route
@app.route('/')
def home():
    return render_template('index.html')


# Route to add new seasonal flavor
@app.route('/add_flavor', methods=['POST', 'GET'])
def add_flavor():
    if request.method == 'POST':
        try:
            # Get details from frontend form
            flavor_name = request.form['flavor_name']
            description = request.form['description']
            
            # Connecting to DB and executing the required query
            with sql.connect("chocolate_house.db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO flavors (flavor_name, description) VALUES (?, ?)", (flavor_name, description))
                con.commit()
                msg = "Flavor successfully added!"
        except Exception as e:
            con.rollback()
            msg = f"Error in insert operation: {e}"
        finally:
            return render_template("index.html", msg=msg)

# Route to delete a seasonal flavor by flavor_name
@app.route('/delete_flavor', methods=['POST'])
def delete_flavor():
    if request.method == 'POST':
        try:
            flavor_name = request.get_json().get('flavor_name')
            id = request.get_json().get('id')
            
            # Connect to the database and delete the flavor by name
            with sql.connect("chocolate_house.db") as con:
                cur = con.cursor()
                cur.execute("DELETE FROM flavors WHERE flavor_name = ? AND id = ?", (flavor_name,id))
                
                # Check if any rows were affected
                if cur.rowcount == 0:
                    msg = "Flavor not found!"
                else:
                    con.commit()
                    return {"success": "true", "message": "Flavor deleted successfully"}, 200
        except Exception as e:
            con.rollback()
            return {"success": "false", "error": str(e)}, 500


# Route to add new ingredient
@app.route('/add_ingredient', methods=['POST', 'GET'])
def add_ingredient():
    if request.method == 'POST':
        try:
            # Get details from frontend form
            ingredient_name = request.form['ingredient_name']
            quantity = request.form['quantity']
            
            # Connecting to DB and executing the required query
            with sql.connect("chocolate_house.db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO ingredients (ingredient_name, quantity) VALUES (?, ?)", (ingredient_name, quantity))
                con.commit()
                msg = "Ingredient successfully added!"
        except Exception as e:
            con.rollback()
            msg = f"Error in insert operation: {e}"
        finally:
            return render_template("index.html", msg=msg)
        
# Route to delete an ingredient by ingredient_name
@app.route('/delete_ingredient', methods=['POST'])
def delete_ingredient():
    if request.method == 'POST':
        try:
            ingredient_name = request.form['ingredient_name']
            
            # Connect to the database and delete the flavor by name
            with sql.connect("chocolate_house.db") as con:
                cur = con.cursor()
                cur.execute("DELETE FROM ingredients WHERE ingredient_name = ?", (ingredient_name,))
                
                # Check if any rows were affected
                if cur.rowcount == 0:
                    msg = "Ingredient not found!"
                else:
                    con.commit()
                    return {"success": "true", "message": "Ingredient deleted successfully"}, 200
        except Exception as e:
            con.rollback()
            return {"success": "false", "error": str(e)}, 500


# Route to add customer suggestion and allergy concern
@app.route('/add_suggestion', methods=['POST', 'GET'])
def add_suggestion():
    if request.method == 'POST':
        try:
            # Get details from frontend form
            customer_name = request.form['customer_name']
            suggestion = request.form['suggestion']
            allergy_concern = request.form.get('allergy_concern', 'No')
            
            # Connecting to DB and executing the required query
            with sql.connect("chocolate_house.db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO suggestions (customer_name, suggestion, allergy_concern) VALUES (?, ?, ?)", 
                            (customer_name, suggestion, allergy_concern))
                con.commit()
                msg = "Suggestion successfully added!"
        except Exception as e:
            con.rollback()
            msg = f"Error in insert operation: {e}"
        finally:
            return render_template("index.html", msg=msg)
        
# Route to delete a suggestion by its id
@app.route('/delete_suggestion', methods=['POST'])
def delete_suggestion():
    if request.method == 'POST':
        try:
            sug_id = request.form['suggestion_id']
            
            # Connect to the database and delete the flavor by name
            with sql.connect("chocolate_house.db") as con:
                cur = con.cursor()
                cur.execute("DELETE FROM suggestions WHERE id = ?", (sug_id,))
                
                # Check if any rows were affected
                if cur.rowcount == 0:
                    msg = "Suggestion not found!"
                else:
                    con.commit()
                    msg = "Suggestion successfully deleted!"
        except Exception as e:
            con.rollback()
            msg = f"Error in delete operation: {e}"
        finally:
            return render_template("index.html", msg=msg)


# Route to view all records (flavors, ingredients, suggestions)
@app.route('/view_records')
def view_records():
    try:
        # Connecting to DB and executing the required queries
        con = sql.connect("chocolate_house.db")
        con.row_factory = sql.Row
        cur = con.cursor()
        
        cur.execute("SELECT * FROM flavors")
        flavors = cur.fetchall()
        
        cur.execute("SELECT * FROM ingredients")
        ingredients = cur.fetchall()
        
        cur.execute("SELECT * FROM suggestions")
        suggestions = cur.fetchall()
        
        return render_template("index.html", flavors=flavors, ingredients=ingredients, suggestions=suggestions)
    except Exception as e:
        return f"Error in fetching records: {e}"


# New route to view all records specifically
@app.route('/view_all')
def view_all():
    try:
        # Connecting to DB and executing the required query
        con = sql.connect("chocolate_house.db")
        con.row_factory = sql.Row
        cur = con.cursor()
        
        cur.execute("SELECT * FROM flavors")
        flavors = cur.fetchall()
        
        cur.execute("SELECT * FROM ingredients")
        ingredients = cur.fetchall()
        
        cur.execute("SELECT * FROM suggestions")
        suggestions = cur.fetchall()
        
        return render_template("view_all.html", flavors=flavors, ingredients=ingredients, suggestions=suggestions)
    except Exception as e:
        return f"Error in fetching records: {e}"
    finally:
        con.close()


if __name__ == '__main__':
    app.run(debug=True)
