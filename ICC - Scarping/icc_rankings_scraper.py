from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json
import os

role_list =["bowling","batting","allrounder"]
gender_list = ["mens","womens"]
formats_list = ["test","odi","t20i"]

options = webdriver.ChromeOptions()
# options.add_argument("--headless")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36")
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.maximize_window()
wait = WebDriverWait(driver,5)

# Handle cookies
driver.get("https://www.icc-cricket.com/")
try:
    wait.until(EC.element_to_be_clickable((By.ID, "onetrust-reject-all-handler"))).click()
except:
    pass

for role in role_list:
    for gender in gender_list:
        for formats in formats_list:
            if gender == "womens" and formats == "test":
                continue
            else:
                url = f"https://www.icc-cricket.com/rankings/{role}/{gender}/{formats}"
                position = 1
                final_list = []
                driver.get(url)
                time.sleep(3)

                wait.until(
                    EC.presence_of_element_located((By.CSS_SELECTOR,"span.si-text.si-fname"))
                )

                print("Web Page loaded Successfully ")

                # Load all players
                load_more = driver.find_element(By.CLASS_NAME,"si-btn-site")
                while True:
                    try:
                        load_more = wait.until(
                            EC.element_to_be_clickable(
                                (By.XPATH, "//button[.='Load More']")
                            )
                        )
                        load_more.click()
                    except:
                        print("All page loaded successfully")
                        break


                player_list = driver.find_elements(By.CLASS_NAME,"si-player-name")
                team_list = driver.find_elements(By.CLASS_NAME,'si-team-name')
                rating_list = driver.find_elements(By.CLASS_NAME,'si-rating')
                rating_list=rating_list[1:]
                best_list = driver.find_elements(By.CLASS_NAME,'si-best')
                best_list=best_list[1:]

                for player,team,rating,best in zip(player_list,team_list,rating_list,best_list):
                    final_list.append({
                        "Position" :position,
                        "Player": player.text.title().replace("\n", " "),
                        "Team": team.text.title(),
                        "Rating": rating.text,
                        "Career Best": best.text,
                    })
                    position+=1

                print("Scraping Completed")

                # Folder structure
                base_dir = "icc_rankings"
                format_dir = os.path.join(base_dir, gender, formats)
                os.makedirs(format_dir, exist_ok=True)

                file_name = f"{role}.json"
                file_path = os.path.join(format_dir, file_name)

                with open(file_path, "w", encoding="utf-8") as f:
                    json.dump(final_list, f, indent=4, ensure_ascii=False)

                print(f"Saved → {file_path}\n")

driver.close()

