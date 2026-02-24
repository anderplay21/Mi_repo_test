import requests
import json
# PATCH request to update a list

curl 'https://api.bird.com/workspaces/{workspaceId}/lists/{listId}' \
  --request PATCH \
  --header 'Content-Type: application/json' \
  --data '{
  "name": "Karritos 24 mayo",
  "description": "pruebas de api",
  "consentType": "single",
  "tags": [
    "123e4567-e89b-12d3-a456-426614174000"
  ],
  "isProof": false
}'