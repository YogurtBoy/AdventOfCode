import math

f = open("day4/manual.txt", "r")

# I AM RECURSIVE
def reorder_updates(rules, updates):
    corrected_updates = updates.copy()
    for ii, page in enumerate(corrected_updates):
        if page in rules:
            intersec = list(set(rules[page]).intersection(corrected_updates[0:ii]))
            if len(intersec):
                bad_idxs = []
                for mis_page in intersec:
                    bad_idxs.append(corrected_updates.index(mis_page))
                fix_idx = min(bad_idxs)
                corrected_updates.remove(page)
                corrected_updates.insert(fix_idx, page)
                return reorder_updates(rules, corrected_updates)
        
    return corrected_updates


rules = {}
page_count = 0
sugery_page_count = 0
for line in f:
    line = line.strip()
    if '|' in line:
        rule = line.split('|')
        if rule[0] in rules:
            rules[rule[0]].append(rule[1])
        else:
            rules[rule[0]] = [rule[1].strip()]
    elif ',' in line:
        updates = line.split(',')

        valid = True
        for ii, page in enumerate(updates):
            if page in rules:
                intersec = list(set(rules[page]).intersection(updates[0:ii]))
                if len(intersec):
                    valid = False
                    break

        if valid:
            middle_idx = math.floor(len(updates)/2)
            page_count += int(updates[middle_idx])
        else:
            corrected_updates = reorder_updates(rules, updates)
            middle_idx = math.floor(len(corrected_updates)/2)
            sugery_page_count += int(corrected_updates[middle_idx])

print(sugery_page_count)

f.close()