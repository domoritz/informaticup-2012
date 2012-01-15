from PyQt4.QtCore import QString, Qt, SIGNAL, SLOT, QRectF, QPointF, QStringList, QRectF, QLineF, qAbs, QSizeF, qrand
from PyQt4.QtGui import *
import math

#############################################################################
##
## INSPIRED BY: elastic.py from the example of PyQt
##
#############################################################################
##
## Copyright (C) 2010 Riverbank Computing Limited.
## Copyright (C) 2010 Nokia Corporation and/or its subsidiary(-ies).
## All rights reserved.
##
## This file is part of the examples of PyQt.
##
## $QT_BEGIN_LICENSE:BSD$
## You may use this file under the terms of the BSD license as follows:
##
## "Redistribution and use in source and binary forms, with or without
## modification, are permitted provided that the following conditions are
## met:
##   * Redistributions of source code must retain the above copyright
##     notice, this list of conditions and the following disclaimer.
##   * Redistributions in binary form must reproduce the above copyright
##     notice, this list of conditions and the following disclaimer in
##     the documentation and/or other materials provided with the
##     distribution.
##   * Neither the name of Nokia Corporation and its Subsidiary(-ies) nor
##     the names of its contributors may be used to endorse or promote
##     products derived from this software without specific prior written
##     permission.
##
## THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
## "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
## LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
## A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
## OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
## SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
## LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
## DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
## THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
## (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
## OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE."
## $QT_END_LICENSE$
##
#############################################################################


class GraphWidget(QGraphicsView):
	def __init__(self, parent):
		super(GraphWidget, self).__init__(parent)

		self.timerId = 0

		self.elastic = False

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

	def itemMoved(self):
		if not self.timerId:
			self.timerId = self.startTimer(1000 / 25)

	def makeElastic(self, value = True):
		self.elastic = value

	def timerEvent(self, event):
		if self.elastic:
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
		sceneRect = self.sceneRect()

		border = 20
		sceneRect.adjust(-border,-border,border,border)

		"""rightShadow = QRectF(sceneRect.right(), sceneRect.top() + 5, 5, sceneRect.height())
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
		painter.drawRect(sceneRect)"""


	def scaleView(self, scaleFactor):
		factor = self.matrix().scale(scaleFactor, scaleFactor).mapRect(QRectF(0, 0, 1, 1)).width()

		if factor < 0.07 or factor > 150:
			return

		self.scale(scaleFactor, scaleFactor)

