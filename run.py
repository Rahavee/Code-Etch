from stepperMotor import stepperMotor
import os
import pandas as pd
import pickle


def load_path(file):
    with open(os.path.join('Paths', file + '.p'), 'rb') as myfile:
        data = pickle.load(myfile)
    return data


def draw_from_cache(file):
    path = load_path(file)
    print(len(path))
    draw_path(path)
    return


def check_start(file, n=6):
    path = load_path(file)
    df = pd.DataFrame(path)
    lefts, downs = tuple(df.cumsum().min().values)
    rights, ups = tuple(df.cumsum().max().values)
    scaling = 26. * 6. / n
    print('Room Needed', '\n--------')
    print('left: ', lefts, 'approx. ', round(lefts / scaling, 2), 'cm')
    print('right:', rights, 'approx. ', round(rights / scaling, 2), 'cm')
    print('up:   ', ups, 'approx. ', round(ups / scaling, 2), 'cm')
    print('down: ', downs, 'approx. ', round(downs / scaling, 2), 'cm')
    return


def draw_path(path):
    leftMotor = stepperMotor([7, 11, 13, 15])
    rightMotor = stepperMotor([31, 33, 35, 37])
    step = 2
    reps = 2
    print('# of Steps: ', len(path))
    stepcounter = 0
    for p in path:
        stepcounter += 1
        if stepcounter % 50:
            print(stepcounter, '/', len(path))
        for rep in range(reps):
            # print('x','y',p)
            x = p[0]
            y = p[1]
            rightMotor.rotate(-step * y)
            leftMotor.rotate(step * x)
    leftMotor.close()
    rightMotor.close()


