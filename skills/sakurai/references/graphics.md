# Graphics (lighting, scale, collision readability, art direction)

Summaries based on the Japanese captions for Masahiro Sakurai on Creating Games. Episode numbers follow the repository’s oldest-first source order.

## 010 Draw the Light, Not the Asset [Graphics]
- Paint the light reflecting off the material. A tree’s color is more than its brown trunk and green leaves.
- Use colored lighting and highlights on surfaces facing upward. Shift hues to add depth and use brighter, filtered colors for distant objects.
- Judge the final image as a depiction of the light in the environment.

## 030 Emphasize Objects with Collision [Graphics]
- Emphasize floors and platforms with collision. Perspective in 3D can make the actual point of contact especially hard to read.
- Keep scenery from competing with playable terrain. Atmospheric perspective can quiet the background. Stop while the scene still looks appealing and favor gameplay readability.
- Artists should know how the objects they draw function in the game.

## 044 Distinguishing Between Major and Minor Elements [Graphics]
- Concentrate limited resources near the center of the screen, in front of the camera, and on the stage. Simplify foreground and distant areas that tend to be off-screen.
- Set priorities by how much screen space something occupies. Budget moderate detail for fighters usually seen at a distance, and more detail for close-ups. LODs can reduce distant geometry and take work to produce.
- Keep playful detail within the schedule and performance budget. A distant car’s spinning tires may be too small to see.

## 063 Get the Sense of Scale Right [Graphics]
- An object can look too small even if its shape is right. Its material is a strong cue for how large it feels.
- Adjust texture tiling and pattern size, restrain saturation and specular highlights, and match normal detail to the object’s scale.
- Add weathering to large objects. Slight hue changes can break up even a monochrome surface.
- Tune materials first. Judge the scene as a whole.

## 090 Supervising Art Through Retouches [Graphics]
- A five- to ten-minute paintover can communicate a revision more reliably than verbal directions alone.
- For a cave, duplicate the layer, increase contrast, shift the hue, and erase the lit portions on the new layer so purple remains on the reflective side. Adjust the overall color to add depth to a monochrome scene.
- Soften distracting areas such as magma by adjusting their brightness and coverage. The lead can use the paintover to communicate direction, and the artist can refine it for the final work.

## 114 The Basics of Pixel Art [Graphics]
- A 15-pixel circle in a 16 × 16 sprite has a center column. Odd widths can help when crafting with a coarse grid.
- With black and white alone, patterns and dithering can suggest different materials. A few highlights on a dark shape can suggest polished metal.
- If you have a third color, use a midtone for shading. A reflective surface can pick up the floor below it. Lighten the edges when they need to stand out from the background.

## 129 Unifying Visual Style [Graphics]
- Have experienced artists make reference boards for the world, characters, objects, and lighting so a team can work toward a consistent style.
- Realistic and cartoon characters need a shared visual treatment. More capable hardware can make matching detailed styles more costly.

## 136 A Fight Between Live Action and Animation [Graphics]
- When characters from different worlds appear together, align the art so they look at home on one screen.
- Use restrained saturation so lighting can shape the color. Add detail to cartoon textures and simplify realistic ones as needed. Adjust proportions, modernize designs when useful, and make facial details such as closed eyelids and the fit of the teeth feel believable.
- Use the same art direction across the cast to reduce visual clashes.

## 150 Do Graphics Impact Fun? [Graphics]
- The importance of scenery depends on what players do. In a game such as Dark Souls, where players advance cautiously, details in the environment can affect the play.
- Store banners and thumbnails can help players notice the game in the first place.
- Design visuals and mechanics to reinforce each other.

## 163 Odds and Ends of Supervising [Graphics]
- For remote reviews, add paintovers, diagrams, and arrows to written instructions.
- Check light and dark, how well the work evokes the source, draw order, visibility of objects, camera position in plan view, the direction of wind and windmills, and background shake.
- Check when an attack’s visuals and collision begin and end. Correct hits with missing effects and hitboxes that remain after the visible effect ends.
- Compare with the source to capture its atmosphere. Use weight shifts and silhouettes to give characters personality, and show strength through the eyes and mouth.

## 172 Making Things Look Miniature [Graphics]
- High angles, blur above and below the subject, and high saturation make scenes look miniature. Reverse those choices if the goal is grandeur.
- Use blur deliberately and keep the viewer’s point of attention readable.
- Use atmospheric perspective on large forms. Distance can reduce saturation and shift colors toward blue. Check the final output as a viewer would see it.

## 182 Dealing With Color Disparity [Graphics]
- Monitors and room lighting can make the same image look different. Give the team a shared reference display for comparing the art.
- Measurements can help calibrate a monitor. Check that shadows and contrast survive on inexpensive TVs and monitors too.
- Use neutral workroom lighting so it does not shift the apparent color of the artwork.

## 190 Motion Blur [Graphics]
- Motion blur suggests a moving object’s path, softens the steps between frames, and adds energy. It can also affect backgrounds as the camera moves.
- Use authored blur, such as a blurred texture for a spinning wheel, or calculate it in hardware.
- Keep the image readable during motion. Adjustable blur strength can accommodate different preferences.

## 203 Making the Imaginary Feel Real [Graphics]
- Game worlds have no physical mass. Art, sound, logic, and tuning make their objects feel present.
- Even a small prop needs believable perspective, volume, placement, and signs of use. Check the impression of the whole scene.
- Air movement is easy to overlook. Let objects sway in the wind or react to the air displaced by an explosion.

## 213 Final Output [Graphics]
- The framebuffer feeds post-processing. Color, reflections, and the overall treatment shape the final image.
- Give someone ownership of the final image so they can adjust effects and color across the whole screen.

## 222 All to Destroy One Wall [Graphics]
- Use paintovers to give outside artists clear direction. A damaged wall may need jagged cross-sections, irregular edges, or broken repetition.
- Check whether repeated serrations or identical columns make the damage look artificial. Inspect it from a distance and from behind.
- Accept work that meets the quality bar even if it differs from the paintover. After repeated revisions stop improving it, decide whether the current version is ready to ship.
- A revision may move only halfway toward the intended result. Ask for a larger adjustment first and dial it back if needed.

## 230 Manga-like Visuals [Graphics]
- Manga-style distortions can read well in games, such as a profile mouth drawn outside the face or eyes showing through the glasses frame.
- Choose the shape that reads best on screen. Kirby’s mouth is an example where appearance can matter more than a literal cross-section.
- Some transitions, such as moving a character from a tight space into an open one, take extra work. Look for an exaggerated treatment that fits.

## 241 Establishing Characters Through Their Design [Graphics]
- Give characters distinctive silhouettes. Check a black fill of the design and try poses that show each character at their best.
- Push forms such as the head, limbs, hair, ribbons, gloves, and feet. Revise existing models where needed to strengthen their identity.
- Everyone contributing to the character should understand its background and reinforce its distinguishing traits.

## 251 Odds and Ends of Supervising: Sora Edition [Graphics]
- Communicate reviews with corrected images, drawings, and diagrams. Judge silhouette, motion, and pose from the game’s actual camera angle.
- Check ground, air, up, and down variants of special moves. Fix rotation axes that make the motion look unnatural.
- Include dark tones so effects read on bright stages. Use stronger contrast in the foreground and less in the distance. Keep characters readable against both effects and scenery.
- Flag stray details or artifacts when you see them. Small corrections add up.
