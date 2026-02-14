from typing import Dict

class VisualPromptAgent:
    """
    VisualPromptAgent converts structured scence intent into a diffusion-ready cinematic prompt.
    """
    
    def run(self, story_data: Dict) -> str:
        environment = story_data.get("environment", "environment")
        mood = story_data.get("mood", "cinematic")
        time_of_day = story_data.get("time_of_day", "")
        lighting = story_data.get("lighting", "cinematic lighting")

        prompt_parts = [
            f"cinematic {environment} {self._format_time(time_of_day)}",
            f"{mood} mood",
            lighting,
            "film still",
            "50mm lens",
            "eye-level camera",
            "shallow depth of field",
            "high realism",
            "detailed textures"
        ]
        return ", ".join(prompt_parts)
    def _format_time(self, time_of_day: str) -> str:
        if time_of_day:
            return f"at {time_of_day}"
        return ""
# Quick manual test
if __name__ == "__main__":
    from story_agent import StoryAgent

    story_agent = StoryAgent()
    visual_agent = VisualPromptAgent()

    story_data = story_agent.run(
        "A dark cyberpunk alley at night with neon lights and rain"
    )

    visual_prompt = visual_agent.run(story_data)
    print("Visual Prompt:\n", visual_prompt)