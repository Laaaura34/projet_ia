# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd
import pickle
from PIL import Image
from plotly import graph_objs as go


im = Image.open("photos/poke.ico")
st.set_page_config(
   page_title="Pokemon Prediction App",
   page_icon=im,
   #layout="wide",
   #initial_sidebar_state="expanded",
   menu_items={
        'About': "Challenge pokémon - Béteille Lisa & Sénécaille Laura"
   }
)

df_pokemon_copie_1 = pd.read_csv("Data/new_pokemon_prediction_1.csv")
df_pokemon_copie_1.set_index("ID", inplace=True)

df_pokemon_1 = pd.read_csv("Data/df_pokemon_1.csv")


dict_type1 = dict(zip(df_pokemon_1['Name'], df_pokemon_copie_1['Type_1']))
dict_type2 = dict(zip(df_pokemon_1['Name'], df_pokemon_copie_1['Type_2']))
dict_HP = dict(zip(df_pokemon_1['Name'], df_pokemon_copie_1['HP']))
dict_Attack = dict(zip(df_pokemon_1['Name'], df_pokemon_copie_1['Attack']))
dict_Defense = dict(zip(df_pokemon_1['Name'], df_pokemon_copie_1['Defense']))
dict_Atq_speciale= dict(zip(df_pokemon_1['Name'], df_pokemon_copie_1['Atq_speciale']))
dict_Def_speciale= dict(zip(df_pokemon_1['Name'], df_pokemon_copie_1['Def_speciale']))
dict_vitesse= dict(zip(df_pokemon_1['Name'], df_pokemon_copie_1['vitesse']))
dict_victoire= dict(zip(df_pokemon_1['Name'], df_pokemon_copie_1['victoire']))
dict_ratio= dict(zip(df_pokemon_1['Name'], df_pokemon_copie_1['ratio']))
dict_gen = dict(zip(df_pokemon_1['Name'], df_pokemon_copie_1['Generation']))
dict_leg = dict(zip(df_pokemon_1['Name'], df_pokemon_copie_1['Legendary']))


st.write("<h1>PREDICTION COMBAT POKEMON</h1>", unsafe_allow_html=True )

col1, col2  = st.columns(2)

