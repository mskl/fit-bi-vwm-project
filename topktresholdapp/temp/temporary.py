'''<td class="product_parameter">
                    <span style="width:{{row[0].acceleration%">{{row[0].acceleration}}%</span>
                </td>
                <td class="product_parameter">
                    <span style="width:{{row[0].speed}}%">{{row[0].speed}}%</span>
                </td>
                <td class="product_parameter">
                    <span style="width:{{row[0].handling}}%">{{row[0].handling}}%</span>
                </td>'''

#@app.route('/param', methods=['GET'])
#def param():
#    sort_parameter = ""
#    if request.method == "GET":
#        sort_parameter = request.args.get('single')
#
#    if sort_parameter == "accel":
#        return render_template("param.html", title='Acceleration', data=car_database.get_accel())
#    elif sort_parameter == "speed":
#        return render_template("param.html", title='Speed', data=car_database.get_speed())
#    elif sort_parameter == "handl":
#        return render_template("param.html", title='Handling', data=car_database.get_handl())


'''
    if arg_sortby is not None:
        if arg_sortby == "accel":
            return render_template("index.html", title='Index', database=car_database.get_accel())
        elif arg_sortby == "speed":
            return render_template("index.html", title='Index', database=car_database.get_speed())
        elif arg_sortby == "handl":
            return render_template("index.html", title='Index', database=car_database.get_handl())
        else:
            return error()
    elif arg_agreg is not None:
        if arg_agreg == "naive_sum":
            return render_template("index.html", title='Index',
                                   database=car_database.naive_rank_sort(a, s, h, CarDatabase.agregate_sum))
        elif arg_agreg == "naive_max":
            return render_template("index.html", title='Index',
                                   database=car_database.naive_rank_sort(a, s, h, CarDatabase.agregate_max))
        else:
            return error()
'''

# <!-- <input type="submit" value="Sort by parameters"> -->