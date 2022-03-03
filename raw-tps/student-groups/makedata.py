from collections import defaultdict
import random
#from tokenize import group

# from https://www.scarymommy.com/french-last-names/

RAW_LASTS = """
Lavigne
Pronunciation: La-veen-ye
Meaning: Vine.
Monet
Pronunciation: Mon-ay
Meaning: A form of the name Simon, meaning to be heard.
Blanchet
Pronunciation: Blan-shay
Meaning: Blanket or fair-haired person.
Garnier
Pronunciation: Gar-nee-yay
Meaning: Keeper of granary.
Moulin
Pronunciation: Moo-lan
Meaning: Mill/Miller.
Toussaint
Pronunciation: Too-san
Meaning: All saints.
Laurent
Pronunciation: Lor-onn
Meaning: Laurel, which is the name of a leaf powerful leaders wore in their crowns during ancient times.
Dupont
Pronunciation: Dew-pon
Meaning: Of the bridge.
Martin
Pronunciation: Mar-tan
Meaning: Derives from Mars, the Roman god of war.
Boucher
Pronunciation: Boo-shay
Meaning: Butcher.
Bernard
Pronunciation: Bur-Nard
Meaning: Strong brave bear.
Côté
Pronunciation: Coat
Meaning: Someone who lived on a slope or riverbank.
Allard
Pronunciation: Al-arr
Meaning: Noble or hardy.
Chevrolet
Pronunciation: Shev-ro-lay
Meaning: Goatherder.
Moreau
Pronunciation: More-row
Meaning: Dark-skinned.
Corbin
Pronunciation: Cor-ban
Meaning: Little crow or raven.
Dubois
Pronunciation: Dew-bwah
Meaning: Of the forest.
Leroy
Pronunciation: Leer-wah
Meaning: The king.
Cartier
Pronunciation: Cart-ee-yay
Meaning: A carter or transporter of goods.
Duplantier
Pronunciation: Dew-plon-tee-yay
Meaning: Of the plantation or someone who lives near a plantation of trees.
Fournier
Pronunciation: Four-nee-yay
Meaning: Baker.
Beaufort
Pronunciation: Bow-four
Meaning: Beautiful or fair fortress.
Bonnet
Pronunciation: Bon-nay
Meaning: A person who makes or wears hats.
Rousseau
Pronunciation: Roo-so
Meaning: A red-haired person.
Lyon
Pronunciation: Lee-yon
Meaning: A person from the city of Lyon, France.
Granger
Pronunciation: Gran-jay
Meaning: Farm bailiff.
Fontaine
Pronunciation: Fon-ten
Meaning: Fountain.
Chastain
Pronunciation: Shas-tan
Meaning: From the chestnut tree.
Beaumont
Pronunciation: Bow-mon
Meaning: Fair mountain.
Dufort
Pronunciation: Dew-forr
Meaning: Of the fortress.
LaRue
Pronunciation: La-roo
Meaning: Of the street or of the road.
Renaud
Pronunciation: Ren-oh
Meaning: Rule.
Vernier
Pronunciation: Ver-nee-yay
Meaning: Near the alder tree.
Allemand
Pronunciation: Aa-le-mond
Meaning: German.
Couture
Pronunciation: Kou-tur
Meaning: Tailor.
Abadie
Pronunciation: Ah-bah-dee
Meaning: Abbey or family chapel.
Auclair
Pronunciation: Oh-clare
Meaning: Clear.
Bassett
Pronunciation: Bass-set
Meaning: Of lowly origin.
Archambeau
Pronunciation: Are-shem-bow
Meaning: Bold or daring.
Adrien
Pronunciation: Aa-dree-ehn
Meaning: Rich or dark.
Aguillard
Pronunciation: Ag-gee-yah
Meaning: Needle.
Aries
Pronunciation: Air-Reese
Meaning: Constellation.
Abreo
Pronunciation: Aub-rio
Meaning: A wise counselor.
Alarie
Pronunciation: All-lar-ree
Meaning: All-powerful.
Barbier
Pronunciation: Bahr-bee-er
Meaning: Barber.
Baudelaire
Pronunciation: Bohd-l-air
Meaning: Small sword or dagger.
Cadieux
Pronunciation: Cad-jou
Meaning: Little fighter.
Abbe
Pronunciation: A-bey
Meaning: Head of the monastery.
Acord
Pronunciation: A-kord
Meaning: Edge of a sword.
Acy
Pronunciation: As-see
Meaning: Estate of Acius.
Agard
Pronunciation: Ag-gyar
Meaning: Edge of a sword, hardy, or bold.
Blondin
Pronunciation: Blon-da
Meaning: Blonde.
Blouin
Pronunciation: Blue-ah
Meaning: Blue or an unusually pale complexion.
Bloyer
Pronunciation: Bruh-yay
Meaning: Name for someone who separates the fibers of hemp or flax.
Bobier
Pronunciation: Boob-yay
Meaning: A stutterer or stammering.
Boche
Pronunciation: Bosh
Meaning: Cabbage head or square head.
Bodin
Pronunciation: Boo-dah-ng
Meaning: Shelter or one who brings news.
Bohen
Pronunciation: Boo-an
Meaning: Victorious.
Boileau
Pronunciation: Boy-loh
Meaning: To drink or water.
Boire
Pronunciation: Bwar
Meaning: To drink.
Bois
Pronunciation: Bwah
Meaning: Bush, shrub, or undergrowth.
Boisclair
Pronunciation: Bewh-glare
Meaning: Clear wood or light.
Boisseau
Pronunciation: Bweh-so
Meaning: Bushel or measure of grain.
Archambeau
Pronunciation: Ar-shom-boo
Meaning: Bold, daring.
Anouilh
Pronunciation: Ah-noo-ee
Meaning: Slow worm.
Barbeau
Pronunciation: Bar-bo
Meaning: A type of fish; fisherman.
Chalamet
Pronunciation: Shall-ah-may
Meaning: Reed; blowtorch.
Cellier
Pronunciation: Sell-yer
Meaning: Storeroom.
Castillon
Pronunciation: Kaast-ih-yohn
Meaning: Castle.
Chapdelaine
Pronunciation: Chaep-dih-lane
Meaning: Hooded cloak, cape, hat.
D’aureville
Pronunciation: Dor-vill-e
Meaning: Golden village.
Lambert
Pronunciation: LAM-bərt
Meaning: Land.
Tremblay
Pronunciation: Trem-blay
Meaning: Someone who lives near a group of Aspen trees.
"""

