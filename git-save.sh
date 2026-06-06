#!/bin/bash

echo "================================="
echo "      Git Quick Save Script"
echo "================================="

# Verificar cambios
if [[ -z $(git status --porcelain) ]]; then
    echo "No hay cambios para commitear."
    exit 0
fi

# Mostrar estado
echo ""
git status

echo ""
read -p "Mensaje del commit: " commit_message

# Validar mensaje
if [[ -z "$commit_message" ]]; then
    echo "El mensaje no puede estar vacío."
    exit 1
fi

# Add + Commit
git add .

git commit -m "$commit_message"

# Verificar si el commit fue exitoso
if [[ $? -ne 0 ]]; then
    echo ""
    echo "Error al hacer commit."
    exit 1
fi

echo ""
echo "Commit realizado correctamente."

# Preguntar por push
echo ""
read -p "¿Deseas hacer push? (y/n): " do_push

if [[ "$do_push" =~ ^[Yy]$ ]]; then
    git push
    echo ""
    echo "Push realizado."
else
    echo ""
    echo "Push omitido."
fi
