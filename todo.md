# Plan de développement & TODO

## Objectif principal : MVP1
Créer une simulation de village modulaire, configurable et réaliste, avec des villageois autonomes et des interactions basiques.

## Étapes principales

### Étape 1 : Modularité et Configurabilité
- [x] Créer des fichiers de configuration :
  - `names.json` pour les noms des villageois.
  - `professions.json` pour les professions.
  - `buildings.json` pour les bâtiments.
- [x] Rendre la taille de la carte, le nombre de bâtiments et de villageois configurables via `settings.py`.
- [x] Modifier `main.py` pour charger les données des fichiers de configuration.

### Étape 2 : Occupations réalistes
- [x] Implémenter une logique d'occupation avec :
  - 10% de chance d'être "idle".
  - 90% de chance de se déplacer vers un bâtiment.
- [ ] S'assurer que les occupations sont choisies parmi les bâtiments disponibles dans la simulation.

### Étape 3 : Système de déplacement
- [x] Implémenter un système de déplacement simplifié :
  - Les villageois se déplacent en ligne droite vers leur cible.
- [ ] Gérer les collisions et les priorités entre villageois.

### Étape 4 : Gestion des bâtiments et affichage
- [ ] Vérifier que le nombre de bâtiments dans l'éditeur correspond à la configuration.
  - Si le nombre est incorrect, afficher un message d'erreur.
- [ ] Afficher les noms des bâtiments à l'écran à leur position respective.

### Étape 5 : Gestion des logs
- [ ] Recréer le fichier de log à chaque lancement de la simulation.

### Étape 6 : Interactions simples
- [ ] Déclencher des interactions basiques lors de rencontres entre villageois.
- [ ] Ajouter un système de dialogues et d'humeurs.

### Étape 7 : Revues de code
- [ ] Revoir le code de `character.py` pour valider les déplacements et les occupations.
- [ ] Revoir le code de `world.py` pour vérifier la gestion des bâtiments et de la carte.
- [ ] Revoir le code de `main.py` pour valider la logique de chargement des configurations.

### Étape 8 : Tests et Debug
- [ ] Tester les comportements des villageois pour s'assurer qu'ils choisissent des occupations réalistes.
- [ ] Debugger les problèmes liés aux déplacements et aux occupations.
- [ ] Ajuster les paramètres pour équilibrer la simulation.

### Étape 9 : Validation finale
- [ ] Valider que la simulation est modulaire et configurable.
- [ ] S'assurer que les comportements des villageois sont réalistes et alignés avec les objectifs du MVP1.

## Notes supplémentaires
- Prioriser les tâches liées à la modularité et à la configurabilité.
- Documenter chaque classe et fonction pour faciliter les futures extensions.
- Préparer une démonstration pour valider le MVP1.
