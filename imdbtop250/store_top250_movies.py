

def store_movie_data_to_db(movie_data):
    print(movie_data)
    sel_sql =  "SELECT * FROM top_250_movies WHERE id =  %d" % (movie_data['movie_id'])

    try:
        cursor.execute(sel_sql)
        result = cursor.fetchall()
    except:
        print("Failed to fetch data")
    if result.__len__() == 0:
        sql = "INSERT INTO top_250_movies id, name, year, rate)  VALUES ('%d', '%s', '%d', '%f')" %  (movie_data['movie_id'], movie_data['movie_name'], movie_data['year'], movie_data['movie_rate'])
        try:
            cursor.execute(sql)
            db.commit()
            print("movie data ADDED to DB table top_250_movies!")
        except:
            # 发生错误时回滚
            db.rollback()
    else:
        print("This movie ALREADY EXISTED!!!")
