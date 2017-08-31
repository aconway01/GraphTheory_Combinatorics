from numpy import *
import matplotlib.pyplot as plt

def stirling(n):
    return sqrt(2*pi*n)*((n/e)**n)

def fact(n):
    if n == 0:
        return 1.0
    else:
        return n*fact(n-1)

def main():
    fact_arr = []
    stirling_arr = []
    x_arr = []
    diff_arr = []
    percent_diff_arr = []

    print("n","    ","fact(n)","        ","stirling(n)","    ","fact(n) - stirling(n)","    ","Percent Difference")
    print("------------------------------------------------------------------------------")

    for i in range(1,11): # for 30 values [1,...,10]
        x_arr.append(i)
        fact_arr.append(fact(i))
        stirling_arr.append(stirling(i))
        diff_arr.append(round(fact_arr[i-1] - stirling_arr[i-1],5))
        percent_diff_arr.append(round((fact_arr[i-1]-stirling_arr[i-1])/((fact_arr[i-1]+stirling_arr[i-1])/2),3))
        print(i,"    ",fact_arr[i-1],"            ",stirling_arr[i-1],"        ",diff_arr[i-1],"        ",percent_diff_arr[i-1])


    # compose plot

    '''
    plt.plot(x_arr,fact_arr,'bo',x_arr,stirling_arr,'r^')
    plt.title('Factorial (blue) vs Stirling Formula (red)')
    plt.ylabel('x(n)')
    plt.xlabel('n')

    plt.plot(x_arr,diff_arr,'b--')
    plt.title('fact(n) - stirling(n)')
    plt.ylabel('difference')
    plt.xlabel('n')
    '''

    plt.plot(x_arr,percent_diff_arr,'b--')
    plt.title('Percent Difference')
    plt.ylabel('Percent')
    plt.xlabel('n')

    plt.show() # show the plot


main()
