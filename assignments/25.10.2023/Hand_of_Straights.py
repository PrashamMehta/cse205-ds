class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize > 0:
            return False
        total_count = len(hand)//groupSize
        count = 0
        hand.sort()

        while len(hand) > 0:
            h = hand.pop()
            size = groupSize - 1
            popi = len(hand)-1

            while popi > -1 and size > 0:
                if hand[popi] == h:
                    popi -= 1
                elif hand[popi] != h-1:
                    return False
                else:
                    h = hand.pop(popi)
                    popi -= 1
                    size -= 1
            count += 1
        return count == total_count