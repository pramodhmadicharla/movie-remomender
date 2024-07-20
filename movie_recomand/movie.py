import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# Sample movie data
movies = [
    {"title": "Inception", "genres": ["Action", "Sci-Fi"], "rating": 8.8},
    {"title": "The Matrix", "genres": ["Action", "Sci-Fi"], "rating": 8.7},
    {"title": "The Shawshank Redemption", "genres": ["Drama"], "rating": 9.3},
    {"title": "The Godfather", "genres": ["Drama"], "rating": 9.2},
    {"title": "Pulp Fiction", "genres": ["Crime", "Drama"], "rating": 8.9},
    {"title": "The Dark Knight", "genres": ["Action", "Crime"], "rating": 9.0},
]

def get_user_preferences():
    """Get user's genre preferences and minimum rating."""
    genres = genres_entry.get().split(',')
    genres = [genre.strip() for genre in genres]
    try:
        min_rating = float(rating_entry.get())
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid rating.")
        return None, None
    return genres, min_rating

def recommend_movies(genres, min_rating):
    """Recommend movies based on user preferences."""
    recommendations = []
    for movie in movies:
        if any(genre in movie["genres"] for genre in genres) and movie["rating"] >= min_rating:
            recommendations.append(movie)
    return recommendations

def show_recommendations():
    """Display movie recommendations."""
    genres, min_rating = get_user_preferences()
    if genres is None or min_rating is None:
        return
    recommendations = recommend_movies(genres, min_rating)
    
    result_text = ""
    if recommendations:
        for movie in recommendations:
            result_text += f"Title: {movie['title']}, Genres: {', '.join(movie['genres'])}, Rating: {movie['rating']}\n"
    else:
        result_text = "No movies match your criteria."
    
    result_label.config(text=result_text)

# Create the main window
root = tk.Tk()
root.title("Movie Recommendation System")

# Load and set the background image
image_path = "C:/Users/LENOVO/projects/movie_recomand/movie1.jpeg"
bg_image = Image.open(image_path)
bg_image = bg_image.resize((800, 600), Image.Resampling.LANCZOS)
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = tk.Label(root, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Create and place widgets
title_label = tk.Label(root, text="Movie Recommendation System", font=("Arial", 24, "bold"), bg="black", fg="white")
title_label.pack(pady=20)

frame = tk.Frame(root, bg="black")
frame.pack(pady=10)

tk.Label(frame, text="Enter preferred genres (comma-separated):", font=("Arial", 14), fg="white", bg="black").grid(row=0, column=0, padx=10, pady=10)
tk.Label(frame, text="Enter minimum rating (0-10):", font=("Arial", 14), fg="white", bg="black").grid(row=1, column=0, padx=10, pady=10)

genres_entry = tk.Entry(frame, font=("Arial", 14))
genres_entry.grid(row=0, column=1, padx=10, pady=10)

rating_entry = tk.Entry(frame, font=("Arial", 14))
rating_entry.grid(row=1, column=1, padx=10, pady=10)

calculate_button = tk.Button(root, text="Get Recommendations", command=show_recommendations, font=("Arial", 14), fg="black", bg="white")
calculate_button.pack(pady=20)

result_label = tk.Label(root, text="", font=("Arial", 16), bg="black", fg="white")
result_label.pack(pady=10)

# Start the main loop
root.geometry("800x600")  # Set the initial window size
root.mainloop()
