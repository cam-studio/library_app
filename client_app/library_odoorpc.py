import odoorpc

class LibraryAPI():
    _MODEL = "library.book"

    def __init__(self, host, port, db, username, password):
        self._api = odoorpc.ODOO(host, port=port)
        self._api.login(db, username, password)
        self._uid = self._api.env.uid
        self._model = self._api.env[self._MODEL]

    def search_read(self, title = None, domain = [], fields = ["id", "name"]):
        domain = [("name", "ilike", title)] if title else []
        return self._model.search_read(domain, fields)
    
    def create(self, title):
        return self._model.create({"name": title})

    def unlink(self, id):
        return self._model.unlink(id)

if __name__ == "__main__":
    host, port, db = "localhost", 8069, "library"
    username, password = "USERNAME", "PASSWORD"
    api = LibraryAPI(host, port, db, username, password)

    # Sample
    print("*** Create ***")
    title = "刷新未來：重新想像AI+HI智能革命下的商業與變革"
    book_id = api.create(title)
    print("New book with ID %d for title %s" % (book_id, title))

    print("*** Search ***")
    books = api.search_read(title)
    for book in books:
        print("%(id)d %(name)s" % book)


    print("*** Delete ***")
    api.unlink(book_id)
    print("Book with ID %s was deleted." % book_id)

    print("*** Search ***")
    books = api.search_read(title)
    for book in books:
        print("%(id)d %(name)s" % book)