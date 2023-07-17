def get_distance(p, q):
    """
    Return euclidean distance between points p and q
    assuming both to have the same number of dimensions
    """
    # sum of squared difference between coordinates
    s_sq_difference = 0
    for p_i, q_i in zip(p, q):
        s_sq_difference += (p_i - q_i) ** 2

    # take sq root of sum of squared difference
    distance = s_sq_difference ** 0.5
    return distance


# # check the function
# a = (2, 3, 6)
# b = (5, 7, 1)
# # distance b/w a and b
# d = get_distance(a, b)
# # display the result
# print(d)

def distance_in_metr(dist):

    distance = dist * 1000

    return distance

def distance_in_mile(dist):

    distance = dist / 1855

    return distance

#Успеет ли человек преодолеть дистанцию за 8 часов
def calc_for_men(dist, speed):
    norm_time = 8
    time=dist/speed
    return norm_time>time


