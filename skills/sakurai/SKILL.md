---
name: sakurai
description: Apply game development principles summarized from all 257 main episodes of Masahiro Sakurai on Creating Games. Use for game design, reviews, or fixes involving gameplay, difficulty, rewards, tutorials, game feel (hitstop, jumping, camera), animation, effects, graphics, UI, audio, tuning, debugging, team management, design proposals, and marketing (trailers, demos, store pages). Use when feedback says a game feels dull, weak, sluggish, visually flat, too hard or easy, or struggles to attract players. Also use when writing game specifications, looking for improvements, or asked what Sakurai would do.
---

# Masahiro Sakurai’s game development principles

Based on AI summaries of the Japanese automatic captions from [Masahiro Sakurai on Creating Games](https://www.youtube.com/@sora_sakurai_en). This skill covers all 257 main episodes in the source set, excluding the compilations.

This file summarizes the principles. Open the relevant file in `references/` when you need specific values, procedures, or examples from published games.

| File | Topics |
|---|---|
| [gameplay.md](references/gameplay.md) | Risk and reward, gameplay across action games, shooters, RPGs, falling-block puzzles, sims, and task-based games, plus difficulty, rewards, randomness, and balance |
| [planning.md](references/planning.md) | Onboarding, tutorials, rewards, fetch quests, story, cutscenes, CPU opponents, customization, originality, and sequels |
| [concepts.md](references/concepts.md) | Design problems and solutions from Kirby, Super Smash Bros., Kirby Air Ride, Meteos, Kid Icarus, and Mushiking |
| [specs.md](references/specs.md) | Eight hitstop guidelines, jumps, camera targets, ledges, units of speed, transitions, stick flicks, and offset centers of gravity |
| [motion.md](references/motion.md) | Windup, strike, and follow-through, attack and damage poses, exaggeration, interpolation and blending, facial animation, and two-axis rotation |
| [effects.md](references/effects.md) | Seven guidelines for hit effects, stages of an explosion, screen shake, flashes, slash trails, and particle cost |
| [graphics.md](references/graphics.md) | Lighting, readability of collidable objects, sense of scale, cohesive art direction, silhouettes, paintovers, and final output |
| [ui.md](references/ui.md) | Clarity and style, type size, color coding, HUDs, control remapping, skipping, help text, and accessibility |
| [sound.md](references/sound.md) | Sound effect priorities, strong attack and moderate reverb, BPM, ambience, arranging music, and audio direction |
| [tech.md](references/tech.md) | Externalized parameters, 【】 notation, live tuning, debug modes, tickets, and version control |
| [team.md](references/team.md) | Prompt decisions, daily reports and screenshots, team presentations, debugging, coordination costs, and cutting scope |
| [mindset.md](references/mindset.md) | Proposals, presentations, committing to a concept and a single plan, decision ownership, and finding ideas |
| [pr.md](references/pr.md) | Showing gameplay first, setting accurate expectations, demo costs, regular updates, and live demonstrations |
| [misc.md](references/misc.md) | Grab Bag episodes on latency, the value of games, competition with older releases, and making the YouTube series |

---

## 0. Guiding principles

- **The ultimate goal is to entertain the player.** Return to that goal when in doubt. Judge decisions from the player’s perspective. Would you explain the reasoning behind that feature to every player?
- **Making games is the work of creating play.** You can design for any genre if you can take apart what makes it fun.
- **Break down what makes play enjoyable.** Analyze the source of the fun and rebuild it in an original form. For example, the risk and reward of drifting in a racing game became charging with the brakes and releasing on the way out in Kirby Air Ride.
- **Give players several reasons to choose your game over its inspiration.** Define original appeals beyond “a game like X.”

## 1. Game essence and risk–reward

- Game essence comes from **decisions where taking a risk can earn a reward**. A good strategy gets the reward while managing the risk.
- **Keep risks and rewards close together and proportional.** Getting close is dangerous, and it lets you land Mario’s stomp or a point-blank burst in Darius. A powerful move can leave a big opening. Calibrate rewards and penalties to what the player actually accomplished.
- Spell out each action’s tradeoff. Jump farther by taking off at the edge and risk falling. Dash for speed and give up control. Close in to strike and enter the enemy’s range. Shoot from safety and manage ammo and positioning. Dodge or parry at the last moment for a bigger payoff.
- **Use opposing forces to make an action feel good.** Falling gives meaning to floating, a slowdown gives meaning to speed, and flying under a bridge feels good because a collision would end the run.
- **Build tension and release it.** Enemies, obstacles, or puzzles create stress. Clearing a barrier, growing stronger, or moving forward releases it. Any obstacle that can create tension can serve this role.
- **Greater strategic depth can narrow the audience.** Choose a target audience before setting the stakes. The original Kirby used inhaling, a health system, and flight to lower risk for beginners. An experienced player’s small risk can be a beginner’s big one.
- **Tuning everything toward the average makes it bland.** Amplify weaknesses along with strengths. Preserve damage and tune recovery, hitboxes, or startup when appropriate. Super Smash Bros. Ultimate’s 87 fighters fell within roughly a 47–51% win-rate range, showing that distinct characters can still be balanced.
- **Give each character or enemy a trait you can describe in one sentence.** Even a stationary Gordo creates decisions through placement. Machines built on identical code can feel distinct when their parameters go to different extremes.
- **Randomness creates variety and rewards adaptation.** Use it carefully in contests decided by skill. A loss attributed solely to bad luck feels arbitrary. Random options tend to go over better when skill determines how well each player uses them.
- For casual competition, consider catch-up mechanics like Mario Kart’s. For skill-driven play, use mild catch-up and some variation in terrain or items. Rank-only leaderboards can discourage everyone below first place. A measure such as Global Smash Power shows where the player stands in the broader population.
- **Allow clever shortcuts.** In-game farming tricks and loopholes can make a game memorable. External modifications are outside this principle.

## 2. Difficulty, retries, and assistance

- Developers know their games inside out, so **err on the easy side of your first estimate**. Try playing one-handed or with reduced health to experience the difficulty from another angle.
- **Keep a path to completion open.** Offer a lower difficulty after repeated losses, a way to skip a bottleneck, or mid-game difficulty changes in a way that lets players save face.
- **Make retries quick.** The longer it takes to get control back after a defeat, the faster players lose interest. Fast restarts matter more than penalty severity. Keep defeat animations short and punchy.
- **Vary the difficulty curve.** Alternate bosses that make players rethink their strategy with easier stretches and opportunities to earn resources. Scaling every enemy to match the player can undermine the feeling of getting stronger.
- In roguelikes, keep teasing what lies ahead. Consider what a stuck player sees after repeating the same opening area.

## 3. Rewards and motivation

- **Decide on rewards as soon as you have the game’s basic structure.** Progress needs a payoff. One of the strongest is simply making the character more powerful.
- Give **numerical rewards a use**, and let players choose how to spend them when that creates interesting decisions. **Keep the next goal in sight**, such as the XP left to level up or gear they can nearly afford.
- Competitive games are a poor fit for permanent power upgrades. Reward players with unlockable characters, stages, music, collectibles, and modes. Achievements give players goals to pursue.
- **Celebrate good play.** Add cheers for KOs, applause for clearing a stage, or confetti to a losing player’s explosion to celebrate the winner.
- Reframe scores in memorable terms, such as brain age, total damage costs, or Global Smash Power.
- For fetch quests, offer fair rewards and frequent small payoffs, allow different routes, end the task promptly after completion, and give players a mystery or something to look forward to.
- Task-based games can revolve around earning money and buying tools that make the work easier. A recognizable premise helps players picture the end result, such as getting a dirty place clean.
- Make customization effects intuitive and visible, push strengths and weaknesses, add sorting or auto-equip, allow immediate testing, and make the result look good.

## 4. Onboarding, time, and pacing

- **Show what makes the game fun within the first three minutes.** Get to a highlight quickly. Kid Icarus: Uprising opens with a boss encounter within the first minute.
- **Teach through normal play.** Weave the tutorial into real encounters and let players learn through their actions. Plan early for how they will learn a complex control scheme.
- **Cut slow moments throughout the game.** Account for travel, waiting, idle time, fades, and black screens. Measure the share of time the player has control and err on the side of brisk pacing.
- Play time is a cost to the player. Keep the fun parts and the moments that support them. A promise of 300 hours has little appeal by itself.
- A button press should get a response. Let multiple buttons confirm choices, and give players a skip prompt if they press a button during a cutscene.
- **Make logos, openings, events, and cutscenes skippable and pausable.** Let players advance dialogue one line at a time when possible. Reassess pacing in an era of accelerated playback.
- Design the story and game mechanics together before full production. Favor the protagonist’s perspective, respect victories earned in play, and handle equipment when party members leave. Consider radio-style dialogue during play for players who want to keep moving.

## 5. Game feel and design specifics

- **Use hitstop in any genre where impacts need feedback.** Shake the target more and the attacker less, affecting visuals while keeping collision fixed. Shake horizontally on the ground and add a vertical component in the air. Start strong and taper off. Set duration using attack power times a move-specific coefficient. Blend the target to the damage pose over about four frames and increase amplitude when the camera is farther away. Add a freeze and flash to boss defeats and player deaths.
- **Start jumps with an initial velocity and constant gravity per frame.** Adapt to the goal. Mario uses variable height and a faster descent, while Ghosts ’n Goblins creates decisions by committing players to a jump arc. Faster descent can feel weightier. A brief extra boost in the first few frames can also help.
- **Keep the 3D camera’s target independent of the character.** Looser vertical tracking communicates height. A small offset in the direction of input can help aiming and add tension.
- **Control when players can fall off ledges.** Decide by action. An attack lunge or dodge can stop at the edge. In 3D, you can require a deliberate stick push to step off.
- Movement speed, inertia, jump physics, and frame rate can make the same button feel very different. Tune for the intended weight. A stable 60 fps is valuable.
- Agree on units of speed as distance over time early, so specifications can state concrete values. **Learn to estimate time in frames.** Counting “one and two and three and” is about 30 frames in Sakurai’s example. Fifteen frames are roughly the startup of a light attack.
- Treat analog stick flick speed as an input for dashes or dodges. Make thresholds adjustable to reduce accidental activations.
- **Offset the visual position or rotation axis slightly** for momentum and presence when straight motion or center-axis rotation looks mechanical.
- Optimization or a move to target hardware can change execution speed and difficulty. Recheck the game on the actual hardware after the move.

## 6. Animation

- Build attacks as **idle → windup → strike → follow-through**. Lock down the idle pose first, as it anchors the rest.
- **Make the windup immediate and exaggerated.** Change the pose on the first frame of input to show that it registered. Prioritize responsiveness over interpolated frames. Give a charge room to build and swing through in one frame. Automatic interpolation can make the strike feel soft.
- **The pose held during hitstop leaves the strongest impression.** Exaggerate it so it reads at a distance. Cross the body’s midline, break symmetry, twist the torso slightly, and check the silhouette from the gameplay camera.
- **Follow-through has the most screen time and shapes the impression.** Place the strike within the first quarter to third of the animation and use the rest for recovery. Powerful moves deserve long recovery. Let the pose linger before returning to idle, with cancel windows along the way.
- When commissioning an attack, specify the idle pose, attack pose, first active frame, and total frame count. Use photos of posed figures to communicate key poses.
- **Push poses and expressions a step further than feels sufficient.** Small or distant characters need bigger movements. CG loses some visual information, so exaggeration can restore readability.
- On the first damage frame, switch to an unmistakably pained pose. Vary reactions by hit location and severity.
- Try volume-preserving squash and stretch. For a natural turn, twist around two axes. Mirror characters facing one another when it helps show both faces.
- Give attack hitboxes a little extra reach where appropriate to reduce frustrating whiffs. Animators should know when and where hitboxes become active.

## 7. Effects and impact feedback

- Give effects clear shapes and **include dark tones so they read against bright backgrounds**. Additive blending alone can look hazy.
- Match hit effects to the strength of the impact, add contrast, spawn them where hitboxes overlap, combine elements such as sparks and shockwaves, keep characters visible, clear the effects quickly, and make them readable against light and dark backgrounds. Let hit effects continue during hitstop.
- Build explosions in stages **flash → fireball → dark smoke → dissipation**. Give them enough time to register. Add screen flash and shake to reinforce the impact.
- Give small, medium, and large impacts different shake patterns. A small shake might be vertical only. Start strong, taper off, add slight randomness, and compensate for camera distance.
- Alternate light and dark flashes to retain contrast. Soften the effect with a closer camera. Character flashes can communicate states such as invincibility in white.
- Sword slash trails make a big difference to perceived impact. Vary shape and color with the weapon’s character.
- Keep characters from disappearing behind effects. Use draw order in 2D, and try open centers or outlines in 3D. Check the perceived scale, such as whether a flaming sword’s fire reads as a candle flame.
- Limit particle count, lifetime, and overlap. Use larger sprites with more visual detail where practical.

## 8. Graphics

- **Paint the light falling on a surface.** Account for colored light, light from above, hue shifts, and atmospheric depth.
- **Emphasize collidable floors and platforms and keep non-interactive backgrounds subdued.** Make the distinction clear during play.
- Spend detail and resources where the player looks, especially near the center and directly in front of the camera. Trim detail from the foreground, distance, and areas the player cannot see.
- Materials are a powerful scale cue. Use texture repetition, moderate saturation, subtle gloss, and weathering. Top-down angles, blur at the top and bottom, and high saturation can make a scene look miniature. Use atmospheric perspective to convey grandeur.
- **Unify the art direction when characters from different worlds share a scene.** Align saturation, detail, proportions, and level of refinement. Create a concept board early as a common target.
- **Give characters recognizable silhouettes.** Stylized proportions can help. Check that characters remain identifiable when filled in black.
- Post-processing and color shape the final image. Assign someone to review the whole output. Check inexpensive monitors and TVs, grayscale, and color-vision simulations for readability.
- **Use paintovers to show visual changes.** Big adjustments often come back smaller than requested, so push further initially and dial back. If a revision fails to improve the result, keep the version that preserves quality.

## 9. UI

- **Set the balance between clarity and style based on the game’s goals and world.** UI and typography alone can change the perceived age group and setting.
- Make frequently used options larger. Color-code modes with a restrained palette and avoid competing colors on one screen. Use character art when it makes options immediately recognizable.
- Allow extra space for localization. Japanese text may need a larger font, while English and French labels may need more width. Check the layout on the actual handheld device.
- **Include control remapping.** Let players select an action and press the desired button. Support duplicate bindings, name-based profiles, confirm/cancel swaps, and a controller diagram.
- Include plain-language menu help that adds information beyond the label. “Play solo” is clearer than “Single Mode.” Let players reach the game by repeatedly confirming from the top menu even if they cannot read it.
- Show HUD information when it makes play easier or more enjoyable. Reveal contextual elements when they become relevant.
- For larger projects, support subtitle size and background, color-vision settings, camera shake controls, presets, and previews. Camera shake settings and a stable center-screen reference can help with 3D motion sickness.
- A simple “Loading” label is enough when there is no dedicated sequence. Keep transition timing independent of an animation’s duration.

## 10. Audio

- **Prioritize sound effects by their impact on the player.** In Smash Bros., the order is KO, hit, special move or voice, explosion, dodge, whiff, jump or landing, walking, then ambience.
- Give hit sounds **a strong attack and moderate reverb**. For heavy attacks, aim to finish the main part of the sound within hitstop.
- Vary footsteps and match them to surface materials. Keep ambience low in the mix and use real recordings where appropriate.
- Match exaggeration to the genre and visuals. Fighting games can use heightened sounds. Realistic sounds help communicate the material involved.
- Match music tempo to the speed of play. Smash Bros. battle tracks are often 130–170 BPM. Keep the track count manageable and reuse arrangements of the main theme.
- **Preserve the original melody in an arrangement.** It should still be recognizable when hummed.
- Compare playback on headphones, computer speakers, and an inexpensive TV.
- Give audio direction with specific language, familiar comparisons, and reference clips. Judge the result by whether it serves the game. Explain which quality to borrow from a reference, such as mood or timbre.
- Keep combat voice clips short and restrained.

## 11. Tuning and programming

- **Move tunable numbers out of the code.** Manage them in a spreadsheet if useful and support relative values when needed.
- In specifications, **put readable parameter names in 【】 and use ○ for the value**. For example, “Start movement at 【Attack startup X velocity】 of ○.” Use the same name for the actual parameter.
- **Apply changes to a running game with one action.** More tuning iterations make finer adjustments possible.
- Provide a debug mode with controls for health, pausing, a free camera, character switching, and toggling the visibility or opacity of parts. Make it usable with the normal controller. Useful debug views can become player-facing features, such as launch trajectories in training mode.
- Choose sortable filenames that put the group first and the direction or number second. In Japanese projects, avoid romanized Japanese where it makes names harder to read.
- Target testing at forced control of other actors (grabs and throws), sequences crossing scene transitions, extreme terrain, and interactions involving parameters or progression. Exhaustive testing becomes impractical.
- Seed random number generators with a variable value so a reset does not reproduce the same first result.
- Let CPU opponents use move data to choose behavior and add reaction delays. Make tougher opponents more aggressive instead of relying on flawless defense.

## 12. Teams and decisions

- **Make decisions promptly.** Work stalls while people wait for an answer. Make small course corrections whenever new information shows a decision needs updating.
- **Let the director own decisions with the full project in view.** Majority decisions tend toward safe choices. Invite staff to raise problems and suggest solutions openly.
- **Keep the concept in view when progress gets difficult.** Rebuilding from scratch costs work and morale. Resolve uncertainty about the project’s direction before moving forward.
- **Cut scope as part of directing.** When schedules slip or costs rise, remove expensive work to get back on course. Flag a likely miss early enough for the team to act.
- Raise concerns while there is time to do something. Pair criticism with a suggested improvement.
- Share a daily screenshot and three to five updates. Hold team presentations every few months. Reply to important messages the same day and reserve time for focused work.
- Budget for coordination. Sakurai’s rule of thumb puts a ten-person team’s hands-on output at roughly seven people’s. Keep testers on the same ROM build and prioritize tickets with reproduction steps.
- **Observe children and first-time players as they play.** Notice where they get stuck or lose interest.

## 13. Proposals, presentations, and marketing

- **Give each proposal page one topic, one diagram, and two lines of text.** Use as many pages as needed and show where each page fits in the outline. Keep research and charts focused. Present one plan you believe in.
- **Write the proposal in one push while the idea is fresh.** Keep it to yourself until the draft is complete to retain the momentum.
- Keep presentations brisk and dense. In a live demo, cover the highlights.
- **Development and marketing multiply each other’s impact.** A game needs to be discovered before it can reach players.
- **Show gameplay early in trailers and on store pages.** Save logos, setting, and character introductions for later. A well-known series has more license to lead with a teaser.
- **Set expectations the game fulfills.** Pick a title with a workable short form. Four characters can work well in Japanese.
- A demo can take as much work as a small release. Budget for version management, leak prevention, and testing.
- Regular updates can become a habit for the audience. Plan assets such as character reveal videos for use in both the game and marketing.
- Budget for roughly half the sales if a sequel offers essentially the same experience. Show what has materially improved.

---

## How to use this skill

1. **Review a game or propose improvements.** Use the sections above as a checklist. Pair each principle the game is missing with a concrete fix. Read the relevant file in `references/` for exact values, procedures, or examples.
2. **Write a proposal or specification.** State the core appeal in one sentence, using risk and reward or tension and release. Define rewards, onboarding, and the target audience’s tolerance for complexity. Write tunable values using 【】 and ○.
3. **Diagnose weak impact.** Check hitstop, hit effects, the sound effect’s attack, screen shake and flash, and finally the speed of the windup and exaggeration of the hit pose. Consult the specs, effects, sound, and motion references.
4. **Diagnose sluggishness.** Check the share of time under player control, transitions and fades, time to retry, the first frame of the windup, and any softness introduced by automatic interpolation.
5. **Cite the source by episode number and title.** Sakurai draws heavily on large productions and action games. Adapt the principle to the project’s genre and scale, whether it is a solo game, visual novel, or puzzle game. Use the player’s enjoyment as the deciding factor.
