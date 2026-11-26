# Convert Japanese srv1 captions to plain text without timestamps.
# Use one paragraph per video to reduce token usage.
import html, re, sys, pathlib

root = pathlib.Path(__file__).parent
titles = {}
for line in (root / "list.tsv").read_text(encoding="utf-8").splitlines():
    vid, title, dur = line.split("\t")
    titles[vid] = (title, dur)

out_dir = root / "text"
out_dir.mkdir(exist_ok=True)
order = [l.split("\t")[0] for l in (root / "list.tsv").read_text(encoding="utf-8").splitlines()]
order.reverse()  # Oldest first

n = 0
for i, vid in enumerate(order):
    if "まとめ" in titles[vid][0]:  # Japanese marker for compilation videos
        continue
    n += 1  # Reserve the number even when captions are missing so adding them later preserves numbering.
    f = None
    for lang in ("ja-orig", "ja"):
        p = root / "raw" / f"{vid}.{lang}.srv1"
        if p.exists():
            f = p
            break
    if not f:
        print("Missing captions:", vid, titles[vid][0], file=sys.stderr)
        continue
    xml = f.read_text(encoding="utf-8")
    parts = [html.unescape(html.unescape(t)) for t in re.findall(r"<text[^>]*>(.*?)</text>", xml, re.S)]
    body = "".join(p.replace("\n", "").strip() for p in parts)
    body = re.sub(r"\[[^\]]*\]", "", body)  # Remove cues such as [music] and [applause].
    body = re.sub(r"\s+", " ", body)
    (out_dir / f"{n:03d}_{vid}.txt").write_text(f"# {titles[vid][0]}\n{body}\n", encoding="utf-8")
print(n, "episodes")
