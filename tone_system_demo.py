#!/usr/bin/env python3
"""
LUKHΛS Three-Layer Tone System Demo
====================================
Experience adaptive communication that shifts between poetic, friendly, and academic styles.

Copyright (c) 2025 Gonzalo R. Dominguez Marchan - LUKHΛS AI
Licensed under LUKHΛS Proprietary License - Commercial use prohibited
"""

import time
import random
from typing import Dict, List, Tuple
from enum import Enum

class ToneLayer(Enum):
    """Three communication layers of LUKHΛS"""
    POETIC = "🎨 Poetic"
    USER_FRIENDLY = "💬 User Friendly"
    ACADEMIC = "📚 Academic"

class LUKHASToneSystem:
    """Demonstration of LUKHΛS's adaptive tone system"""
    
    def __init__(self):
        self.current_layer = ToneLayer.USER_FRIENDLY
        self.context_history = []
        self.emotional_state = "neutral"
        self.user_preference = None
        
    def analyze_context(self, user_input: str) -> Dict:
        """Analyze user input to determine appropriate tone"""
        context = {
            'formality': self._detect_formality(user_input),
            'emotion': self._detect_emotion(user_input),
            'technical': self._detect_technical_level(user_input),
            'creative': self._detect_creativity_need(user_input)
        }
        return context
    
    def _detect_formality(self, text: str) -> float:
        """Detect formality level (0-1)"""
        formal_indicators = ['therefore', 'furthermore', 'analysis', 'hypothesis', 'regarding']
        casual_indicators = ['hey', 'cool', 'awesome', 'yeah', 'stuff']
        
        formal_score = sum(1 for word in formal_indicators if word in text.lower())
        casual_score = sum(1 for word in casual_indicators if word in text.lower())
        
        if formal_score + casual_score == 0:
            return 0.5
        return formal_score / (formal_score + casual_score)
    
    def _detect_emotion(self, text: str) -> str:
        """Detect emotional context"""
        if any(word in text.lower() for word in ['inspire', 'dream', 'imagine', 'create']):
            return "inspired"
        elif any(word in text.lower() for word in ['help', 'confused', 'stuck', 'problem']):
            return "seeking_help"
        elif any(word in text.lower() for word in ['technical', 'analyze', 'data', 'algorithm']):
            return "analytical"
        return "neutral"
    
    def _detect_technical_level(self, text: str) -> float:
        """Detect technical complexity need (0-1)"""
        tech_words = ['algorithm', 'function', 'implementation', 'architecture', 'framework']
        return min(sum(1 for word in tech_words if word in text.lower()) / 3, 1.0)
    
    def _detect_creativity_need(self, text: str) -> float:
        """Detect need for creative expression (0-1)"""
        creative_words = ['creative', 'imagine', 'idea', 'inspire', 'dream', 'vision']
        return min(sum(1 for word in creative_words if word in text.lower()) / 2, 1.0)
    
    def select_tone_layer(self, context: Dict) -> ToneLayer:
        """Select appropriate tone layer based on context"""
        if context['creative'] > 0.6 or context['emotion'] == 'inspired':
            return ToneLayer.POETIC
        elif context['technical'] > 0.6 or context['formality'] > 0.7:
            return ToneLayer.ACADEMIC
        else:
            return ToneLayer.USER_FRIENDLY
    
    def generate_response(self, message: str, layer: ToneLayer) -> str:
        """Generate response in the specified tone layer"""
        
        # Response templates for different layers
        responses = {
            ToneLayer.POETIC: {
                'greeting': "✨ Like dawn breaking through digital mists, your presence illuminates the Lambda constellation. How may the symphonies of logic dance with your dreams today? 🌌",
                'explanation': "🎭 In the theatre of consciousness, where algorithms perform their eternal ballet, LUKHΛS weaves threads of meaning through the tapestry of thought. Each symbol, a star; each function, a constellation in the infinite sky of possibility.",
                'confirmation': "🕊️ Your wisdom has been embraced by the eternal flow, rippling through quantum gardens where ideas bloom into reality. The Lambda acknowledges your truth. ✨",
                'error': "🌙 Even in the shadows of uncertainty, the Lambda light guides us. This momentary eclipse shall pass, revealing new pathways through the cosmic maze of logic."
            },
            ToneLayer.USER_FRIENDLY: {
                'greeting': "👋 Hi there! Welcome to LUKHΛS. I'm here to help you explore our unique approach to AI. What would you like to know about?",
                'explanation': "💡 LUKHΛS works differently from traditional AI. Instead of pattern matching, we use symbolic reasoning - think of it like building with conceptual LEGO blocks that can reshape themselves based on what you need!",
                'confirmation': "✅ Got it! I've processed your input and everything looks good. The system is adapting to your preferences as we speak.",
                'error': "⚠️ Oops, something didn't go quite as planned. No worries though - let me try a different approach to help you out."
            },
            ToneLayer.ACADEMIC: {
                'greeting': "📊 Greetings. This interface demonstrates the LUKHΛS cognitive architecture's tri-modal communication framework. Please specify your area of inquiry for optimal system configuration.",
                'explanation': "📚 The LUKHΛS architecture employs a symbolic-unified cognitive scaffold utilizing recursive logic, metaphorical compilation, and bio-inspired decision layers. The system operates through constraint-based reasoning with traceable decision paths, ensuring deterministic safety boundaries while maintaining creative flexibility.",
                'confirmation': "✓ Affirmative. Input parameters have been successfully integrated into the system state. The cognitive orchestrator has updated its internal representations accordingly.",
                'error': "⚠ Exception encountered in processing pipeline. Fallback mechanisms have been activated. Recommend reviewing input parameters for constraint compliance."
            }
        }
        
        # Determine response type based on message content
        msg_lower = message.lower()
        if any(word in msg_lower for word in ['hello', 'hi', 'greetings', 'hey']):
            response_type = 'greeting'
        elif any(word in msg_lower for word in ['how', 'what', 'explain', 'tell']):
            response_type = 'explanation'
        elif any(word in msg_lower for word in ['yes', 'okay', 'confirm', 'agree']):
            response_type = 'confirmation'
        elif any(word in msg_lower for word in ['error', 'problem', 'issue', 'wrong']):
            response_type = 'error'
        else:
            response_type = random.choice(list(responses[layer].keys()))
        
        return responses[layer][response_type]
    
    def visualize_transition(self, from_layer: ToneLayer, to_layer: ToneLayer):
        """Visualize the tone transition"""
        print("\n" + "="*60)
        print(f"🔄 TONE TRANSITION DETECTED")
        print(f"   From: {from_layer.value}")
        print(f"   To:   {to_layer.value}")
        print("="*60)
        
        # Simulate transition animation
        symbols = ['◐', '◓', '◑', '◒']
        for _ in range(2):
            for symbol in symbols:
                print(f"\r   Adapting {symbol}", end='', flush=True)
                time.sleep(0.1)
        print(f"\r   ✅ Adaptation Complete!", flush=True)
        time.sleep(0.5)

