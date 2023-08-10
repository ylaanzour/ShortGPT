from gui.gui_gradio import ShortGptUI

app = ShortGptUI(colab=False, share=True)
app.launch()
