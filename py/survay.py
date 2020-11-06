from flask import Flask,render_template,request
import sqlite3 as sql
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('page1.html')

@app.route("/page2",methods=['POST','GET'])
def page2():
    if request.method=='POST':
        try:
            result=request.form
            surname=result['surname']
            fullName=result['FullNames']
            contact=result['Contact']
            date=result['Date']
            age =result['Age']
            out=result['out']
            movies=result['movies']
            tv=result['TV']
            radio=result['radio']
            key=list(result.keys())
            pizz,pasta,papa,chicken,beef,other='','','','','',''
            if 'Pizza'in key:
                pizz =result['Pizza']
            if 'Pasta'in key:
                pasta =result['Pasta']
            if 'PapandWors'in key:
                papa =result['PapandWors']
            if 'Chicken'in key:
                chicken =result['Chicken']
            if 'Beef'in key:
                beef =result['Beef']
            if 'other'in key:
                other =result['other']

            with sql.connect('database.db') as con:
                cur=con.cursor()

                cur.execute('INSERT INTO survey (surname,fullname,contact,date,age,pizza,pasta,pap,chicken,beef,other,movies,tv,radio,out)'
                            'VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',(surname,fullName,contact,date,age,pizz,pasta,papa,chicken,beef,other,movies,tv,radio,out))
                con.commit()

                msg='rescord updated successfully'
                return render_template('page1.html')
        except :
            #con.rollback()
            msg ='Error accured'
            print(msg)



    return render_template('page2.html')
@app.route("/page3")
def page3():
    con=sql.connect('database.db')
    con.row_factory=sql.Row

    sumOfAge=0
    cur=con.cursor()
    result={}
    pizz,pasta,pap,=0,0,0
    out,movies,tv,radio=0,0,0,0
    try:
        cur.execute('SELECT * FROM survey ')
        rows=cur.fetchall()
        youngest = rows[0]['Age']
        oldest = rows[0]['Age']
        total=len(rows)
        test='true'
        for x in rows:
            sumOfAge=sumOfAge+x['Age']
            if youngest>x['Age']:
                youngest = x['Age']
            if oldest<x['Age']:
                oldest = x['Age']
            if x['pizza']==test:
                pizz=+1
            if x['pasta']==test:
                pasta=+1
            if x['pap']==test:
                pap=+1
            if x['out']=='op1' or x['out']=='op2':
                out =out+1
            if x['movies']=='op1' or x['movies']=='op2' :
                movies = movies+1
            if x['tv']=='op1' or x['tv']=='op2':
                tv = tv+1
            if x['radio']=='op1' or x['radio']=='op2':
                radio =radio +1

        avAge=sumOfAge/total
        perPizza=round((pizz/total)*100,2)
        perPasta = round((pasta / total) * 100,2)
        perPap = round((pap / total) * 100,2)
        avOut=round(out/total,2)
        avMovies=round(movies/total,2)
        avTv=round(tv/total,2)
        avRadio=round(radio/total,2)
        result['total']=total
        result['avAge'] = avAge
        result['youngest'] = youngest
        result['oldest'] = oldest
        result['pizza'] = perPizza
        result['pap'] = perPap
        result['pasta'] = perPasta
        result['avOut'] = avOut
        result['avMovies'] = avMovies
        result['avTv'] = avTv
        result['avRadio'] = avRadio
        return render_template('page3.html', rows=result)
    except :
        print('erro in table')
        return render_template('/')



if __name__ == "__main__":
    app.run(debug=True)