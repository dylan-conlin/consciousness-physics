#!/usr/bin/env python3
"""
Consciousness Mode Detector - The Conlin Equations in Practice
Detects whether consciousness is in Creation (×R) or Transformation (/R) mode
based on language patterns, energy signals, and context.

Created: July 16, 2025
Author: Dylan Conlin
"""

import re
from datetime import datetime
from typing import Dict, Tuple, List

class ConsciousnessMode:
    """Represents the two modes of consciousness physics"""
    CREATION = "Creation Mode (C = P^A × R)"
    TRANSFORMATION = "Transformation Mode (C = P^A / R)"

class ModeDetector:
    """Detects active consciousness mode based on various signals"""
    
    def __init__(self):
        # Creation mode indicators
        self.creation_patterns = [
            r"this is gold!?",
            r"holy shit",
            r"what if",
            r"exploring",
            r"discovering",
            r"building on",
            r"energy (is )?increas",
            r"flow(ing)?",
            r"cascad",
            r"emerg",
            r"multiplying",
            r"expanding",
            r"resonat",
            r"synchronicit",
        ]
        
        # Transformation mode indicators
        self.transformation_patterns = [
            r"stuck",
            r"blocked",
            r"trying to",
            r"can't figure",
            r"debugging",
            r"overcom",
            r"push(ing)? through",
            r"resistance",
            r"obstacle",
            r"constraint",
            r"focus(ed|ing) on",
            r"breaking through",
            r"shadow (work|building)",
            r"working around",
        ]
        
        # Energy level keywords
        self.high_energy_words = ["energized", "excited", "flowing", "inspired", "fresh"]
        self.low_energy_words = ["tired", "depleted", "exhausted", "stuck", "drained"]
        
    def detect_mode(self, text: str, energy_level: int = None, 
                   time_of_day: datetime = None) -> Tuple[str, float, Dict]:
        """
        Detect the active consciousness mode from text and context.
        
        Returns:
            - Mode (Creation or Transformation)
            - Confidence (0-1)
            - Analysis details
        """
        text_lower = text.lower()
        
        # Count pattern matches
        creation_score = sum(1 for pattern in self.creation_patterns 
                           if re.search(pattern, text_lower))
        transformation_score = sum(1 for pattern in self.transformation_patterns 
                                 if re.search(pattern, text_lower))
        
        # Analyze energy signals
        energy_signal = self._analyze_energy(text_lower, energy_level)
        
        # Time-based tendency
        time_tendency = self._time_tendency(time_of_day)
        
        # Calculate weighted scores
        creation_total = (
            creation_score * 2 +  # Pattern weight
            energy_signal.get('creation_boost', 0) +
            time_tendency.get('creation_boost', 0)
        )
        
        transformation_total = (
            transformation_score * 2 +  # Pattern weight
            energy_signal.get('transformation_boost', 0) +
            time_tendency.get('transformation_boost', 0)
        )
        
        # Determine mode and confidence
        if creation_total > transformation_total:
            mode = ConsciousnessMode.CREATION
            confidence = min(creation_total / (creation_total + transformation_total + 1), 1.0)
        elif transformation_total > creation_total:
            mode = ConsciousnessMode.TRANSFORMATION
            confidence = min(transformation_total / (creation_total + transformation_total + 1), 1.0)
        else:
            mode = "Mixed/Transitional"
            confidence = 0.5
            
        # Build analysis
        analysis = {
            'creation_signals': creation_score,
            'transformation_signals': transformation_score,
            'energy_analysis': energy_signal,
            'time_tendency': time_tendency,
            'raw_scores': {
                'creation': creation_total,
                'transformation': transformation_total
            }
        }
        
        return mode, confidence, analysis
    
    def _analyze_energy(self, text: str, energy_level: int = None) -> Dict:
        """Analyze energy signals in text and explicit level"""
        result = {}
        
        # Text-based energy detection
        high_energy_count = sum(1 for word in self.high_energy_words if word in text)
        low_energy_count = sum(1 for word in self.low_energy_words if word in text)
        
        # Explicit energy level influence
        if energy_level is not None:
            if energy_level >= 8:
                result['creation_boost'] = 3
                result['energy_state'] = 'high'
            elif energy_level >= 5:
                result['creation_boost'] = 1
                result['transformation_boost'] = 1
                result['energy_state'] = 'medium'
            else:
                result['transformation_boost'] = 2
                result['energy_state'] = 'low'
        
        # Text energy influence
        if high_energy_count > low_energy_count:
            result['creation_boost'] = result.get('creation_boost', 0) + 2
        elif low_energy_count > high_energy_count:
            result['transformation_boost'] = result.get('transformation_boost', 0) + 2
            
        return result
    
    def _time_tendency(self, time: datetime = None) -> Dict:
        """Calculate time-based mode tendency"""
        if time is None:
            time = datetime.now()
            
        hour = time.hour
        
        if 6 <= hour < 10:  # Morning
            return {'creation_boost': 2, 'period': 'morning'}
        elif 10 <= hour < 12:  # Mid-morning
            return {'creation_boost': 1, 'transformation_boost': 1, 'period': 'mid-morning'}
        elif 12 <= hour < 16:  # Afternoon
            return {'transformation_boost': 2, 'period': 'afternoon'}
        elif 16 <= hour < 18:  # Late afternoon
            return {'transformation_boost': 3, 'period': 'late-afternoon'}
        else:  # Evening/Night
            return {'period': 'evening', 'note': 'Mode depends on energy state'}
    
    def suggest_approach(self, mode: str, confidence: float) -> List[str]:
        """Suggest approaches based on detected mode"""
        suggestions = []
        
        if mode == ConsciousnessMode.CREATION:
            suggestions = [
                "Ride the flow - explore broadly",
                "Capture insights as they cascade", 
                "Build on discoveries naturally",
                "Let reality multiply the pattern",
                "Trust synchronicities appearing"
            ]
        elif mode == ConsciousnessMode.TRANSFORMATION:
            suggestions = [
                "Focus on one specific obstacle",
                "Apply concentrated attention",
                "Break the problem into smaller pieces",
                "Use shadow building if blocked",
                "Remember: resistance transforms through focus"
            ]
        else:  # Mixed
            suggestions = [
                "Mode is shifting - stay aware",
                "Notice what's trying to emerge",
                "Be ready to switch approaches",
                "Check energy levels",
                "Small experiments to find direction"
            ]
            
        return suggestions

