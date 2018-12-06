def main():
    try:
        for movie in get_top250_movies_list():
            store_movie_data_to_db(movie)
            get_movie_detail_data(movie)
    finally:
        db.close()


if __name__ == '__main__':
    main()
