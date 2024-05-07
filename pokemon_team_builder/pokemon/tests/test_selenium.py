# Test the functionality of the pokemon application
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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


    def test_pokemon(self):
        nav_button = self.driver.find_element(By.LINK_TEXT, "POKEMON")
        nav_button.click()
        self.assertEqual(self.driver.title, "Pokedex")
        show_filters_button = self.driver.find_element(By.ID, "filterFormButton")
        show_filters_button.click()
        type_filter = self.driver.find_element(By.NAME, "type")
        type_filter.click()
        type_filter_option = type_filter.find_elements(By.TAG_NAME, "option")[1]
        type_filter_option.click()
        time.sleep(1)
        ability_filter = self.driver.find_element(By.NAME, "ability")
        ability_filter.click()
        ability_filter_option = ability_filter.find_elements(By.TAG_NAME, "option")[1]
        ability_filter_option.click()
        time.sleep(1)
        apply_button = self.driver.find_element(By.ID, "filter_form_submit_button")
        apply_button.click()
        self.assertEqual(self.driver.title, "Pokedex")
        next_page_button = self.driver.find_element(By.LINK_TEXT, "next")
        next_page_button.click()
        self.assertEqual(self.driver.title, "Pokedex")
        serperior_button = self.driver.find_element(By.LINK_TEXT, "#497 | serperior | grass")
        serperior_button.click()
        self.assertEqual(self.driver.title, "serperior Details")
        back_button = self.driver.find_element(By.LINK_TEXT, "Back to all Pokemon")
        back_button.click()
        self.assertEqual(self.driver.title, "Pokedex")
        self.driver.close()

    def test_team(self):
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
        time.sleep(1)
        ability1_dropdown = self.driver.find_element(By.ID, "id_ability1")
        ability1_dropdown.click()
        ability1_option = ability1_dropdown.find_elements(By.TAG_NAME, "option")[1]
        ability1_option.click()
        move1_1_dropdown = self.driver.find_element(By.ID, "id_move1_1")
        move1_1_dropdown.click()
        move1_1_option = move1_1_dropdown.find_elements(By.TAG_NAME, "option")[3]
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
        time.sleep(1)
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
        time.sleep(1)
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
        time.sleep(1)
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
        time.sleep(1)
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
        time.sleep(1)
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
        self.assertEqual(self.driver.title, "test team Details")
        edit_team_button = self.driver.find_element(By.ID, "edit_team_button")
        edit_team_button.click()
        self.assertEqual(self.driver.title, "Edit Team")
        pokemon1_dropdown = self.driver.find_element(By.ID, "id_pokemon1")
        pokemon1_dropdown.click()
        pokemon1_option = pokemon1_dropdown.find_elements(By.TAG_NAME, "option")[5]
        pokemon1_option.click()
        submit_team_button = self.driver.find_element(By.ID, "edit_team_submit_button")
        submit_team_button.click()
        self.assertEqual(self.driver.find_element(By.TAG_NAME, "h1").text, "test team Members", )
        delete_team_button = self.driver.find_element(By.ID, "delete_team_button")
        delete_team_button.click()
        alert = WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        alert.accept()
        self.assertEqual(self.driver.title, "Teams")
        self.driver.quit()
    
    def test_moves(self):
        moves_nav = self.driver.find_element(By.LINK_TEXT, "MOVES")
        moves_nav.click()
        self.assertEqual(self.driver.title, "Moves")
        show_filters_button = self.driver.find_element(By.ID, "movesfilterFormButton")
        show_filters_button.click()
        move_type_filter = self.driver.find_element(By.ID, "id_move_type")
        move_type_filter.click()
        move_type_option = move_type_filter.find_elements(By.TAG_NAME, "option")[1]
        move_type_option.click()
        search_button = self.driver.find_element(By.ID, "movesfilterFormSubmit")
        search_button.click()
        self.assertEqual(self.driver.title, "Moves")
        next_page_button = self.driver.find_element(By.LINK_TEXT, "Next")
        next_page_button.click()
        self.assertEqual(self.driver.title, "Moves")
        syrup_bomb = self.driver.find_element(By.LINK_TEXT, "syrup-bomb | grass",)
        syrup_bomb.click()
        self.assertEqual(self.driver.title, "syrup-bomb Details")
        back_button = self.driver.find_element(By.ID, "back_to_moves_button")
        back_button.click()
        self.assertEqual(self.driver.title, "Moves")
        self.driver.quit()

    def test_profile(self):
        login_button = self.driver.find_element(By.LINK_TEXT, "LOGIN")
        login_button.click()
        self.assertEqual(self.driver.title, "Login")
        register_button = self.driver.find_element(By.LINK_TEXT, "Register")
        register_button.click()
        self.assertEqual(self.driver.title, "Registration Form")
        username_input = self.driver.find_element(By.NAME, "username")
        username_input.clear()
        username_input.send_keys("Seleniumtestuser")
        firstname_input = self.driver.find_element(By.NAME, "first_name")
        firstname_input.clear()
        firstname_input.send_keys("Selenium")
        lastname_input = self.driver.find_element(By.NAME, "last_name")
        lastname_input.clear()
        lastname_input.send_keys("Test")
        password_input = self.driver.find_element(By.NAME, "password")
        password_input.clear()
        password_input.send_keys("password1!")
        submit_button = self.driver.find_element(By.ID, "register_submit_button")
        submit_button.click()
        time.sleep(2)
        self.assertEqual(self.driver.title, "Login")
        username_input = self.driver.find_element(By.NAME, "username")
        username_input.clear()
        username_input.send_keys("Seleniumtestuser")
        password_input = self.driver.find_element(By.NAME, "password")
        password_input.clear()
        password_input.send_keys("password1!")
        login_submit_button = self.driver.find_element(By.ID, "login_submit_button")
        login_submit_button.click()
        time.sleep(3)
        profile_nav = self.driver.find_element(By.LINK_TEXT, "PROFILE")
        profile_nav.click()
        self.assertEqual(self.driver.title, "Seleniumtestuser's Profile")
        edit_profile_button = self.driver.find_element(By.ID, "edit_profile_button")
        edit_profile_button.click()
        self.assertEqual(self.driver.title, "Edit Profile")
        firstname_input = self.driver.find_element(By.ID, "id_first_name")
        firstname_input.clear()
        firstname_input.send_keys("firstSelenium")
        lastname_input = self.driver.find_element(By.ID, "id_last_name")
        lastname_input.clear()
        lastname_input.send_keys("lastSelenium")
        submit_profile_button = self.driver.find_element(By.ID, "edit_profile_submit_button")
        submit_profile_button.click()
        self.assertEqual(self.driver.title, "Seleniumtestuser's Profile")
        self.assertEqual(self.driver.find_element(By.TAG_NAME, "h1").text, "Seleniumtestuser's Profile", )
        self.assertEqual(self.driver.find_element(By.TAG_NAME, "li").text, "Name: firstSelenium, lastSelenium", )
        delete_profile_button = self.driver.find_element(By.ID, "delete_profile_button")
        delete_profile_button.click()
        username_input = self.driver.find_element(By.NAME, "username")
        username_input.clear()
        username_input.send_keys("Seleniumtestuser")
        password_input = self.driver.find_element(By.NAME, "password")
        password_input.clear()
        password_input.send_keys("password1!")
        delete_submit_button = self.driver.find_element(By.ID, "delete_profile_submit_button")
        delete_submit_button.click()
        self.assertEqual(self.driver.title, "Login")
        self.driver.quit()

    


if __name__ == "__main__":
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestPokemonApp)
    runner = unittest.TextTestRunner(verbosity=2)

    suite = unittest.TestSuite()
    suite.addTest(TestPokemonApp("test_pokemon"))
    runner.run(suite)
