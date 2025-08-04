# Village Simulator

🎯 **Objectif de la simulation**

Simulation autonome d’un village peuplé d’environ 30 personnages, chacun doté de caractéristiques propres, d’un cycle de vie, d’activités quotidiennes et d’interactions avec les autres. La visualisation s’effectue en temps réel avec Pygame.

🛠️ **Changements récents**

- Refactorisation des classes `Character` et `World` pour améliorer la modularité.
- Ajout d’une grille dans `World` pour gérer les positions.
- Simplification des logs pour réduire les informations inutiles.
- Ajout d’un éditeur de carte (`map_editor.py`) pour générer `map.json`.
- Introduction d’une classe `Simulation` chargée d’avancer le temps (à intégrer dans la boucle principale).
- Ajout d’un fichier `.gitignore` pour exclure les fichiers temporaires.

📋 **Prochaines étapes**

- Corriger l’appel à `move_towards_target` dans `Simulation.run_tick`.
- Intégrer la classe `Simulation` dans `main.py` pour animer les personnages.
- Étendre `Character.choose_action` aux phases du soir et de la nuit.
- Conserver le type et la taille des bâtiments dans l’éditeur et vérifier les limites de la carte.
- Assurer l’encodage UTF‑8 lors de la lecture/écriture de `map.json`.
- Exploiter `KMH_TO_PIXELS_PER_TICK` pour la vitesse ou supprimer la constante si elle reste inutilisée.
- Ignorer les fichiers de logs comme `simulation.log` via `.gitignore`.
 
Consultez `TODO.md` pour la feuille de route complète vers le MVP1.
## Éditeur de Carte

Un éditeur de carte simple est disponible pour créer la carte du village :

- Lancer `map_editor.py` pour afficher une carte vide.
- Cliquez successivement pour positionner les bâtiments (maison, ferme, forge, etc.).
- Une fois tous les bâtiments placés, la carte est sauvegardée dans `map.json` et peut être utilisée dans la simulation principale.

🧰 **Éléments techniques à définir ensuite**

- Modèle de simulation (discret/continu)
- Sauvegarde/chargement de l’état du monde
- Extensions futures possibles : maladies, météo, reproduction, économie locale…

📌 **Règles importantes**

- Tout nouveau fichier ou modification doit être testable immédiatement.
- Les classes doivent rester simples, découplées et réutilisables.
- Chaque commit doit inclure une description claire des ajouts.
- Ne jamais tout mettre dans un seul fichier.
- Ajouter des `TODO` ou `# next step` quand une fonction est prévue mais non finie.