first_pokemon = col1.selectbox("Saisissez le premier pokémon", key = "First_pokemon", index = 4,
                               options=("Bulbasaur","Ivysaur","Venusaur","Mega Venusaur","Charmander","Charmeleon",
                                "Charizard","Mega Charizard X","Mega Charizard Y","Squirtle","Wartortle","Blastoise",
                                "Mega Blastoise","Caterpie","Metapod","Butterfree","Weedle","Kakuna","Beedrill","Mega Beedrill",
                                "Pidgey","Pidgeotto","Pidgeot","Mega Pidgeot","Rattata","Raticate","Spearow","Fearow","Ekans","Arbok",
                                "Pikachu","Raichu","Sandshrew","Sandslash","Nidoran♀","Nidorina","Nidoqueen","Nidoran♂","Nidorino",
                                "Nidoking","Clefairy","Clefable","Vulpix","Ninetales","Jigglypuff","Wigglytuff","Zubat","Golbat","Oddish",
                                "Gloom","Vileplume","Paras","Parasect","Venonat","Venomoth","Diglett","Dugtrio","Meowth","Persian","Psyduck",
                                "Golduck","Mankey","Primeape","Growlithe","Arcanine","Poliwag","Poliwhirl","Poliwrath","Abra","Kadabra",
                                "Alakazam","Mega Alakazam","Machop","Machoke","Machamp","Bellsprout","Weepinbell","Victreebel","Tentacool",
                                "Tentacruel","Geodude","Graveler","Golem","Ponyta","Rapidash","Slowpoke","Slowbro","Mega Slowbro","Magnemite",
                                "Magneton","Farfetch'd","Doduo","Dodrio","Seel","Dewgong","Grimer","Muk","Shellder","Cloyster","Gastly",
                                "Haunter", "Gengar","Mega Gengar","Onix","Drowzee","Hypno","Krabby","Kingler","Voltorb","Electrode","Exeggcute",
                                "Exeggutor","Cubone","Marowak","Hitmonlee","Hitmonchan","Lickitung","Koffing","Weezing","Rhyhorn","Rhydon",
                                "Chansey","Tangela","Kangaskhan","Mega Kangaskhan","Horsea","Seadra","Goldeen","Seaking","Staryu","Starmie",
                                "Mr. Mime","Scyther","Jynx","Electabuzz","Magmar","Pinsir","Mega Pinsir","Tauros","Magikarp","Gyarados",
                                "Mega Gyarados","Lapras","Ditto","Eevee","Vaporeon","Jolteon","Flareon","Porygon","Omanyte","Omastar",
                                "Kabuto","Kabutops","Aerodactyl","Mega Aerodactyl","Snorlax","Articuno","Zapdos","Moltres","Dratini","Dragonair",
                                "Dragonite","Mewtwo","Mega Mewtwo X","Mega Mewtwo Y","Mew","Chikorita","Bayleef","Meganium","Cyndaquil",
                                "Quilava","Typhlosion","Totodile","Croconaw","Feraligatr","Sentret","Furret","Hoothoot","Noctowl","Ledyba",
                                "Ledian","Spinarak","Ariados","Crobat","Chinchou","Lanturn","Pichu","Cleffa","Igglybuff","Togepi","Togetic",
                                "Natu","Xatu","Mareep","Flaaffy","Ampharos","Mega Ampharos","Bellossom","Marill","Azumarill","Sudowoodo",
                                "Politoed","Hoppip","Skiploom","Jumpluff","Aipom","Sunkern","Sunflora","Yanma","Wooper","Quagsire","Espeon","Umbreon","Murkrow","Slowking",
                                "Misdreavus","Unown","Wobbuffet","Girafarig","Pineco","Forretress","Dunsparce","Gligar","Steelix",
                                "Mega Steelix","Snubbull","Granbull", "Qwilfish","Scizor","Mega Scizor","Shuckle","Heracross","Mega Heracross",
                                "Sneasel","Teddiursa","Ursaring","Slugma","Magcargo","Swinub","Piloswine","Corsola","Remoraid","Octillery",
                                "Delibird","Mantine","Skarmory","Houndour","Houndoom","Mega Houndoom","Kingdra","Phanpy","Donphan","Porygon2",
                                "Stantler", "Smeargle","Tyrogue","Hitmontop","Smoochum","Elekid","Magby","Miltank","Blissey","Raikou",
                                "Entei","Suicune","Larvitar","Pupitar","Tyranitar","Mega Tyranitar","Lugia","Ho-oh","Celebi","Treecko","Grovyle",
                                "Sceptile","Mega Sceptile","Torchic","Combusken","Blaziken","Mega Blaziken","Mudkip","Marshtomp","Swampert",
                                "Mega Swampert","Poochyena","Mightyena","Zigzagoon","Linoone","Wurmple","Silcoon","Beautifly","Cascoon",
                                "Dustox","Lotad","Lombre","Ludicolo","Seedot","Nuzleaf","Shiftry","Taillow","Swellow","Wingull","Pelipper","Ralts",
                                "Kirlia","Gardevoir","Mega Gardevoir","Surskit","Masquerain","Shroomish","Breloom","Slakoth","Vigoroth",
                                "Slaking","Nincada","Ninjask","Shedinja","Whismur","Loudred","Exploud","Makuhita","Hariyama","Azurill",
                                "Nosepass","Skitty","Delcatty","Sableye","Mega Sableye","Mawile","Mega Mawile","Aron","Lairon","Aggron",
                                "Mega Aggron","Meditite","Medicham","Mega Medicham","Electrike","Manectric","Mega Manectric","Plusle",
                                "Minun","Volbeat","Illumise","Roselia","Gulpin","Swalot","Carvanha","Sharpedo","Mega Sharpedo","Wailmer",
                                "Wailord","Numel","Camerupt","Mega Camerupt","Torkoal","Spoink","Grumpig","Spinda","Trapinch","Vibrava",
                                "Flygon","Cacnea","Cacturne", "Swablu","Altaria","Mega Altaria","Zangoose","Seviper","Lunatone","Solrock",
                                "Barboach","Whiscash","Corphish","Crawdaunt","Baltoy","Claydol","Lileep","Cradily","Anorith",
                                "Armaldo","Feebas","Milotic","Castform","Kecleon","Shuppet","Banette","Mega Banette","Duskull", "Dusclops",
                                "Tropius","Chimecho","Absol","Mega Absol","Wynaut","Snorunt","Glalie","Mega Glalie","Spheal","Sealeo",
                                "Walrein","Clamperl","Huntail","Gorebyss","Relicanth","Luvdisc","Bagon","Shelgon",
                                "Salamence","Mega Salamence","Beldum","Metang","Metagross","Mega Metagross","Regirock","Regice",
                                "Registeel","Latias","Mega Latias","Latios","Mega Latios","Kyogre","Primal Kyogre","Groudon","Primal Groudon",
                                "Rayquaza","Mega Rayquaza","Jirachi","Deoxys Normal Forme","DeoxysAttack Forme","Deoxys Defense Forme","Deoxys Speed Forme",
                                "Turtwig","Grotle","Torterra","Chimchar","Monferno","Infernape","Piplup","Prinplup","Empoleon","Starly","Staravia",
                                "Staraptor","Bidoof","Bibarel","Kricketot","Kricketune","Shinx","Luxio","Luxray","Budew","Roserade","Cranidos",
                                "Rampardos","Shieldon","Bastiodon","Burmy","Wormadam Plant Cloak","Wormadam Sandy Cloak","Wormadam Trash Cloak",
                                "Mothim","Combee","Vespiquen","Pachirisu","Buizel","Floatzel","Cherubi","Cherrim","Shellos","Gastrodon","Ambipom",
                                "Drifloon","Drifblim","Buneary","Lopunny","Mega Lopunny","Mismagius","Honchkrow","Glameow","Purugly","Chingling",
                                "Stunky","Skuntank", "Bronzor","Bronzong","Bonsly","Mime Jr.","Happiny","Chatot",
                                "Spiritomb","Gible","Gabite","Garchomp","Mega Garchomp","Munchlax","Riolu","Lucario","Mega Lucario","Hippopotas",
                                "Hippowdon","Skorupi","Drapion","Croagunk","Toxicroak","Carnivine","Finneon","Lumineon",
                                "Mantyke","Snover","Abomasnow","Mega Abomasnow","Weavile","Magnezone","Lickilicky","Rhyperior",
                                "Tangrowth","Electivire","Magmortar","Togekiss","Yanmega","Leafeon","Glaceon","Gliscor","Mamoswine","Porygon-Z","Gallade","Mega Gallade",
                                "Probopass","Dusknoir","Froslass","Rotom","Heat Rotom","Wash Rotom","Frost Rotom","Fan Rotom","Mow Rotom",
                                "Uxie","Mesprit","Azelf","Dialga","Palkia","Heatran","Regigigas","Giratina Altered Forme","Giratina Origin Forme",
                                "Cresselia","Phione","Manaphy","Darkrai","Shaymin Land Forme","Shaymin Sky Forme","Arceus","Victini","Snivy","Servine",
                                "Serperior","Tepig","Pignite","Emboar","Oshawott","Dewott","Samurott","Patrat","Watchog","Lillipup","Herdier",
                                "Stoutland","Purrloin","Liepard","Pansage","Simisage","Pansear","Simisear","Panpour","Simipour","Munna","Musharna",
                                "Pidove","Tranquill","Unfezant","Blitzle","Zebstrika","Roggenrola","Boldore","Gigalith","Woobat","Swoobat","Drilbur",
                                "Excadrill","Audino","Mega Audino","Timburr","Gurdurr","Conkeldurr","Tympole","Palpitoad","Seismitoad","Throh","Sawk",
                                "Sewaddle","Swadloon","Leavanny","Venipede","Whirlipede","Scolipede","Cottonee","Whimsicott","Petilil",
                                "Lilligant","Basculin","Sandile","Krokorok","Krookodile","Darumaka","Darmanitan Standard Mode","Darmanitan Zen Mode",
                                "Maractus","Dwebble","Crustle","Scraggy","Scrafty","Sigilyph","Yamask","Cofagrigus","Tirtouga","Carracosta","Archen",
                                "Archeops","Trubbish","Garbodor","Zorua","Zoroark","Minccino","Cinccino","Gothita","Gothorita","Gothitelle","Solosis",
                                "Duosion","Reuniclus","Ducklett","Swanna","Vanillite","Vanillish","Vanilluxe","Deerling","Sawsbuck","Emolga","Karrablast",
                                "Escavalier","Foongus","Amoonguss","Frillish","Jellicent","Alomomola","Joltik","Galvantula","Ferroseed","Ferrothorn",
                                "Klink","Klang","Klinklang","Tynamo","Eelektrik","Eelektross","Elgyem","Beheeyem","Litwick","Lampent","Chandelure",
                                "Axew","Fraxure","Haxorus","Cubchoo","Beartic","Cryogonal","Shelmet","Accelgor","Stunfisk","Mienfoo","Mienshao",
                                "Druddigon","Golett","Golurk","Pawniard","Bisharp","Bouffalant","Rufflet","Braviary","Vullaby","Mandibuzz","Heatmor","Durant",
                                "Deino","Zweilous","Hydreigon","Larvesta","Volcarona","Cobalion","Terrakion","Virizion","Tornadus Incarnate Forme",
                                "Tornadus Therian Forme","Thundurus Incarnate Forme","Thundurus Therian Forme","Reshiram","Zekrom","Landorus Incarnate Forme",
                                "Landorus Therian Forme","Kyurem","Kyurem Black Kyurem","Kyurem White Kyurem","Keldeo Ordinary Forme","Keldeo Resolute Forme",
                                "Meloetta Aria Forme","Meloetta Pirouette Forme","Genesect","Chespin","Quilladin","Chesnaught","Fennekin","Braixen",
                                "Delphox","Froakie","Frogadier","Greninja","Bunnelby","Diggersby","Fletchling","Fletchinder","Talonflame","Scatterbug","Spewpa",
                                "Vivillon","Litleo","Pyroar","Flabébé","Floette","Florges","Skiddo","Gogoat","Pancham","Pangoro","Furfrou","Espurr","Meowstic Male",
                                "Meowstic Female","Honedge","Doublade","Aegislash Blade Forme","Aegislash Shield Forme","Spritzee","Aromatisse","Swirlix","Slurpuff",
                                "Inkay","Malamar","Binacle","Barbaracle","Skrelp","Dragalge","Clauncher","Clawitzer","Helioptile","Heliolisk","Tyrunt",
                                "Tyrantrum","Amaura","Aurorus","Sylveon","Hawlucha","Dedenne","Carbink","Goomy","Sliggoo","Goodra","Klefki","Phantump","Trevenant",
                                "Pumpkaboo Average Size","Pumpkaboo Small Size","Pumpkaboo Large Size","Pumpkaboo Super Size","Gourgeist Average Size",
                                "Gourgeist Small Size","Gourgeist Large Size","Gourgeist Super Size","Bergmite","Avalugg","Noibat","Noivern","Xerneas",
                                "Yveltal","Zygarde Half Forme","Diancie","Mega Diancie","Hoopa Confined","Hoopa Unbound","Volcanion"))
