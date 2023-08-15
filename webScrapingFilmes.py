#Lista de dicionários com os filmes
movies = [{"titulo": "O senhor dos Anéis", "ano": 2001, "avaliacao": 8.8}, {"titulo": "Matrix", "ano": 1999, "avaliacao": 9.3}, {"titulo": "Interestelar", "ano": 2014, "avaliacao": 8.6}]

#Função que calcula a média de avaliação dos filmes
def movieRatingAverage(movies):
    rating = [movie["avaliacao"] for movie in movies]

    averageRating = sum(rating) / len(rating)

    return f"A média das avaliações dos filmes é {averageRating}"

#Função que mostra o título com a maior avaliação
def bestRating(movies):
    highestRating = max(movies, key=lambda movie: movie["avaliacao"])

    return f"A maior avaliação entre os filmes é a do filme " + highestRating["titulo"]

#Função que mostra o ano do filme com pior avaliação
def worstRating(movies):
    badRating = min(movies, key=lambda movie: movie["avaliacao"])

    return f"A pior avaliação entre os filmes é a do filme lançado no ano de " + str(badRating["ano"])

print(f"Esses são os filmes e suas informações: {movies}")
print(movieRatingAverage(movies))
print(bestRating(movies))
print(worstRating(movies))
