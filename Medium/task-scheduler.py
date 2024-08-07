class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)
        ctr = Counter(tasks)
        hp = []
        for c, count in ctr.items():
            heappush(hp, (-count, c))
        time = 0
        cooldown = {}
        while hp or cooldown:
            time += 1
            if hp:
                freq, ltr = heappop(hp)
                freq = -freq
                if freq > 1:
                    cooldown[ltr] = (time + n, freq - 1)
            ready_tasks = [task for task, (cool_time, freq) in cooldown.items() if cool_time == time]
            for task in ready_tasks:
                heappush(hp, (-cooldown[task][1], task))
                del cooldown[task]
        return time
