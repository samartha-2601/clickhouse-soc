from backend.detection_engine.rule_loader import load_rules

rules = load_rules()

for rule in rules:

    print(rule)