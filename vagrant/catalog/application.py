from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Ingredients, RecipeItem

app = Flask(__name__)

engine = create_engine('sqlite:///ingredientsrecipe.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/')
@app.route('/ingredients/<int:ingredients_id>/')
def ingredientsRecipe(ingredients_id):
    ingredients = session.query(Ingredients).filter_by(id=ingredients_id).one()
    items = session.query(RecipeItem).filter_by(ingredients_id=ingredients.id)
    return render_template('recipe.html', ingredients=ingredients, items=items)

@app.route('/ingredients/<int:ingredients_id>/new/', methods=['GET', 'POST'])
def newRecipeItem(ingredients_id):
    if request.method == 'POST':
        newItem = RecipeItem(name = request.form['name'],ingredients_id = ingredients_id)
        session.add(newItem)
        session.commit()
        return redirect(url_for('ingredientsRecipe', ingredients_id = ingredients_id))
    else:
        return render_template('newrecipeitem.html', ingredients_id = ingredients_id)

@app.route('/ingredients/<int:ingredients_id>/<int:recipe_id>/edit/')
def editRecipeItem(ingredients_id, recipe_id):
    return "page to edit a recipe item"

@app.route('/ingredients/<int:ingredients_id>/<int:recipe_id>/delete/')
def deleteRecipeItem(ingredients_id, recipe_id):
    return "page to delete a recipe"

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