second_pokemon = col2.selectbox("Saisissez le second pokémon", key = "Second_pokemon", index = 0, 
                               options=("Bulbasaur","Ivysaur","Venusaur","Mega Venusaur","Charmander","Charmeleon",
                                "Charizard","Mega Charizard X","Mega Charizard Y","Squirtle","Wartortle","Blastoise",
                                "Mega Blastoise","Caterpie","Metapod","Butterfree","Weedle","Kakuna","Beedrill","Mega Beedrill",
                                "Pidgey","Pidgeotto","Pidgeot","Mega Pidgeot","Rattata","Raticate","Spearow","Fearow","Ekans","Arbok",
                                "Pikachu","Raichu","Sandshrew","Sandslash","Nidoran♀","Nidorina","Nidoqueen","Nidoran♂","Nidorino",
                                "Nidoking","Clefairy","Clefable","Vulpix","Ninetales","Jigglypuff","Wigglytuff","Zubat","Golbat","Oddish",
                                "Gloom","Vileplume","Paras","Parasect","Venonat","Venomoth","Diglett","Dugtrio","Meowth","Persian","Psyduck",
                                "Golduck","Mankey","Primeape","Growlithe","Arcanine","Poliwag","Poliwhirl","Poliwrath","Abra","Kadabra",
                                "Alakazam","Mega Alakazam","Machop","Machoke","Machamp","Bellsprout","Weepinbell","Victreebel","Tentacool",
                                "Tentacruel","Geodude","Graveler","Golem","Ponyta","Rapidash","Slowpoke","Slowbro","Mega Slowbro","Magnemite",
                                "Magneton","Farfetch'd","Doduo","Dodrio","Seel","Dewgong","Grimer","Muk","Shellder","Cloyster","Gastly",
                                "Haunter", "Gengar","Mega Gengar","Onix","Drowzee","Hypno","Krabby","Kingler","Voltorb","Electrode","Exeggcute",
                                "Exeggutor","Cubone","Marowak","Hitmonlee","Hitmonchan","Lickitung","Koffing","Weezing","Rhyhorn","Rhydon",
                                "Chansey","Tangela","Kangaskhan","Mega Kangaskhan","Horsea","Seadra","Goldeen","Seaking","Staryu","Starmie",
                                "Mr. Mime","Scyther","Jynx","Electabuzz","Magmar","Pinsir","Mega Pinsir","Tauros","Magikarp","Gyarados",
                                "Mega Gyarados","Lapras","Ditto","Eevee","Vaporeon","Jolteon","Flareon","Porygon","Omanyte","Omastar",
                                "Kabuto","Kabutops","Aerodactyl","Mega Aerodactyl","Snorlax","Articuno","Zapdos","Moltres","Dratini","Dragonair",
                                "Dragonite","Mewtwo","Mega Mewtwo X","Mega Mewtwo Y","Mew","Chikorita","Bayleef","Meganium","Cyndaquil",
                                "Quilava","Typhlosion","Totodile","Croconaw","Feraligatr","Sentret","Furret","Hoothoot","Noctowl","Ledyba",
                                "Ledian","Spinarak","Ariados","Crobat","Chinchou","Lanturn","Pichu","Cleffa","Igglybuff","Togepi","Togetic",
                                "Natu","Xatu","Mareep","Flaaffy","Ampharos","Mega Ampharos","Bellossom","Marill","Azumarill","Sudowoodo",
                                "Politoed","Hoppip","Skiploom","Jumpluff","Aipom","Sunkern","Sunflora","Yanma","Wooper","Quagsire","Espeon","Umbreon","Murkrow","Slowking",
                                "Misdreavus","Unown","Wobbuffet","Girafarig","Pineco","Forretress","Dunsparce","Gligar","Steelix",
                                "Mega Steelix","Snubbull","Granbull", "Qwilfish","Scizor","Mega Scizor","Shuckle","Heracross","Mega Heracross",
                                "Sneasel","Teddiursa","Ursaring","Slugma","Magcargo","Swinub","Piloswine","Corsola","Remoraid","Octillery",
                                "Delibird","Mantine","Skarmory","Houndour","Houndoom","Mega Houndoom","Kingdra","Phanpy","Donphan","Porygon2",
                                "Stantler", "Smeargle","Tyrogue","Hitmontop","Smoochum","Elekid","Magby","Miltank","Blissey","Raikou",
                                "Entei","Suicune","Larvitar","Pupitar","Tyranitar","Mega Tyranitar","Lugia","Ho-oh","Celebi","Treecko","Grovyle",
                                "Sceptile","Mega Sceptile","Torchic","Combusken","Blaziken","Mega Blaziken","Mudkip","Marshtomp","Swampert",
                                "Mega Swampert","Poochyena","Mightyena","Zigzagoon","Linoone","Wurmple","Silcoon","Beautifly","Cascoon",
                                "Dustox","Lotad","Lombre","Ludicolo","Seedot","Nuzleaf","Shiftry","Taillow","Swellow","Wingull","Pelipper","Ralts",
                                "Kirlia","Gardevoir","Mega Gardevoir","Surskit","Masquerain","Shroomish","Breloom","Slakoth","Vigoroth",
                                "Slaking","Nincada","Ninjask","Shedinja","Whismur","Loudred","Exploud","Makuhita","Hariyama","Azurill",
                                "Nosepass","Skitty","Delcatty","Sableye","Mega Sableye","Mawile","Mega Mawile","Aron","Lairon","Aggron",
                                "Mega Aggron","Meditite","Medicham","Mega Medicham","Electrike","Manectric","Mega Manectric","Plusle",
                                "Minun","Volbeat","Illumise","Roselia","Gulpin","Swalot","Carvanha","Sharpedo","Mega Sharpedo","Wailmer",
                                "Wailord","Numel","Camerupt","Mega Camerupt","Torkoal","Spoink","Grumpig","Spinda","Trapinch","Vibrava",
                                "Flygon","Cacnea","Cacturne", "Swablu","Altaria","Mega Altaria","Zangoose","Seviper","Lunatone","Solrock",
                                "Barboach","Whiscash","Corphish","Crawdaunt","Baltoy","Claydol","Lileep","Cradily","Anorith",
                                "Armaldo","Feebas","Milotic","Castform","Kecleon","Shuppet","Banette","Mega Banette","Duskull", "Dusclops",
                                "Tropius","Chimecho","Absol","Mega Absol","Wynaut","Snorunt","Glalie","Mega Glalie","Spheal","Sealeo",
                                "Walrein","Clamperl","Huntail","Gorebyss","Relicanth","Luvdisc","Bagon","Shelgon",
                                "Salamence","Mega Salamence","Beldum","Metang","Metagross","Mega Metagross","Regirock","Regice",
                                "Registeel","Latias","Mega Latias","Latios","Mega Latios","Kyogre","Primal Kyogre","Groudon","Primal Groudon",
                                "Rayquaza","Mega Rayquaza","Jirachi","Deoxys Normal Forme","DeoxysAttack Forme","Deoxys Defense Forme","Deoxys Speed Forme",
                                "Turtwig","Grotle","Torterra","Chimchar","Monferno","Infernape","Piplup","Prinplup","Empoleon","Starly","Staravia",
                                "Staraptor","Bidoof","Bibarel","Kricketot","Kricketune","Shinx","Luxio","Luxray","Budew","Roserade","Cranidos",
                                "Rampardos","Shieldon","Bastiodon","Burmy","Wormadam Plant Cloak","Wormadam Sandy Cloak","Wormadam Trash Cloak",
                                "Mothim","Combee","Vespiquen","Pachirisu","Buizel","Floatzel","Cherubi","Cherrim","Shellos","Gastrodon","Ambipom",
                                "Drifloon","Drifblim","Buneary","Lopunny","Mega Lopunny","Mismagius","Honchkrow","Glameow","Purugly","Chingling",
                                "Stunky","Skuntank", "Bronzor","Bronzong","Bonsly","Mime Jr.","Happiny","Chatot",
                                "Spiritomb","Gible","Gabite","Garchomp","Mega Garchomp","Munchlax","Riolu","Lucario","Mega Lucario","Hippopotas",
                                "Hippowdon","Skorupi","Drapion","Croagunk","Toxicroak","Carnivine","Finneon","Lumineon",
                                "Mantyke","Snover","Abomasnow","Mega Abomasnow","Weavile","Magnezone","Lickilicky","Rhyperior",
                                "Tangrowth","Electivire","Magmortar","Togekiss","Yanmega","Leafeon","Glaceon","Gliscor","Mamoswine","Porygon-Z","Gallade","Mega Gallade",
                                "Probopass","Dusknoir","Froslass","Rotom","Heat Rotom","Wash Rotom","Frost Rotom","Fan Rotom","Mow Rotom",
                                "Uxie","Mesprit","Azelf","Dialga","Palkia","Heatran","Regigigas","Giratina Altered Forme","Giratina Origin Forme",
                                "Cresselia","Phione","Manaphy","Darkrai","Shaymin Land Forme","Shaymin Sky Forme","Arceus","Victini","Snivy","Servine",
                                "Serperior","Tepig","Pignite","Emboar","Oshawott","Dewott","Samurott","Patrat","Watchog","Lillipup","Herdier",
                                "Stoutland","Purrloin","Liepard","Pansage","Simisage","Pansear","Simisear","Panpour","Simipour","Munna","Musharna",
                                "Pidove","Tranquill","Unfezant","Blitzle","Zebstrika","Roggenrola","Boldore","Gigalith","Woobat","Swoobat","Drilbur",
                                "Excadrill","Audino","Mega Audino","Timburr","Gurdurr","Conkeldurr","Tympole","Palpitoad","Seismitoad","Throh","Sawk",
                                "Sewaddle","Swadloon","Leavanny","Venipede","Whirlipede","Scolipede","Cottonee","Whimsicott","Petilil",
                                "Lilligant","Basculin","Sandile","Krokorok","Krookodile","Darumaka","Darmanitan Standard Mode","Darmanitan Zen Mode",
                                "Maractus","Dwebble","Crustle","Scraggy","Scrafty","Sigilyph","Yamask","Cofagrigus","Tirtouga","Carracosta","Archen",
                                "Archeops","Trubbish","Garbodor","Zorua","Zoroark","Minccino","Cinccino","Gothita","Gothorita","Gothitelle","Solosis",
                                "Duosion","Reuniclus","Ducklett","Swanna","Vanillite","Vanillish","Vanilluxe","Deerling","Sawsbuck","Emolga","Karrablast",
                                "Escavalier","Foongus","Amoonguss","Frillish","Jellicent","Alomomola","Joltik","Galvantula","Ferroseed","Ferrothorn",
                                "Klink","Klang","Klinklang","Tynamo","Eelektrik","Eelektross","Elgyem","Beheeyem","Litwick","Lampent","Chandelure",
                                "Axew","Fraxure","Haxorus","Cubchoo","Beartic","Cryogonal","Shelmet","Accelgor","Stunfisk","Mienfoo","Mienshao",
                                "Druddigon","Golett","Golurk","Pawniard","Bisharp","Bouffalant","Rufflet","Braviary","Vullaby","Mandibuzz","Heatmor","Durant",
                                "Deino","Zweilous","Hydreigon","Larvesta","Volcarona","Cobalion","Terrakion","Virizion","Tornadus Incarnate Forme",
                                "Tornadus Therian Forme","Thundurus Incarnate Forme","Thundurus Therian Forme","Reshiram","Zekrom","Landorus Incarnate Forme",
                                "Landorus Therian Forme","Kyurem","Kyurem Black Kyurem","Kyurem White Kyurem","Keldeo Ordinary Forme","Keldeo Resolute Forme",
                                "Meloetta Aria Forme","Meloetta Pirouette Forme","Genesect","Chespin","Quilladin","Chesnaught","Fennekin","Braixen",
                                "Delphox","Froakie","Frogadier","Greninja","Bunnelby","Diggersby","Fletchling","Fletchinder","Talonflame","Scatterbug","Spewpa",
                                "Vivillon","Litleo","Pyroar","Flabébé","Floette","Florges","Skiddo","Gogoat","Pancham","Pangoro","Furfrou","Espurr","Meowstic Male",
                                "Meowstic Female","Honedge","Doublade","Aegislash Blade Forme","Aegislash Shield Forme","Spritzee","Aromatisse","Swirlix","Slurpuff",
                                "Inkay","Malamar","Binacle","Barbaracle","Skrelp","Dragalge","Clauncher","Clawitzer","Helioptile","Heliolisk","Tyrunt",
                                "Tyrantrum","Amaura","Aurorus","Sylveon","Hawlucha","Dedenne","Carbink","Goomy","Sliggoo","Goodra","Klefki","Phantump","Trevenant",
                                "Pumpkaboo Average Size","Pumpkaboo Small Size","Pumpkaboo Large Size","Pumpkaboo Super Size","Gourgeist Average Size",
                                "Gourgeist Small Size","Gourgeist Large Size","Gourgeist Super Size","Bergmite","Avalugg","Noibat","Noivern","Xerneas",
                                "Yveltal","Zygarde Half Forme","Diancie","Mega Diancie","Hoopa Confined","Hoopa Unbound","Volcanion"))

