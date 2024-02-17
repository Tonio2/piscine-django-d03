#!/bin/bash

# Vérifie si le script est sourcé ou exécuté normalement
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    echo "Ce script doit être sourcé pour activer l'environnement virtuel"
    echo "Utilisez 'source my_script.sh' au lieu de './my_script.sh'"
    exit 1
fi

# Création de l'environnement virtuel s'il n'existe pas
if [ ! -d "django_venv" ]; then
    python3 -m venv django_venv
fi

# Activation de l'environnement virtuel
source django_venv/bin/activate

# Installation des dépendances si requirements.txt est présent
if [ -f "requirements.txt" ]; then
    pip install -r requirements.txt
else
    echo "Le fichier requirements.txt est introuvable"
fi
