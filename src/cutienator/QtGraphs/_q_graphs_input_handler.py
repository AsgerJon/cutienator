"""
QGraphsInputHandler binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGraphs/6.12.0/QtGraphs/private/qgraphsinputhandler_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QGraphsInputHandler to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtCore import Qt
from ..QtGui import QPointingDevice
from ..QtQuick import QQuickItem
from . import QtGraphs3D

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QPoint
  from ..QtGui import QEventPoint, QHoverEvent, QVector2D
  from ..QtQuick import QQuickWheelEvent
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEventPoint = WAIT['QEventPoint']
  QHoverEvent = WAIT['QHoverEvent']
  QPoint = WAIT['QPoint']
  QQuickWheelEvent = WAIT['QQuickWheelEvent']
  QVector2D = WAIT['QVector2D']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QGraphsInputHandler(QQuickItem):
  """
  The cute side of Qt's QGraphsInputHandler: a plain Python object standing
  in front of one C++ QGraphsInputHandler.

  It is built on the cute 'QQuickItem', as Qt's QGraphsInputHandler is built
  on Qt's QQuickItem, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QGraphsInputHandler that has a ritual and that
  Python can call so far, 29 names in all: 'metaObject', 'pendingPoint',
  'setZoomEnabled', 'isZoomEnabled', 'setZoomAtTargetEnabled',
  'isZoomAtTargetEnabled', 'setRotationEnabled', 'isRotationEnabled',
  'setPanEnabled', 'isPanEnabled', 'setDragMode', 'dragMode',
  'setSelectionEnabled', 'isSelectionEnabled', 'setDefaultInputHandler',
  'unsetDefaultInputHandler', 'unsetDefaultTapHandler',
  'unsetDefaultDragHandler', 'unsetDefaultWheelHandler',
  'unsetDefaultPinchHandler', 'setDragButton', 'setPanButton', 'onTapped',
  'onTranslationChanged', 'onGrabChanged', 'onWheel', 'onPinchScaleChanged',
  'mouseMove', 'hoverMoveEvent'. None can be made from Python: one comes out
  of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QGraphsInputHandler::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QGraphsInputHandler::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QGraphsInputHandler::~QGraphsInputHandler()': the destructor:
    Python never removes a C++ QGraphsInputHandler.

  What has no ritual
  ------------------

  5 of the 37 functions Qt declares: 3 leans on 'QGraphsInputHandler; 2 not a
  gap.

  What to expect
  --------------

  - The C++ QGraphsInputHandler is created at the first use, not by
    'QGraphsInputHandler(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGraphsInputHandler.
  - Qt tells when it has removed the C++ QGraphsInputHandler. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QGraphsInputHandler that has no cute function yet,
    '__init__', 'setGraphsItem', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGraphsInputHandler'

  #  A C++ QGraphsInputHandler Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QGraphsInputHandler'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QGraphsInputHandler::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphsinputhandler.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QGraphsInputHandler::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK19QGraphsInputHandler10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setZoomEnabled(self, enable: bool) -> None:
    """
    Calls Qt's 'void QGraphsInputHandler::setZoomEnabled(bool enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphsinputhandler.html#setZoomEnabled

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QGraphsInputHandler::setZoomEnabled(bool enable)
    self.uglySide.call(
        'ritual_ZN19QGraphsInputHandler14setZoomEnabledEb', enable,
    )

  @overload(bool)
  def setZoomAtTargetEnabled(self, enable: bool) -> None:
    """
    Calls Qt's 'void QGraphsInputHandler::setZoomAtTargetEnabled(bool
    enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphsinputhandler.html#setZoomAtTargetEnabled

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QGraphsInputHandler::setZoomAtTargetEnabled(bool enable)
    self.uglySide.call(
        'ritual_ZN19QGraphsInputHandler22setZoomAtTargetEnabledEb', enable,
    )

  @overload(bool)
  def setRotationEnabled(self, enable: bool) -> None:
    """
    Calls Qt's 'void QGraphsInputHandler::setRotationEnabled(bool enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphsinputhandler.html#setRotationEnabled

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QGraphsInputHandler::setRotationEnabled(bool enable)
    self.uglySide.call(
        'ritual_ZN19QGraphsInputHandler18setRotationEnabledEb', enable,
    )

  @overload(bool)
  def setPanEnabled(self, enable: bool) -> None:
    """
    Calls Qt's 'void QGraphsInputHandler::setPanEnabled(bool enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphsinputhandler.html#setPanEnabled

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QGraphsInputHandler::setPanEnabled(bool enable)
    self.uglySide.call(
        'ritual_ZN19QGraphsInputHandler13setPanEnabledEb', enable,
    )

  @overload(QtGraphs3D.DragMode)
  def setDragMode(self, mode: QtGraphs3D.DragMode) -> None:
    """
    Calls Qt's 'void QGraphsInputHandler::setDragMode(QtGraphs3D::DragMode
    mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphsinputhandler.html#setDragMode

    Parameters
    ----------

    mode : QtGraphs3D.DragMode
      Passed on as its number.
    """
    #  void QGraphsInputHandler::setDragMode(QtGraphs3D::DragMode mode)
    self.uglySide.call(
        'ritual_ZN19QGraphsInputHandler11setDragModeEN10QtGraphs3D8DragMode'
        'E',
        mode.value,
    )

  @overload(bool)
  def setSelectionEnabled(self, enable: bool) -> None:
    """
    Calls Qt's 'void QGraphsInputHandler::setSelectionEnabled(bool enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphsinputhandler.html#setSelectionEnabled

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QGraphsInputHandler::setSelectionEnabled(bool enable)
    self.uglySide.call(
        'ritual_ZN19QGraphsInputHandler19setSelectionEnabledEb', enable,
    )

  def setDefaultInputHandler(self) -> None:
    """
    Calls Qt's 'void QGraphsInputHandler::setDefaultInputHandler()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphsinputhandler.html#setDefaultInputHandler
    """
    #  void QGraphsInputHandler::setDefaultInputHandler()
    self.uglySide.call(
        'ritual_ZN19QGraphsInputHandler22setDefaultInputHandlerEv',
    )

  @overload(Qt.MouseButtons)
  def setDragButton(self, button: Qt.MouseButtons) -> None:
    """
    Calls Qt's 'void QGraphsInputHandler::setDragButton(Qt::MouseButtons
    button)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphsinputhandler.html#setDragButton

    Parameters
    ----------

    button : Qt.MouseButtons
      Passed on as its number.
    """
    #  void QGraphsInputHandler::setDragButton(Qt::MouseButtons button)
    self.uglySide.call(
        'ritual_ZN19QGraphsInputHandler13setDragButtonE6QFlagsIN2Qt11MouseB'
        'uttonEE',
        button.value,
    )

  @overload(Qt.MouseButtons)
  def setPanButton(self, button: Qt.MouseButtons) -> None:
    """
    Calls Qt's 'void QGraphsInputHandler::setPanButton(Qt::MouseButtons
    button)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphsinputhandler.html#setPanButton

    Parameters
    ----------

    button : Qt.MouseButtons
      Passed on as its number.
    """
    #  void QGraphsInputHandler::setPanButton(Qt::MouseButtons button)
    self.uglySide.call(
        'ritual_ZN19QGraphsInputHandler12setPanButtonE6QFlagsIN2Qt11MouseBu'
        'ttonEE',
        button.value,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QGraphsInputHandler::QGraphsInputHandler(QQuickItem *parent)':
    leans on 'QGraphsInputHandler::qt_metacall(QMetaObject::Call, int,
    void**)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QGraphsInputHandler.__init__' has no cute function yet. Qt's "
        "'QGraphsInputHandler::QGraphsInputHandler(QQuickItem *parent)': "
        "leans on 'QGraphsInputHandler::qt_metacall(QMetaObject::Call, int, "
        "void**)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def pendingPoint(self) -> QPoint:
    """
    Calls Qt's 'QPoint QGraphsInputHandler::pendingPoint()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphsinputhandler.html#pendingPoint

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint QGraphsInputHandler::pendingPoint()
    address = self.uglySide.call(
        'ritual_ZN19QGraphsInputHandler12pendingPointEv',
    )
    from ..QtCore import QPoint
    return QPoint._cuteOwning(address)

  def isZoomEnabled(self) -> bool:
    """
    Calls Qt's 'bool QGraphsInputHandler::isZoomEnabled()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphsinputhandler.html#isZoomEnabled
    """
    #  bool QGraphsInputHandler::isZoomEnabled()
    return self.uglySide.call(
        'ritual_ZN19QGraphsInputHandler13isZoomEnabledEv',
    )

  def isZoomAtTargetEnabled(self) -> bool:
    """
    Calls Qt's 'bool QGraphsInputHandler::isZoomAtTargetEnabled()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphsinputhandler.html#isZoomAtTargetEnabled
    """
    #  bool QGraphsInputHandler::isZoomAtTargetEnabled()
    return self.uglySide.call(
        'ritual_ZN19QGraphsInputHandler21isZoomAtTargetEnabledEv',
    )

  def isRotationEnabled(self) -> bool:
    """
    Calls Qt's 'bool QGraphsInputHandler::isRotationEnabled()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphsinputhandler.html#isRotationEnabled
    """
    #  bool QGraphsInputHandler::isRotationEnabled()
    return self.uglySide.call(
        'ritual_ZN19QGraphsInputHandler17isRotationEnabledEv',
    )

  def isPanEnabled(self) -> bool:
    """
    Calls Qt's 'bool QGraphsInputHandler::isPanEnabled()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphsinputhandler.html#isPanEnabled
    """
    #  bool QGraphsInputHandler::isPanEnabled()
    return self.uglySide.call(
        'ritual_ZN19QGraphsInputHandler12isPanEnabledEv',
    )

  def dragMode(self) -> QtGraphs3D.DragMode:
    """
    Calls Qt's 'QtGraphs3D::DragMode QGraphsInputHandler::dragMode()'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphsinputhandler.html#dragMode

    Returns
    -------

    QtGraphs3D.DragMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QtGraphs3D.DragMode(number)' gives.
    """
    #  QtGraphs3D::DragMode QGraphsInputHandler::dragMode()
    return QtGraphs3D.DragMode(self.uglySide.call(
        'ritual_ZN19QGraphsInputHandler8dragModeEv',
    ))

  def isSelectionEnabled(self) -> bool:
    """
    Calls Qt's 'bool QGraphsInputHandler::isSelectionEnabled()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphsinputhandler.html#isSelectionEnabled
    """
    #  bool QGraphsInputHandler::isSelectionEnabled()
    return self.uglySide.call(
        'ritual_ZN19QGraphsInputHandler18isSelectionEnabledEv',
    )

  def unsetDefaultInputHandler(self) -> None:
    """
    Calls Qt's 'void QGraphsInputHandler::unsetDefaultInputHandler()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphsinputhandler.html#unsetDefaultInputHandler
    """
    #  void QGraphsInputHandler::unsetDefaultInputHandler()
    self.uglySide.call(
        'ritual_ZN19QGraphsInputHandler24unsetDefaultInputHandlerEv',
    )

  def unsetDefaultTapHandler(self) -> None:
    """
    Calls Qt's 'void QGraphsInputHandler::unsetDefaultTapHandler()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphsinputhandler.html#unsetDefaultTapHandler
    """
    #  void QGraphsInputHandler::unsetDefaultTapHandler()
    self.uglySide.call(
        'ritual_ZN19QGraphsInputHandler22unsetDefaultTapHandlerEv',
    )

  def unsetDefaultDragHandler(self) -> None:
    """
    Calls Qt's 'void QGraphsInputHandler::unsetDefaultDragHandler()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphsinputhandler.html#unsetDefaultDragHandler
    """
    #  void QGraphsInputHandler::unsetDefaultDragHandler()
    self.uglySide.call(
        'ritual_ZN19QGraphsInputHandler23unsetDefaultDragHandlerEv',
    )

  def unsetDefaultWheelHandler(self) -> None:
    """
    Calls Qt's 'void QGraphsInputHandler::unsetDefaultWheelHandler()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphsinputhandler.html#unsetDefaultWheelHandler
    """
    #  void QGraphsInputHandler::unsetDefaultWheelHandler()
    self.uglySide.call(
        'ritual_ZN19QGraphsInputHandler24unsetDefaultWheelHandlerEv',
    )

  def unsetDefaultPinchHandler(self) -> None:
    """
    Calls Qt's 'void QGraphsInputHandler::unsetDefaultPinchHandler()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphsinputhandler.html#unsetDefaultPinchHandler
    """
    #  void QGraphsInputHandler::unsetDefaultPinchHandler()
    self.uglySide.call(
        'ritual_ZN19QGraphsInputHandler24unsetDefaultPinchHandlerEv',
    )

  def onTapped(self) -> None:
    """
    Calls Qt's 'void QGraphsInputHandler::onTapped()'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphsinputhandler.html#onTapped
    """
    #  void QGraphsInputHandler::onTapped()
    self.uglySide.call('ritual_ZN19QGraphsInputHandler8onTappedEv')

  @overload(QVector2D)
  def onTranslationChanged(self, delta: QVector2D) -> None:
    """
    Calls Qt's 'void QGraphsInputHandler::onTranslationChanged(QVector2D
    delta)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphsinputhandler.html#onTranslationChanged

    Parameters
    ----------

    delta : QVector2D
      Passed on as a value: Qt reads the C++ QVector2D, which stays Python's
      own.
    """
    #  void QGraphsInputHandler::onTranslationChanged(QVector2D delta)
    self.uglySide.call(
        'ritual_ZN19QGraphsInputHandler20onTranslationChangedE9QVector2D',
        self._valueOf(delta),
    )

  @overload(QPointingDevice.GrabTransition, QEventPoint)
  def onGrabChanged(
      self,
      transition: QPointingDevice.GrabTransition,
      point: QEventPoint,
  ) -> None:
    """
    Calls Qt's 'void
    QGraphsInputHandler::onGrabChanged(QPointingDevice::GrabTransition
    transition, QEventPoint point)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphsinputhandler.html#onGrabChanged

    Parameters
    ----------

    transition : QPointingDevice.GrabTransition
      Passed on as its number.

    point : QEventPoint
      Passed on as a value: Qt reads the C++ QEventPoint, which stays
      Python's own.
    """
    #  void
    #      QGraphsInputHandler::onGrabChanged(QPointingDevice::GrabTransition
    #      transition, QEventPoint point)
    self.uglySide.call(
        'ritual_ZN19QGraphsInputHandler13onGrabChangedEN15QPointingDevice14'
        'GrabTransitionE11QEventPoint',
        transition.value, self._valueOf(point),
    )

  @overload(QQuickWheelEvent)
  @overload(NoneType)
  def onWheel(self, event: Optional[QQuickWheelEvent]) -> None:
    """
    Calls Qt's 'void QGraphsInputHandler::onWheel(QQuickWheelEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphsinputhandler.html#onWheel

    Parameters
    ----------

    event : Optional[QQuickWheelEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphsInputHandler::onWheel(QQuickWheelEvent *event)
    self.uglySide.call(
        'ritual_ZN19QGraphsInputHandler7onWheelEP16QQuickWheelEvent',
        self._addressOf(event),
    )

  @overload(float)
  def onPinchScaleChanged(self, delta: float) -> None:
    """
    Calls Qt's 'void QGraphsInputHandler::onPinchScaleChanged(qreal delta)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphsinputhandler.html#onPinchScaleChanged

    Parameters
    ----------

    delta : float
      Passed on as it is.
    """
    #  void QGraphsInputHandler::onPinchScaleChanged(qreal delta)
    self.uglySide.call(
        'ritual_ZN19QGraphsInputHandler19onPinchScaleChangedEd', delta,
    )

  @overload(QPoint)
  def mouseMove(self, mousePos: QPoint) -> None:
    """
    Calls Qt's 'void QGraphsInputHandler::mouseMove(QPoint mousePos)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphsinputhandler.html#mouseMove

    Parameters
    ----------

    mousePos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void QGraphsInputHandler::mouseMove(QPoint mousePos)
    self.uglySide.call(
        'ritual_ZN19QGraphsInputHandler9mouseMoveE6QPoint',
        self._valueOf(mousePos),
    )

  @overload(QHoverEvent)
  @overload(NoneType)
  def hoverMoveEvent(self, event: Optional[QHoverEvent]) -> None:
    """
    Calls Qt's 'void QGraphsInputHandler::hoverMoveEvent(QHoverEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphsinputhandler.html#hoverMoveEvent

    Parameters
    ----------

    event : Optional[QHoverEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphsInputHandler::hoverMoveEvent(QHoverEvent *event)
    self.uglySide.call(
        'ritual_ZN19QGraphsInputHandler14hoverMoveEventEP11QHoverEvent',
        self._addressOf(event),
    )

  @staticmethod
  def setGraphsItem(*__, **_) -> Never:
    """
    Qt's 'void QGraphsInputHandler::setGraphsItem(QQuickGraphsItem *item)':
    leans on 'QGraphsInputHandler::staticMetaObject', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QGraphsInputHandler.setGraphsItem' has no cute function yet. Qt's "
        "'void QGraphsInputHandler::setGraphsItem(QQuickGraphsItem *item)': "
        "leans on 'QGraphsInputHandler::staticMetaObject', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")
