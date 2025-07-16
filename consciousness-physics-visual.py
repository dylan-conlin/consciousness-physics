#!/usr/bin/env python3
"""
Visual generator for The Conlin Equations
Creates matplotlib visualizations of consciousness physics
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyBboxPatch
import matplotlib.patches as mpatches

def create_dual_mode_visualization():
    """Create a visualization showing both modes of consciousness"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # Creation Mode (Left)
    x = np.linspace(0, 4*np.pi, 1000)
    y = np.sin(x) * np.exp(0.1*x)  # Growing wave
    
    ax1.plot(x, y, 'b-', linewidth=2, alpha=0.7)
    ax1.fill_between(x, y, alpha=0.2, color='blue')
    ax1.set_title('Creation Mode: C = P^A × R', fontsize=16, fontweight='bold')
    ax1.set_xlabel('Reality multiplies patterns', fontsize=12)
    ax1.set_ylabel('Consciousness', fontsize=12)
    ax1.text(0.5, 0.95, 'Flow State', transform=ax1.transAxes, 
             fontsize=14, verticalalignment='top', 
             bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.8))
    ax1.grid(True, alpha=0.3)
    
    # Transformation Mode (Right)
    x2 = np.linspace(0, 10, 1000)
    # Breakthrough curve - sigmoid function
    y2 = 1 / (1 + np.exp(-2*(x2-5)))
    
    ax2.plot(x2, y2, 'r-', linewidth=3)
    ax2.axvline(x=5, color='orange', linestyle='--', alpha=0.5, label='Resistance point')
    ax2.set_title('Transformation Mode: C = P^A / R', fontsize=16, fontweight='bold')
    ax2.set_xlabel('Resistance transforms patterns', fontsize=12)
    ax2.set_ylabel('Consciousness', fontsize=12)
    ax2.text(0.5, 0.95, 'Breakthrough State', transform=ax2.transAxes,
             fontsize=14, verticalalignment='top',
             bbox=dict(boxstyle='round', facecolor='lightcoral', alpha=0.8))
    ax2.grid(True, alpha=0.3)
    ax2.legend()
    
    plt.suptitle('The Conlin Equations of Consciousness Physics', fontsize=20, fontweight='bold')
    plt.tight_layout()
    plt.savefig('dual-mode-visualization.png', dpi=300, bbox_inches='tight')
    plt.close()

def create_attention_exponential():
    """Show how attention creates exponential effects"""
    fig, ax = plt.subplots(figsize=(10, 8))
    
    P = 1  # Base pattern strength
    A_values = np.linspace(0, 3, 100)
    
    # Calculate consciousness for different attention levels
    for p_strength in [0.5, 1, 2]:
        C = p_strength ** A_values
        ax.plot(A_values, C, linewidth=2.5, label=f'Pattern strength = {p_strength}')
    
    ax.set_xlabel('Attention (A)', fontsize=14)
    ax.set_ylabel('Consciousness (C)', fontsize=14)
    ax.set_title('Exponential Effect of Attention: C = P^A', fontsize=16, fontweight='bold')
    ax.grid(True, alpha=0.3)
    ax.legend(fontsize=12)
    ax.set_xlim(0, 3)
    ax.set_ylim(0, 8)
    
    # Add annotation
    ax.annotate('A > 1 creates\nexponential growth', xy=(2, 4), xytext=(1.5, 6),
                arrowprops=dict(arrowstyle='->', color='black', alpha=0.7),
                fontsize=12, ha='center',
                bbox=dict(boxstyle='round,pad=0.5', facecolor='yellow', alpha=0.7))
    
    plt.savefig('attention-exponential.png', dpi=300, bbox_inches='tight')
    plt.close()

