import serial
import string
import time
import numpy as np

from file_handling import format_filename, export_recorded
from plot import plot_data


windows = 'COM5'
linux = '/dev/ttyACM0'
ser = serial.Serial(windows, 230400, timeout=1)


def read() -> list:

    line = str(ser.readline()).replace(' ', '').replace('\\r\\n', '').replace('b\'', '').replace('\'', '')
    #print('__b__readline: ', line, '\n')
    return line.split(';')


def write(command) -> None:
    ser.write(command.encode())


def read_bytes(amount) -> bytes:
    return ser.read(amount)
    
#def save_datas(dumping)


def main():
    #channel_names = ['A0', 'A1', 'A2', 'A3', 'A4', 'A5']
    channel_names = ['A0', 'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10', 'A11', 'A12', 'A13', 'A14', 'A15', 'A16', 'A17']
    #print('channel_names: ', channel_names , '\n')
    
    data_channels = list()
    #print('data_channels: ', data_channels, '\n')

    input('Presiona "Enter" para iniciar grabacion, deten la grabacion presionando crtl+c: ')
    #input('start recording by pressing any button, stop recording by using keyboard interrupt crtl+c: ')
    try:
        while True:
            data_channels.append(read())
            #print('data_channels: ', data_channels)
            #print('data_channels.append: ', data_channels.append, '\n')
    except KeyboardInterrupt:
        #s = np.transpose(np.array(data_channels))
        #plot_data(channel_names, s)
        plot_data([channel_names, np.transpose(np.array(data_channels))])
        print('Export buffer in a file...')
        r=open("datas.txt",'w')
        #r.write(str(data_channels).replace('], ', '\n'))
        r.write(str(data_channels).replace('], ', '\n').replace('\'', '').replace('[', '').replace(', ', ''))
        r.close()
        print('listo!!')



if __name__ == '__main__':
    main()
