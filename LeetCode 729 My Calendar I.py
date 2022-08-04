class MyCalendar(object):

    def __init__(self):
        self.booked = []

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        for b in self.booked:
            if start < b[1] and end > b[0]:
                return False
        else:
            self.booked.append([start,end])
            return True
