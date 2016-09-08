#Thanks to darnriti. https://gist.github.com/danriti/7345074
ROOM_ID=""
AUTH_TOKEN=""
MESSAGE="Ti stanno imboccando a casa!"

curl -H "Content-Type: application/json" \
     -X POST \
     -d "{\"color\": \"purple\", \"message_format\": \"text\", \"message\": \"$MESSAGE\" }" \
     https://api.hipchat.com/v2/room/$ROOM_ID/notification?auth_token=$AUTH_TOKEN
