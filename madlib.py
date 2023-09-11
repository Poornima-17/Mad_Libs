import tkinter as tk

def generate_story():
    noun1 = entry_noun1.get()
    noun2 = entry_noun2.get()
    noun3 = entry_noun3.get()
    place = entry_place.get()
    adjective1 = entry_adjective1.get()
    adjective2 = entry_adjective2.get()
    adjective3 = entry_adjective3.get()
    adverb1 = entry_adverb1.get()
    adverb2 = entry_adverb2.get()
    exclamation = entry_exclamation.get()

    story = (
        f"One day {noun1} went to {place}. "
        f"{noun1} felt very lonely, even though the view was {adjective1}. "
        f"{noun1} decided to call his two best friends {noun2} and {noun3}. "
        f"When they came, they told {noun1} something {adjective2} had happened. "
        f"{noun1} went there very {adverb1}. "
        f"When {noun1} came, {noun1} found out that his other friend was falling off a cliff. "
        f"{noun1} said {exclamation}. Inside {noun1} was feeling {adjective3}. "
        f"{noun1} managed to save him. "
        f"After that, they had a {adverb2} celebration. They all laughed."
    )
    
    story_label.config(text=story)

# Create a Tkinter window
window = tk.Tk()
window.geometry('700x650')
window.title("Mad Libs Game")

# Create and place labels and entry widgets
tk.Label(window, text="Enter your name:").pack()
entry_noun1 = tk.Entry(window)
entry_noun1.pack()

tk.Label(window, text="Enter your friend's name:").pack()
entry_noun2 = tk.Entry(window)
entry_noun2.pack()

tk.Label(window, text="Enter another friend's name:").pack()
entry_noun3 = tk.Entry(window)
entry_noun3.pack()

tk.Label(window, text="Enter a place name:").pack()
entry_place = tk.Entry(window)
entry_place.pack()

tk.Label(window, text="Enter an adjective:").pack()
entry_adjective1 = tk.Entry(window)
entry_adjective1.pack()

tk.Label(window, text="Enter another adjective:").pack()
entry_adjective2 = tk.Entry(window)
entry_adjective2.pack()

tk.Label(window, text="Enter one more adjective:").pack()
entry_adjective3 = tk.Entry(window)
entry_adjective3.pack()

tk.Label(window, text="Enter an adverb:").pack()
entry_adverb1 = tk.Entry(window)
entry_adverb1.pack()

tk.Label(window, text="Enter another adverb:").pack()
entry_adverb2 = tk.Entry(window)
entry_adverb2.pack()

tk.Label(window, text="Enter an emotion:").pack()
entry_exclamation = tk.Entry(window)
entry_exclamation.pack()

# Create a button to generate the story
generate_button = tk.Button(window, text="Generate Story", activebackground='green', command=generate_story)
generate_button.pack()

# Create a label to display the story
story_label = tk.Label(window, text="", wraplength=400)
story_label.pack()

window.mainloop()
