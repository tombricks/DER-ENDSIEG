import unidecode
titles = [
    "Reichskommissar",
    "Deputy Reichskommissar",
    "SS and Police Leader",
    "Generalfeldmarschall",
    "Oberkommandant",
    "Poglavnik",
    "Duce",
    "Fører",
    "Caudillo",
    
    "General",
    "Commander",
    "Supreme Commander",
    "Supreme Leader",
    "Grand Admiral",
    "Field Marshal",
    "Marshal",
    "Captain",
    
    "General Secretary",
    "First Secretary",
    "Chairman",
    "Premier",
    
    "King",
    "Prince",
    "Princess",
    "Sultan",
    "Caliph",
    
    "Vice President",
    "Vice Chancellor",
    "Governor",
    "Minister President",
    "Minister"
]
scriptloc1 = ""
scriptloc2 = ""
localisation = ""
traits = ""
for title in titles:
    tag = unidecode.unidecode(title.replace(" ", "_"))
    traits += F"    TITLE_{tag} = {{  }}\n"
    localisation += F" TITLE_{tag}: \"{title}\"\n"
    scriptloc1 += F"    text = {{ trigger = {{ has_country_leader_with_trait = TITLE_{tag} }} localization_key = TITLE_{tag} }}\n"
    scriptloc2 += F"    text = {{ trigger = {{ has_idea_with_trait = TITLE_{tag} }} localization_key = TITLE_{tag} }}\n"

print("Traits:")
print(traits)
print("Localisation:")
print(localisation)
print("Leader Titles:")
print(scriptloc1)
print("Deputy Titles:")
print(scriptloc2)
