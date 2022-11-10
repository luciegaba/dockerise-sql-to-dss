
import pandas as pd
from settings import AUTH_URL, BASE_URL, playlist_id
from credentials import CREDS_SPOTIFY, CREDS_MYSQL
import requests
import re
import mysql.connector
from mysql.connector import Error
from sqlalchemy import create_engine


def authentification_token(AUTH_URL,creds_spotify):
    auth_response = requests.post(AUTH_URL,creds_spotify)
    auth_response_data= auth_response.json()
    access_token = auth_response_data['access_token']
    headers = {
    'Authorization': 'Bearer {token}'.format(token=access_token)}
    return headers

def API_requesting_playlist(playlist_id,headers):
    liste=[]
    r = requests.get(BASE_URL + 'playlists/' + playlist_id  + "playlist_tracks", headers=headers)
    tracks=r.json()
    tracks_=tracks["tracks"]["items"]
    for track in tracks_:
        dic_songs=dict_for_principal_car(track)
        dic_songs.update(get_audio_features(BASE_URL,headers,dic_songs["track_uri"]))
        liste.append(dic_songs)

    df=pd.DataFrame(liste)       
            
    return df

def dict_for_principal_car(track):
    dictionnaire={"track_uri":re.sub(r"[a-zA-Z]+:[a-zA-Z]+:","",track["track"]["uri"]), 
    "track_name":track["track"]["name"],
    "artist_uri":track["track"]["artists"][0]["uri"],
    "artist_name":track["track"]["artists"][0]["name"],
    "album":track["track"]["album"]["name"],
    "track_pop":track["track"]["popularity"]
    }
    return dictionnaire

def get_audio_features(BASE_URL,headers,track_id):
    r=requests.get(BASE_URL + 'audio-features/' + track_id , headers=headers)
    audio_features=r.json()
    return audio_features



def test_connection_mysql(config):
    try:
        connection = mysql.connector.connect(host=config.get('host'),
                                            database=config.get('database'),
                                            user=config.get('user'),
                                            password=config.get('password'))
        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("You're connected to database: ", record)
        return connection

    except Error as e:
        print("Error while connecting to MySQL", e)

def push_table_to_mysql(config,tracks):
    name="Spotify"
    engine = create_engine(f"mysql+pymysql://{config.get('user')}:{config.get('password')}@{config.get('host')}/{config.get('database')}")
    tracks.to_sql(con=engine.connect(), name=name, if_exists='fail')
    print("Succesfully imported")

def from_api_to_sql():
    headers=authentification_token(AUTH_URL,CREDS_SPOTIFY)
    tracks=API_requesting_playlist(playlist_id,headers)
    print(tracks)
    connection=test_connection_mysql(CREDS_MYSQL)
    push_table_to_mysql(CONFIG,tracks)
    #return tracks


if __name__== "__main__":
    from_api_to_sql()