#!/bin/bash

# Initialize Git
git init

# Add all files
git add .

# Commit
git commit -m "Tulpar Kurye Transformation Complete - Static Site Ready"

# Rename branch to main
git branch -M main

echo "Git başarıyla başlatıldı ve dosyalar eklendi!"
echo "Şimdi GitHub reponuzun linkini ekleyip push yapabilirsiniz."
echo "Örnek: git remote add origin https://github.com/KULLANICI_ADIN/REPO_ADIN.git"
echo "git push -u origin main"
