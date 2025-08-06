# Documentation du Village Simulator

Cette documentation décrit en détail le fonctionnement du programme de simulation de village en 2D. Elle couvre l'architecture générale, les différents modules, les fichiers de données ainsi que le déroulement d'une journée simulée.

## Architecture générale

Le simulateur est organisé autour d'une structure d'objets en arbre (`SimNode`) qui relie les différents éléments logiques : monde, bâtiments et personnages. La boucle de simulation met à jour ces objets à chaque tick, tandis que le module `renderer` se charge de l'affichage Pygame.

## Principaux modules

### `main.py`
Point d'entrée de l'application : initialise Pygame, charge les données (bâtiments, carte, noms, genres, professions), crée les personnages et démarre la boucle principale. Chaque tick, la simulation est avancée et l'état affiché par `Renderer`.

### `settings.py`
Définit toutes les constantes de configuration (dimensions de l'écran, durée d'un tick, nombre de villageois, vitesse de déplacement, fatigue, etc.) regroupées dans la dataclass `Config`.

### `simnode.py`
Implémente la classe de base `SimNode` qui maintient des relations parent‑enfant et fournit la méthode `update` appelée récursivement dans l'arbre d'objets.

### `world.py`
Contient la représentation logique du village :
- `World` gère la grille, la liste des bâtiments et des personnages. Chaque mise à jour, il réinitialise les occupants, fait avancer les personnages puis déclenche la production des bâtiments.
- `Building` stocke position, taille, type, production possible et inventaire. La méthode `produce` augmente les ressources en fonction du nombre d'occupants.

### `character.py`
Modélise un villageois avec un nom, un genre, un rôle et divers états (position, cible, fatigue, inventaire). Ses principales responsabilités :
- choisir une destination selon la phase de la journée (`choose_action`)
- se déplacer avec une part d'aléatoire (`move_towards_target`)
- tenter d'acheter des biens (`attempt_purchase`)
- mettre à jour son temps de travail et sa fatigue (`update` et `update_fatigue`)

### `simulation.py`
Gère la boucle de simulation. Maintient le tick courant, la phase de la journée (matin, midi, après-midi, soir, nuit) et l'heure simulée. À chaque tick, il appelle `world.update` et réinitialise les compteurs en début de journée.

### `renderer.py`
Assure le rendu graphique avec Pygame : les bâtiments sont dessinés sur un fond statique. Les personnages sont représentés par un disque coloré (genre au centre, occupation en bordure) avec leur nom et leur rôle. Le panneau latéral affiche l'heure, les activités, les stocks des bâtiments et, si un personnage est sélectionné, ses caractéristiques.

### `economy.py`
Fournit deux fonctions :
- `pay_salary` : verse un salaire d'un bâtiment à un personnage.
- `buy_good` : transfert de biens entre un vendeur et un acheteur avec échange d'argent.

### `map_editor.py`
Outil interactif pour placer les bâtiments à la souris et générer `map.json`. Il charge les types de bâtiments définis dans `buildings.json` et les place successivement sur la carte.

## Fichiers de données

- `buildings.json` : liste des types de bâtiments, leur apparence et leur production.
- `map.json` : disposition des bâtiments sur la carte (créée par l'éditeur).
- `names.json` : prénoms classés par genre.
- `genders.json` : genres disponibles et couleur associée.
- `professions.json` : rôles des personnages, bâtiment de travail et couleur.

## Déroulement d'une journée simulée

1. **Matin / Après-midi** : chaque personnage décide d'aller travailler selon son rôle et son quota de travail (`work_time_ratio`). Ceux qui ne travaillent pas choisissent un bâtiment de loisirs.
2. **Midi** : les adultes cherchent un restaurant, les enfants se rendent à l'école.
3. **Soir** : tout le monde retourne à la maison.
4. **Nuit** : les personnages dorment et leur fatigue retombe à zéro. S'ils dépassent la limite de fatigue, ils s'écroulent pour une durée fixée.

À chaque tick :
- `Simulation` actualise la phase et l'heure.
- `World` met à jour les personnages puis les bâtiments produisent.
- `Renderer` affiche l'état courant.

## Économie et inventaire

Les bâtiments producteurs génèrent des ressources stockées dans leur inventaire. Les travailleurs y gagnent de l'argent via `pay_salary`. Les personnages disposant de fonds peuvent acheter des ressources à un bâtiment avec `buy_good`, ce qui transfère un objet vers leur inventaire et déplace l'argent en conséquence.

## Outils de tests

Le répertoire `tests/` contient des tests Pytest validant notamment la gestion de la fatigue, le fonctionnement du renderer et la progression de la simulation.

## Utilisation

1. Installer les dépendances : `pip install -r requirements.txt`
2. Lancer la simulation : `python main.py`
3. Contrôles principaux :
   - `P` pour mettre en pause/reprendre
   - cliquer sur un personnage pour afficher ses détails

Cette documentation résume l'ensemble du projet et peut servir de référence pour de futures évolutions.