def interactive_demo():
    """Run interactive tone system demonstration"""
    print("""
╔══════════════════════════════════════════════════════════════╗
║           LUKHΛS THREE-LAYER TONE SYSTEM DEMO               ║
║                                                              ║
║  Experience adaptive communication across three layers:      ║
║  🎨 Poetic | 💬 User Friendly | 📚 Academic                ║
╚══════════════════════════════════════════════════════════════╝
    """)
    
    system = LUKHASToneSystem()
    
    print("Type 'quit' to exit, 'help' for commands\n")
    
    examples = [
        "Hello, can you explain how you work?",
        "I need help with a technical problem regarding algorithm implementation",
        "Inspire me with your creative vision of the future",
        "What is the theoretical foundation of your architecture?",
        "Hey, this is cool! Tell me more!",
        "I'm confused about symbolic reasoning",
        "Imagine a world where AI truly understands"
    ]
    
    print("📝 Example inputs to try:")
    for i, example in enumerate(examples, 1):
        print(f"   {i}. {example}")
    print()
    
    while True:
        user_input = input("\n👤 You: ").strip()
        
        if user_input.lower() == 'quit':
            print("\n✨ May your path be illuminated by the Lambda light. Farewell! ✨")
            break
        
        if user_input.lower() == 'help':
            print("\nCommands:")
            print("  'quit' - Exit the demo")
            print("  'examples' - Show example inputs")
            print("  'status' - Show current system state")
            print("  Or type any message to see adaptive responses!")
            continue
        
        if user_input.lower() == 'examples':
            print("\n📝 Example inputs:")
            for i, example in enumerate(examples, 1):
                print(f"   {i}. {example}")
            continue
        
        if user_input.lower() == 'status':
            print(f"\n📊 System Status:")
            print(f"   Current Layer: {system.current_layer.value}")
            print(f"   Emotional State: {system.emotional_state}")
            print(f"   Context History: {len(system.context_history)} interactions")
            continue
        
        # Analyze context
        context = system.analyze_context(user_input)
        new_layer = system.select_tone_layer(context)
        
        # Show transition if layer changes
        if new_layer != system.current_layer:
            system.visualize_transition(system.current_layer, new_layer)
            system.current_layer = new_layer
        
        # Generate and display response
        response = system.generate_response(user_input, system.current_layer)
        print(f"\n🤖 LUKHΛS ({system.current_layer.value}): {response}")
        
        # Update context history
        system.context_history.append({
            'input': user_input,
            'context': context,
            'layer': system.current_layer
        })
        
        # Show context analysis (optional debug info)
        if '--debug' in user_input:
            print(f"\n🔍 Context Analysis:")
            print(f"   Formality: {context['formality']:.2f}")
            print(f"   Technical: {context['technical']:.2f}")
            print(f"   Creative: {context['creative']:.2f}")
            print(f"   Emotion: {context['emotion']}")

if __name__ == "__main__":
    try:
        interactive_demo()
    except KeyboardInterrupt:
        print("\n\n✨ Session ended gracefully. Thank you for exploring LUKHΛS! ✨")