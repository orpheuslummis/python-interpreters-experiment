import interpreters
import tracemalloc
import statistics

def create_interpreters(n):
    interpreters_list = []
    for _ in range(n):
        interp = interpreters.create()
        interp.exec("pass")  # Minimal execution to initialize the interpreter
        interpreters_list.append(interp)
    return interpreters_list

# Measure memory usage with tracemalloc
def measure_memory(n_interpreters, module_name=None):
    tracemalloc.start()
    snapshot1 = tracemalloc.take_snapshot()

    # Create multiple interpreters and optionally load a module
    interpreters_list = create_interpreters(n_interpreters)
    if module_name:
        for interp in interpreters_list:
            interp.exec(f"import {module_name}")

    snapshot2 = tracemalloc.take_snapshot()
    tracemalloc.stop()

    top_stats = snapshot2.compare_to(snapshot1, 'lineno')
    total_memory = sum(stat.size_diff for stat in top_stats)
    return total_memory / (1024 * 1024)  # Return memory in MB

def run_experiment(n_interpreters, n_runs, module_name=None):
    memory_usages = []

    # Measure baseline memory usage
    baseline_memory = measure_memory(0)
    print(f'Baseline memory usage: {baseline_memory:.2f} MB')

    for _ in range(n_runs):
        memory_usage = measure_memory(n_interpreters, module_name)
        memory_usages.append(memory_usage)
        print(f'Memory usage with {n_interpreters} interpreters: {memory_usage:.2f} MB')

    avg_memory = statistics.mean(memory_usages)
    std_dev_memory = statistics.stdev(memory_usages)

    print(f'Average memory usage with {n_interpreters} interpreters: {avg_memory:.2f} MB')
    print(f'Standard deviation: {std_dev_memory:.2f} MB')

    total_overhead = avg_memory - baseline_memory
    print(f'Total memory overhead: {total_overhead:.2f} MB')

    return memory_usages, avg_memory, std_dev_memory, baseline_memory

# Parameters
n_interpreters = 10
n_runs = 5
module_name = "json"

# Run the experiment
memory_usages, avg_memory, std_dev_memory, baseline_memory = run_experiment(n_interpreters, n_runs, module_name)

# Detailed results
print("\nDetailed memory usage per run:")
for i, usage in enumerate(memory_usages, 1):
    print(f'Run {i}: {usage:.2f} MB')

# Final summary
print("\nFinal Summary:")
print(f'Baseline Memory Usage: {baseline_memory:.2f} MB')
print(f'Average Memory Usage with {n_interpreters} Interpreters: {avg_memory:.2f} MB')
print(f'Standard Deviation: {std_dev_memory:.2f} MB')
print(f'Total Memory Overhead: {total_overhead:.2f} MB')