#!/bin/bash

echo "Создание директории logs"
mkdir logs

echo "Переименование файла .env"
mv .env.example .env

echo "Пароль должен быть не менее 8 символов и содежать строчные и заглавные буквы, числа и спец. символы"
read -p "Введите пароль: " password

sed -i "s/<password>/$password/g" .env
