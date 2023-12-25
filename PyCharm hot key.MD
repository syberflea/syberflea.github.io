# Editor basics

`Alt 1` Projects

`Alt 2` Bookmarks

`Alt 3` Find

`Alt 4` Open Run window

`Alt 5` Open Debug window

`Alt 6` Problems

`Alt 7` Structure

`Alt 8` Services

`Alt 9` Version Control

## Context Action

`Alt Enter` to invoke Show Context Action


## Search for actions

`Ctrl Shift A` - Find Action. Or

`Shift Shift` - поиск в классе, функции, файле, PyCharm action и в настройках.


## Expand and shrink the code selection

`Ctrl+W`  to select the word under the caret

`Ctrl+W`  again to select the whole string

`Ctrl+W`  for the third time to include quotes in the selection

`Ctrl+W`  four times to select whole call

`Ctrl+Shift+W`  to shrink selection back to the arguments

`Ctrl+W` two times at the beginning of 'if' select all statement


## Comment line

`Ctrl+/` Comment out any line, multiple lines also. Uncomment the commented line.


## Duplicate and delete lines

`Ctrl+D` Дублировать строку.

`Ctrl+Y` Удалить строку.


## Move code fragments

`Alt+Shift+(вверх, вниз)` — Переместить строку вверх или вниз.

`Ctrl+Shift+(вверх, вниз)` — Переместить метод вверх или вниз.


## Collapse

`Ctrl+Minus`  collapse a code fragment

`Ctrl+Equals` expand a code region

`Ctrl+Shift+Minus`  collapse all code regions

`Ctrl+Shift+Equals` expand all code region


## Surround and unwrap

`Ctrl Alt T` surround the selected code fragment with some template code.

`Ctrl Shift Delete` return to previous state.


## Multiple selections

`Alt+J` select the symbol at the caret

`Alt+J` press again to select next occurence of the symbol 

`Alt+Shift+J` deselect the last occurence

`Ctrl+Alt+Shift+J` to select all occurences in the file

Type `something` to replace all `occurences` with `something`.


## Code completion  

By default, PyCharm proposes completionfor your code instantly

`Ctrl` `Space` to activate basic completion explicitly

### Tab completion

Suppose you want to replace `current` with `total`. Invoke completion by pressing `Ctrl Space`. 

Select `total` item using keyboard arrows or just start typing it. Press `Tab`, not `Enter` to replace `current` with `total`.

### Postfix completion

Postfix completion helps you to reduce backward caret jumps as you write code. For example, type `.if`, select the point and press `Enter`.

### Type-matching completion

Sometime Basic Completion doesn't work, try Smart Completion by invoking `Ctrl Shift Space` instead. 


## Refactorings

`Ctrl Alt Shift T` press to list all refactorings available in the current context.

### Rename

`Shift F6` press to rename

### Extract variable

`Ctrl Alt V` press to extract a local variable from the expression.

`Ctrl Alt M` press to extract selected code block to a method. Объединить выделенный код в функцию/метод.

### Quick-fix refactoring (section incomplete)

`Alt Enter` invoke intentions while edititng code.

### In-place refactoring (section incomplete)  

`Alt Enter` invoke intentions while edititng code.


## Code assistance

### Restore removed code   

Imagine you need to restore code that was deleted earlier. Undo won't work because there have been multiple changes since then and you don't want to lose those changes.

Use Local History to restore the deleted code with just a few clicks. Right-click anywhere in the editor to open the context menu.
Choose Local History -> Show History…

The left pane of the Local History dialog displays a list of saved revisions of the current file. The project state is automatically saved in Local History every time you edit code, run tests, or perform other actions. Lets select the revision that is highlighted.

The right pane displays the differences between the selected and current revisions of the file. In this case, the selected revision contains the code that was deleted earlier. To restore the code fragment, click the chevron button ».

Close the dialog to return to the changed code. Press Escape.

### Code format   

PyCharm can help you correct code formatting with just one action. Press `Ctrl Alt L` to reformat the selected code fragment.

To reformat the whole file when no lines are selected, use `Ctrl Alt L`

Use `Ctrl Alt Shift L` to show reformat settings. Here you can configure reformat options. For example, switch Optimize Imports on and click Run.

### Parameter info 

`Ctrl+P` see the method's signature

### Quick popups

`Ctrl+Q` to see documentaion for the symbol at the caret

`Ctrl+Shift+I` to see definition of the symbol at the caret

### Editor code assistance

`F2` to go to the next highlighted error in the file

`Alt Enter` to open context menu and fix the error.

`Ctrl+F1` to expand the warning description

`Alt+Shift+Enter` to remove unexpected arguments

`Ctrl+Shift+F7` to highlight all usages of the symbol at the caret within the file


## Navigation

### Search everywhere

`Shift Shift` open Search Everywhere.

