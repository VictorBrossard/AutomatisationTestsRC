# Automatisation des tests RC
Projet : Automatisation des tests du logiciel qui réalise l’interface entre l’opérateur et la machine

Entreprise : Europlacer

## Objectif du projet
1. Mettre en place l’environnement de test, et être capable de démarrer automatiquement le logiciel sous test ainsi que le simulateur de la machine.

2. Entrer dans différents menus en simulant des cliques, et pouvoir réaliser des impressions écran pour analyser (en cas de problème) ce qui a été vu.

3. Coder un cas simple de test (à définir) avec lecture de fichiers et de bases de données pour valider le test et généré un rapport de test avec le statut (OK / NOK) de chaque étape du test (le format reste à définir).

4. Coder différents cas de tests en fonction du temps restant.

## Explictation du projet
Voir le fichier Documentation

## Convention du projet
### Visibilité des méthodes
Si une méthode ou une classe commence par "__" alors c'est une méthode "privé".

Si une méthode ou une classe commence par "_" alors c'est une méthode "protected".

Dans les commentaires des méthodes, le premier caractère signifie : 
- "+" = Public
- "-" = Private
- "#" = Protected

### Choses à savoir
Les combinaisons de touches supérieures à trois touches en même temps ne sont pas disponible.

Le bouton shift et tab reste écris dans le fichier même s'il n'est pas utile.

### Utilisation de l'interface UserEntryPopUp
Cette interface peut afficher des entrées de textes, des entrées d'entiers et des comboboxs.

Les entiers dans la liste widget_list devront respecté ce format:
- "0" = entrée de texte
- "1" = entrée d'entier
- "2" = comboboxs
- "3" = limited text entry

La liste combobox_list contient juste les valeurs des comboboxs. Elle n'est utilisé que dans le cas où il y a un "2" dans le liste widget_list.
