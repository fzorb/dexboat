from dexboat.commands import option_types
from dexboat.commands.command import Command
from dexboat.commands.cuvantul_zilei import cuvantul_zilei
from dexboat.commands.definitie import definitie
from dexboat.commands.option import Option

COMMANDS = []
COMMANDS.append(Command("definitie", "obține definiția din DEX a unui cuvânt", definitie, options=[
    Option(name="cuvânt", description="Cuvântul al cărei definiții vrei să o vezi", type=option_types.STRING, required=True)
]))
COMMANDS.append(Command("cuvantulzilei", "obține cuvântul zilei de pe Dexonline", cuvantul_zilei))