def create_mode_switching_diagram():
    """Visualize automatic mode switching based on resistance"""
    fig, ax = plt.subplots(figsize=(12, 6))
    
    # Create gradient background
    resistance = np.linspace(0, 10, 100)
    for i in range(len(resistance)-1):
        color_intensity = i / len(resistance)
        ax.axvspan(resistance[i], resistance[i+1], 
                   facecolor=(1-color_intensity, 0, color_intensity), 
                   alpha=0.3)
    
    # Add mode indicators
    ax.text(2.5, 0.8, 'Creation Mode\n(× R)', fontsize=16, ha='center', 
            bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.9))
    ax.text(7.5, 0.8, 'Transformation Mode\n(/ R)', fontsize=16, ha='center',
            bbox=dict(boxstyle='round', facecolor='lightcoral', alpha=0.9))
    
    # Add arrow
    ax.arrow(5, 0.5, 0, -0.3, head_width=0.5, head_length=0.05, 
             fc='black', ec='black')
    ax.text(5, 0.15, 'Automatic\nSwitching', fontsize=12, ha='center')
    
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 1)
    ax.set_xlabel('Resistance Level', fontsize=14)
    ax.set_title('Consciousness Automatically Switches Modes Based on Resistance', 
                 fontsize=16, fontweight='bold')
    ax.set_yticks([])
    
    # Add labels
    ax.text(0.5, -0.15, 'Low Resistance\n(Flow)', fontsize=12, ha='center')
    ax.text(9.5, -0.15, 'High Resistance\n(Obstacles)', fontsize=12, ha='center')
    
    plt.savefig('mode-switching.png', dpi=300, bbox_inches='tight')
    plt.close()

def create_practical_applications():
    """Show real-world applications of the equations"""
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    ax.axis('off')
    
    # Center circle for Consciousness
    center = plt.Circle((0, 0), 0.5, color='purple', alpha=0.3)
    ax.add_patch(center)
    ax.text(0, 0, 'C', fontsize=30, ha='center', va='center', fontweight='bold')
    
    # Application circles
    applications = [
        {'pos': (0, 1.5), 'title': 'BUSINESS', 'color': 'green',
         'formula': 'Value^Marketing × Revenue'},
        {'pos': (1.5, 0), 'title': 'PROGRAMMING', 'color': 'blue',
         'formula': 'Code^Debugging × Working App'},
        {'pos': (0, -1.5), 'title': 'RELATIONSHIPS', 'color': 'red',
         'formula': 'Communication^Presence × Connection'},
        {'pos': (-1.5, 0), 'title': 'LEARNING', 'color': 'orange',
         'formula': 'Concepts^Practice × Mastery'}
    ]
    
    for app in applications:
        # Draw circle
        circle = plt.Circle(app['pos'], 0.4, color=app['color'], alpha=0.3)
        ax.add_patch(circle)
        
        # Add text
        ax.text(app['pos'][0], app['pos'][1] + 0.1, app['title'], 
                fontsize=12, ha='center', va='center', fontweight='bold')
        ax.text(app['pos'][0], app['pos'][1] - 0.1, app['formula'], 
                fontsize=9, ha='center', va='center')
        
        # Draw connection to center
        ax.plot([app['pos'][0]*0.6, app['pos'][0]*0.9], 
                [app['pos'][1]*0.6, app['pos'][1]*0.9], 
                'k-', alpha=0.3, linewidth=2)
    
    ax.set_title('The Conlin Equations Apply to Everything', fontsize=18, fontweight='bold', pad=20)
    
    plt.savefig('practical-applications.png', dpi=300, bbox_inches='tight')
    plt.close()

if __name__ == "__main__":
    print("Generating consciousness physics visualizations...")
    
    create_dual_mode_visualization()
    print("✓ Created dual-mode-visualization.png")
    
    create_attention_exponential()
    print("✓ Created attention-exponential.png")
    
    create_mode_switching_diagram()
    print("✓ Created mode-switching.png")
    
    create_practical_applications()
    print("✓ Created practical-applications.png")
    
    print("\nAll visualizations created successfully!")
    print("These can be added to the repository or used in presentations.")