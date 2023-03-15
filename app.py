from flask import Flask,render_template
from flask_restful import Api,Resource


app=Flask(__name__)
api=Api(app)

location={"1":"Jersey+City,New+York+NY","2":"New+York"}
#"/google_api/Jersey+City,New+York+NY&New+York"
#http://127.0.0.1:5000/google_api/Jersey+City,New+York+NY&New+York


@app.route("/google_api/<ori_des>",methods = ['POST', 'GET'])
def render_map(ori_des:str):
        has_divider=ori_des.find("&")
        print(ori_des)
        if has_divider==-1:
            return print("error & character not found")
        ori=ori_des[:has_divider]
        des=ori_des[has_divider+1:]
        return render_template('template.html', ori=ori,des=des)



@app.route('/')
def hello():
    return render_template('teste_1_ITW.html')
#api.add_resource(render_map,"/google_api/<string:ori_des>")
# class render_map(Resource):
#     def get(self,ori_des:str):
#         has_divider=ori_des.find("&")
#         if has_divider==-1:
#             return print("error & character not found")
#         ori=ori_des[:has_divider]
#         des=ori_des[has_divider+1:]

#         render_template('template.html', ori=ori,des=des)
#         return 


"""
<iframe width="600" height="450" style="border:0" loading="lazy" allowfullscreen
 src="https://www.google.com/maps/embed/v1/directions?origin=Jersey+City,New+York+NY&destination=place_id:ChIJqXwSpAFZwokR28_WgZDMzb4&key=AIzaSyBHQUnv5VzxQpzCHrFGvKDLPgkkGHp_0_0"></iframe> 
 """