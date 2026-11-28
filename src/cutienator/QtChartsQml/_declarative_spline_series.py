"""
DeclarativeSplineSeries binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtChartsQml/6.12.0/QtChartsQml/private/declarativesplineseries_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means DeclarativeSplineSeries to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QObject
from ..QtQml import QQmlParserStatus
from ..QtCharts import QSplineSeries, QXYSeries
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


class DeclarativeSplineSeries(QSplineSeries, DeclarativeXySeries, QQmlParserStatus):
  """
  The cute side of Qt's DeclarativeSplineSeries: a plain Python object
  standing in front of one C++ DeclarativeSplineSeries.

  It is built on the cute 'QSplineSeries', as Qt's DeclarativeSplineSeries is
  built on Qt's QSplineSeries, and has everything that class has. It is built
  on the cute 'DeclarativeXySeries' as well, as Qt's DeclarativeSplineSeries
  is built on Qt's DeclarativeXySeries too, and has everything that class
  has. It is built on the cute 'QQmlParserStatus' as well, as Qt's
  DeclarativeSplineSeries is built on Qt's QQmlParserStatus too, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's DeclarativeSplineSeries that has a ritual and that
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

  - Qt's 'void *DeclarativeSplineSeries::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int DeclarativeSplineSeries::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QQmlListProperty<QObject>
    DeclarativeSplineSeries::declarativeChildren()': gives a type Python has
    no way to take yet.
  - Qt's 'void DeclarativeSplineSeries::appendDeclarativeChildren(
    QQmlListProperty<QObject> *list, QObject *element)': names
    'QQmlListProperty<QObject>', which has no cute class yet.

  What has no ritual
  ------------------

  2 of the 50 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ DeclarativeSplineSeries is created at the first use, not by
    'DeclarativeSplineSeries(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ DeclarativeSplineSeries.
  - Qt tells when it has removed the C++ DeclarativeSplineSeries. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's DeclarativeSplineSeries that has no cute function yet,
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
    Calls Qt's 'QString DeclarativeSplineSeries::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/declarativesplineseries.html#tr

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
    #  QString DeclarativeSplineSeries::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN23DeclarativeSplineSeries2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'DeclarativeSplineSeries'

  #  Qt's DeclarativeSplineSeries is built on more than one class. The part
  #  of a C++ DeclarativeSplineSeries that belongs to a class after the first
  #  begins somewhere inside the object, and the ritual named for that class
  #  gives where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'DeclarativeXySeries':
          'ritual_cast_DeclarativeSplineSeries_DeclarativeXySeries',
      'QQmlParserStatus':
          'ritual_cast_DeclarativeSplineSeries_QQmlParserStatus',
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
    Calls Qt's 'const QMetaObject *DeclarativeSplineSeries::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativesplineseries.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *DeclarativeSplineSeries::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK23DeclarativeSplineSeries10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def width(self) -> float:
    """
    Calls Qt's 'qreal DeclarativeSplineSeries::width() const'.

    Qt's own words: https://doc.qt.io/qt-6/declarativesplineseries.html#width
    """
    #  qreal DeclarativeSplineSeries::width() const
    return self.uglySide.call('ritual_ZNK23DeclarativeSplineSeries5widthEv')

  def style(self) -> Qt.PenStyle:
    """
    Calls Qt's 'Qt::PenStyle DeclarativeSplineSeries::style() const'.

    Qt's own words: https://doc.qt.io/qt-6/declarativesplineseries.html#style

    Returns
    -------

    Qt.PenStyle
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.PenStyle(number)'
      gives.
    """
    #  Qt::PenStyle DeclarativeSplineSeries::style() const
    return Qt.PenStyle(self.uglySide.call(
        'ritual_ZNK23DeclarativeSplineSeries5styleEv',
    ))

  def capStyle(self) -> Qt.PenCapStyle:
    """
    Calls Qt's 'Qt::PenCapStyle DeclarativeSplineSeries::capStyle() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativesplineseries.html#capStyle

    Returns
    -------

    Qt.PenCapStyle
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.PenCapStyle(number)'
      gives.
    """
    #  Qt::PenCapStyle DeclarativeSplineSeries::capStyle() const
    return Qt.PenCapStyle(self.uglySide.call(
        'ritual_ZNK23DeclarativeSplineSeries8capStyleEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QAbstractAxis)
  @overload(NoneType)
  def setAxisX(self, axis: Optional[QAbstractAxis]) -> None:
    """
    Calls Qt's 'void DeclarativeSplineSeries::setAxisX(QAbstractAxis *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativesplineseries.html#setAxisX

    Parameters
    ----------

    axis : Optional[QAbstractAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DeclarativeSplineSeries::setAxisX(QAbstractAxis *axis)
    self.uglySide.call(
        'ritual_ZN23DeclarativeSplineSeries8setAxisXEP13QAbstractAxis',
        self._addressOf(axis),
    )

  @overload(QAbstractAxis)
  @overload(NoneType)
  def setAxisY(self, axis: Optional[QAbstractAxis]) -> None:
    """
    Calls Qt's 'void DeclarativeSplineSeries::setAxisY(QAbstractAxis *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativesplineseries.html#setAxisY

    Parameters
    ----------

    axis : Optional[QAbstractAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DeclarativeSplineSeries::setAxisY(QAbstractAxis *axis)
    self.uglySide.call(
        'ritual_ZN23DeclarativeSplineSeries8setAxisYEP13QAbstractAxis',
        self._addressOf(axis),
    )

  @overload(QAbstractAxis)
  @overload(NoneType)
  def setAxisXTop(self, axis: Optional[QAbstractAxis]) -> None:
    """
    Calls Qt's 'void DeclarativeSplineSeries::setAxisXTop(QAbstractAxis
    *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativesplineseries.html#setAxisXTop

    Parameters
    ----------

    axis : Optional[QAbstractAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DeclarativeSplineSeries::setAxisXTop(QAbstractAxis *axis)
    self.uglySide.call(
        'ritual_ZN23DeclarativeSplineSeries11setAxisXTopEP13QAbstractAxis',
        self._addressOf(axis),
    )

  @overload(QAbstractAxis)
  @overload(NoneType)
  def setAxisYRight(self, axis: Optional[QAbstractAxis]) -> None:
    """
    Calls Qt's 'void DeclarativeSplineSeries::setAxisYRight(QAbstractAxis
    *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativesplineseries.html#setAxisYRight

    Parameters
    ----------

    axis : Optional[QAbstractAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DeclarativeSplineSeries::setAxisYRight(QAbstractAxis *axis)
    self.uglySide.call(
        'ritual_ZN23DeclarativeSplineSeries13setAxisYRightEP13QAbstractAxis',
        self._addressOf(axis),
    )

  @overload(QAbstractAxis)
  @overload(NoneType)
  def setAxisAngular(self, axis: Optional[QAbstractAxis]) -> None:
    """
    Calls Qt's 'void DeclarativeSplineSeries::setAxisAngular(QAbstractAxis
    *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativesplineseries.html#setAxisAngular

    Parameters
    ----------

    axis : Optional[QAbstractAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DeclarativeSplineSeries::setAxisAngular(QAbstractAxis *axis)
    self.uglySide.call(
        'ritual_ZN23DeclarativeSplineSeries14setAxisAngularEP13QAbstractAxi'
        's',
        self._addressOf(axis),
    )

  @overload(QAbstractAxis)
  @overload(NoneType)
  def setAxisRadial(self, axis: Optional[QAbstractAxis]) -> None:
    """
    Calls Qt's 'void DeclarativeSplineSeries::setAxisRadial(QAbstractAxis
    *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativesplineseries.html#setAxisRadial

    Parameters
    ----------

    axis : Optional[QAbstractAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DeclarativeSplineSeries::setAxisRadial(QAbstractAxis *axis)
    self.uglySide.call(
        'ritual_ZN23DeclarativeSplineSeries13setAxisRadialEP13QAbstractAxis',
        self._addressOf(axis),
    )

  @overload(float)
  def setWidth(self, width: float) -> None:
    """
    Calls Qt's 'void DeclarativeSplineSeries::setWidth(qreal width)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativesplineseries.html#setWidth

    Parameters
    ----------

    width : float
      Passed on as it is.
    """
    #  void DeclarativeSplineSeries::setWidth(qreal width)
    self.uglySide.call(
        'ritual_ZN23DeclarativeSplineSeries8setWidthEd', width,
    )

  @overload(Qt.PenStyle)
  def setStyle(self, style: Qt.PenStyle) -> None:
    """
    Calls Qt's 'void DeclarativeSplineSeries::setStyle(Qt::PenStyle style)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativesplineseries.html#setStyle

    Parameters
    ----------

    style : Qt.PenStyle
      Passed on as its number.
    """
    #  void DeclarativeSplineSeries::setStyle(Qt::PenStyle style)
    self.uglySide.call(
        'ritual_ZN23DeclarativeSplineSeries8setStyleEN2Qt8PenStyleE',
        style.value,
    )

  @overload(Qt.PenCapStyle)
  def setCapStyle(self, capStyle: Qt.PenCapStyle) -> None:
    """
    Calls Qt's 'void DeclarativeSplineSeries::setCapStyle(Qt::PenCapStyle
    capStyle)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativesplineseries.html#setCapStyle

    Parameters
    ----------

    capStyle : Qt.PenCapStyle
      Passed on as its number.
    """
    #  void DeclarativeSplineSeries::setCapStyle(Qt::PenCapStyle capStyle)
    self.uglySide.call(
        'ritual_ZN23DeclarativeSplineSeries11setCapStyleEN2Qt11PenCapStyleE',
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
    'DeclarativeSplineSeries::DeclarativeSplineSeries(QObject *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativesplineseries.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  DeclarativeSplineSeries::DeclarativeSplineSeries(QObject *parent)
    self._noteCreation(DeclarativeSplineSeries, lambda: Rituals.call(
        'ritual_ZN23DeclarativeSplineSeriesC1EP7QObject',
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
    Calls Qt's 'QXYSeries *DeclarativeSplineSeries::xySeries()'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativesplineseries.html#xySeries

    Returns
    -------

    Optional[QXYSeries]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QXYSeries *DeclarativeSplineSeries::xySeries()
    ritual = 'ritual_ZN23DeclarativeSplineSeries8xySeriesEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN23DeclarativeSplineSeries8xySeriesEv'
    address = self.uglySide.call(ritual)
    return QXYSeries._cuteAt(address)

  def axisX(self) -> Optional[QAbstractAxis]:
    """
    Calls Qt's 'QAbstractAxis *DeclarativeSplineSeries::axisX()'.

    Qt's own words: https://doc.qt.io/qt-6/declarativesplineseries.html#axisX

    Returns
    -------

    Optional[QAbstractAxis]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractAxis *DeclarativeSplineSeries::axisX()
    address = self.uglySide.call(
        'ritual_ZN23DeclarativeSplineSeries5axisXEv',
    )
    from ..QtCharts import QAbstractAxis
    return QAbstractAxis._cuteAt(address)

  def axisY(self) -> Optional[QAbstractAxis]:
    """
    Calls Qt's 'QAbstractAxis *DeclarativeSplineSeries::axisY()'.

    Qt's own words: https://doc.qt.io/qt-6/declarativesplineseries.html#axisY

    Returns
    -------

    Optional[QAbstractAxis]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractAxis *DeclarativeSplineSeries::axisY()
    address = self.uglySide.call(
        'ritual_ZN23DeclarativeSplineSeries5axisYEv',
    )
    from ..QtCharts import QAbstractAxis
    return QAbstractAxis._cuteAt(address)

  def axisXTop(self) -> Optional[QAbstractAxis]:
    """
    Calls Qt's 'QAbstractAxis *DeclarativeSplineSeries::axisXTop()'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativesplineseries.html#axisXTop

    Returns
    -------

    Optional[QAbstractAxis]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractAxis *DeclarativeSplineSeries::axisXTop()
    address = self.uglySide.call(
        'ritual_ZN23DeclarativeSplineSeries8axisXTopEv',
    )
    from ..QtCharts import QAbstractAxis
    return QAbstractAxis._cuteAt(address)

  def axisYRight(self) -> Optional[QAbstractAxis]:
    """
    Calls Qt's 'QAbstractAxis *DeclarativeSplineSeries::axisYRight()'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativesplineseries.html#axisYRight

    Returns
    -------

    Optional[QAbstractAxis]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractAxis *DeclarativeSplineSeries::axisYRight()
    address = self.uglySide.call(
        'ritual_ZN23DeclarativeSplineSeries10axisYRightEv',
    )
    from ..QtCharts import QAbstractAxis
    return QAbstractAxis._cuteAt(address)

  def axisAngular(self) -> Optional[QAbstractAxis]:
    """
    Calls Qt's 'QAbstractAxis *DeclarativeSplineSeries::axisAngular()'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativesplineseries.html#axisAngular

    Returns
    -------

    Optional[QAbstractAxis]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractAxis *DeclarativeSplineSeries::axisAngular()
    address = self.uglySide.call(
        'ritual_ZN23DeclarativeSplineSeries11axisAngularEv',
    )
    from ..QtCharts import QAbstractAxis
    return QAbstractAxis._cuteAt(address)

  def axisRadial(self) -> Optional[QAbstractAxis]:
    """
    Calls Qt's 'QAbstractAxis *DeclarativeSplineSeries::axisRadial()'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativesplineseries.html#axisRadial

    Returns
    -------

    Optional[QAbstractAxis]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractAxis *DeclarativeSplineSeries::axisRadial()
    address = self.uglySide.call(
        'ritual_ZN23DeclarativeSplineSeries10axisRadialEv',
    )
    from ..QtCharts import QAbstractAxis
    return QAbstractAxis._cuteAt(address)

  def classBegin(self) -> None:
    """
    Calls Qt's 'void DeclarativeSplineSeries::classBegin()'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativesplineseries.html#classBegin
    """
    #  void DeclarativeSplineSeries::classBegin()
    ritual = 'ritual_ZN23DeclarativeSplineSeries10classBeginEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN23DeclarativeSplineSeries10classBeginEv'
    self.uglySide.call(ritual)

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void DeclarativeSplineSeries::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativesplineseries.html#componentComplete
    """
    #  void DeclarativeSplineSeries::componentComplete()
    ritual = 'ritual_ZN23DeclarativeSplineSeries17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN23DeclarativeSplineSeries17componentCompleteEv'
    self.uglySide.call(ritual)

  @overload(float, float)
  def append(self, x: float, y: float) -> None:
    """
    Calls Qt's 'void DeclarativeSplineSeries::append(qreal x, qreal y)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativesplineseries.html#append

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.
    """
    #  void DeclarativeSplineSeries::append(qreal x, qreal y)
    self.uglySide.call('ritual_ZN23DeclarativeSplineSeries6appendEdd', x, y)

  @overload(float, float, float, float)
  def replace(
      self,
      oldX: float,
      oldY: float,
      newX: float,
      newY: float,
  ) -> None:
    """
    Calls Qt's 'void DeclarativeSplineSeries::replace(qreal oldX, qreal oldY,
    qreal newX, qreal newY)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativesplineseries.html#replace

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
    #  void DeclarativeSplineSeries::replace(qreal oldX, qreal oldY, qreal
    #      newX, qreal newY)
    self.uglySide.call(
        'ritual_ZN23DeclarativeSplineSeries7replaceEdddd',
        oldX, oldY, newX, newY,
    )

  @overload(int, float, float)
  def replace(self, index: int, newX: float, newY: float) -> None:
    """
    Calls Qt's 'void DeclarativeSplineSeries::replace(int index, qreal newX,
    qreal newY)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativesplineseries.html#replace

    Parameters
    ----------

    index : int
      Passed on as it is.

    newX : float
      Passed on as it is.

    newY : float
      Passed on as it is.
    """
    #  void DeclarativeSplineSeries::replace(int index, qreal newX, qreal
    #      newY)
    self.uglySide.call(
        'ritual_ZN23DeclarativeSplineSeries7replaceEidd', index, newX, newY,
    )

  @overload(float, float)
  def remove(self, x: float, y: float) -> None:
    """
    Calls Qt's 'void DeclarativeSplineSeries::remove(qreal x, qreal y)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativesplineseries.html#remove

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.
    """
    #  void DeclarativeSplineSeries::remove(qreal x, qreal y)
    self.uglySide.call('ritual_ZN23DeclarativeSplineSeries6removeEdd', x, y)

  @overload(int)
  def remove(self, index: int) -> None:
    """
    Calls Qt's 'void DeclarativeSplineSeries::remove(int index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativesplineseries.html#remove

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void DeclarativeSplineSeries::remove(int index)
    self.uglySide.call('ritual_ZN23DeclarativeSplineSeries6removeEi', index)

  @overload(int, int)
  def removePoints(self, index: int, count: int) -> None:
    """
    Calls Qt's 'void DeclarativeSplineSeries::removePoints(int index, int
    count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativesplineseries.html#removePoints

    Parameters
    ----------

    index : int
      Passed on as it is.

    count : int
      Passed on as it is.
    """
    #  void DeclarativeSplineSeries::removePoints(int index, int count)
    self.uglySide.call(
        'ritual_ZN23DeclarativeSplineSeries12removePointsEii', index, count,
    )

  @overload(int, float, float)
  def insert(self, index: int, x: float, y: float) -> None:
    """
    Calls Qt's 'void DeclarativeSplineSeries::insert(int index, qreal x,
    qreal y)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativesplineseries.html#insert

    Parameters
    ----------

    index : int
      Passed on as it is.

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.
    """
    #  void DeclarativeSplineSeries::insert(int index, qreal x, qreal y)
    self.uglySide.call(
        'ritual_ZN23DeclarativeSplineSeries6insertEidd', index, x, y,
    )

  def clear(self) -> None:
    """
    Calls Qt's 'void DeclarativeSplineSeries::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/declarativesplineseries.html#clear
    """
    #  void DeclarativeSplineSeries::clear()
    self.uglySide.call('ritual_ZN23DeclarativeSplineSeries5clearEv')

  @overload(int)
  def at(self, index: int) -> QPointF:
    """
    Calls Qt's 'QPointF DeclarativeSplineSeries::at(int index)'.

    Qt's own words: https://doc.qt.io/qt-6/declarativesplineseries.html#at

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF DeclarativeSplineSeries::at(int index)
    address = self.uglySide.call(
        'ritual_ZN23DeclarativeSplineSeries2atEi', index,
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  @overload(int)
  def countChanged(self, count: int) -> None:
    """
    Calls Qt's 'void DeclarativeSplineSeries::countChanged(int count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativesplineseries.html#countChanged

    Parameters
    ----------

    count : int
      Passed on as it is.
    """
    #  void DeclarativeSplineSeries::countChanged(int count)
    self.uglySide.call(
        'ritual_ZN23DeclarativeSplineSeries12countChangedEi', count,
    )

  @overload(QAbstractAxis)
  @overload(NoneType)
  def axisXChanged(self, axis: Optional[QAbstractAxis]) -> None:
    """
    Calls Qt's 'void DeclarativeSplineSeries::axisXChanged(QAbstractAxis
    *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativesplineseries.html#axisXChanged

    Parameters
    ----------

    axis : Optional[QAbstractAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DeclarativeSplineSeries::axisXChanged(QAbstractAxis *axis)
    self.uglySide.call(
        'ritual_ZN23DeclarativeSplineSeries12axisXChangedEP13QAbstractAxis',
        self._addressOf(axis),
    )

  @overload(QAbstractAxis)
  @overload(NoneType)
  def axisYChanged(self, axis: Optional[QAbstractAxis]) -> None:
    """
    Calls Qt's 'void DeclarativeSplineSeries::axisYChanged(QAbstractAxis
    *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativesplineseries.html#axisYChanged

    Parameters
    ----------

    axis : Optional[QAbstractAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DeclarativeSplineSeries::axisYChanged(QAbstractAxis *axis)
    self.uglySide.call(
        'ritual_ZN23DeclarativeSplineSeries12axisYChangedEP13QAbstractAxis',
        self._addressOf(axis),
    )

  @overload(QAbstractAxis)
  @overload(NoneType)
  def axisXTopChanged(self, axis: Optional[QAbstractAxis]) -> None:
    """
    Calls Qt's 'void DeclarativeSplineSeries::axisXTopChanged(QAbstractAxis
    *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativesplineseries.html#axisXTopChanged

    Parameters
    ----------

    axis : Optional[QAbstractAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DeclarativeSplineSeries::axisXTopChanged(QAbstractAxis *axis)
    self.uglySide.call(
        'ritual_ZN23DeclarativeSplineSeries15axisXTopChangedEP13QAbstractAx'
        'is',
        self._addressOf(axis),
    )

  @overload(QAbstractAxis)
  @overload(NoneType)
  def axisYRightChanged(self, axis: Optional[QAbstractAxis]) -> None:
    """
    Calls Qt's 'void DeclarativeSplineSeries::axisYRightChanged(QAbstractAxis
    *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativesplineseries.html#axisYRightChanged

    Parameters
    ----------

    axis : Optional[QAbstractAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DeclarativeSplineSeries::axisYRightChanged(QAbstractAxis *axis)
    self.uglySide.call(
        'ritual_ZN23DeclarativeSplineSeries17axisYRightChangedEP13QAbstract'
        'Axis',
        self._addressOf(axis),
    )

  @overload(QAbstractAxis)
  @overload(NoneType)
  def axisAngularChanged(self, axis: Optional[QAbstractAxis]) -> None:
    """
    Calls Qt's 'void
    DeclarativeSplineSeries::axisAngularChanged(QAbstractAxis *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativesplineseries.html#axisAngularChanged

    Parameters
    ----------

    axis : Optional[QAbstractAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DeclarativeSplineSeries::axisAngularChanged(QAbstractAxis *axis)
    self.uglySide.call(
        'ritual_ZN23DeclarativeSplineSeries18axisAngularChangedEP13QAbstrac'
        'tAxis',
        self._addressOf(axis),
    )

  @overload(QAbstractAxis)
  @overload(NoneType)
  def axisRadialChanged(self, axis: Optional[QAbstractAxis]) -> None:
    """
    Calls Qt's 'void DeclarativeSplineSeries::axisRadialChanged(QAbstractAxis
    *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativesplineseries.html#axisRadialChanged

    Parameters
    ----------

    axis : Optional[QAbstractAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DeclarativeSplineSeries::axisRadialChanged(QAbstractAxis *axis)
    self.uglySide.call(
        'ritual_ZN23DeclarativeSplineSeries17axisRadialChangedEP13QAbstract'
        'Axis',
        self._addressOf(axis),
    )

  @overload(float)
  def widthChanged(self, width: float) -> None:
    """
    Calls Qt's 'void DeclarativeSplineSeries::widthChanged(qreal width)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativesplineseries.html#widthChanged

    Parameters
    ----------

    width : float
      Passed on as it is.
    """
    #  void DeclarativeSplineSeries::widthChanged(qreal width)
    self.uglySide.call(
        'ritual_ZN23DeclarativeSplineSeries12widthChangedEd', width,
    )

  @overload(Qt.PenStyle)
  def styleChanged(self, style: Qt.PenStyle) -> None:
    """
    Calls Qt's 'void DeclarativeSplineSeries::styleChanged(Qt::PenStyle
    style)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativesplineseries.html#styleChanged

    Parameters
    ----------

    style : Qt.PenStyle
      Passed on as its number.
    """
    #  void DeclarativeSplineSeries::styleChanged(Qt::PenStyle style)
    self.uglySide.call(
        'ritual_ZN23DeclarativeSplineSeries12styleChangedEN2Qt8PenStyleE',
        style.value,
    )

  @overload(Qt.PenCapStyle)
  def capStyleChanged(self, capStyle: Qt.PenCapStyle) -> None:
    """
    Calls Qt's 'void DeclarativeSplineSeries::capStyleChanged(Qt::PenCapStyle
    capStyle)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativesplineseries.html#capStyleChanged

    Parameters
    ----------

    capStyle : Qt.PenCapStyle
      Passed on as its number.
    """
    #  void DeclarativeSplineSeries::capStyleChanged(Qt::PenCapStyle
    #      capStyle)
    self.uglySide.call(
        'ritual_ZN23DeclarativeSplineSeries15capStyleChangedEN2Qt11PenCapSt'
        'yleE',
        capStyle.value,
    )

  @overload(int)
  def handleCountChanged(self, index: int) -> None:
    """
    Calls Qt's 'void DeclarativeSplineSeries::handleCountChanged(int index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativesplineseries.html#handleCountChanged

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void DeclarativeSplineSeries::handleCountChanged(int index)
    self.uglySide.call(
        'ritual_ZN23DeclarativeSplineSeries18handleCountChangedEi', index,
    )

  @staticmethod
  def appendDeclarativeChildren(*__, **_) -> Never:
    """
    Qt's 'void DeclarativeSplineSeries::appendDeclarativeChildren(
    QQmlListProperty<QObject> *list, QObject *element)': names
    'QQmlListProperty<QObject>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'DeclarativeSplineSeries.appendDeclarativeChildren' has no cute "
        "function yet. Qt's 'void "
        "DeclarativeSplineSeries::appendDeclarativeChildren(QQmlListProperty"
        "<QObject> *list, QObject *element)': names "
        "'QQmlListProperty<QObject>', which has no cute class yet.")

  @staticmethod
  def declarativeChildren(*__, **_) -> Never:
    """
    Qt's 'QQmlListProperty<QObject>
    DeclarativeSplineSeries::declarativeChildren()': gives a type Python has
    no way to take yet.
    """
    raise NotImplementedError(
        "'DeclarativeSplineSeries.declarativeChildren' has no cute function "
        "yet. Qt's 'QQmlListProperty<QObject> "
        "DeclarativeSplineSeries::declarativeChildren()': gives a type "
        "Python has no way to take yet.")
