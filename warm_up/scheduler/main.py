"""
- Read from input -> data structure [idx:int, start-time:?, duration:int]
    3
    0000 30
    0015 16
    0020 11
    [[0, '0000', '30'], [1, '0015', '16'], [2, '0020', '11'],
        [3, '0030', '10'], [4, '0031', '12']]

- Find the algorithm to assign minimum workers
    - sort by start time

    - [0, '0000', '30'] -> [w0:30]  -> [j0:w0]
    - [1, '0015', '16'] -> [w0:15, w1:16]  -> [j0:w0, j1:w1]
    - [2, '0020', '11'] -> [w0:10, w1:11, w2:11]  -> [j0:w0, j1:w1, j2:w2]
    - [3, '0030', '10'] -> [w0:0, w1:1, w2:1, w3:10]  -> [j0:w0, j1:w1, j2:w2, j3:w3]
    - [4, '0031', '12'] -> [w0:12, w1:0, w2:0, w3:9]  -> [j0:w0, j1:w1, j2:w2, j3:w3, j4:w0]
"""
from dataclasses import dataclass


@dataclass
class Job:
    id: int
    start_time: int
    duration: int


@dataclass
class Worker:
    id: int
    rem_work_time: int


@dataclass
class Allocation:
    job_id: int
    worker_id: int


def allocate_workers(jobs: list[Job]) -> tuple[int, list[Allocation]]:

    sorted_jobs = sorted(jobs, key=lambda job: job.start_time)

    workers: list[Worker] = []
    allocations: list[Allocation] = list()
    prev_start_time = 0

    for job in sorted_jobs:

        next_worker: Worker | None = None

        for worker in workers:
            elapsed_time = job.start_time - prev_start_time
            if worker.rem_work_time - elapsed_time < 0 and next_worker is None:
                worker.rem_work_time = job.duration
                next_worker = worker
            else:
                worker.rem_work_time = max(
                    worker.rem_work_time - elapsed_time, 0)

        prev_start_time = job.start_time

        if next_worker is None:
            next_worker = Worker(len(workers), job.duration)
            workers.append(next_worker)

        allocations.append(Allocation(job.id, next_worker.id))
    return len(workers), allocations


def read_input() -> list[Job]:
    N = int(input())

    jobs = []

    for idx in range(N):
        start_time, duration = input().split()
        jobs.append(
            Job(idx, int(start_time), int(duration))
        )
    return jobs


def main():

    jobs = read_input()

    num_of_workers, allocations = allocate_workers(jobs)
    print(num_of_workers)
    for allocation in sorted(allocations, key=lambda allocation: allocation.job_id):
        print(f"J{allocation.job_id} W{allocation.worker_id}")


main()
