import pytz

class DataHandler:


    def __init__(self, file_path):
        
        self.file_path=file_path
        self.data_df=pd.read_csv(self.file_path, index_col="time")
        self.data_df.index=pd.to_datetime(self.data_df.index)

        self.data_df.index=self.data_df.index.tz_convert('US/Eastern')
              
    def resample_to_frequency(self,time_frequency="5min"):
        """

        :param time_frequency:
        :return:
        """
        #Es importante hacer una copia del dataframe
        tmp_data=self.data_df.copy()
        tmp_data["day_of_trade"]=[i.date() for i in tmp_data.index]
        
        re_data=tmp_data.groupby(["day_of_trade"]).resample(time_frequency).last()["close"]
                       
        return re_data
    
    

    def count_nans(self,time_frequency):
        """

        :param time_frequency:
        :return:
        """
     
        return 
    
    def visualize_nans(self,time_frequency):
        """

        :param time_frequency:
        :return:
        """
    @property
    def daily_closes(self):
        temp_df=pd.DataFrame(self.resample_to_frequency(time_frequency="1d")).reset_index()\
                 .set_index("day_of_trade").drop(columns=["time"])
        temp_df.columns=[self.file_path]
        return temp_df