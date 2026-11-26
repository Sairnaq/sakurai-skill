# Animation (windup, attack poses, follow-through, exaggeration)

Summaries based on the Japanese captions for Masahiro Sakurai on Creating Games. Episode numbers follow the repository’s oldest-first source order.

## 014 Assigning Animations [Animation]
- Start with a list of animations. Describe each action and specify its duration, the first active attack frame, and any loop behavior.
- Include reference photos of posed figures in the specifications, roughly 70–80 per character. Cite the exact frame when using the source work. Describe poses in text when a figure cannot reproduce them.
- Treat the brief as a starting point. Figures and digital models have different ranges of motion. Give animators freedom to solve the pose and review the result in several passes.
- Share animation guidelines and lessons across the team so everyone can avoid repeating the same mistakes.

## 028 Too Much is Just Right [Animation]
- Push attack animation beyond the pose that first feels acceptable. Movement is more likely to look underplayed on a small screen.
- Favor momentum in motion. An extreme pose that looks broken in a still frame can work at speed. Cleaning it up too much can make the movement weaker.
- Overshoot and settle back a little to give straight movement energy. Kirby’s Needle used this technique in the Famicom era.

## 036 Breaking Down Attack Animations [Animation]
- Build attacks as idle → windup → attack → follow-through. Establish a stable idle pose first.
- Make the windup a big change on the first frame. It acknowledges the input and gives the opponent time to react.
- Hold the contact pose during hitstop and make it count. Use the recovery time for a follow-through rather than an early return to idle.
- Add a cancel window during the recovery so players can act before the character fully returns to idle.
- In an animation brief, specify the idle pose, hit pose, first active frame, and total frames until a cancel.

## 049 Making Lead-ins Instant and Impactful [Animation]
- Change the pose as soon as the input registers. Prioritize the response even if interpolation needs to skip frames.
- Attacks with almost no windup, such as one-frame light attacks and jabs in Final Fight, can feel especially responsive.
- A charge can mask online latency and communicate a stronger attack. Give it time to do its job.

## 062 Attack Poses [Animation]
- The pose held at impact during hitstop is often the most memorable. Build the attack around it.
- Exaggerate for distance. Swing across the body’s midline, use asymmetry for most poses, and twist the torso slightly. A strike posed too far forward or back may become hard to see.
- Hold the attack a little beyond the middle of the swing. Check how the pose reads facing either side of the screen.
- Prioritize the silhouette from the actual gameplay camera, including the strict side view in side-on games.
- Practice posing figures in 3D to develop an eye for strong poses.

## 077 Follow-Throughs Make the Impact [Animation]
- The follow-through stays on screen the longest and strongly shapes how the attack feels.
- An attack often connects a quarter to a third of the way through the animation, or as early as a fifth for fast attacks. The rest is recovery. Standard attacks take under a second, and even big smash attacks rarely run longer.
- Give powerful attacks a meaningful recovery window. A large payoff with little exposure reduces the tradeoff.
- Let the follow-through show the force and direction of the attack. Hold it nearly to the end before returning to idle.
- Put the cancel window where the character visibly looks ready to act again.

## 091 Exaggerate to Make Up for Information Loss [Animation]
- A polygon model or animated character carries less visual information than a real actor. Exaggerate the performance and adjust motion capture to suit the character.
- Move small or distant characters boldly so their actions read. Account for screen size and how the input feels.

## 106 Posing Suggestions [Animation]
- Pose articulated figures to learn what reads from different angles.
- For a standing pose, break symmetry, tuck the chin, tilt the neck, and offset the torso, hips, and legs. Pick an angle that shows the flow of loose items such as a scarf.
- Try slightly raised shoulders, different arm angles, lightly bent wrists, and a small weight shift. Keep the arms from spreading too far and stagger the feet for a gentle C-shaped stance.
- Handling and posing physical figures develops a feel for what looks good.

