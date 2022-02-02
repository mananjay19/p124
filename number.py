from flask import Flask,request,jsonify
app=Flask(__name__)

tasks = {
    "data":[
    {
        'id':1,
        'name':u'Raju',
        'number':u'9830478934',
        'done':False
    },
     {
        'id':2,
        'name':u'Raul',
        'number':u'7895463215',
        'done':False
    },
    {
        'id':3,
        'name':u'haly',
        'number':u'6483698647',
        'done':False
    } 
    ] 
}
@app.route('/get-data')
def gettask():
    return jsonify({
        'data':tasks
    })
@app.route('/add-data',methods=['POST'])
def addtask():
    if not request.json:
        return jsonify({
            'status':'error',
            'message':'please provide the data in json format'
        },400)
    task={
        'id':tasks[-1]['id']+1,
        'name':request.json['name'],
        'number':request.json.get('number',""),
        'done':False
    }
    tasks.append(task)
    return jsonify({
            'status':'success',
            'message':'task added successfully'
        },400)
if(__name__=='__main__'):
    app.run(debug=True)