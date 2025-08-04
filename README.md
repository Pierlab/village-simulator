🎯 Objectif de la Simulation
Simulation autonome d’un village peuplé d’environ 30 personnages, chacun doté de caractéristiques propres, d’un cycle de vie, d’activités quotidiennes et d’interactions avec les autres. Visualisation en temps réel avec Pygame.

🛠️ Changements récents :
- Refactorisation des classes `Character` et `World` pour améliorer la modularité.
- Ajout d’une grille dans `World` pour gérer les positions.
- Simplification des logs pour réduire les informations inutiles.

📋 Prochaines étapes :
- Implémenter un système de pathfinding pour les déplacements.
- Ajouter des interactions entre villageois.
- Finaliser le MVP1 avec un comportement réaliste des villageois.

## Éditeur de Carte

Un éditeur de carte simple est disponible pour créer la carte du village :

- Lancer `map_editor.py` pour afficher une carte vide.
- Cliquez successivement pour positionner les bâtiments (maison, ferme, forge, etc.).
- Une fois tous les bâtiments placés, la carte est sauvegardée dans `map.json` et peut être utilisée dans la simulation principale.

🧰 Éléments Techniques à Définir Ensuite
  - Modèle de simulation (discret/continu)
  - Sauvegarde/chargement de l’état du monde
  - Extensions futures possibles : maladies, météo, reproduction, économie locale…

📌 Règles importantes
  - Tout nouveau fichier ou modification doit être testable immédiatement
  - Les classes doivent rester simples, découplées et réutilisables
  - Chaque commit doit inclure une description claire des ajouts
  - Ne jamais tout mettre dans un seul fichier
  - Ajouter des TODO ou # next step: quand une fonction est prévue mais non finie