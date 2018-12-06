def store_director_data_in_db(movie):
    sel_sql = "SELECT * FROM directors \
               WHERE id =  %d" % (movie['director_id'])

    try:
        # 执行sql语句
        cursor.execute(sel_sql)
        # 执行sql语句
        result = cursor.fetchall()

    except:
        print("Failed to fetch data")

    if result.__len__() == 0:
        sql = "INSERT INTO directors \
                            (id, name) \
                         VALUES ('%d', '%s')" % \
              (movie['director_id'], movie['director_name'])
        try:
            # 执行sql语句
            cursor.execute(sql)
            # 执行sql语句
            db.commit()
            print("Director data ADDED to DB table directors!", movie['director_name'] )
        except:
            # 发生错误时回滚
            db.rollback()
    else:
        print("This Director ALREADY EXISTED!!")

    sel_sql = "SELECT * FROM direct_movie \
                   WHERE director_id =  %d AND movie_id = %d" % (movie['director_id'], movie['movie_id'])

    try:
        # 执行sql语句
        cursor.execute(sel_sql)
        # 执行sql语句
        result = cursor.fetchall()

    except:
        print("Failed to fetch data")

    if result.__len__() == 0:
        sql = "INSERT INTO direct_movie \
                                (director_id, movie_id) \
                             VALUES ('%d', '%d')" % \
              (movie['director_id'], movie['movie_id'])
        try:
            # 执行sql语句
            cursor.execute(sql)
            # 执行sql语句
            db.commit()
            print("Director direct movie data ADD to DB table direct_movie!")
        except:
            # 发生错误时回滚
            db.rollback()
    else:
        print("This Director direct movie ALREADY EXISTED!!!")
