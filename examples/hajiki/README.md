# Example game — Hajiki (Godot 4.6)

<img src="hajiki_icon.gif" width="200" align="right">

Claude Code used this repository’s `sakurai` skill to design, implement, and polish a single-screen action prototype, including its title screen and icon.

- **Play** on [unityroom](https://unityroom.com/games/hajiki) in your browser.
- **Engine** is Godot 4.6.3, with about 2,000 lines of GDScript. The game draws its shapes and generates its sound effects in code.
- **Process** consisted of a person directing what to make and giving playtest feedback. The table entries below record which episode informed each design decision.

> Episode numbers follow this repository’s oldest-first source order (001–259). See the [reference directory](../../skills/sakurai/references/) for the summaries. This fan project has no affiliation with Masahiro Sakurai or Sora Ltd.

## How it plays

**The closer a projectile gets before you deflect it, the harder it hits on the way back.** Deflect early for safety or wait until just before impact for a stronger counterattack.

| Title screen | Gameplay | Results |
|---|---|---|
| ![Title screen](title.png) | ![Gameplay](play.png) | ![Results](result.png) |

- Deflections have three timing grades. Last Second deals 3 damage, Nice deals 2, and Safe deals 1.
- Deflections fill the Hajiki gauge. At full charge, trigger a burst to send back every projectile on screen.
- Six waves make up one loop. The last wave is a boss, with a bonus wave earlier in the loop. The results screen awards a rank. Walls that block projectiles and new enemy types appear from the second loop onward.
- Clearing waves without taking damage raises Intensity. Completing any of 20 challenges counts toward unlocking racket colors.

| Boss | Bonus wave | Walls (loop 2 onward) | Challenge list |
|---|---|---|---|
| ![Boss](boss.png) | ![Bonus wave](bonus.png) | ![Walls](wall.png) | ![Challenge list](challenges.png) |

## How the skill guided development

1. **Concept.** The proposal workflow in [SKILL.md](../../skills/sakurai/SKILL.md) helped reduce the concept to one line. The closer the projectile, the stronger the deflection. See #006 Risk and Reward.
2. **Implementation.** Sections 5 (game feel), 6 (animation), 7 (effects), and 10 (audio) served as a checklist.
3. **Polish.** A second agent reviewed the game using the same skill. It reported 13 findings with supporting episode numbers. The game incorporated 11 of those suggestions and two new enemy types.
4. **Tuning.** A playtester found that the burst made enemies too easy to kill. The notes below explain the adjustment and the references it drew on.
5. **Title and icon.** The title screen and its icon drew on the onboarding, UI, and marketing principles.
6. **Level design and replayability.** The creator asked for a level design pass based on the series and more reasons to keep playing. The agent consulted the relevant episodes, diagnosed problems, and revised the wave progression and challenges.

## Where the game uses the skill

Code identifiers use the names found in the prototype, including the Japanese keys in `params.json`.

### Core concept

| Principle | Episode | Implementation |
|---|---|---|
| Keep risk and reward close and proportional | #006 Risk and Reward | `_grade_of` grades a deflection by the frames left before impact. `【ギリギリの残りフレーム】` (Last Second threshold) is 5 and `【ナイスの残りフレーム】` (Nice threshold) is 11. |
| Give whiffs a cost | #006 / #191 Game Essence in Action Games | A whiff leaves the player unable to deflect for 20 frames, set by `【空振り後隙フレーム】` (whiff recovery). |
| Build tension, then release it | #009 Squeeze and Release | Fill the gauge and spend it on a burst (`_burst`). |
| Make each enemy describable in one line. Avoid averaging out its traits. | #204 Using Parameters to Establish Characters / #216 Average and Mediocre Are the Same Thing | Five types are Normal (straight shot), Scatter (three directions), Heavy (large and slow, pierces on a Last Second return), Accelerator (speeds up when close), and Double Shot (delayed second projectile). |
| Break down what makes the mechanic fun and rebuild it | #057 Deconstruct, Analyze, and Rebuild | Deflection is built around the risk and payoff of waiting until near impact. |

### Onboarding and pace

| Principle | Episode | Implementation |
|---|---|---|
| Show the appeal in the first three minutes and lead with a highlight | #017 Just Let Them Play! / #233 Start with the Climax | The title screen is playable. Deflect an incoming projectile into the START sign to break it and begin (`_update_title`). |
| Teach controls through play | #171 Teaching Players How to Play / #085 Making Tutorials Feel Natural | The game shows one tip at a time at the bottom and advances after the player performs the action. Players who deflect on the title screen skip the first tip. |
| Respond to every button press | #104 Don't Be Unresponsive | Pressing during recovery plays a muted visual cue and sound. The game buffers input during hitstop for up to six frames (`【先行入力フレーム】`). Any button can confirm. |
| Make the game usable without reading the language | #238 Making Things Clear, Even Without Words | Enter or Start begins immediately. Control prompts show key icons. |
| Keep transitions quick | #073 Say No to Slow! / #244 Speedy Screen Transitions | The main game starts about half a second after the sign breaks. |
| Make retries quick | #116 Make Retries Quick | After a defeat, one button immediately restarts the current wave. |

### Impact feedback

| Principle | Episode | Implementation |
|---|---|---|
| Use hitstop, shake the target more than the attacker, and freeze briefly on defeat | #003 Stop for Big Moments! / #047 Eight Hit Stop Techniques | Deflections pause for 4/7/12 frames by grade. Enemy kills pause for 9, bursts for 20, and player defeats for 30. During the pause, the projectile shakes ±3 px and the player ±1 px. |
| Make the windup immediate and exaggerated. Shape the impact pose and follow-through. | #049 Making Lead-ins Instant and Impactful / #062 Attack Poses / #077 Follow-Throughs Make the Impact | The player squashes into the windup at the first frame of input. The swing ends in an exaggerated pose held briefly before returning to idle (`_draw_player`). |
| Push the poses and use squash and stretch | #028 Too Much is Just Right / #120 Squashing and Scaling | The body squashes or stretches on jumps, landings, and deflections. |
| Make hit effects readable | #130 Hit Marks / #035 Let Your Characters Shine | A black-outlined star appears offset in the projectile’s direction and clears in eight frames. The player is drawn in front of it. |
| Stage explosions as flash, fireball, and dark smoke | #056 Flash, Blast, and Smoke | Enemy defeat effects use three stages (`_draw_explosion`). |
| Use distinct patterns for small, medium, and large screen shake | #103 Screen Shake | Small shakes are vertical, medium shakes are mostly vertical, and large shakes are mostly horizontal, reversing every two frames. |
| Alternate bright and dark tones in flashes | #221 Flashing Effects | Flashes alternate white with a dark tone. |
| Mix by importance. Give hits a strong attack and moderate reverb. | #032 Strike a Balance with Sound Effects / #165 Strong Attack, Light Reverb | The loudest sounds are kills, then Last Second deflections, taking damage, Nice deflections, and so on. Last Second sounds start with a sharp crack (`crack` in `_tone`). |
| Telegraph enemy attacks | #036 Breaking Down Attack Animations | Before firing, enemies swell for 22 frames and play a quiet cue. |

### Readability and UI

| Principle | Episode | Implementation |
|---|---|---|
| Emphasize objects with collision | #030 Emphasize Objects with Collision | Bright floor edges stand out against a low-contrast background. Projectiles have a black outline and a white center. |
| Design in frames and make them measurable | #076 Learn to Count Frames! | Projectile outlines indicate when to deflect (white for Last Second, gold for Nice). A faint line shows the Last Second boundary before the player presses. F1 shows the frames remaining for each projectile. |
| Change the HUD as the meter changes state | #252 HUDs | A full gauge triggers a sound, a ring, and a “Burst ready!” message. The player’s outline glows gold while the gauge stays full. |
| Make sequences skippable and pausable | #178 Let Them Skip, Let Them Pause | Players can skip the clear and results screens. The pause menu lists controls. |

### Rewards and motivation

| Principle | Episode | Implementation |
|---|---|---|
| Consider rewards early and make play move something forward | #075 Consider Rewards First / #149 Planning Your Game’s Rewards | Six waves complete a loop. The results screen awards S–C ranks based on Last Second rate and whether the player used a continue. New enemies appear in loop 2. |
| Keep the next goal visible | #023 Keeping Rewards in Sight | Streaks carry between waves and the counter bounces at 10 and 20. The title screen shows the player’s best score. |
| Praise the player | #095 Praise the Player! | Messages include “Last Second!”, “One Hit!”, and “Multi-hit ×N!” Applause plays at the end of a wave. |
| Tie the reward to what the player accomplished | #236 How Good Were the Player’s Actions? | Each kill scores according to the best deflection grade that hit that enemy. The game shows the reason, such as “Last Second ×3.” |
| Vary the challenge instead of steadily turning it up | #105 Mountain Climbing Is More Than Just Climbing / #127 Is Your Game Appealing Enough to Start Over? | A single Heavy enemy provides a breather. Loop 2 adds enemies that change when players need to deflect. |
| Think about how the score is presented | #198 Presenting Scores | BEST records separate scores for runs with and without continues. |

### Tuning the burst after playtesting

A playtester reported that the burst made enemies too easy to kill. Four ideas from the series guided the adjustment.

- **#009 Squeeze and Release**. Preserve the satisfying release. A burst still deals two damage to each enemy.
- **#236 How Good Were the Player’s Actions?**. Keep the burst powerful and make the player earn it.
- **#006 Risk and Reward**. Change the gauge gains from 10/20/34 to **4/10/25** for Safe, Nice, and Last Second. The largest gain now requires the riskiest timing.
- **#009 and player choice**. Burst kills count as Safe for scoring. Players can spend the gauge to stay safe or save it and try to score higher with a deflection.

### Tuning and development tools

| Principle | Episode | Implementation |
|---|---|---|
| Keep tunable values outside the program and give them bracketed names | #046 Making Your Game Easy to Tune / #068 Put Parameters in Brackets | `params.json` uses Japanese names such as `【ギリギリの残りフレーム】` (Last Second threshold). F5 reloads it live. |
| Provide a debug mode | #193 Debug Mode | F1 shows timing and collision information, F2 slows time, F3 enables invincibility, and F6 advances the wave. Autoplay and screenshot tools let the agent inspect the game during development. |

### Title and icon

| Principle | Episode | Implementation |
|---|---|---|
| Set accurate expectations and use a short title | #101 Paint an Accurate Picture of Your Game | The title is “Hajiki.” Its tagline describes the action directly. “Wait until the last second and deflect the shots!” |
| Show gameplay and use the thumbnail to attract interest | #184 Show the Actual Game! / #150 Do Graphics Impact Fun? | The looping GIF holds on a Last Second deflection. |
| Keep the character readable by silhouette | #241 Establishing Characters Through Their Design | The icon enlarges the character and gives it a thick black outline. |

### Level design and replayability pass

**Problems with the first wave layout**

- Enemy counts simply went 1 → 2 → 2 → 1 → 3 → 3. No wave challenged players to rethink their approach or gave them a place to build up their score. See #105 Mountain Climbing Is More Than Just Climbing.
- Enemies stood in a line and fired. Their placement afforded few tactical options. See #204 Using Parameters to Establish Characters.
- Higher difficulty only sped up shots. Stuck players had no way to ease the challenge. See #211 Better Than Not Being Able to Beat the Game.

**Revised wave layout**

| Loop | W1 | W2 | W3 | W4 | W5 | W6 |
|---|---|---|---|---|---|---|
| 1 | Normal | Normal ×2 | Scatter + Normal | Heavy | **Bonus** | **Boss** |
| 2 onward | **Wall** + Accelerator | Double Shot + Normal | Heavy + Wall + Scatter | **Bonus** | Double Shot + Accelerator + Scatter | **Boss + Wall ×2** |

| Principle | Episode | Implementation |
|---|---|---|
| Alternate challenges and breathers. Make bosses prompt new strategies and reward the effort. | #105 Mountain Climbing Is More Than Just Climbing | Each loop ends with an 18 HP boss that cycles three-shot bursts, five-way spreads, and large projectiles (`_boss_fire`). A Last Second return on a large shot deals 6 damage. The kill bonus is 2,000 × Intensity. |
| Allow more than one strategy | #217 Mandatory Strategies and Strategic Balance | Each firing pattern calls for a different response. For a five-way spread, players can get close and return the shots together or back off and wait it out. |
| Give players a place to rack up points | #105 | A bonus wave before the boss offers many easy targets. Last Second kills award double points (`【ボーナスウェーブのギリギリ点倍率】`). |
| Placement gives even stationary enemies strategic depth. Cover trades offense for safety. | #204 / #191 Game Essence in Action Games | Walls stop incoming and returned shots (`_wall_at`). Players can recover behind cover or go around it to return fire. A Last Second return on a Heavy shot pierces walls. |
| Introduce new elements in isolation | #085 Making Tutorials Feel Natural | Only one or two Heavy shots, Accelerators, or walls appear the first time. A brief tip appears as they are introduced (`_wave_banner`). |
| Let Intensity rise with good play and drop automatically upon failure | #041 The Fiend's Cauldron | Clearing a wave without damage raises Intensity by 0.5. Taking a hit drops it by 1.0. Higher Intensity speeds up shots and multiplies score (`【本気度】` in the parameters). |
| Keep a path to completion open | #211 Better Than Not Being Able to Beat the Game | Repeated hits automatically drop Intensity below 1 and slow the projectiles. |
| Use achievements to give players goals in moderation | #149 Planning Your Game’s Rewards / #059 Kirby Air Ride (Checklist) | There are 20 challenges. Press ↓ on the title screen to open the list (`CHALLENGES`). |
| Give players goals for using particular actions | #191 | “Airborne Last Second” uses jumping, “Shield User” uses wall cover, and “Skewer” uses a Heavy shot’s piercing. |
| Make room for clever shortcuts and different playstyles | #048 Let Players Cheat the System | “Sealed” rewards a loop cleared without a burst. “Blow Them All Away” rewards taking out three enemies with one burst. |
| Reward players with unlocks, including cosmetic ones | #149 / #180 Customization Lets Your Imagination Play | Completing 3, 6, 10, 15, and 20 challenges unlocks racket colors with identical stats. |
| Celebrate achievements | #095 Praise the Player! | Challenge completion plays a sound and shows “Challenge complete!” Another message announces a new racket color. |

## Features the prototype still lacks

- Control remapping (#195 Button Settings)
- Background music (#025 Make the Tempo Match the Game)
- Finished visuals beyond placeholder shapes
