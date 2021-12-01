<center><h1> Modèle de Schelling </h1></center>

## Sommaire
1. [Introduction](#introduction)
2. [Présentation du modèle](#presenration-du-modele)  
   a. [Définition des paramètres](#definition-des-parametres)  
   b. [Présentation des individus](#presentation-des-individus)  
3. [Expériances éffectuées](#experiences-effectuees)

&nbsp;  

# Introduction  <a name="introduction"></a>

<div style="text-align: justify">
Cette simulation a pour but de montrer comment le modèle de Schelling peut être utilisé pour simuler un système de répartition d'une population mobile.
Nous étudirons la façon dont les individus de répartissent dans un espace définis et durant les expériences, nous ferons varier plusieurs paramètres
afin d'observer leur impact sur la population. Notre problématique est la suivante : quel facteur influence la répartition des individus dans un espace défini ?
Pour cela nous présenterons le modèle utilisé, les expériences menées et les résultats obtenus.
</div>

## Présentation du modèle  <a name="presenration-du-modele"></a>

### Définition des paramètres  <a name="definition-des-parametres"></a>

<div style="text-align: justify">
Pour ce modèle, les paramètres que nous allons utiliser sont les suivants :
<ul>
    <li> la durée de la simulation.  </li>  
    <li> la taille du monde dans lequel les individus vont se déplacer. </li>  
    <li> le seuil de tolérance des individus. </li>  
    <li> la densité de la population. </li>
</ul>
</div>

### Présentation des individus  <a name="presentation-des-individus"></a>

<div style="text-align: justify">
Les individus sont représentés par des carrés colorés de taille 1x1, les carrés jaunes et violets représentent chacun un "type" d'individu et les carrés turquoises 
représentent las cases vides. L'insatisfaction des individus est déterminé par leur voisinage, c'est-à-dire les cases adjacentes à l'individu (cela 
inclut également les diagonales), et le seuil de tolérance définis. Ils se déplacent dans un monde dont la taille est définie au début de l'expérience, 
les individus chercheront à se déplacer de façon à être satisfait de leur voisinage.
</div>

<div style="page-break-after: always;"></div>

## Expériences éffectuées  <a name="experiences-effectuees"></a>  

<div style="text-align: justify">
Comme expliqué précédemment, nous allons faire varier certains paramètres afin d'observer leur impact sur la population. La durée de la simulation est fixée à 10 000 itérations 
maximum dans le cas où aucune répartition stable n'est obtenue. Les individus évoluront successivement dans un monde de taille 10x10, 20x20 et 50x50, au-delà de cela les temps de calcul seraient
beaucoup trop longs. 
</div>