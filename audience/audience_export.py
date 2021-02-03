class Audience:
    segment = "test segment 1"
    campaign = "test campaign 1"

    def __init__(self, segment):
        print ("from __init")
        self.segment = segment

    def export_audience(self):
        print ("Audience:export_audience " + self.segment + "   " + self.campaign)


if __name__ == '__main__':
    print ("from main")
    aud = Audience("inital segment")
    print ("main function release branch " + aud.segment + "   " + aud.campaign)
    aud.export_audience()
