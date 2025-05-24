# Projet Django - Gestion des Pays et Régions

## Présentation du projet

Ce projet est une application web développée avec Django, permettant la gestion des pays d’Europe ainsi que de leurs régions.  
Elle offre une interface simple et intuitive pour consulter, ajouter, modifier ou supprimer des pays et des régions.
L’objectif est de fournir un outil fonctionnel, facile à prendre en main, avec un design épuré.

---

## Structure du projet

- **Modèles** :  
  - *Pays* : contient le nom du pays.  
  - *Région* : contient le nom, la capitale (ville), la population, la superficie, et une relation vers un pays.

- **Pages principales** :  
  - Liste des pays (avec possibilité de sélectionner plusieurs pays pour les supprimer).  
  - Liste des régions, affichant également les informations détaillées (capitale, population, superficie), avec des options pour modifier ou supprimer plusieurs régions simultanément.  
  - Formulaires pour ajouter ou modifier un pays ou une région.

- **Fonctionnalités** :  
  - Ajout de pays ou de régions via des formulaires simples.  
  - Modification des entrées existantes.  
  - Suppression multiple d’éléments sélectionnés.  
  - Navigation fluide entre les listes et les formulaires.

---

## Mode d’emploi

1. **Démarrage**  
   Après avoir installé les dépendances et lancé le serveur Django, vous pouvez accéder à l’application via un navigateur web.

2. **Consultation des listes**  
   Sur la page d’accueil ou les pages listes, toutes les entrées actuelles sont affichées.  
   Pour les régions, vous disposez aussi des détails comme la capitale, la population, la superficie, et le pays associé.

3. **Ajout**  
   Cliquez sur le bouton “Ajouter un pays” ou “Ajouter une région” pour accéder au formulaire.  
   Complétez les informations demandées et validez pour enregistrer la nouvelle entrée.

4. **Modification**  
   Dans les listes, cliquez sur “Modifier” à côté d’un pays ou d’une région pour mettre à jour ses informations.

5. **Suppression**  
   Sélectionnez les pays ou régions à supprimer en cochant les cases correspondantes, puis validez la suppression.

---

## Auteur

- Maëlys Fomholtz  
- Date de remise : mai 2025

