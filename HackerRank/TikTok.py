# Squarespace
# TikTok Recommendation Engine
# Intern Summer 2022
import json
import os
import sys

class RecommendationEngine(object):
    """ A RecommendationEngine class

    You must implement code in the constructor, `getSimilarityIndex`,
    `getRecommendations` following the spec described in the instructions

    You may also implement private helper methods or other classes as 
    needed.

    """

    def __init__(self, engine_videos, engine_profiles):
        self.__engine_videos = engine_videos # array of video names
        self.__engine_profiles = engine_profiles # dictionary of users with ratings
        self.__num_videos = len(self.__engine_videos)
        pass

    def getSimilarityIndex(self, user_a, user_b):
        # improve runtime for edge case
        if (user_a == user_b):
            return 1
        
        ratings_a = self.__engine_profiles[user_a]
        ratings_b = self.__engine_profiles[user_b]        
        count = 0
        similarity = 0

        for i in range(self.__num_videos):
            if (ratings_a[i] != 0 and ratings_b[i] != 0):
                count += 1
                if (ratings_a[i] == ratings_b[i]):
                    similarity += 1 # both users liked/disliked a video
                else:
                    similarity -= 1 # they have opposing viewpoints
        # avoid divide by 0
        if (count > 0):
            return float(similarity / count)
        return 0
        pass

    # assume there will always be at least 3 videos to recommend
    def getRecommendations(self, user):
        ratings = self.__engine_profiles[user]
        scores = [0] * self.__num_videos
        indices = self.__getRecommendationsHelper(user)

        for i in range(self.__num_videos):
            # user has not seen video
            if (ratings[i] == 0):
                count = 0
                for key in self.__engine_profiles:
                    if (self.__engine_profiles[key][i] != 0):
                        scores[i] += float(self.__engine_profiles[key][i] * indices[key])
                        count += 1
                # avoid divide by 0
                if (count > 0):
                    scores[i] /= float(count)
            # already seen video should not be recommended
            else:
                scores[i] = -2 # makes sure video is on the bottom of recommended list

        output = sorted(zip(scores, self.__engine_videos), reverse = True)[:3]
        return [output[0][1], output[1][1], output[2][1]]
        pass
    
    # preprocess similarity scores
    def __getRecommendationsHelper(self, user):
        indices = {}
        for key in self.__engine_profiles:
            if (key != user):
                indices[key] = self.getSimilarityIndex(key, user)
        return indices
        pass

VIDEOS = [
    'A baby jaguar goes swimming',
    'A ferret shows off his dance moves',
    'A pomeranian puppy in a panda costume',
    'A pro chicken hunter, who was saved from a cage, gets the best birthday gift',
    'A wholesome hummingbird',
    'A wildlife conservationist gets chased by two tigers',
    'A-Punk',
    'Bear suit daredevil',
    'Checkered clown check',
    'Create an eyeshadow look by randomly picking three different colors!',
    'Creating the perfect blue glitter acrylic',
    'Crocs + shaving cream',
    'Donating your phone to frisbee parkour',
    'Drop Dance',
    'HBS Dance',
    'Hey Julie',
    'Hitting home runs everywhere',
    'Laxed (SIREN BEAT)',
    'Lots of effort, but still a basketball fail',
    'Lottery',
    'Man vs Wild: Roach Edition',
    'Multicolor hair highlights',
    'No hands needed here',
    'Not the pet we expected to be waiting at the door',
    'Obsessed Dance',
    'Old Town Road - Remix',
    'Roses (Imanbek Remix)',
    'Scary Spooky Skeleton',
    'Six different festival fashion trends',
    'Stunnin',
    'Supalonely',
    'Swimming pool fun takes a hilarious twist',
    'Talk about focus',
    'That contour and highlight, though!',
    'The 223',
    'The Chucky Cheese',
    'The Git Up',
    'The Woah',
    'The goodest dachshund puppies',
    'They did surgery on a banana!',
    'This puppy shares his life story',
    'Try not to flinch',
    'Unicorn-colored braid!',
    'What’s going on inside this cat’s head?',
    'When a hamster isn’t so cute and cuddly',
    'When being fans of different teams gets in the way of love',
    'When the beat distracts you from the game',
    'World record experiment'
]

