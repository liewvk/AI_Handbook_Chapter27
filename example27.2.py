def tutor_prompt(topic, learner_level):
    return (f"Teach {topic} to a {learner_level} learner. "
            "Explain the idea, show one worked example, "
            "then ask two questions without revealing answers. "
            "State any uncertainty.")
print(tutor_prompt("linear regression", "beginner"))

