
def Newton_cotes(f,dx):
    N = len(y)
    integral = 0.0
    for i in range(0,N-1,2):
        integral = integral+f[i-1]+4.0*f[i]+f[i+1]
        integral=integral*dx/3.0

    return integral