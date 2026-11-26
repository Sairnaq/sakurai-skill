# sakurai-skill

An Agent Skill for game development based on AI summaries of the Japanese captions from **all 257 main episodes** of [Masahiro Sakurai on Creating Games](https://www.youtube.com/@sora_sakurai_jp). You can watch the series on the [official English channel](https://www.youtube.com/@sora_sakurai_en).

Use it to design, review, and refine gameplay, difficulty, rewards, onboarding, game feel (hitstop, jumping, camera), animation, effects, graphics, UI, and audio. It also covers parameter tuning, debugging, team management, game proposals, and marketing. It can help diagnose feedback like “the hits feel weak” or “the controls feel sluggish.”

> This is an unofficial fan project. It has no affiliation with Masahiro Sakurai or Sora Ltd. The skill contains AI-generated summaries. Consult the original videos for Sakurai’s exact wording and context.

## Watch the walkthrough

The [announcement on X](https://x.com/MvKWt5XpPV36233/status/2120977715864252887) includes a roughly 100-second walkthrough. It uses the example game to show installation, prompting, ways to improve impact feedback, a second AI agent’s review, and a level design pass.

## Install

```bash
git clone https://github.com/Sairnaq/sakurai-skill.git
mkdir -p ~/.claude/skills
cp -r sakurai-skill/skills/sakurai ~/.claude/skills/
```

In Claude Code, try “What would Sakurai do?” or “Review this game’s feel.”

## Example game — Hajiki

<img src="examples/hajiki/hajiki_icon.gif" width="160" align="right">

An AI agent using the skill built this single-screen action game in Godot 4.6, from initial design through polish, title screen, and icon. The closer an enemy projectile gets before you deflect it, the harder it hits on the way back.

- [Play on unityroom](https://unityroom.com/games/hajiki)
- [See how the game used the skill, with episode numbers](examples/hajiki/README.md)

<br clear="right">

## Repository layout

```text
skills/sakurai/
  SKILL.md            14 sections of principles and workflows for design, review, and game feel
  references/         Episode summaries by topic, intended for selective reading
    gameplay.md  planning.md  concepts.md  specs.md  motion.md  effects.md  graphics.md
    ui.md  sound.md  tech.md  team.md  mindset.md  pr.md  misc.md
tools/
  to_text.py          Convert Japanese srv1 captions into plain text without timestamps
  build_refs.py       Group episode notes into reference files by category
```

- For specific values, procedures, and examples from published games, open the relevant file in `references/`.
- Episode numbers and titles identify the source for each summary. The numbers follow the repository’s oldest-first source order (001–259).

## Related project

[kokuren333/Sakurai-Skills](https://github.com/kokuren333/Sakurai-Skills) is an earlier project based on the same channel.

| | kokuren333/Sakurai-Skills | This repository |
|---|---|---|
| Source material | Gemini summaries of the category compilations, excluding Grab Bag episodes. Its README says the notes were not checked against the videos. | Summaries made directly from automatically generated captions for all 257 main episodes. |
| Coverage | 177 principles and 17 cross-cutting principles | All 257 main episodes, including Grab Bag episodes in `misc.md` |
| Language | Primarily English, with a Japanese README | English translation of [the Japanese original](https://github.com/kociden/sakurai-skill) |
| Structure | 24 task-specific skills, a router, checklists, a principle graph, lint rules, and tests | One skill with 14 reference files |
| Source tracking | SOURCE, GENERALIZED, and AGENT layers distinguish the source notes from interpretations. | Episode numbers and titles accompany the summaries. |
| Typical use | Repeatable reviews and checklists across stages of a large project | Quick access during a conversation, including specific values, procedures, and examples |

Both projects use AI-generated summaries and have not been checked by hand against every video. Automatic captioning errors may carry over into these summaries.

## Notes

- Sakurai draws heavily on experience with large productions and action games. Adapt the principles to the project’s genre and scale, with the player’s enjoyment as the deciding factor.
- Please open an issue if you find an error or omission.
