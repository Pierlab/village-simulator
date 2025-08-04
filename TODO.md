# Plan de développement

## Stabilisation
- [x] Empêcher les personnages de quitter le périmètre de leur bâtiment lorsqu'ils sont immobiles.
- [x] Ajouter des tests unitaires pour valider les déplacements et le changement de phase.
- [ ] Introduire un système de seed pour rendre les tests déterministes.
- [ ] Vérifier la stabilité après plusieurs jours de simulation.
- [ ] Surveiller la dérive numérique en recentrant périodiquement les positions.

## Règles de vie
- [x] Les enfants passent la journée à l'école.
- [x] Chaque personnage possède un rôle et se rend dans le bâtiment associé.
- [x] Chaque bâtiment produit des ressources au fil du temps.
- [x] Gestion d'un inventaire pour les personnages et les bâtiments.
- [x] Les travailleurs gagnent de l'argent et peuvent le dépenser.
- [x] Transfert d'argent ou de matériel entre personnages et bâtiments.
- [ ] Gestion de besoins supplémentaires (sociabilité, santé, hygiène).
- [ ] Traits de personnalité influençant les décisions.
- [ ] Événements ponctuels : maladies, fêtes ou catastrophes.

## Mécaniques futures
- Système de pathfinding pour éviter les obstacles.
- Dialogues, humeurs et interactions sociales simples.
- Météo influençant les activités.
- Gestion des familles et du passage du temps.
- Échanges commerciaux avec d'autres villages ou marchands itinérants.
- Construction et amélioration de bâtiments.
- Économie avec offre, demande et prix variables.

## Améliorations techniques
- Profiler la boucle de simulation pour identifier les goulots d'étranglement.
- Mettre en place une intégration continue pour exécuter les tests.
- Exporter des logs pour analyser les comportements anormaux.

## Brainstorm
- Lier un agent LLM à chaque personnage pour un comportement émergent.
- Génération procédurale de quêtes ou d'histoires.
- Mode multijoueur ou interaction entre villages distants.
- Support d'une carte étendue avec zoom et défilement.
- Simulation de saisons, de climat et de catastrophes naturelles.