image = Image.open('photos/pokeball.png')
image1 = Image.open("pokemon/"+first_pokemon+".png")
image2 = Image.open("pokemon/"+second_pokemon+".png")

#col11, col22, col33 , col44, col55 = st.columns([2, 4, 3.5, 1, 2.5])
col22, col33 , col44= st.columns([2,1,2])

with col22:
    st.image(image1, width=250)
with col44:
    st.image(image2, width=250)
with col33 :
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")

    st.image(image, width=100)
    st.write(" ")
    st.write(" ")
    st.write(" ")

    button1 = st.button('Fight')

st.write('<hr>',unsafe_allow_html=True  )


df_combat = pd.DataFrame([[first_pokemon,second_pokemon]],
columns= ['First_pokemon','Second_pokemon'])

df_combat_copie = df_combat.copy()

df_combat_copie['First_pokemon_type1'] = df_combat_copie['First_pokemon'].replace(dict_type1)
df_combat_copie['First_pokemon_type2'] = df_combat_copie['First_pokemon'].replace(dict_type2)
df_combat_copie['First_pokemon_HP'] = df_combat_copie['First_pokemon'].replace(dict_HP)
df_combat_copie['First_pokemon_Attack'] = df_combat_copie['First_pokemon'].replace(dict_Attack)
df_combat_copie['First_pokemon_Defense'] = df_combat_copie['First_pokemon'].replace(dict_Defense)
df_combat_copie['First_pokemon_Atq_speciale'] = df_combat_copie['First_pokemon'].replace(dict_Atq_speciale)
df_combat_copie['First_pokemon_Def_speciale'] = df_combat_copie['First_pokemon'].replace(dict_Def_speciale)
df_combat_copie['First_pokemon_vitesse'] = df_combat_copie['First_pokemon'].replace(dict_vitesse)
df_combat_copie['First_pokemon_victoire'] = df_combat_copie['First_pokemon'].replace(dict_victoire)
df_combat_copie['First_pokemon_ratio'] = df_combat_copie['First_pokemon'].replace(dict_ratio)
df_combat_copie['First_pokemon_gen'] = df_combat_copie['First_pokemon'].replace(dict_gen)
df_combat_copie['First_pokemon_leg'] = df_combat_copie['First_pokemon'].replace(dict_leg)

