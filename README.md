# TMTP-Text-Editor
This is a ROMHacking tool for the DSiWare game "Too Much Tingle Pack."

Note: As of 0.9.5, this game (both vanilla and edited) does not emulate correctly in MelonDS. As such, you will have to run it through a loader on hardware (e.g. TwilightMenu++).

To get started, download TinkeDSi by R-YaTian. If it has a release after 0.9.3, download it from here: https://github.com/R-YaTian/TinkeDSi/releases.
Otherwise, you will need to download the "nightly" version from here: https://github.com/R-YaTian/TinkeDSi/actions/runs/4741139830 (you want the "Artifact" at the bottom).

After extracting the zip, rename the folder you from TinkeDSi... to just TinkeDSi, then drag it over into this very folder. Now open Tinke.exe in there, and choose your
Dekisugi Tincle Pack ROM. Click on the "root" folder in the tree, then press "Extract," and choose this folder as the destination.

Now we can run split.bat. This requires you to have Python 3+ installed, but I mean you are hacking a DSiWare game so that shouldn't be too difficult. This will create
a series of five "OVL" folders, inside which are a variety of text files. Some of them appear to be gibberish or code or something; the easiest way to check is by opening them
in Notepad++, since that renders it in Japanese automatically if possible. Basically, don't mess with anything that doesn't look like text.

When you are ready to insert, first run merge.bat, which creates a series of "output_overlay" files. Then, open up your ROM in tinke, choose whichever overlay(s) you edited, click
on it, and press "Change File." In the file popup menu from that, choose the corresponding output_overlay, then press Save ROM. On the screen that pops up from that, keep both
check-boxes unchecked, then prss "Accept." Now you get to name your new ROM file, and you're done!

Finally, much of this game's text is stored in graphic files. Thankfully, there is an existing editor for those, which can be found here: https://www.romhacking.net/utilities/1628/.
Our process that created the "root" file already extracted the viw's, and then you can just reinsert them the same way as the overlays.

P.S. This was not a problem for me with text, but in case it comes up for graphics, here is how to fix the "DSi binaries missing" problem (credit to R-YaTian for originally writing
this up):
1. Open a vanilla ROM in tinke, press "Game Information" up top, then press the "Dump Donor Header button."
2. Open your edited ROM, press "Game Information" there, then "Edit header and banner," then "import donor iheader." Choose the header you just exported to import.
3. Save the ROM (specifically as a new file) and close tinke, then open it back up (with the edited ROM again). Now go to root/ftc, and replace arm7i.bin and arm9i.bin with those
from a vanilla ROM (e.g. from the "root" folder you made earlier). Save the ROM again.