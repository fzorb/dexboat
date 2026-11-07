# Dexboat
Dexboat is a Discord bot that queries the Romanian Dictionary (DEX) via the https://dexonline.ro API. It is designed to run as a Google Cloud Run Function. 

During the development process of this bot, I have honestly overcomplicated it to the point where I believe this could be considered somewhat of a "microframework". Please feel free to fork it and model this into your own bot!

## Note on internationalization
It makes little sense to internationalize this Discord bot, because it only has one audience: speakers of the Romanian language.

## Commands
`/definitie <cuvânt>` - gives you the definition of a word  
`/cuvantulzilei` - shows you dexonline.ro's daily word and its definiton
