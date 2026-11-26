# Group episode summaries from notes/*.md into skill reference files by category.
# Keep the first entry for each episode number. Send low-insight episodes to misc.
import re, sys, pathlib

root = pathlib.Path(__file__).parent
out = pathlib.Path(sys.argv[1])
out.mkdir(parents=True, exist_ok=True)

# Japanese tags are accepted so notes from the original workflow still work.
CATEGORIES = (
    ("ゲーム性", "Game Essence", "gameplay", "Game essence (risk and reward, strategy, difficulty, rewards)"),
    ("企画・ゲーム設計", "Planning & Game Design", "planning", "Planning and game design (onboarding, tutorials, rewards, time, originality)"),
    ("企画コンセプト", "Game Concepts", "concepts", "Game concepts (design challenges and solutions in Sakurai’s games)"),
    ("仕様", "Design Specifics", "specs", "Design specifics (hitstop, jumping, cameras, ledges, transitions, randomness)"),
    ("モーション", "Animation", "motion", "Animation (windup, attack poses, follow-through, exaggeration)"),
    ("エフェクト", "Effects", "effects", "Effects (hit effects, explosions, screen shake, flashes)"),
    ("グラフィック", "Graphics", "graphics", "Graphics (lighting, scale, collision readability, art direction)"),
    ("UI", "UI", "ui", "UI (menus, text, HUDs, control remapping, skipping)"),
    ("サウンド", "Audio", "sound", "Audio (sound effect priorities, attack, background music, arrangements)"),
    ("プログラム・テクニカル", "Programming & Tech", "tech", "Programming and tech (parameters, debug modes, management)"),
    ("チーム運営", "Team Management", "team", "Team management (decisions, information sharing, testing, roles)"),
    ("仕事の姿勢", "Work Ethic", "mindset", "Work ethic (proposals, presentations, staying true to the concept)"),
    ("広報", "Marketing", "pr", "Marketing (showing gameplay, setting expectations, demos, updates)"),
)
CATS = {tag: (slug, heading) for japanese, english, slug, heading in CATEGORIES for tag in (japanese, english)}
CATS["Planning & Design"] = CATS["Planning & Game Design"]  # Official tag on episode 198.
MISC = ("misc", "Grab Bag and miscellaneous episodes")

text = "\n".join(p.read_text(encoding="utf-8") for p in sorted((root / "notes").glob("*.md")))
blocks = re.split(r"(?m)^(?=## \d{3} )", text)
seen, groups = set(), {}
for b in blocks:
    m = re.match(r"## (\d{3}) (.*)", b)
    if not m:
        continue
    num, title = m.groups()
    if num in seen:
        continue
    seen.add(num)
    body = b.strip()
    body = re.sub(r"\n# .*$", "", body, flags=re.S)  # Drop the next input file’s top-level heading.
    japanese_tag = re.search(r"【(.+?)】", title)
    english_tag = re.search(r"\[([^\[\]]+)\]\s*$", title)
    category_tag = japanese_tag or english_tag
    key = CATS.get(category_tag[1]) if category_tag else None
    summary = body.split("\n", 1)[-1]
    few_takeaways = summary.lstrip().startswith(("(Few takeaways)", "- (Few takeaways)"))
    if key is None or "（知見少なめ）" in summary[:12] or few_takeaways:
        key = MISC
    groups.setdefault(key, []).append((num, body))

for (slug, name), items in groups.items():
    items.sort()
    s = f"# {name}\n\nSummaries based on the Japanese captions for Masahiro Sakurai on Creating Games. Episode numbers follow the repository’s oldest-first source order.\n\n"
    s += "\n\n".join(b for _, b in items) + "\n"
    (out / f"{slug}.md").write_text(s, encoding="utf-8")
    print(slug, len(items))
print("Total:", len(seen))
