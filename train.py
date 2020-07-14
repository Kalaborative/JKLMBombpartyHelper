from random import choice, shuffle

set_words_1 = ["sifaka", "scissortail", "scutella", "reseau", "mudejar", "brachyurous", "voulge", "chlorophytum", "sciamachy",
    "eleutherarch", "plumbum", "azulejos", "wharepuni", "zooxanthellae", "durchkomponiert", "avuncularities", "quaquaversally",
    "saibling", "agammaglobulinemia", "hoactzines", "ozokerites", "kingklips", "kydst", "dreamholes", "wingchairs", "jarlsberg",
    "jnanas", "bitchfest", "tooarts", "zoysia", "chechaquos", "assythment", "sulfinpyrazone"
]

set_words_2 = ["synecphonesis", "chickenshit", "gimcrackeries", "splendiferously", "zeuglodont", "dysgraphia", "tchoukball", "zinziberaceous",
    "blanchisseuse", "kestrel", "skeuomorphic", "prolegomenon", "puftaloonies", "zareeba", "psychogalvanic", "microspectrophotometers", "jerque",
    "braunschweiger", "bildungsromane", "shillingsworth", "hobbledehoyhood", "cunjevois", "caatinga", "slumpflationary",
    "countercountermeasures", "middelmannetjie", "thalassaemia", "machzor", "thermojunction", "akratic", "weltanschauungen", "madrassah",
    "electrodesiccation", "gewurztraminer", "ethylenediaminetetraacetates"
]

set_words_3 = ["counterdemonstrations", "counterretaliations", "kohutuhutu", "woollybutt", "floccinaucinihilipilification", "bremsstrahlungs",
    "skrimshankers", "vichyssoises", "schutzstaffels", "kinnikinnicks", "kolkhozniki", "andouillettes", "gesellschaften", "mangoldwurzel",
    "femtoseconds", "dvornik", "syncroflash", "zabaglione", "shabracque", "rijksdaalers", "affenpinschers", "spitchcocking", "slipshoddiness"
]

set_words_4 = ["superbitches", "sonofabitch", "cleverdicks", "sharksucker", "autosuggestions", "merchantabilities", "apneustic", "foolhardiness",
    "staminiferous", "scordatura", "skeletonizers", "hyperemotional", "softheartedness", "melongene", "bouleversements", "spruik",
    "antineutrino", "forhooied", "phosphoenolpyruvates", "trouvailles", "kuvaszok", "standpattism", "britzska", "electroluminescent",
    "chalumeaux", "kowhaiwhai", "quidditative", "gelandesprungs", "fatbrained", "kalamkari", "schizognathous", "ginkgos"
]

set_words_5 = ["pseudopseudohypoparathyroidism", "morganite", "crosslinguistically", "hemidemisemiquaver", "anisotropic", "sliversmithing",
    "flagellomania", "isoimmunisation", "zhomo", "symmetrophobia", "quattuordecillion", "keratoconjunctivitises", "eisteddfodau", "ravigottes",
    "wiltjas", "drunkathons", "diphtheroid", "diphenhydramine", "quinquereme", "pancreatectomized", "exsiccant", "amissibility",
    "zingari", "propylitize", "defeasance", "demulcent", "jacqueries", "definitivenesses", "brachiocephalic", "eschscholtzia", "rijsttafel"
]

set_words_6 = ["immunoelectrophoreses", "hexakosioihexekontahexaphobia", "orthogonalization", "abcoulomb", "carnivalesque", "strandwolf", "sunworshippers",
    "jigamaree", "abortifacient", "polemonium", "superpatriotic", "tokoloshis", "stockjobbery", "sesquialtera", "pseudovector", "bumfluff", "perique", 
    "frondescence", "struthious", "mijnheer", "quadrivalences", "exculpation", "bougainvillaeas", "staffage", "beaverboard", "ampullosity",
    "seldseen", "alphabetiform", "phlegmatic", "pseudonymously", "sprachgefuhl"
]

set_words_7 = ["adventitia", "shiatsu", "meshuggenahs", "primogeniture", "aefauld", "henpeckery", "satrapies", "arrasene",
    "hemelytra", "euouaes", "duomo", "jackshafts", "antherozoids", "luteolins", "proudhearted", "sultanates", "outblustering",
    "cytotechnologists", "crummacks", "quodlibetarian", "mucronations", "deinothere", "diamantiferous", "spacefarings", "sashays",
    "ultradistant", "metapsychologists", "supersuccessful"
]

letters = list('qwertyuiopasdfghjklzxcvbnm')

with open("sowpods.txt", "r") as wordlist:
    english_dict = wordlist.read().splitlines()
    print("Loading syllables...")
    syllable_list = set()
    for e in english_dict:
        for i in range(len(e)):
            if i < len(e):
                syllable_list.add(e[i-1:i+1]) # for two-letter syllables
                syllable_list.add(e[i-2:i+1]) # for three-letter syllables

    syllable_list = list(syllable_list)

master_training_set = []

def add_to_set(trainingList):
    for t in trainingList:
        master_training_set.append(t)

add_to_set(set_words_1)
add_to_set(set_words_2)
add_to_set(set_words_3)
add_to_set(set_words_4)
add_to_set(set_words_5)
add_to_set(set_words_6)
add_to_set(set_words_7)

def generate_prompt():
    return choice(syllable_list)

while True:
    print("\n")
    custom_prompt = input("Type prompt or hit enter for a random: ")
    if custom_prompt:
        new_prompt = custom_prompt
    else:
        new_prompt = generate_prompt()
    print("Prompt: {}".format(new_prompt))
    solution = input("Type your solution: ")
    if new_prompt in solution:
        if solution in master_training_set:
            print("Nice! You used one of your training words.")
        else:
            matching = [m for m in master_training_set if new_prompt in m]
            if matching:
                print("Missed opportunity! You could have used:")
                for t in matching:
                    print(t)
            else:
                if solution in english_dict:
                    print("Good job! No training words could have been used.")
                else:
                    print("Not a valid word.")
        print("Other example words:")
        matching_from_dict = []
        found = False
        for word in english_dict:
            if new_prompt in word.lower():
                found = True
                matching_from_dict.append(word)
        if not found:
            print("None with this combination")
        else:
            shuffle(matching_from_dict)
            results = matching_from_dict[:3]
            for r in results:
                print(r)
    else:
        print("Word did not match prompt. Moving on!")
        matching = [m for m in master_training_set if new_prompt in m]
        if matching:
            print("Missed opportunity! You could have used:")
            for t in matching:
                print(t)
        print("Other example words:")
        matching_from_dict = []
        found = False
        for word in english_dict:
            if new_prompt in word.lower():
                found = True
                matching_from_dict.append(word)
        if not found:
            print("None with this combination")
        else:
            shuffle(matching_from_dict)
            results = matching_from_dict[:3]
            for r in results:
                print(r)