from django.core.management.base import BaseCommand

from core.models import Character, Ship


DATA = [
    {"name": "Luke Skywalker", "species": "Human", "homeworld": "Tatooine", "bio": "A farmboy who became a Jedi Knight and helped overthrow the Empire.", "ship": {"name": "X-wing Red Five", "model": "T-65 X-wing"}},
    {"name": "Leia Organa", "species": "Human", "homeworld": "Alderaan", "bio": "Princess, senator and leader in the Rebel Alliance; skilled diplomat and commander.", "ship": {"name": "Leia's Escort", "model": "Consular-class cruiser"}},
    {"name": "Han Solo", "species": "Human", "homeworld": "Corellia", "bio": "Smuggler turned hero, captain of the Millennium Falcon and a leader in the Rebellion.", "ship": {"name": "Millennium Falcon", "model": "YT-1300f light freighter"}},
    {"name": "Chewbacca", "species": "Wookiee", "homeworld": "Kashyyyk", "bio": "Loyal Wookiee warrior and Han Solo's copilot and friend.", "ship": {"name": "Millennium Falcon (copilot)", "model": "YT-1300f"}},
    {"name": "Obi-Wan Kenobi", "species": "Human", "homeworld": "Stewjon", "bio": "Jedi Master who mentored Anakin and Luke Skywalker; known for wisdom and sacrifice.", "ship": {"name": "Jedi Starfighter", "model": "Delta-7 Aethersprite"}},
    {"name": "Anakin Skywalker", "species": "Human", "homeworld": "Tatooine", "bio": "Powerful Jedi Knight who fell to the dark side and became Darth Vader.", "ship": {"name": "Anakin's Starfighter", "model": "Eta-2 Actis-class"}},
    {"name": "Padme Amidala", "species": "Human", "homeworld": "Naboo", "bio": "Queen and later senator of Naboo; advocate for peace and democracy.", "ship": {"name": "Naboo Royal Starship", "model": "Naboo royal starship"}},
    {"name": "Yoda", "species": "Unknown", "homeworld": "Unknown", "bio": "Legendary Jedi Master noted for wisdom, powerful use of the Force and unique speech.", "ship": {"name": "Jedi Council Transport", "model": "Jedi shuttle"}},
    {"name": "Emperor Palpatine", "species": "Human", "homeworld": "Naboo", "bio": "Politician who secretly became the Sith Lord Emperor, ruling the Galactic Empire.", "ship": {"name": "Imperial Shuttle", "model": "Sith shuttle"}},
    {"name": "Darth Vader", "species": "Human (cyborg)", "homeworld": "Tatooine", "bio": "Once Anakin Skywalker, a Jedi who became the dark enforcer of the Empire.", "ship": {"name": "Vader's TIE Advanced", "model": "TIE Advanced x1"}},

    {"name": "Boba Fett", "species": "Human", "homeworld": "Kamino", "bio": "Renowned bounty hunter known for his armor and pursuit of bounties.", "ship": {"name": "Slave I", "model": "Firespray-class patrol craft"}},
    {"name": "Jango Fett", "species": "Human", "homeworld": "Mandalore", "bio": "Famous bounty hunter and genetic template for the Clone Army.", "ship": {"name": "Jango's Firespray", "model": "Firespray-class"}},
    {"name": "Lando Calrissian", "species": "Human", "homeworld": "Socorro", "bio": "Gambler, entrepreneur and later Rebel Alliance leader; once owner of the Falcon.", "ship": {"name": "Lando's Gambit", "model": "Modified YT-1300"}},
    {"name": "Wedge Antilles", "species": "Human", "homeworld": "Corellia", "bio": "Veteran starfighter pilot who played key roles in major battles for the Rebellion.", "ship": {"name": "Red Two X-wing", "model": "T-65 X-wing"}},
    {"name": "Poe Dameron", "species": "Human", "homeworld": "Yavin 4", "bio": "Ace Resistance pilot known for bravery and flying skill.", "ship": {"name": "Black One", "model": "T-70 X-wing"}},
    {"name": "Finn", "species": "Human", "homeworld": "Unknown", "bio": "Former First Order stormtrooper who defected and fought for the Resistance.", "ship": {"name": "Resistance Transport", "model": "U-wing"}},
    {"name": "Rey", "species": "Human", "homeworld": "Jakku", "bio": "Scavenger who became a powerful Force user and helped defeat the First Order.", "ship": {"name": "Rey's Speeder", "model": "MPC-0A Interceptor"}},
    {"name": "Kylo Ren", "species": "Human", "homeworld": "Chandrila", "bio": "A conflicted dark-side user, heir to Skywalker lineage and leader in the First Order.", "ship": {"name": "TIE Silencer", "model": "TIE/fo"}},
    {"name": "Supreme Leader Snoke", "species": "Unknown", "homeworld": "Unknown", "bio": "Mysterious dark-side leader of the First Order.", "ship": {"name": "Snoke's Transport", "model": "First Order command ship"}},
    {"name": "Captain Phasma", "species": "Human", "homeworld": "Parnassos", "bio": "Elite stormtrooper commander known for chrome armor and discipline.", "ship": {"name": "Phasma's Shuttle", "model": "First Order shuttle"}},

    {"name": "Admiral Ackbar", "species": "Mon Calamari", "homeworld": "Mon Cala", "bio": "Rebel Alliance admiral celebrated for tactical leadership.", "ship": {"name": "Home One", "model": "Mon Calamari cruiser"}},
    {"name": "Mon Mothma", "species": "Human", "homeworld": "Chandrila", "bio": "Political leader who helped organize and lead the Rebel Alliance.", "ship": {"name": "Senate Transport", "model": "Consular-class"}},
    {"name": "Grand Moff Tarkin", "species": "Human", "homeworld": "Eriadu", "bio": "Ruthless Imperial governor who commanded the Death Star.", "ship": {"name": "Tarkin's Escort", "model": "Imperial Star Destroyer"}},
    {"name": "Jyn Erso", "species": "Human", "homeworld": "Vallis", "bio": "Rebel operative crucial to acquiring the Death Star plans.", "ship": {"name": "Jyn's Transport", "model": "U-wing"}},
    {"name": "Cassian Andor", "species": "Human", "homeworld": "Fest", "bio": "Rebel intelligence officer who took great risks for the cause.", "ship": {"name": "Cassian's Shuttle", "model": "Rebel transport"}},

    {"name": "K-2SO", "species": "Droid", "homeworld": "Factory", "bio": "Reprogrammed Imperial security droid with a blunt sense of humor.", "ship": {"name": "Droid Carrier", "model": "Service craft"}},
    {"name": "R2-D2", "species": "Droid", "homeworld": "Naboo", "bio": "Resourceful astromech droid who aided heroes across generations.", "ship": {"name": "Astromech Dock", "model": "Various starfighters"}},
    {"name": "C-3PO", "species": "Droid", "homeworld": "Tatooine (assembled)", "bio": "Protocol droid fluent in many languages, serving allies faithfully.", "ship": {"name": "Protocol Case", "model": "N/A"}},
    {"name": "BB-8", "species": "Droid", "homeworld": "Unknown", "bio": "Loyal astromech to Poe Dameron and a brave companion in the Resistance.", "ship": {"name": "BB-8 Dock", "model": "Resistance craft"}},
    {"name": "Jabba the Hutt", "species": "Hutt", "homeworld": "Nal Hutta", "bio": "Powerful crime lord who controlled a wide criminal network.", "ship": {"name": "Hutt Barge", "model": "Hutt barge"}},

    {"name": "Ahsoka Tano", "species": "Togruta", "homeworld": "Shili", "bio": "Former Jedi apprentice turned independent warrior and leader.", "ship": {"name": "Ahsoka's Shuttle", "model": "Shuttle"}},
    {"name": "Ezra Bridger", "species": "Human", "homeworld": "Lothal", "bio": "Force-sensitive who grew into a Rebel leader and key operative.", "ship": {"name": "Ghost", "model": "VCX-100 light freighter"}},
    {"name": "Hera Syndulla", "species": "Twi'lek", "homeworld": "Ryloth", "bio": "Pilot and leader of the Ghost crew; skilled commander.", "ship": {"name": "Ghost", "model": "VCX-100"}},
    {"name": "Sabine Wren", "species": "Human", "homeworld": "Mandalore", "bio": "Mandalorian artist, explosives expert and Rebel fighter.", "ship": {"name": "Sabine's Craft", "model": "Stealth shuttle"}},
    {"name": "Kanan Jarrus", "species": "Human", "homeworld": "Cantonica", "bio": "Jedi survivor who trained Ezra and fought for freedom.", "ship": {"name": "Blade of the Phoenix", "model": "Gunship"}},

    {"name": "Grand Admiral Thrawn", "species": "Chiss", "homeworld": "Csilla", "bio": "Tactical mastermind who rose to prominence in the Empire.", "ship": {"name": "Chimaera", "model": "Imperial Star Destroyer"}},
    {"name": "Orson Krennic", "species": "Human", "homeworld": "Alderaan", "bio": "Ambitious Director of Advanced Weapons for the Empire.", "ship": {"name": "Krennic's Shuttle", "model": "T-4a shuttle"}},
    {"name": "Galen Erso", "species": "Human", "homeworld": "Corellia", "bio": "Scientist coerced into contributing to the Death Star's development.", "ship": {"name": "Research Vessel", "model": "Laboratory shuttle"}},
    {"name": "Bodhi Rook", "species": "Human", "homeworld": "Jedha", "bio": "Imperial pilot who defected to the Rebellion and aided the cause.", "ship": {"name": "Rebel Transport", "model": "Cargo shuttle"}},
    {"name": "Chirrut Îmwe", "species": "Human", "homeworld": "Jedha", "bio": "Devout warrior guided by faith in the Force; skilled combatant.", "ship": {"name": "Chirrut's Skiff", "model": "Light skiff"}},

    {"name": "Baze Malbus", "species": "Human", "homeworld": "Jedha", "bio": "Battle-hardened protector and ally of Chirrut.", "ship": {"name": "Guardian Craft", "model": "Support skiff"}},
    {"name": "Wicket", "species": "Ewok", "homeworld": "Endor", "bio": "Ewok who helped the Rebels during the Battle of Endor.", "ship": {"name": "Ewok Glider", "model": "Tribal craft"}},
    {"name": "Nien Nunb", "species": "Sullustan", "homeworld": "Sullust", "bio": "Skilled pilot who co-piloted at key Rebel victories.", "ship": {"name": "Support Fighter", "model": "Multi-role craft"}},
    {"name": "Biggs Darklighter", "species": "Human", "homeworld": "Tatooine", "bio": "Friend of Luke and Rebel pilot who fought at Yavin.", "ship": {"name": "Biggs's X-wing", "model": "T-65 X-wing"}},

    {"name": "Plo Koon", "species": "Kel Dor", "homeworld": "Dorin", "bio": "Respected Jedi Master and General in the Clone Wars.", "ship": {"name": "Jedi Cruiser", "model": "Delta-7 variant"}},
    {"name": "Kit Fisto", "species": "Nautolan", "homeworld": "Glee Anselm", "bio": "Jedi Master skilled in lightsaber combat, especially underwater.", "ship": {"name": "Nautolan Transport", "model": "Jedi shuttle"}},
    {"name": "Mace Windu", "species": "Human", "homeworld": "Haruun Kal", "bio": "Powerful Jedi Master and Council member, known for leadership.", "ship": {"name": "Council Shuttle", "model": "Jedi transport"}},
    {"name": "Count Dooku", "species": "Human", "homeworld": "Serenno", "bio": "Former Jedi turned Sith Lord who led Separatist forces.", "ship": {"name": "Dooku's Yacht", "model": "Solar Sailer"}},
    {"name": "General Grievous", "species": "Kaleesh (cyborg)", "homeworld": "Kalee", "bio": "Cyborg commander noted for hunting Jedi and skilled combat.", "ship": {"name": "Invisible Hand", "model": "Providence-class cruiser"}},

    {"name": "Qui-Gon Jinn", "species": "Human", "homeworld": "Coruscant", "bio": "Maverick Jedi Master who followed the living Force and trained Obi-Wan.", "ship": {"name": "Queen's Starship", "model": "Naboo starfighter"}},
    {"name": "Dengar", "species": "Human", "homeworld": "Corellia", "bio": "Ruthless bounty hunter known for tenacity in the field.", "ship": {"name": "Dengar's Skiff", "model": "Bounty skiff"}},
    {"name": "Bossk", "species": "Trandoshan", "homeworld": "Trandosha", "bio": "Reptilian bounty hunter feared for hunting skills.", "ship": {"name": "Bossk's Runner", "model": "Heavy skiff"}},
    {"name": "IG-88", "species": "Droid", "homeworld": "Unknown", "bio": "Assassin droid turned bounty hunter with deadly efficiency.", "ship": {"name": "IG Craft", "model": "Droid carrier"}},

    {"name": "Zam Wesell", "species": "Clawdite", "homeworld": "Zolan", "bio": "Shape-shifting bounty hunter involved in clandestine plots.", "ship": {"name": "Zam's Skiff", "model": "Stealth skiff"}},
    {"name": "Greedo", "species": "Rodian", "homeworld": "Rodia", "bio": "Bounty hunter who encountered Han Solo in Mos Eisley.", "ship": {"name": "Greedo's Scout", "model": "Light freighter"}},
    {"name": "Watto", "species": "Toydarian", "homeworld": "Toydaria", "bio": "Tatooine junk dealer who owned Anakin and Shmi Skywalker.", "ship": {"name": "Watto's Cart", "model": "Trader barge"}},
    {"name": "Nute Gunray", "species": "Neimoidian", "homeworld": "Neimoidia", "bio": "Viceroy of the Trade Federation who plotted during the Clone Wars.", "ship": {"name": "Trade Federation Vessel", "model": "Droid control ship"}},

    {"name": "Shmi Skywalker", "species": "Human", "homeworld": "Tatooine", "bio": "Mother of Anakin Skywalker who protected him as best she could.", "ship": {"name": "Tatooine Cart", "model": "Local transport"}},
    {"name": "Owen Lars", "species": "Human", "homeworld": "Tatooine", "bio": "Moisture farmer who raised Luke with Beru on Tatooine.", "ship": {"name": "Moisture Wagon", "model": "Local freighter"}},
    {"name": "Beru Whitesun Lars", "species": "Human", "homeworld": "Tatooine", "bio": "Kind caretaker who helped raise Luke Skywalker.", "ship": {"name": "Farm Cart", "model": "Tatooine wagon"}},

    {"name": "Rose Tico", "species": "Human", "homeworld": "Unknown", "bio": "Maintenance worker turned Resistance fighter dedicated to her comrades.", "ship": {"name": "Resistance Transport", "model": "Gunship"}},
    {"name": "Snap Wexley", "species": "Human", "homeworld": "Unknown", "bio": "Resistance pilot and veteran of the later conflicts.", "ship": {"name": "Rogue Support", "model": "X-wing variant"}},
    {"name": "Admiral Rae Sloane", "species": "Human", "homeworld": "Unknown", "bio": "Senior officer who rose through Imperial and First Order ranks.", "ship": {"name": "Sloane's Flagship", "model": "Command cruiser"}},
    {"name": "Maz Kanata", "species": "Unknown", "homeworld": "Takodana", "bio": "Ancient being who sheltered and advised many heroes.", "ship": {"name": "Maz's Caravan", "model": "Transport"}},

    {"name": "L3-37", "species": "Droid", "homeworld": "Unknown", "bio": "Self-aware droid and activist for droid rights; modified a freighter's systems.", "ship": {"name": "L3's Mod", "model": "Modified freighter"}},
    {"name": "Qi'ra", "species": "Human", "homeworld": "Corellia", "bio": "Underworld figure with complex loyalties and ambition.", "ship": {"name": "Corellian Transport", "model": "Smuggler's craft"}},
    {"name": "Tobias Beckett", "species": "Human", "homeworld": "Unknown", "bio": "Criminal mentor who taught skills to a young Han Solo.", "ship": {"name": "Beckett's Run", "model": "Light freighter"}},
    {"name": "Dryden Vos", "species": "Human", "homeworld": "Unknown", "bio": "Wealthy crime lord who led Crimson Dawn.", "ship": {"name": "Vos's Yacht", "model": "Luxury cruiser"}},

    {"name": "Moff Gideon", "species": "Human", "homeworld": "Unknown", "bio": "Former Imperial officer who sought powerful artifacts after the Empire's fall.", "ship": {"name": "Gideon's Cruiser", "model": "Imperial gunship"}},
    {"name": "Din Djarin", "species": "Human", "homeworld": "Mandalore (by creed)", "bio": "Mandalorian bounty hunter who becomes Grogu's protector.", "ship": {"name": "Razor Crest", "model": "Gunslinger-class"}},
    {"name": "Grogu", "species": "Unknown", "homeworld": "Unknown", "bio": "A Force-sensitive Child protected by the Mandalorian.", "ship": {"name": "Grogu's Pod", "model": "N/A"}},
    {"name": "Cara Dune", "species": "Human", "homeworld": "Denum", "bio": "Former shock trooper turned lawkeeper and ally to the Mandalorian.", "ship": {"name": "Shock Troop Shuttle", "model": "Transport"}},

    {"name": "Bo-Katan Kryze", "species": "Human", "homeworld": "Mandalore", "bio": "Mandalorian leader who seeks to restore Mandalore's legacy.", "ship": {"name": "Mandalorian Cruiser", "model": "Kryze class"}},
    {"name": "Aayla Secura", "species": "Togruta", "homeworld": "Ryloth", "bio": "Jedi Knight who fought in the Clone Wars.", "ship": {"name": "Jedi Cruiser", "model": "Jedi transport"}},
    {"name": "Shaak Ti", "species": "Togruta", "homeworld": "Shili", "bio": "Jedi Master who served on the Jedi Council during turbulent times.", "ship": {"name": "Council Vessel", "model": "Jedi shuttle"}},
    {"name": "Admiral Piett", "species": "Human", "homeworld": "Alderaan", "bio": "Imperial officer who served under Vader and Tarkin with distinction.", "ship": {"name": "Star Destroyer Piett", "model": "Imperial Star Destroyer"}},

    {"name": "General Hux", "species": "Human", "homeworld": "Arkanis", "bio": "Fanatical First Order officer and political rival within the regime.", "ship": {"name": "Hux's Command", "model": "First Order destroyer"}},
    {"name": "Paige Tico", "species": "Human", "homeworld": "D'Qar", "bio": "Resistance gunner who fought bravely in the later conflicts.", "ship": {"name": "Resistance Gunship", "model": "Crait transport"}},
    {"name": "Greef Karga", "species": "Human", "homeworld": "Nevarro", "bio": "Leader of the bounty hunter guild who later allied with the Mandalorian.", "ship": {"name": "Guild Transport", "model": "Transport"}},
    {"name": "IG-11", "species": "Droid", "homeworld": "Unknown", "bio": "Bounty hunter droid reprogrammed to serve as a protector.", "ship": {"name": "Droid Carrier", "model": "Service craft"}},
    {"name": "Lor San Tekka", "species": "Human", "homeworld": "Taanab", "bio": "Collector of artifacts and ally to the Resistance.", "ship": {"name": "Tekka's Vessel", "model": "Light transport"}},
    {"name": "Phalanx", "species": "Droid", "homeworld": "Unknown", "bio": "Combat droid deployed across Imperial and post-Imperial forces.", "ship": {"name": "Phalanx Shuttle", "model": "Combat transport"}},
]


class Command(BaseCommand):
    help = "Populate the DB with 82 curated Star Wars characters and a ship each."

    def handle(self, *args, **options):
        created = 0
        for item in DATA:
            name = item["name"]
            defaults = {
                "species": item.get("species", ""),
                "homeworld": item.get("homeworld", ""),
                "bio": item.get("bio", ""),
            }
            char, was_created = Character.objects.get_or_create(name=name, defaults=defaults)
            if was_created:
                created += 1

            ship_info = item.get("ship", {})
            ship_name = ship_info.get("name", f"Ship of {name}")
            ship_defaults = {"model": ship_info.get("model", "")}
            Ship.objects.get_or_create(name=ship_name, owner=char, defaults=ship_defaults)

        self.stdout.write(self.style.SUCCESS(f"Population complete. Characters created: {created}"))

