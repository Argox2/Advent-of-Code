import logging
import re
from collections import defaultdict

logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger(__name__)

data = '''
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
'''.strip()

rules, manuals = re.split(r'\n\s*\n', data)


# Prepare rules. 
list_rules = re.findall(r'\d+', rules)

dict_rules = defaultdict(list)

for i in range(1, len(list_rules), 2):
    key = int(list_rules[i])
    value = int(list_rules[i-1])
    dict_rules[key].append(value)

logger.info("Rules:")
for key, values in dict_rules.items():
    logger.info(f"  {key}: {values}")

# Prepare manuals. 
list_manuals = [[int(num) for num in re.split(r',', manual)] for manual in re.split(r'\n', manuals)]

logger.info("Manuals:")
for manual in list_manuals:
    logger.info(f"  {manual}")


def order_manual(manual):
    for i, page in enumerate(manual):
        logger.info(f"  Page: {page}")

        if page in dict_rules.keys():
            logger.info(f"    Pages should be before: {set(dict_rules[page])}")
            logger.info(f"    Pages actually are after: {set(manual[i+1:])}")

            coincidence_set = set(dict_rules[page]) & set(manual[i+1:])
            logger.info(f"    Coincidences: {coincidence_set}")

            if len(coincidence_set) > 0:
                coincidence = coincidence_set.pop()
                temp_page = page

                manual[i] = coincidence
                # print(manual)
                manual.insert(i+1, temp_page)
                # print(manual)
                del manual[manual.index(coincidence, i+1)]
                # print(manual)
                return False, manual

    return True, manual


add_up = 0

for manual in list_manuals:
    logger.info(f"Manual: {manual}")

    order = False
    manual_temp = manual
    attemps = 0

    while not order:
        logger.info(f"Temp manual: {manual}")
        order, manual_temp = order_manual(manual_temp)
        attemps += 1

    manual = manual_temp

    if attemps > 1:
        logger.info(f"New ordered manual: {manual}")
        middle_page = manual[len(manual) // 2]
        logger.info(middle_page)
        add_up += middle_page 

logger.info(f"Middle page add up = {add_up}")



