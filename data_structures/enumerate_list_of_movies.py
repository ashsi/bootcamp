""" Use enumerate to loop over movie names in a list. """

# Store 5 favourite movies.
movies = ["The Big Short", "The Menu", "Howl's Moving Castle", "Fight Club", "Monty Python's Life of Brian"]

# Print numbered movie names.
for i, movie in enumerate(movies, start=1):
    print(f"Movie {i}: {movie}.")
