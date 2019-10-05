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

    # data values used to predict line
    x = np.array([8.8, 47.6, 26.8, 25.8, 27.8, 28.3, 16.7, 28.2, 107.4, 27.1, 13.0])
    y = np.array([4.0, 14.1, 11.6, 21.6, 9.0, 13.5, 6.6, 12.7, 29.4, 9.1, 4.5])

    (m, b) = error_cost(m, b, x, y, 0.0001);

    max_value = np.amax(x)
    x_inputs = np.arange(max_value)

    print(x_inputs)
    plt.scatter(x, y);
    plt.plot(m*x_inputs + b);
    plt.show();


main()














