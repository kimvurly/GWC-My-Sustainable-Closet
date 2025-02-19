from flask import Blueprint, render_template, request

auth = Blueprint('auth', __name__)

@auth.route('/swiping', methods=['GET', 'POST'])
def swiping():
    if request.method == 'POST':
        button = request.form['submitButton']
        if button == "dontLike":
            pass 
            ''' 
            display another photo from the database based on available data, closest to user's preference
            note down the style and put it in a database called "dontLikes" or something similar
            use AI to figure out what photo should be displayed next
            use AI to figure out what styles the person doesnt like by analyzing similar aspects in "dontLikes" database
            '''
        if button == "notSure":
            pass 
            '''
            display another photo from the database based on available data, closest to user's preference
            note down the style and put it in a database called "notSures" or something similar
            use AI to figure out what photo should be displayed next
                - display similar photos of the style but with slightly different attributes, like fusion styles. 
                use this to figure out the user's style completely
            '''
        if button == "like":
            pass
            '''
            display another photo from the database based on available data, closest to user's preference
            note down style and put it in a database called "likes" or something similar
            use the new data to find more outfits and photos that match the user's style
            '''
    return render_template("swiping.html")