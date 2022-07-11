from unittest import TestCase
from server import app
from model import connect_to_db, db, example_data
from flask import session




class FlaskTestsDatabase(TestCase):
    """Flask tests that use the database."""

    def setUp(self):
        """Stuff to do before every test."""

        # Get the Flask test client
        self.client = app.test_client()
        # Show Flask errors that happen during tests
        app.config['TESTING'] = True

        # Connect to test database
        connect_to_db(app, "postgresql:///testdb")

        # Create tables and add sample data
        db.create_all()
        example_data()

    def tearDown(self):
        """Do at end of every test."""

        db.session.remove()
        db.drop_all()
        db.engine.dispose()

   
    def test_volunteer_login(self):
        """Test volunteer login."""

        result = self.client.post("/login",
                                  data={"vemail": "ana_costa@gmail.com", "vpassword": "test123"},
                                  follow_redirects=True)
        self.assertIn(b"Your Information", result.data)


    def test_institution_login(self):
        """Test volunteer login."""

        result = self.client.post("/login",
                                  data={"iemail": 'drm@gmail.com', "ipassword": "test123"},
                                  follow_redirects=True)
        self.assertIn(b"Create a new event", result.data)




class FlaskTestsLoggedOut(TestCase):
    """Flask tests with user logged in to session."""

    def setUp(self):
        """Stuff to do before every test."""

        app.config['TESTING'] = True
        self.client = app.test_client()

    def test_volunteer_logout(self):
        """Test logout route for volunteer."""

        with self.client as v:
            with v.session_transaction() as sess:
                sess['volunteer_id'] = '1'

            result = self.client.get('/logout', follow_redirects=True)

            self.assertNotIn(b'user_id', session)
            self.assertIn(b'Logged Out', result.data)

    def test_institution_logout(self):
        """Test logout route for institution."""

        with self.client as v:
            with v.session_transaction() as sess:
                sess['volunteer_id'] = '1'

            result = self.client.get('/logout', follow_redirects=True)

            self.assertNotIn(b'user_id', session)
            self.assertIn(b'Logged Out', result.data)



if __name__ == "__main__":
    import unittest

    unittest.main()