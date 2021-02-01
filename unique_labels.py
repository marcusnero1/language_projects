import tekore as tk

#print("Enter your client ID")
#client_id = str(input())
client_id = '28db4fbdcb6f4a2ab409fd009b39e987'
#print("Enter your client secret")
#client_secret = str(input())   
client_secret = '5d583a5036b14358a313388291bc8d31'

app_token = tk.request_client_token(client_id, client_secret)
spotify = tk.Spotify(app_token)

print('Enter playlist URI')
uri = str(input())
if ':' in uri:
    playlist = uri.split(':')[2]
else:
    playlist = uri
playlist = spotify.playlist(playlist)


print(sorted({spotify.album(str(i.track.album.uri.split(':')[2])).label for i in playlist.tracks.items}))