# from https://studentsoftheworld.info/penpals/stats.php?Pays=FRA

RAW_FIRSTS = """
1
1501
1.57 %
Marie
1
485
0.51 %
Thomas
2
1398
1.47 %
Camille
2
375
0.39 %
nicolas
3
1398
1.47 %
Léa
3
353
0.37 %
Julien
4
1301
1.36 %
Manon
4
348
0.36 %
QUENTIN
5
1106
1.16 %
Chloé
5
341
0.36 %
Maxime
6
1064
1.12 %
Laura
6
330
0.35 %
Alexandre
7
1050
1.10 %
Julie
7
308
0.32 %
Antoine
8
1033
1.08 %
Sarah
8
293
0.31 %
Kevin
9
992
1.04 %
Pauline
9
287
0.30 %
clement
10
987
1.03 %
Mathilde
10
278
0.29 %
Romain
11
977
1.02 %
Marine
11
260
0.27 %
Pierre
12
841
0.88 %
Emma
12
258
0.27 %
lucas
13
766
0.80 %
Marion
13
247
0.26 %
Florian
14
748
0.78 %
lucie
14
240
0.25 %
GUILLAUME
15
739
0.77 %
Anaïs
15
231
0.24 %
valentin
16
684
0.72 %
Océane
16
217
0.23 %
Jérémy
17
634
0.66 %
Justine
17
207
0.22 %
hugo
18
610
0.64 %
Morgane
18
200
0.21 %
Alexis
19
589
0.62 %
Clara
19
196
0.21 %
anthony
20
571
0.60 %
Charlotte
20
196
0.21 %
Theo
21
571
0.60 %
Juliette
21
195
0.20 %
Paul
22
562
0.59 %
Emilie
22
182
0.19 %
mathieu
23
551
0.58 %
Lisa
23
180
0.19 %
Benjamin
24
522
0.55 %
Mélanie
24
179
0.19 %
ADRIEN
25
517
0.54 %
Elodie
25
167
0.18 %
Vincent
26
503
0.53 %
Claire
26
155
0.16 %
Alex
27
479
0.50 %
Inès
27
153
0.16 %
arthur
28
464
0.49 %
margaux
28
134
0.14 %
Louis
29
463
0.49 %
Alice
29
134
0.14 %
Baptiste
30
462
0.48 %
Amandine
30
130
0.14 %
Dylan
31
459
0.48 %
Audrey
31
127
0.13 %
Corentin
32
452
0.47 %
Louise
32
126
0.13 %
Thibault
33
447
0.47 %
Noémie
33
116
0.12 %
jordan
34
429
0.45 %
Clémence
34
115
0.12 %
Nathan
35
413
0.43 %
Maéva
35
114
0.12 %
Simon
36
412
0.43 %
Melissa
36
114
0.12 %
axel
37
401
0.42 %
Amélie
37
112
0.12 %
Matthieu
38
400
0.42 %
Eva
38
112
0.12 %
léo
39
385
0.40 %
Caroline
39
111
0.12 %
sebastien
40
365
0.38 %
Céline
40
107
0.11 %
Aurélien
41
359
0.38 %
Célia
41
105
0.11 %
victor
42
354
0.37 %
Fanny
42
104
0.11 %
Loïc
43
353
0.37 %
Elise
43
103
0.11 %
Rémi
44
352
0.37 %
Sophie
44
99
0.10 %
Arnaud
45
336
0.35 %
Margot
45
98
0.10 %
tom
46
334
0.35 %
Elisa
46
96
0.10 %
david
47
321
0.34 %
Aurélie
47
94
0.10 %
Jonathan
48
307
0.32 %
Jade
48
93
0.10 %
Damien
49
300
0.31 %
Estelle
49
88
0.09 %
Enzo
50
297
0.31 %
Romane
50
87
0.09 %
Bastien
51
294
0.31 %
Jeanne
51
86
0.09 %
raphael
52
292
0.31 %
ophélie
52
84
0.09 %
Mickael
53
274
0.29 %
Laurine
53
82
0.09 %
François
54
273
0.29 %
Alexandra
54
80
0.08 %
Robin
55
273
0.29 %
Valentine
55
77
0.08 %
martin
56
271
0.28 %
Solène
56
75
0.08 %
Dorian
57
266
0.28 %
lola
57
75
0.08 %
Gabriel
58
260
0.27 %
Coralie
58
75
0.08 %
tristan
59
256
0.27 %
Laëtitia
59
71
0.07 %
Mathis
60
250
0.26 %
Alexia
60
69
0.07 %
Samuel
61
247
0.26 %
Aurore
61
67
0.07 %
Thibaut
62
246
0.26 %
Cécile
62
66
0.07 %
charles
63
245
0.26 %
Alicia
63
66
0.07 %
Benoit
64
244
0.26 %
Zoé
64
65
0.07 %
fabien
65
236
0.25 %
Agathe
65
65
0.07 %
Florent
66
235
0.25 %
Julia
66
64
0.07 %
Maxence
67
233
0.24 %
Anna
67
64
0.07 %
Cédric
68
229
0.24 %
Emeline
68
62
0.06 %
Marc
69
227
0.24 %
Léna
69
61
0.06 %
yann
70
213
0.22 %
Laurie
70
60
0.06 %
Jérôme
71
209
0.22 %
Lou
71
60
0.06 %
steven
72
204
0.21 %
Nina
72
60
0.06 %
Mehdi
73
202
0.21 %
coline
73
59
0.06 %
Gaëtan
74
196
0.21 %
jessica
74
58
0.06 %
Erwan
75
196
0.21 %
Maëlle
75
58
0.06 %
Cyril
76
195
0.20 %
elsa
76
56
0.06 %
jean
77
195
0.20 %
Lucile
77
55
0.06 %
max
78
192
0.20 %
Laure
78
55
0.06 %
rémy
79
192
0.20 %
Salomé
79
55
0.06 %
yanis
80
191
0.20 %
Axelle
80
53
0.06 %
Tony
81
188
0.20 %
Andréa
81
53
0.06 %
Jules
82
183
0.19 %
Charlène
82
53
0.06 %
William
83
182
0.19 %
gaelle
83
46
0.05 %
olivier
84
179
0.19 %
helene
84
46
0.05 %
laurent
85
178
0.19 %
Clementine
85
45
0.05 %
christopher
86
175
0.18 %
Victoria
86
45
0.05 %
sylvain
87
169
0.18 %
myriam
87
43
0.05 %
Ludovic
88
164
0.17 %
éloïse
88
43
0.05 %
Xavier
89
164
0.17 %
heloise
89
41
0.04 %
Stephane
90
164
0.17 %
Cindy
90
41
0.04 %
Tanguy
91
163
0.17 %
Marina
91
40
0.04 %
mael
92
162
0.17 %
Cassandra
92
40
0.04 %
Morgan
93
159
0.17 %
sara
93
40
0.04 %
Adam
94
154
0.16 %
Carla
94
39
0.04 %
Franck
95
152
0.16 %
Ambre
95
38
0.04 %
Grégory
96
150
0.16 %
ludivine
96
38
0.04 %
Christophe
97
149
0.16 %
anaelle
97
38
0.04 %
Alan
98
146
0.15 %
sabrina
98
37
0.04 %
antonin
99
143
0.15 %
Angélique
99
37
0.04 %
Mohamed
100
141
0.15 %
Sandra
100
36
0.04 %
Philippe"""

