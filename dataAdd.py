import pandas as pd
import datetime as dt
import os

data_path='/home/omkar/Desktop/Accedent_detection_dashboard/dataset/Partition_Dataset'

default_row={
 'ID': 'A-161277',
 'Severity': 4,
 'Start_Time': '2016-01-14 20:18:33',
 'End_Time': '2017-03-29 12:26:40',
 'Start_Lat': 40.630609,
 'Start_Lng': -75.470606,
 'End_Lat': 40.630292,
 'End_Lng': -75.47169699999998,
 'Distance(mi)': 0.061,
 'City': 'Whitehall',
 'County': 'Lehigh',
 'State': 'PA',
 'Zipcode': 18052,
 'Country': 'US',
 'Timezone': 'US/Eastern',
 'Weather_Timestamp': '2016-01-14 19:51:00',
 'Temperature(F)': 31.0,
 'Wind_Chill(F)': 31.0,
 'Humidity(%)': 69.0,
 'Pressure(in)': 29.53,
 'Visibility(mi)': 10.0,
 'Wind_Direction': 'N',
 'Wind_Speed(mph)': 3.0,
 'Weather_Condition': 'Fair',
 'Sunrise_Sunset': 'Day'}


defult_row={}

def get_lat_lon_path(path:str):
    lat=path.split("/")[-1].split(".")[0].split("-")[0]
    lon=path.split("/")[-1].split(".")[0].split("-")[1]
    lat=float(float(lat.split("_")[0])+float(lat.split("_")[1])/(10**len(lat.split("_")[1])))
    lon=float(float(lon.split("_")[0])+float(lon.split("_")[1])/(10**len(lon.split("_")[1])))
    # print(lat,lon)
    return lat,lon

def adddata(Video_path:str):
    lat,lon=get_lat_lon_path(Video_path)
    curr=dt.datetime.today()
    year=int(curr.year)
    month=int(curr.month)
    data_partition_paths=os.listdir(data_path)
    is_csv_exits=False
    data_partition_path=""
    for path in data_partition_paths:
        Y=int(path.split("_")[0].split("-")[0])
        M=int(path.split("_")[0].split("-")[1])
        if Y==year and month==M:
            data_partition_path=path
            is_csv_exits=True
    if is_csv_exits:
        df=pd.read_csv(f"{data_path}/{data_partition_path}")
        row_add={**default_row,'Start_Lat':lat,'Start_Lng':lon,'Start_Time':curr.strftime('%Y-%m-%d %H:%M:%S'),'End_Time':curr.strftime('%Y-%m-%d %H:%M:%S')}
        row_df=pd.DataFrame([row_add])
        updated_df=pd.concat([df,row_df],ignore_index=True)
        updated_df.reset_index()
        updated_df.to_csv(f"{data_path}/{data_partition_path}",index=False)
        print(updated_df)
    else:
        if month<10:
            data_partition_path=f'{year}-0{month}_data.csv'
        else:
            data_partition_path=f'{year}-{month}_data.csv'
        row_add={**default_row,'Start_Lat':lat,'Start_Lng':lon,'Start_Time':curr.strftime('%Y-%m-%d %H:%M:%S'),'End_Time':curr.strftime('%Y-%m-%d %H:%M:%S')}
        row_df=pd.DataFrame([row_add])
        row_df.to_csv(f"{data_path}/{data_partition_path}",index=False)
        print(row_df)



# if __name__=="__main__":
#     adddata("/home/omkar/Desktop/18_6517-73_7000.mp4")

