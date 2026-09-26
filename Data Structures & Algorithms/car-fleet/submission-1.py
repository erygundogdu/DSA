class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        time = []
        cars = sorted(zip(position, speed), reverse=True)
        for p,s in cars:
            t = (target - p) / s
            if time :
                if time[-1] < t:
                    time.append(t)
            else:
                    time.append(t)
        return len(time)
            
        








        