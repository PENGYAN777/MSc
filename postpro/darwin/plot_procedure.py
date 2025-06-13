import matplotlib.pyplot as plt
import numpy as np

# Define box properties
box_props = dict(boxstyle="round,pad=0.3", facecolor="#e0f7fa", edgecolor="black")

# Define all labels
labels = [
    "Mesh Level m",
    "Computed Solution Field (m)",
    "Error Estimation",
    "Multi Passages",
    "Grid Modification",
    "Mesh Level m+1",
]

# Number of points
n = len(labels)

# Circle center and radius
center = (0.5, 0.5)
radius = 0.40

# Calculate positions evenly spaced on a circle
angles = np.linspace(0, 2 * np.pi, n, endpoint=False)
positions = [(center[0] + radius * np.cos(angle), center[1] + radius * np.sin(angle)) for angle in angles]

# Create the plot
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

# Manual arrow start/end points for problematic arrows
manual_arrows = {
    "Computed Solution Field (m)": ((0.50, 0.85), (0.42, 0.85)),
    "Grid Modification": ((0.43, 0.15), (0.57, 0.15)),
}

# Draw boxes and arrows in a circle
for i, (label, (x, y)) in enumerate(zip(labels, positions)):
    ax.text(x, y, label, ha='center', va='center', bbox=box_props, fontsize=14)
    
    # Next box position (wrap around)
    x_next, y_next = positions[(i + 1) % n]
    
    if label in manual_arrows:
        start, end = manual_arrows[label]
        ax.annotate(
            "",
            xy=end,
            xytext=start,
            arrowprops=dict(arrowstyle="->", color='black', linewidth=2)
        )
    else:
        # Calculate direction vector
        dx = x_next - x
        dy = y_next - y
        shrink_ratio = 0.1
        
        # Adjust start and end points to avoid overlap
        start_x = x + dx * shrink_ratio
        start_y = y + dy * shrink_ratio
        end_x = x_next - dx * shrink_ratio
        end_y = y_next - dy * shrink_ratio
        
        ax.annotate(
            "",
            xy=(end_x, end_y),
            xytext=(start_x, start_y),
            arrowprops=dict(arrowstyle="->", color='black', linewidth=2)
        )

plt.title("Circular Adaptive Mesh Workflow", fontsize=20)
plt.tight_layout()
fig.savefig("procedure.pdf", bbox_inches='tight')
plt.show()