class Edge(QGraphicsItem):
	Pi = math.pi
	TwoPi = 2.0 * Pi

	Type = QGraphicsItem.UserType + 2

	def __init__(self, sourceNode, destNode, state=1, text=""):
		super(Edge, self).__init__()

		self.arrowSize = 15.0
		self.sourcePoint = QPointF()
		self.destPoint = QPointF()

		self.setAcceptedMouseButtons(Qt.NoButton)
		self.source = sourceNode
		self.dest = destNode
		self.source.addEdge(self)
		self.dest.addEdge(self)
		self.adjust()

		self.state = state
		self.text = text

		line = QLineF(sourceNode.pos(), destNode.pos())
		self.weight = line.length()

	def __len__(self):
		line = QLineF(self.sourceNode().pos(), self.destNode().pos())
		return line.length() 

	def type(self):
		return Edge.Type

	def sourceNode(self):
		return self.source

	def setSourceNode(self, node):
		self.source = node
		self.adjust()

	def destNode(self):
		return self.dest

	def setDestNode(self, node):
		self.dest = node
		self.adjust()

	def adjust(self):
		if not self.source or not self.dest:
			return

		line = QLineF(self.mapFromItem(self.source, 0, 0),
				self.mapFromItem(self.dest, 0, 0))
		length = line.length()

		self.prepareGeometryChange()

		if length > 20.0:
			edgeOffset = QPointF((line.dx() * 10) / length,
						(line.dy() * 10) / length)

			self.sourcePoint = line.p1() + edgeOffset
			self.destPoint = line.p2() - edgeOffset
		else:
			self.sourcePoint = line.p1()
			self.destPoint = line.p1()

	def setVisible(self, value = True):
		if value:
			self.state = 1
		else:
			self.state = 0

	def setActive(self, value = True):
		if value:
			self.state = 3
		else:
			self.state = 1

	def setTempActive(self, value = True):
		if value:
			self.state = 2
		else:
			self.state = 1

	def boundingRect(self):
		if not self.source or not self.dest:
			return QRectF()

		penWidth = 1.0
		extra = (penWidth + self.arrowSize) / 2.0 + 100

		return QRectF(self.sourcePoint,
				QSizeF(self.destPoint.x() - self.sourcePoint.x(),
		   self.destPoint.y() - self.sourcePoint.y())).normalized().adjusted(-extra, -extra, extra, extra)

	def paint(self, painter, option, widget):
		if not self.source or not self.dest:
			return

		# Draw the line itself.
		line = QLineF(self.sourcePoint, self.destPoint)

		if line.length() == 0.0:
			return

		palette = QPalette()

		self.setZValue(self.state)

		if self.state == 3:
			pen = QPen(Qt.red, 2, Qt.SolidLine,
					  Qt.RoundCap, Qt.RoundJoin)
		if self.state == 2:
			pen = QPen(Qt.red, 2, Qt.DashLine,
					  Qt.RoundCap, Qt.RoundJoin)
		elif self.state == 1:
			pen = QPen(palette.color(QPalette.Disabled,QPalette.WindowText), 0, Qt.SolidLine,
					  Qt.RoundCap, Qt.RoundJoin)
		elif self.state == 0:
			pen = QPen()
			pen.setBrush(QBrush(Qt.NoBrush))

		painter.setPen(pen)

		painter.drawLine(line)

		angle = math.acos(line.dx() / line.length())
		if line.dy() >= 0:
			angle = Edge.TwoPi - angle

		# draw arrowheads
		if self.state == 2 or self.state == 3:

			# Draw the arrows if there's enough room.
			sourceArrowP1 = self.sourcePoint + QPointF(math.sin(angle + Edge.Pi / 3) * self.arrowSize,
												 math.cos(angle + Edge.Pi / 3) * self.arrowSize)
			sourceArrowP2 = self.sourcePoint + QPointF(math.sin(angle + Edge.Pi - Edge.Pi / 3) * self.arrowSize,
												 math.cos(angle + Edge.Pi - Edge.Pi / 3) * self.arrowSize);   
			destArrowP1 = self.destPoint + QPointF(math.sin(angle - Edge.Pi / 3) * self.arrowSize,
											 math.cos(angle - Edge.Pi / 3) * self.arrowSize)
			destArrowP2 = self.destPoint + QPointF(math.sin(angle - Edge.Pi + Edge.Pi / 3) * self.arrowSize,
											 math.cos(angle - Edge.Pi + Edge.Pi / 3) * self.arrowSize)

			painter.setPen(QPen(Qt.red, 2, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
			painter.setBrush(QBrush(Qt.red,Qt.SolidPattern))
			painter.drawPolygon(QPolygonF([line.p1(), sourceArrowP1, sourceArrowP2]))
			#painter.drawPolygon(QPolygonF([line.p2(), destArrowP1, destArrowP2]))

		if self.state > 0 and self.source > self.dest:
			point = QPointF((self.sourcePoint.x() + self.destPoint.x())/2,(self.sourcePoint.y() + self.destPoint.y())/2)
			point = QPointF(point.x() + math.sin(angle)*16,point.y()+ math.cos(angle)*16)
			painter.drawText(point, self.text)
			#self.textItem = QGraphicsTextItem(self.text,self)
			#self.textItem.setPos(point)


class Node(QGraphicsItem):
	Type = QGraphicsItem.UserType + 1

	def __init__(self, graphWidget, text=""):
		super(Node, self).__init__()

		self.graph = graphWidget
		self.edgeList = []
		self.newPos = QPointF()

		self.setFlag(QGraphicsItem.ItemIsMovable)
		self.setFlag(QGraphicsItem.ItemSendsGeometryChanges)
		self.setCacheMode(QGraphicsItem.DeviceCoordinateCache)
		self.setZValue(1)

		self.text = text
		self.active = False

		self.b = 15

	def type(self):
		return Node.Type

	def addEdge(self, edge):
		self.edgeList.append(edge)
		edge.adjust()

	def setActive(self, value = True):
		self.active =value


	def edges(self):
		return self.edgeList

	def calculateForces(self):
		if not self.scene() or self.scene().mouseGrabberItem() is self:
			self.newPos = self.pos()
			return

		# Sum up all forces pushing this item away.
		xvel = 0.0
		yvel = 0.0
		for item in self.scene().items():
			if not isinstance(item, Node):
				continue

			line = QLineF(self.mapFromItem(item, 0, 0),
						QPointF(0, 0))
			dx = line.dx()
			dy = line.dy()
			l = 2.0 * (dx * dx + dy * dy)
			if l > 0:
				xvel += (dx * 150.0) / l
				yvel += (dy * 150.0) / l

		# Now subtract all forces pulling items together.
		#weight = (len(self.edgeList) + 1) * 100.0
		for edge in self.edgeList:
			if edge.sourceNode() is self:
				pos = self.mapFromItem(edge.destNode(), 0, 0)
			else:
				weight = edge.weight*6
				pos = self.mapFromItem(edge.sourceNode(), 0, 0)
				xvel += pos.x() / weight
				yvel += pos.y() / weight

		if qAbs(xvel) < 0.1 and qAbs(yvel) < 0.1:
			xvel = yvel = 0.0

		sceneRect = self.scene().sceneRect()
		self.newPos = self.pos() + QPointF(xvel, yvel)
		self.newPos.setX(min(max(self.newPos.x(), sceneRect.left() + 10), sceneRect.right() - 10))
		self.newPos.setY(min(max(self.newPos.y(), sceneRect.top() + 10), sceneRect.bottom() - 10))

	def advance(self):
		if self.newPos == self.pos():
			return False

		self.setPos(self.newPos)
		return True

	def boundingRect(self):
		adjust = 2.0
		return QRectF(-self.b - adjust, -self.b - adjust, 2*self.b+3 + adjust,
				2*self.b+3 + adjust)

	def shape(self):
		path = QPainterPath()
		path.addEllipse(-self.b, -self.b, 2*self.b, 2*self.b)
		return path

	def paint(self, painter, option, widget):
		self.setZValue(5)
		palette = QPalette()

		painter.setPen(Qt.NoPen)
		painter.setBrush(Qt.darkGray)


		gradient = QRadialGradient(-3, -3, 15)
		if option.state & QStyle.State_Sunken or self.active:
			gradient.setCenter(3, 3)
			gradient.setFocalPoint(3, 3)
			gradient.setColorAt(1, palette.color(QPalette.Active,QPalette.Button))
			gradient.setColorAt(0, palette.color(QPalette.Active,QPalette.Button))
			pen = QPen(palette.color(QPalette.Active,QPalette.ButtonText), 2)
		else:
			gradient.setColorAt(1, palette.color(QPalette.Disabled,QPalette.Button))
			gradient.setColorAt(0, palette.color(QPalette.Disabled,QPalette.Button))
			pen = QPen(palette.color(QPalette.Disabled,QPalette.ButtonText), 0)

		painter.setBrush(QBrush(gradient))
		painter.setPen(pen)
		painter.drawEllipse(-self.b, -self.b, 2*self.b, 2*self.b)

		painter.drawText(self.boundingRect(), Qt.AlignCenter, self.text)

	def itemChange(self, change, value):
		if change == QGraphicsItem.ItemPositionHasChanged:
			for edge in self.edgeList:
				edge.adjust()
				self.graph.itemMoved()

		return super(Node, self).itemChange(change, value)

	def mousePressEvent(self, event):
		self.update()
		super(Node, self).mousePressEvent(event)

	def mouseReleaseEvent(self, event):
		self.update()
		super(Node, self).mouseReleaseEvent(event)
