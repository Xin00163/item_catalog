from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Ingredient, Base, RecipeItem

engine = create_engine('sqlite:///ingredientrecipe.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()


# Recipe for beef
ingredient1 = Ingredient(name="Beef")

session.add(ingredient1)
session.commit()


recipeItem1 = RecipeItem(name="Quick Beef Stir Fry", method="Heat vegetable oil in a large wok or skillet over medium-high heat; cook and stir beef until browned, 3 to 4 minutes. Move beef to the side of the wok and add broccoli, bell pepper, carrots, green onion, and garlic to the center of the wok. Cook and stir vegetables for 2 minutes. Stir beef into vegetables and season with soy sauce and sesame seeds. Continue to cook and stir until vegetables are tender, about 2 more minutes.",
                     time_needed="25m", ingredient=ingredient1)

session.add(recipeItem1)
session.commit()

recipeItem2 = RecipeItem(name="Mushroom Slow Cooker Roast Beef", method="Place the mushrooms in the bottom of a slow cooker; set the roast atop the mushrooms; sprinkle the onion soup mix over the beef and pour the beer over everything; season with black pepper. Set slow cooker to LOW; cook 9 to 10 hours until the meat is easily pulled apart with a fork.",
                     time_needed="9h5m", ingredient=ingredient1)

session.add(recipeItem2)
session.commit()

recipeItem3 = RecipeItem(name="Boeuf Bourguignon", method="1. Heat oil in a large, heavy skillet over medium heat. Add onions; cook and stir until tender, about 10 minutes. Transfer to a bowl. 2. Cook and stir beef in the same skillet until browned, 1 to 2 minutes per side. Sprinkle flour, marjoram, thyme, and pepper over beef. Pour red wine and beef broth into the skillet; stir well. Reduce heat to low and simmer until beef is tender, 1 1/2 to 2 hours. 3. Stir onions into the skillet. Add mushrooms. Cook, stirring, until mushrooms are tender and sauce is thick and dark brown, about 30 minutes.", time_needed="2h34m", ingredient=ingredient1)

session.add(recipeItem3)
session.commit()

recipeItem4 = RecipeItem(name="Horsey Beef Pretzel Bites", method="Arrange Pretzel Crisps(R) onto a large tray. Top with roast beef and a piece of mozzarella cheese. Add a slice or 2 of red onion. Put a dollop (about 1/4 teaspoon) of horseradish on the onion. Garnish with chives.",
                     time_needed="50m", ingredient=ingredient1)

session.add(recipeItem4)
session.commit()

recipeItem5 = RecipeItem(name="Salisbury Steak", method="In a large bowl, mix together 1/3 cup condensed French onion soup with ground beef, bread crumbs, egg, salt and black pepper. Shape into 6 oval patties. In a large skillet over medium-high heat, brown both sides of patties. Pour off excess fat. In a small bowl, blend flour and remaining soup until smooth. Mix in ketchup, water, Worcestershire sauce and mustard powder. Pour over meat in skillet. Cover, and cook for 20 minutes, stirring occasionally.", time_needed="40m", ingredient=ingredient1)

session.add(recipeItem5)
session.commit()

recipeItem6 = RecipeItem(name="Meatball Nirvana", method="Preheat an oven to 400 degrees F (200 degrees C). Place the beef into a mixing bowl, and season with salt, onion, garlic salt, Italian seasoning, oregano, red pepper flakes, hot pepper sauce, and Worcestershire sauce; mix well. Add the milk, Parmesan cheese, and bread crumbs. Mix until evenly blended, then form into 1 1/2-inch meatballs, and place onto a baking sheet. Bake in the preheated oven until no longer pink in the center, 20to25 minutes.", time_needed="40m", ingredient=ingredient1)

session.add(recipeItem6)
session.commit()

recipeItem7 = RecipeItem(name="Beef Tips and Noodles", method="Preheat oven to 400 degrees F (200 degrees C). In a 13x9 inch casserole dish, combine the mushroom and beef onion soups, canned mushrooms and water. Mix thoroughly and add beef tips. Turn to coat well. Bake in a preheated oven for 1 hour. While beef tips are baking, bring a large pot of lightly salted water to a boil. Add pasta and cook for 8 to 10 minutes or until al dente; drain. Serve beef tips and sauce over noodles.",
                     time_needed="1h15m", ingredient=ingredient1)

session.add(recipeItem7)
session.commit()

recipeItem8 = RecipeItem(name="Broccoli Beef", method="In a small bowl, combine flour, broth, sugar, and soy sauce. Stir until sugar and flour are dissolved. In a large skillet or wok over high heat, cook and stir beef 2 to 4 minutes, or until browned. Stir in broth mixture, ginger, garlic, and broccoli. Bring to a boil, then reduce heat. Simmer 5 to 10 minutes, or until sauce thickens.",
                     time_needed="30m", ingredient=ingredient1)

session.add(recipeItem8)
session.commit()


# Recipe for pork
ingredient2 = Ingredient(name="Pork")

session.add(ingredient2)
session.commit()


recipeItem1 = RecipeItem(name="Apple Butter Pork Loin", method="Preheat the oven to 350 degrees F (175 degrees C). Season the pork loins with seasoning salt, and place them in a 9x13 inch baking dish or small roasting pan. Pour apple juice over the pork, and cover the dish with a lid or aluminum foil. Bake for 1 hour in the preheated oven. While the pork is roasting, mix together the apple butter, brown sugar, water, cinnamon, and cloves. Remove pork roasts from the oven, and spread with apple butter mixture. Cover, and return to the oven for 2 hours, or until fork-tender.",
            time_needed="3h15m", ingredient=ingredient2)

session.add(recipeItem1)
session.commit()

recipeItem2 = RecipeItem(name="Sweet and Sour Pork", method="Place cubed pork in a medium bowl, and season with 1 teaspoon salt, 1/4 teaspoon sugar, and 1 teaspoon soy sauce. Mix in the egg white and green onions. Cover, and place in the refrigerator at least 1 hour. Heat 1 quart oil to 365 degrees F (185 degrees C) in a large, heavy saucepan or deep fryer. Coat the pork with 1/2 cup cornstarch, and fry in the heated oil about 10 minutes, until evenly browned. Drain on paper towels. Heat 1 tablespoon oil in a wok over medium heat. Stir in the celery, green bell pepper, and onion, and cook until tender. Season with salt and sugar. Remove from heat, and set aside. In a large saucepan, mix 1 cup water, 1/4 teaspoon salt, 3/4 cup sugar, apple cider vinegar, ketchup, and 1/2 teaspoon soy sauce. Bring to a boil, and stir in the cooked pork, celery mixture, and the pineapple chunks with juice. Return to boil, and mix in 2 tablespoons cornstarch and 1/4 cup water to thicken.", time_needed="2h", ingredient=ingredient2)

session.add(recipeItem2)
session.commit()

recipeItem3 = RecipeItem(name="Delicious Ham and Potato Soup", method="Combine the potatoes, celery, onion, ham and water in a stockpot. Bring to a boil, then cook over medium heat until potatoes are tender, about 10 to 15 minutes. Stir in the chicken bouillon, salt and pepper.In a separate saucepan, melt butter over medium-low heat. Whisk in flour with a fork, and cook, stirring constantly until thick, about 1 minute. Slowly stir in milk as not to allow lumps to form until all of the milk has been added. Continue stirring over medium-low heat until thick, 4 to 5 minutes. Stir the milk mixture into the stockpot, and cook soup until heated through. Serve immediately.",
time_needed="45m", ingredient=ingredient2)

session.add(recipeItem3)
session.commit()

recipeItem4 = RecipeItem(name="Amazing Pork Tenderloin in the Slow Cooker", method="Place pork tenderloin in a slow cooker with the contents of the soup packet. Pour water, wine, and soy sauce over the top, turning the pork to coat. Carefully spread garlic over the pork, leaving as much on top of the roast during cooking as possible. Sprinkle with pepper, cover, and cook on low setting for 4 hours. Serve with cooking liquid on the side as au jus.",
                     time_needed="4h15m", ingredient=ingredient2)

session.add(recipeItem4)
session.commit()

recipeItem5 = RecipeItem(name="Best Grilled Pork Chops", method="Mix water, soy sauce, vegetable oil, lemon pepper seasoning, and minced garlic in a deep bowl; add pork chops and marinate in refrigerator at least 2 hours. Preheat an outdoor grill for medium-high heat and lightly oil the grate. Remove pork chops from the marinade and shake off excess. Discard the remaining marinade. Cook the pork chops on the preheated grill until no longer pink in the center, 5 to 6 minutes per side. An instant-read thermometer inserted into the center should read 145 degrees F (63 degrees C).",
                     time_needed="2h15m", ingredient=ingredient2)

session.add(recipeItem5)
session.commit()

recipeItem6 = RecipeItem(name="BBQ Pork for Sandwiches", method="Pour can of beef broth into slow cooker, and add boneless pork ribs. Cook on High heat for 4 hours, or until meat shreds easily. Remove meat, and shred with two forks. It will seem that it's not working right away, but it will. Preheat oven to 350 degrees F (175 degrees C). Transfer the shredded pork to a Dutch oven or iron skillet, and stir in barbeque sauce. Bake in the preheated oven for 30 minutes, or until heated through.", time_needed="4h45m", ingredient=ingredient2)

session.add(recipeItem6)
session.commit()



print "added recipe items!"
