"""
DeclarativeCandlestickSeries binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtChartsQml/6.12.0/QtChartsQml/private/declarativecandlestickseries_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means DeclarativeCandlestickSeries to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtQml import QQmlParserStatus
from ..QtCharts import QCandlestickSeries

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from ..QtCharts import QAbstractAxis, QCandlestickSet
  from . import DeclarativeCandlestickSet
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  DeclarativeCandlestickSet = WAIT['DeclarativeCandlestickSet']
  QAbstractAxis = WAIT['QtCharts:QAbstractAxis']
  QCandlestickSet = WAIT['QCandlestickSet']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class DeclarativeCandlestickSeries(QCandlestickSeries, QQmlParserStatus):
  """
  The cute side of Qt's DeclarativeCandlestickSeries: a plain Python object
  standing in front of one C++ DeclarativeCandlestickSeries.

  It is built on the cute 'QCandlestickSeries', as Qt's
  DeclarativeCandlestickSeries is built on Qt's QCandlestickSeries, and has
  everything that class has. It is built on the cute 'QQmlParserStatus' as
  well, as Qt's DeclarativeCandlestickSeries is built on Qt's
  QQmlParserStatus too, and has everything that class has.

  What exists
  -----------

  Every function of Qt's DeclarativeCandlestickSeries that has a ritual and
  that Python can call so far, 33 names in all: 'metaObject', 'setAxisX',
  'axisX', 'setAxisY', 'axisY', 'setAxisXTop', 'axisXTop', 'setAxisYRight',
  'axisYRight', 'brushFilename', 'at', 'append', 'remove', 'insert', 'clear',
  'classBegin', 'componentComplete', 'axisXChanged', 'axisYChanged',
  'axisXTopChanged', 'axisYRightChanged', 'clicked', 'hovered', 'pressed',
  'released', 'doubleClicked', 'brushFilenameChanged', 'onClicked',
  'onHovered', 'onPressed', 'onReleased', 'onDoubleClicked',
  'handleBrushChanged'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *DeclarativeCandlestickSeries::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int DeclarativeCandlestickSeries::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QQmlListProperty<QObject>
    DeclarativeCandlestickSeries::seriesChildren()': gives a type Python has
    no way to take yet.
  - Qt's 'void DeclarativeCandlestickSeries::appendSeriesChildren(
    QQmlListProperty<QObject> *list, QObject *element)': names
    'QQmlListProperty<QObject>', which has no cute class yet.

  What has no ritual
  ------------------

  5 of the 44 functions Qt declares: 2 not a gap; 2 leans on
  'DeclarativeCandlestickSeries; 1 leans on 'vtable for
  DeclarativeCandlestickSeries', which Qt's source does not mark for use from
  outside Qt and has no code for that could be taken.

  What to expect
  --------------

  - The C++ DeclarativeCandlestickSeries is created at the first use, not by
    'DeclarativeCandlestickSeries(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ DeclarativeCandlestickSeries.
  - Qt tells when it has removed the C++ DeclarativeCandlestickSeries. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's DeclarativeCandlestickSeries that has no cute function
    yet, '__init__', 'appendSeriesChildren', 'seriesChildren',
    'setBrushFilename', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'DeclarativeCandlestickSeries'

  #  Qt's DeclarativeCandlestickSeries is built on more than one class. The
  #  part of a C++ DeclarativeCandlestickSeries that belongs to a class after
  #  the first begins somewhere inside the object, and the ritual named for
  #  that class gives where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QQmlParserStatus':
          'ritual_cast_DeclarativeCandlestickSeries_QQmlParserStatus',
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *DeclarativeCandlestickSeries::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativecandlestickseries.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *DeclarativeCandlestickSeries::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK28DeclarativeCandlestickSeries10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def brushFilename(self) -> str:
    """
    Calls Qt's 'QString DeclarativeCandlestickSeries::brushFilename() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativecandlestickseries.html#brushFilename

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString DeclarativeCandlestickSeries::brushFilename() const
    return self.uglySide.call(
        'ritual_ZNK28DeclarativeCandlestickSeries13brushFilenameEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QAbstractAxis)
  @overload(NoneType)
  def setAxisX(self, axis: Optional[QAbstractAxis]) -> None:
    """
    Calls Qt's 'void DeclarativeCandlestickSeries::setAxisX(QAbstractAxis
    *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativecandlestickseries.html#setAxisX

    Parameters
    ----------

    axis : Optional[QAbstractAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DeclarativeCandlestickSeries::setAxisX(QAbstractAxis *axis)
    self.uglySide.call(
        'ritual_ZN28DeclarativeCandlestickSeries8setAxisXEP13QAbstractAxis',
        self._addressOf(axis),
    )

  @overload(QAbstractAxis)
  @overload(NoneType)
  def setAxisY(self, axis: Optional[QAbstractAxis]) -> None:
    """
    Calls Qt's 'void DeclarativeCandlestickSeries::setAxisY(QAbstractAxis
    *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativecandlestickseries.html#setAxisY

    Parameters
    ----------

    axis : Optional[QAbstractAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DeclarativeCandlestickSeries::setAxisY(QAbstractAxis *axis)
    self.uglySide.call(
        'ritual_ZN28DeclarativeCandlestickSeries8setAxisYEP13QAbstractAxis',
        self._addressOf(axis),
    )

  @overload(QAbstractAxis)
  @overload(NoneType)
  def setAxisXTop(self, axis: Optional[QAbstractAxis]) -> None:
    """
    Calls Qt's 'void DeclarativeCandlestickSeries::setAxisXTop(QAbstractAxis
    *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativecandlestickseries.html#setAxisXTop

    Parameters
    ----------

    axis : Optional[QAbstractAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DeclarativeCandlestickSeries::setAxisXTop(QAbstractAxis *axis)
    self.uglySide.call(
        'ritual_ZN28DeclarativeCandlestickSeries11setAxisXTopEP13QAbstractA'
        'xis',
        self._addressOf(axis),
    )

  @overload(QAbstractAxis)
  @overload(NoneType)
  def setAxisYRight(self, axis: Optional[QAbstractAxis]) -> None:
    """
    Calls Qt's 'void
    DeclarativeCandlestickSeries::setAxisYRight(QAbstractAxis *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativecandlestickseries.html#setAxisYRight

    Parameters
    ----------

    axis : Optional[QAbstractAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DeclarativeCandlestickSeries::setAxisYRight(QAbstractAxis *axis)
    self.uglySide.call(
        'ritual_ZN28DeclarativeCandlestickSeries13setAxisYRightEP13QAbstrac'
        'tAxis',
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's
    'DeclarativeCandlestickSeries::DeclarativeCandlestickSeries(QQuickItem
    *parent)': leans on 'vtable for DeclarativeCandlestickSeries', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'DeclarativeCandlestickSeries.__init__' has no cute function yet. "
        "Qt's "
        "'DeclarativeCandlestickSeries::DeclarativeCandlestickSeries(QQuickI"
        "tem *parent)': leans on 'vtable for DeclarativeCandlestickSeries', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

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

  def axisX(self) -> Optional[QAbstractAxis]:
    """
    Calls Qt's 'QAbstractAxis *DeclarativeCandlestickSeries::axisX()'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativecandlestickseries.html#axisX

    Returns
    -------

    Optional[QAbstractAxis]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractAxis *DeclarativeCandlestickSeries::axisX()
    address = self.uglySide.call(
        'ritual_ZN28DeclarativeCandlestickSeries5axisXEv',
    )
    from ..QtCharts import QAbstractAxis
    return QAbstractAxis._cuteAt(address)

  def axisY(self) -> Optional[QAbstractAxis]:
    """
    Calls Qt's 'QAbstractAxis *DeclarativeCandlestickSeries::axisY()'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativecandlestickseries.html#axisY

    Returns
    -------

    Optional[QAbstractAxis]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractAxis *DeclarativeCandlestickSeries::axisY()
    address = self.uglySide.call(
        'ritual_ZN28DeclarativeCandlestickSeries5axisYEv',
    )
    from ..QtCharts import QAbstractAxis
    return QAbstractAxis._cuteAt(address)

  def axisXTop(self) -> Optional[QAbstractAxis]:
    """
    Calls Qt's 'QAbstractAxis *DeclarativeCandlestickSeries::axisXTop()'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativecandlestickseries.html#axisXTop

    Returns
    -------

    Optional[QAbstractAxis]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractAxis *DeclarativeCandlestickSeries::axisXTop()
    address = self.uglySide.call(
        'ritual_ZN28DeclarativeCandlestickSeries8axisXTopEv',
    )
    from ..QtCharts import QAbstractAxis
    return QAbstractAxis._cuteAt(address)

  def axisYRight(self) -> Optional[QAbstractAxis]:
    """
    Calls Qt's 'QAbstractAxis *DeclarativeCandlestickSeries::axisYRight()'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativecandlestickseries.html#axisYRight

    Returns
    -------

    Optional[QAbstractAxis]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractAxis *DeclarativeCandlestickSeries::axisYRight()
    address = self.uglySide.call(
        'ritual_ZN28DeclarativeCandlestickSeries10axisYRightEv',
    )
    from ..QtCharts import QAbstractAxis
    return QAbstractAxis._cuteAt(address)

  @overload(int)
  def at(self, index: int) -> Optional[DeclarativeCandlestickSet]:
    """
    Calls Qt's 'DeclarativeCandlestickSet
    *DeclarativeCandlestickSeries::at(int index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativecandlestickseries.html#at

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    Optional[DeclarativeCandlestickSet]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DeclarativeCandlestickSet *DeclarativeCandlestickSeries::at(int index)
    address = self.uglySide.call(
        'ritual_ZN28DeclarativeCandlestickSeries2atEi', index,
    )
    from . import DeclarativeCandlestickSet
    return DeclarativeCandlestickSet._cuteAt(address)

  @overload(DeclarativeCandlestickSet)
  @overload(NoneType)
  def append(self, set: Optional[DeclarativeCandlestickSet]) -> bool:
    """
    Calls Qt's 'bool
    DeclarativeCandlestickSeries::append(DeclarativeCandlestickSet *set)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativecandlestickseries.html#append

    Parameters
    ----------

    set : Optional[DeclarativeCandlestickSet]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool DeclarativeCandlestickSeries::append(DeclarativeCandlestickSet
    #      *set)
    return self.uglySide.call(
        'ritual_ZN28DeclarativeCandlestickSeries6appendEP25DeclarativeCandl'
        'estickSet',
        self._addressOf(set),
    )

  @overload(float, float, float, float, float)
  def append(
      self,
      open: float,
      high: float,
      low: float,
      close: float,
      timestamp: float,
  ) -> bool:
    """
    Calls Qt's 'bool DeclarativeCandlestickSeries::append(qreal open, qreal
    high, qreal low, qreal close, qreal timestamp)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativecandlestickseries.html#append

    Parameters
    ----------

    open : float
      Passed on as it is.

    high : float
      Passed on as it is.

    low : float
      Passed on as it is.

    close : float
      Passed on as it is.

    timestamp : float
      Passed on as it is.
    """
    #  bool DeclarativeCandlestickSeries::append(qreal open, qreal high,
    #      qreal low, qreal close, qreal timestamp)
    return self.uglySide.call(
        'ritual_ZN28DeclarativeCandlestickSeries6appendEddddd',
        open, high, low, close, timestamp,
    )

  @overload(DeclarativeCandlestickSet)
  @overload(NoneType)
  def remove(self, set: Optional[DeclarativeCandlestickSet]) -> bool:
    """
    Calls Qt's 'bool
    DeclarativeCandlestickSeries::remove(DeclarativeCandlestickSet *set)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativecandlestickseries.html#remove

    Parameters
    ----------

    set : Optional[DeclarativeCandlestickSet]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool DeclarativeCandlestickSeries::remove(DeclarativeCandlestickSet
    #      *set)
    return self.uglySide.call(
        'ritual_ZN28DeclarativeCandlestickSeries6removeEP25DeclarativeCandl'
        'estickSet',
        self._addressOf(set),
    )

  @overload(float)
  def remove(self, timestamp: float) -> bool:
    """
    Calls Qt's 'bool DeclarativeCandlestickSeries::remove(qreal timestamp)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativecandlestickseries.html#remove

    Parameters
    ----------

    timestamp : float
      Passed on as it is.
    """
    #  bool DeclarativeCandlestickSeries::remove(qreal timestamp)
    return self.uglySide.call(
        'ritual_ZN28DeclarativeCandlestickSeries6removeEd', timestamp,
    )

  @overload(int, DeclarativeCandlestickSet)
  @overload(int, NoneType)
  def insert(
      self,
      index: int,
      set: Optional[DeclarativeCandlestickSet],
  ) -> bool:
    """
    Calls Qt's 'bool DeclarativeCandlestickSeries::insert(int index,
    DeclarativeCandlestickSet *set)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativecandlestickseries.html#insert

    Parameters
    ----------

    index : int
      Passed on as it is.

    set : Optional[DeclarativeCandlestickSet]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool DeclarativeCandlestickSeries::insert(int index,
    #      DeclarativeCandlestickSet *set)
    return self.uglySide.call(
        'ritual_ZN28DeclarativeCandlestickSeries6insertEiP25DeclarativeCand'
        'lestickSet',
        index, self._addressOf(set),
    )

  def clear(self) -> None:
    """
    Calls Qt's 'void DeclarativeCandlestickSeries::clear()'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativecandlestickseries.html#clear
    """
    #  void DeclarativeCandlestickSeries::clear()
    self.uglySide.call('ritual_ZN28DeclarativeCandlestickSeries5clearEv')

  def classBegin(self) -> None:
    """
    Calls Qt's 'void DeclarativeCandlestickSeries::classBegin()'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativecandlestickseries.html#classBegin
    """
    #  void DeclarativeCandlestickSeries::classBegin()
    ritual = 'ritual_ZN28DeclarativeCandlestickSeries10classBeginEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN28DeclarativeCandlestickSeries10classBeginEv'
    self.uglySide.call(ritual)

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void DeclarativeCandlestickSeries::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativecandlestickseries.html
    """
    #  void DeclarativeCandlestickSeries::componentComplete()
    ritual = 'ritual_ZN28DeclarativeCandlestickSeries17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN28DeclarativeCandlestickSeries17componentCompleteEv')
    self.uglySide.call(ritual)

  @overload(QAbstractAxis)
  @overload(NoneType)
  def axisXChanged(self, axis: Optional[QAbstractAxis]) -> None:
    """
    Calls Qt's 'void DeclarativeCandlestickSeries::axisXChanged(QAbstractAxis
    *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativecandlestickseries.html#axisXChanged

    Parameters
    ----------

    axis : Optional[QAbstractAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DeclarativeCandlestickSeries::axisXChanged(QAbstractAxis *axis)
    self.uglySide.call(
        'ritual_ZN28DeclarativeCandlestickSeries12axisXChangedEP13QAbstract'
        'Axis',
        self._addressOf(axis),
    )

  @overload(QAbstractAxis)
  @overload(NoneType)
  def axisYChanged(self, axis: Optional[QAbstractAxis]) -> None:
    """
    Calls Qt's 'void DeclarativeCandlestickSeries::axisYChanged(QAbstractAxis
    *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativecandlestickseries.html#axisYChanged

    Parameters
    ----------

    axis : Optional[QAbstractAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DeclarativeCandlestickSeries::axisYChanged(QAbstractAxis *axis)
    self.uglySide.call(
        'ritual_ZN28DeclarativeCandlestickSeries12axisYChangedEP13QAbstract'
        'Axis',
        self._addressOf(axis),
    )

  @overload(QAbstractAxis)
  @overload(NoneType)
  def axisXTopChanged(self, axis: Optional[QAbstractAxis]) -> None:
    """
    Calls Qt's 'void
    DeclarativeCandlestickSeries::axisXTopChanged(QAbstractAxis *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativecandlestickseries.html#axisXTopChanged

    Parameters
    ----------

    axis : Optional[QAbstractAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DeclarativeCandlestickSeries::axisXTopChanged(QAbstractAxis
    #      *axis)
    self.uglySide.call(
        'ritual_ZN28DeclarativeCandlestickSeries15axisXTopChangedEP13QAbstr'
        'actAxis',
        self._addressOf(axis),
    )

  @overload(QAbstractAxis)
  @overload(NoneType)
  def axisYRightChanged(self, axis: Optional[QAbstractAxis]) -> None:
    """
    Calls Qt's 'void
    DeclarativeCandlestickSeries::axisYRightChanged(QAbstractAxis *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativecandlestickseries.html

    Parameters
    ----------

    axis : Optional[QAbstractAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DeclarativeCandlestickSeries::axisYRightChanged(QAbstractAxis
    #      *axis)
    self.uglySide.call(
        'ritual_ZN28DeclarativeCandlestickSeries17axisYRightChangedEP13QAbs'
        'tractAxis',
        self._addressOf(axis),
    )

  @overload(DeclarativeCandlestickSet)
  @overload(NoneType)
  def clicked(self, set: Optional[DeclarativeCandlestickSet]) -> None:
    """
    Calls Qt's 'void
    DeclarativeCandlestickSeries::clicked(DeclarativeCandlestickSet *set)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativecandlestickseries.html#clicked

    Parameters
    ----------

    set : Optional[DeclarativeCandlestickSet]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DeclarativeCandlestickSeries::clicked(DeclarativeCandlestickSet
    #      *set)
    self.uglySide.call(
        'ritual_ZN28DeclarativeCandlestickSeries7clickedEP25DeclarativeCand'
        'lestickSet',
        self._addressOf(set),
    )

  @overload(bool, DeclarativeCandlestickSet)
  @overload(bool, NoneType)
  def hovered(
      self,
      status: bool,
      set: Optional[DeclarativeCandlestickSet],
  ) -> None:
    """
    Calls Qt's 'void DeclarativeCandlestickSeries::hovered(bool status,
    DeclarativeCandlestickSet *set)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativecandlestickseries.html#hovered

    Parameters
    ----------

    status : bool
      Passed on as it is.

    set : Optional[DeclarativeCandlestickSet]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DeclarativeCandlestickSeries::hovered(bool status,
    #      DeclarativeCandlestickSet *set)
    self.uglySide.call(
        'ritual_ZN28DeclarativeCandlestickSeries7hoveredEbP25DeclarativeCan'
        'dlestickSet',
        status, self._addressOf(set),
    )

  @overload(DeclarativeCandlestickSet)
  @overload(NoneType)
  def pressed(self, set: Optional[DeclarativeCandlestickSet]) -> None:
    """
    Calls Qt's 'void
    DeclarativeCandlestickSeries::pressed(DeclarativeCandlestickSet *set)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativecandlestickseries.html#pressed

    Parameters
    ----------

    set : Optional[DeclarativeCandlestickSet]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DeclarativeCandlestickSeries::pressed(DeclarativeCandlestickSet
    #      *set)
    self.uglySide.call(
        'ritual_ZN28DeclarativeCandlestickSeries7pressedEP25DeclarativeCand'
        'lestickSet',
        self._addressOf(set),
    )

  @overload(DeclarativeCandlestickSet)
  @overload(NoneType)
  def released(self, set: Optional[DeclarativeCandlestickSet]) -> None:
    """
    Calls Qt's 'void
    DeclarativeCandlestickSeries::released(DeclarativeCandlestickSet *set)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativecandlestickseries.html#released

    Parameters
    ----------

    set : Optional[DeclarativeCandlestickSet]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DeclarativeCandlestickSeries::released(DeclarativeCandlestickSet
    #      *set)
    self.uglySide.call(
        'ritual_ZN28DeclarativeCandlestickSeries8releasedEP25DeclarativeCan'
        'dlestickSet',
        self._addressOf(set),
    )

  @overload(DeclarativeCandlestickSet)
  @overload(NoneType)
  def doubleClicked(self, set: Optional[DeclarativeCandlestickSet]) -> None:
    """
    Calls Qt's 'void
    DeclarativeCandlestickSeries::doubleClicked(DeclarativeCandlestickSet
    *set)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativecandlestickseries.html#doubleClicked

    Parameters
    ----------

    set : Optional[DeclarativeCandlestickSet]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DeclarativeCandlestickSeries::doubleClicked(
    #      DeclarativeCandlestickSet *set)
    self.uglySide.call(
        'ritual_ZN28DeclarativeCandlestickSeries13doubleClickedEP25Declarat'
        'iveCandlestickSet',
        self._addressOf(set),
    )

  @overload(str)
  def brushFilenameChanged(self, brushFilename: str) -> None:
    """
    Calls Qt's 'void DeclarativeCandlestickSeries::brushFilenameChanged(const
    QString &brushFilename)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativecandlestickseries.html

    Parameters
    ----------

    brushFilename : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void DeclarativeCandlestickSeries::brushFilenameChanged(const QString
    #      &brushFilename)
    self.uglySide.call(
        'ritual_ZN28DeclarativeCandlestickSeries20brushFilenameChangedERK7Q'
        'String',
        brushFilename,
    )

  @overload(QCandlestickSet)
  @overload(NoneType)
  def onClicked(self, set: Optional[QCandlestickSet]) -> None:
    """
    Calls Qt's 'void DeclarativeCandlestickSeries::onClicked(QCandlestickSet
    *set)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativecandlestickseries.html#onClicked

    Parameters
    ----------

    set : Optional[QCandlestickSet]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DeclarativeCandlestickSeries::onClicked(QCandlestickSet *set)
    self.uglySide.call(
        'ritual_ZN28DeclarativeCandlestickSeries9onClickedEP15QCandlestickS'
        'et',
        self._addressOf(set),
    )

  @overload(bool, QCandlestickSet)
  @overload(bool, NoneType)
  def onHovered(self, status: bool, set: Optional[QCandlestickSet]) -> None:
    """
    Calls Qt's 'void DeclarativeCandlestickSeries::onHovered(bool status,
    QCandlestickSet *set)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativecandlestickseries.html#onHovered

    Parameters
    ----------

    status : bool
      Passed on as it is.

    set : Optional[QCandlestickSet]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DeclarativeCandlestickSeries::onHovered(bool status,
    #      QCandlestickSet *set)
    self.uglySide.call(
        'ritual_ZN28DeclarativeCandlestickSeries9onHoveredEbP15QCandlestick'
        'Set',
        status, self._addressOf(set),
    )

  @overload(QCandlestickSet)
  @overload(NoneType)
  def onPressed(self, set: Optional[QCandlestickSet]) -> None:
    """
    Calls Qt's 'void DeclarativeCandlestickSeries::onPressed(QCandlestickSet
    *set)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativecandlestickseries.html#onPressed

    Parameters
    ----------

    set : Optional[QCandlestickSet]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DeclarativeCandlestickSeries::onPressed(QCandlestickSet *set)
    self.uglySide.call(
        'ritual_ZN28DeclarativeCandlestickSeries9onPressedEP15QCandlestickS'
        'et',
        self._addressOf(set),
    )

  @overload(QCandlestickSet)
  @overload(NoneType)
  def onReleased(self, set: Optional[QCandlestickSet]) -> None:
    """
    Calls Qt's 'void DeclarativeCandlestickSeries::onReleased(QCandlestickSet
    *set)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativecandlestickseries.html#onReleased

    Parameters
    ----------

    set : Optional[QCandlestickSet]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DeclarativeCandlestickSeries::onReleased(QCandlestickSet *set)
    self.uglySide.call(
        'ritual_ZN28DeclarativeCandlestickSeries10onReleasedEP15QCandlestic'
        'kSet',
        self._addressOf(set),
    )

  @overload(QCandlestickSet)
  @overload(NoneType)
  def onDoubleClicked(self, set: Optional[QCandlestickSet]) -> None:
    """
    Calls Qt's 'void
    DeclarativeCandlestickSeries::onDoubleClicked(QCandlestickSet *set)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativecandlestickseries.html#onDoubleClicked

    Parameters
    ----------

    set : Optional[QCandlestickSet]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DeclarativeCandlestickSeries::onDoubleClicked(QCandlestickSet
    #      *set)
    self.uglySide.call(
        'ritual_ZN28DeclarativeCandlestickSeries15onDoubleClickedEP15QCandl'
        'estickSet',
        self._addressOf(set),
    )

  def handleBrushChanged(self) -> None:
    """
    Calls Qt's 'void DeclarativeCandlestickSeries::handleBrushChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativecandlestickseries.html
    """
    #  void DeclarativeCandlestickSeries::handleBrushChanged()
    self.uglySide.call(
        'ritual_ZN28DeclarativeCandlestickSeries18handleBrushChangedEv',
    )

  @staticmethod
  def appendSeriesChildren(*__, **_) -> Never:
    """
    Qt's 'void DeclarativeCandlestickSeries::appendSeriesChildren(
    QQmlListProperty<QObject> *list, QObject *element)': names
    'QQmlListProperty<QObject>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'DeclarativeCandlestickSeries.appendSeriesChildren' has no cute "
        "function yet. Qt's 'void "
        "DeclarativeCandlestickSeries::appendSeriesChildren(QQmlListProperty"
        "<QObject> *list, QObject *element)': names "
        "'QQmlListProperty<QObject>', which has no cute class yet.")

  @staticmethod
  def seriesChildren(*__, **_) -> Never:
    """
    Qt's 'QQmlListProperty<QObject>
    DeclarativeCandlestickSeries::seriesChildren()': gives a type Python has
    no way to take yet.
    """
    raise NotImplementedError(
        "'DeclarativeCandlestickSeries.seriesChildren' has no cute function "
        "yet. Qt's 'QQmlListProperty<QObject> "
        "DeclarativeCandlestickSeries::seriesChildren()': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def setBrushFilename(*__, **_) -> Never:
    """
    Qt's 'void DeclarativeCandlestickSeries::setBrushFilename(const QString
    &brushFilename)': leans on
    'DeclarativeCandlestickSeries::brushFilenameChanged(QString const&)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'DeclarativeCandlestickSeries.setBrushFilename' has no cute "
        "function yet. Qt's 'void "
        "DeclarativeCandlestickSeries::setBrushFilename(const QString "
        "&brushFilename)': leans on "
        "'DeclarativeCandlestickSeries::brushFilenameChanged(QString "
        "const&)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")