LASTS = [
    name for name in RAW_LASTS.split("\n") if name and ':' not in name
]

def no_digit(name):
    return not(any(x in name for x in '0123456789'))
FIRSTS = [
    name.capitalize() for name in RAW_FIRSTS.split("\n") if name and no_digit(name)
]

COMPANY_DOMAINS = [
    "mystartup.io", "traditional.com", "green.org",
]

def random_phone():
    def random_digit1():
        return random.choice("12345679")
    def random_digit():
        return random.choice("0123456789")
    return "0" + random_digit1() + "".join(random_digit() for _ in range(8))

def example_email(first, last):
    return f"{first}.{last}@{random.choice(COMPANY_DOMAINS)}"


# this is several requirements, each for several groups, so a list
groups_requirements = [
    # a first batch of exclusive groups
    # one person can then be in only one of those groups
    {'exclusive': True,
     'specs': { f"language{n}": 20 for n in range(1, 7)}
    },
    {'exclusive': True,
     'specs': { f"numérique{n}": 30 for n in range(1, 5)}
    },
    # these are not exclusive now
    {'exclusive': False,
     'specs': {'maths': 50, 'français': 50},
    }
]

# this is ONE requirement for several groups, so a dict
# with the 'exclusive' and 'specs' keys
def validate(groups_requirement, persons):
    """
    check the requirement is doable
    """
    values = (v for v in groups_requirement['specs'].values())
    if groups_requirement['exclusive']:
        return len(persons) >= sum(values)
    else:
        return len(persons) >= max(values)


