
class DiskUsage:
    def __init__(self, major_number, minor_number, device_name, reads_completed, reads_merged, sectors_read, time_spent_reading, writes_completed, writes_merged, sectors_written, time_spent_writing, io_in_progress, io_time, weighted_io_time):
        self.major_number = major_number
        self.minor_number = minor_number
        self.device_name = device_name
        self.reads_completed = reads_completed
        self.reads_merged = reads_merged
        self.sectors_read = sectors_read
        self.time_spent_reading = time_spent_reading
        self.writes_completed = writes_completed
        self.writes_merged = writes_merged
        self.sectors_written = sectors_written
        self.time_spent_writing = time_spent_writing
        self.io_in_progress = io_in_progress
        self.io_time = io_time
        self.weighted_io_time = weighted_io_time

    def __str__(self):
        return 'major_number:{0} minor_number:{1} device_name:{2} reads_completed:{3} reads_merged:{4} sectors_read:{5} time_spent_reading:{6} writes_completed:{7} writes_merged:{8} sectors_written:{9} time_spent_writing:{10} io_in_progress:{11} io_time:{12} weighted_io_time:{13}'.format(
            self.major_number,
            self.minor_number,
            self.device_name,
            self.reads_completed,
            self.reads_merged,
            self.sectors_read,
            self.time_spent_reading,
            self.writes_completed,
            self.writes_merged,
            self.sectors_written,
            self.time_spent_writing,
            self.io_in_progress,
            self.io_time,
            self.weighted_io_time,
        )

    def __lt__(self, other):
        return self.weighted_io_time < other.weighted_io_time
    
    def __le__(self, other):
        return self.weighted_io_time <= other.weighted_io_time
    
    def __eq__(self, other):
        return self.device_name == other.device_name
    
    def __ne__(self, other):
        return self.device_name != other.device_name
    
    def __gt__(self, other):
        return self.weighted_io_time > other.weighted_io_time
    
    def __ge__(self, other):
        return self.weighted_io_time >= other.weighted_io_time