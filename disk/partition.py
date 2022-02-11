
# Represent a disk partition.

class Partition:
    """
    This class represents a disk partition.
    """

    def __init__(self, major, minor, blocks, name):
        self.major = major
        self.minor = minor
        self.blocks = blocks
        self.name = name
    
    def __str__(self):
        return 'major:{0} minor:{1} blocks:{2} name:{3}'.format(
            self.major,
            self.minor,
            self.blocks,
            self.name,
        )
    
    def __repr__(self):
        return '{0} {1} {2} {3}'.format(
            self.major,
            self.minor,
            self.blocks,
            self.name,
        )
    
    def __lt__(self, other):
        return self.blocks < other.blocks
    
    def __le__(self, other):
        return self.blocks <= other.blocks
    
    def __eq__(self, other):
        return self.blocks == other.blocks and self.major == other.major

    def __ne__(self, other):
        return self.blocks != other.blocks or self.major != other.major
    
    def __gt__(self, other):
        return self.blocks > other.blocks
    
    def __ge__(self, other):
        return self.blocks >= other.blocks
    
    def __hash__(self):
        return hash(self.name)