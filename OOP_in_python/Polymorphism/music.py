#################################################################################
# Implement a class hierarchy for a music player. Use polymorphism
# to create different player types like MP3Player, CDPlayer, and StreamingPlayer.
#################################################################################
class MusicPlayer:
    def play(self):
        pass
class MP3Player(MusicPlayer):
    def play(self):
        return "playing MP3 music"
class CDPlayer(MusicPlayer):
    def play(self):
        return "Playing music form CD"
class StreamingPlayer(MusicPlayer):
    def play(self):
        return "Streaming music online"
def play_music(player):
    print(player.play())
def main():
    mp3_player=MP3Player()
    cd_player=CDPlayer()
    online_player=StreamingPlayer()
    #print the sound
    play_music(mp3_player)
    play_music(cd_player)
    play_music(online_player)
if __name__:='__main__':
    main()