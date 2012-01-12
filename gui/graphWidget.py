from PyQt4.QtCore import QString, Qt, SIGNAL, SLOT, QRectF, QPointF, QStringList, QRectF
from PyQt4.QtGui import *
import math

class GraphWidget(QGraphicsView):
	def __init__(self, parent):
		super(GraphWidget, self).__init__(parent)

		self.timerId = 0

		scene = QGraphicsScene(self)
		scene.setItemIndexMethod(QGraphicsScene.NoIndex)
		#scene.setSceneRect(-200, -200, 400, 400)
		self.setScene(scene)
		self.setCacheMode(QGraphicsView.CacheBackground)
		self.setViewportUpdateMode(QGraphicsView.BoundingRectViewportUpdate)
		self.setRenderHint(QPainter.Antialiasing)
		self.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)
		self.setResizeAnchor(QGraphicsView.AnchorViewCenter)


		self.scale(0.9, 0.9)
		self.setMinimumSize(480, 480)

	def itemMoved(self):
		if not self.timerId:
			self.timerId = self.startTimer(1000 / 25)

	def keyPressEvent(self, event):
		key = event.key()

		if key == Qt.Key_Up:
			self.centerNode.moveBy(0, -20)
		elif key == Qt.Key_Down:
			self.centerNode.moveBy(0, 20)
		elif key == Qt.Key_Left:
			self.centerNode.moveBy(-20, 0)
		elif key == Qt.Key_Right:
			self.centerNode.moveBy(20, 0)
		elif key == Qt.Key_Plus:
			self.scaleView(1.2)
		elif key == Qt.Key_Minus:
			self.scaleView(1 / 1.2)
		elif key == Qt.Key_Space or key == Qt.Key_Enter:
			for item in self.scene().items():
				if isinstance(item, Node):
					item.setPos(-150 + qrand() % 300, -150 + qrand() % 300)
				else:
					super(GraphWidget, self).keyPressEvent(event)

	def timerEvent(self, event):
		nodes = [item for item in self.scene().items() if isinstance(item, Node)]

		for node in nodes:
			node.calculateForces()

		itemsMoved = False
		for node in nodes:
			if node.advance():
				itemsMoved = True

		if not itemsMoved:
			self.killTimer(self.timerId)
			self.timerId = 0

	def wheelEvent(self, event):
		self.scaleView(math.pow(2.0, -event.delta() / 240.0))

	def drawBackground(self, painter, rect):
		# Shadow.
		sceneRect = self.sceneRect()
		
		border = 20
		sceneRect.adjust(-border,-border,border,border)

		rightShadow = QRectF(sceneRect.right(), sceneRect.top() + 5, 5, sceneRect.height())
		bottomShadow = QRectF(sceneRect.left() + 5, sceneRect.bottom(), sceneRect.width(), 5)
		if rightShadow.intersects(rect) or rightShadow.contains(rect):
			painter.fillRect(rightShadow, Qt.darkGray)
			if bottomShadow.intersects(rect) or bottomShadow.contains(rect):
				painter.fillRect(bottomShadow, Qt.darkGray)

		# Fill.
		gradient = QLinearGradient(sceneRect.topLeft(),
							 sceneRect.bottomRight())
		gradient.setColorAt(0, Qt.white)
		gradient.setColorAt(1, Qt.lightGray)
		painter.setBrush(Qt.NoBrush)
		painter.drawRect(sceneRect)


	def scaleView(self, scaleFactor):
		factor = self.matrix().scale(scaleFactor, scaleFactor).mapRect(QRectF(0, 0, 1, 1)).width()

		if factor < 0.07 or factor > 100:
			return

		self.scale(scaleFactor, scaleFactor)