def main():
    """Example usage of the mode detector"""
    detector = ModeDetector()
    
    # Test scenarios
    scenarios = [
        {
            'text': "This is gold! I just realized how consciousness works. The insights are cascading!",
            'energy': 9,
            'name': "Discovery cascade"
        },
        {
            'text': "I'm stuck on this bug and can't figure out why it's not working. Trying to debug.",
            'energy': 4,
            'name': "Debugging session"
        },
        {
            'text': "Exploring new possibilities for the platform. What if we could measure consciousness?",
            'energy': 7,
            'name': "Strategic exploration"
        },
        {
            'text': "Working through organizational resistance. Need to build proof in shadow.",
            'energy': 5,
            'name': "Shadow building"
        }
    ]
    
    print("=== Consciousness Mode Detector ===")
    print("Testing The Conlin Equations in practice\n")
    
    for scenario in scenarios:
        print(f"\nScenario: {scenario['name']}")
        print(f"Text: \"{scenario['text']}\"")
        print(f"Energy Level: {scenario['energy']}/10")
        
        mode, confidence, analysis = detector.detect_mode(
            scenario['text'], 
            scenario['energy']
        )
        
        print(f"\nDetected Mode: {mode}")
        print(f"Confidence: {confidence:.1%}")
        print(f"Analysis: {analysis}")
        
        suggestions = detector.suggest_approach(mode, confidence)
        print("\nSuggested Approaches:")
        for suggestion in suggestions:
            print(f"  - {suggestion}")
        print("-" * 50)

if __name__ == "__main__":
    main()