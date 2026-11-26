# Effects (hit effects, explosions, screen shake, flashes)

Summaries based on the Japanese captions for Masahiro Sakurai on Creating Games. Episode numbers follow the repository’s oldest-first source order.

## 016 Make It "Pop" [Effects]
- Additive blending makes effects glow. Heavy use can wash out detail and leave effects that read only against dark backgrounds.
- Build most of the effect from clearly drawn shapes, such as polygons and opaque art. Add glow where needed and include dark colors so the effect shows up against bright backgrounds.
- Use curved and straight lines or light and dark tones together to establish contrast.

## 035 Let Your Characters Shine [Effects]
- Keep characters readable through big effects. In 2D, you can draw the character on top.
- Forcing the draw order in 3D can break perspective. Try an opening in the center of the effect or vary the height of the front and back portions to leave the character visible.
- Outlines can also help the character stand out.

## 056 Flash, Blast, and Smoke [Effects]
- Stage an explosion as flash → fireball → black smoke → dissipation. Give each phase time to read.
- The first flash signals a violent event. Mix in black so the flash is visible on bright backgrounds.
- Expand the fireball forcefully from the center. Let smoke take over as the fire fades, with embers lingering at the end.
- Clear the effect promptly while giving the player enough time to feel the impact.
- A screen flash and shake add impact. Ground and aerial explosions can use different treatments, as can sustained explosions.

## 079 Visual Effects in Slow Motion [Effects]
- Effects show a lot of information in an instant. Study them in slow motion or with the background removed. This also helps when studying animation.
- Turning off effects shows how much they contribute to the feel of an action. Use them to bring the game to life.

## 103 Screen Shake [Effects]
- A brief screen shake communicates a strong impact. Keep play readable during the shake.
- You can move the camera or offset the finished frame. With camera movement, distant scenery may barely move, so consider adjusting the target. Moving the finished frame can shake the UI and expose black edges.
- Give small, medium, and large shakes distinct patterns. A small shake might be vertical only, with a sideways component added for medium. Sustained shakes and ground tremors are chiefly vertical.
- Adjust amplitude for camera distance and field of view. Start strong, taper the shake, and vary it slightly.
- Even a small shake can strongly improve feedback.

## 130 Hit Marks [Effects]
- Scale the hit effect to the impact. Use strong contrast, place it where the collision volumes overlap, and layer components such as shockwaves, splashes, and sparks. Keep the character visible and clear the effect quickly, especially on repeated hits. Include dark color or black so the effect reads on both light and dark backgrounds.
- Keep the hit effect animating during hitstop. That pause can also communicate game-specific information, such as how input changes the launch direction.

## 151 Billboards [Effects]
- A billboard is a flat polygon that faces the camera. It is inexpensive to draw and works well for smoke, fire, explosions, and many other particles.
- From some camera angles, a billboard’s flatness can become obvious. A billboard constrained to turn around only the Y axis can appear edge-on.

## 177 Blade Trails [Effects]
- Build a translucent fan-shaped polygon along the blade’s path and fade it out. Another option is to show a flat polygon for an instant during a one-frame swing, with hitstop holding it long enough to read.
- A fast swing can produce a trail that barely registers, especially when seen edge-on. Adjust the pose or swing path to show the trail from the gameplay camera.
- Match the trail to the weapon. Emphasize the tip of a tip-heavy attack, use a rougher trail for a heavy blade, and use glow or a fire afterimage for an energy blade or burning sword.
- A readable blade trail makes a large difference to impact feedback.

## 199 Making Effects the Right Size [Effects]
- Effects need believable scale just like characters and stages. A flaming sword can look as though it is carrying a candle flame without a good size reference.
- Use a reference image to show the intended size of the flame.
- Moving effects can be rough and fast without showing fine detail. Try adding animation loops or using particle billboards.

## 221 Flashing Effects [Effects]
- A full-screen flash strengthens impact. Flashes on a character can communicate a state change such as invincibility or damage.
- An even additive flash lowers contrast and can disappear against bright backgrounds. Alternate light and dark tones.
- A close camera makes flashing cover more of the screen. Reduce the intensity at closer distances.
- Use colors to distinguish states. For example, use white for invincibility and yellow for a vulnerable state after a throw. A brief rim light can emphasize the edges instead of filling the character.

## 242 The Limitations of Particle Effects [Effects]
- Control rendering cost by shortening particle lifetimes and limiting simultaneous emissions. Vary timing and position to reduce wasted overlap.
- Use larger, more detailed billboards when the budget cannot support many tiny particles.
- For Kirby’s defeat effect, the designer placed stars by hand for each frame. Coordinate data can be bulky, but the effect is easy to work with. Inhaling uses both dark and light dots so they read against any background.
