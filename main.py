def get_live_chat_id(youtube):
  """
  Get the Live Chat ID of the currently active broadcast.
  """
  request = youtube.liveBroadcasts().list(
      part='snippet',
      broadcastStatus='active',
      broadcastType='all'
  )
  response = request.execute()

  if response['items']:
      return response['items'][0]['snippet']['liveChatId']
  else:
      raise ValueError("No active live broadcasts found.")


def send_message(youtube, live_chat_id, message):
  """
  Send a message to the specified live chat.
  """
  request = youtube.liveChatMessages().insert(
      part="snippet",
      body={
          "snippet": {
              "liveChatId": live_chat_id,
              "type": "textMessageEvent",
              "textMessageDetails": {
                  "messageText": message
              }
          }
      }
  )
  request.execute()
  print(f"Message sent: {message}")
