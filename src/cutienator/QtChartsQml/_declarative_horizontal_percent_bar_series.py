"""
DeclarativeHorizontalPercentBarSeries binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtChartsQml/6.12.0/QtChartsQml/private/declarativebarseries_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means DeclarativeHorizontalPercentBarSeries to be private: it declares
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
from ..QtCharts import QHorizontalPercentBarSeries

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


class DeclarativeHorizontalPercentBarSeries(QHorizontalPercentBarSeries, QQmlParserStatus):
  """
  The cute side of Qt's DeclarativeHorizontalPercentBarSeries: a plain Python
  object standing in front of one C++ DeclarativeHorizontalPercentBarSeries.

  It is built on the cute 'QHorizontalPercentBarSeries', as Qt's
  DeclarativeHorizontalPercentBarSeries is built on Qt's
  QHorizontalPercentBarSeries, and has everything that class has. It is built
  on the cute 'QQmlParserStatus' as well, as Qt's
  DeclarativeHorizontalPercentBarSeries is built on Qt's QQmlParserStatus
  too, and has everything that class has.

  What exists
  -----------

  Every function of Qt's DeclarativeHorizontalPercentBarSeries that has a
  ritual and that Python can call so far, 21 names in all: 'metaObject',
  'tr', 'axisX', 'setAxisX', 'axisY', 'setAxisY', 'axisXTop', 'setAxisXTop',
  'axisYRight', 'setAxisYRight', 'at', 'append', 'insert', 'remove', 'clear',
  'classBegin', 'componentComplete', 'axisXChanged', 'axisYChanged',
  'axisXTopChanged', 'axisYRightChanged'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *DeclarativeHorizontalPercentBarSeries::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int
    DeclarativeHorizontalPercentBarSeries::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QQmlListProperty<QObject>
    DeclarativeHorizontalPercentBarSeries::seriesChildren()': gives a type
    Python has no way to take yet.
  - Qt's 'void DeclarativeHorizontalPercentBarSeries::appendSeriesChildren(
    QQmlListProperty<QObject> *list, QObject *element)': names
    'QQmlListProperty<QObject>', which has no cute class yet.

  What has no ritual
  ------------------

  2 of the 28 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ DeclarativeHorizontalPercentBarSeries is created at the first
    use, not by 'DeclarativeHorizontalPercentBarSeries(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ DeclarativeHorizontalPercentBarSeries.
  - Qt tells when it has removed the C++
    DeclarativeHorizontalPercentBarSeries. Every call on the cute object, and
    every use of it as an argument, then raises 'RuntimeError', and nothing
    reaches C++.
  - Each name of Qt's DeclarativeHorizontalPercentBarSeries that has no cute
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
    Calls Qt's 'QString DeclarativeHorizontalPercentBarSeries::tr(const char
    *s, const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativehorizontalpercentbarseries.html#tr

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
    #  QString DeclarativeHorizontalPercentBarSeries::tr(const char *s, const
    #      char *c, int n)
    return Rituals.call(
        'ritual_ZN37DeclarativeHorizontalPercentBarSeries2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'DeclarativeHorizontalPercentBarSeries'

  #  Qt's DeclarativeHorizontalPercentBarSeries is built on more than one
  #  class. The part of a C++ DeclarativeHorizontalPercentBarSeries that
  #  belongs to a class after the first begins somewhere inside the object,
  #  and the ritual named for that class gives where; see
  #  'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QQmlParserStatus':
          'ritual_cast_DeclarativeHorizontalPercentBarSeries_QQmlParserStatus',
  }

  #  A C++ DeclarativeHorizontalPercentBarSeries Python makes is of a C++
  #  class of ours, in which Python can take functions over. This ritual
  #  hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_DeclarativeHorizontalPercentBarSeries'

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
    *DeclarativeHorizontalPercentBarSeries::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativehorizontalpercentbarseries.html

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *DeclarativeHorizontalPercentBarSeries::metaObject()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK37DeclarativeHorizontalPercentBarSeries10metaObjectEv',
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
    DeclarativeHorizontalPercentBarSeries::setAxisX(QAbstractAxis *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativehorizontalpercentbarseries.html

    Parameters
    ----------

    axis : Optional[QAbstractAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DeclarativeHorizontalPercentBarSeries::setAxisX(QAbstractAxis
    #      *axis)
    self.uglySide.call(
        'ritual_ZN37DeclarativeHorizontalPercentBarSeries8setAxisXEP13QAbst'
        'ractAxis',
        self._addressOf(axis),
    )

  @overload(QAbstractAxis)
  @overload(NoneType)
  def setAxisY(self, axis: Optional[QAbstractAxis]) -> None:
    """
    Calls Qt's 'void
    DeclarativeHorizontalPercentBarSeries::setAxisY(QAbstractAxis *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativehorizontalpercentbarseries.html

    Parameters
    ----------

    axis : Optional[QAbstractAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DeclarativeHorizontalPercentBarSeries::setAxisY(QAbstractAxis
    #      *axis)
    self.uglySide.call(
        'ritual_ZN37DeclarativeHorizontalPercentBarSeries8setAxisYEP13QAbst'
        'ractAxis',
        self._addressOf(axis),
    )

  @overload(QAbstractAxis)
  @overload(NoneType)
  def setAxisXTop(self, axis: Optional[QAbstractAxis]) -> None:
    """
    Calls Qt's 'void
    DeclarativeHorizontalPercentBarSeries::setAxisXTop(QAbstractAxis *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativehorizontalpercentbarseries.html

    Parameters
    ----------

    axis : Optional[QAbstractAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DeclarativeHorizontalPercentBarSeries::setAxisXTop(QAbstractAxis
    #      *axis)
    self.uglySide.call(
        'ritual_ZN37DeclarativeHorizontalPercentBarSeries11setAxisXTopEP13Q'
        'AbstractAxis',
        self._addressOf(axis),
    )

  @overload(QAbstractAxis)
  @overload(NoneType)
  def setAxisYRight(self, axis: Optional[QAbstractAxis]) -> None:
    """
    Calls Qt's 'void
    DeclarativeHorizontalPercentBarSeries::setAxisYRight(QAbstractAxis
    *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativehorizontalpercentbarseries.html

    Parameters
    ----------

    axis : Optional[QAbstractAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void
    #      DeclarativeHorizontalPercentBarSeries::setAxisYRight(QAbstractAxis
    #      *axis)
    self.uglySide.call(
        'ritual_ZN37DeclarativeHorizontalPercentBarSeries13setAxisYRightEP1'
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
    Notes what was given, for Qt's 'DeclarativeHorizontalPercentBarSeries::
    DeclarativeHorizontalPercentBarSeries(QQuickItem *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativehorizontalpercentbarseries.html

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  DeclarativeHorizontalPercentBarSeries::
    #      DeclarativeHorizontalPercentBarSeries(QQuickItem *parent)
    self._noteCreation(
        DeclarativeHorizontalPercentBarSeries, lambda: Rituals.call(
            'ritual_ZN37DeclarativeHorizontalPercentBarSeriesC1EP10QQuickIt'
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
    *DeclarativeHorizontalPercentBarSeries::axisX()'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativehorizontalpercentbarseries.html#axisX

    Returns
    -------

    Optional[QAbstractAxis]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractAxis *DeclarativeHorizontalPercentBarSeries::axisX()
    address = self.uglySide.call(
        'ritual_ZN37DeclarativeHorizontalPercentBarSeries5axisXEv',
    )
    from ..QtCharts import QAbstractAxis
    return QAbstractAxis._cuteAt(address)

  def axisY(self) -> Optional[QAbstractAxis]:
    """
    Calls Qt's 'QAbstractAxis
    *DeclarativeHorizontalPercentBarSeries::axisY()'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativehorizontalpercentbarseries.html#axisY

    Returns
    -------

    Optional[QAbstractAxis]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractAxis *DeclarativeHorizontalPercentBarSeries::axisY()
    address = self.uglySide.call(
        'ritual_ZN37DeclarativeHorizontalPercentBarSeries5axisYEv',
    )
    from ..QtCharts import QAbstractAxis
    return QAbstractAxis._cuteAt(address)

  def axisXTop(self) -> Optional[QAbstractAxis]:
    """
    Calls Qt's 'QAbstractAxis
    *DeclarativeHorizontalPercentBarSeries::axisXTop()'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativehorizontalpercentbarseries.html

    Returns
    -------

    Optional[QAbstractAxis]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractAxis *DeclarativeHorizontalPercentBarSeries::axisXTop()
    address = self.uglySide.call(
        'ritual_ZN37DeclarativeHorizontalPercentBarSeries8axisXTopEv',
    )
    from ..QtCharts import QAbstractAxis
    return QAbstractAxis._cuteAt(address)

  def axisYRight(self) -> Optional[QAbstractAxis]:
    """
    Calls Qt's 'QAbstractAxis
    *DeclarativeHorizontalPercentBarSeries::axisYRight()'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativehorizontalpercentbarseries.html

    Returns
    -------

    Optional[QAbstractAxis]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractAxis *DeclarativeHorizontalPercentBarSeries::axisYRight()
    address = self.uglySide.call(
        'ritual_ZN37DeclarativeHorizontalPercentBarSeries10axisYRightEv',
    )
    from ..QtCharts import QAbstractAxis
    return QAbstractAxis._cuteAt(address)

  @overload(int)
  def at(self, index: int) -> Optional[DeclarativeBarSet]:
    """
    Calls Qt's 'DeclarativeBarSet
    *DeclarativeHorizontalPercentBarSeries::at(int index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativehorizontalpercentbarseries.html#at

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
    #  DeclarativeBarSet *DeclarativeHorizontalPercentBarSeries::at(int
    #      index)
    address = self.uglySide.call(
        'ritual_ZN37DeclarativeHorizontalPercentBarSeries2atEi', index,
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
    *DeclarativeHorizontalPercentBarSeries::append(QString label,
    QVariantList values)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativehorizontalpercentbarseries.html#append

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
    #      *DeclarativeHorizontalPercentBarSeries::append(QString label,
    #      QVariantList values)
    address = self.uglySide.call(
        'ritual_ZN37DeclarativeHorizontalPercentBarSeries6appendE7QString5Q'
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
    *DeclarativeHorizontalPercentBarSeries::insert(int index, QString label,
    QVariantList values)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativehorizontalpercentbarseries.html#insert

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
    #  DeclarativeBarSet *DeclarativeHorizontalPercentBarSeries::insert(int
    #      index, QString label, QVariantList values)
    address = self.uglySide.call(
        'ritual_ZN37DeclarativeHorizontalPercentBarSeries6insertEi7QString5'
        'QListI8QVariantE',
        index, label, self._valueOf(values),
    )
    from . import DeclarativeBarSet
    return DeclarativeBarSet._cuteAt(address)

  @overload(QBarSet)
  @overload(NoneType)
  def remove(self, barset: Optional[QBarSet]) -> bool:
    """
    Calls Qt's 'bool DeclarativeHorizontalPercentBarSeries::remove(QBarSet
    *barset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativehorizontalpercentbarseries.html#remove

    Parameters
    ----------

    barset : Optional[QBarSet]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool DeclarativeHorizontalPercentBarSeries::remove(QBarSet *barset)
    return self.uglySide.call(
        'ritual_ZN37DeclarativeHorizontalPercentBarSeries6removeEP7QBarSet',
        self._addressOf(barset),
    )

  def clear(self) -> None:
    """
    Calls Qt's 'void DeclarativeHorizontalPercentBarSeries::clear()'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativehorizontalpercentbarseries.html#clear
    """
    #  void DeclarativeHorizontalPercentBarSeries::clear()
    self.uglySide.call(
        'ritual_ZN37DeclarativeHorizontalPercentBarSeries5clearEv',
    )

  def classBegin(self) -> None:
    """
    Calls Qt's 'void DeclarativeHorizontalPercentBarSeries::classBegin()'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativehorizontalpercentbarseries.html
    """
    #  void DeclarativeHorizontalPercentBarSeries::classBegin()
    ritual = 'ritual_ZN37DeclarativeHorizontalPercentBarSeries10classBeginEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN37DeclarativeHorizontalPercentBarSeries10classBegin'
          'Ev')
    self.uglySide.call(ritual)

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void
    DeclarativeHorizontalPercentBarSeries::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativehorizontalpercentbarseries.html
    """
    #  void DeclarativeHorizontalPercentBarSeries::componentComplete()
    ritual = (
        'ritual_ZN37DeclarativeHorizontalPercentBarSeries17componentComplet'
        'eEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN37DeclarativeHorizontalPercentBarSeries17componentC'
          'ompleteEv')
    self.uglySide.call(ritual)

  @overload(QAbstractAxis)
  @overload(NoneType)
  def axisXChanged(self, axis: Optional[QAbstractAxis]) -> None:
    """
    Calls Qt's 'void
    DeclarativeHorizontalPercentBarSeries::axisXChanged(QAbstractAxis
    *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativehorizontalpercentbarseries.html

    Parameters
    ----------

    axis : Optional[QAbstractAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DeclarativeHorizontalPercentBarSeries::axisXChanged(QAbstractAxis
    #      *axis)
    self.uglySide.call(
        'ritual_ZN37DeclarativeHorizontalPercentBarSeries12axisXChangedEP13'
        'QAbstractAxis',
        self._addressOf(axis),
    )

  @overload(QAbstractAxis)
  @overload(NoneType)
  def axisYChanged(self, axis: Optional[QAbstractAxis]) -> None:
    """
    Calls Qt's 'void
    DeclarativeHorizontalPercentBarSeries::axisYChanged(QAbstractAxis
    *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativehorizontalpercentbarseries.html

    Parameters
    ----------

    axis : Optional[QAbstractAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DeclarativeHorizontalPercentBarSeries::axisYChanged(QAbstractAxis
    #      *axis)
    self.uglySide.call(
        'ritual_ZN37DeclarativeHorizontalPercentBarSeries12axisYChangedEP13'
        'QAbstractAxis',
        self._addressOf(axis),
    )

  @overload(QAbstractAxis)
  @overload(NoneType)
  def axisXTopChanged(self, axis: Optional[QAbstractAxis]) -> None:
    """
    Calls Qt's 'void
    DeclarativeHorizontalPercentBarSeries::axisXTopChanged(QAbstractAxis
    *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativehorizontalpercentbarseries.html

    Parameters
    ----------

    axis : Optional[QAbstractAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DeclarativeHorizontalPercentBarSeries::axisXTopChanged(
    #      QAbstractAxis *axis)
    self.uglySide.call(
        'ritual_ZN37DeclarativeHorizontalPercentBarSeries15axisXTopChangedE'
        'P13QAbstractAxis',
        self._addressOf(axis),
    )

  @overload(QAbstractAxis)
  @overload(NoneType)
  def axisYRightChanged(self, axis: Optional[QAbstractAxis]) -> None:
    """
    Calls Qt's 'void
    DeclarativeHorizontalPercentBarSeries::axisYRightChanged(QAbstractAxis
    *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativehorizontalpercentbarseries.html

    Parameters
    ----------

    axis : Optional[QAbstractAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DeclarativeHorizontalPercentBarSeries::axisYRightChanged(
    #      QAbstractAxis *axis)
    self.uglySide.call(
        'ritual_ZN37DeclarativeHorizontalPercentBarSeries17axisYRightChange'
        'dEP13QAbstractAxis',
        self._addressOf(axis),
    )

  @staticmethod
  def appendSeriesChildren(*__, **_) -> Never:
    """
    Qt's 'void DeclarativeHorizontalPercentBarSeries::appendSeriesChildren(
    QQmlListProperty<QObject> *list, QObject *element)': names
    'QQmlListProperty<QObject>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'DeclarativeHorizontalPercentBarSeries.appendSeriesChildren' has "
        "no cute function yet. Qt's 'void "
        "DeclarativeHorizontalPercentBarSeries::appendSeriesChildren(QQmlLis"
        "tProperty<QObject> *list, QObject *element)': names "
        "'QQmlListProperty<QObject>', which has no cute class yet.")

  @staticmethod
  def seriesChildren(*__, **_) -> Never:
    """
    Qt's 'QQmlListProperty<QObject>
    DeclarativeHorizontalPercentBarSeries::seriesChildren()': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'DeclarativeHorizontalPercentBarSeries.seriesChildren' has no cute "
        "function yet. Qt's 'QQmlListProperty<QObject> "
        "DeclarativeHorizontalPercentBarSeries::seriesChildren()': gives a "
        "type Python has no way to take yet.")
