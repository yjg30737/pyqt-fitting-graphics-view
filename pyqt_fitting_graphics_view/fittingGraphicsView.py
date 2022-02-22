from PyQt5.QtCore import Qt
from pyqt_single_image_graphics_view import SingleImageGraphicsView


class FittingGraphicsView(SingleImageGraphicsView):
    def __init__(self):
        super().__init__()

    def resizeEvent(self, e):
        if self._item:
            self.fitInView(self._item, Qt.KeepAspectRatio)
        return super().resizeEvent(e)
