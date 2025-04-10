from datetime import datetime
import json

class BaseMindEngine:
    def __init__(self, threshold=2):
        self.threshold = threshold
        self.insight_history = []

    def load_insight_memory(self, filepath="logs/insight_history.json"):
        try:
            with open(filepath, "r") as f:
                self.insight_history = json.load(f)
            return True
        except (FileNotFoundError, json.JSONDecodeError):
            self.insight_history = []
            return False

    def clarity_signal_detected(self, logic_stream, pattern_stream):
        overlap = list(set(logic_stream).intersection(set(pattern_stream)))
        return overlap if len(overlap) >= self.threshold else []

    def emotional_alignment_confirmed(self, response):
        return response.lower().strip() == "y"

    def logic_integrity_verified(self, fallacy_response, pressure_response):
        return fallacy_response == "n" and pressure_response == "y"

    def compute_resonance_score(self, responses):
        score = 0
        if responses["resonance"] == "y":
            score += 40
        if responses["fallacy"] == "n":
            score += 30
        if responses["pressure"] == "y":
            score += 30
        if responses["action"].strip():
            score += 10
        return min(score, 100)

    def compute_recursion_depth(self, insight):
        similar = [entry for entry in self.insight_history if entry["insight"] == insight]
        return len(similar) + 1

    def action_gate_protocol(self, insight, action_area):
        return action_area

    def embody_insight(self, logic_stream, pattern_stream, insight, responses, phase="UNSPECIFIED"):
        overlap = self.clarity_signal_detected(logic_stream, pattern_stream)
        if overlap:
            if self.emotional_alignment_confirmed(responses["resonance"]):
                if self.logic_integrity_verified(responses["fallacy"], responses["pressure"]):
                    action = self.action_gate_protocol(insight, responses["action"])
                    self.log_insight(insight, overlap, action, phase, responses)
                    return "Insight embodied and deployed.", True
        return "Recursion continues — insight not fully stabilized.", False

    def log_insight(self, insight, overlap, action, phase, responses):
        recursion_depth = self.compute_recursion_depth(insight)
        resonance_score = self.compute_resonance_score(responses)
        entry = {
            "timestamp": datetime.now().isoformat(),
            "insight": insight,
            "overlap": overlap,
            "action": action,
            "phase": phase,
            "recursion_depth": recursion_depth,
            "resonance_score": resonance_score
        }
        self.insight_history.append(entry)

    def export_insights_to_json(self, filepath="logs/insight_history.json"):
        with open(filepath, "w") as f:
            json.dump(self.insight_history, f, indent=4)
        return filepath

    def analyze_identity_arc(self):
        themes = {}
        for entry in self.insight_history:
            for term in entry["overlap"]:
                themes[term] = themes.get(term, 0) + 1
        sorted_themes = sorted(themes.items(), key=lambda x: x[1], reverse=True)
        top_themes = [f"{theme} x{count}" for theme, count in sorted_themes[:5]]
        phases = [entry["phase"] for entry in self.insight_history]
        dominant_phase = max(set(phases), key=phases.count) if phases else "UNDEFINED"
        dominant_theme = sorted_themes[0][0] if sorted_themes else "None"
        return top_themes, dominant_phase, dominant_theme
