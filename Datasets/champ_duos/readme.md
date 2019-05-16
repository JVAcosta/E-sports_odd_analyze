# Champ Duos

In this dataset we have all the duos champs by lane, seaseon, team, We have the following combinations of lanes:

```
*Jungle with top laner
*Jungle with mid laner
*Jungle with adc
*Jungle with support
*ADC with support
```

## Mining

To get this data we use the following python files in the folder:
```
champ_duos_miner
champ_duos_processor
```

## Structure
The strcture of an line of this dataset is given by:

```json
CHAMP1,CHAMP2,CHAMP1_POSITION,CHAMP2_POSITION,VICTORY,DEFEAT,TOTALPLAYED,PERCENTVICTORY,PERCENTDEFEAT,YEAR,SEASON,TEAM
Irelia,RekSai,TOP_LANER,JUNGLER,5,4,9,0.5555555555555556,0.4444444444444444,2015,Spring,Blue
```