#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 21:36:05 2017

@author: sss
"""

def song_playlist(songs, max_size):
    """
    songs: list of tuples, ('song_name', song_len, song_size)
    max_size: float, maximum size of total songs that you can fit

    Start with the song first in the 'songs' list, then pick the next 
    song to be the one with the lowest file size not already picked, repeat

    Returns: a list of a subset of songs fitting in 'max_size' in the order 
             in which they were chosen.
    """
    result = []
    size_taken = 0
    first_song = songs[0]
    # first song size larger than max_size
    if first_song[2] > max_size:
        return result
    # first song can be added
    result.append(first_song[0])
    size_taken += first_song[2]
    other_songs = songs[1:]
    other_songs.sort(key=lambda x: x[2])
#    print(other_songs)
#    print(size_taken)
#    print("max size:", max_size)
    while len(other_songs) > 0 and (size_taken + other_songs[0][2] <= max_size): 
        """
        !!! 怎么犯了这样的错误？上面需要将剩余 songs 第一首 size 和 size_taken 相加后与
        max_size 比较！！！
        """
        song = other_songs[0]
#        print(song)
#        print("size taken in while:", size_taken, "max_size", max_size)
        result.append(song[0])
        other_songs.remove(song)
        size_taken += song[2]
#    print("size taken:", size_taken)
    return result
    
    
songs_one = [('Roar',4.4, 4.0),('Sail',3.5, 7.7),('Timber', 5.1, 6.9),('Wannabe',2.7, 1.2)]
max_size_one = 12.2

max_size_two = 11