df_combat_copie['Second_pokemon_type1'] = df_combat_copie['Second_pokemon'].replace(dict_type1)
df_combat_copie['Second_pokemon_type2'] = df_combat_copie['Second_pokemon'].replace(dict_type2)
df_combat_copie['Second_pokemon_HP'] = df_combat_copie['Second_pokemon'].replace(dict_HP)
df_combat_copie['Second_pokemon_Attack'] = df_combat_copie['Second_pokemon'].replace(dict_Attack)
df_combat_copie['Second_pokemon_Defense'] = df_combat_copie['Second_pokemon'].replace(dict_Defense)
df_combat_copie['Second_pokemon_Atq_speciale'] = df_combat_copie['Second_pokemon'].replace(dict_Atq_speciale)
df_combat_copie['Second_pokemon_Def_speciale'] = df_combat_copie['Second_pokemon'].replace(dict_Def_speciale)
df_combat_copie['Second_pokemon_vitesse'] = df_combat_copie['Second_pokemon'].replace(dict_vitesse)
df_combat_copie['Second_pokemon_victoire'] = df_combat_copie['Second_pokemon'].replace(dict_victoire)
df_combat_copie['Second_pokemon_ratio'] = df_combat_copie['Second_pokemon'].replace(dict_ratio)
df_combat_copie['Second_pokemon_gen'] = df_combat_copie['Second_pokemon'].replace(dict_gen)
df_combat_copie['Second_pokemon_leg'] = df_combat_copie['Second_pokemon'].replace(dict_leg)

