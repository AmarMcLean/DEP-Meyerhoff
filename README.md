Program usage and capabilities:

File:
- To load file click "load" (It is the leftmost "load" if you have selected "2")
- To save file click "save"
- To have a second file loaded, currently for viewing purposes only, click "2" then "load" (rightmost)
- To remove the second file from view click "1"

Search:
Enter the desired keyword into the box and click search.
Keep in mind the current search functionally works for one attribute at a time.
For instance searching "John Doe" as Firstname Lastname attributes will not work, you'd have to search "John" or "Doe"

Reformat:
- View currently isn't functional.
It's purpose, however, is to query the data to display only the desired attributes in the table
- Split, on the other hand, is fully functional.
Its function is to create and save a separate file that only contains the desired attributes selected by the user.
Click the checkboxes for the desired attributes to include in the file, then click the "create" button and save.

Entry:
The purpose of this feature is strictly to change attributes of existing rows within the file.
Currently, this does not act as a way to insert new rows, but this will soon be changed.
To use it, click the checkboxes for the attributes in which will be used as identifiers to find a row within the file.
Then enter the value into the checked attribute.
Next, enter the value in which you'd like to change in unchecked attributes.
Empty attributes will be unaffected.
Finally, click Add to add the unchecked attributes to the row
- WARNING: Any changes made will be final as there is currently no undo button
- WARNING: Make sure you do not leave any spaces in empty attributes as this will replace any data with a space
- The easiest way to avoid the above problem is to fully "backspace" any edited attributes

The current look is temporary, although very different from before, as I'm experimenting with the aesthetic.
That being said, this version is just plain white for usability.

Adding and Deleting:
To Add or Delete a row, right-click the left-hand index column, then click "Add Row(s)".
To Add or Delete a column, right-click the top attribute row, and click on "column" then "Add".

Be wary of doing anything important in this version as it is not final and all kinks aren't yet ironed out.

When recreating distributable use 'pyinstaller --onefile --hidden-import pandastable ../src/GUI.py' from distributables folder