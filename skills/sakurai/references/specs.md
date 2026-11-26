# Design specifics (hitstop, jumping, cameras, ledges, transitions, randomness)

Summaries based on the Japanese captions for Masahiro Sakurai on Creating Games. Episode numbers follow the repository’s oldest-first source order.

## 003 Stop for Big Moments! [Design Specifics]
- Briefly freeze the action when an attack connects. Hitstop makes a dramatic difference to impact feedback across genres.
- Use a brief freeze and flash when the player defeats a boss or loses their ship. Holding the moment gives the player time to register what happened.
- In shooters, it can be hard to tell when or how you were hit. A brief stop clarifies the hit and is relatively easy to implement.

## 019 Giving "Weight" to Buttons [Design Specifics]
- The same button can feel lighter or heavier depending on movement speed, inertia, jump physics, and frame rate. This is one of the expressive tools available to game developers.
- Design around the sensation between input and on-screen response. Smash Bros. gives each character a distinct sense of weight, including how far they swing to attack.
- Analog sticks vary across controllers. Calibrate the dead zone and other thresholds for the hardware.

## 037 Jump Physics [Design Specifics]
- Give the jump an initial velocity and apply constant downward acceleration each frame. Keep lateral velocity constant or let it gradually fall off.
- Tune to match the game. Mario rises slowly, falls quickly, and gets more height from holding the button. Metroid’s floaty jump helps with vertical aiming. Ghosts ’n Goblins commits the player to a low jump with a fixed landing point.
- A faster descent can make a landing feel stronger. Timing can change the feel even when the path is the same.
- Try exaggerating upward and downward motion for the first few frames, then easing abruptly before returning to the usual rate. This gives some room for a late reaction, at the cost of more parameters.

## 047 Eight Hit Stop Techniques [Design Specifics]
- Freezing alone provides hitstop. Add a slight shake to strengthen the impact.
- Shake the target more and the attacker less. Shift the visuals while leaving collision detection in place so hits still count.
- Use horizontal shake on the ground and add a vertical component in the air. Avoid pushing grounded feet below the floor. Begin at a larger amplitude and taper toward zero.
- Scale the hitstop by attack power and multiply by a move-specific coefficient. This can distinguish a strong tip hit from a weaker hit near the base and give characters different weights.
- Blend the recipient into the damage pose over roughly four frames. Let the attacker keep moving a tiny amount when that makes the swing feel better. Make the choice per move.
- Increase visual shake amplitude when the camera is farther away so the hit still reads.

## 061 Don't Anchor Your Center Point [Design Specifics]
- Setting the 3D camera target directly to the character’s position makes jump height hard to judge.
- Reduce or remove vertical tracking. In Super Mario 64, Mario can jump away from the center of the screen.
- Offsets can help the action read. Armored Core offsets the mech in the direction of input so shots are easier to see. In Kirby Air Ride, drifting moves the machine off center, adding a sense of control and the thrill of brushing a wall.
- Tune the camera for the kind of action. For example, show more of the area in the direction of travel.

## 073 Say No to Slow! [Design Specifics]
- Slowness includes travel, waiting for actions, and stretches with nothing to do.
- Measure how much time actually gives the player control and trim gaps where possible.
- Some loading time is unavoidable. Remove artificial waits and use cutscenes or events as intentional breaks.
- Err slightly on the side of tighter pacing.

## 084 Units of Speed [Design Specifics]
- Speed is distance divided by time. Agree on distance and time units so specifications can give concrete velocities.
- Older 2D systems express speed in pixels per frame. Different resolutions make the same value feel different. In 3D, units such as km/h or m/s can make speeds easier to picture.
- Some games specify the movement per frame directly. Speedometers can read surprisingly low at character scale. Kirby was treated as roughly 20 cm tall in Kirby Air Ride.
- Learn to translate how far something should move into a parameter value.

## 102 Behavior at Ledges [Design Specifics]
- Decide which actions can carry a character off a ledge.
- Keep small involuntary movements, such as a step into an attack, from causing falls where appropriate. A dodge might stop at the edge while a committed charge can go over.
- Watch how speed carries through at takeoff. A risky move might stop only near the end when it reaches a ledge. Expose velocity as a parameter.
- In 3D, require a deliberate push toward the drop or use a correction to catch a shallow misstep. Test whether the result feels natural.

