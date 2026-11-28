"""
DeclarativeHorizontalStackedBarSeries binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtChartsQml/6.12.0/QtChartsQml/private/declarativebarseries_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means DeclarativeHorizontalStackedBarSeries to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList
from ..QtQml import QQmlParserStatus
from ..QtCharts import QHorizontalStackedBarSeries

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QVariant
  from ..QtCharts import QAbstractAxis, QBarSet
  from ..QtQuick import QQuickItem
  from . import DeclarativeBarSet
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAbstractAxis = WAIT['QtCharts:QAbstractAxis']
  QBarSet = WAIT['QtCharts:QBarSet']
  QQuickItem = WAIT['QQuickItem']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class DeclarativeHorizontalStackedBarSeries(QHorizontalStackedBarSeries, QQmlParserStatus):
  """
  The cute side of Qt's DeclarativeHorizontalStackedBarSeries: a plain Python
  object standing in front of one C++ DeclarativeHorizontalStackedBarSeries.

  It is built on the cute 'QHorizontalStackedBarSeries', as Qt's
  DeclarativeHorizontalStackedBarSeries is built on Qt's
  QHorizontalStackedBarSeries, and has everything that class has. It is built
  on the cute 'QQmlParserStatus' as well, as Qt's
  DeclarativeHorizontalStackedBarSeries is built on Qt's QQmlParserStatus
  too, and has everything that class has.

  What exists
  -----------

  Every function of Qt's DeclarativeHorizontalStackedBarSeries that has a
  ritual and that Python can call so far, 21 names in all: 'metaObject',
  'tr', 'axisX', 'setAxisX', 'axisY', 'setAxisY', 'axisXTop', 'setAxisXTop',
  'axisYRight', 'setAxisYRight', 'at', 'append', 'insert', 'remove', 'clear',
  'classBegin', 'componentComplete', 'axisXChanged', 'axisYChanged',
  'axisXTopChanged', 'axisYRightChanged'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *DeclarativeHorizontalStackedBarSeries::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int
    DeclarativeHorizontalStackedBarSeries::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QQmlListProperty<QObject>
    DeclarativeHorizontalStackedBarSeries::seriesChildren()': gives a type
    Python has no way to take yet.
  - Qt's 'void DeclarativeHorizontalStackedBarSeries::appendSeriesChildren(
    QQmlListProperty<QObject> *list, QObject *element)': names
    'QQmlListProperty<QObject>', which has no cute class yet.

  What has no ritual
  ------------------

  2 of the 28 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ DeclarativeHorizontalStackedBarSeries is created at the first
    use, not by 'DeclarativeHorizontalStackedBarSeries(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ DeclarativeHorizontalStackedBarSeries.
  - Qt tells when it has removed the C++
    DeclarativeHorizontalStackedBarSeries. Every call on the cute object, and
    every use of it as an argument, then raises 'RuntimeError', and nothing
    reaches C++.
  - Each name of Qt's DeclarativeHorizontalStackedBarSeries that has no cute
    function yet, 'appendSeriesChildren', 'seriesChildren', holds a function
    that raises 'NotImplementedError', and its docstring says why.
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
    Calls Qt's 'QString DeclarativeHorizontalStackedBarSeries::tr(const char
    *s, const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativehorizontalstackedbarseries.html#tr

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
    #  QString DeclarativeHorizontalStackedBarSeries::tr(const char *s, const
    #      char *c, int n)
    return Rituals.call(
        'ritual_ZN37DeclarativeHorizontalStackedBarSeries2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'DeclarativeHorizontalStackedBarSeries'

  #  Qt's DeclarativeHorizontalStackedBarSeries is built on more than one
  #  class. The part of a C++ DeclarativeHorizontalStackedBarSeries that
  #  belongs to a class after the first begins somewhere inside the object,
  #  and the ritual named for that class gives where; see
  #  'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QQmlParserStatus':
          'ritual_cast_DeclarativeHorizontalStackedBarSeries_QQmlParserStatus',
  }

  #  A C++ DeclarativeHorizontalStackedBarSeries Python makes is of a C++
  #  class of ours, in which Python can take functions over. This ritual
  #  hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_DeclarativeHorizontalStackedBarSeries'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject
    *DeclarativeHorizontalStackedBarSeries::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativehorizontalstackedbarseries.html

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *DeclarativeHorizontalStackedBarSeries::metaObject()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK37DeclarativeHorizontalStackedBarSeries10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QAbstractAxis)
  @overload(NoneType)
  def setAxisX(self, axis: Optional[QAbstractAxis]) -> None:
    """
    Calls Qt's 'void
    DeclarativeHorizontalStackedBarSeries::setAxisX(QAbstractAxis *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativehorizontalstackedbarseries.html

    Parameters
    ----------

    axis : Optional[QAbstractAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DeclarativeHorizontalStackedBarSeries::setAxisX(QAbstractAxis
    #      *axis)
    self.uglySide.call(
        'ritual_ZN37DeclarativeHorizontalStackedBarSeries8setAxisXEP13QAbst'
        'ractAxis',
        self._addressOf(axis),
    )

  @overload(QAbstractAxis)
  @overload(NoneType)
  def setAxisY(self, axis: Optional[QAbstractAxis]) -> None:
    """
    Calls Qt's 'void
    DeclarativeHorizontalStackedBarSeries::setAxisY(QAbstractAxis *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativehorizontalstackedbarseries.html

    Parameters
    ----------

    axis : Optional[QAbstractAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DeclarativeHorizontalStackedBarSeries::setAxisY(QAbstractAxis
    #      *axis)
    self.uglySide.call(
        'ritual_ZN37DeclarativeHorizontalStackedBarSeries8setAxisYEP13QAbst'
        'ractAxis',
        self._addressOf(axis),
    )

  @overload(QAbstractAxis)
  @overload(NoneType)
  def setAxisXTop(self, axis: Optional[QAbstractAxis]) -> None:
    """
    Calls Qt's 'void
    DeclarativeHorizontalStackedBarSeries::setAxisXTop(QAbstractAxis *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativehorizontalstackedbarseries.html

    Parameters
    ----------

    axis : Optional[QAbstractAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DeclarativeHorizontalStackedBarSeries::setAxisXTop(QAbstractAxis
    #      *axis)
    self.uglySide.call(
        'ritual_ZN37DeclarativeHorizontalStackedBarSeries11setAxisXTopEP13Q'
        'AbstractAxis',
        self._addressOf(axis),
    )

  @overload(QAbstractAxis)
  @overload(NoneType)
  def setAxisYRight(self, axis: Optional[QAbstractAxis]) -> None:
    """
    Calls Qt's 'void
    DeclarativeHorizontalStackedBarSeries::setAxisYRight(QAbstractAxis
    *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativehorizontalstackedbarseries.html

    Parameters
    ----------

    axis : Optional[QAbstractAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void
    #      DeclarativeHorizontalStackedBarSeries::setAxisYRight(QAbstractAxis
    #      *axis)
    self.uglySide.call(
        'ritual_ZN37DeclarativeHorizontalStackedBarSeries13setAxisYRightEP1'
        '3QAbstractAxis',
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
  @overload(QQuickItem)
  @overload(NoneType)
  def __init__(self, parent: Optional[QQuickItem] = None) -> None:
    """
    Notes what was given, for Qt's 'DeclarativeHorizontalStackedBarSeries::
    DeclarativeHorizontalStackedBarSeries(QQuickItem *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativehorizontalstackedbarseries.html

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  DeclarativeHorizontalStackedBarSeries::
    #      DeclarativeHorizontalStackedBarSeries(QQuickItem *parent)
    self._noteCreation(
        DeclarativeHorizontalStackedBarSeries, lambda: Rituals.call(
            'ritual_ZN37DeclarativeHorizontalStackedBarSeriesC1EP10QQuickIt'
            'em',
            self._addressOf(parent),
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

  def axisX(self) -> Optional[QAbstractAxis]:
    """
    Calls Qt's 'QAbstractAxis
    *DeclarativeHorizontalStackedBarSeries::axisX()'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativehorizontalstackedbarseries.html#axisX

    Returns
    -------

    Optional[QAbstractAxis]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractAxis *DeclarativeHorizontalStackedBarSeries::axisX()
    address = self.uglySide.call(
        'ritual_ZN37DeclarativeHorizontalStackedBarSeries5axisXEv',
    )
    from ..QtCharts import QAbstractAxis
    return QAbstractAxis._cuteAt(address)

  def axisY(self) -> Optional[QAbstractAxis]:
    """
    Calls Qt's 'QAbstractAxis
    *DeclarativeHorizontalStackedBarSeries::axisY()'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativehorizontalstackedbarseries.html#axisY

    Returns
    -------

    Optional[QAbstractAxis]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractAxis *DeclarativeHorizontalStackedBarSeries::axisY()
    address = self.uglySide.call(
        'ritual_ZN37DeclarativeHorizontalStackedBarSeries5axisYEv',
    )
    from ..QtCharts import QAbstractAxis
    return QAbstractAxis._cuteAt(address)

  def axisXTop(self) -> Optional[QAbstractAxis]:
    """
    Calls Qt's 'QAbstractAxis
    *DeclarativeHorizontalStackedBarSeries::axisXTop()'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativehorizontalstackedbarseries.html

    Returns
    -------

    Optional[QAbstractAxis]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractAxis *DeclarativeHorizontalStackedBarSeries::axisXTop()
    address = self.uglySide.call(
        'ritual_ZN37DeclarativeHorizontalStackedBarSeries8axisXTopEv',
    )
    from ..QtCharts import QAbstractAxis
    return QAbstractAxis._cuteAt(address)

  def axisYRight(self) -> Optional[QAbstractAxis]:
    """
    Calls Qt's 'QAbstractAxis
    *DeclarativeHorizontalStackedBarSeries::axisYRight()'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativehorizontalstackedbarseries.html

    Returns
    -------

    Optional[QAbstractAxis]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractAxis *DeclarativeHorizontalStackedBarSeries::axisYRight()
    address = self.uglySide.call(
        'ritual_ZN37DeclarativeHorizontalStackedBarSeries10axisYRightEv',
    )
    from ..QtCharts import QAbstractAxis
    return QAbstractAxis._cuteAt(address)

  @overload(int)
  def at(self, index: int) -> Optional[DeclarativeBarSet]:
    """
    Calls Qt's 'DeclarativeBarSet
    *DeclarativeHorizontalStackedBarSeries::at(int index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativehorizontalstackedbarseries.html#at

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    Optional[DeclarativeBarSet]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DeclarativeBarSet *DeclarativeHorizontalStackedBarSeries::at(int
    #      index)
    address = self.uglySide.call(
        'ritual_ZN37DeclarativeHorizontalStackedBarSeries2atEi', index,
    )
    from . import DeclarativeBarSet
    return DeclarativeBarSet._cuteAt(address)

  @overload(str, QList[QVariant])
  def append(
      self,
      label: str,
      values: QList[QVariant],
  ) -> Optional[DeclarativeBarSet]:
    """
    Calls Qt's 'DeclarativeBarSet
    *DeclarativeHorizontalStackedBarSeries::append(QString label,
    QVariantList values)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativehorizontalstackedbarseries.html#append

    Parameters
    ----------

    label : str
      Passed on as it is: a QString is made of it for the call.

    values : QList[QVariant]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    Returns
    -------

    Optional[DeclarativeBarSet]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DeclarativeBarSet
    #      *DeclarativeHorizontalStackedBarSeries::append(QString label,
    #      QVariantList values)
    address = self.uglySide.call(
        'ritual_ZN37DeclarativeHorizontalStackedBarSeries6appendE7QString5Q'
        'ListI8QVariantE',
        label, self._valueOf(values),
    )
    from . import DeclarativeBarSet
    return DeclarativeBarSet._cuteAt(address)

  @overload(int, str, QList[QVariant])
  def insert(
      self,
      index: int,
      label: str,
      values: QList[QVariant],
  ) -> Optional[DeclarativeBarSet]:
    """
    Calls Qt's 'DeclarativeBarSet
    *DeclarativeHorizontalStackedBarSeries::insert(int index, QString label,
    QVariantList values)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativehorizontalstackedbarseries.html#insert

    Parameters
    ----------

    index : int
      Passed on as it is.

    label : str
      Passed on as it is: a QString is made of it for the call.

    values : QList[QVariant]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    Returns
    -------

    Optional[DeclarativeBarSet]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DeclarativeBarSet *DeclarativeHorizontalStackedBarSeries::insert(int
    #      index, QString label, QVariantList values)
    address = self.uglySide.call(
        'ritual_ZN37DeclarativeHorizontalStackedBarSeries6insertEi7QString5'
        'QListI8QVariantE',
        index, label, self._valueOf(values),
    )
    from . import DeclarativeBarSet
    return DeclarativeBarSet._cuteAt(address)

  @overload(QBarSet)
  @overload(NoneType)
  def remove(self, barset: Optional[QBarSet]) -> bool:
    """
    Calls Qt's 'bool DeclarativeHorizontalStackedBarSeries::remove(QBarSet
    *barset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativehorizontalstackedbarseries.html#remove

    Parameters
    ----------

    barset : Optional[QBarSet]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool DeclarativeHorizontalStackedBarSeries::remove(QBarSet *barset)
    return self.uglySide.call(
        'ritual_ZN37DeclarativeHorizontalStackedBarSeries6removeEP7QBarSet',
        self._addressOf(barset),
    )

  def clear(self) -> None:
    """
    Calls Qt's 'void DeclarativeHorizontalStackedBarSeries::clear()'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativehorizontalstackedbarseries.html#clear
    """
    #  void DeclarativeHorizontalStackedBarSeries::clear()
    self.uglySide.call(
        'ritual_ZN37DeclarativeHorizontalStackedBarSeries5clearEv',
    )

  def classBegin(self) -> None:
    """
    Calls Qt's 'void DeclarativeHorizontalStackedBarSeries::classBegin()'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativehorizontalstackedbarseries.html
    """
    #  void DeclarativeHorizontalStackedBarSeries::classBegin()
    ritual = 'ritual_ZN37DeclarativeHorizontalStackedBarSeries10classBeginEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN37DeclarativeHorizontalStackedBarSeries10classBegin'
          'Ev')
    self.uglySide.call(ritual)

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void
    DeclarativeHorizontalStackedBarSeries::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativehorizontalstackedbarseries.html
    """
    #  void DeclarativeHorizontalStackedBarSeries::componentComplete()
    ritual = (
        'ritual_ZN37DeclarativeHorizontalStackedBarSeries17componentComplet'
        'eEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN37DeclarativeHorizontalStackedBarSeries17componentC'
          'ompleteEv')
    self.uglySide.call(ritual)

  @overload(QAbstractAxis)
  @overload(NoneType)
  def axisXChanged(self, axis: Optional[QAbstractAxis]) -> None:
    """
    Calls Qt's 'void
    DeclarativeHorizontalStackedBarSeries::axisXChanged(QAbstractAxis
    *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativehorizontalstackedbarseries.html

    Parameters
    ----------

    axis : Optional[QAbstractAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DeclarativeHorizontalStackedBarSeries::axisXChanged(QAbstractAxis
    #      *axis)
    self.uglySide.call(
        'ritual_ZN37DeclarativeHorizontalStackedBarSeries12axisXChangedEP13'
        'QAbstractAxis',
        self._addressOf(axis),
    )

  @overload(QAbstractAxis)
  @overload(NoneType)
  def axisYChanged(self, axis: Optional[QAbstractAxis]) -> None:
    """
    Calls Qt's 'void
    DeclarativeHorizontalStackedBarSeries::axisYChanged(QAbstractAxis
    *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativehorizontalstackedbarseries.html

    Parameters
    ----------

    axis : Optional[QAbstractAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DeclarativeHorizontalStackedBarSeries::axisYChanged(QAbstractAxis
    #      *axis)
    self.uglySide.call(
        'ritual_ZN37DeclarativeHorizontalStackedBarSeries12axisYChangedEP13'
        'QAbstractAxis',
        self._addressOf(axis),
    )

  @overload(QAbstractAxis)
  @overload(NoneType)
  def axisXTopChanged(self, axis: Optional[QAbstractAxis]) -> None:
    """
    Calls Qt's 'void
    DeclarativeHorizontalStackedBarSeries::axisXTopChanged(QAbstractAxis
    *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativehorizontalstackedbarseries.html

    Parameters
    ----------

    axis : Optional[QAbstractAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DeclarativeHorizontalStackedBarSeries::axisXTopChanged(
    #      QAbstractAxis *axis)
    self.uglySide.call(
        'ritual_ZN37DeclarativeHorizontalStackedBarSeries15axisXTopChangedE'
        'P13QAbstractAxis',
        self._addressOf(axis),
    )

  @overload(QAbstractAxis)
  @overload(NoneType)
  def axisYRightChanged(self, axis: Optional[QAbstractAxis]) -> None:
    """
    Calls Qt's 'void
    DeclarativeHorizontalStackedBarSeries::axisYRightChanged(QAbstractAxis
    *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativehorizontalstackedbarseries.html

    Parameters
    ----------

    axis : Optional[QAbstractAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DeclarativeHorizontalStackedBarSeries::axisYRightChanged(
    #      QAbstractAxis *axis)
    self.uglySide.call(
        'ritual_ZN37DeclarativeHorizontalStackedBarSeries17axisYRightChange'
        'dEP13QAbstractAxis',
        self._addressOf(axis),
    )

  @staticmethod
  def appendSeriesChildren(*__, **_) -> Never:
    """
    Qt's 'void DeclarativeHorizontalStackedBarSeries::appendSeriesChildren(
    QQmlListProperty<QObject> *list, QObject *element)': names
    'QQmlListProperty<QObject>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'DeclarativeHorizontalStackedBarSeries.appendSeriesChildren' has "
        "no cute function yet. Qt's 'void "
        "DeclarativeHorizontalStackedBarSeries::appendSeriesChildren(QQmlLis"
        "tProperty<QObject> *list, QObject *element)': names "
        "'QQmlListProperty<QObject>', which has no cute class yet.")

  @staticmethod
  def seriesChildren(*__, **_) -> Never:
    """
    Qt's 'QQmlListProperty<QObject>
    DeclarativeHorizontalStackedBarSeries::seriesChildren()': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'DeclarativeHorizontalStackedBarSeries.seriesChildren' has no cute "
        "function yet. Qt's 'QQmlListProperty<QObject> "
        "DeclarativeHorizontalStackedBarSeries::seriesChildren()': gives a "
        "type Python has no way to take yet.")