PROFILES = {
    'Angel': [0, 0, -1, 0, 1, 0, 0, 0, 0, 0, 0, -1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, -1, 0, 0, -1, 0, 0, 0, 0, 1, 1, 0, -1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, -1, 0, 0, -1],
    'Anisha': [-1, 1, -1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, -1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, -1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, -1, 0, 0, 0],
    'Anne': [0, -1, -1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, -1, 0, -1, 0, -1, 0, 0, 1, 1, 0, 0, 1, -1, 0, 1, 1, 0, 0, 0, 0, 1, -1, -1, 0, 1, 0, 0, 0, -1, 0, 0, 1, 0, 0, -1],
    'Ashley': [0, 0, 0, 0, 0, 0, 1, -1, 1, -1, 0, 0, 0, 0, 0, 0, 0, 1, 0, -1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, -1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 1],
    'Brett': [0, 0, 0, 0, 1, 0, 0, 0, 1, -1, 0, -1, 1, 0, 0, 0, 1, 0, 1, 0, -1, 0, 0, 0, 0, 0, 0, -1, 1, 0, 0, -1, 0, -1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
    'Bryce': [-1, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, -1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 1, 0],
    'Calvin': [0, 0, 0, 0, -1, 1, 1, 0, 0, -1, -1, -1, -1, 0, -1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, -1, -1, 0, -1, -1, -1, -1, 1, -1, 1, -1, 1, 0, 0, 0, 1, 0, -1, 1, 0, -1, -1, 0],
    'Carah': [0, 1, 0, 0, 0, 0, -1, 0, 0, 1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, -1, -1, 0, 0, 0, 1, 0, -1, 0, -1, 0, -1, 0, 0, 0],
    'David': [0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, -1, 0, 1, 0, 0, 1, 0, -1, 0, 0, 0, 0, 1, 0, -1, -1, 1, 0, 0, 0, 0, 0, 1, 0, -1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, -1, 0],
    'Delanie': [0, 0, -1, 0, 1, 0, 1, 0, -1, 0, 0, 0, 0, 1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, -1, 1, 0, 0, 0, 0, 1, 1, 0, 0, -1],
    'Eddie': [1, 1, 1, 1, 0, 1, 0, 0, -1, -1, 0, 0, 0, 0, 0, 1, 0, -1, 0, 0, 0, 0, 0, 1, 0, -1, 0, -1, 0, 0, -1, 0, 0, 1, 1, 1, 0, 0, -1, 1, 0, -1, -1, 1, 0, 0, 0, 0],
    'Emily': [-1, 1, -1, 0, 0, 0, 0, 0, 1, 1, -1, -1, 1, -1, -1, -1, 1, 0, 1, -1, -1, 0, 1, -1, -1, 1, 0, -1, 0, 0, -1, 0, 0, -1, 0, -1, 0, 0, 1, 0, -1, -1, -1, -1, -1, 0, 1, 1],
    'Eva': [0, 1, -1, 0, 0, 0, 0, 0, 1, -1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, 1, 1, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, -1, 0, 1, -1, 0, 1, 1, 0, 0, 0],
    'George': [0, 0, 0, -1, 1, 0, 0, 1, 0, 1, 0, 1, -1, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, -1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, -1, 0, 0, -1, 0, 1, 0, 0, 1],
    'Ida': [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, -1, -1, -1, 1, 0, 1, -1, 0, 1, 1, 0, 0, 0, 0, -1, 0, 0, -1, 1, 0, 0, 1, -1, 0],
    'Ijemma': [0, 1, 0, 1, -1, 0, 1, -1, 1, -1, 0, -1, 0, -1, 1, 1, -1, 0, -1, 1, 0, -1, 1, 1, 0, 1, 0, 0, -1, -1, 0, 0, -1, -1, 0, 0, 0, 0, 1, -1, 0, 0, -1, 1, 1, 0, -1, 0],
    'Jackie': [1, 1, 1, 0, 0, 0, 0, 1, 1, 1, -1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, -1, -1, 0, 0, -1, -1, 0, 1, -1, 0, 0],
    'Janet': [0, 0, 0, -1, -1, -1, 0, 0, -1, 1, -1, 1, -1, 1, 1, -1, 0, 1, 1, -1, 0, 0, -1, -1, 1, -1, 1, 1, 1, -1, 1, 1, 1, 1, 1, 1, 0, 1, -1, 1, 0, 0, 1, -1, -1, 1, 1, 1],
    'Jasmine': [0, 0, 0, 0, -1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, -1, 1, 0, 0, -1, 1, 0, 1, 0, 0, 0, -1, 1, 1, -1, 0, -1, 0, -1, 0, -1, 0, 0, 0, 0],
    'Jason': [0, -1, 0, 1, -1, 0, 0, -1, 1, -1, 1, 1, 0, 1, -1, 1, 0, 0, 0, 1, 1, 0, -1, 1, 1, 1, -1, 1, 0, 0, -1, 1, -1, 0, 1, -1, 0, 0, 1, -1, 0, 1, 1, 1, 1, -1, -1, 1],
    'Jessie': [0, 0, 0, 0, 0, -1, 0, 0, 1, 1, 0, -1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, -1, 0, 0, 0, 0, 0, 1, 0, 0, -1, 0, 0, 1, 0, 0],
    'Jewel': [1, 0, -1, 0, 1, 0, 0, 1, 0, 1, 0, 1, -1, -1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, -1, 0, -1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1],
    'Joanna': [1, -1, -1, -1, -1, -1, -1, 1, 0, 0, 1, 1, -1, 0, 1, -1, 0, -1, -1, -1, 0, 0, -1, -1, 0, 0, 1, 0, 0, 0, 1, 0, 1, -1, 1, 1, 1, -1, 1, 1, 1, 1, -1, 0, 1, -1, 1, -1],
    'Joel': [-1, -1, -1, 0, 1, -1, -1, 1, 1, 0, 1, -1, 1, 1, 0, -1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, -1, 0, -1, 0, -1, -1, 0, 0, -1, 1, -1, -1, 0, -1, -1, 0, 0, 0, 1, -1, 1, -1],
    'Jon': [1, 0, -1, 1, -1, -1, 0, -1, 0, 0, 0, 0, 0, 1, 0, -1, 0, 0, 1, -1, 0, 0, -1, 1, -1, -1, -1, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, -1, 0, 1, 1, 1, 0, 0, 0],
    'Julia': [1, 1, -1, -1, 0, 1, 1, 1, 1, -1, 1, 1, 1, 0, 1, -1, 1, -1, 0, 1, 1, -1, 1, 1, 0, -1, 1, 0, -1, -1, 0, 1, 1, 0, 0, -1, -1, 0, 1, 0, 1, 1, -1, 0, -1, 0, 0, 1],
    'Julian': [-1, 0, -1, -1, 0, -1, -1, -1, -1, 1, 0, -1, 1, -1, -1, 1, 1, -1, -1, 0, -1, 0, -1, 0, -1, -1, 0, 1, 0, 0, 1, 1, 0, 1, -1, 0, -1, -1, 0, 0, -1, 1, -1, 0, 1, -1, 1, 0],
    'Katey': [0, 0, 0, 0, -1, 0, 0, 0, 0, -1, -1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, -1, 1, 0, -1, 0, 0, 1, 1, 0, 0, -1, 0, 1, 0, 0, -1, 0, 0],
    'Kevin': [0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, -1, 0, 1, 0, 0, -1, -1, -1, 0, 0, -1, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, -1, 0, 0],
    'Mackenzie': [1, 1, -1, 0, 0, 1, 0, -1, -1, -1, 0, 0, 0, 0, 0, 0, 1, 0, 0, -1, -1, 0, 0, 1, 0, 0, -1, 0, 0, 0, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0, 1, 0, 0, 1, -1, 0, 0, 0],
    'Mariya': [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, -1, 0, -1, 0, 0, 0, 0, -1, 0, 1, -1, 0, -1, 0, 0, -1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    'Matt': [0, 1, 1, 1, 1, -1, 0, 0, 0, -1, -1, 0, -1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, -1, -1, 0, 1, 1, -1, 1, -1, -1, -1, 1, 1, 0, 1, 1, -1, 0, -1, 0, 0, -1, -1, -1, 1, 0],
    'Mika': [0, 0, 0, -1, 0, 0, 0, -1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, -1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, -1, 0, -1, -1, -1, 1, -1, 0, -1, 1, 0, -1, 0, 0, 0, 0, 0],
    'Nathan': [0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, -1, 1, -1, 1, 1, 0, 1, 1, 0, -1, 0, 0, 0, 0, 0, 1, 1, -1, -1, 1, -1, 0, -1, 1, 0, 1, -1, 0, 1, 1, 0, 0],
    'Nick': [0, -1, -1, 0, 1, -1, -1, 1, -1, 0, -1, 1, 0, 1, 1, 1, -1, 0, -1, 1, 1, 0, 1, -1, -1, 0, 0, 1, 1, -1, 1, 1, -1, -1, 0, 1, -1, 0, 0, -1, 1, -1, 0, -1, 1, 0, 1, -1],
    'Pat': [0, -1, 0, -1, -1, 0, 0, 0, 0, 0, 0, -1, -1, 0, -1, -1, 0, 0, -1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, -1, -1, 0, 1, 1, 1, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0],
    'Piper': [1, -1, 0, -1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, -1, 0, -1, 0, 0, -1, -1, 1, 0, 0, 0, 1, -1, 1, -1, 0, 0, -1, 0, 0, -1, 0, 1, 0, -1, 0, 1, 1, -1, 0, 0, 0],
    'Ramphis': [0, 0, 1, 1, 0, 1, 1, 0, 0, -1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, -1, 1, 0, 1, 1, -1, -1, 0, -1, 0, 1, -1, 0, 0, 0, 1, 0, -1, 1, -1, 0, 1, 1, 1, -1, 1, -1],
    'Rose': [0, 0, 0, -1, 1, 0, 0, 0, 0, -1, 1, 1, -1, 1, 1, -1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, -1, 0, 0, 0, 0, -1, 0, 1, -1, 0, 0, 1, -1, 0, 0, -1, 0, -1, 0, -1, -1],
    'Ryan': [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, -1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, -1, 1, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    'Selma': [0, 0, 0, 1, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, -1, 0, -1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, -1, 1, 0, -1, 0, 0, 0, 0, -1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
    'Skyler': [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, -1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, -1, -1, 0, 1, 0, 0, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 1, -1],
    'Steve': [0, 0, 1, -1, 1, 1, 0, 1, 0, 1, -1, -1, -1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 1, -1, -1, 0, 0, -1, -1, 0, -1, -1, 0, 0, 0, 0, 0, 1, 1],
    'Su': [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, -1, 0, 0, 0, 1, 0, -1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, -1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0],
    'Tiffany': [0, 0, 0, -1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, -1, 0, 0, 0, -1, 0, 0, -1, 0, 1, -1, 0, -1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, -1],
    'Trent': [-1, 0, 0, 0, 0, 1, 0, 0, -1, 1, 0, 0, 1, 0, -1, 1, 1, 1, -1, 1, 0, 0, 1, 0, 0, -1, 0, 0, 0, 1, -1, 0, 0, 1, 0, 0, 0, -1, 0, 0, 0, -1, 0, 0, 0, -1, -1, 0],
    'Vivi': [0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 1, 0, -1, 0, 0, -1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, -1, 1, 0, 1, -1, 0, 0, -1, 0, -1, 0, 0, 0],
    'Xiaodan': [1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, -1, -1, -1, 0, 0, 0, -1, 0, 0, 0, 1, 1, 0, 0, -1, 0, 1, 0, 0, 1, 0, 0, -1, 1, 1, 0, 0, 1, -1, 0, 0, 1, 0, 0, 0],
    'Zach': [0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, -1, -1, 0, 0, 1, -1, 0, 0, 0, 0, -1, -1, -1, 0, 0, -1, -1, 0, 0, 1, 1, -1, 0, -1, 0, 0, 0, 0, 0, 1, 0, 1],
    'Ziggy': [1, 1, 1, -1, 0, 0, 1, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, -1, -1, 0, -1, 0, 0, -1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, -1, 1, -1, 0, 0],
    'Zoe': [0, 0, -1, -1, 0, 0, 1, 0, 0, 0, 0, 1, -1, 0, 1, 1, -1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, -1, 0, -1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
}

RECOMMENDATION_ENGINE = RecommendationEngine(VIDEOS, PROFILES)


# Hackerrank miscellaneous - Please Ignore
if __name__ == '__main__':
    FPTR = open(os.environ['OUTPUT_PATH'], 'w')

    for line in sys.stdin:
        input_bits = line.rstrip().split(',')

        func = input_bits[0]
        arg1 = input_bits[1]

        if len(input_bits) == 3:
            arg2 = input_bits[2]

        break

    if len(input_bits) == 3:
        RES = getattr(RECOMMENDATION_ENGINE, func)(arg1, arg2)
    else:
        RES = getattr(RECOMMENDATION_ENGINE, func)(arg1)

    if isinstance(RES, float):
        RES = round(RES, 2)
        FPTR.write('"{:.2f}"'.format(RES))
    else:
        FPTR.write(json.dumps(RES, separators=(',', ':')))
    FPTR.close()