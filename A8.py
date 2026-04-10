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
        self.timer = QTimer()
        self.timer.timeout.connect(self.next)
        #needs something to show the frames per second
        self.fps = '1'
        #needs something to track image order
        self.order = 0

        # Make the GUI in the setupUI method
        self.setupUI()


    def setupUI(self):
        # An application needs a central widget - often a QFrame
        frame = QFrame()

        #need layout for base + images
        base_layout = QHBoxLayout()
        image_layout = QVBoxLayout()

        # on the left need label with image like in example screenshot
        self.image_display = QLabel()
        self.image_display.setPixmap(self.frames[self.order])

        # need start & stop below label like in example screenshot
        self.startbutton = QPushButton("Start")
        self.startbutton.clicked.connect(self.start)

        image_layout.addWidget(self.startbutton)
        image_layout.addWidget(self.image_display)

        # Fps display
        image_layout.addWidget(QLabel("Frames per second:"))
        self.fps_display = QLabel(self.fps)
        image_layout.addWidget(self.fps_display)

        #needs slider
        self.slider = QSlider()
        self.slider.setRange(1, 100)
        self.slider.setValue(1)
        self.slider.valueChanged.connect(self.change)

        #tick marks
        self.slider.setTickPosition(QSlider.TickPosition.TicksRight)
        self.slider.setTickInterval(10)

        #need menu
        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        base_menu = menubar.addMenu("&File")

        #inside menu need pause
        pause = QAction("&Pause", self)
        pause.triggered.connect(self.pauseRun)
        base_menu.addAction(pause)

        #inside menu need exit
        exit = QAction("&Exit", self)
        exit.triggered.connect(self.exitRun)
        base_menu.addAction(exit)

        # Create needed connections between the UI components and slot methods
        # you define in this class.
        base_layout.addLayout(image_layout)
        base_layout.addWidget(self.slider)

        frame.setLayout(base_layout)
        self.setCentralWidget(frame)

    # You will need methods in the class to act as slots to connect to signals
    def start(self):
        fps_num = int(self.fps)
        if self.startbutton.text() == "Start":
            self.timer.start(int(1000 / fps_num))
            self.startbutton.setText("Stop")
        else:
            self.timer.stop()
            self.startbutton.setText("Start")

    def change(self):
        self.fps = self.slider.value()
        self.fps_display.setText(str(self.fps))
        if self.timer.isActive():
            fps_num = int(self.fps)
            self.timer.start(int(1000 / fps_num))

    def next(self):
        self.order += 1
        if self.order >= self.num_frames:
            self.order = 0
        self.image_display.setPixmap(self.frames[self.order])
        self.repaint()

    def pauseRun(self):
        self.timer.stop()
        self.startbutton.setText("Start")

    def exitRun(self):
        self.close()


def main():
    app = QApplication([])
    # Create our custom application
    window = SpritePreview()
    # And show it
    window.show()
    app.exec()

if __name__ == "__main__":
    main()
