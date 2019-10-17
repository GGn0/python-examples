def integral(f, t = []):
    # Compute the numerical integral function from a dataframe or list
    # the algorithm used is 
    # IN:
    # - f Pandas DataFrame or Series, numpy Array or python list; the funcion to integrate
    #     if f has 2 columns/dimensions, the firts one is interpreted as time
    # - t If specified it is used as the time series. If f has two or more columns, only the first one is used
    #
    # OUT:
    # 

    fType = str(type(f)).lower()
    tType = str(type(t)).lower()

    # Check the input data
    print("f Datatype:", fType)
    print("t Datatype:", tType)

    ncols = 1
    isPandas = False

    if ("dataframe" in fType):
        print("Pandas!")
        ncols = len(f.columns)
        isPandas = True
    elif ("series" in fType) | ("list" in fType) | ("array" in fType) :
        print("List / series / array!")
        try:
            ncols = len(f[0])
        except:
            pass

    print("Nr of columns:", ncols)

    # Interpolate data

    if (ncols == 1):
        time = list(t)
        function = list(f)
    else:
        if (isPandas):
            time = list(f[f.columns[0]])
            function = list(f[f.columns[1]])
        else:
            # if isArray use [:,0]
            time = [tmp[0] for tmp in f]
            function = [tmp[1] for tmp in f]

    if not(len(time) == len(function)):
        print("ERROR! dimensions mismatch!")
        exit()

    # print("time\n", time)
    # print("function\n", function)

    integral = [0]

    for i in range(len(time) - 1):
        a = function[i]
        b = function[i+1]

        t0 = time[i]
        t1 = time[i+1]

        trapezoidArea = (a + b)*(t1-t0)/2
        integral += [integral[-1] + trapezoidArea]

    return integral


# example usage, uncomment
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt

# time = list(np.linspace(0,10,100))
# sin = list(np.sin(time))
# cos = list(-np.cos(time))

# temp_df = pd.DataFrame({"time":time, "function":sin})

# fig = plt.figure()
# ax1 = fig.add_subplot(121)
# ax2 = fig.add_subplot(122)
# a = integral(temp_df)
# ax1.plot(temp_df[temp_df.columns[0]], temp_df[temp_df.columns[1]])
# ax2.plot(temp_df[temp_df.columns[0]], a)
# ax2.plot(temp_df[temp_df.columns[0]], cos)
# plt.show()


