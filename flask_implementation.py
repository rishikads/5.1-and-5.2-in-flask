from flask import Flask , request , url_for
app = Flask(__name__)

def ERP_51(body):
  revolution={}
    #u1=int(input("Enter the number of 2nd year UG students "))
    #u2=int(input("Enter the number of 3rd year UG students "))
    #u3=int(input("Enter the number of 4th year UG students "))                
    #p1=int(input("Enter the number of 1st year PG students "))
    #p2=int(input("Enter the number of 2st year PG students "))
    #F=int(input("Total Number of faculty Members in the department "))

  u1=int(body['u1'])
  u2=int(body['u2'])
  u3=int(body['u3'])
  p1=int(body['p1'])
  p2=int(body['p2'])
  F=int(body['F'])
  S=u1+u2+u3+p1+p2
  SFR=S/F
  revolution["result"]={}
  revolution["result"]['sfr']=float(SFR)
  revolution["result"]['u1']=u1
  revolution["result"]['u2']=u2
  revolution["result"]['u3']=u3
  revolution["result"]['p1']=p1
  revolution["result"]['p2']=p2
  revolution["result"]['F']=F
  print("No of students in the department= " +str(S))
  print("Student faculty ratio= " +str(SFR))
  print(revolution)
  return SFR
    #Avg_SFR=(revolution[2019]['sfr'] + revolution[2020]['sfr'] + revolution[2021]['sfr'])/3
    #print("average SFR= " +str(Avg_SFR))
    #if Avg_SFR<=15:
    #  score=20
    #elif Avg_SFR<=17:
    #  score=18
    #elif Avg_SFR<=19:
    #  score=16
    #elif Avg_SFR<=21:
    #  score=14
    #elif Avg_SFR<=23:
    #  score=12
    #elif Avg_SFR<=25:
    #  score=10
    #elif Avg_SFR>25:
    #  score=0
    #revolution["Average SFR="]=Avg_SFR
    #print(revolution)
    #print("marks=" +str(score))
    #return score
    
def ERP_52(body):
  professors={}
    #N=int(input("Enter the number of students "))
    #a_F1=int(input("Number of Available Professors "))
    #a_F2=int(input("Number of Associate Professors "))
    #a_F3=int(input("Number of Assistant professors "))
  N=int(body['N'])
  a_F1=int(body['a_F1'])
  a_F2=int(body['a_F2'])
  a_F3=int(body['a_F3'])
  r_F1=1/9*((N/15))
  r_F2=2/9*((N/15))
  r_F3=6/9*((N/15))
  r_F1=round(r_F1)
  r_F2=round(r_F2)
  r_F3=round(r_F3)
  print("Number of professors required in " + "=" + str(r_F1))
  print("Number of Associate professors required in " + "=" + str(r_F2))
  print("Number of Assistant professors required in " + "=" + str(r_F3))
  professors["result"]={}
  professors["result"]['Students']=N
  professors["result"]['Available_professors']=a_F1
  professors["result"]['Available_associate_professors']=a_F2
  professors["result"]['Available_assistant_professors']=a_F3
  professors["result"]['Required_professors']=r_F1
  professors["result"]['Required_associate_professors']=r_F2
  professors["result"]['Required_assistant_professors']=r_F3
    #avg_a_F1=(professors[2019]['Available_professors']+professors[2020]['Available_professors']+professors[2021]['Available_professors'])/3
    #avg_a_F2=(professors[2019]['Available_associate_professors']+professors[2020]['Available_associate_professors']+professors[2021]['Available_associate_professors'])/3
    #avg_a_F3=(professors[2019]['Available_assistant_professors']+professors[2020]['Available_assistant_professors']+professors[2021]['Available_assistant_professors'])/3
    #avg_r_F1=(professors[2019]['Required_professors']+professors[2020]['Required_professors']+professors[2021]['Required_professors'])/3
    #avg_r_F2=(professors[2019]['Required_associate_professors']+professors[2020]['Required_associate_professors']+professors[2021]['Required_associate_professors'])/3
    #avg_r_F3=(professors[2019]['Required_assistant_professors']+professors[2020]['Required_assistant_professors']+professors[2021]['Required_assistant_professors'])/3
    #avg_a_F1=round(avg_a_F1)
    #avg_a_F2=round(avg_a_F2)
    #avg_a_F3=round(avg_a_F3)
    #avg_r_F1=round(avg_r_F1)
    #avg_r_F2=round(avg_r_F2)
    #avg_r_F3=round(avg_r_F3)
    #print("Average available professors="+str(avg_a_F1))
    #print("Average available associate professors="+str(avg_a_F2))
    #print("Average available assistant professors="+str(avg_a_F3))
    #print("Average required assistant professors="+str(avg_r_F1))
    #print("Average required assistant professors="+str(avg_r_F2))
    #print("Average required assistant professors="+str(avg_r_F3))
    #professors['avg']={}
    #professors['avg']['Average_available_professors']=avg_a_F1
    #professors['avg']['Average_available_assistant_professors']=avg_a_F2
    #professors['avg']['Average_available_associate_professors']=avg_a_F3
    #professors['avg']['Average_required_professors']=avg_r_F1
    #professors['avg']['Average_required_assistant_professors']=avg_r_F2
    #professors['avg']['Average_required_assosiate_professors']=avg_r_F3

  if a_F1==a_F2==0:
      CRD=0
  else:
      CRD=((a_F1/r_F1)+((a_F2*0.6)/r_F2)+((a_F3*0.4)/r_F3))*12.5
  if CRD>25:
      CRD=25
  professors['CRD']=CRD
  print("Cadre Ratio Marks "+str(CRD))
  print(professors)
  return CRD

@app.route('/' , methods=['POST'])
def home():
  return "N/O"

@app.route('/5.1' , methods=['POST'])
def ERP51():
  body = request.get_json()
  a = ERP_51(body)
  return str(a)

@app.route('/5.2' , methods=['POST'])
def ERP52():
  body = request.get_json()
  a = ERP_52(body)
  return str(a)

if __name__ == '__main__' :
  app.run(debug=True, port=5000)


