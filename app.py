from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load the model and similarity data
netflix = pickle.load(open('Deployed Model/netflix.pkl', 'rb'))
similarity = pickle.load(open('Deployed Model/similarity.pkl', 'rb'))

# Get the list of shows
shows = netflix['title'].values

@app.route('/', methods=['GET', 'POST'])
def index():
    recommended_shows = []
    if request.method == 'POST':
        selected_show = request.form.get('show')
        if selected_show:
            recommendations = recommend(selected_show)
            recommended_shows = recommendations
    return render_template('index.html', shows=shows, recommendations=recommended_shows)

def recommend(movie):
    movie_index = netflix[netflix['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_shows = []
    for i in movie_list:
        recommended_shows.append(netflix.iloc[i[0]].title)
    return recommended_shows

if __name__ == '__main__':
    app.run(debug=True)
