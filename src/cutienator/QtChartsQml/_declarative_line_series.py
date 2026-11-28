"""
DeclarativeLineSeries binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtChartsQml/6.12.0/QtChartsQml/private/declarativelineseries_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means DeclarativeLineSeries to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QObject
from ..QtQml import QQmlParserStatus
from ..QtCharts import QLineSeries, QXYSeries
from . import DeclarativeXySeries

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QPointF
  from ..QtCharts import QAbstractAxis
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAbstractAxis = WAIT['QtCharts:QAbstractAxis']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class DeclarativeLineSeries(QLineSeries, DeclarativeXySeries, QQmlParserStatus):
  """
  The cute side of Qt's DeclarativeLineSeries: a plain Python object standing
  in front of one C++ DeclarativeLineSeries.

  It is built on the cute 'QLineSeries', as Qt's DeclarativeLineSeries is
  built on Qt's QLineSeries, and has everything that class has. It is built
  on the cute 'DeclarativeXySeries' as well, as Qt's DeclarativeLineSeries is
  built on Qt's DeclarativeXySeries too, and has everything that class has.
  It is built on the cute 'QQmlParserStatus' as well, as Qt's
  DeclarativeLineSeries is built on Qt's QQmlParserStatus too, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's DeclarativeLineSeries that has a ritual and that
  Python can call so far, 41 names in all: 'metaObject', 'tr', 'xySeries',
  'axisX', 'setAxisX', 'axisY', 'setAxisY', 'axisXTop', 'setAxisXTop',
  'axisYRight', 'setAxisYRight', 'axisAngular', 'setAxisAngular',
  'axisRadial', 'setAxisRadial', 'width', 'setWidth', 'style', 'setStyle',
  'capStyle', 'setCapStyle', 'classBegin', 'componentComplete', 'append',
  'replace', 'remove', 'removePoints', 'insert', 'clear', 'at',
  'countChanged', 'axisXChanged', 'axisYChanged', 'axisXTopChanged',
  'axisYRightChanged', 'axisAngularChanged', 'axisRadialChanged',
  'widthChanged', 'styleChanged', 'capStyleChanged', 'handleCountChanged'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *DeclarativeLineSeries::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int DeclarativeLineSeries::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QQmlListProperty<QObject>
    DeclarativeLineSeries::declarativeChildren()': gives a type Python has no
    way to take yet.
  - Qt's 'void DeclarativeLineSeries::appendDeclarativeChildren(
    QQmlListProperty<QObject> *list, QObject *element)': names
    'QQmlListProperty<QObject>', which has no cute class yet.

  What has no ritual
  ------------------

  2 of the 50 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ DeclarativeLineSeries is created at the first use, not by
    'DeclarativeLineSeries(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ DeclarativeLineSeries.
  - Qt tells when it has removed the C++ DeclarativeLineSeries. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's DeclarativeLineSeries that has no cute function yet,
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
    Calls Qt's 'QString DeclarativeLineSeries::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/declarativelineseries.html#tr

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
    #  QString DeclarativeLineSeries::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN21DeclarativeLineSeries2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'DeclarativeLineSeries'

  #  Qt's DeclarativeLineSeries is built on more than one class. The part of
  #  a C++ DeclarativeLineSeries that belongs to a class after the first
  #  begins somewhere inside the object, and the ritual named for that class
  #  gives where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'DeclarativeXySeries':
          'ritual_cast_DeclarativeLineSeries_DeclarativeXySeries',
      'QQmlParserStatus':
          'ritual_cast_DeclarativeLineSeries_QQmlParserStatus',
  }

  #  A C++ DeclarativeLineSeries Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_DeclarativeLineSeries'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *DeclarativeLineSeries::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativelineseries.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *DeclarativeLineSeries::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK21DeclarativeLineSeries10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def width(self) -> float:
    """
    Calls Qt's 'qreal DeclarativeLineSeries::width() const'.

    Qt's own words: https://doc.qt.io/qt-6/declarativelineseries.html#width
    """
    #  qreal DeclarativeLineSeries::width() const
    return self.uglySide.call('ritual_ZNK21DeclarativeLineSeries5widthEv')

  def style(self) -> Qt.PenStyle:
    """
    Calls Qt's 'Qt::PenStyle DeclarativeLineSeries::style() const'.

    Qt's own words: https://doc.qt.io/qt-6/declarativelineseries.html#style

    Returns
    -------

    Qt.PenStyle
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.PenStyle(number)'
      gives.
    """
    #  Qt::PenStyle DeclarativeLineSeries::style() const
    return Qt.PenStyle(self.uglySide.call(
        'ritual_ZNK21DeclarativeLineSeries5styleEv',
    ))

  def capStyle(self) -> Qt.PenCapStyle:
    """
    Calls Qt's 'Qt::PenCapStyle DeclarativeLineSeries::capStyle() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativelineseries.html#capStyle

    Returns
    -------

    Qt.PenCapStyle
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.PenCapStyle(number)'
      gives.
    """
    #  Qt::PenCapStyle DeclarativeLineSeries::capStyle() const
    return Qt.PenCapStyle(self.uglySide.call(
        'ritual_ZNK21DeclarativeLineSeries8capStyleEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QAbstractAxis)
  @overload(NoneType)
  def setAxisX(self, axis: Optional[QAbstractAxis]) -> None:
    """
    Calls Qt's 'void DeclarativeLineSeries::setAxisX(QAbstractAxis *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativelineseries.html#setAxisX

    Parameters
    ----------

    axis : Optional[QAbstractAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DeclarativeLineSeries::setAxisX(QAbstractAxis *axis)
    self.uglySide.call(
        'ritual_ZN21DeclarativeLineSeries8setAxisXEP13QAbstractAxis',
        self._addressOf(axis),
    )

  @overload(QAbstractAxis)
  @overload(NoneType)
  def setAxisY(self, axis: Optional[QAbstractAxis]) -> None:
    """
    Calls Qt's 'void DeclarativeLineSeries::setAxisY(QAbstractAxis *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativelineseries.html#setAxisY

    Parameters
    ----------

    axis : Optional[QAbstractAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DeclarativeLineSeries::setAxisY(QAbstractAxis *axis)
    self.uglySide.call(
        'ritual_ZN21DeclarativeLineSeries8setAxisYEP13QAbstractAxis',
        self._addressOf(axis),
    )

  @overload(QAbstractAxis)
  @overload(NoneType)
  def setAxisXTop(self, axis: Optional[QAbstractAxis]) -> None:
    """
    Calls Qt's 'void DeclarativeLineSeries::setAxisXTop(QAbstractAxis
    *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativelineseries.html#setAxisXTop

    Parameters
    ----------

    axis : Optional[QAbstractAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DeclarativeLineSeries::setAxisXTop(QAbstractAxis *axis)
    self.uglySide.call(
        'ritual_ZN21DeclarativeLineSeries11setAxisXTopEP13QAbstractAxis',
        self._addressOf(axis),
    )

  @overload(QAbstractAxis)
  @overload(NoneType)
  def setAxisYRight(self, axis: Optional[QAbstractAxis]) -> None:
    """
    Calls Qt's 'void DeclarativeLineSeries::setAxisYRight(QAbstractAxis
    *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativelineseries.html#setAxisYRight

    Parameters
    ----------

    axis : Optional[QAbstractAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DeclarativeLineSeries::setAxisYRight(QAbstractAxis *axis)
    self.uglySide.call(
        'ritual_ZN21DeclarativeLineSeries13setAxisYRightEP13QAbstractAxis',
        self._addressOf(axis),
    )

  @overload(QAbstractAxis)
  @overload(NoneType)
  def setAxisAngular(self, axis: Optional[QAbstractAxis]) -> None:
    """
    Calls Qt's 'void DeclarativeLineSeries::setAxisAngular(QAbstractAxis
    *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativelineseries.html#setAxisAngular

    Parameters
    ----------

    axis : Optional[QAbstractAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DeclarativeLineSeries::setAxisAngular(QAbstractAxis *axis)
    self.uglySide.call(
        'ritual_ZN21DeclarativeLineSeries14setAxisAngularEP13QAbstractAxis',
        self._addressOf(axis),
    )

  @overload(QAbstractAxis)
  @overload(NoneType)
  def setAxisRadial(self, axis: Optional[QAbstractAxis]) -> None:
    """
    Calls Qt's 'void DeclarativeLineSeries::setAxisRadial(QAbstractAxis
    *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativelineseries.html#setAxisRadial

    Parameters
    ----------

    axis : Optional[QAbstractAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DeclarativeLineSeries::setAxisRadial(QAbstractAxis *axis)
    self.uglySide.call(
        'ritual_ZN21DeclarativeLineSeries13setAxisRadialEP13QAbstractAxis',
        self._addressOf(axis),
    )

  @overload(float)
  def setWidth(self, width: float) -> None:
    """
    Calls Qt's 'void DeclarativeLineSeries::setWidth(qreal width)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativelineseries.html#setWidth

    Parameters
    ----------

    width : float
      Passed on as it is.
    """
    #  void DeclarativeLineSeries::setWidth(qreal width)
    self.uglySide.call('ritual_ZN21DeclarativeLineSeries8setWidthEd', width)

  @overload(Qt.PenStyle)
  def setStyle(self, style: Qt.PenStyle) -> None:
    """
    Calls Qt's 'void DeclarativeLineSeries::setStyle(Qt::PenStyle style)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativelineseries.html#setStyle

    Parameters
    ----------

    style : Qt.PenStyle
      Passed on as its number.
    """
    #  void DeclarativeLineSeries::setStyle(Qt::PenStyle style)
    self.uglySide.call(
        'ritual_ZN21DeclarativeLineSeries8setStyleEN2Qt8PenStyleE',
        style.value,
    )

  @overload(Qt.PenCapStyle)
  def setCapStyle(self, capStyle: Qt.PenCapStyle) -> None:
    """
    Calls Qt's 'void DeclarativeLineSeries::setCapStyle(Qt::PenCapStyle
    capStyle)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativelineseries.html#setCapStyle

    Parameters
    ----------

    capStyle : Qt.PenCapStyle
      Passed on as its number.
    """
    #  void DeclarativeLineSeries::setCapStyle(Qt::PenCapStyle capStyle)
    self.uglySide.call(
        'ritual_ZN21DeclarativeLineSeries11setCapStyleEN2Qt11PenCapStyleE',
        capStyle.value,
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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'DeclarativeLineSeries::DeclarativeLineSeries(QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativelineseries.html#DeclarativeLineSeries

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  DeclarativeLineSeries::DeclarativeLineSeries(QObject *parent)
    self._noteCreation(DeclarativeLineSeries, lambda: Rituals.call(
        'ritual_ZN21DeclarativeLineSeriesC1EP7QObject',
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
    Calls Qt's 'QXYSeries *DeclarativeLineSeries::xySeries()'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativelineseries.html#xySeries

    Returns
    -------

    Optional[QXYSeries]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QXYSeries *DeclarativeLineSeries::xySeries()
    ritual = 'ritual_ZN21DeclarativeLineSeries8xySeriesEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21DeclarativeLineSeries8xySeriesEv'
    address = self.uglySide.call(ritual)
    return QXYSeries._cuteAt(address)

  def axisX(self) -> Optional[QAbstractAxis]:
    """
    Calls Qt's 'QAbstractAxis *DeclarativeLineSeries::axisX()'.

    Qt's own words: https://doc.qt.io/qt-6/declarativelineseries.html#axisX

    Returns
    -------

    Optional[QAbstractAxis]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractAxis *DeclarativeLineSeries::axisX()
    address = self.uglySide.call('ritual_ZN21DeclarativeLineSeries5axisXEv')
    from ..QtCharts import QAbstractAxis
    return QAbstractAxis._cuteAt(address)

  def axisY(self) -> Optional[QAbstractAxis]:
    """
    Calls Qt's 'QAbstractAxis *DeclarativeLineSeries::axisY()'.

    Qt's own words: https://doc.qt.io/qt-6/declarativelineseries.html#axisY

    Returns
    -------

    Optional[QAbstractAxis]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractAxis *DeclarativeLineSeries::axisY()
    address = self.uglySide.call('ritual_ZN21DeclarativeLineSeries5axisYEv')
    from ..QtCharts import QAbstractAxis
    return QAbstractAxis._cuteAt(address)

  def axisXTop(self) -> Optional[QAbstractAxis]:
    """
    Calls Qt's 'QAbstractAxis *DeclarativeLineSeries::axisXTop()'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativelineseries.html#axisXTop

    Returns
    -------

    Optional[QAbstractAxis]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractAxis *DeclarativeLineSeries::axisXTop()
    address = self.uglySide.call(
        'ritual_ZN21DeclarativeLineSeries8axisXTopEv',
    )
    from ..QtCharts import QAbstractAxis
    return QAbstractAxis._cuteAt(address)

  def axisYRight(self) -> Optional[QAbstractAxis]:
    """
    Calls Qt's 'QAbstractAxis *DeclarativeLineSeries::axisYRight()'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativelineseries.html#axisYRight

    Returns
    -------

    Optional[QAbstractAxis]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractAxis *DeclarativeLineSeries::axisYRight()
    address = self.uglySide.call(
        'ritual_ZN21DeclarativeLineSeries10axisYRightEv',
    )
    from ..QtCharts import QAbstractAxis
    return QAbstractAxis._cuteAt(address)

  def axisAngular(self) -> Optional[QAbstractAxis]:
    """
    Calls Qt's 'QAbstractAxis *DeclarativeLineSeries::axisAngular()'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativelineseries.html#axisAngular

    Returns
    -------

    Optional[QAbstractAxis]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractAxis *DeclarativeLineSeries::axisAngular()
    address = self.uglySide.call(
        'ritual_ZN21DeclarativeLineSeries11axisAngularEv',
    )
    from ..QtCharts import QAbstractAxis
    return QAbstractAxis._cuteAt(address)

  def axisRadial(self) -> Optional[QAbstractAxis]:
    """
    Calls Qt's 'QAbstractAxis *DeclarativeLineSeries::axisRadial()'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativelineseries.html#axisRadial

    Returns
    -------

    Optional[QAbstractAxis]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractAxis *DeclarativeLineSeries::axisRadial()
    address = self.uglySide.call(
        'ritual_ZN21DeclarativeLineSeries10axisRadialEv',
    )
    from ..QtCharts import QAbstractAxis
    return QAbstractAxis._cuteAt(address)

  def classBegin(self) -> None:
    """
    Calls Qt's 'void DeclarativeLineSeries::classBegin()'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativelineseries.html#classBegin
    """
    #  void DeclarativeLineSeries::classBegin()
    ritual = 'ritual_ZN21DeclarativeLineSeries10classBeginEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21DeclarativeLineSeries10classBeginEv'
    self.uglySide.call(ritual)

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void DeclarativeLineSeries::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativelineseries.html#componentComplete
    """
    #  void DeclarativeLineSeries::componentComplete()
    ritual = 'ritual_ZN21DeclarativeLineSeries17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21DeclarativeLineSeries17componentCompleteEv'
    self.uglySide.call(ritual)

  @overload(float, float)
  def append(self, x: float, y: float) -> None:
    """
    Calls Qt's 'void DeclarativeLineSeries::append(qreal x, qreal y)'.

    Qt's own words: https://doc.qt.io/qt-6/declarativelineseries.html#append

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.
    """
    #  void DeclarativeLineSeries::append(qreal x, qreal y)
    self.uglySide.call('ritual_ZN21DeclarativeLineSeries6appendEdd', x, y)

  @overload(float, float, float, float)
  def replace(
      self,
      oldX: float,
      oldY: float,
      newX: float,
      newY: float,
  ) -> None:
    """
    Calls Qt's 'void DeclarativeLineSeries::replace(qreal oldX, qreal oldY,
    qreal newX, qreal newY)'.

    Qt's own words: https://doc.qt.io/qt-6/declarativelineseries.html#replace

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
    #  void DeclarativeLineSeries::replace(qreal oldX, qreal oldY, qreal
    #      newX, qreal newY)
    self.uglySide.call(
        'ritual_ZN21DeclarativeLineSeries7replaceEdddd',
        oldX, oldY, newX, newY,
    )

  @overload(int, float, float)
  def replace(self, index: int, newX: float, newY: float) -> None:
    """
    Calls Qt's 'void DeclarativeLineSeries::replace(int index, qreal newX,
    qreal newY)'.

    Qt's own words: https://doc.qt.io/qt-6/declarativelineseries.html#replace

    Parameters
    ----------

    index : int
      Passed on as it is.

    newX : float
      Passed on as it is.

    newY : float
      Passed on as it is.
    """
    #  void DeclarativeLineSeries::replace(int index, qreal newX, qreal newY)
    self.uglySide.call(
        'ritual_ZN21DeclarativeLineSeries7replaceEidd', index, newX, newY,
    )

  @overload(float, float)
  def remove(self, x: float, y: float) -> None:
    """
    Calls Qt's 'void DeclarativeLineSeries::remove(qreal x, qreal y)'.

    Qt's own words: https://doc.qt.io/qt-6/declarativelineseries.html#remove

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.
    """
    #  void DeclarativeLineSeries::remove(qreal x, qreal y)
    self.uglySide.call('ritual_ZN21DeclarativeLineSeries6removeEdd', x, y)

  @overload(int)
  def remove(self, index: int) -> None:
    """
    Calls Qt's 'void DeclarativeLineSeries::remove(int index)'.

    Qt's own words: https://doc.qt.io/qt-6/declarativelineseries.html#remove

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void DeclarativeLineSeries::remove(int index)
    self.uglySide.call('ritual_ZN21DeclarativeLineSeries6removeEi', index)

  @overload(int, int)
  def removePoints(self, index: int, count: int) -> None:
    """
    Calls Qt's 'void DeclarativeLineSeries::removePoints(int index, int
    count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativelineseries.html#removePoints

    Parameters
    ----------

    index : int
      Passed on as it is.

    count : int
      Passed on as it is.
    """
    #  void DeclarativeLineSeries::removePoints(int index, int count)
    self.uglySide.call(
        'ritual_ZN21DeclarativeLineSeries12removePointsEii', index, count,
    )

  @overload(int, float, float)
  def insert(self, index: int, x: float, y: float) -> None:
    """
    Calls Qt's 'void DeclarativeLineSeries::insert(int index, qreal x, qreal
    y)'.

    Qt's own words: https://doc.qt.io/qt-6/declarativelineseries.html#insert

    Parameters
    ----------

    index : int
      Passed on as it is.

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.
    """
    #  void DeclarativeLineSeries::insert(int index, qreal x, qreal y)
    self.uglySide.call(
        'ritual_ZN21DeclarativeLineSeries6insertEidd', index, x, y,
    )

  def clear(self) -> None:
    """
    Calls Qt's 'void DeclarativeLineSeries::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/declarativelineseries.html#clear
    """
    #  void DeclarativeLineSeries::clear()
    self.uglySide.call('ritual_ZN21DeclarativeLineSeries5clearEv')

  @overload(int)
  def at(self, index: int) -> QPointF:
    """
    Calls Qt's 'QPointF DeclarativeLineSeries::at(int index)'.

    Qt's own words: https://doc.qt.io/qt-6/declarativelineseries.html#at

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF DeclarativeLineSeries::at(int index)
    address = self.uglySide.call(
        'ritual_ZN21DeclarativeLineSeries2atEi', index,
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  @overload(int)
  def countChanged(self, count: int) -> None:
    """
    Calls Qt's 'void DeclarativeLineSeries::countChanged(int count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativelineseries.html#countChanged

    Parameters
    ----------

    count : int
      Passed on as it is.
    """
    #  void DeclarativeLineSeries::countChanged(int count)
    self.uglySide.call(
        'ritual_ZN21DeclarativeLineSeries12countChangedEi', count,
    )

  @overload(QAbstractAxis)
  @overload(NoneType)
  def axisXChanged(self, axis: Optional[QAbstractAxis]) -> None:
    """
    Calls Qt's 'void DeclarativeLineSeries::axisXChanged(QAbstractAxis
    *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativelineseries.html#axisXChanged

    Parameters
    ----------

    axis : Optional[QAbstractAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DeclarativeLineSeries::axisXChanged(QAbstractAxis *axis)
    self.uglySide.call(
        'ritual_ZN21DeclarativeLineSeries12axisXChangedEP13QAbstractAxis',
        self._addressOf(axis),
    )

  @overload(QAbstractAxis)
  @overload(NoneType)
  def axisYChanged(self, axis: Optional[QAbstractAxis]) -> None:
    """
    Calls Qt's 'void DeclarativeLineSeries::axisYChanged(QAbstractAxis
    *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativelineseries.html#axisYChanged

    Parameters
    ----------

    axis : Optional[QAbstractAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DeclarativeLineSeries::axisYChanged(QAbstractAxis *axis)
    self.uglySide.call(
        'ritual_ZN21DeclarativeLineSeries12axisYChangedEP13QAbstractAxis',
        self._addressOf(axis),
    )

  @overload(QAbstractAxis)
  @overload(NoneType)
  def axisXTopChanged(self, axis: Optional[QAbstractAxis]) -> None:
    """
    Calls Qt's 'void DeclarativeLineSeries::axisXTopChanged(QAbstractAxis
    *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativelineseries.html#axisXTopChanged

    Parameters
    ----------

    axis : Optional[QAbstractAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DeclarativeLineSeries::axisXTopChanged(QAbstractAxis *axis)
    self.uglySide.call(
        'ritual_ZN21DeclarativeLineSeries15axisXTopChangedEP13QAbstractAxis',
        self._addressOf(axis),
    )

  @overload(QAbstractAxis)
  @overload(NoneType)
  def axisYRightChanged(self, axis: Optional[QAbstractAxis]) -> None:
    """
    Calls Qt's 'void DeclarativeLineSeries::axisYRightChanged(QAbstractAxis
    *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativelineseries.html#axisYRightChanged

    Parameters
    ----------

    axis : Optional[QAbstractAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DeclarativeLineSeries::axisYRightChanged(QAbstractAxis *axis)
    self.uglySide.call(
        'ritual_ZN21DeclarativeLineSeries17axisYRightChangedEP13QAbstractAx'
        'is',
        self._addressOf(axis),
    )

  @overload(QAbstractAxis)
  @overload(NoneType)
  def axisAngularChanged(self, axis: Optional[QAbstractAxis]) -> None:
    """
    Calls Qt's 'void DeclarativeLineSeries::axisAngularChanged(QAbstractAxis
    *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativelineseries.html#axisAngularChanged

    Parameters
    ----------

    axis : Optional[QAbstractAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DeclarativeLineSeries::axisAngularChanged(QAbstractAxis *axis)
    self.uglySide.call(
        'ritual_ZN21DeclarativeLineSeries18axisAngularChangedEP13QAbstractA'
        'xis',
        self._addressOf(axis),
    )

  @overload(QAbstractAxis)
  @overload(NoneType)
  def axisRadialChanged(self, axis: Optional[QAbstractAxis]) -> None:
    """
    Calls Qt's 'void DeclarativeLineSeries::axisRadialChanged(QAbstractAxis
    *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativelineseries.html#axisRadialChanged

    Parameters
    ----------

    axis : Optional[QAbstractAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DeclarativeLineSeries::axisRadialChanged(QAbstractAxis *axis)
    self.uglySide.call(
        'ritual_ZN21DeclarativeLineSeries17axisRadialChangedEP13QAbstractAx'
        'is',
        self._addressOf(axis),
    )

  @overload(float)
  def widthChanged(self, width: float) -> None:
    """
    Calls Qt's 'void DeclarativeLineSeries::widthChanged(qreal width)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativelineseries.html#widthChanged

    Parameters
    ----------

    width : float
      Passed on as it is.
    """
    #  void DeclarativeLineSeries::widthChanged(qreal width)
    self.uglySide.call(
        'ritual_ZN21DeclarativeLineSeries12widthChangedEd', width,
    )

  @overload(Qt.PenStyle)
  def styleChanged(self, style: Qt.PenStyle) -> None:
    """
    Calls Qt's 'void DeclarativeLineSeries::styleChanged(Qt::PenStyle
    style)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativelineseries.html#styleChanged

    Parameters
    ----------

    style : Qt.PenStyle
      Passed on as its number.
    """
    #  void DeclarativeLineSeries::styleChanged(Qt::PenStyle style)
    self.uglySide.call(
        'ritual_ZN21DeclarativeLineSeries12styleChangedEN2Qt8PenStyleE',
        style.value,
    )

  @overload(Qt.PenCapStyle)
  def capStyleChanged(self, capStyle: Qt.PenCapStyle) -> None:
    """
    Calls Qt's 'void DeclarativeLineSeries::capStyleChanged(Qt::PenCapStyle
    capStyle)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativelineseries.html#capStyleChanged

    Parameters
    ----------

    capStyle : Qt.PenCapStyle
      Passed on as its number.
    """
    #  void DeclarativeLineSeries::capStyleChanged(Qt::PenCapStyle capStyle)
    self.uglySide.call(
        'ritual_ZN21DeclarativeLineSeries15capStyleChangedEN2Qt11PenCapStyl'
        'eE',
        capStyle.value,
    )

  @overload(int)
  def handleCountChanged(self, index: int) -> None:
    """
    Calls Qt's 'void DeclarativeLineSeries::handleCountChanged(int index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativelineseries.html#handleCountChanged

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void DeclarativeLineSeries::handleCountChanged(int index)
    self.uglySide.call(
        'ritual_ZN21DeclarativeLineSeries18handleCountChangedEi', index,
    )

  @staticmethod
  def appendDeclarativeChildren(*__, **_) -> Never:
    """
    Qt's 'void DeclarativeLineSeries::appendDeclarativeChildren(
    QQmlListProperty<QObject> *list, QObject *element)': names
    'QQmlListProperty<QObject>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'DeclarativeLineSeries.appendDeclarativeChildren' has no cute "
        "function yet. Qt's 'void "
        "DeclarativeLineSeries::appendDeclarativeChildren(QQmlListProperty<Q"
        "Object> *list, QObject *element)': names "
        "'QQmlListProperty<QObject>', which has no cute class yet.")

  @staticmethod
  def declarativeChildren(*__, **_) -> Never:
    """
    Qt's 'QQmlListProperty<QObject>
    DeclarativeLineSeries::declarativeChildren()': gives a type Python has no
    way to take yet.
    """
    raise NotImplementedError(
        "'DeclarativeLineSeries.declarativeChildren' has no cute function "
        "yet. Qt's 'QQmlListProperty<QObject> "
        "DeclarativeLineSeries::declarativeChildren()': gives a type Python "
        "has no way to take yet.")
