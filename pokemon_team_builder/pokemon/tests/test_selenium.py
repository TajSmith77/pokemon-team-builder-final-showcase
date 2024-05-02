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
        logout_button = self.driver.find_element(By.LINK_TEXT, "LOGOUT")
        logout_button.click()

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

    def test_create_team(self):
        nav_button = self.driver.find_element(By.LINK_TEXT, "TEAMS")
        nav_button.click()
        if self.driver.find_element(By.LINK_TEXT, "LOGIN").text == "LOGIN":
            username_input = self.driver.find_element(By.NAME, "username")
            username_input.send_keys("ogtestuser")
            password_input = self.driver.find_element(By.NAME, "password")
            password_input.send_keys("password1!")
            password_input.send_keys(Keys.RETURN)
            time.sleep(3)
            nav_button = self.driver.find_element(By.LINK_TEXT, "TEAMS")
            nav_button.click()
        create_team_button = self.driver.find_element(By.LINK_TEXT, "Create Team")
        create_team_button.click()
        self.assertEqual(self.driver.title, "Create Team")
        name_input = self.driver.find_element(By.NAME, "name")
        name_input.send_keys("test team")
        pokemon1_dropdown = self.driver.find_element(By.ID, "id_pokemon1")
        pokemon1_dropdown.click()
        pokemon1_option = pokemon1_dropdown.find_elements(By.TAG_NAME, "option")[1]
        pokemon1_option.click()
        ability1_dropdown = self.driver.find_element(By.ID, "id_ability1")
        ability1_dropdown.click()
        ability1_option = ability1_dropdown.find_elements(By.TAG_NAME, "option")[1]
        ability1_option.click()
        move1_1_dropdown = self.driver.find_element(By.ID, "id_move1_1")
        move1_1_dropdown.click()
        move1_1_option = move1_1_dropdown.find_elements(By.TAG_NAME, "option")[1]
        move1_1_option.click()
        move1_2_dropdown = self.driver.find_element(By.ID, "id_move1_2")
        move1_2_dropdown.click()
        move1_2_option = move1_2_dropdown.find_elements(By.TAG_NAME, "option")[1]
        move1_2_option.click()
        move1_3_dropdown = self.driver.find_element(By.ID, "id_move1_3")
        move1_3_dropdown.click()
        move1_3_option = move1_3_dropdown.find_elements(By.TAG_NAME, "option")[1]
        move1_3_option.click()
        move1_4_dropdown = self.driver.find_element(By.ID, "id_move1_4")
        move1_4_dropdown.click()
        move1_4_option = move1_4_dropdown.find_elements(By.TAG_NAME, "option")[1]
        move1_4_option.click()
        pokemon2_dropdown = self.driver.find_element(By.ID, "id_pokemon2")
        pokemon2_dropdown.click()
        pokemon2_option = pokemon2_dropdown.find_elements(By.TAG_NAME, "option")[1]
        pokemon2_option.click()
        ability2_dropdown = self.driver.find_element(By.ID, "id_ability2")
        ability2_dropdown.click()
        ability2_option = pokemon2_dropdown.find_elements(By.TAG_NAME, "option")[1]
        ability2_option.click()
        move2_1_dropdown = self.driver.find_element(By.ID, "id_move2_1")
        move2_1_dropdown.click()
        move2_1_option = move2_1_dropdown.find_elements(By.TAG_NAME, "option")[1]
        move2_1_option.click()
        move2_2_dropdown = self.driver.find_element(By.ID, "id_move2_2")
        move2_2_dropdown.click()
        move2_2_option = move2_2_dropdown.find_elements(By.TAG_NAME, "option")[1]
        move2_2_option.click()
        move2_3_dropdown = self.driver.find_element(By.ID, "id_move2_3")
        move2_3_dropdown.click()
        move2_3_option = move2_3_dropdown.find_elements(By.TAG_NAME, "option")[1]
        move2_3_option.click()
        move2_4_dropdown = self.driver.find_element(By.ID, "id_move2_4")
        move2_4_dropdown.click()
        move2_4_option = move2_4_dropdown.find_elements(By.TAG_NAME, "option")[1]
        move2_4_option.click()
        pokemon3_dropdown = self.driver.find_element(By.ID, "id_pokemon3")
        pokemon3_dropdown.click()
        pokemon3_option = pokemon3_dropdown.find_elements(By.TAG_NAME, "option")[1]
        pokemon3_option.click()
        ability3_dropdown = self.driver.find_element(By.ID, "id_ability3")
        ability3_dropdown.click()
        ability3_option = pokemon3_dropdown.find_elements(By.TAG_NAME, "option")[1]
        ability3_option.click()
        move3_1_dropdown = self.driver.find_element(By.ID, "id_move3_1")
        move3_1_dropdown.click()
        move3_1_option = move3_1_dropdown.find_elements(By.TAG_NAME, "option")[1]
        move3_1_option.click()
        move3_2_dropdown = self.driver.find_element(By.ID, "id_move3_2")
        move3_2_dropdown.click()
        move3_2_option = move3_2_dropdown.find_elements(By.TAG_NAME, "option")[1]
        move3_2_option.click()
        move3_3_dropdown = self.driver.find_element(By.ID, "id_move3_3")
        move3_3_dropdown.click()
        move3_3_option = move3_3_dropdown.find_elements(By.TAG_NAME, "option")[1]
        move3_3_option.click()
        move3_4_dropdown = self.driver.find_element(By.ID, "id_move3_4")
        move3_4_dropdown.click()
        move3_4_option = move3_4_dropdown.find_elements(By.TAG_NAME, "option")[1]
        move3_4_option.click()
        pokemon4_dropdown = self.driver.find_element(By.ID, "id_pokemon4")
        pokemon4_dropdown.click()
        pokemon4_option = pokemon4_dropdown.find_elements(By.TAG_NAME, "option")[1]
        pokemon4_option.click()
        ability4_dropdown = self.driver.find_element(By.ID, "id_ability4")
        ability4_dropdown.click()
        ability4_option = pokemon4_dropdown.find_elements(By.TAG_NAME, "option")[1]
        ability4_option.click()
        move4_1_dropdown = self.driver.find_element(By.ID, "id_move4_1")
        move4_1_dropdown.click()
        move4_1_option = move4_1_dropdown.find_elements(By.TAG_NAME, "option")[1]
        move4_1_option.click()
        move4_2_dropdown = self.driver.find_element(By.ID, "id_move4_2")
        move4_2_dropdown.click()
        move4_2_option = move4_2_dropdown.find_elements(By.TAG_NAME, "option")[1]
        move4_2_option.click()
        move4_3_dropdown = self.driver.find_element(By.ID, "id_move4_3")
        move4_3_dropdown.click()
        move4_3_option = move4_3_dropdown.find_elements(By.TAG_NAME, "option")[1]
        move4_3_option.click()
        move4_4_dropdown = self.driver.find_element(By.ID, "id_move4_4")
        move4_4_dropdown.click()
        move4_4_option = move4_4_dropdown.find_elements(By.TAG_NAME, "option")[1]
        move4_4_option.click()
        pokemon5_dropdown = self.driver.find_element(By.ID, "id_pokemon5")
        pokemon5_dropdown.click()
        pokemon5_option = pokemon5_dropdown.find_elements(By.TAG_NAME, "option")[1]
        pokemon5_option.click()
        ability5_dropdown = self.driver.find_element(By.ID, "id_ability5")
        ability5_dropdown.click()
        ability5_option = pokemon5_dropdown.find_elements(By.TAG_NAME, "option")[1]
        ability5_option.click()
        move5_1_dropdown = self.driver.find_element(By.ID, "id_move5_1")
        move5_1_dropdown.click()
        move5_1_option = move5_1_dropdown.find_elements(By.TAG_NAME, "option")[1]
        move5_1_option.click()
        move5_2_dropdown = self.driver.find_element(By.ID, "id_move5_2")
        move5_2_dropdown.click()
        move5_2_option = move5_2_dropdown.find_elements(By.TAG_NAME, "option")[1]
        move5_2_option.click()
        move5_3_dropdown = self.driver.find_element(By.ID, "id_move5_3")
        move5_3_dropdown.click()
        move5_3_option = move5_3_dropdown.find_elements(By.TAG_NAME, "option")[1]
        move5_3_option.click()
        move5_4_dropdown = self.driver.find_element(By.ID, "id_move5_4")
        move5_4_dropdown.click()
        move5_4_option = move5_4_dropdown.find_elements(By.TAG_NAME, "option")[1]
        move5_4_option.click()
        pokemon6_dropdown = self.driver.find_element(By.ID, "id_pokemon6")
        pokemon6_dropdown.click()
        pokemon6_option = pokemon6_dropdown.find_elements(By.TAG_NAME, "option")[1]
        pokemon6_option.click()
        ability6_dropdown = self.driver.find_element(By.ID, "id_ability6")
        ability6_dropdown.click()
        ability6_option = pokemon6_dropdown.find_elements(By.TAG_NAME, "option")[1]
        ability6_option.click()
        move6_1_dropdown = self.driver.find_element(By.ID, "id_move6_1")
        move6_1_dropdown.click()
        move6_1_option = move6_1_dropdown.find_elements(By.TAG_NAME, "option")[1]
        move6_1_option.click()
        move6_2_dropdown = self.driver.find_element(By.ID, "id_move6_2")
        move6_2_dropdown.click()
        move6_2_option = move6_2_dropdown.find_elements(By.TAG_NAME, "option")[1]
        move6_2_option.click()
        move6_3_dropdown = self.driver.find_element(By.ID, "id_move6_3")
        move6_3_dropdown.click()
        move6_3_option = move6_3_dropdown.find_elements(By.TAG_NAME, "option")[1]
        move6_3_option.click()
        move6_4_dropdown = self.driver.find_element(By.ID, "id_move6_4")
        move6_4_dropdown.click()
        move6_4_option = move6_4_dropdown.find_elements(By.TAG_NAME, "option")[1]
        move6_4_option.click()
        create_team_button = self.driver.find_element(By.NAME, "CreateTeam")
        create_team_button.click()
        self.assertEqual(self.driver.title, "Create Team")

if __name__ == "__main__":
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestPokemonApp)
    runner = unittest.TextTestRunner(verbosity=2)

    suite = unittest.TestSuite()
    suite.addTest(TestPokemonApp("test_create_team"))
    runner.run(suite)
