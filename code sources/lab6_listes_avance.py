notes = [12, 9, 15, 8, 17, 13, 19, 10]
total = 0
nb_notes = len(notes)
if not notes:
    print("Aucune note à traiter.")
    exit()
notes_sur_100=[]
for note in notes:
     notes_sur_100.append(100 * note / 20)
print(notes_sur_100)
notes = notes_sur_100
for note in notes:
    total += note  # total = total + note
moyenne = total / nb_notes
print(f"Moyenne : {moyenne:.2f}")
#Ajouter +1 à chaque note:
notes_bonus = [min(note + 5, 100) for note in notes]
print("Notes après bonus :", notes_bonus)
#Filtrer les notes au-dessus d’un seuil:
seuil = 60
notes_valides = [note for note in notes if note >= seuil]
print(f"Notes ≥ {seuil} :", notes_valides)
notes_valides_bonus = [note for note in notes_bonus if note >= seuil]
print(f"Notes ≥ {seuil} :", notes_valides_bonus)
notes_rattrappage = [note for note in notes_bonus if note < 60 and note >= 30]
print("30>= Notes >60 :", notes_rattrappage)
notes_Échec = [note for note in notes_bonus if note < 30]
print(f"Notes < 30 :", notes_Échec)

#Générer un petit rapport texte:
moyenne_initiale = sum(notes) / nb_notes
moyenne_bonus = sum(notes_bonus) / len(notes_bonus)
lignes = []
lignes.append("=== Rapport des notes ===")
lignes.append(f"Nombre d'étudiants : {nb_notes}")
lignes.append(f"Notes originales : {notes}")
lignes.append(f"Notes après bonus : {notes_bonus}")
lignes.append(f"Moyenne initiale : {moyenne_initiale:.2f}")
lignes.append(f"Moyenne après bonus : {moyenne_bonus:.2f}")
lignes.append(f"Notes ≥ {seuil} : {notes_valides} (soit {len(notes_valides)} étudiants)")
lignes.append(f"notes_bonus>={seuil}: {notes_valides_bonus}")
lignes.append("Détails par étudiant :")
for index, note in enumerate(notes, start=1):
    bonus = notes_bonus[index - 1]
    if bonus >= seuil:
        categorie = "Validation"
    elif bonus < 60 and bonus >= 30:
        categorie = "Rattrapage"
    else:
        categorie = "Echec"
    lignes.append(f"  Étudiant {index:02d} — note {note:>5.2f} → bonus {bonus:>5.2f} → categorie : {categorie} ")
top_3_notes=[]
top_3_notes = sorted(notes, reverse=True)[:3]
lignes.append(f"top_3_notes : {top_3_notes}")
rapport = "\n".join(lignes)
print(rapport)
with open("rapport_notes.txt", "w", encoding="utf-8") as f:
    f.write(rapport)