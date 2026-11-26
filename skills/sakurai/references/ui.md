# UI (menus, text, HUDs, control remapping, skipping)

Summaries based on the Japanese captions for Masahiro Sakurai on Creating Games. Episode numbers follow the repository’s oldest-first source order.

## 018 Clarity vs. Style [UI]
- A UI organizes whatever the game needs to present. Choose a balance of clarity and style that fits the quantity and kind of information.
- Guide the eye with sizing, grouped windows, contrast, and typography. Match the presentation to the game’s world and the player’s needs.

## 033 Text Size [UI]
- Dense Japanese characters often need larger text. English can be smaller but may occupy more horizontal space, and French can run longer still.
- Give localized text room to grow and consider a type-size option.
- Test on actual handheld hardware. Readability may require larger text even if you prefer the look of smaller type.

## 055 Modern Quality of Life Features [UI]
- For a large project, plan substantial accessibility options. The Last of Us Part I is an example for color-vision settings, high contrast, HUD size, and motion sickness options.
- Let players preview changes and apply related settings with presets.
- Reduce camera shake and offer a fixed center-screen reference for motion sickness. Direction arrows and audio cues can communicate information outside the player’s view.
- Consider an extra confirmation for settings that directly affect difficulty.
- Let players name mappings, restore the defaults, hold to avoid accidental changes, and support sideways controllers and swapped sticks as appropriate.
- Offer subtitle size and background settings, speaker colors, and voice direction cues. Other useful choices include quality or performance modes, a brightness comparison, and disabling controller vibration in cutscenes.
- A broad audience needs room to adapt the controls to individual preferences.

## 078 Loading Screens [UI]
- A loading transition can serve the game, as with the doors in Resident Evil.
- A simple “Loading” label is enough if there is no purpose-built effect.
- Optimization can change load durations. Keep the indication independent of the length of an animation so it can work wherever needed.
- With time to invest, use the loading screen to convey something about the setting.

## 093 Emphasizing Text [UI]
- Use size, color, animation, fonts, and screen shake to convey emotion and variety in text-heavy games.
- Let translators adjust effects in the script data. Emphasis lands differently across languages.
- Manga offers examples such as hand lettering, sweat marks, and stress lines. Use typographic and visual expression where it helps the text.

## 111 Menus Define Your World [UI]
- Menus and typography can make the same game feel mature, cute, scary, Japanese, or futuristic.
- Design fonts, colors, decoration, backgrounds, and icons together. Convey the setting while keeping the interface legible.

## 132 Color-Coding Your Game [UI]
- Color-code modes to orient players. In Super Smash Bros. Ultimate, Smash is red and Spirits is green. Choose colors that suit the game’s tone.
- Use a restrained palette within each screen to avoid a cluttered look.
- A large character image can be faster to recognize and easier to remember than a text label.

## 145 Make Important Elements Bigger [UI]
- Make icon size reflect importance or frequency of use. The GameCube controller’s large A button follows the same principle.
- Use equal sizing where all options carry equal weight.
- Allow for long labels in other languages when sizing icons.

## 167 I Want to Choose Fast! [UI]
- Consider a wheel or jog dial for quick menu navigation, with satisfying physical clicks.
- Moving an analog stick to navigate menus can feel imprecise. New hardware is a chance to reconsider familiar controls.
- Expert-only shortcuts can make fast selection harder for the broader audience.

## 178 Let Them Skip, Let Them Pause [UI]
- Let players skip logos, openings, and events, including when revisiting a sequence. If platform rules require an opening display, keep the remainder skippable. Allowing players to move through cutscenes one line at a time can help.
- Let players pause cutscenes for interruptions such as a call or a visitor.

## 195 Button Settings [UI]
- Include control remapping even in simple games. Players may depend on it.
- A controller diagram makes the mapping easier to understand than a list alone, though it takes work to build.
- Use a cursor to select an action, then listen for the new button. This avoids conflicts with inputs such as the button used to leave the screen.
- Let more than one button trigger the same action.
- Save mappings under a named profile so guests can restore theirs quickly. Store them on the controller if the hardware allows it.
- Confirm and cancel conventions vary by platform. Offer an in-game swap because system-wide remapping affects all apps.

## 209 Advancing Text [UI]
- Players can often read subtitles faster than the dialogue plays. Let them advance one line at a time.
- Video viewers commonly use double-speed playback. Check whether dialogue delivery feels slow, and accommodate players who prefer both faster and slower pacing.

## 227 Adding Help Text to Menus [UI]
- Add brief help text near menu items, for example at the bottom of the screen.
- Explain what the option does in words the player can already understand.
- Avoid specialist words such as “config” and favor simple writing, including hiragana where it helps in Japanese. “Play solo” is clearer than “Single Mode.”

## 238 Making Things Clear, Even Without Words [UI]
- Use images and characters in icons so players can use the game even when they cannot read the labels.
- Set defaults so repeatedly pressing Confirm takes players into the game, through character selection and into an opening stage or tutorial.

## 252 HUDs [UI]
- A HUD is screen-attached information, sometimes drawn to follow a character. Some games present many details, while others hide or toggle them for immersion. Show what makes the game easier or more enjoyable to play.
- Portraits can emphasize character on a small screen, and animated backgrounds can add energy. Fade overlapping elements, show contextual cursors only when needed, and change meters to reflect status. An icon can identify a defeated target that was hard to see in 3D.
