#Name: Sprite-Previewer


import math
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *

# This function loads a series of sprite images stored in a folder with a
# consistent naming pattern: sprite_# or sprite_##. It returns a list of the images.
def load_sprite(sprite_folder_name, number_of_frames):
    frames = []
    padding = math.ceil(math.log(number_of_frames - 1, 10))
    for frame in range(number_of_frames):
        folder_and_file_name = sprite_folder_name + "/sprite_" + str(frame).rjust(padding, '0') + ".png"
        frames.append(QPixmap(folder_and_file_name))

    return frames

class SpritePreview(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sprite Animation Preview")

        # This loads the provided sprite and would need to be changed for your own.
        self.num_frames = 21
        self.frames = load_sprite('spriteImages',self.num_frames)

        # Add any other instance variables needed to track information as the program
        # runs here

        #needs timer
        #needs something to show the frames per second
        #needs something to track image order

        # Make the GUI in the setupUI method
        self.setupUI()


    def setupUI(self):
        # An application needs a central widget - often a QFrame
        frame = QFrame()

        #need layout for base + images

        # on the left need label with image like in example screenshot

        # need start & stop below label like in example screenshot

        #on right need slider

        #label that displays fps

        #stop/start button

        #need menu

        #inside menu need pause

        #inside menu need exit


        # Create needed connections between the UI components and slot methods
        # you define in this class.

        self.setCentralWidget(frame)

    # You will need methods in the class to act as slots to connect to signals

    def main():
        app = QApplication([])
        # Create our custom application
        window = SpritePreview()
        # And show it
        window.show()
        app.exec()

    if __name__ == "__main__":
        main()
