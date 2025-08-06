# Village Simulator

Une simulation minimaliste d'un village en 2D. Les habitants se déplacent entre les bâtiments selon les différentes phases de la journée et réagissent de manière autonome.

## Fonctionnalités actuelles

- Chargement d'une carte (à partir de `map.json`) contenant les bâtiments du village.
- Personnages générés avec des noms aléatoires et une maison d'origine.
- Phases de la journée : matin, midi, soir et nuit.
- Déplacement en ligne droite avec une légère part d'aléatoire.
- Regroupement des personnages au **centre** des bâtiments.
- Quand ils sont immobiles, les personnages restent dans un petit périmètre autour de leur bâtiment et bougent de manière saccadée.
- Chaque villageois possède un **genre** (couleur intérieure) et un **rôle** (couleur extérieure) déterminant son lieu de travail.
- Les enfants sont plus petits et se rendent automatiquement à l'école pendant la journée.
- Le nombre d'occurrences de chaque bâtiment est défini dans `buildings.json` et utilisable dans l'éditeur.
- Possibilité de mettre la simulation en pause (`P`) et d'inspecter un personnage en cliquant dessus.
- Système économique basique : les travailleurs reçoivent un salaire, peuvent dépenser leur argent et transporter des ressources.
- La proportion de temps consacrée au travail est configurable (`work_time_ratio`).
- Architecture en arbre (`SimNode`) permettant d'ajouter facilement de nouveaux objets ou règles.
- Support de plugins déclarés dans `settings.py`.
- Visualisation de la structure via `python main.py --tree`.

## Lancer la simulation

```bash
pip install -r requirements.txt
python main.py            # lance la simulation
python main.py --tree     # affiche l'arbre des objets
```

## Contrôles

- `P` : mettre en pause ou reprendre la simulation
- Cliquez sur un personnage pour afficher ses caractéristiques dans le panneau latéral

## Prochaines étapes

Les idées d'évolutions futures sont listées dans [TODO.md](TODO.md).

## Licence

Projet open source destiné à l'expérimentation.
