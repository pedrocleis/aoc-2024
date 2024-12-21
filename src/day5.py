from collections import defaultdict

with open("inputs/day5.txt", "r", encoding="utf-8") as f:
  content = f.read().split("\n\n")
  rules = content[0].split("\n")
  updates = content[1].split("\n")

def get_rules(rules):
  rule_dict = {}
  for rule in rules:
    rule_split = rule.split("|")
    if rule_split[0] not in rule_dict:
      rule_dict[rule_split[0]] = []
    rule_dict[rule_split[0]].append(rule_split[1])
  return rule_dict

def get_updates(updates, rules_dict, count1, count2):
  for update in updates:
    update_ok = True
    update_split = update.split(",")
    for i in range(len(update_split)):
      if update_split[i] in rules_dict:
        for j in range(len(rules_dict[update_split[i]])):
          if rules_dict[update_split[i]][j] in update_split:
            update_j = update_split.index(rules_dict[update_split[i]][j])
            if i > update_j:
              update_ok = False
              break
      if not update_ok:
        break
    if update_ok:
      count1 += int(update_split[int(len(update_split)//2)])
    else:
      count2 += make_update_right(update_split, rules_dict)
  return count1, count2

def make_update_right(update, rules_dict):
  rules_dict = defaultdict(list, rules_dict)
  sorted_update = sorted(update, key=lambda x: sum(1 for dep in rules_dict.get(x, []) if dep in update), reverse=True)
  return int(sorted_update[int(len(sorted_update)//2)])

count1 = 0
count2 = 0
rule_dict = get_rules(rules)
print(get_updates(updates, rule_dict, count1, count2))