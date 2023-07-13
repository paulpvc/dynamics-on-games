
# Dynamique dans les jeux et applications à la sécurité dans les réseaux

La théorie des jeux est une branche des mathématiques et de
l’informatique qui permet d’analyser des comportements stratégiques d’agents
rationnels. Il est possible d’utiliser cette stratégie pour simuler la dynamique de
phénomènes informatiques, par exemple d’´echange de paquets dans des réseaux.
Une première étude des mécanismes formels et leur application dans le routage
dans les réseaux a été effectuée en 2019.
Voici le lien de l'article:
https://www.researchgate.net/publication/336208467_Dynamics_on_Games_Simulation-Based_Techniques_and_Applications_to_Routing

Ce projet est proposition d'implémentation de la simulation de la dynamique
de stratégies dans des réseaux et aussi des tests
de conditions nécessaires et/ou suffisantes pour la terminaison des dynamiques,
telles qu’expliquées dans l’article.


Pour tenter de détecter des dispute wheel, nous nous sommes aussi basé sur un article écrit par Timothy G.Griffin, F. Bruce Shepherd et Gordon Wilfong, traitant ce sujet:

https://www.cs.princeton.edu/courses/archive/spring10/cos598D/gsw02.pdf

Ce projet a été réalisé dans le cadre d'un stage de recherche en L1, par Bill-Kelly GOUTCHOWANOU et Paul VIGEOLAS-CHOURY, encadré par Monsieur Benjamin Monmege.

Ce simulateur a pour but de faciliter les tests sur des graphes de jeux, notamment pour observer la terminaison des différentes dynamiques proposées.



## Installation-dépendances

Le simulateur se trouve dans le fichier Propre, il requiert d'installer plusieurs bibliothèques python(3.X) comme: networkx, matplotlib, itertools


    
## Demo

Pour utiliser le simulateur nous avons mis à disposition plusieurs classes et un fichier util contenant tout un tas de fonction utilisées à l'intérieur des classes 

Pour représenter le graphe de jeu, il faut utiliser la classe Game.Pour cela, il faut initialiser une liste de joueur de type Player, ainsi que leurs préférences de stratégies, de type Strategy:

```python
import Player from Propre.Game.Player

player = Player("v1")
```
Ici nous initialisons un joueur ```player``` qui à pour nom ```v1```

```python
import Strategy from Propre.Game.Strategy

strategy = Strategy({"c1", "s2"})
```

Ici nous initialisons une stratégie ```strategy``` qui correspond au chemin ``` c1 -> s2 ``` 

Par exemple, supposons une liste players de joueurs et ```strat(i)``` la stratégie numéro i de type Strategy, et ```edges``` la liste des arcs du graphe de jeu:

```python
import Game from Propre.Game.Game

preferences = {players[0]: [(strat1, strat2), (strat2, strat3)],...,players[len(players)-1]: [(strat4, strat5)]}

game_graph = Game(players, edges, preferences)
```

Nous avons initialisé le graphe de jeu avec ```players``` comme noeuds, ```edges``` comme les arcs du graphe de jeu et ```preferences``` un dictionnaire qui associe à chaque joueur, une liste de tuples, où chaque tuple représente l'ordre de préférences direct sur des stratégies données.

La classe Game se charge de générer les graphes de dynamiques et par exemple pour savoir quelles dynamiques se terminent on peut utiliser la fonction ```python
game.display_dynamics_terminations()``` qui affichera dans la console si les dynamiques terminent ou non.


Pour plus d'utilisation, dans le dossier Utilities/tests, se trouvent plusieurs fichiers tests, qui sont des exemples d'exécution du simulateur sur différent graphe, permettant de comprendre l'utilisation des différentes fonctions.


