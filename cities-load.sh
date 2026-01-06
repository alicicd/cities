#!/bin/bash

DATA_FILE="app/cities.json"
API_URL="http://localhost:8000/city"

if [ ! -f "$DATA_FILE" ]; then
  echo "Error: $DATA_FILE not found!"
  exit 1
fi

echo "Starting manual data seeding..."

jq -c '.[]' "$DATA_FILE" | while read -r city; do
  NAME=$(echo $city | jq -r '.name')
  POPULATION=$(echo $city | jq -r '.population')

  echo -n "Adding $NAME ($POPULATION)... "

  RESPONSE=$(curl -s -X POST "$API_URL?name=$NAME&population=$POPULATION")

  echo "Response: $RESPONSE"
done

echo "Seeding finished!"
