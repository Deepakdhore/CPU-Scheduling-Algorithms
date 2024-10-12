import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# Read the output file
with open('output.txt', 'r') as f:
    lines = f.readlines()

# Process the output to extract data for each algorithm
algorithms = []
current_algorithm = {}
for line in lines:
    if line.strip() == '------------------------------------------------':
        if current_algorithm:
            algorithms.append(current_algorithm)
            current_algorithm = {}
        continue
    
    if any(alg in line for alg in ['RR', 'FCFS', 'SPN']):
        if current_algorithm:
            algorithms.append(current_algorithm)
        alg_name = line.split()[0]
        current_algorithm = {'name': alg_name, 'processes': {}}
        continue
    
    if current_algorithm:
        parts = line.split('|')
        if len(parts) > 1:
            process_name = parts[0].strip()
            timeline = parts[1].strip().replace(' ', '')
            current_algorithm['processes'][process_name] = timeline

# Function to create Gantt chart for each algorithm
def create_gantt_chart(algorithm):
    fig, ax = plt.subplots(figsize=(10, 5))
    colors = {'P1': 'blue', 'P2': 'green', 'P3': 'red', 'P4': 'purple', 'P5': 'orange'}
    
    for i, (process, timeline) in enumerate(algorithm['processes'].items()):
        start = 0
        for t in timeline:
            if t == '*':
                ax.broken_barh([(start, 1)], (i*10, 9), facecolors=colors[process])
            start += 1
    
    ax.set_yticks([i*10+5 for i in range(len(algorithm['processes']))])
    ax.set_yticklabels(algorithm['processes'].keys())
    ax.set_xlabel('Time')
    ax.set_title(algorithm['name'])
    
    plt.show()

# Generate Gantt charts for each algorithm
for algorithm in algorithms:
    create_gantt_chart(algorithm)
