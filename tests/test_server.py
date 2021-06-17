import unittest
from dateutil.relativedelta import relativedelta
from datetime import datetime
from server import app
from server.user import init_db, db

class TestAppService(unittest.TestCase):
    """ App Server Tests """

    @classmethod
    def setUpClass(cls):
        """ Run once before all tests """
        app.debug = True
        app.testing = True
        # Set up the test database
        app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite://'
        init_db(app)

    @classmethod
    def tearDownClass(cls):
        """ Run once after all tests """
        db.session.close()

    def setUp(self):
        """ Runs before each test """
        db.drop_all()  # clean up the last tests
        db.create_all()  # create new tables
        self.app = app.test_client()
        self.username = 'test'

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def _create_user(self, username, dob):
        data = {"dateOfBirth": dob}
        resp = self.app.put(f"/hello/{username}", json=data)
        # Response code for put should be 204
        self.assertEqual(resp.status_code, 204)
        return resp

    def test_index(self):
        """ Test the Home Page """
        resp = self.app.get("/")
        self.assertEqual(resp.status_code, 200)
        data = resp.get_data(as_text=True)
        self.assertEqual(data, "Hello, World!")

    def test_set_birthdate(self):
        resp = self._create_user(self.username, '2020-05-01')
        data = resp.get_data(as_text=True)
        # Empty response body
        self.assertEqual(data, "")
        return resp

    def test_future_date_not_allowed(self):
        future_date = datetime.now() + relativedelta(years=1)
        dob = future_date.strftime('%Y-%m-%d')
        data = {"dateOfBirth": dob}
        resp = self.app.put("/hello/{self.username}",json=data)
        self.assertEqual(resp.status_code, 400)

    def test_get_birthday_of_non_existent_user(self):
        resp = self.app.get(f"/hello/{self.username}")
        # Get method shouldn't be allowed
        self.assertEqual(resp.status_code, 404)
        data = resp.get_json(force=True)
        self.assertEqual(data['message'], "Mr. Holmes has been notified of missing user")

    def test_get_birthday_of_user(self):
        now = datetime.now()
        dob = f"2020-{now.month}-{now.day+2}"
        resp = self._create_user(self.username, dob)
        resp = self.app.get(f"/hello/{self.username}")
        self.assertEqual(resp.status_code, 200)
        data = resp.get_json(force=True)
        self.assertEqual(
            data['message'],
            f"Hello, {self.username}! Your birthday is in 2 day(s)"
        )

    def test_get_birthday_msg(self):
        now = datetime.now()
        dob = f"2020-{now.month}-{now.day}"
        resp = self._create_user(self.username, dob)
        resp = self.app.get(f"/hello/{self.username}")
        self.assertEqual(resp.status_code, 200)
        data = resp.get_json(force=True)
        self.assertEqual(
            data['message'],
            f"Hello, {self.username}! Happy birthday!"
        )

    def test_update_dob(self):
        # Create a user
        now = datetime.now()
        dob = f"2020-{now.month}-{now.day+2}"
        resp = self._create_user(self.username, dob)
        resp = self.app.get(f"/hello/{self.username}")
        self.assertEqual(resp.status_code, 200)
        data = resp.get_json(force=True)
        self.assertEqual(
            data['message'],
            f"Hello, {self.username}! Your birthday is in 2 day(s)"
        )
        # Update the entry
        dob = f"2020-{now.month}-{now.day+4}"
        self._create_user(self.username, dob)
        resp = self.app.get(f"/hello/{self.username}")
        self.assertEqual(resp.status_code, 200)
        data = resp.get_json(force=True)
        self.assertEqual(
            data['message'],
            f"Hello, {self.username}! Your birthday is in 4 day(s)"
        )

if __name__ == "__main__":
    unittest.main()