## 118 Maps Are Game Screens, Too [Design Specifics]
- A corner minimap can pull attention away from the scenery. Repeated trips to a full-screen map can also interrupt play.
- Try a translucent map overlay, as in Mystery Dungeon. Give the main screen readable clues, such as turn-depth guides in racing or landmarks near corners and points of interest.
- Design around where the player is looking while playing.

## 139 Unexpected Results [Design Specifics]
- Late optimization can change difficulty when game behavior depends on processing speed. Meteos became harder than intended.
- Development boards and retail hardware can run at different speeds. In Mushiking, the hunger mechanic ended up progressing too quickly.
- CPU opponents can also feel stronger than expected for unclear reasons. Retuning difficulty requires extensive retesting. Online updates and changes to specific modes helped address this.
- Check difficulty and pacing on target hardware after optimization and hardware transitions.

## 152 Flick Input [Design Specifics]
- An analog stick can report the rate at which it tilts as well as its direction and magnitude. A quick flick for a dash or dodge can feel more immediate than a double tap.
- Flicks can trigger accidentally. Make the speed threshold tunable.
- Consider new hardware features when they serve the game. Smash Bros. Brawl left some Nunchuk and pointer features unused. A standard device can still support distinctive controls.

## 171 Teaching Players How to Play [Design Specifics]
- Long instructions or practice in an empty room can make players impatient. A common approach is to introduce text and practice opportunities along the first stage.
- Teach through active play. The original Smash Bros. used Break the Targets to build proficiency. A mode for learning techniques hands-on was dropped due to the schedule.
- Plan for teaching complex controls early.

## 187 Randomness Spices Games Up [Design Specifics]
- Randomness changes how a run unfolds. Varying outcomes can reward players for adapting to new situations.
- Luck can undo hard work and make a loss feel arbitrary. Players need enough information and control to understand why they lost.
- An RPG’s explicit luck stat can make chance understandable, although players may overlook a low-priority stat.
- Use randomness carefully in skill-based matches. Random choices can work when players still decide how to use them. In party games, random items can keep comebacks possible.
- Pseudorandom generators can repeat their opening values after a reset. Use a varying seed such as the clock.

## 200 Handicap Systems [Design Specifics]
- Close matches tend to be more fun. In casual play, consider catch-up boosts or stronger items for trailing players, as in Mario Kart.
- If skill should determine the result, use gentle assistance such as making the Smash Ball harder for the leader to get or filling the losing side’s Final Smash meter faster. Terrain and items can add variation.
- In couch play, players can agree to ban oppressive tactics or handicap themselves by taking hits or letting others grab items. That works less well online.
- Tell players when an auto-handicap option is available.

## 216 Average and Mediocre Are the Same Thing [Design Specifics]
- Numerical balance can flatten performance and erase personality. Push a weakness along with a strength to keep a distinct identity.
- Different options create a wider range of decisions when they compete.
- Distinct strengths will divide opinion. Check actual match data to get past amplified online opinions about what is strong or weak.
- Super Smash Bros. Ultimate’s 87 fighters had online win rates of roughly 47.1–51.4%, even with distinct playstyles.

## 229 Online Updates [Design Specifics]
- Modern games are complex and teams get limited time on a finished build. The public can uncover rare bugs across far more play sessions than internal testers, so plan for post-release updates.
- Fix critical bugs. Balance changes are ongoing support and cost development time.
- Ship as close to the best state you can. An early bad experience can drive players away for good.

## 244 Speedy Screen Transitions [Design Specifics]
- Keep fades, black screens, and waits for control brief. Use enough of a transition to orient the player.
- A black screen can cover loading. Resident Evil’s door animations also turned the wait into a moment of horror. Choose a transition that suits the game.
- Simple fades are often enough. A faster wipe can carry its own meaning, such as an iris that suggests looking through a keyhole.

## 253 What Happens When You Shift the Center of Gravity? [Design Specifics]
- For a sense of momentum and presence, offset a mechanical movement path or rotation slightly.
- Move a projectile sprite through a six-frame loop of horizontal and vertical offsets for an impression of blur. Give a bomb an off-center spin, or shift a sword move’s pivot away from the grip.
- Animators may do this instinctively. Movement implemented straight from a technical specification can benefit from a final pass for personality.
