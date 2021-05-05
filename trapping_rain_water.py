class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            # It takes 3 to hold anything
            return 0
        depths = [self.depth(height, x) for x in range(1, len(height) - 1)]
        return sum(depths)

    # Depth of water in one cell
    def depth(self, height: List[int], x) -> int:
        water_level = min([max(height[:x]),
                           max(height[x:])])
        if water_level > height[x]:
            return water_level - height[x]
        return 0
