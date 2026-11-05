import ast
from pathlib import Path

root = Path(__file__).resolve().parent

words_text = (root / "data" / "words.js").read_text(encoding="utf-8")
synonyms_text = (root / "data" / "synonyms.js").read_text(encoding="utf-8")

words_obj = words_text.split("=", 1)[1].strip().rstrip(";")
synonyms_obj = synonyms_text.split("=", 1)[1].strip().rstrip(";")

words = ast.literal_eval(words_obj)
synonyms = ast.literal_eval(synonyms_obj)

group_counts = {}
for item in synonyms:
    group_counts[item["group"]] = group_counts.get(item["group"], 0) + 1

print(f"synonyms_total={len(synonyms)}")
print(f"group_counts={group_counts}")
assert len(synonyms) == 809, len(synonyms)
assert len(group_counts) == 10, len(group_counts)
assert sum(group_counts.values()) == 809, sum(group_counts.values())
assert sorted(group_counts.values()) == [80, 81, 81, 81, 81, 81, 81, 81, 81, 81], sorted(group_counts.values())

seen = set()
for item in synonyms:
    pair = tuple(sorted((item["a"], item["b"])))
    assert pair not in seen, f"duplicate pair: {pair}"
    seen.add(pair)

for item in synonyms:
    assert item["a"] in words, f"missing word {item['a']}"
    assert item["b"] in words, f"missing word {item['b']}"
    assert words[item["a"]]["def"], f"empty def for {item['a']}"
    assert words[item["b"]]["def"], f"empty def for {item['b']}"

print("check_ok")