dropCols_new2 = ['First_pokemon', 'Second_pokemon', 'First_pokemon_type1', 'First_pokemon_type2', 'Second_pokemon_type1', 'Second_pokemon_type2',
                 'Second_pokemon_gen', 'Second_pokemon_leg', 'First_pokemon_gen', 'First_pokemon_leg']
df_test_copie = df_combat_copie.drop(dropCols_new2, axis=1)

model = pickle.load(open('best_model.pkl', 'rb')) 

prediction = model.predict(df_test_copie)

df_test_new = df_combat.copy()

df_test_new['First Win'] = prediction

gagnant = pd.DataFrame(df_test_new.apply(lambda x: x["First_pokemon"] if x["First Win"]==1 else x["Second_pokemon"], axis=1), columns=["Winner"])

df_test_new = pd.concat([df_test_new, gagnant], axis=1)

df_test_new = df_test_new.drop('First Win', axis=1)

noms_pokemon = dict(zip(df_pokemon_1['ID'], df_pokemon_1['Name']))
colonne = ['First_pokemon', 'Second_pokemon', 'Winner']
df_combat_nom = df_test_new[colonne].replace(noms_pokemon)

col_pok1 = st.columns(2)



if button1:
    st.write('<hr>',unsafe_allow_html=True  )
    with col_pok1[0]:
      st.write('<center><h3>',df_combat_nom.iloc[0]['First_pokemon'],'</h3></center>', unsafe_allow_html=True )
      st.write('<center><p>Score de victoire : <strong>',  str(round(df_test_copie.iloc[0]['First_pokemon_ratio'], 3)), '</strong></p></center>', unsafe_allow_html=True)
      st.write('<center><p>Pokémon de la génération <strong>', str(df_combat_copie.iloc[0]['First_pokemon_gen']), '</strong></p></center>', unsafe_allow_html=True)
      if(df_combat_copie.iloc[0]['First_pokemon_leg']==False) :
          st.write("<center><p>Ce n'est pas un pokémon légendaire</p></center>", unsafe_allow_html=True)
      else : 
          st.write("<center><p>Il s'agit d'un pokémon légendaire</p></center>", unsafe_allow_html=True)

    with col_pok1[1]:
      st.write('<center><h3>', df_combat_nom.iloc[0]['Second_pokemon'], '</h3></center>',unsafe_allow_html=True  )
      st.write('<center><p>Score de victoire : <strong>', str(round(df_test_copie.iloc[0]['Second_pokemon_ratio'], 3)), '</strong></p></center>', unsafe_allow_html=True)
      st.write('<center><p>Pokémon de la génération <strong>', str(df_combat_copie.iloc[0]['Second_pokemon_gen']), '</strong></p></center>', unsafe_allow_html=True)
      if(df_combat_copie.iloc[0]['Second_pokemon_leg']==False) :
          st.write("<center><p>Ce n'est pas un pokémon légendaire</p></center>", unsafe_allow_html=True)
      else : 
          st.write("<center><p>Il s'agit d'un pokémon légendaire</p></center>", unsafe_allow_html=True)

    st.write('<center><p class="big-font">Le vainqueur du combat est<b> ', df_combat_nom.iloc[0]['Winner'], '</b></p></center>',unsafe_allow_html=True)
    st.write('<hr>',unsafe_allow_html=True  )


