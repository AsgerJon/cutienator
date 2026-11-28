"""
DeclarativeScatterSeries binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtChartsQml/6.12.0/QtChartsQml/private/declarativescatterseries_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means DeclarativeScatterSeries to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from ..QtQml import QQmlParserStatus
from ..QtCharts import QScatterSeries, QXYSeries
from . import DeclarativeXySeries

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QPointF
  from ..QtGui import QBrush
  from ..QtCharts import QAbstractAxis
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAbstractAxis = WAIT['QtCharts:QAbstractAxis']
  QBrush = WAIT['QBrush']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class DeclarativeScatterSeries(QScatterSeries, DeclarativeXySeries, QQmlParserStatus):
  """
  The cute side of Qt's DeclarativeScatterSeries: a plain Python object
  standing in front of one C++ DeclarativeScatterSeries.

  It is built on the cute 'QScatterSeries', as Qt's DeclarativeScatterSeries
  is built on Qt's QScatterSeries, and has everything that class has. It is
  built on the cute 'DeclarativeXySeries' as well, as Qt's
  DeclarativeScatterSeries is built on Qt's DeclarativeXySeries too, and has
  everything that class has. It is built on the cute 'QQmlParserStatus' as
  well, as Qt's DeclarativeScatterSeries is built on Qt's QQmlParserStatus
  too, and has everything that class has.

  What exists
  -----------

  Every function of Qt's DeclarativeScatterSeries that has a ritual and that
  Python can call so far, 42 names in all: 'metaObject', 'tr', 'xySeries',
  'axisX', 'setAxisX', 'axisY', 'setAxisY', 'axisXTop', 'setAxisXTop',
  'axisYRight', 'setAxisYRight', 'axisAngular', 'setAxisAngular',
  'axisRadial', 'setAxisRadial', 'borderWidth', 'setBorderWidth',
  'brushFilename', 'setBrushFilename', 'setBrush', 'brush', 'classBegin',
  'componentComplete', 'append', 'replace', 'remove', 'removePoints',
  'insert', 'clear', 'at', 'countChanged', 'axisXChanged', 'axisYChanged',
  'borderWidthChanged', 'axisXTopChanged', 'axisYRightChanged',
  'axisAngularChanged', 'axisRadialChanged', 'brushFilenameChanged',
  'brushChanged', 'handleCountChanged', 'handleBrushChanged'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *DeclarativeScatterSeries::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int DeclarativeScatterSeries::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QQmlListProperty<QObject>
    DeclarativeScatterSeries::declarativeChildren()': gives a type Python has
    no way to take yet.
  - Qt's 'void DeclarativeScatterSeries::appendDeclarativeChildren(
    QQmlListProperty<QObject> *list, QObject *element)': names
    'QQmlListProperty<QObject>', which has no cute class yet.

  What has no ritual
  ------------------

  2 of the 51 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ DeclarativeScatterSeries is created at the first use, not by
    'DeclarativeScatterSeries(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ DeclarativeScatterSeries.
  - Qt tells when it has removed the C++ DeclarativeScatterSeries. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's DeclarativeScatterSeries that has no cute function yet,
    'appendDeclarativeChildren', 'declarativeChildren', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  @overload(NoneType)
  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  @overload(str, str, int)
  @overload(str, NoneType, int)
  @overload(NoneType, str, int)
  @overload(NoneType, NoneType, int)
  def tr(s: Optional[str], c: Optional[str] = None, n: int = -1) -> str:
    """
    Calls Qt's 'QString DeclarativeScatterSeries::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/declarativescatterseries.html#tr

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    c : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString DeclarativeScatterSeries::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN24DeclarativeScatterSeries2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'DeclarativeScatterSeries'

  #  Qt's DeclarativeScatterSeries is built on more than one class. The part
  #  of a C++ DeclarativeScatterSeries that belongs to a class after the
  #  first begins somewhere inside the object, and the ritual named for that
  #  class gives where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'DeclarativeXySeries':
          'ritual_cast_DeclarativeScatterSeries_DeclarativeXySeries',
      'QQmlParserStatus':
          'ritual_cast_DeclarativeScatterSeries_QQmlParserStatus',
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
    Calls Qt's 'const QMetaObject *DeclarativeScatterSeries::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativescatterseries.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *DeclarativeScatterSeries::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK24DeclarativeScatterSeries10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def borderWidth(self) -> float:
    """
    Calls Qt's 'qreal DeclarativeScatterSeries::borderWidth() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativescatterseries.html#borderWidth
    """
    #  qreal DeclarativeScatterSeries::borderWidth() const
    return self.uglySide.call(
        'ritual_ZNK24DeclarativeScatterSeries11borderWidthEv',
    )

  def brushFilename(self) -> str:
    """
    Calls Qt's 'QString DeclarativeScatterSeries::brushFilename() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativescatterseries.html#brushFilename

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString DeclarativeScatterSeries::brushFilename() const
    return self.uglySide.call(
        'ritual_ZNK24DeclarativeScatterSeries13brushFilenameEv',
    )

  def brush(self) -> QBrush:
    """
    Calls Qt's 'QBrush DeclarativeScatterSeries::brush() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativescatterseries.html#brush

    Returns
    -------

    QBrush
      A new cute QBrush around the copy Qt gave back. Python owns it.
    """
    #  QBrush DeclarativeScatterSeries::brush() const
    address = self.uglySide.call(
        'ritual_ZNK24DeclarativeScatterSeries5brushEv',
    )
    from ..QtGui import QBrush
    return QBrush._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QAbstractAxis)
  @overload(NoneType)
  def setAxisX(self, axis: Optional[QAbstractAxis]) -> None:
    """
    Calls Qt's 'void DeclarativeScatterSeries::setAxisX(QAbstractAxis
    *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativescatterseries.html#setAxisX

    Parameters
    ----------

    axis : Optional[QAbstractAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DeclarativeScatterSeries::setAxisX(QAbstractAxis *axis)
    self.uglySide.call(
        'ritual_ZN24DeclarativeScatterSeries8setAxisXEP13QAbstractAxis',
        self._addressOf(axis),
    )

  @overload(QAbstractAxis)
  @overload(NoneType)
  def setAxisY(self, axis: Optional[QAbstractAxis]) -> None:
    """
    Calls Qt's 'void DeclarativeScatterSeries::setAxisY(QAbstractAxis
    *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativescatterseries.html#setAxisY

    Parameters
    ----------

    axis : Optional[QAbstractAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DeclarativeScatterSeries::setAxisY(QAbstractAxis *axis)
    self.uglySide.call(
        'ritual_ZN24DeclarativeScatterSeries8setAxisYEP13QAbstractAxis',
        self._addressOf(axis),
    )

  @overload(QAbstractAxis)
  @overload(NoneType)
  def setAxisXTop(self, axis: Optional[QAbstractAxis]) -> None:
    """
    Calls Qt's 'void DeclarativeScatterSeries::setAxisXTop(QAbstractAxis
    *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativescatterseries.html#setAxisXTop

    Parameters
    ----------

    axis : Optional[QAbstractAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DeclarativeScatterSeries::setAxisXTop(QAbstractAxis *axis)
    self.uglySide.call(
        'ritual_ZN24DeclarativeScatterSeries11setAxisXTopEP13QAbstractAxis',
        self._addressOf(axis),
    )

  @overload(QAbstractAxis)
  @overload(NoneType)
  def setAxisYRight(self, axis: Optional[QAbstractAxis]) -> None:
    """
    Calls Qt's 'void DeclarativeScatterSeries::setAxisYRight(QAbstractAxis
    *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativescatterseries.html#setAxisYRight

    Parameters
    ----------

    axis : Optional[QAbstractAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DeclarativeScatterSeries::setAxisYRight(QAbstractAxis *axis)
    self.uglySide.call(
        'ritual_ZN24DeclarativeScatterSeries13setAxisYRightEP13QAbstractAxi'
        's',
        self._addressOf(axis),
    )

  @overload(QAbstractAxis)
  @overload(NoneType)
  def setAxisAngular(self, axis: Optional[QAbstractAxis]) -> None:
    """
    Calls Qt's 'void DeclarativeScatterSeries::setAxisAngular(QAbstractAxis
    *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativescatterseries.html#setAxisAngular

    Parameters
    ----------

    axis : Optional[QAbstractAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DeclarativeScatterSeries::setAxisAngular(QAbstractAxis *axis)
    self.uglySide.call(
        'ritual_ZN24DeclarativeScatterSeries14setAxisAngularEP13QAbstractAx'
        'is',
        self._addressOf(axis),
    )

  @overload(QAbstractAxis)
  @overload(NoneType)
  def setAxisRadial(self, axis: Optional[QAbstractAxis]) -> None:
    """
    Calls Qt's 'void DeclarativeScatterSeries::setAxisRadial(QAbstractAxis
    *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativescatterseries.html#setAxisRadial

    Parameters
    ----------

    axis : Optional[QAbstractAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DeclarativeScatterSeries::setAxisRadial(QAbstractAxis *axis)
    self.uglySide.call(
        'ritual_ZN24DeclarativeScatterSeries13setAxisRadialEP13QAbstractAxi'
        's',
        self._addressOf(axis),
    )

  @overload(float)
  def setBorderWidth(self, borderWidth: float) -> None:
    """
    Calls Qt's 'void DeclarativeScatterSeries::setBorderWidth(qreal
    borderWidth)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativescatterseries.html#setBorderWidth

    Parameters
    ----------

    borderWidth : float
      Passed on as it is.
    """
    #  void DeclarativeScatterSeries::setBorderWidth(qreal borderWidth)
    self.uglySide.call(
        'ritual_ZN24DeclarativeScatterSeries14setBorderWidthEd', borderWidth,
    )

  @overload(str)
  def setBrushFilename(self, brushFilename: str) -> None:
    """
    Calls Qt's 'void DeclarativeScatterSeries::setBrushFilename(const QString
    &brushFilename)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativescatterseries.html#setBrushFilename

    Parameters
    ----------

    brushFilename : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void DeclarativeScatterSeries::setBrushFilename(const QString
    #      &brushFilename)
    self.uglySide.call(
        'ritual_ZN24DeclarativeScatterSeries16setBrushFilenameERK7QString',
        brushFilename,
    )

  @overload(QBrush)
  def setBrush(self, brush: QBrush) -> None:
    """
    Calls Qt's 'void DeclarativeScatterSeries::setBrush(const QBrush
    &brush)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativescatterseries.html#setBrush

    Parameters
    ----------

    brush : QBrush
      Passed on as a value: Qt reads the C++ QBrush, which stays Python's
      own.
    """
    #  void DeclarativeScatterSeries::setBrush(const QBrush &brush)
    ritual = 'ritual_ZN24DeclarativeScatterSeries8setBrushERK6QBrush'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN24DeclarativeScatterSeries8setBrushERK6QBrush'
    self.uglySide.call(ritual, self._valueOf(brush))

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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'DeclarativeScatterSeries::DeclarativeScatterSeries(QObject *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativescatterseries.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  DeclarativeScatterSeries::DeclarativeScatterSeries(QObject *parent)
    self._noteCreation(DeclarativeScatterSeries, lambda: Rituals.call(
        'ritual_ZN24DeclarativeScatterSeriesC1EP7QObject',
        self._addressOf(parent, 'QObject'),
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

  def xySeries(self) -> Optional[QXYSeries]:
    """
    Calls Qt's 'QXYSeries *DeclarativeScatterSeries::xySeries()'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativescatterseries.html#xySeries

    Returns
    -------

    Optional[QXYSeries]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QXYSeries *DeclarativeScatterSeries::xySeries()
    ritual = 'ritual_ZN24DeclarativeScatterSeries8xySeriesEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN24DeclarativeScatterSeries8xySeriesEv'
    address = self.uglySide.call(ritual)
    return QXYSeries._cuteAt(address)

  def axisX(self) -> Optional[QAbstractAxis]:
    """
    Calls Qt's 'QAbstractAxis *DeclarativeScatterSeries::axisX()'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativescatterseries.html#axisX

    Returns
    -------

    Optional[QAbstractAxis]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractAxis *DeclarativeScatterSeries::axisX()
    address = self.uglySide.call(
        'ritual_ZN24DeclarativeScatterSeries5axisXEv',
    )
    from ..QtCharts import QAbstractAxis
    return QAbstractAxis._cuteAt(address)

  def axisY(self) -> Optional[QAbstractAxis]:
    """
    Calls Qt's 'QAbstractAxis *DeclarativeScatterSeries::axisY()'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativescatterseries.html#axisY

    Returns
    -------

    Optional[QAbstractAxis]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractAxis *DeclarativeScatterSeries::axisY()
    address = self.uglySide.call(
        'ritual_ZN24DeclarativeScatterSeries5axisYEv',
    )
    from ..QtCharts import QAbstractAxis
    return QAbstractAxis._cuteAt(address)

  def axisXTop(self) -> Optional[QAbstractAxis]:
    """
    Calls Qt's 'QAbstractAxis *DeclarativeScatterSeries::axisXTop()'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativescatterseries.html#axisXTop

    Returns
    -------

    Optional[QAbstractAxis]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractAxis *DeclarativeScatterSeries::axisXTop()
    address = self.uglySide.call(
        'ritual_ZN24DeclarativeScatterSeries8axisXTopEv',
    )
    from ..QtCharts import QAbstractAxis
    return QAbstractAxis._cuteAt(address)

  def axisYRight(self) -> Optional[QAbstractAxis]:
    """
    Calls Qt's 'QAbstractAxis *DeclarativeScatterSeries::axisYRight()'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativescatterseries.html#axisYRight

    Returns
    -------

    Optional[QAbstractAxis]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractAxis *DeclarativeScatterSeries::axisYRight()
    address = self.uglySide.call(
        'ritual_ZN24DeclarativeScatterSeries10axisYRightEv',
    )
    from ..QtCharts import QAbstractAxis
    return QAbstractAxis._cuteAt(address)

  def axisAngular(self) -> Optional[QAbstractAxis]:
    """
    Calls Qt's 'QAbstractAxis *DeclarativeScatterSeries::axisAngular()'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativescatterseries.html#axisAngular

    Returns
    -------

    Optional[QAbstractAxis]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractAxis *DeclarativeScatterSeries::axisAngular()
    address = self.uglySide.call(
        'ritual_ZN24DeclarativeScatterSeries11axisAngularEv',
    )
    from ..QtCharts import QAbstractAxis
    return QAbstractAxis._cuteAt(address)

  def axisRadial(self) -> Optional[QAbstractAxis]:
    """
    Calls Qt's 'QAbstractAxis *DeclarativeScatterSeries::axisRadial()'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativescatterseries.html#axisRadial

    Returns
    -------

    Optional[QAbstractAxis]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractAxis *DeclarativeScatterSeries::axisRadial()
    address = self.uglySide.call(
        'ritual_ZN24DeclarativeScatterSeries10axisRadialEv',
    )
    from ..QtCharts import QAbstractAxis
    return QAbstractAxis._cuteAt(address)

  def classBegin(self) -> None:
    """
    Calls Qt's 'void DeclarativeScatterSeries::classBegin()'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativescatterseries.html#classBegin
    """
    #  void DeclarativeScatterSeries::classBegin()
    ritual = 'ritual_ZN24DeclarativeScatterSeries10classBeginEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN24DeclarativeScatterSeries10classBeginEv'
    self.uglySide.call(ritual)

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void DeclarativeScatterSeries::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativescatterseries.html#componentComplete
    """
    #  void DeclarativeScatterSeries::componentComplete()
    ritual = 'ritual_ZN24DeclarativeScatterSeries17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN24DeclarativeScatterSeries17componentCompleteEv'
    self.uglySide.call(ritual)

  @overload(float, float)
  def append(self, x: float, y: float) -> None:
    """
    Calls Qt's 'void DeclarativeScatterSeries::append(qreal x, qreal y)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativescatterseries.html#append

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.
    """
    #  void DeclarativeScatterSeries::append(qreal x, qreal y)
    self.uglySide.call('ritual_ZN24DeclarativeScatterSeries6appendEdd', x, y)

  @overload(float, float, float, float)
  def replace(
      self,
      oldX: float,
      oldY: float,
      newX: float,
      newY: float,
  ) -> None:
    """
    Calls Qt's 'void DeclarativeScatterSeries::replace(qreal oldX, qreal
    oldY, qreal newX, qreal newY)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativescatterseries.html#replace

    Parameters
    ----------

    oldX : float
      Passed on as it is.

    oldY : float
      Passed on as it is.

    newX : float
      Passed on as it is.

    newY : float
      Passed on as it is.
    """
    #  void DeclarativeScatterSeries::replace(qreal oldX, qreal oldY, qreal
    #      newX, qreal newY)
    self.uglySide.call(
        'ritual_ZN24DeclarativeScatterSeries7replaceEdddd',
        oldX, oldY, newX, newY,
    )

  @overload(int, float, float)
  def replace(self, index: int, newX: float, newY: float) -> None:
    """
    Calls Qt's 'void DeclarativeScatterSeries::replace(int index, qreal newX,
    qreal newY)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativescatterseries.html#replace

    Parameters
    ----------

    index : int
      Passed on as it is.

    newX : float
      Passed on as it is.

    newY : float
      Passed on as it is.
    """
    #  void DeclarativeScatterSeries::replace(int index, qreal newX, qreal
    #      newY)
    self.uglySide.call(
        'ritual_ZN24DeclarativeScatterSeries7replaceEidd', index, newX, newY,
    )

  @overload(float, float)
  def remove(self, x: float, y: float) -> None:
    """
    Calls Qt's 'void DeclarativeScatterSeries::remove(qreal x, qreal y)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativescatterseries.html#remove

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.
    """
    #  void DeclarativeScatterSeries::remove(qreal x, qreal y)
    self.uglySide.call('ritual_ZN24DeclarativeScatterSeries6removeEdd', x, y)

  @overload(int)
  def remove(self, index: int) -> None:
    """
    Calls Qt's 'void DeclarativeScatterSeries::remove(int index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativescatterseries.html#remove

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void DeclarativeScatterSeries::remove(int index)
    self.uglySide.call('ritual_ZN24DeclarativeScatterSeries6removeEi', index)

  @overload(int, int)
  def removePoints(self, index: int, count: int) -> None:
    """
    Calls Qt's 'void DeclarativeScatterSeries::removePoints(int index, int
    count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativescatterseries.html#removePoints

    Parameters
    ----------

    index : int
      Passed on as it is.

    count : int
      Passed on as it is.
    """
    #  void DeclarativeScatterSeries::removePoints(int index, int count)
    self.uglySide.call(
        'ritual_ZN24DeclarativeScatterSeries12removePointsEii', index, count,
    )

  @overload(int, float, float)
  def insert(self, index: int, x: float, y: float) -> None:
    """
    Calls Qt's 'void DeclarativeScatterSeries::insert(int index, qreal x,
    qreal y)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativescatterseries.html#insert

    Parameters
    ----------

    index : int
      Passed on as it is.

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.
    """
    #  void DeclarativeScatterSeries::insert(int index, qreal x, qreal y)
    self.uglySide.call(
        'ritual_ZN24DeclarativeScatterSeries6insertEidd', index, x, y,
    )

  def clear(self) -> None:
    """
    Calls Qt's 'void DeclarativeScatterSeries::clear()'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativescatterseries.html#clear
    """
    #  void DeclarativeScatterSeries::clear()
    self.uglySide.call('ritual_ZN24DeclarativeScatterSeries5clearEv')

  @overload(int)
  def at(self, index: int) -> QPointF:
    """
    Calls Qt's 'QPointF DeclarativeScatterSeries::at(int index)'.

    Qt's own words: https://doc.qt.io/qt-6/declarativescatterseries.html#at

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF DeclarativeScatterSeries::at(int index)
    address = self.uglySide.call(
        'ritual_ZN24DeclarativeScatterSeries2atEi', index,
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  @overload(int)
  def countChanged(self, count: int) -> None:
    """
    Calls Qt's 'void DeclarativeScatterSeries::countChanged(int count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativescatterseries.html#countChanged

    Parameters
    ----------

    count : int
      Passed on as it is.
    """
    #  void DeclarativeScatterSeries::countChanged(int count)
    self.uglySide.call(
        'ritual_ZN24DeclarativeScatterSeries12countChangedEi', count,
    )

  @overload(QAbstractAxis)
  @overload(NoneType)
  def axisXChanged(self, axis: Optional[QAbstractAxis]) -> None:
    """
    Calls Qt's 'void DeclarativeScatterSeries::axisXChanged(QAbstractAxis
    *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativescatterseries.html#axisXChanged

    Parameters
    ----------

    axis : Optional[QAbstractAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DeclarativeScatterSeries::axisXChanged(QAbstractAxis *axis)
    self.uglySide.call(
        'ritual_ZN24DeclarativeScatterSeries12axisXChangedEP13QAbstractAxis',
        self._addressOf(axis),
    )

  @overload(QAbstractAxis)
  @overload(NoneType)
  def axisYChanged(self, axis: Optional[QAbstractAxis]) -> None:
    """
    Calls Qt's 'void DeclarativeScatterSeries::axisYChanged(QAbstractAxis
    *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativescatterseries.html#axisYChanged

    Parameters
    ----------

    axis : Optional[QAbstractAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DeclarativeScatterSeries::axisYChanged(QAbstractAxis *axis)
    self.uglySide.call(
        'ritual_ZN24DeclarativeScatterSeries12axisYChangedEP13QAbstractAxis',
        self._addressOf(axis),
    )

  @overload(float)
  def borderWidthChanged(self, width: float) -> None:
    """
    Calls Qt's 'void DeclarativeScatterSeries::borderWidthChanged(qreal
    width)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativescatterseries.html#borderWidthChanged

    Parameters
    ----------

    width : float
      Passed on as it is.
    """
    #  void DeclarativeScatterSeries::borderWidthChanged(qreal width)
    self.uglySide.call(
        'ritual_ZN24DeclarativeScatterSeries18borderWidthChangedEd', width,
    )

  @overload(QAbstractAxis)
  @overload(NoneType)
  def axisXTopChanged(self, axis: Optional[QAbstractAxis]) -> None:
    """
    Calls Qt's 'void DeclarativeScatterSeries::axisXTopChanged(QAbstractAxis
    *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativescatterseries.html#axisXTopChanged

    Parameters
    ----------

    axis : Optional[QAbstractAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DeclarativeScatterSeries::axisXTopChanged(QAbstractAxis *axis)
    self.uglySide.call(
        'ritual_ZN24DeclarativeScatterSeries15axisXTopChangedEP13QAbstractA'
        'xis',
        self._addressOf(axis),
    )

  @overload(QAbstractAxis)
  @overload(NoneType)
  def axisYRightChanged(self, axis: Optional[QAbstractAxis]) -> None:
    """
    Calls Qt's 'void
    DeclarativeScatterSeries::axisYRightChanged(QAbstractAxis *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativescatterseries.html#axisYRightChanged

    Parameters
    ----------

    axis : Optional[QAbstractAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DeclarativeScatterSeries::axisYRightChanged(QAbstractAxis *axis)
    self.uglySide.call(
        'ritual_ZN24DeclarativeScatterSeries17axisYRightChangedEP13QAbstrac'
        'tAxis',
        self._addressOf(axis),
    )

  @overload(QAbstractAxis)
  @overload(NoneType)
  def axisAngularChanged(self, axis: Optional[QAbstractAxis]) -> None:
    """
    Calls Qt's 'void
    DeclarativeScatterSeries::axisAngularChanged(QAbstractAxis *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativescatterseries.html#axisAngularChanged

    Parameters
    ----------

    axis : Optional[QAbstractAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DeclarativeScatterSeries::axisAngularChanged(QAbstractAxis *axis)
    self.uglySide.call(
        'ritual_ZN24DeclarativeScatterSeries18axisAngularChangedEP13QAbstra'
        'ctAxis',
        self._addressOf(axis),
    )

  @overload(QAbstractAxis)
  @overload(NoneType)
  def axisRadialChanged(self, axis: Optional[QAbstractAxis]) -> None:
    """
    Calls Qt's 'void
    DeclarativeScatterSeries::axisRadialChanged(QAbstractAxis *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativescatterseries.html#axisRadialChanged

    Parameters
    ----------

    axis : Optional[QAbstractAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DeclarativeScatterSeries::axisRadialChanged(QAbstractAxis *axis)
    self.uglySide.call(
        'ritual_ZN24DeclarativeScatterSeries17axisRadialChangedEP13QAbstrac'
        'tAxis',
        self._addressOf(axis),
    )

  @overload(str)
  def brushFilenameChanged(self, brushFilename: str) -> None:
    """
    Calls Qt's 'void DeclarativeScatterSeries::brushFilenameChanged(const
    QString &brushFilename)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativescatterseries.html#brushFilenameChanged

    Parameters
    ----------

    brushFilename : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void DeclarativeScatterSeries::brushFilenameChanged(const QString
    #      &brushFilename)
    self.uglySide.call(
        'ritual_ZN24DeclarativeScatterSeries20brushFilenameChangedERK7QStri'
        'ng',
        brushFilename,
    )

  def brushChanged(self) -> None:
    """
    Calls Qt's 'void DeclarativeScatterSeries::brushChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativescatterseries.html#brushChanged
    """
    #  void DeclarativeScatterSeries::brushChanged()
    self.uglySide.call('ritual_ZN24DeclarativeScatterSeries12brushChangedEv')

  @overload(int)
  def handleCountChanged(self, index: int) -> None:
    """
    Calls Qt's 'void DeclarativeScatterSeries::handleCountChanged(int
    index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativescatterseries.html#handleCountChanged

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void DeclarativeScatterSeries::handleCountChanged(int index)
    self.uglySide.call(
        'ritual_ZN24DeclarativeScatterSeries18handleCountChangedEi', index,
    )

  def handleBrushChanged(self) -> None:
    """
    Calls Qt's 'void DeclarativeScatterSeries::handleBrushChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativescatterseries.html#handleBrushChanged
    """
    #  void DeclarativeScatterSeries::handleBrushChanged()
    self.uglySide.call(
        'ritual_ZN24DeclarativeScatterSeries18handleBrushChangedEv',
    )

  @staticmethod
  def appendDeclarativeChildren(*__, **_) -> Never:
    """
    Qt's 'void DeclarativeScatterSeries::appendDeclarativeChildren(
    QQmlListProperty<QObject> *list, QObject *element)': names
    'QQmlListProperty<QObject>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'DeclarativeScatterSeries.appendDeclarativeChildren' has no cute "
        "function yet. Qt's 'void "
        "DeclarativeScatterSeries::appendDeclarativeChildren(QQmlListPropert"
        "y<QObject> *list, QObject *element)': names "
        "'QQmlListProperty<QObject>', which has no cute class yet.")

  @staticmethod
  def declarativeChildren(*__, **_) -> Never:
    """
    Qt's 'QQmlListProperty<QObject>
    DeclarativeScatterSeries::declarativeChildren()': gives a type Python has
    no way to take yet.
    """
    raise NotImplementedError(
        "'DeclarativeScatterSeries.declarativeChildren' has no cute "
        "function yet. Qt's 'QQmlListProperty<QObject> "
        "DeclarativeScatterSeries::declarativeChildren()': gives a type "
        "Python has no way to take yet.")
