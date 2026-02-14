from typing import Dict


class StoryAgent:
    """
    StoryAgent converts a raw user story prompt into a structured scene intent.
    This version uses simple rules (no LLM) for clarity and debuggability.
    """

    def run(self, user_prompt: str) -> Dict:
        user_prompt_lower = user_prompt.lower()

        environment = self._infer_environment(user_prompt_lower)
        mood = self._infer_mood(user_prompt_lower)
        time_of_day = self._infer_time(user_prompt_lower)
        lighting = self._infer_lighting(user_prompt_lower)

        return {
            "environment": environment,
            "mood": mood,
            "time_of_day": time_of_day,
            "lighting": lighting,
            "camera_style": "cinematic film still",
            "scale": "human-scale"
        }

    def _infer_environment(self, text: str) -> str:
        if "alley" in text:
            return "urban alley"
        if "forest" in text:
            return "forest environment"
        if "city" in text:
            return "urban cityscape"
        return "generic environment"

    def _infer_mood(self, text: str) -> str:
        if "dark" in text or "moody" in text:
            return "dark, cinematic"
        if "bright" in text:
            return "bright, vibrant"
        return "neutral cinematic"

    def _infer_time(self, text: str) -> str:
        if "night" in text:
            return "night"
        if "dawn" in text or "sunrise" in text:
            return "dawn"
        if "dusk" in text or "sunset" in text:
            return "dusk"
        return "daytime"

    def _infer_lighting(self, text: str) -> str:
        if "neon" in text:
            return "neon rim lighting"
        if "sunlight" in text:
            return "natural sunlight"
        return "soft cinematic lighting"


# Quick manual test
if __name__ == "__main__":
    agent = StoryAgent()
    result = agent.run(
        "A dark cyberpunk alley at night with neon lights and rain"
    )
    print(result)
