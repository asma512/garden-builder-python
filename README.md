## 🌸 Garden Maker CLI — Branching Strategy & Code Explanation

This project uses a simple **feature branch workflow** to keep development organized and the `main` branch stable.

---

### 🌿 Branching Strategy Used

I created a feature branch called **`feature/implement-garden-builder`** to build the main application. This branch includes all the core functionality of the Garden Maker CLI.

I also created a separate branch called **`docs/update-readme`** to update documentation without mixing it with code changes.

Additionally, I created a **`refactor/add-folder-structure`**  branch to improve the project layout by adding src folder to hold python code

Each branch was created from `main`, worked on independently, and then merged back using a Pull Request. This keeps changes clean and easy to review.

---

### 💻 Code Explanation

The program is a simple **command-line app** that lets users manage a list of flowers.

At the start, I created an empty list called `garden`:

* This list stores all the flowers the user adds while the program is running.

The program runs inside a **while loop**, which keeps it running until the user chooses to exit:

* This allows the user to perform multiple actions without restarting the program.

Inside the loop, a **menu is displayed**:

* Add flower
* View garden
* Remove flower
* Exit

Each option triggers a different block of code:

* **Add flower**: takes user input and adds it to the list
* **View garden**: prints all flowers currently in the list
* **Remove flower**: removes a flower if it exists in the list
* **Exit**: stops the loop and ends the program

I also added:

* Input normalization (capitalization) so “rose” and “Rose” are treated the same
* Basic validation so invalid menu choices show a message instead of breaking the program

---

### 🚀 Production Improvements

If this were a real production app, I would:

* Split the code into functions or separate files
* Save data so the garden is not lost when the program closes
* Add automated tests
* Improve error handling and input validation
* Add logging for debugging and tracking issues

---

This project is a simple but solid example of basic Python logic, user input handling, and state management in a CLI application.

