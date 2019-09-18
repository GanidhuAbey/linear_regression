import numpy as np;
import matplotlib.pyplot as plt;
#error cost square function
    # equation of the line we create : y = mx + b
    # re-write the equation to create the error cost function: y = mx + b
    #                                                          0 = mx + b - y
    
    # square the function to create the error cost:            (mx + b - y)^2

    # we need to create a squared function so that we can find the minimum of the function.
    # the general form of the error cost squared function is (prediction - target)^2
    
    # obviously the goal in a linear regression algorithm is to get the prediction as close to the target as possible,
    # doing this results in the error function also becoming equal to 0 or the minimum of the function

    # in the equation we created "mx + b" uses our predicted values (m, b) tp calculate a _prediction_ of y.
    # and then substracts it by the real y or the _target_.

    # hence our function also boils down to (prediction - target)^2


def error_cost(m, b, x, y, learning_rate):
    #x and y aren't multiple values so the function has to take the sum of all the y and x inputs and divide by the average
    
    # we need to calculate the derivative because it not only tells us when to stop calculating 'm' and 'b' but also tells us off we are and guides our calculations

    # calculate the partial derivative of m and the partial derivative of b and use it re-calculate m and b
    # derivative with respect to x = 2(mx + b - y)x
    while True:
        m_derivative = 2 * (np.sum(x*(m*x + b - y)) / y.size)
        b_derivative = 2 * (np.sum(m*x + b - y) / y.size)

        prev_m = m
        prev_b = b

        print(m, b)

        m = m - (m_derivative * learning_rate)
        b = b - (b_derivative * learning_rate)

        print(m, b)

        #the if statement should be based on how different it was from last time
        if prev_m > (m - 1e-6) and prev_m < (m + 1e-6) and prev_b > (b - 1e-6) and prev_b < (b + 1e-6):
            return m, b 
        

def main():
    m = np.random.randint(1, 100)
    b = np.random.randint(1, 100)

    x = np.array([1, 2, 3, 4])
    y = np.array([2, 4, 6, 8])

    (m, b) = error_cost(m, b, x, y, 0.0001);

    plt.set_cmap("jet")
    plt.scatter(x, y);
    plt.plot(2*x);
    plt.show();


main()
