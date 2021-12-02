<center><h1> Modèle de Schelling </h1></center>

## Sommaire
1. [Introduction](#introduction)
2. [Présentation du modèle](#presenration-du-modele)  
   a. [Définition des paramètres](#definition-des-parametres)  
   b. [Présentation des individus](#presentation-des-individus)  
3. [Expériances éffectuées](#experiences-effectuees)

&nbsp;  

# 1. Introduction  <a name="introduction"></a>

<div style="text-align: justify">
Cette simulation a pour but de montrer comment le modèle de Schelling peut être utilisé pour simuler un système de répartition de populations mobiles.
Nous étudirons la façon dont les individus de répartissent dans un espace définis et durant les expériences, nous ferons varier plusieurs paramètres
afin d'observer leur impact sur les populations. Notre problématique est la suivante : quel facteur influence la répartition des individus dans un espace défini ?
Pour cela nous présenterons le modèle utilisé, les expériences menées et les résultats obtenus.
</div>

## 2. Présentation du modèle  <a name="presenration-du-modele"></a>

### a. Définition des paramètres  <a name="definition-des-parametres"></a>

<div style="text-align: justify">
Pour ce modèle, les paramètres que nous allons utiliser sont les suivants :
<ul>
    <li> la durée de la simulation. (Constante : 10 000)  </li>  
    <li> la taille du monde dans lequel les individus vont se déplacer. (Valeurs possibles : 10, 20, 50) </li> 
    <li> le seuil de tolérance des individus. (Valeurs possibles : 0.1, 0.25, 0.5, 0.75, 1.0) </li>  
    <li> la densité de la population. (Cette variable est issue d'un calcul expliqué au point 3) </li>
</ul>
</div>

### b. Présentation des individus  <a name="presentation-des-individus"></a>

<div style="text-align: justify">
Les individus sont représentés par des carrés colorés de taille 1x1, les carrés jaunes et violets représentent chacun une population d'individu et les carrés turquoises 
représentent las cases vides. L'insatisfaction des individus est déterminé par leur voisinage, c'est-à-dire les cases adjacentes à l'individu (cela 
inclut également les diagonales), et le seuil de tolérance définis. Ils se déplacent dans un monde dont la taille est définie au début de l'expérience, 
les individus chercheront à se déplacer de façon à être satisfait de leur voisinage.
</div>

<div style="page-break-after: always;"></div>

# 3. Expériences éffectuées  <a name="experiences-effectuees"></a>  

<div style="text-align: justify">
Comme expliqué précédemment, nous allons faire varier certains paramètres afin d'observer leur impact sur la population. La durée de la simulation est fixée à 10 000 itérations 
maximum dans le cas où aucune répartition stable n'est obtenue. Les individus évoluront successivement dans un monde de taille 10x10, 20x20 et 50x50, au-delà de cela les temps de calcul seraient
beaucoup trop longs. Le seuil de tolérance est un pourcentage exprimé sous la forme d'une valeur allant de 0 à 1, si l'insatisfaction d'un individu est supérieur à ce seuil il se déplacera. 
La densité d'une population est exprimé par la formule suivante ((taille_monde*taille_monde)//2) - N, le nombre de case vides dans le monde correspond à N*2.

N.B. : le symbole // est utilisé pour la division entière.
</div>

### a. Résultats prévisibles  <a name="resultats-previsibles"></a>

<div style="text-align: justify">
Cette section est consacrée aux expériences dont la valeur d'un ou plusieurs paramètres permettent d'obtenir le même résultat.  

Seuil de tolérance : 0.1

Nous pourrons remarquer dans les expériences suivantes que lorsque le seuil de tolérance est fixé à 0.1, la simulation se termine après les 10 000 itérations. 
Cela s'explique par le fait que l'insatisfaction des individus est toujours supérieur au seuil et ne peuvent donc trouver une position qui puisse les satisfaire 
et ce peu importe la taille du monde ou la densité de la population. 
</div>

&nbsp;  

&nbsp;  

<div style="text-align: center">
<b>Taille du monde : 10x10 &nbsp;Densité d'une population : 40 individus</b>
</div>

| ![](./Images/t10tins0.1dens10.png) | ![](./Images/t10tins0.1dens10fin.png) |
| :--------------------------------: | :-----------------------------------: |
|               Fig. 1               |                Fig. 2                 |

<div style="page-break-after: always;"></div>

<div style="text-align: center">
<b>Taille du monde : 20x20 &nbsp;Densité d'une population : 180 individus</b>
</div>

| ![](./Images/t20tins0.1dens20.png) | ![](./Images/t20tins0.1dens20fin.png) |
| :--------------------------------: | :-----------------------------------: |
|               Fig. 3               |                Fig. 4                 |