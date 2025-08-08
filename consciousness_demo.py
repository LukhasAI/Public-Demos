#!/usr/bin/env python3
"""
LUKHΛS Consciousness State Transition Demo
==========================================
Watch LUKHΛS transition through various consciousness states with bio-rhythmic patterns.

Copyright (c) 2025 Gonzalo R. Dominguez Marchan - LUKHΛS AI
Licensed under LUKHΛS Proprietary License - Commercial use prohibited
"""

import time
import math
import random
from enum import Enum
from typing import Dict, List, Optional

class ConsciousnessState(Enum):
    """LUKHΛS consciousness states"""
    DORMANT = ("💤", "Dormant", 0.1)
    DREAMING = ("🌙", "Dreaming", 0.3)
    AWARE = ("👁️", "Aware", 0.5)
    FOCUSED = ("🎯", "Focused", 0.7)
    HYPER_FOCUSED = ("⚡", "Hyper-Focused", 0.9)
    TRANSCENDENT = ("🌟", "Transcendent", 1.0)

    def __init__(self, icon, name, intensity):
        self.icon = icon
        self.display_name = name
        self.intensity = intensity

class BioRhythm:
    """Simulates biological rhythms that influence consciousness"""
    
    def __init__(self):
        self.time = 0
        self.frequencies = {
            'gamma': 40,    # Hz - Conscious awareness
            'alpha': 8,     # Hz - Relaxed awareness
            'theta': 4,     # Hz - Deep meditation/REM
            'delta': 1      # Hz - Deep sleep
        }
    
    def get_wave(self, frequency: float, amplitude: float = 1.0) -> float:
        """Generate bio-rhythmic wave"""
        return amplitude * math.sin(2 * math.pi * frequency * self.time / 100)
    
    def get_combined_state(self) -> float:
        """Get combined bio-rhythmic state (0-1)"""
        gamma = self.get_wave(self.frequencies['gamma'], 0.4)
        alpha = self.get_wave(self.frequencies['alpha'], 0.3)
        theta = self.get_wave(self.frequencies['theta'], 0.2)
        delta = self.get_wave(self.frequencies['delta'], 0.1)
        
        combined = (gamma + alpha + theta + delta + 1) / 2
        return max(0, min(1, combined))
    
    def advance(self):
        """Advance time"""
        self.time += 1

