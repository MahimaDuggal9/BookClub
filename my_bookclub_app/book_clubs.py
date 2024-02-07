from book_club import BookClub
class BookClubs:
    def __init__(self):
        self.book_clubs = []

    def add(self, book_club):
        self.book_clubs.append(book_club)

    def get_all(self):
        return self.book_clubs

    def get(self, book_club_id):
        for book_club in self.book_clubs:
            if book_club.id == book_club_id:
                return book_club

        return None

    def update(self, book_club):
        for book_club in self.book_clubs:
            if book_club.id == book_club.id:
                book_club.name = book_club.name
                book_club.description = book_club.description

                return

    def sort_by_name(self):
        self.book_clubs.sort(key=lambda book_club: book_club.name)

    def get_active_book_clubs(self):
        active_book_clubs = []
        for book_club in self.book_clubs:
            if book_club.status == "active":
                active_book_clubs.append(book_club)

        return active_book_clubs
    
    def create_book_club(self, name, description):
        book_club = BookClub(name, description)
        self.add(book_club)

        return book_club

