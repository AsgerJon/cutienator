"""
QSurface3DSeriesPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGraphs/6.12.0/QtGraphs/private/qsurface3dseries_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QSurface3DSeriesPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QAbstract3DSeriesPrivate, QSurface3DSeries

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QPoint
  from ..QtGui import QColor, QImage
  from . import QAbstractDataProxy, QQuickGraphsItem, QValue3DAxis
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAbstractDataProxy = WAIT['QtGraphs:QAbstractDataProxy']
  QColor = WAIT['QColor']
  QImage = WAIT['QImage']
  QPoint = WAIT['QPoint']
  QQuickGraphsItem = WAIT['QQuickGraphsItem']
  QValue3DAxis = WAIT['QtGraphs:QValue3DAxis']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSurface3DSeriesPrivate(QAbstract3DSeriesPrivate):
  """
  The cute side of Qt's QSurface3DSeriesPrivate: a plain Python object
  standing in front of one C++ QSurface3DSeriesPrivate.

  It is built on the cute 'QAbstract3DSeriesPrivate', as Qt's
  QSurface3DSeriesPrivate is built on Qt's QAbstract3DSeriesPrivate, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QSurface3DSeriesPrivate that has a ritual and that
  Python can call so far, 17 names in all: 'q_func', 'setDataProxy',
  'connectGraphAndProxy', 'createItemLabel', 'setSelectedPoint',
  'setDrawMode', 'setTexture', 'setWireframeColor', 'setRowsSanitized',
  'clearRow', 'clearArray', 'setAxisX', 'setAxisY', 'setAxisZ', 'resetAxisX',
  'resetAxisY', 'resetAxisZ'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QSurface3DSeries *QSurface3DSeriesPrivate::q_func() const':
    takes in Python what 'QSurface3DSeries
    *QSurface3DSeriesPrivate::q_func()' takes.
  - Qt's 'QSurface3DSeriesPrivate::~QSurface3DSeriesPrivate()': the
    destructor: Python never removes a C++ QSurface3DSeriesPrivate.
  - Qt's 'void QSurface3DSeriesPrivate::setShading(const
    QSurface3DSeries::Shading shading)': takes a type Python has no way to
    hand over yet.
  - Qt's 'void QSurface3DSeriesPrivate::setDataArray(const QSurfaceDataArray
    &newDataArray)': takes a type Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ QSurface3DSeriesPrivate is created at the first use, not by
    'QSurface3DSeriesPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSurface3DSeriesPrivate.
  - Each name of Qt's QSurface3DSeriesPrivate that has no cute function yet,
    'setDataArray', 'setShading', holds a function that raises
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
  __qt_class__ = 'QSurface3DSeriesPrivate'
  #  The part of Qt it is of, as another part has a class of its name too.
  __qt_part__ = 'QtGraphs'

  #  A C++ QSurface3DSeriesPrivate Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSurface3DSeriesPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QAbstractDataProxy)
  @overload(NoneType)
  def setDataProxy(self, proxy: Optional[QAbstractDataProxy]) -> None:
    """
    Calls Qt's 'void QSurface3DSeriesPrivate::setDataProxy(QAbstractDataProxy
    *proxy)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsurface3dseriesprivate.html#setDataProxy

    Parameters
    ----------

    proxy : Optional[QAbstractDataProxy]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSurface3DSeriesPrivate::setDataProxy(QAbstractDataProxy *proxy)
    ritual = (
        'ritual_ZN23QSurface3DSeriesPrivate12setDataProxyEP18QAbstractDataP'
        'roxy')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN23QSurface3DSeriesPrivate12setDataProxyEP18QAbstrac'
          'tDataProxy')
    self.uglySide.call(ritual, self._addressOf(proxy))

  @overload(QPoint)
  def setSelectedPoint(self, position: QPoint) -> None:
    """
    Calls Qt's 'void QSurface3DSeriesPrivate::setSelectedPoint(QPoint
    position)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsurface3dseriesprivate.html#setSelectedPoint

    Parameters
    ----------

    position : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void QSurface3DSeriesPrivate::setSelectedPoint(QPoint position)
    self.uglySide.call(
        'ritual_ZN23QSurface3DSeriesPrivate16setSelectedPointE6QPoint',
        self._valueOf(position),
    )

  @overload(QSurface3DSeries.DrawFlags)
  def setDrawMode(self, mode: QSurface3DSeries.DrawFlags) -> None:
    """
    Calls Qt's 'void
    QSurface3DSeriesPrivate::setDrawMode(QSurface3DSeries::DrawFlags mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsurface3dseriesprivate.html#setDrawMode

    Parameters
    ----------

    mode : QSurface3DSeries.DrawFlags
      Passed on as its number.
    """
    #  void QSurface3DSeriesPrivate::setDrawMode(QSurface3DSeries::DrawFlags
    #      mode)
    self.uglySide.call(
        'ritual_ZN23QSurface3DSeriesPrivate11setDrawModeE6QFlagsIN16QSurfac'
        'e3DSeries8DrawFlagEE',
        mode.value,
    )

  @overload(QImage)
  def setTexture(self, texture: QImage) -> None:
    """
    Calls Qt's 'void QSurface3DSeriesPrivate::setTexture(const QImage
    &texture)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsurface3dseriesprivate.html#setTexture

    Parameters
    ----------

    texture : QImage
      Passed on as a value: Qt reads the C++ QImage, which stays Python's
      own.
    """
    #  void QSurface3DSeriesPrivate::setTexture(const QImage &texture)
    self.uglySide.call(
        'ritual_ZN23QSurface3DSeriesPrivate10setTextureERK6QImage',
        self._valueOf(texture),
    )

  @overload(QColor)
  def setWireframeColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QSurface3DSeriesPrivate::setWireframeColor(QColor
    color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsurface3dseriesprivate.html#setWireframeColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QSurface3DSeriesPrivate::setWireframeColor(QColor color)
    self.uglySide.call(
        'ritual_ZN23QSurface3DSeriesPrivate17setWireframeColorE6QColor',
        self._valueOf(color),
    )

  @overload(bool)
  def setRowsSanitized(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QSurface3DSeriesPrivate::setRowsSanitized(bool
    enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsurface3dseriesprivate.html#setRowsSanitized

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QSurface3DSeriesPrivate::setRowsSanitized(bool enabled)
    self.uglySide.call(
        'ritual_ZN23QSurface3DSeriesPrivate16setRowsSanitizedEb', enabled,
    )

  @overload(QValue3DAxis)
  @overload(NoneType)
  def setAxisX(self, axis: Optional[QValue3DAxis]) -> None:
    """
    Calls Qt's 'void QSurface3DSeriesPrivate::setAxisX(QValue3DAxis *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsurface3dseriesprivate.html#setAxisX

    Parameters
    ----------

    axis : Optional[QValue3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSurface3DSeriesPrivate::setAxisX(QValue3DAxis *axis)
    self.uglySide.call(
        'ritual_ZN23QSurface3DSeriesPrivate8setAxisXEP12QValue3DAxis',
        self._addressOf(axis),
    )

  @overload(QValue3DAxis)
  @overload(NoneType)
  def setAxisY(self, axis: Optional[QValue3DAxis]) -> None:
    """
    Calls Qt's 'void QSurface3DSeriesPrivate::setAxisY(QValue3DAxis *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsurface3dseriesprivate.html#setAxisY

    Parameters
    ----------

    axis : Optional[QValue3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSurface3DSeriesPrivate::setAxisY(QValue3DAxis *axis)
    self.uglySide.call(
        'ritual_ZN23QSurface3DSeriesPrivate8setAxisYEP12QValue3DAxis',
        self._addressOf(axis),
    )

  @overload(QValue3DAxis)
  @overload(NoneType)
  def setAxisZ(self, axis: Optional[QValue3DAxis]) -> None:
    """
    Calls Qt's 'void QSurface3DSeriesPrivate::setAxisZ(QValue3DAxis *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsurface3dseriesprivate.html#setAxisZ

    Parameters
    ----------

    axis : Optional[QValue3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSurface3DSeriesPrivate::setAxisZ(QValue3DAxis *axis)
    self.uglySide.call(
        'ritual_ZN23QSurface3DSeriesPrivate8setAxisZEP12QValue3DAxis',
        self._addressOf(axis),
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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QSurface3DSeriesPrivate::QSurface3DSeriesPrivate()', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsurface3dseriesprivate.html
    """
    #  QSurface3DSeriesPrivate::QSurface3DSeriesPrivate()
    self._noteCreation(QSurface3DSeriesPrivate, lambda: Rituals.call(
        'ritual_ZN23QSurface3DSeriesPrivateC1Ev',
    ))

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

  def q_func(self) -> Optional[QSurface3DSeries]:
    """
    Calls Qt's 'QSurface3DSeries *QSurface3DSeriesPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsurface3dseriesprivate.html#q_func

    Returns
    -------

    Optional[QSurface3DSeries]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSurface3DSeries *QSurface3DSeriesPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN23QSurface3DSeriesPrivate6q_funcEv',
    )
    return QSurface3DSeries._cuteAt(address)

  @overload(QQuickGraphsItem)
  @overload(NoneType)
  def connectGraphAndProxy(
      self,
      newGraph: Optional[QQuickGraphsItem],
  ) -> None:
    """
    Calls Qt's 'void
    QSurface3DSeriesPrivate::connectGraphAndProxy(QQuickGraphsItem
    *newGraph)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsurface3dseriesprivate.html#connectGraphAndProxy

    Parameters
    ----------

    newGraph : Optional[QQuickGraphsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSurface3DSeriesPrivate::connectGraphAndProxy(QQuickGraphsItem
    #      *newGraph)
    ritual = (
        'ritual_ZN23QSurface3DSeriesPrivate20connectGraphAndProxyEP16QQuick'
        'GraphsItem')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN23QSurface3DSeriesPrivate20connectGraphAndProxyEP16'
          'QQuickGraphsItem')
    self.uglySide.call(ritual, self._addressOf(newGraph))

  def createItemLabel(self) -> None:
    """
    Calls Qt's 'void QSurface3DSeriesPrivate::createItemLabel()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsurface3dseriesprivate.html#createItemLabel
    """
    #  void QSurface3DSeriesPrivate::createItemLabel()
    ritual = 'ritual_ZN23QSurface3DSeriesPrivate15createItemLabelEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN23QSurface3DSeriesPrivate15createItemLabelEv'
    self.uglySide.call(ritual)

  @overload(int)
  def clearRow(self, rowIndex: int) -> None:
    """
    Calls Qt's 'void QSurface3DSeriesPrivate::clearRow(qsizetype rowIndex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsurface3dseriesprivate.html#clearRow

    Parameters
    ----------

    rowIndex : int
      Passed on as it is.
    """
    #  void QSurface3DSeriesPrivate::clearRow(qsizetype rowIndex)
    self.uglySide.call(
        'ritual_ZN23QSurface3DSeriesPrivate8clearRowEx', rowIndex,
    )

  def clearArray(self) -> None:
    """
    Calls Qt's 'void QSurface3DSeriesPrivate::clearArray()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsurface3dseriesprivate.html#clearArray
    """
    #  void QSurface3DSeriesPrivate::clearArray()
    self.uglySide.call('ritual_ZN23QSurface3DSeriesPrivate10clearArrayEv')

  def resetAxisX(self) -> None:
    """
    Calls Qt's 'void QSurface3DSeriesPrivate::resetAxisX()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsurface3dseriesprivate.html#resetAxisX
    """
    #  void QSurface3DSeriesPrivate::resetAxisX()
    self.uglySide.call('ritual_ZN23QSurface3DSeriesPrivate10resetAxisXEv')

  def resetAxisY(self) -> None:
    """
    Calls Qt's 'void QSurface3DSeriesPrivate::resetAxisY()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsurface3dseriesprivate.html#resetAxisY
    """
    #  void QSurface3DSeriesPrivate::resetAxisY()
    self.uglySide.call('ritual_ZN23QSurface3DSeriesPrivate10resetAxisYEv')

  def resetAxisZ(self) -> None:
    """
    Calls Qt's 'void QSurface3DSeriesPrivate::resetAxisZ()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsurface3dseriesprivate.html#resetAxisZ
    """
    #  void QSurface3DSeriesPrivate::resetAxisZ()
    self.uglySide.call('ritual_ZN23QSurface3DSeriesPrivate10resetAxisZEv')

  @staticmethod
  def setDataArray(*__, **_) -> Never:
    """
    Qt's 'void QSurface3DSeriesPrivate::setDataArray(const QSurfaceDataArray
    &newDataArray)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSurface3DSeriesPrivate.setDataArray' has no cute function yet. "
        "Qt's 'void QSurface3DSeriesPrivate::setDataArray(const "
        "QSurfaceDataArray &newDataArray)': takes a type Python has no way "
        "to hand over yet.")

  @staticmethod
  def setShading(*__, **_) -> Never:
    """
    Qt's 'void QSurface3DSeriesPrivate::setShading(const
    QSurface3DSeries::Shading shading)': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QSurface3DSeriesPrivate.setShading' has no cute function yet. "
        "Qt's 'void QSurface3DSeriesPrivate::setShading(const "
        "QSurface3DSeries::Shading shading)': takes a type Python has no "
        "way to hand over yet.")
