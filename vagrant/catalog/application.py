from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Ingredient, RecipeItem

app = Flask(__name__)

engine = create_engine('sqlite:///ingredientrecipe.db')
inspector = inspect(engine)
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/ingredients/<int:ingredient_id>/recipe/JSON')
def ingredientRecipeJSON(ingredient_id):
    ingredient = session.query(Ingredient).filter_by(id=ingredient_id).one()
    items = session.query(RecipeItem).filter_by(ingredient_id=ingredient_id).all()
    return jsonify(RecipeItem=[i.serialize for i in items])

@app.route('/ingredients/<int:ingredient_id>/recipe/<int:recipe_id>/JSON/')
def recipeItemJSON(ingredient_id, recipe_id):
    Recipe_Item = session.query(RecipeItem).filter_by(id=recipe_id).one()
    return jsonify(Recipe_Item=Recipe_Item.serialize)

@app.route('/ingredient/JSON')
def ingredientsJSON():
    ingredients = session.query(Ingredient).all()
    return jsonify(ingredients=[i.serialize for i in ingredients])

# Show all ingredients
@app.route('/')
@app.route('/ingredients/')
def showIngredients():
    ingredients = session.query(Ingredient).all()
    return render_template('ingredients.html', ingredients=ingredients)

@app.route('/ingredient/new', methods=['GET', 'POST'])
def newIngredient():
    if request.method == 'POST':
        newIngredient = Ingredient(name = request.form['name'])
        session.add(newIngredient)
        session.commit()
        flash("new ingredient item created!")
        return redirect(url_for('showIngredients'))
    else:
        return render_template('newIngredient.html')

@app.route('/ingredient/<int:ingredient_id>/edit', methods=['GET', 'POST'])
def editIngredient(ingredient_id):
    editedIngredient = session.query(Ingredient).filter_by(id=ingredient_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editedIngredient.name = request.form['name']
            return redirect(url_for('showIngredients'))
    else:
        return render_template(
        'editIngredient.html', ingredient=editedIngredient)

@app.route('/ingredient/<int:ingredient_id>/delete', methods=['GET', 'POST'])
def deleteIngredient(ingredient_id):
    ingredientToDelete = session.query(Ingredient).filter_by(id=ingredient_id).one()
    if request.method == 'POST':
        session.delete(ingredientToDelete)
        session.commit()
        return redirect(url_for('showIngredients', ingredient_id=ingredient_id))
    else:
        return render_template(
            'deleteIngredient.html', ingredient=ingredientToDelete)

@app.route('/ingredients/<int:ingredient_id>/')
@app.route('/ingredients/<int:ingredient_id>/recipe')
def ingredientRecipe(ingredient_id):
    ingredient = session.query(Ingredient).filter_by(id=ingredient_id).one()
    print ingredient
    items = session.query(RecipeItem).filter_by(ingredient_id=ingredient_id)
    return render_template('recipe.html', ingredient=ingredient, items=items,
    ingredient_id=ingredient_id)

@app.route('/ingredients/<int:ingredient_id>/recipe/new', methods=['GET', 'POST'])
def newRecipeItem(ingredient_id):
    if request.method == 'POST':
        newItem = RecipeItem(name = request.form['name'], method=request.form[
                           'method'], time_needed=request.form['time_needed'],
                           ingredient_id=ingredient_id)
        session.add(newItem)
        session.commit()
        flash("new recipe item created!")
        return redirect(url_for('ingredientRecipe', ingredient_id=ingredient_id))
    else:
        return render_template('newrecipeitem.html', ingredient_id=ingredient_id)

@app.route('/ingredients/<int:ingredient_id>/recipe/<int:recipe_id>/edit',
            methods=['GET', 'POST'])
def editRecipeItem(ingredient_id, recipe_id):
    editedItem = session.query(RecipeItem).filter_by(id=recipe_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editedItem.name = request.form['name']
        if request.form['method']:
            editedItem.method = request.form['method']
        if request.form['time_needed']:
            editedItem.time_needed = request.form['time_needed']

        session.add(editedItem)
        flash("Recipe Item has been edited")
        session.commit()
        return redirect(url_for('ingredientRecipe', ingredient_id=ingredient_id))
    else:
        return render_template(
            'editrecipeitem.html', ingredient_id=ingredient_id, recipe_id=recipe_id,
            item=editedItem)

@app.route('/ingredients/<int:ingredient_id>/recipe/<int:recipe_id>/delete', methods=['GET', 'POST'])
def deleteRecipeItem(ingredient_id, recipe_id):
    itemToDelete = session.query(RecipeItem).filter_by(id=recipe_id).one()
    if request.method == 'POST':
        session.delete(itemToDelete)
        session.commit()
        flash("Recipe Item has been deleted")
        return redirect(url_for('ingredientRecipe', ingredient_id=ingredient_id))
    else:
        return render_template('deleterecipe.html', item=itemToDelete)

if __name__ == '__main__':
    app.secret_key = 'Clarke'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
