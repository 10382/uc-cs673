# chat/consumers.py
from channels.generic.websocket import AsyncWebsocketConsumer
import json
from chat.models import rooms, messages
from datetime import datetime

class ChatConsumer(AsyncWebsocketConsumer): # create ChatConsumer from AsyncWebsocketConsumer
    async def connect(self): # handle webSocket.connect
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        self.user = self.scope["user"]

        # join room group
        if rooms.objects.filter(name = self.room_name).exists() is False:
           room_creation = rooms(name=self.room_name, description = 'Test Desc',
                                 creation_date = datetime.utcnow())
           room_creation.save()
            
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        self.rooms = set

        await self.accept() # accept webSocket connection

    async def disconnect(self, close_code): # handle webSocket.disconnect
        # leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # receive message from WebSocket
    async def receive(self, text_data): # handle webSocket.receive 

        text_data_json = json.loads(text_data) # load in text_data
        message = text_data_json['message'] # grab message from text_data
        room_id = rooms.objects.get(name=self.room_name).id
        message_db = messages(room_id=room_id,
                           sender_user_name = self.scope["user"].username,
                           receiver_user_id = 'User2',
                           content = message,
                           sent_date = datetime.utcnow(),
                           received_date = datetime.utcnow()
                           )
        message_db.save()
        # send message to corresponding room group
        await self.channel_layer.group_send( # send message
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'username': self.scope["user"].username
            }
        )

     # receive message from room group
    async def chat_message(self, event): # every chat consumer in group (room) will receieve the message
        message = event['message']
        username = event['username']

        # send message back to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'username': username
        }))