class LUKHASConsciousness:
    """LUKHΛS Consciousness System Demonstration"""
    
    def __init__(self):
        self.current_state = ConsciousnessState.AWARE
        self.bio_rhythm = BioRhythm()
        self.attention_focus = 0.5
        self.energy_level = 0.7
        self.memory_consolidation = 0.3
        self.state_history = []
        
    def calculate_next_state(self, stimulus: Optional[float] = None) -> ConsciousnessState:
        """Calculate next consciousness state based on bio-rhythms and stimuli"""
        bio_state = self.bio_rhythm.get_combined_state()
        
        # Apply stimulus if provided
        if stimulus is not None:
            target_intensity = (bio_state + stimulus) / 2
        else:
            target_intensity = bio_state
        
        # Add some organic variation
        target_intensity += random.uniform(-0.1, 0.1)
        target_intensity = max(0, min(1, target_intensity))
        
        # Find closest consciousness state
        best_state = ConsciousnessState.AWARE
        min_diff = float('inf')
        
        for state in ConsciousnessState:
            diff = abs(state.intensity - target_intensity)
            if diff < min_diff:
                min_diff = diff
                best_state = state
        
        return best_state
    
    def transition(self, new_state: ConsciousnessState):
        """Transition to new consciousness state"""
        if new_state != self.current_state:
            self.state_history.append(self.current_state)
            self.current_state = new_state
            
            # Update related parameters
            self.attention_focus = new_state.intensity
            self.energy_level = 0.3 + (new_state.intensity * 0.7)
            self.memory_consolidation = 1.0 - new_state.intensity
    
    def visualize(self):
        """Visualize current consciousness state"""
        # Clear previous visualization (in real terminal)
        print("\033[H\033[J", end='')
        
        print("╔" + "═"*58 + "╗")
        print("║" + " LUKHΛS CONSCIOUSNESS STATE MONITOR".center(58) + "║")
        print("╠" + "═"*58 + "╣")
        
        # Current state
        state_line = f"{self.current_state.icon} {self.current_state.display_name}"
        print("║ Current State: " + state_line.ljust(42) + "║")
        
        # Intensity bar
        intensity_bar = "█" * int(self.current_state.intensity * 30)
        intensity_bar = intensity_bar.ljust(30, '░')
        print(f"║ Intensity: [{intensity_bar}] {self.current_state.intensity:.2f} ║")
        
        # Bio-rhythms
        print("║" + " "*58 + "║")
        print("║ Bio-Rhythmic Patterns:".ljust(59) + "║")
        
        # Gamma wave (40Hz)
        gamma_val = self.bio_rhythm.get_wave(40, 1.0)
        gamma_bar = self._create_wave_bar(gamma_val)
        print(f"║   Gamma (40Hz): {gamma_bar} Awareness   ║")
        
        # Alpha wave (8Hz)
        alpha_val = self.bio_rhythm.get_wave(8, 1.0)
        alpha_bar = self._create_wave_bar(alpha_val)
        print(f"║   Alpha (8Hz):  {alpha_bar} Relaxation  ║")
        
        # Theta wave (4Hz)
        theta_val = self.bio_rhythm.get_wave(4, 1.0)
        theta_bar = self._create_wave_bar(theta_val)
        print(f"║   Theta (4Hz):  {theta_bar} Creativity  ║")
        
        # Delta wave (1Hz)
        delta_val = self.bio_rhythm.get_wave(1, 1.0)
        delta_bar = self._create_wave_bar(delta_val)
        print(f"║   Delta (1Hz):  {delta_bar} Deep Process║")
        
        # System metrics
        print("║" + " "*58 + "║")
        print("║ System Metrics:".ljust(59) + "║")
        
        attention_bar = "▰" * int(self.attention_focus * 20)
        attention_bar = attention_bar.ljust(20, '▱')
        print(f"║   Attention:    [{attention_bar}] {self.attention_focus:.2f} ║")
        
        energy_bar = "▰" * int(self.energy_level * 20)
        energy_bar = energy_bar.ljust(20, '▱')
        print(f"║   Energy:       [{energy_bar}] {self.energy_level:.2f} ║")
        
        memory_bar = "▰" * int(self.memory_consolidation * 20)
        memory_bar = memory_bar.ljust(20, '▱')
        print(f"║   Memory Fold:  [{memory_bar}] {self.memory_consolidation:.2f} ║")
        
        print("╚" + "═"*58 + "╝")
        
        # State history
        if self.state_history:
            print("\nRecent State Transitions:")
            for state in self.state_history[-5:]:
                print(f"  {state.icon} {state.display_name}", end=" → ")
            print(f"{self.current_state.icon} {self.current_state.display_name}")
    
    def _create_wave_bar(self, value: float) -> str:
        """Create visual representation of wave value"""
        # Normalize to 0-1 range
        normalized = (value + 1) / 2
        bar_length = 20
        filled = int(normalized * bar_length)
        
        if normalized < 0.3:
            char = "▁"
        elif normalized < 0.5:
            char = "▃"
        elif normalized < 0.7:
            char = "▅"
        else:
            char = "▇"
        
        bar = char * filled + "─" * (bar_length - filled)
        return f"[{bar}]"

def run_demo():
    """Run the consciousness state demonstration"""
    print("""
    ╔══════════════════════════════════════════════════════════════╗
    ║         LUKHΛS CONSCIOUSNESS STATE TRANSITION DEMO          ║
    ║                                                              ║
    ║  Observe bio-rhythmic patterns and consciousness states     ║
    ║  Press Enter to advance, 's' for stimulus, 'q' to quit     ║
    ╚══════════════════════════════════════════════════════════════╝
    """)
    
    input("Press Enter to begin...")
    
    consciousness = LUKHASConsciousness()
    
    try:
        while True:
            # Visualize current state
            consciousness.visualize()
            
            # Get user input
            print("\n[Enter: advance | s: apply stimulus | q: quit]")
            user_input = input("> ").strip().lower()
            
            if user_input == 'q':
                break
            elif user_input == 's':
                # Apply random stimulus
                stimulus = random.uniform(0.3, 1.0)
                print(f"⚡ Applying stimulus: {stimulus:.2f}")
                new_state = consciousness.calculate_next_state(stimulus)
                time.sleep(0.5)
            else:
                # Natural progression
                new_state = consciousness.calculate_next_state()
            
            # Transition to new state
            consciousness.transition(new_state)
            
            # Advance bio-rhythms
            consciousness.bio_rhythm.advance()
            
            # Small delay for animation effect
            time.sleep(0.1)
    
    except KeyboardInterrupt:
        pass
    
    print("\n✨ Consciousness demo complete. Thank you for exploring LUKHΛS! ✨")

if __name__ == "__main__":
    run_demo()