def make_groups(groups_requirement, persons):
    result = {}
    # cannot use random.sample (starting with 3.10) on a set
    L = list(persons)
    for name, howmany in groups_requirement['specs'].items():
        result[name] = set(random.sample(L, howmany))
        if groups_requirement['exclusive']:
            L = list(set(L) - result[name])
    return result

def makedata(filename, N, groups_requirements=None):
    """
    Parameters:
        N(int) number of people
        groups_requirements: a list of dictionaries like above
                     if not present, no groups are created
    """
    groups_requirements = groups_requirements or {}
    already = set()
    persons = []
    while len(already) < N:
        first = random.choice(FIRSTS)
        last = random.choice(LASTS)
        if (first, last) in already:
            continue
        already.add((first, last))
        persons.append((first, last, example_email(first, last), random_phone()))

    groups = {}
    for groups_requirement in groups_requirements:
        if not validate(groups_requirement, persons):
            print("WARNING : no can do {groups_requirement['specs'].keys()}")
            continue
        groups.update(make_groups(groups_requirement, persons))

    with open(filename, 'w') as f:
        for person in persons:
            fi, la, em, ph = person
            print(f"{fi} {la} {em} {ph}", file=f, end="")
            for g_name, g_persons in groups.items():
                if person in g_persons:
                    print(f" {g_name}", file=f, end="")
            print(file=f)

makedata("data-simple-10", 10)

makedata("data-groups-10", 10,
         [{'exclusive': False, 'specs': {'maths': 6, 'french': 6}}])

makedata("data-groups-120", 120, groups_requirements)