Suppose you are looking for a class with the words quadratic and equation in the name. Type `que` (initial letters of these words) in the search field.

Select `QuadraticEquationsSolver` with the keyboard arrows and press `Enter` to jump to the definition of this class.

Great! However, sometimes you need to find only classes or search only in some specific directories. Use `Ctrl N` to search for classes.

Suppose you need some library class responsible for buffered reading from an input stream. Type `bufre` (initial letters of the search words), but do not navigate yet.

Now you can see there is a matching class in the demo project. However, we need to find a class in libraries. Let's switch the Project Files filter to `All Places` to bring up matching classes from available libraries.

`Ctri Q` to preview documentation for the selected class.

`Escape` to close the popup.

`Ctrl+Alt+Shift+N`  to look for a method or a global variable.

`Ctrl+N` — Найти класс по названию (по всем местам).

`Ctrl+Shift+N` — Найти файл по названию (по всем местам).

### Find and replace in files

Ctrl+R — Изменить название класса/функции и т. п. по всему проекту.

Suppose you want to find all occurrences of some string in the project. 

`Ctrl Shift F` to open the Find in Files… window.

Type `apple` to search for all textual occurrences in the Learning project.

You were supposed to find the `apple` string but also got some pineapple entries. Let's narrow down the search to a whole word. Click `W` or press `Alt W`

You can see the context of the found string in the embedded editor. Click the highlighted row or navigate to it by using and buttons.

Also, you can open the selected file in the main editor. Press Enter or double-click the highlighted item to move to the corresponding file.

Suppose you want to replace all found occurrences with another string. It may be very boring to perform replacing in each file sequentially.

`Ctrl Shift R` to open **Replace in Files…** window.

`Alt D` to narrow the replacement only to current directory.

`Replace All` to start the replacement.

Finally, click `Replace` in the dialog to confirm.

### Declaration and usages

`Ctrl B` to jump to the declaration of a method. Now the caret is at the method's declaration. Use the same shortcut `Ctrl B` to see all of its usages, then select one of them.

`Alt F7` to see a more detailed view of usages. You can invoke `Alt F7` on either a declaration or a usage.

From the Find view you can navigate both to usages and declarations. The next search will override these results in the Find view. To prevent it, pin the results:

`Right-click` the tab title, ... in All Places. Select Pin Tab. 

When you have finished browsing usages, press `Shift Escape` to hide the view.

`Alt 3` to open the Find view again.

### File structure

A large source file can be difficult to read and navigate. Sometimes you only need to preview it. 

`Ctrl F12` to open the file structure.

Suppose you want to find a method with Homo and Sapiens words in its name. Type hosa (prefixes of the required words) to filter the file structure.

Only one item remains. Now press Enter to jump to the selected item.

PyCharm can also show you the file structure as a tool window. 

Open it with `Alt 7`.

### Recent files and locations

`Ctrl B` to jump to the declaration of a method.

`Ctrl+E` — Навигация по файлам (отображает список файлов в хронологическом порядке).

`Ctrl+Shift+E` recently visited files


## Run and debug



### Run configuration

`Ctrl+Shift+F10` run the current file

Running `Current File` does not create any run configurations.

Now PyCharm has created a temporary run configuration. Temporary configurations are automatically deleted when their number exceeds the default limit of five. Let's convert the temporary configuration into a permanent one. 

Click `:` (3 vertical dots) next to the `Run and Debug` buttons.

Show more actions | Select Save Configuration.

Now let's look at the run configurations popup. Click the drop-down.

To edit run configurations or add new ones, click the drop-down while holding Shift or open the drop-down and click Edit Configurations…

This is a place for managing all run configurations. Here you can set program parameters, JVM arguments, environment variables, and so on.

Tip: To make a run configuration accessible to your colleagues, store it as a separate file and share this file via a version control system.

`Alt Shift E` Execute Selection in Python Console

### Debug workflow

Let's set a breakpoint to start investigating the problem. 

To do so, click the gutter at the desired line or set the caret to that line and press `Ctrl F8`.

`Ctrl+F8` set a beakpoint

`Shift+F9` start debugging

`Ctrl Shift Enter` add expression to Debugger watches

`Ctrl Shift A` add selected text to Debugger watches

`Ctrl Alt F8` Quick Evaluate Expression

`Ctrl F5` rerun program

`F9` resume program execution

`Alt F9` execute the program up to the line where the caret is.

`Ctrl F2` finish debuging.


## VCS

`Ctrl K` Open Commit window

`Ctrl Shift K` open Push dialog

`Alt 9` open Git tool window


---

# Miscellaneous section

`Ctrl+Alt+S` — Перейти в настройки (откроется та часть где вы остановились).

`Ctrl+J` — Использовать шаблон кода.

$OutputEncoding = [System.Console]::OutputEncoding = [System.Console]::InputEncoding = [System.Text.Encoding]::UTF8
