from flask import Flask, render_template, request, redirect, url_for, flash
from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Ingredient, RecipeItem

app = Flask(__name__)

engine = create_engine('sqlite:///ingredientrecipe.db')
inspector = inspect(engine)
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/')
@app.route('/ingredient/new', methods=['GET', 'POST'])
def newIngredientItem():
    if request.method == 'POST':
        newItem = IngredientItem(name = request.form['name'])
        session.add(newItem)
        session.commit()
        flash("new ingredient item created!")
        return redirect(url_for('ingredient'))
    else:
        return render_template('newIngredient.html')

@app.route('/ingredients/<int:ingredient_id>/recipe')
def ingredientRecipe(ingredient_id):
    ingredient = session.query(Ingredient).filter_by(id=ingredient_id).one()
    print ingredient
    items = session.query(RecipeItem).filter_by(ingredient_id=ingredient_id)
    return render_template('recipe.html', ingredient=ingredient, items=items,
    ingredient_id=ingredient_id)

@app.route('/ingredients/<int:ingredient_id>/new', methods=['GET', 'POST'])
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

@app.route('/ingredients/<int:ingredient_id>/<int:recipe_id>/edit',
            methods=['GET', 'POST'])
def editRecipeItem(ingredient_id, recipe_id):
    editedItem = session.query(RecipeItem).filter_by(id=recipe_id).one()
    if request.method == 'POST':
        if request.form['name']:
            edtiedItem.name = request.form['name']
        session.add(editedItem)
        flash("Menu Item has been edited")
        session.commit()
        return redirect(url_for('ingredientRecipe', ingredient_id=ingredient_id))
    else:
        return render_template(
            'editrecipeitem.html', ingredient_id=ingredient_id, recipe_id=recipe_id,
            item=editedItem)

@app.route('/ingredients/<int:ingredient_id>/<int:recipe_id>/delete', methods=['GET', 'POST'])
def deleteRecipeItem(ingredient_id, recipe_id):
    itemToDelete = session.query(RecipeItem).filter_by(id=recipe_id).one()
    if request.method == 'POST':
        session.delete(itemToDelete)
        session.commit()
        flash("Menu Item has been deleted")
        return redirect(url_for('ingredientRecipe', ingredient_id=ingredient_id))
    else:
        return render_template('deleteconfirmation.html', item=itemToDelete)

if __name__ == '__main__':
    app.secret_key = 'Clarke'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
