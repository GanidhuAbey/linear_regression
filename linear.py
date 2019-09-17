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


def error_cost(m, b, x, y):
    #x and y aren't multiple values so the function has to take the sum of all the y and x inputs and divide by the average
    prediction = np.sum(m*x + b) / x.size;
    target = np.sum(y) / y.size;


def predict():
    pass

def main():
    pass


main()
