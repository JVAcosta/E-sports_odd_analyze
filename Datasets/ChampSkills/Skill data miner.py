from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import csv

class AbilitiesMiner:

    def __init__(self):
        self.link ='http://leagueoflegends.wikia.com/wiki/'
        self.result = {}
        

    def mine(self,tipo):
        link =self.link+tipo
        driver = webdriver.ChromeOptions()
        driver = webdriver.Chrome()
        driver.get(link)
        elements=driver.find_elements_by_css_selector('span.inline-image.label-after.ability-icon.tooltips-init-complete')
        
        for x in elements:
            champion = x.get_attribute('data-champion')
            skill = x.get_attribute('data-ability')
            try:
                if tipo not in self.result[skill]['type']:
                    self.result[skill]['type'].append(tipo)
                self.result[skill]['champion'] = champion
                self.result[skill]['skill'] = skill 
            except:
                try:
                    self.result[skill]['type'] = []
                    if tipo not in self.result[skill]['type']:
                        self.result[skill]['type'].append(tipo)
                    self.result[skill]['champion'] = champion
                    self.result[skill]['skill'] = skill 
                except:
                    self.result[skill]={}
                    self.result[skill]['type'] = []
                    if tipo not in self.result[skill]['type']:
                        self.result[skill]['type'].append(tipo)
                    self.result[skill]['skill'] = skill 
                    self.result[skill]['champion'] = champion
        driver.quit()   
        return self.result
    
        

tipos = ['Aura','Blink','Combat_status','Magic_damage','Physical_damage','True_damage','Dash','Debuff','Sight','Spell_shield','Untargetability']
am = AbilitiesMiner()
for x in tipos:
    am.mine(x)

with open('../treasures/skill_treasure.csv', 'w') as f:  # Just use 'w' mode in 3.x
    w = csv.DictWriter(f, am.result["Dragon's Descent"].keys())
    w.writeheader()
    for key in am.result.keys():
        w.writerow(am.result[key])
