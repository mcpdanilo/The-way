import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Function to draw an alarm loop with appropriate labeling for each component
def draw_alarm_loop_with_labels(title, config, resistor=None):
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 6)
    ax.axis('off')
    
    # Draw wires and components based on configuration
    if config == '2 NO':
        # Power and ground
        ax.plot([1, 2], [3, 3], color='black', lw=2)
        ax.plot([10, 11], [3, 3], color='black', lw=2)
        # First NO sensor
        ax.plot([2, 3], [3, 3], color='black', lw=2)
        ax.plot([3, 3], [3, 5], color='black', lw=2)
        ax.plot([3, 4], [5, 5], color='black', lw=2)
        ax.plot([4, 4], [5, 3], color='black', lw=2)
        ax.plot([4, 5], [3, 3], color='black', lw=2)
        # Second NO sensor
        ax.plot([5, 6], [3, 3], color='black', lw=2)
        ax.plot([6, 6], [3, 5], color='black', lw=2)
        ax.plot([6, 7], [5, 5], color='black', lw=2)
        ax.plot([7, 7], [5, 3], color='black', lw=2)
        ax.plot([7, 8], [3, 3], color='black', lw=2)
        # Connect to ground
        ax.plot([8, 10], [3, 3], color='black', lw=2)
        # Labels
        ax.text(2, 2.5, 'PWR', fontsize=12, ha='center')
        ax.text(10, 2.5, 'GND', fontsize=12, ha='center')
        ax.text(3.5, 5.2, 'NO', fontsize=12, ha='center')
        ax.text(6.5, 5.2, 'NO', fontsize=12, ha='center')

    elif config == '2 NC':
        # Power and ground
        ax.plot([1, 2], [3, 3], color='black', lw=2)
        ax.plot([10, 11], [3, 3], color='black', lw=2)
        # First NC sensor
        ax.plot([2, 3], [3, 3], color='black', lw=2)
        ax.plot([3, 3], [3, 5], color='black', lw=2)
        ax.plot([3, 4], [5, 5], color='black', lw=2)
        ax.plot([4, 4], [5, 3], color='black', lw=2)
        ax.plot([4, 5], [3, 3], color='black', lw=2, linestyle='dashed')
        # Second NC sensor
        ax.plot([5, 6], [3, 3], color='black', lw=2)
        ax.plot([6, 6], [3, 5], color='black', lw=2)
        ax.plot([6, 7], [5, 5], color='black', lw=2)
        ax.plot([7, 7], [5, 3], color='black', lw=2)
        ax.plot([7, 8], [3, 3], color='black', lw=2, linestyle='dashed')
        # Connect to ground
        ax.plot([8, 10], [3, 3], color='black', lw=2)
        # Labels
        ax.text(2, 2.5, 'PWR', fontsize=12, ha='center')
        ax.text(10, 2.5, 'GND', fontsize=12, ha='center')
        ax.text(3.5, 5.2, 'NC', fontsize=12, ha='center')
        ax.text(6.5, 5.2, 'NC', fontsize=12, ha='center')

    elif config == 'Mixed':
        # Power and ground
        ax.plot([1, 2], [3, 3], color='black', lw=2)
        ax.plot([10, 11], [3, 3], color='black', lw=2)
        # First NO sensor
        ax.plot([2, 3], [3, 3], color='black', lw=2)
        ax.plot([3, 3], [3, 5], color='black', lw=2)
        ax.plot([3, 4], [5, 5], color='black', lw=2)
        ax.plot([4, 4], [5, 3], color='black', lw=2)
        ax.plot([4, 5], [3, 3], color='black', lw=2)
        # Second NC sensor
        ax.plot([5, 6], [3, 3], color='black', lw=2)
        ax.plot([6, 6], [3, 5], color='black', lw=2)
        ax.plot([6, 7], [5, 5], color='black', lw=2)
        ax.plot([7, 7], [5, 3], color='black', lw=2, linestyle='dashed')
        ax.plot([7, 8], [3, 3], color='black', lw=2)
        # Connect to ground
        ax.plot([8, 10], [3, 3], color='black', lw=2)
        # Labels
        ax.text(2, 2.5, 'PWR', fontsize=12, ha='center')
        ax.text(10, 2.5, 'GND', fontsize=12, ha='center')
        ax.text(3.5, 5.2, 'NO', fontsize=12, ha='center')
        ax.text(6.5, 5.2, 'NC', fontsize=12, ha='center')

    elif config == '2 NC with Resistor':
        # Power and ground
        ax.plot([1, 2], [3, 3], color='black', lw=2)
        ax.plot([10, 11], [3, 3], color='black', lw=2)
        # First NC sensor
        ax.plot([2, 3], [3, 3], color='black', lw=2)
        ax.plot([3, 3], [3, 5], color='black', lw=2)
        ax.plot([3, 4], [5, 5], color='black', lw=2)
        ax.plot([4, 4], [5, 3], color='black', lw=2)
        ax.plot([4, 5], [3, 3], color='black', lw=2)
        # Resistor 5kΩ
        ax.plot([5, 6], [3, 3], color='blue', lw=2)
        ax.text(5.5, 2.5, '5kΩ', color='blue', fontsize=12, ha='center')
        # Second NC sensor
        ax.plot([6, 7], [3, 3], color='black', lw=2, linestyle='dashed')
        ax.plot([7, 8], [3, 3], color='black', lw=2)
        # Connect to ground
        ax.plot([8, 10], [3, 3], color='black', lw=2)
        # Labels
        ax.text(2, 2.5, 'PWR', fontsize=12, ha='center')
        ax.text(10, 2.5, 'GND', fontsize=12, ha='center')
        ax.text(3.5, 5.2, 'NC', fontsize=12, ha='center')

    elif config == '2 NO with Resistor':
        # Power and ground
        ax.plot([1, 2], [3, 3], color='black', lw=2)
        ax.plot([10, 11], [3, 3], color='black', lw=2)
        # First NO sensor
        ax.plot([2, 3], [3, 3], color='black', lw=2)
        ax.plot([3, 3], [3, 5], color='black', lw=2)
        ax.plot([3, 4], [5, 5], color='black', lw=2)
        ax.plot([4, 4], [5, 3], color='black', lw=2)
        ax.plot([4, 5], [3, 3], color='black', lw=2)
        # Resistor 5kΩ
        ax.plot([5, 6], [3, 3], color='blue', lw=2)
        ax.text(5.5, 2.5, '5kΩ', color='blue', fontsize=12, ha='center', lw=2)