##################### GRAPHIQUE RADAR CHART
####PREMIER POKEMON
df_combat_graph = df_combat_copie.copy()
dropCols_poke1 = ['First_pokemon', 'Second_pokemon', 'First_pokemon_type1', 'First_pokemon_type2', 'Second_pokemon_type1', 'Second_pokemon_type2',
            'Second_pokemon_HP', 'Second_pokemon_Attack', 'Second_pokemon_Defense', 'Second_pokemon_Atq_speciale','Second_pokemon_Def_speciale',
            'Second_pokemon_vitesse', 'Second_pokemon_ratio', 'Second_pokemon_victoire', 'First_pokemon_victoire','First_pokemon_ratio',
            'Second_pokemon_gen', 'Second_pokemon_leg', 'First_pokemon_gen', 'First_pokemon_leg']
df_poke_best_poke1 = df_combat_graph.drop(dropCols_poke1, axis=1)

df_poke_best_poke1.rename(columns = {'First_pokemon_HP' : 'PV' , 'First_pokemon_Attack' : 'Attaque', 'First_pokemon_Defense' : 'Defense', 'First_pokemon_Atq_speciale' : 'Atq. Speciale','First_pokemon_Def_speciale' : 'Def. Speciale', "First_pokemon_vitesse" : "Vitesse"}, inplace = True)

