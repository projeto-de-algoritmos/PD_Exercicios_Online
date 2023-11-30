def jobScheduling(startTime, endTime, profit):
    
    def achar_ultimo_compativel(arr, index_atual):
        for i in range(index_atual - 1, -1, -1):
            if arr[i].end_time <= arr[index_atual].start_time:
                return i + 1
        
        return 0
    
    class Job:
        def __init__(self, start_time, end_time, profit):
            self.start_time = start_time
            self.end_time = end_time
            self.profit = profit
    
    jobs = []
    p = []
    M = []

    for i in range(len(startTime)):
        job = Job(startTime[i], endTime[i], profit[i])
        jobs.append(job)
    
    sorted_jobs = sorted(jobs, key=lambda x: x.end_time)

    for i in range(len(sorted_jobs)):
        p.append(achar_ultimo_compativel(sorted_jobs, i))


    M.append(0)
    for i in range(1, len(startTime) + 1):
        M.append(-1)
    
    def Compute_Opt(j):
        if (M[j] == -1):
            M[j] = max(sorted_jobs[j - 1].profit + Compute_Opt(p[j - 1]), Compute_Opt(j - 1))
        return M[j]
    
    return Compute_Opt(len(startTime))

    """
        # Iteração do Compute Opt
        M.append(0)

        for i in range(1, len(startTime) + 1):
            M.append(max(sorted_jobs[i - 1].profit + M[p[i - 1]], M[i -1]))
        
        return M.pop()
    """

print(jobScheduling([1,2,3,3], [3,4,5,6], [50,10,40,70]))

print(jobScheduling([1,2,3,4,6], [3,5,10,6,9], [20,20,100,70,60]))

print(jobScheduling([1,1,1], [2,3,4], [5,6,4]))