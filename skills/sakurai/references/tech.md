# Programming and tech (parameters, debug modes, management)

Summaries based on the Japanese captions for Masahiro Sakurai on Creating Games. Episode numbers follow the repository’s oldest-first source order.

## 022 Name Files Logically [Programming & Tech]
- Put the action category first and the direction or number second so filenames and move labels sort together. Examples include attack1, attack2, attack3, attackS4, and attackAirS. Use numbers for strength levels.
- Keep names long enough to recognize at a glance.
- Avoid romanizing Japanese words in filenames. Choose names colleagues, including staff overseas, can understand.

## 046 Making Your Game Easy to Tune [Programming & Tech]
- Put tunable values such as attack power outside the program. A spreadsheet lets the designer adjust them. Sakurai likens the program to the skeleton and the parameters to the muscles.
- Hide seldom-used fields so important values stand out and mistakes are less likely. Formulas let you define one move with half the power of another.
- Make one button convert and apply values to a running development build. The older workflow took ten minutes and required a restart. Faster iteration lets you tune more thoroughly.

## 094 Using Tickets to Manage Tasks [Programming & Tech]
- Track production tasks in a shared ticket system and give each ticket an owner so work does not get missed.
- A single character can have separate tickets for planning, specifications, modeling, animation, programming, effects, audio, and tuning.
- Use statuses such as in progress, done, pending, and dropped. Set deadlines and have leads review them. Where possible, let downstream work start with a provisional version.
- Use the same process for bugs. Leads triage them, then the assignee fixes them and returns them for review.

## 117 Family BASIC [Programming & Tech]
- The episode introduces early home computers for making and playing games. (Few takeaways)
- Simple sprite controls taught Sakurai how inertia affects game feel, which helped him make the first Kirby. Making a small game is a way to learn those effects firsthand.
- The Famicom assigns background palette attributes to 16 × 16 pixel areas. Adjust placement, sometimes by a single tile, to make the desired colors fit the hardware limits.

## 143 Knockback in Super Smash Bros. [Programming & Tech]
- Smash Bros. attacks build damage. A more powerful hit launches a target with higher accumulated damage farther.
- Each attack can define a launch angle, a knockback multiplier, an additive minimum knockback, or fixed knockback independent of accumulated damage. Combo hits can use fixed knockback and an air-combo correction to keep targets from drifting out before the normal final launch.
- These parameters make it possible to fine-tune knockback for the game’s rules.

## 170 How Multiple People Work on One File [Programming & Tech]
- Use version control to manage shared project files. Files that cannot be merged can be locked during editing and released after upload.
- Locking a large file serializes work. With concurrent editing, let the version control tool merge compatible changes and resolve conflicts manually.
- Edits can be accidentally overwritten by an older version. Use history and backups to recover individual changes.

## 193 Debug Mode [Programming & Tech]
- Use a debug mode to set health, freeze the game, swap characters, move the camera freely, or change states. Make extreme parameter values easy to test.
- Useful debug views can become public features, such as the launch trajectory in training mode.
- Let developers use the normal controller for debugging.
- Debug features are often stripped from shipping builds. Keep the menus organized because the team uses them daily.

## 215 Transparency Features [Programming & Tech]
- Let developers hide or fade an entire model or part of one. Hiding a cloak can help check a pose.
- Individual visibility toggles are useful for development and screenshots.
