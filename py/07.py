import re

test_case = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags."""

rules = test_case.split("\n")


def parse_rule(rule):
    rule_split = re.split("contain|,", rule)
    rule_bags = [re.sub("bag(s?)|\.", "", i).strip() for i in rule_split]
    bag_color, *other_bags = rule_bags
    other_bags_split = [re.match("([0-9]*?)( ?)([a-z ]+)", i).groups() for i in other_bags]
    other_bags_clean = [i[2] for i in other_bags_split if i[2] != "no other"]
    other_bags_number = [try_converting_to_int(i[0]) for i in other_bags_split if i[2] != "no other"]
    return bag_color, other_bags_clean, other_bags_number


def try_converting_to_int(s):
    try:
        return int(s)
    except ValueError:
        return 0


parsed_rules = list(map(parse_rule, rules))


def count_bag_colors(bag_color, parsed_rules):
    color_set = {bag_color}
    old_color_set = set()

    while old_color_set != color_set:
        old_color_set = old_color_set.union(color_set)
        new_colors = [rule[0] for rule in parsed_rules if len(color_set.intersection(rule[1])) > 0]
        [color_set.add(color) for color in new_colors]

    return len(color_set) - 1


assert count_bag_colors('shiny gold', parsed_rules) == 4


x = open("raw/07.txt").read().split("\n")
parsed_rules = list(map(parse_rule, x))
count_bag_colors('shiny gold', parsed_rules)


## Part Two

test_case2 = """shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags."""

rules2 = test_case2.split("\n")


def count_bags_one_level(color, parsed_rules):
    for rule in parsed_rules:
        outer_bag, colors, numbers = rule
        if outer_bag == color:
            return sum(numbers), colors


def rec_test(color, parsed_rules_key, total_count = 0):
    if len(color) == 0:
        return total_count
    else:
        new_colors, bag_count = parsed_rules_key.get(color)
        print(color, " // colors: ", new_colors, "bag count: ", bag_count)
        for c, bc in zip(new_colors, bag_count):
            sub_bag_count = rec_test(c, parsed_rules_key, 0)
            print(c, "total count:", sub_bag_count)
            total_count += (sub_bag_count + 1) * bc
        print(color, "total:", total_count)
        return total_count


parsed_rules = list(map(parse_rule, rules))
parsed_rules_key = {i[0]:(i[1], i[2]) for i in parsed_rules}
test_out = rec_test("shiny gold", parsed_rules_key)
assert test_out == 32


parsed_rules2 = list(map(parse_rule, rules2))
parsed_rules_key2 = {i[0]:(i[1], i[2]) for i in parsed_rules2}
test_out2 = rec_test("shiny gold", parsed_rules_key2)
assert test_out2 == 126


x = open("raw/07.txt").read().split("\n")
parsed_rules = list(map(parse_rule, x))
parsed_rules_key = {i[0]:(i[1], i[2]) for i in parsed_rules}
rec_test("shiny gold", parsed_rules_key)
