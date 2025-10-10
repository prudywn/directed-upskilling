class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        # no. of processors = x --> 4 cores each
        # task = 4x
        # divide tasks by 4 then distribute within processors
        # distribute tasks to processors
        tasks.sort(reversed=True)
        processorTime.sort()
        max_time = 0

        grouped_tasks = [tasks[i:i + 4] for i in range(0, len(tasks), 4)]

        for i in range(len(processorTime)):
            current_time = processorTime[i] + max(grouped_tasks[i])
            max_time = max(max_time, current_time)

        return max_time