## 120 Squashing and Scaling [Animation]
- Use scaling alongside movement and rotation. Squash and stretch can add momentum, as in a bouncing ball.
- Preserve apparent volume by widening the shape when compressing it vertically. Simple scaling can flatten the form. Use blend shapes to keep rounded edges, as you would when drawing a squashed sprite.
- Try scaling when a movement needs more character.

## 140 Damage Animations [Animation]
- Hitstop holds the first damage frame on screen. Give it a pained pose distinct from idle so the hit reads at a distance.
- Use a little interpolation from the point where the attack caught the character so the blend still reads as a damage reaction.
- Vary reactions by hit location and strength. High, middle, and low hits at three strengths give nine variations.
- Use asymmetry and a twist to keep the limbs readable in silhouette. The damage pose conveys impact to both attacker and target.
- Different body proportions make animation reuse harder and can drive up the cost of adding characters.

## 148 The Perils of Interpolation [Animation]
- Automatic interpolation can make the same key poses feel sluggish, especially when adapting sharp 2D movement to 3D.
- In an eight-frame kick, spend time on the windup and strike and trim the in-betweens. Push the key poses to make the movement read more sharply.
- Hold the windup and swing through in one frame. Give the follow-through a different path from the swing and cut frames spent near idle.
- Review the resulting animation at gameplay speed to see whether the blending dulled the impact.

## 164 Facial Animations [Animation]
- Give even small characters readable expressions. A broad expression can communicate more than fine lip sync.
- Push the face further once it seems expressive enough. Show the whites above and below widened eyes and separate the teeth.
- Exaggeration compensates for information lost in CG. Adjust to realistic or comic art direction and keep expressions true to the character.

## 179 Flipped Animation [Animation]
- Mirror poses and movement so two characters facing one another can both show their faces to the camera. Facial expressions add information.
- Mirroring means tracking changes such as a right punch becoming a left punch or a held item changing hands. Asymmetrical characters, such as sword users, are harder to mirror.
- A strict side view can hide the face and some movement. Consider letting the character run slightly diagonally so the face stays visible.
- Some designs use mirrored lettering, such as the symmetric M in MAXIMUM.

## 192 Animation Blending [Animation]
- Blend two or more animations over time using weights. When a new action begins after a cancel frame, a short blend can soften the switch.
- A blend is easier to see going from an attack to a walk than going from idle to a walk.
- Keep the blend short so it does not dull the motion.
- Blend guard motion with a centered pose to shift the guard direction. In 3D, blending can control upper and lower body separately, place feet on terrain, or tilt a weapon. Fast competitive action often needs shorter blends.

## 208 Portraying Fingers [Animation]
- Align a held object across the grip. Angle it when the forearm’s movement calls for it, and curl the fingers naturally.
- Finger rigs can be costly for such small details. Fixed poses or a few prepared hand shapes can be enough.
- Spend the processing budget where it improves what players can see.

## 223 Always Keep Attack Collision in Mind [Animation]
- Give attack hitboxes some extra reach beyond the sword or fist to avoid frustrating near misses.
- A little difference in size can work. The collision still needs to follow the visible path of the move.
- Time collision to a convincing impact pose. Players remember the pose held during hitstop.
- Animators should know the timing and range of attack hitboxes as they work.

## 234 The Limitations of Skeletons [Animation]
- FK and IK rigs help with editing and planting feet. A rigid 180-degree joint limit can make acting too literal. Consider bending beyond straight when exaggeration serves a pose.
- Treat the rig as a tool and test the limits it imposes. Additional joints increase the cost and require an animator who can use them well.

## 249 Rotation on Two Axes [Animation]
- A single-axis head turn can look mechanical. Combine two axes for a twist, such as X + Y to turn downward or Z + Y for a tilted turn.
- Move linked parts such as the shoulders and collarbones. Offset the timing and add reactions to make the turn expressive even when the final pose stays the same.
- Account for eye movement when turning the head.
