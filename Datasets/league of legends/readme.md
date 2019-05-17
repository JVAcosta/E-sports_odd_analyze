# Champ Duos

This datasets have all the datas about league of legends champs, lore, skills name, name...

## Mining

To get tthis data we have to download it from league of legends api https://ddragon.leagueoflegends.com/cdn/dragontail-*.*.*.tgz

## Structure
The structure of an champion is given by

```json
    "Aatrox": {
      "version": "6.24.1",
      "id": "Aatrox",
      "key": "266",
      "name": "Aatrox",
      "title": "a Espada Darkin",
      "blurb": "Aatrox é um guerreiro lendário, um dos cinco restantes de uma raça antiga conhecida como Darkin. Ele empunha sua massiva espada com graça e pompa, dilacerando legiões inteiras com um estilo hipnótico a se contemplar. Com cada adversário derrubado, a ...",
      "info": {
        "attack": 8,
        "defense": 4,
        "magic": 3,
        "difficulty": 4
      },
      "image": {
        "full": "Aatrox.png",
        "sprite": "champion0.png",
        "group": "champion",
        "x": 0,
        "y": 0,
        "w": 48,
        "h": 48
      },
      "tags": [
        "Fighter",
        "Tank"
      ],
      "partype": "BloodWell",
      "stats": {
        "hp": 537.8,
        "hpperlevel": 85,
        "mp": 105.6,
        "mpperlevel": 45,
        "movespeed": 345,
        "armor": 24.384,
        "armorperlevel": 3.8,
        "spellblock": 32.1,
        "spellblockperlevel": 1.25,
        "attackrange": 150,
        "hpregen": 6.59,
        "hpregenperlevel": 0.5,
        "mpregen": 0,
        "mpregenperlevel": 0,
        "crit": 0,
        "critperlevel": 0,
        "attackdamage": 60.376,
        "attackdamageperlevel": 3.2,
        "attackspeedoffset": -0.04,
        "attackspeedperlevel": 3
      }
    }
```