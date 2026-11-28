"""
AxisRenderer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGraphs/6.12.0/QtGraphs/private/axisrenderer_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means AxisRenderer to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtCore import Qt
from ..QtGui import QPointingDevice
from ..QtQuick import QQuickItem, QQuickText

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QEventPoint, QVector2D, QWheelEvent
  from . import QAbstractAxis, QGraphsTheme
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAbstractAxis = WAIT['QtGraphs:QAbstractAxis']
  QEventPoint = WAIT['QEventPoint']
  QVector2D = WAIT['QVector2D']
  QWheelEvent = WAIT['QWheelEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class AxisRenderer(QQuickItem):
  """
  The cute side of Qt's AxisRenderer: a plain Python object standing in front
  of one C++ AxisRenderer.

  It is built on the cute 'QQuickItem', as Qt's AxisRenderer is built on Qt's
  QQuickItem, and has everything that class has.

  What exists
  -----------

  Every function of Qt's AxisRenderer that has a ritual and that Python can
  call so far, 16 names in all: 'metaObject', 'initialize', 'handleWheel',
  'handlePinchScale', 'handlePinchGrab', 'updateAxisTitles',
  'deleteDragHandler', 'onTranslationChanged', 'onGrabChanged',
  'getValueStepsFromRange', 'getValueDecimalsFromRange',
  'setLabelTextProperties', 'windowToAxisCoords', 'calculateZoom', 'zoom',
  'theme'. None can be made from Python: one comes out of a function of
  another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *AxisRenderer::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int AxisRenderer::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'AxisRenderer::~AxisRenderer()': the destructor: Python never
    removes a C++ AxisRenderer.
  - Qt's 'bool AxisRenderer::hasAxisTitle(const AxisProperties &ax) const':
    takes a type Python has no way to hand over yet.
  - Qt's 'bool AxisRenderer::isAxisBottomOrRight(const AxisProperties &ax)
    const': takes a type Python has no way to hand over yet.
  - Qt's 'QString AxisRenderer::formatValueLabel(double number, int decimals,
    const QString &format, char defaultFormat) const': takes a single letter
    as C has it.
  - Qt's 'const AxisProperties &AxisRenderer::getAxisX(QAbstractSeries
    *series) const': gives a type Python has no way to take yet.
  - Qt's 'const AxisProperties &AxisRenderer::getAxisY(QAbstractSeries
    *series) const': gives a type Python has no way to take yet.

  What has no ritual
  ------------------

  22 of the 46 functions Qt declares: 11 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 4 leans on
  'AxisTicker; 3 leans on 'AxisRenderer; 2 not a gap; 2 leans on 'AxisGrid.

  What to expect
  --------------

  - The C++ AxisRenderer is created at the first use, not by
    'AxisRenderer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ AxisRenderer.
  - Qt tells when it has removed the C++ AxisRenderer. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  - Each name of Qt's AxisRenderer that has no cute function yet, '__init__',
    'createDragHandler', 'formatValueLabel', 'getAxisX', 'getAxisY',
    'handlePolish', 'hasAxisTitle', 'isAxisBottomOrRight',
    'populateAxisItems', 'updateAxis', 'updateAxisGrid',
    'updateAxisGridShadow', 'updateAxisLabelItems', 'updateAxisMeasurements',
    'updateAxisTickers', 'updateAxisTickersShadow', 'updateBarXAxisLabels',
    'updateBarYAxisLabels', 'updateDateTimeXAxisLabels',
    'updateDateTimeYAxisLabels', 'updateLogValueXAxisLabels',
    'updateLogValueYAxisLabels', 'updateValueXAxisLabels',
    'updateValueYAxisLabels', holds a function that raises
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
  __qt_class__ = 'AxisRenderer'

  #  A C++ AxisRenderer Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_AxisRenderer'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *AxisRenderer::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/axisrenderer.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *AxisRenderer::metaObject() const
    address = self.uglySide.call('ritual_ZNK12AxisRenderer10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload(float)
  def getValueStepsFromRange(self, range: float) -> float:
    """
    Calls Qt's 'double AxisRenderer::getValueStepsFromRange(double range)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/axisrenderer.html#getValueStepsFromRange

    Parameters
    ----------

    range : float
      Passed on as it is.
    """
    #  double AxisRenderer::getValueStepsFromRange(double range) const
    return self.uglySide.call(
        'ritual_ZNK12AxisRenderer22getValueStepsFromRangeEd', range,
    )

  @overload(float)
  def getValueDecimalsFromRange(self, range: float) -> int:
    """
    Calls Qt's 'int AxisRenderer::getValueDecimalsFromRange(double range)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/axisrenderer.html#getValueDecimalsFromRange

    Parameters
    ----------

    range : float
      Passed on as it is.
    """
    #  int AxisRenderer::getValueDecimalsFromRange(double range) const
    return self.uglySide.call(
        'ritual_ZNK12AxisRenderer25getValueDecimalsFromRangeEd', range,
    )

  def theme(self) -> Optional[QGraphsTheme]:
    """
    Calls Qt's 'QGraphsTheme *AxisRenderer::theme() const'.

    Qt's own words: https://doc.qt.io/qt-6/axisrenderer.html#theme

    Returns
    -------

    Optional[QGraphsTheme]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGraphsTheme *AxisRenderer::theme() const
    address = self.uglySide.call('ritual_ZNK12AxisRenderer5themeEv')
    from . import QGraphsTheme
    return QGraphsTheme._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QQuickItem, str, bool)
  @overload(NoneType, str, bool)
  @overload(QQuickItem, str, bool, QQuickText.HAlignment)
  @overload(NoneType, str, bool, QQuickText.HAlignment)
  @overload(
      QQuickItem, str, bool, QQuickText.HAlignment, QQuickText.VAlignment,
  )
  @overload(
      NoneType, str, bool, QQuickText.HAlignment, QQuickText.VAlignment,
  )
  @overload(
      QQuickItem, str, bool, QQuickText.HAlignment, QQuickText.VAlignment,
      Qt.TextElideMode,
  )
  @overload(
      NoneType, str, bool, QQuickText.HAlignment, QQuickText.VAlignment,
      Qt.TextElideMode,
  )
  def setLabelTextProperties(
      self,
      item: Optional[QQuickItem],
      text: str,
      xAxis: bool,
      hAlign: QQuickText.HAlignment = QQuickText.HAlignment.AlignHCenter,
      vAlign: QQuickText.VAlignment = QQuickText.VAlignment.AlignVCenter,
      elide: Qt.TextElideMode = Qt.TextElideMode.ElideNone,
  ) -> None:
    """
    Calls Qt's 'void AxisRenderer::setLabelTextProperties(QQuickItem *item,
    const QString &text, bool xAxis, QQuickText::HAlignment hAlign,
    QQuickText::VAlignment vAlign, Qt::TextElideMode elide)'.

    Qt's own words:
    https://doc.qt.io/qt-6/axisrenderer.html#setLabelTextProperties

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    text : str
      Passed on as it is: a QString is made of it for the call.

    xAxis : bool
      Passed on as it is.

    hAlign : QQuickText.HAlignment
      Passed on as its number. May be left out, as in Qt: it is then
      QQuickText.HAlignment.AlignHCenter.

    vAlign : QQuickText.VAlignment
      Passed on as its number. May be left out, as in Qt: it is then
      QQuickText.VAlignment.AlignVCenter.

    elide : Qt.TextElideMode
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.TextElideMode.ElideNone.
    """
    #  void AxisRenderer::setLabelTextProperties(QQuickItem *item, const
    #      QString &text, bool xAxis, QQuickText::HAlignment hAlign,
    #      QQuickText::VAlignment vAlign, Qt::TextElideMode elide)
    self.uglySide.call(
        'ritual_ZN12AxisRenderer22setLabelTextPropertiesEP10QQuickItemRK7QS'
        'tringbN10QQuickText10HAlignmentENS5_10VAlignmentEN2Qt13TextElideMo'
        'deE',
        self._addressOf(item), text, xAxis, hAlign.value, vAlign.value,
        elide.value,
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
    Qt's 'AxisRenderer::AxisRenderer(QQuickItem *parent)': leans on
    'AxisRenderer::qt_metacall(QMetaObject::Call, int, void**)', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'AxisRenderer.__init__' has no cute function yet. Qt's "
        "'AxisRenderer::AxisRenderer(QQuickItem *parent)': leans on "
        "'AxisRenderer::qt_metacall(QMetaObject::Call, int, void**)', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

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

  def initialize(self) -> None:
    """
    Calls Qt's 'void AxisRenderer::initialize()'.

    Qt's own words: https://doc.qt.io/qt-6/axisrenderer.html#initialize
    """
    #  void AxisRenderer::initialize()
    self.uglySide.call('ritual_ZN12AxisRenderer10initializeEv')

  @overload(QWheelEvent)
  @overload(NoneType)
  def handleWheel(self, event: Optional[QWheelEvent]) -> bool:
    """
    Calls Qt's 'bool AxisRenderer::handleWheel(QWheelEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/axisrenderer.html#handleWheel

    Parameters
    ----------

    event : Optional[QWheelEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool AxisRenderer::handleWheel(QWheelEvent *event)
    return self.uglySide.call(
        'ritual_ZN12AxisRenderer11handleWheelEP11QWheelEvent',
        self._addressOf(event),
    )

  @overload(float)
  def handlePinchScale(self, delta: float) -> None:
    """
    Calls Qt's 'void AxisRenderer::handlePinchScale(qreal delta)'.

    Qt's own words: https://doc.qt.io/qt-6/axisrenderer.html#handlePinchScale

    Parameters
    ----------

    delta : float
      Passed on as it is.
    """
    #  void AxisRenderer::handlePinchScale(qreal delta)
    self.uglySide.call('ritual_ZN12AxisRenderer16handlePinchScaleEd', delta)

  @overload(QPointingDevice.GrabTransition, QEventPoint)
  def handlePinchGrab(
      self,
      transition: QPointingDevice.GrabTransition,
      point: QEventPoint,
  ) -> None:
    """
    Calls Qt's 'void
    AxisRenderer::handlePinchGrab(QPointingDevice::GrabTransition transition,
    QEventPoint point)'.

    Qt's own words: https://doc.qt.io/qt-6/axisrenderer.html#handlePinchGrab

    Parameters
    ----------

    transition : QPointingDevice.GrabTransition
      Passed on as its number.

    point : QEventPoint
      Passed on as a value: Qt reads the C++ QEventPoint, which stays
      Python's own.
    """
    #  void AxisRenderer::handlePinchGrab(QPointingDevice::GrabTransition
    #      transition, QEventPoint point)
    self.uglySide.call(
        'ritual_ZN12AxisRenderer15handlePinchGrabEN15QPointingDevice14GrabT'
        'ransitionE11QEventPoint',
        transition.value, self._valueOf(point),
    )

  def updateAxisTitles(self) -> None:
    """
    Calls Qt's 'void AxisRenderer::updateAxisTitles()'.

    Qt's own words: https://doc.qt.io/qt-6/axisrenderer.html#updateAxisTitles
    """
    #  void AxisRenderer::updateAxisTitles()
    self.uglySide.call('ritual_ZN12AxisRenderer16updateAxisTitlesEv')

  def deleteDragHandler(self) -> None:
    """
    Calls Qt's 'void AxisRenderer::deleteDragHandler()'.

    Qt's own words:
    https://doc.qt.io/qt-6/axisrenderer.html#deleteDragHandler
    """
    #  void AxisRenderer::deleteDragHandler()
    self.uglySide.call('ritual_ZN12AxisRenderer17deleteDragHandlerEv')

  @overload(QVector2D)
  def onTranslationChanged(self, delta: QVector2D) -> None:
    """
    Calls Qt's 'void AxisRenderer::onTranslationChanged(QVector2D delta)'.

    Qt's own words:
    https://doc.qt.io/qt-6/axisrenderer.html#onTranslationChanged

    Parameters
    ----------

    delta : QVector2D
      Passed on as a value: Qt reads the C++ QVector2D, which stays Python's
      own.
    """
    #  void AxisRenderer::onTranslationChanged(QVector2D delta)
    self.uglySide.call(
        'ritual_ZN12AxisRenderer20onTranslationChangedE9QVector2D',
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
    AxisRenderer::onGrabChanged(QPointingDevice::GrabTransition transition,
    QEventPoint point)'.

    Qt's own words: https://doc.qt.io/qt-6/axisrenderer.html#onGrabChanged

    Parameters
    ----------

    transition : QPointingDevice.GrabTransition
      Passed on as its number.

    point : QEventPoint
      Passed on as a value: Qt reads the C++ QEventPoint, which stays
      Python's own.
    """
    #  void AxisRenderer::onGrabChanged(QPointingDevice::GrabTransition
    #      transition, QEventPoint point)
    self.uglySide.call(
        'ritual_ZN12AxisRenderer13onGrabChangedEN15QPointingDevice14GrabTra'
        'nsitionE11QEventPoint',
        transition.value, self._valueOf(point),
    )

  @overload(QVector2D)
  def windowToAxisCoords(self, coords: QVector2D) -> QVector2D:
    """
    Calls Qt's 'QVector2D AxisRenderer::windowToAxisCoords(QVector2D
    coords)'.

    Qt's own words:
    https://doc.qt.io/qt-6/axisrenderer.html#windowToAxisCoords

    Parameters
    ----------

    coords : QVector2D
      Passed on as a value: Qt reads the C++ QVector2D, which stays Python's
      own.

    Returns
    -------

    QVector2D
      A new cute QVector2D around the copy Qt gave back. Python owns it.
    """
    #  QVector2D AxisRenderer::windowToAxisCoords(QVector2D coords)
    address = self.uglySide.call(
        'ritual_ZN12AxisRenderer18windowToAxisCoordsE9QVector2D',
        self._valueOf(coords),
    )
    from ..QtGui import QVector2D
    return QVector2D._cuteOwning(address)

  @overload(QAbstractAxis, float)
  @overload(NoneType, float)
  def calculateZoom(
      self,
      axis: Optional[QAbstractAxis],
      delta: float,
  ) -> bool:
    """
    Calls Qt's 'bool AxisRenderer::calculateZoom(QAbstractAxis *axis, qreal
    delta)'.

    Qt's own words: https://doc.qt.io/qt-6/axisrenderer.html#calculateZoom

    Parameters
    ----------

    axis : Optional[QAbstractAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    delta : float
      Passed on as it is.
    """
    #  bool AxisRenderer::calculateZoom(QAbstractAxis *axis, qreal delta)
    return self.uglySide.call(
        'ritual_ZN12AxisRenderer13calculateZoomEP13QAbstractAxisd',
        self._addressOf(axis), delta,
    )

  @overload(float)
  def zoom(self, delta: float) -> bool:
    """
    Calls Qt's 'bool AxisRenderer::zoom(qreal delta)'.

    Qt's own words: https://doc.qt.io/qt-6/axisrenderer.html#zoom

    Parameters
    ----------

    delta : float
      Passed on as it is.
    """
    #  bool AxisRenderer::zoom(qreal delta)
    return self.uglySide.call('ritual_ZN12AxisRenderer4zoomEd', delta)

  @staticmethod
  def createDragHandler(*__, **_) -> Never:
    """
    Qt's 'void AxisRenderer::createDragHandler()': leans on
    'AxisRenderer::staticMetaObject', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'AxisRenderer.createDragHandler' has no cute function yet. Qt's "
        "'void AxisRenderer::createDragHandler()': leans on "
        "'AxisRenderer::staticMetaObject', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def formatValueLabel(*__, **_) -> Never:
    """
    Qt's 'QString AxisRenderer::formatValueLabel(double number, int decimals,
    const QString &format, char defaultFormat) const': takes a single letter
    as C has it.
    """
    raise NotImplementedError(
        "'AxisRenderer.formatValueLabel' has no cute function yet. Qt's "
        "'QString AxisRenderer::formatValueLabel(double number, int "
        "decimals, const QString &format, char defaultFormat) const': takes "
        "a single letter as C has it.")

  @staticmethod
  def getAxisX(*__, **_) -> Never:
    """
    Qt's 'const AxisProperties &AxisRenderer::getAxisX(QAbstractSeries
    *series) const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'AxisRenderer.getAxisX' has no cute function yet. Qt's 'const "
        "AxisProperties &AxisRenderer::getAxisX(QAbstractSeries *series) "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def getAxisY(*__, **_) -> Never:
    """
    Qt's 'const AxisProperties &AxisRenderer::getAxisY(QAbstractSeries
    *series) const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'AxisRenderer.getAxisY' has no cute function yet. Qt's 'const "
        "AxisProperties &AxisRenderer::getAxisY(QAbstractSeries *series) "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def handlePolish(*__, **_) -> Never:
    """
    Qt's 'void AxisRenderer::handlePolish()': Qt's library has no name for
    it, and its code in Qt's source does not compile apart from its file: use
    of undeclared identifier 'QGraphs2DAxisRendererHandlePolish'.
    """
    raise NotImplementedError(
        "'AxisRenderer.handlePolish' has no cute function yet. Qt's 'void "
        "AxisRenderer::handlePolish()': Qt's library has no name for it, "
        "and its code in Qt's source does not compile apart from its file: "
        "use of undeclared identifier 'QGraphs2DAxisRendererHandlePolish'.")

  @staticmethod
  def hasAxisTitle(*__, **_) -> Never:
    """
    Qt's 'bool AxisRenderer::hasAxisTitle(const AxisProperties &ax) const':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'AxisRenderer.hasAxisTitle' has no cute function yet. Qt's 'bool "
        "AxisRenderer::hasAxisTitle(const AxisProperties &ax) const': takes "
        "a type Python has no way to hand over yet.")

  @staticmethod
  def isAxisBottomOrRight(*__, **_) -> Never:
    """
    Qt's 'bool AxisRenderer::isAxisBottomOrRight(const AxisProperties &ax)
    const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'AxisRenderer.isAxisBottomOrRight' has no cute function yet. Qt's "
        "'bool AxisRenderer::isAxisBottomOrRight(const AxisProperties &ax) "
        "const': takes a type Python has no way to hand over yet.")

  @staticmethod
  def populateAxisItems(*__, **_) -> Never:
    """
    Qt's 'void AxisRenderer::populateAxisItems()': leans on
    'AxisTicker::origoChanged()', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'AxisRenderer.populateAxisItems' has no cute function yet. Qt's "
        "'void AxisRenderer::populateAxisItems()': leans on "
        "'AxisTicker::origoChanged()', which Qt's source does not mark for "
        "use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def updateAxis(*__, **_) -> Never:
    """
    Qt's 'void AxisRenderer::updateAxis()': Qt's library has no name for it,
    and its code in Qt's source does not compile apart from its file: use of
    undeclared identifier 'QGraphs2DAxisRendererUpdateAxis'.
    """
    raise NotImplementedError(
        "'AxisRenderer.updateAxis' has no cute function yet. Qt's 'void "
        "AxisRenderer::updateAxis()': Qt's library has no name for it, and "
        "its code in Qt's source does not compile apart from its file: use "
        "of undeclared identifier 'QGraphs2DAxisRendererUpdateAxis'.")

  @staticmethod
  def updateAxisGrid(*__, **_) -> Never:
    """
    Qt's 'void AxisRenderer::updateAxisGrid()': leans on
    'AxisGrid::gridColorChanged()', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'AxisRenderer.updateAxisGrid' has no cute function yet. Qt's 'void "
        "AxisRenderer::updateAxisGrid()': leans on "
        "'AxisGrid::gridColorChanged()', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def updateAxisGridShadow(*__, **_) -> Never:
    """
    Qt's 'void AxisRenderer::updateAxisGridShadow()': leans on
    'AxisGrid::gridColorChanged()', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'AxisRenderer.updateAxisGridShadow' has no cute function yet. Qt's "
        "'void AxisRenderer::updateAxisGridShadow()': leans on "
        "'AxisGrid::gridColorChanged()', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def updateAxisLabelItems(*__, **_) -> Never:
    """
    Qt's 'void AxisRenderer::updateAxisLabelItems(QList<QQuickItem *>
    &textItems, qsizetype neededSize, QQmlComponent *component)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier
    'QGraphs2DAxisRendererUpdateAxisLabelItems'.
    """
    raise NotImplementedError(
        "'AxisRenderer.updateAxisLabelItems' has no cute function yet. Qt's "
        "'void AxisRenderer::updateAxisLabelItems(QList<QQuickItem *> "
        "&textItems, qsizetype neededSize, QQmlComponent *component)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'QGraphs2DAxisRendererUpdateAxisLabelItems'.")

  @staticmethod
  def updateAxisMeasurements(*__, **_) -> Never:
    """
    Qt's 'void AxisRenderer::updateAxisMeasurements()': leans on
    'AxisTicker::origoChanged()', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'AxisRenderer.updateAxisMeasurements' has no cute function yet. "
        "Qt's 'void AxisRenderer::updateAxisMeasurements()': leans on "
        "'AxisTicker::origoChanged()', which Qt's source does not mark for "
        "use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def updateAxisTickers(*__, **_) -> Never:
    """
    Qt's 'void AxisRenderer::updateAxisTickers()': leans on
    'AxisTicker::baseChanged()', which Qt's source does not mark for use from
    outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'AxisRenderer.updateAxisTickers' has no cute function yet. Qt's "
        "'void AxisRenderer::updateAxisTickers()': leans on "
        "'AxisTicker::baseChanged()', which Qt's source does not mark for "
        "use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def updateAxisTickersShadow(*__, **_) -> Never:
    """
    Qt's 'void AxisRenderer::updateAxisTickersShadow()': leans on
    'AxisTicker::baseChanged()', which Qt's source does not mark for use from
    outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'AxisRenderer.updateAxisTickersShadow' has no cute function yet. "
        "Qt's 'void AxisRenderer::updateAxisTickersShadow()': leans on "
        "'AxisTicker::baseChanged()', which Qt's source does not mark for "
        "use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def updateBarXAxisLabels(*__, **_) -> Never:
    """
    Qt's 'void AxisRenderer::updateBarXAxisLabels(AxisProperties &ax, const
    QRectF rect)': Qt's library has no name for it, and its code in Qt's
    source does not compile apart from its file: use of undeclared identifier
    'QGraphs2DAxisRendererUpdateBarXAxisLabels'.
    """
    raise NotImplementedError(
        "'AxisRenderer.updateBarXAxisLabels' has no cute function yet. Qt's "
        "'void AxisRenderer::updateBarXAxisLabels(AxisProperties &ax, const "
        "QRectF rect)': Qt's library has no name for it, and its code in "
        "Qt's source does not compile apart from its file: use of "
        "undeclared identifier 'QGraphs2DAxisRendererUpdateBarXAxisLabels'.")

  @staticmethod
  def updateBarYAxisLabels(*__, **_) -> Never:
    """
    Qt's 'void AxisRenderer::updateBarYAxisLabels(AxisProperties &ax, const
    QRectF rect)': Qt's library has no name for it, and its code in Qt's
    source does not compile apart from its file: use of undeclared identifier
    'QGraphs2DAxisRendererUpdateBarYAxisLabels'.
    """
    raise NotImplementedError(
        "'AxisRenderer.updateBarYAxisLabels' has no cute function yet. Qt's "
        "'void AxisRenderer::updateBarYAxisLabels(AxisProperties &ax, const "
        "QRectF rect)': Qt's library has no name for it, and its code in "
        "Qt's source does not compile apart from its file: use of "
        "undeclared identifier 'QGraphs2DAxisRendererUpdateBarYAxisLabels'.")

  @staticmethod
  def updateDateTimeXAxisLabels(*__, **_) -> Never:
    """
    Qt's 'void AxisRenderer::updateDateTimeXAxisLabels(AxisProperties &ax,
    const QRectF rect)': Qt's library has no name for it, and its code in
    Qt's source does not compile apart from its file: use of undeclared
    identifier 'QGraphs2DAxisRendererUpdateDateTimeXAxisLabels'.
    """
    raise NotImplementedError(
        "'AxisRenderer.updateDateTimeXAxisLabels' has no cute function yet. "
        "Qt's 'void AxisRenderer::updateDateTimeXAxisLabels(AxisProperties "
        "&ax, const QRectF rect)': Qt's library has no name for it, and its "
        "code in Qt's source does not compile apart from its file: use of "
        "undeclared identifier "
        "'QGraphs2DAxisRendererUpdateDateTimeXAxisLabels'.")

  @staticmethod
  def updateDateTimeYAxisLabels(*__, **_) -> Never:
    """
    Qt's 'void AxisRenderer::updateDateTimeYAxisLabels(AxisProperties &ax,
    const QRectF rect)': Qt's library has no name for it, and its code in
    Qt's source does not compile apart from its file: use of undeclared
    identifier 'QGraphs2DAxisRendererUpdateDateTimeYAxisLabels'.
    """
    raise NotImplementedError(
        "'AxisRenderer.updateDateTimeYAxisLabels' has no cute function yet. "
        "Qt's 'void AxisRenderer::updateDateTimeYAxisLabels(AxisProperties "
        "&ax, const QRectF rect)': Qt's library has no name for it, and its "
        "code in Qt's source does not compile apart from its file: use of "
        "undeclared identifier "
        "'QGraphs2DAxisRendererUpdateDateTimeYAxisLabels'.")

  @staticmethod
  def updateLogValueXAxisLabels(*__, **_) -> Never:
    """
    Qt's 'void AxisRenderer::updateLogValueXAxisLabels(AxisProperties &ax,
    const QRectF rect)': Qt's library has no name for it, and its code in
    Qt's source does not compile apart from its file: use of undeclared
    identifier 'QGraphs2DAxisRendererUpdateLogValueXAxisLabels'.
    """
    raise NotImplementedError(
        "'AxisRenderer.updateLogValueXAxisLabels' has no cute function yet. "
        "Qt's 'void AxisRenderer::updateLogValueXAxisLabels(AxisProperties "
        "&ax, const QRectF rect)': Qt's library has no name for it, and its "
        "code in Qt's source does not compile apart from its file: use of "
        "undeclared identifier "
        "'QGraphs2DAxisRendererUpdateLogValueXAxisLabels'.")

  @staticmethod
  def updateLogValueYAxisLabels(*__, **_) -> Never:
    """
    Qt's 'void AxisRenderer::updateLogValueYAxisLabels(AxisProperties &ax,
    const QRectF rect)': Qt's library has no name for it, and its code in
    Qt's source does not compile apart from its file: use of undeclared
    identifier 'QGraphs2DAxisRendererUpdateLogValueYAxisLabels'.
    """
    raise NotImplementedError(
        "'AxisRenderer.updateLogValueYAxisLabels' has no cute function yet. "
        "Qt's 'void AxisRenderer::updateLogValueYAxisLabels(AxisProperties "
        "&ax, const QRectF rect)': Qt's library has no name for it, and its "
        "code in Qt's source does not compile apart from its file: use of "
        "undeclared identifier "
        "'QGraphs2DAxisRendererUpdateLogValueYAxisLabels'.")

  @staticmethod
  def updateValueXAxisLabels(*__, **_) -> Never:
    """
    Qt's 'void AxisRenderer::updateValueXAxisLabels(AxisProperties &ax, const
    QRectF rect)': Qt's library has no name for it, and its code in Qt's
    source does not compile apart from its file: use of undeclared identifier
    'QGraphs2DAxisRendererUpdateValueXAxisLabels'.
    """
    raise NotImplementedError(
        "'AxisRenderer.updateValueXAxisLabels' has no cute function yet. "
        "Qt's 'void AxisRenderer::updateValueXAxisLabels(AxisProperties "
        "&ax, const QRectF rect)': Qt's library has no name for it, and its "
        "code in Qt's source does not compile apart from its file: use of "
        "undeclared identifier "
        "'QGraphs2DAxisRendererUpdateValueXAxisLabels'.")

  @staticmethod
  def updateValueYAxisLabels(*__, **_) -> Never:
    """
    Qt's 'void AxisRenderer::updateValueYAxisLabels(AxisProperties &ax, const
    QRectF rect)': Qt's library has no name for it, and its code in Qt's
    source does not compile apart from its file: use of undeclared identifier
    'QGraphs2DAxisRendererUpdateValueYAxisLabels'.
    """
    raise NotImplementedError(
        "'AxisRenderer.updateValueYAxisLabels' has no cute function yet. "
        "Qt's 'void AxisRenderer::updateValueYAxisLabels(AxisProperties "
        "&ax, const QRectF rect)': Qt's library has no name for it, and its "
        "code in Qt's source does not compile apart from its file: use of "
        "undeclared identifier "
        "'QGraphs2DAxisRendererUpdateValueYAxisLabels'.")
