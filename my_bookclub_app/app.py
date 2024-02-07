# my_bookclub_app/app.py

from flask import Flask, jsonify, render_template, redirect, session, url_for, request
from book_clubs import BookClubs
from book_club import BookClub

app = Flask(__name__)

clubs = []

wishlist_data = {}
app.secret_key = 'your_secret_key'

users = {
    'user123': {
        'password': 'password123',  # Passwords should be securely hashed in a real app
        'wishlist': [],
    }
}

@app.route('/')
def index():
    if 'user_id' in session:
        user_id = session['user_id']
        return render_template('index.html', user_id=user_id)
    else:
        return redirect(url_for('login'))
    
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_id = request.form.get('user_id')
        password = request.form.get('password')

        if user_id in users and users[user_id]['password'] == password:
            session['user_id'] = user_id
            return redirect(url_for('index'))
        else:
            return 'Login failed. Please check your credentials.'

    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user_id = request.form.get('user_id')
        password = request.form.get('password')

        # if user_id in users:
            
        # else:
            # In a real app, you should securely hash and salt the password.
        users[user_id] = {
                'password': password,
                'wishlist': [],
        }
            
        return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('login'))

@app.route("/get_create_book_club")
def get_create_book_club():
  return render_template("create_book_club.html")

@app.route("/book_clubs")
def book_clubs():
    return render_template("book_clubs.html", book_clubs=clubs)

@app.route('/create_book_club', methods=['POST'])
def create_book_club():
    # Extract club data from the form
    name = request.form.get('name')
    description = request.form.get('description')
    owner = request.form.get('owner')
    location = request.form.get('location')

    # Create a new club dictionary
    new_club = {
        'name': name,
        'description': description,
        'owner': owner,
        'location': location
    }

    # Append the new club to the list
    clubs.append(new_club)

    # Return the new club data as JSON
    return jsonify(new_club)

@app.route('/get_club_list')
def get_club_list():
    # Return the list of clubs as JSON
    return jsonify({'clubs': clubs})

@app.route("/wishlist")
def wishlist():
    if 'user_id' in session:
        user_id = session['user_id']
        return render_template('wishlist.html', user_id=user_id)
    else:
        return redirect(url_for('login'))


@app.route('/add_to_wishlist', methods=['POST'])
def add_to_wishlist():
    book_id = request.form.get('book_id')
    user_id = session['user_id']

    # Add book to user's wishlist
    if user_id not in wishlist_data:
        wishlist_data[user_id] = []
    wishlist_data[user_id].append(book_id)

    return jsonify({'message': 'Book added to wishlist'})

@app.route('/get_wishlist')
def get_wishlist():
    user_id = session['user_id']
    wishlist = wishlist_data.get(user_id, [])
    return jsonify({'wishlist': wishlist})



if __name__ == "__main__":
    app.run(debug=True)
