from pipeline import extract_text, to_sorted_items, group_into_lines

result = extract_text('data/samples/kvitto6.jpeg')
sorted_list = to_sorted_items(result)
lines = group_into_lines(sorted_list)
for line in lines:
    print(line)