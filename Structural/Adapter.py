# Adapter Pattern

# Target - Interface for modern music players (supports MP3 files)
class ModernMusicPlayer:
    def play_mp3(self, file):
        print(f"Playing MP3 file: {file}")


# Adaptee - Legacy audio player (supports WAV files)
class LegacyAudioPlayer:
    def play_wav(self, file):
        print(f"Playing WAV file: {file}")


# Adapter - Wraps around the LegacyAudioPlayer to make it compatible with ModernMusicPlayer
class WavToMp3Adapter(ModernMusicPlayer):
    def __init__(self, legacy_audio_player):
        self.legacy_audio_player = legacy_audio_player

    def play_mp3(self, file):
        # Convert MP3 to WAV and use the LegacyAudioPlayer to play the WAV file
        print(f"Converting MP3 to WAV: {file}")
        self.legacy_audio_player.play_wav(file)


# Client Code
if __name__ == "__main__":
    # Modern music player (supports MP3 files)
    modern_player = ModernMusicPlayer()
    modern_player.play_mp3("song.mp3")

    # Legacy audio player (supports WAV files)
    legacy_player = LegacyAudioPlayer()
    legacy_player.play_wav("music.wav")

    # Adapter allows modern music player to play WAV files using the legacy audio player
    wav_adapter = WavToMp3Adapter(legacy_player)
    wav_adapter.play_mp3("music.wav")
