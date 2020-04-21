emp={
    1001:{
        'ename':'ashish',
        'des.code':'e',
        'dept':'R&D',
        'Basic':20000,
        'HRA':8000,
        'IT':3000},
     1002:{
         'ename':'sushma',
         'des.code':'c',
         'dept':'PM',
         'Basic':30000,
         'HRA':12000,
         'IT':9000},
     1003:{
         'ename':'rahul',
         'des.code':'k',
         'dept':'Account',
         'Basic':10000,
         'HRA':8000,
         'IT':1000},
     1004:{
         'ename':'chahat',
         'des.code':'r',
         'dept':'Front desk',
         'Basic':50000,
         'HRA':20000,
         'IT':2000},
     1005:{
         'ename':'ranjan',
         'des.code':'m',
         'dept':'Engg Mech',
         'Basic':50000,
         'HRA':20000,
         'IT':20000},
     1006:{
         'ename':'suman',
         'des.code':'e',
         'dept':'cse.Engg',
         'Basic':23000,
         'HRA':9000,
         'IT':4400},
     1007:{
         'ename':'tanmay',
         'des.code':'c',
         'dept':'PM',
         'Basic':29000,
         'HRA':12000,
         'IT':10000}}
da={'e':{'des':'Engineer','Da':20000},
    'c':{'des':'Consultant','Da':32000},
    'k':{'des':'Clerk','Da':12000},
    'r':{'des':'Recptionist','Da':15000},
    'm':{'des':'Manager','Da':40000}}

empno=int(input("enter employee number: "))
if empno==1007,1006,1005,1004,1003,1002,1001:
salary=emp[empno]['Basic']+emp[empno]['HRA']+emp[empno]['IT']
print("Employe id: ",empno,"\n",
      "Employe name: ",emp[empno]['ename'],"\n",
      "Department: ",emp[empno]['dept'],"\n",
      "Basic: ",emp[empno]['Basic'],"\n",
      "HRA: ",emp[empno]['HRA'],"\n",
      "IT :",emp[empno]['IT'],"\n",
      "total Salry: ",salary,"\n",
      "Designation code: ",emp[empno]['des.code'])
dacode=da[emp[empno]['des.code']]
print("Designation: ",dacode['des'],"\n",
      "DA: ",dacode['Da'])
