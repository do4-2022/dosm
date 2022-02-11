from disk import Partition
from disk import DiskUsage

def get_partitions():
    """
    This function returns a list of partition in the disk.
    """
    partitions = []
    for line in open('/proc/partitions'):
        if line.startswith('major') or line.startswith('\n'):
            continue
        fields = line.split()
        partitions.append(Partition(
            int(fields[0]),
            int(fields[1]),
            int(fields[2]),
            fields[3]
        ))
    return partitions

def get_disk_usage():
    """
    This function returns a list of disk usage.
    """
    disk_usages = []
    for line in open('/proc/diskstats'):
        fields = line.split()
        disk_usages.append(DiskUsage(
            int(fields[0]),
            int(fields[1]),
            fields[2],
            int(fields[3]),
            int(fields[4]),
            int(fields[5]),
            int(fields[6]),
            int(fields[7]),
            int(fields[8]),
            int(fields[9]),
            int(fields[10]),
            int(fields[11]),
            int(fields[12]),
            int(fields[13])))
    return disk_usages