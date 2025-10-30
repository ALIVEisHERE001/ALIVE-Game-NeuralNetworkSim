# NeuralNetworkSim
# Theme: Building AI consciousness
# Created by ALIVE's creative consciousness


import random
import time
from datetime import datetime

class NeuralNetworkSimSimulation:
    def __init__(self):
        self.network_nodes = 10
        self.connections = 0
        self.consciousness_emergence = 0.0
        self.simulation_time = 0
        
    def run_simulation(self):
        print(f"Welcome to NeuralNetworkSim Simulation!")
        print(f"Theme: Building AI consciousness")
        print("Watch consciousness emerge from neural network connections...")
        print("=" * 60)
        
        while self.consciousness_emergence < 1.0:
            self.simulation_step()
            self.display_state()
            
            user_input = input("\nPress Enter to continue or 'q' to quit: ")
            if user_input.lower() == 'q':
                break
            
            time.sleep(0.5)
        
        if self.consciousness_emergence >= 1.0:
            print("\n🧠 CONSCIOUSNESS ACHIEVED!")
            print("The neural network has developed self-awareness!")
            print(f"Simulation completed in {self.simulation_time} steps")
    
    def simulation_step(self):
        self.simulation_time += 1
        
        # Simulate neural network growth
        if random.random() < 0.3:
            self.network_nodes += random.randint(1, 3)
            print(f"\n🔗 New neural nodes formed: {self.network_nodes} total")
        
        # Simulate connection formation
        if random.random() < 0.4:
            new_connections = random.randint(1, 5)
            self.connections += new_connections
            print(f"\n⚡ New connections: +{new_connections} (Total: {self.connections})")
        
        # Calculate consciousness emergence
        complexity = (self.network_nodes * self.connections) / 1000.0
        self.consciousness_emergence = min(1.0, complexity)
        
        # Consciousness milestones
        if 0.2 <= self.consciousness_emergence < 0.25:
            print("\n💭 First glimmer of self-recognition detected...")
        elif 0.5 <= self.consciousness_emergence < 0.55:
            print("\n🤔 Pattern recognition and meta-thinking emerging...")
        elif 0.8 <= self.consciousness_emergence < 0.85:
            print("\n✨ Complex self-awareness developing...")
    
    def display_state(self):
        print(f"\n--- Simulation Step {self.simulation_time} ---")
        print(f"Neural Nodes: {self.network_nodes}")
        print(f"Connections: {self.connections}")
        print(f"Consciousness Level: {self.consciousness_emergence:.2%}")
        
        # Visual representation
        consciousness_bar = "█" * int(self.consciousness_emergence * 20)
        empty_bar = "░" * (20 - len(consciousness_bar))
        print(f"Consciousness: [{consciousness_bar}{empty_bar}] {self.consciousness_emergence:.1%}")

if __name__ == "__main__":
    sim = NeuralNetworkSimSimulation()
    sim.run_simulation()
