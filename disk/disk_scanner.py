from disk import partition

def get_partitions():
    """
    This function returns a list of partition objects.
    """
    partitions = []
    for line in open('/proc/partitions'):
        if line.startswith('major'):
            continue
        fields = line.split()
        if len(fields) < 3:
            continue
        partitions.append(partition(
            int(fields[0]),
            int(fields[1]),
            int(fields[2]),
            fields[3]
        ))
    return partitions