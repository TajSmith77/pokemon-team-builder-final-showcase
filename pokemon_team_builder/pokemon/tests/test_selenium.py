# Test the functionality of the pokemon application
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class TestPokemonApp(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(options=webdriver.ChromeOptions().add_experimental_option("detach", True))
        self.driver.get("http://127.0.0.1:8000")

    def tearDown(self):
        self.driver.quit()

    def test_pokemon_nav_button(self):
        nav_button = self.driver.find_element(By.LINK_TEXT, "POKEMON")
        nav_button.click()
        self.assertEqual(self.driver.title, "Pokedex")

    def test_bulbasaur_button(self):
        nav_button = self.driver.find_element(By.LINK_TEXT, "POKEMON")
        nav_button.click()
        time.sleep(1)
        bulbasaur_button = self.driver.find_element(By.TAG_NAME, "li")
        bulbasaur_button.click()
        self.assertEqual(self.driver.title, "bulbasaur Details")

    def test_home_button(self):
        nav_button = self.driver.find_element(By.LINK_TEXT, "POKEMON")
        nav_button.click()
        time.sleep(1)
        bulbasaur_button = self.driver.find_element(By.TAG_NAME, "li")
        bulbasaur_button.click()
        time.sleep(3)
        home_button = self.driver.find_element(By.LINK_TEXT, "HOME")
        home_button.click()
        self.assertEqual(self.driver.title, "Pokemon Team Builder")

    def test_teams_nav_button(self):
        nav_button = self.driver.find_element(By.LINK_TEXT, "TEAMS")
        nav_button.click()
        time.sleep(3)
        self.assertEqual(self.driver.title, "Login")
        username_input = self.driver.find_element(By.NAME, "username")
        username_input.send_keys("ogtestuser")
        password_input = self.driver.find_element(By.NAME, "password")
        password_input.send_keys("password1!")
        password_input.send_keys(Keys.RETURN)
        time.sleep(3)
        self.assertEqual(self.driver.title, "Pokemon Team Builder")
        self.assertEqual(self.driver.find_element(By.LINK_TEXT, "LOGOUT").text, "LOGOUT")
        nav_button = self.driver.find_element(By.LINK_TEXT, "TEAMS")
        nav_button.click()
        time.sleep(1)
        self.assertEqual(self.driver.title, "Teams")


    def test_login_button(self):
        login_button = self.driver.find_element(By.LINK_TEXT, "LOGIN")
        login_button.click()
        self.assertEqual(self.driver.title, "Login")

    def test_logging_in(self):
        login_button = self.driver.find_element(By.LINK_TEXT, "LOGIN")
        login_button.click()
        username_input = self.driver.find_element(By.NAME, "username")
        username_input.send_keys("ogtestuser")
        password_input = self.driver.find_element(By.NAME, "password")
        password_input.send_keys("password1!")
        password_input.send_keys(Keys.RETURN)
        time.sleep(3)
        self.assertEqual(self.driver.title, "Pokemon Team Builder")
        self.assertEqual(self.driver.find_element(By.LINK_TEXT, "LOGOUT").text, "LOGOUT")

    def test_logout(self):
        login_button = self.driver.find_element(By.LINK_TEXT, "LOGIN")
        login_button.click()
        username_input = self.driver.find_element(By.NAME, "username")
        username_input.send_keys("ogtestuser")
        password_input = self.driver.find_element(By.NAME, "password")
        password_input.send_keys("password1!")
        password_input.send_keys(Keys.RETURN)
        time.sleep(3)
        logout_button = self.driver.find_element(By.LINK_TEXT, "LOGOUT")
        logout_button.click()
        self.assertEqual(self.driver.title, "Login")
        self.assertEqual(self.driver.find_element(By.LINK_TEXT, "LOGIN").text, "LOGIN")


if __name__ == "__main__":
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestPokemonApp)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)