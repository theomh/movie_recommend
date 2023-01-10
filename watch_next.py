# A program to recommend a suggestion of what to watch next using NLP and semantic similarity.

import spacy  # import spacy module

nlp = spacy.load('en_core_web_md')  # import medium language model

hulk_desc = """Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, 
the Illuminati trick Hulk in to a shuttle and launch him into space to a planet where the Hulk can live in 
peace. Unfortunately, Hulk lands on the planet Sakaar where he is sold into slavery and trained as a gladiator."""


# Function to return what to watch next from fed in description  =====================

def watch_next(find_recommendation):
    desc_list = []
    movie_list = []
    best_recommendation = 0

    with open('movies.txt', 'r') as movies:  # Load in Movie, Desc. from file.
        for line in movies:
            movie, desc = line.split(" :")
            desc = desc.strip("\n")
            movie_list.append(movie)
            desc_list.append(desc)
        movies.close()

    for desc in desc_list:
        similarity = nlp(desc).similarity(find_recommendation)
        title_index = desc_list.index(desc)
        #print((movie_list[title_index], similarity))  # prints title & similarity
        if similarity > best_recommendation:  # get greatest similarity and update recommendation on this
            best_recommendation = similarity
            title_to_recommend = movie_list[title_index]
    return title_to_recommend  # return recommendation

# Main =====================


model_desc = nlp(hulk_desc)  # Process desc. in

print(f"You should watch {watch_next(model_desc)}!")  # Pass to function to return recommendation.