value_best_poke1 = df_poke_best_poke1.values[0]
value_best_poke1 = value_best_poke1.tolist()
index_best_poke1 = list(df_poke_best_poke1.columns)

####DEUXIÈME POKEMON
df_combat_graph_2 = df_combat_copie.copy()
dropCols_poke2 = ['First_pokemon', 'Second_pokemon', 'First_pokemon_type1', 'First_pokemon_type2', 'Second_pokemon_type1', 'Second_pokemon_type2',
            'First_pokemon_HP', 'First_pokemon_Attack', 'First_pokemon_Defense', 'First_pokemon_Atq_speciale','First_pokemon_Def_speciale',
            'First_pokemon_vitesse', 'Second_pokemon_ratio', 'First_pokemon_victoire','First_pokemon_ratio', 'Second_pokemon_victoire',
            'Second_pokemon_gen', 'Second_pokemon_leg', 'First_pokemon_gen', 'First_pokemon_leg']
df_poke_best_poke2 = df_combat_graph_2.drop(dropCols_poke2, axis=1)

df_poke_best_poke2.rename(columns = {'Second_pokemon_HP' : 'PV' , 'Second_pokemon_Attack' : 'Attaque', 'Second_pokemon_Defense' : 'Defense', 'Second_pokemon_Atq_speciale' : 'Atq. Speciale','Second_pokemon_Def_speciale' : 'Def. Speciale', 'Second_pokemon_vitesse' : 'Vitesse'}, inplace = True)

value_best_poke2 = df_poke_best_poke2.values[0]
value_best_poke2 = value_best_poke2.tolist()
index_best_poke2 = list(df_poke_best_poke2.columns)

fig = go.Figure()

fig.add_trace(go.Scatterpolar(
      r=df_poke_best_poke1.values[0],
      theta=index_best_poke1,
      fill='toself',
      fillcolor = 'lightsteelblue',
      name= df_combat_nom.iloc[0]['First_pokemon']
))
fig.add_trace(go.Scatterpolar(
      r=df_poke_best_poke2.values[0],
      theta=index_best_poke2,
      fill='toself',
      name=df_combat_nom.iloc[0]['Second_pokemon']
))

fig.update_layout(
  title={
        'text': ("Statistiques de "+df_combat_nom.iloc[0]['First_pokemon']+" et "+df_combat_nom.iloc[0]['Second_pokemon']),
        'y':0.9,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
  showlegend=True,
  width=400,
  height=400,
  polar=dict(
    radialaxis=dict(
      color="black",
      visible=True)),
  font=dict(
        size=11,
        color="white"
    )
)


left, middle, right = st.columns((2, 5, 2))
with middle:
  radar_chart = st.write(fig)
#####################
