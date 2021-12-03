<center><h1>Modèle de diffusion d'une maladie mortelle hautement infectieuse dans une population d'agents mobiles</h1></center>

## Sommaire
1. [Introduction](#introduction)  
2. [Présentation du modèle](#presenration-du-modele)  
   a. [Définition des paramètres](#definition-des-parametres)  
   b. [Présentation des agents](#presentation-des-agents)  
3. [Expériances éffectuées](#experiences-effectuees)  
4. [Conclusion](#conclusion)  

&nbsp;  

# 1. Introduction <a name="introduction"></a>

<div style="text-align: justify;">
Cette étude a été crée dans le but de comprendre comment une maladie mortelle hautement infectieuse (MMHI) se diffuse dans une population d'agents mobiles 
en fontion du temps. Le problème auquel nous sommes confrontés est le suivant : quelles mesures peuvent être prises pour protéger la population en ralentissant 
ou en éliminant la maladie ? Nous commencerons par présenter le modèle mis en place et les agents qui le composent puis nous présenterons et expliquerons les
résultats obtenus.
</div>

## 2. Présentation du modèle <a name="presenration-du-modele"></a>

### a. Définition des paramètres <a name="definition-des-parametres"></a>

<div style="text-align: justify;">
Pour ce modèle nous avons utilisé l'outil NetLogo, un logiciel de modélisation de simulation. Les paramètres utilisés dans notre étude seront les suivants :
<ul>
    <li>La contagiosité : exprime la probabilité qu'un individu infecté infecte un autre individu. Afin de rester pertinant, la valeur minimum de ce paramètre est de 60 %</li>
    <li>La probabilité de guérison.</li>
    <li>La durée de l'immunité.</li>
    <li>La durée de la maladie.</li>
</ul>

### b. Présentation des agents <a name="presentation-des-agents"></a>

<div style="text-align: justify;">
Les agents sont définis par leur état de santé (sain, infecté, immunisé), si il y a suffisamment de place dans le monde, ils peuvent se reproduire. Lorque qu'un agent est infecté, 
il peut guérir ou mourir selon la probabilité de guérison ou après avoir excédé leur durée de vie de 50 ans.