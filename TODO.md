# TODO

## Backlog vers MVP1

### Simulation
- Corriger l'appel à `move_towards_target` dans `Simulation.run_tick`.
- Intégrer `Simulation` dans `main.py` et animer les personnages.
- Étendre `Character.choose_action` aux phases du soir et de la nuit.
- Utiliser `KMH_TO_PIXELS_PER_TICK` pour régler la vitesse.

### Éditeur et monde
- Conserver type et taille des bâtiments lors de la sauvegarde dans l'éditeur.
- Vérifier les limites de la carte dans `World.add_building`.
- Assurer l'encodage UTF-8 pour `map.json`.

### Logs
- Recréer le fichier de log à chaque lancement.

### Interactions à venir
- Ajouter un pathfinding basique.
- Déclencher des interactions entre villageois.
