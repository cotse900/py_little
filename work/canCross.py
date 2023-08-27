class Solution:
    def canCross(self, stones: List[int]) -> bool:
        stone_set = set(stones)
        
        jump_sizes = {stone: set() for stone in stones}
        jump_sizes[0].add(0)
        
        for stone in stones:
            for jump in jump_sizes[stone]:
                for next_jump in [jump - 1, jump, jump + 1]:
                    if next_jump > 0 and stone + next_jump in stone_set:
                        jump_sizes[stone + next_jump].add(next_jump)
        
        return bool(jump_sizes[stones[-1]])
