import sys

fibonacci=[1,1]

#Determine nth element in fibonacci in naive way
def fib_naive(n,naive_solution,string=""):
    if n==1:
        naive_solution.write("fib(1) = 1 \n")
        return 1
    elif n==2:
        naive_solution.write("fib(2) = 1 \n")
        return 1
    else:
        string+=f"fib({n}) = fib({n-1}) + fib({n-2}) \n" 
        naive_solution.write(string)
        return fib_naive(n-1,naive_solution)+fib_naive(n-2,naive_solution)
    
#Check the input validity and write correct results in naive solution
def naive(integers,naive_solution):
    dash_character="-"*32
    dash_character_n="-"*32+"\n"
    for number in integers:
        if number<=0:
            naive_solution.write(dash_character_n)
            result="Calculating "+str(number)+". Fibonacci number:"+"\n"
            naive_solution.write(result)
            naive_solution.write("ERROR: Fibonacci cannot be calculated for the non-positive numbers!\n")
            result=f"{number}. Fibonacci number is: nan\n"
            naive_solution.write(result)
        else:
            naive_solution.write(dash_character_n)
            result="Calculating "+str(number)+". Fibonacci number:"+"\n"
            naive_solution.write(result)
            result=fib_naive(number,naive_solution)
            result=str(number)+". Fibonacci number is: "+str(result)+"\n"
            naive_solution.write(result)
            if number==integers[-1]:
                naive_solution.write(dash_character)

#Determine nth element in fibonacci in eager way
def fib_eager(n,iterate,eager_solution,string=""):
    if  n>len(fibonacci):
        string=f"fib({n}) = fib({n-1}) + fib({n-2}) \n"
        eager_solution.write(string)
        if n-len(fibonacci)==1:
            for i in range(iterate-len(fibonacci)):
                fibonacci.append(fibonacci[n-2+i]+fibonacci[n-3+i])
        return fib_eager(n-1,iterate,eager_solution)+fib_eager(n-2,iterate,eager_solution)
    else:
        string=f"fib({n})= "+str(fibonacci[n-1]) + "\n"
        eager_solution.write(string)
        return fibonacci[n-1]
    
#Check the input validity and write correct results in eager solution
def eager(integers,eager_solution):
    dash_character="-"*32
    dash_character_n="-"*32+"\n"
    for number in integers:
        if number<=0:
            eager_solution.write(dash_character_n)
            result="Calculating "+str(number)+". Fibonacci number:"+"\n"
            eager_solution.write(result)
            eager_solution.write("ERROR: Fibonacci cannot be calculated for the non-positive numbers!\n")
            result=f"{number}. Fibonacci number is: nan \n"
            eager_solution.write(result)
        else:
            eager_solution.write(dash_character_n)
            result="Calculating "+str(number)+". Fibonacci number:"+"\n"
            eager_solution.write(result)
            result=fib_eager(number,number,eager_solution)
            result=str(number)+". Fibonacci number is: "+str(result)+"\n"
            eager_solution.write(result)
            if number==integers[-1]:
                eager_solution.write(dash_character_n)
                eager_solution.write("Structure for the eager solution:\n")
                structure=str(fibonacci)+"\n"
                eager_solution.write(structure)
                eager_solution.write(dash_character)
def main():
    input_file=open(sys.argv[1],"r") 
    numbers=input_file.read()
    input_file.close()
    numbers_list=numbers.split("\n")
    integers=[int(number) for number in numbers_list]
    naive_solution=open(sys.argv[2],"a")
    eager_solution=open(sys.argv[3],"a")
    
    naive(integers,naive_solution)
    eager(integers,eager_solution)

    
    naive_solution.close
    eager_solution.close
if __name__=="__main__":
    main()