# my_bookclub_app/bookclub/book_club.py
from flask import Flask, render_template, request

class BookClub:
    def __init__(self, name, description):
        self.name = name
        self.description = description

app = Flask(__name__)

@app.route("/create_book_club", methods=["POST"])
def create_book_club():
  name = request.form["name"]
  description = request.form["description"]

  # Create a new book club object in the database

  # Render the create club page again with a success message
  return render_template("create_book_club.html", success_message="Book club created successfully!")


@app.route("/get_create_book_club")
def get_create_book_club():
  return render_template("create_book_club.html")

