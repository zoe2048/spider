def store_actor_data_to_db(actor, movie):
    sel_sql = "SELECT * FROM actors \
           WHERE id =  %d" % (actor['actor_id'])

    try:
        # 执行sql语句
        cursor.execute(sel_sql)
        # 执行sql语句
        result = cursor.fetchall()

    except:
        print("Failed to fetch data")

    if result.__len__() == 0:
        sql = "INSERT INTO actors \
                        (id, name) \
                     VALUES ('%d', '%s')" % \
              (actor['actor_id'], actor['actor_name'])

        try:
            # 执行sql语句
            cursor.execute(sql)
            # 执行sql语句
            db.commit()
            print("actor data ADDED to DB table actors!")
        except:
            # 发生错误时回滚
            db.rollback()
    else:
        print("This actor has been saved already")

    sel_sql = "SELECT * FROM cast_in_movie \
               WHERE actor_id =  %d AND movie_id = %d" % (actor['actor_id'], movie['movie_id'])
    try:
        # 执行sql语句
        cursor.execute(sel_sql)
        # 执行sql语句
        result = cursor.fetchall()

    except:
        print("Failed to fetch data")

    if result.__len__() == 0:
        sql = "INSERT INTO cast_in_movie \
                        (actor_id, movie_id) \
                     VALUES ('%d', '%d')" % \
              (actor['actor_id'], movie['movie_id'])

        try:
            # 执行sql语句
            cursor.execute(sql)
            # 执行sql语句
            db.commit()
            print("actor casted in movie data ADDED to DB table cast_in_movie!")
        except:
            # 发生错误时回滚
            db.rollback()
    else:
        print("This actor casted in movie data ALREADY EXISTED")
