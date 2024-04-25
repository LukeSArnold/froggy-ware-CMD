from pytube import YouTube
import os
from youtubesearchpython import VideosSearch
from engine.conversions import minutes_to_ms
import engine.scrubber as scrubber


class YoutubeEngine:
    def __init__(self, log_bool=False):
        self.logging = log_bool

    def within_bounds(self, ms_1, ms_2, allowance):
        """ this class checks to see whether two time stamps are within 10 seconds of eachother """

        difference = abs(ms_1 - ms_2)
        if difference < (allowance * 1000):
            return True
        else:
            return False

    def search_from_list(self, songs):
        """This method takes in a list of dictionaries, where each dictionary consists of song info"""
        song_info = []
        for song in songs:
            artist = song['artist']
            track = song['track']
            track_length = song['duration_ms']
            search_string = "{} {} ".format(track, artist)
            search_depth = 6

            if self.logging:
                print("===========================")
                print(f"Attempting conversion for {track} by {artist}")

            link = self.vet_search_results(track_length, search_string, search_depth)

            if link is None:
                search_string = "{} {} lyrics".format(track, artist)
                link = self.vet_search_results(track_length, search_string, search_depth)

            track = {'link': link}
            for key in song:
                track[key] = song[key]

            song_info.append(track)

        return song_info


    def vet_search_results(self, track_length, search_string, search_depth):
        """searches for corresponding YouTube searches for an input song, if there exists
        an acceptable video, return the link. If there is not an acceptable string, return None"""

        # get all videos from YouTube
        videos_search = VideosSearch(search_string, limit=search_depth)

        link = None

        for index, video in enumerate(videos_search.result()['result']):
            title = video['title']
            video_length = minutes_to_ms(video['duration'])

            if self.logging:
                print("\n----------------------------------")
                print(f"Vetting result {title}")
                print(f"Video length of {title} is {video_length}")

            # music videos occasionally have additional noises, and an intro / outro. This checks to see
            # if a song is a music video, and if it is, impose tighter restrictions on time
            if ('video' in title) and (self.within_bounds(track_length, video_length, 1)):
                if self.logging:
                    print(f"Found result {title} within bounds, converting and returning {title}")

                link = video['link']
                break
            # music videos vetted out, now just see if the result is in acceptable bounds
            if self.within_bounds(track_length, video_length, 5):
                if self.logging:
                    print(f"Found result {title} within bounds, converting and returning {title}")

                link = video['link']
                break

        return link

    def download_track(self, url, artist, track, directory, sam_configuration=False, total_data=None):
        try:
            yt = YouTube(url, use_oauth=True, allow_oauth_cache=True)
            video = yt.streams.filter(only_audio=True).first()

            # download the file
            out_file = video.download(output_path=directory)
            base, ext = os.path.splitext(directory + "/" + out_file)

            if sam_configuration:
                new_file = f"{artist} - {track}.m4a"
                new_file = new_file.replace("/", "_")
            else:
                new_file = "" + track + "_" + artist + '.m4a'
                new_file = new_file.replace(" ", "_")
                new_file = new_file.replace("/", "_")

            os.rename(out_file, directory + "/" + new_file)

            total_file = f"{directory}/{new_file}"

            scrubber.m4a_to_mp3(total_file)

            total_file_mp3 = f"{total_file[:-4]}.mp3"

            if total_data is None:
                scrubber.add_metadata(total_file_mp3, artist, track)
            else:
                scrubber.add_metadata(total_file_mp3, artist, track, total_data['album'], total_data['track_number'],
                                      total_data['release_date'])
                scrubber.add_cover_art(total_file_mp3, total_data['album_art'])

            scrubber.fix_file(total_file_mp3, directory)

            if self.logging:
                print("...CONVERTED {}.mp3".format(new_file[:-4]))

            os.remove(total_file)
        except:
            if self.logging:
                print(f"\n\n=======================")
                print(f"| Something went wrong when converting {url}")
                print(f"| for {track} by {artist}")
                print(f"| Ignoring song")
                print(f"=======================")