
class Audience:

    segment = "test segment 1"
    campaign = "test campaign 1"

    def __init__(self, segment):
        self.segment = segment

    def export_audience (self):
        print ("Audience:export_audience " + self.segment + "   " + self.campaign )





aud = Audience ("inital segment")
print ("main function " + aud.segment + "   " + aud.campaign)
aud.export_audience()