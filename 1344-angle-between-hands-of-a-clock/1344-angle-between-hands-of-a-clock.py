class Solution(object):
    def angleClock(self, hour, minutes):
        hour = (hour+(minutes/60.0))%(12)
        ha = (hour/12.0)*360
        ma = (minutes/60.0)*360
        ans = abs(ha-ma)
        return min(ans,360-ans)