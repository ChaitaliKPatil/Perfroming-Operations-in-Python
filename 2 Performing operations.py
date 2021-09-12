#Q1
a,b,c,d,e,f=1,2,3,4,5,6
print('Q1: Doing Arithmetic\na+b*c-f/c=',a+b*c-f/c)
a=7
b=2
print('\nAddition\t',a+b,end='\n')
print('Subtraction\t',a-b,end='\n')
print('Multiplication\t',a*b,end='\n')
print('Floating pt Division\t',a/b,end='\n')#floating point division
print('Floor Division\t',a//b,end='\n')# Integer division
print('Modulo or Remainder\t',a%b,end='\n')# remainder
print('Exponent\t',a,'raised to',b,'=',a**b,end='\n')# exponents
print('\n\n\n\n\n')




#Q2
print('Q2: Assigning values\n')
a=15
b=4
print(a,' ',b)
a+=b
print(a,' ',b)
a-=b
print(a,' ',b)
a*=b
print(a,' ',b)
a/=b
print(a,' ',b)
a%=b
print(a,' ',b)
a**=b
print(a,' ',b)
a//=b
print(a,' ',b)
print('\n\n\n\n\n')



#Q3
a=15.5
b=4
print('Q3: Assigning values\na=',a,' b=',b)
a+=b
print('Addition: a+=b\na=',a,' b=',b)
a-=b
print('Subtraction: a-=b\na=',a,' b=',b)
a*=b
print('Multiplication: a*=b\na=',a,' b=',b)
a/=b
print('Division: a/=b\na=',a,' b=',b)
a%=b
print('Remainder/modula: a%=b\na=',a,' b=',b)
a**=b
print('Exponent: a**=b\na=',a,' b=',b)
a//=b
print('Floor Division: a//=b\na=',a,' b=',b)
print('\n\n\n\n\n')



#Q4
#Comaperitive test of two numbers or texts using equality and inequality operators
nil=0
num=0
max=1
two=2
maxx=2
cap='A'
low='a'
print('Q4: Comparing values\n1.nil =',nil,'\tnum=',num,'\nEQUALITY TEST\n',nil,'==',num,nil==num,end='\n') #Equality check True
print('2.cap =',cap,'\tlow=',low,'\nEQUALITY TEST\n',cap,'==',low,cap==low,end='\n') #Equality check False
print('3.cap =',cap,'\tlow=',low,'\nINEQUALITY TEST\n',cap,'!=',low,cap!=low,end='\n') #Inequality check True
print('4.nil =',nil,'\tmax=',max,'\nGREATER THAN TEST\n',nil,'>',max,nil>max,end='\n') #Greater than check 
print('5.nil =',nil,'\tmax=',max,'\nLESS THAN TEST\n',nil,'<',max,nil<max,end='\n') #less than check 
print('6.nil =',nil,'\ttwo =',two,'\tmaxx=',maxx,'\nLESS THAN OR EQUAL TO TEST\n',nil,'<=',maxx,nil<=maxx,'\n',two,'<=',maxx,two<=maxx) #less than or equal to check 
print('7.nil =',nil,'\tmax=',max,'\ttwo =',two,'\nGREATER THAN OR EQUAL TO TEST\n',nil,'>=',max,nil>=max,'\n',two,'>=',max,two>=max)
#Greater than or equal to check 
print('\n\n\n\n')




#Q5
print('Q5: Logical operators like and, or, not')
a=True
b=False
print('1.AND LOGIC\na=',a,'\tb=',b,'\ta and b=',a and b)#True and false gives false always
print('a=',a,'\ta and a=',a and a)
print('b=',b,'\tb and b=',b and b)
print('2.OR LOGIC\na=',a,'\tb=',b,'\ta or b=',a or b)#true or false always gives true
print('a=',a,'\ta or a=',a or a)
print('b=',b,'\tb or b=',b or b)
print('3.NOT LOGIC\na=',a,'\tnot a=',not a)#not true is always false and viz.
print('b=',b,'\tnot b=',not b)
print('\n\n\n\n')




#Q6
#Examining conditions: If_Else statements
print('Q6: Examining conditions: If_Else statements\n')
e=input('1.\nEnter value for e: ')
f=input('Enter value for f: ')
e=int(e)
f=int(f)
print(e if (e<f) else f,'\n')
print('\n\n\n\n')





#Q7
print('Q7: Setting precedence')
a=2
b=4
c=8
print('a,b,c values respectively are: ',a,b,c,sep='\t')
#Default precedence and forced addition before multiplication
print('\n1. Default precedence and forced addition before multiplication\nDefault: ',a,'*',c,'+',b,'= ',a*c+b)
print('\nForced: ',a,'*(',c,'+',b,')= ',a*(c+b))
#Default precedence and forced addition before modulo operation
print('\n1. Default precedence and forced addition before modulo\nDefault: ',a,'%',c,'+',b,'= ',a%c+b)
print('\nForced: ',a,'%(',c,'+',b,')= ',a%(c+b))
#Default precedence and forced addition before exponent operation
print('\n1. Default precedence and forced addition before exponent\nDefault: ',a,'**',c,'+',b,'= ',a**c+b)
print('\nForced: ',a,'**(',c,'+',b,')= ',a**(c+b))
#Default precedence and forced subtraction before division
print('\n2. Default precedence and forced subtraction before division\nDefault: ',c,'//',b,'-',a,'= ',c//b-a)
print('\nForced: ',c,'//(',b,'-',a,')= ',c//(b-a))
#Default precedence and forced subtraction before modulo operation
print('\n2. Default precedence and forced subtraction before modulo operation\nDefault: ',c,'%',b,'-',a,'= ',c%b-a)
print('\nForced: ',c,'%(',b,'-',a,')= ',c%(b-a))
print('\n\n\n\n')




#Q8
print('Q8: Casting Datatypes\n8+2= ',8+2)#addition of two integers gives int
print('8.2+6.8= ',8.2+6.8)#addition of two floating point numbers gives number
print('\'8\'+\'2\'= ','\'8'+'2\'\n')#Addition of two strings gives string
#Datatypes
a=input('Enter a no.')
b=input('Enter other no.')
#add the variable values together then display the combined result and its data type – to see a concatenated string value result
print('1. Add the variable values together then display the combined result and its data type – to see a concatenated string value result\n',type(a))
sum=a+b
print('Data Type sum: ',sum,type(sum))
#add the variable values together then display the combined result and its data type – to see a total integer value result
print('\n2. Add the variable values together then display the combined result and its data type – to see a total integer value result')
sum=int(a)+int(b)
print('Data Type sum: ',sum,type(sum))
#cast a variable value then display the result and its data type – to see a total float value
print('\n3. Cast a variable value then display the result and its data type – to see a total float value')
sum=float(sum)
print('Data Type sum: ',sum,type(sum))
#cast an integer representation of a variable value then display the result and its data type – to see a character string value
print('\n4. Cast an integer representation of a variable value then display the result and its data type – to see a character string value')
sum=chr(int(sum))
print('\nData Type sum: ',sum,type(sum))
print('\n\n\n\n')




#Q9
print('Q9: Number Swaping/ Manipulating bits\n')
a=input('Enter value of a: ')
b=input('Enter value of b: ')
print(a,b,sep='\t')
a=int(a)
b=int(b)
a=a^b
b=a^b
a=a^b
print(a,b,sep='\t')