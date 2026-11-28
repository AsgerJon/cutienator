"""
DeclarativeBoxPlotSeries binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtChartsQml/6.12.0/QtChartsQml/private/declarativeboxplotseries_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means DeclarativeBoxPlotSeries to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList
from ..QtQml import QQmlParserStatus
from ..QtCharts import QBoxPlotSeries

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QVariant
  from ..QtCharts import QAbstractAxis, QBoxSet
  from ..QtQuick import QQuickItem
  from . import DeclarativeBoxSet
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  DeclarativeBoxSet = WAIT['DeclarativeBoxSet']
  QAbstractAxis = WAIT['QtCharts:QAbstractAxis']
  QBoxSet = WAIT['QBoxSet']
  QQuickItem = WAIT['QQuickItem']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class DeclarativeBoxPlotSeries(QBoxPlotSeries, QQmlParserStatus):
  """
  The cute side of Qt's DeclarativeBoxPlotSeries: a plain Python object
  standing in front of one C++ DeclarativeBoxPlotSeries.

  It is built on the cute 'QBoxPlotSeries', as Qt's DeclarativeBoxPlotSeries
  is built on Qt's QBoxPlotSeries, and has everything that class has. It is
  built on the cute 'QQmlParserStatus' as well, as Qt's
  DeclarativeBoxPlotSeries is built on Qt's QQmlParserStatus too, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's DeclarativeBoxPlotSeries that has a ritual and that
  Python can call so far, 35 names in all: 'metaObject', 'tr', 'axisX',
  'setAxisX', 'axisY', 'setAxisY', 'axisXTop', 'setAxisXTop', 'axisYRight',
  'setAxisYRight', 'brushFilename', 'setBrushFilename', 'at', 'append',
  'insert', 'remove', 'clear', 'classBegin', 'componentComplete',
  'axisXChanged', 'axisYChanged', 'axisXTopChanged', 'axisYRightChanged',
  'clicked', 'hovered', 'pressed', 'released', 'doubleClicked',
  'brushFilenameChanged', 'onHovered', 'onClicked', 'onPressed',
  'onReleased', 'onDoubleClicked', 'handleBrushChanged'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *DeclarativeBoxPlotSeries::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int DeclarativeBoxPlotSeries::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QQmlListProperty<QObject>
    DeclarativeBoxPlotSeries::seriesChildren()': gives a type Python has no
    way to take yet.
  - Qt's 'void
    DeclarativeBoxPlotSeries::appendSeriesChildren(QQmlListProperty<QObject>
    *list, QObject *element)': names 'QQmlListProperty<QObject>', which has
    no cute class yet.

  What has no ritual
  ------------------

  2 of the 43 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ DeclarativeBoxPlotSeries is created at the first use, not by
    'DeclarativeBoxPlotSeries(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ DeclarativeBoxPlotSeries.
  - Qt tells when it has removed the C++ DeclarativeBoxPlotSeries. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's DeclarativeBoxPlotSeries that has no cute function yet,
    'appendSeriesChildren', 'seriesChildren', holds a function that raises
    'NotImplementedError', and its docstring says why.
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
    Calls Qt's 'QString DeclarativeBoxPlotSeries::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/declarativeboxplotseries.html#tr

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
    #  QString DeclarativeBoxPlotSeries::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN24DeclarativeBoxPlotSeries2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'DeclarativeBoxPlotSeries'

  #  Qt's DeclarativeBoxPlotSeries is built on more than one class. The part
  #  of a C++ DeclarativeBoxPlotSeries that belongs to a class after the
  #  first begins somewhere inside the object, and the ritual named for that
  #  class gives where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QQmlParserStatus':
          'ritual_cast_DeclarativeBoxPlotSeries_QQmlParserStatus',
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
    Calls Qt's 'const QMetaObject *DeclarativeBoxPlotSeries::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativeboxplotseries.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *DeclarativeBoxPlotSeries::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK24DeclarativeBoxPlotSeries10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def brushFilename(self) -> str:
    """
    Calls Qt's 'QString DeclarativeBoxPlotSeries::brushFilename() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativeboxplotseries.html#brushFilename

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString DeclarativeBoxPlotSeries::brushFilename() const
    return self.uglySide.call(
        'ritual_ZNK24DeclarativeBoxPlotSeries13brushFilenameEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QAbstractAxis)
  @overload(NoneType)
  def setAxisX(self, axis: Optional[QAbstractAxis]) -> None:
    """
    Calls Qt's 'void DeclarativeBoxPlotSeries::setAxisX(QAbstractAxis
    *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativeboxplotseries.html#setAxisX

    Parameters
    ----------

    axis : Optional[QAbstractAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DeclarativeBoxPlotSeries::setAxisX(QAbstractAxis *axis)
    self.uglySide.call(
        'ritual_ZN24DeclarativeBoxPlotSeries8setAxisXEP13QAbstractAxis',
        self._addressOf(axis),
    )

  @overload(QAbstractAxis)
  @overload(NoneType)
  def setAxisY(self, axis: Optional[QAbstractAxis]) -> None:
    """
    Calls Qt's 'void DeclarativeBoxPlotSeries::setAxisY(QAbstractAxis
    *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativeboxplotseries.html#setAxisY

    Parameters
    ----------

    axis : Optional[QAbstractAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DeclarativeBoxPlotSeries::setAxisY(QAbstractAxis *axis)
    self.uglySide.call(
        'ritual_ZN24DeclarativeBoxPlotSeries8setAxisYEP13QAbstractAxis',
        self._addressOf(axis),
    )

  @overload(QAbstractAxis)
  @overload(NoneType)
  def setAxisXTop(self, axis: Optional[QAbstractAxis]) -> None:
    """
    Calls Qt's 'void DeclarativeBoxPlotSeries::setAxisXTop(QAbstractAxis
    *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativeboxplotseries.html#setAxisXTop

    Parameters
    ----------

    axis : Optional[QAbstractAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DeclarativeBoxPlotSeries::setAxisXTop(QAbstractAxis *axis)
    self.uglySide.call(
        'ritual_ZN24DeclarativeBoxPlotSeries11setAxisXTopEP13QAbstractAxis',
        self._addressOf(axis),
    )

  @overload(QAbstractAxis)
  @overload(NoneType)
  def setAxisYRight(self, axis: Optional[QAbstractAxis]) -> None:
    """
    Calls Qt's 'void DeclarativeBoxPlotSeries::setAxisYRight(QAbstractAxis
    *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativeboxplotseries.html#setAxisYRight

    Parameters
    ----------

    axis : Optional[QAbstractAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DeclarativeBoxPlotSeries::setAxisYRight(QAbstractAxis *axis)
    self.uglySide.call(
        'ritual_ZN24DeclarativeBoxPlotSeries13setAxisYRightEP13QAbstractAxi'
        's',
        self._addressOf(axis),
    )

  @overload(str)
  def setBrushFilename(self, brushFilename: str) -> None:
    """
    Calls Qt's 'void DeclarativeBoxPlotSeries::setBrushFilename(const QString
    &brushFilename)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativeboxplotseries.html#setBrushFilename

    Parameters
    ----------

    brushFilename : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void DeclarativeBoxPlotSeries::setBrushFilename(const QString
    #      &brushFilename)
    self.uglySide.call(
        'ritual_ZN24DeclarativeBoxPlotSeries16setBrushFilenameERK7QString',
        brushFilename,
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
    Notes what was given, for Qt's
    'DeclarativeBoxPlotSeries::DeclarativeBoxPlotSeries(QQuickItem *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativeboxplotseries.html

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  DeclarativeBoxPlotSeries::DeclarativeBoxPlotSeries(QQuickItem *parent)
    self._noteCreation(DeclarativeBoxPlotSeries, lambda: Rituals.call(
        'ritual_ZN24DeclarativeBoxPlotSeriesC1EP10QQuickItem',
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
    Calls Qt's 'QAbstractAxis *DeclarativeBoxPlotSeries::axisX()'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativeboxplotseries.html#axisX

    Returns
    -------

    Optional[QAbstractAxis]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractAxis *DeclarativeBoxPlotSeries::axisX()
    address = self.uglySide.call(
        'ritual_ZN24DeclarativeBoxPlotSeries5axisXEv',
    )
    from ..QtCharts import QAbstractAxis
    return QAbstractAxis._cuteAt(address)

  def axisY(self) -> Optional[QAbstractAxis]:
    """
    Calls Qt's 'QAbstractAxis *DeclarativeBoxPlotSeries::axisY()'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativeboxplotseries.html#axisY

    Returns
    -------

    Optional[QAbstractAxis]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractAxis *DeclarativeBoxPlotSeries::axisY()
    address = self.uglySide.call(
        'ritual_ZN24DeclarativeBoxPlotSeries5axisYEv',
    )
    from ..QtCharts import QAbstractAxis
    return QAbstractAxis._cuteAt(address)

  def axisXTop(self) -> Optional[QAbstractAxis]:
    """
    Calls Qt's 'QAbstractAxis *DeclarativeBoxPlotSeries::axisXTop()'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativeboxplotseries.html#axisXTop

    Returns
    -------

    Optional[QAbstractAxis]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractAxis *DeclarativeBoxPlotSeries::axisXTop()
    address = self.uglySide.call(
        'ritual_ZN24DeclarativeBoxPlotSeries8axisXTopEv',
    )
    from ..QtCharts import QAbstractAxis
    return QAbstractAxis._cuteAt(address)

  def axisYRight(self) -> Optional[QAbstractAxis]:
    """
    Calls Qt's 'QAbstractAxis *DeclarativeBoxPlotSeries::axisYRight()'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativeboxplotseries.html#axisYRight

    Returns
    -------

    Optional[QAbstractAxis]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractAxis *DeclarativeBoxPlotSeries::axisYRight()
    address = self.uglySide.call(
        'ritual_ZN24DeclarativeBoxPlotSeries10axisYRightEv',
    )
    from ..QtCharts import QAbstractAxis
    return QAbstractAxis._cuteAt(address)

  @overload(int)
  def at(self, index: int) -> Optional[DeclarativeBoxSet]:
    """
    Calls Qt's 'DeclarativeBoxSet *DeclarativeBoxPlotSeries::at(int index)'.

    Qt's own words: https://doc.qt.io/qt-6/declarativeboxplotseries.html#at

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    Optional[DeclarativeBoxSet]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DeclarativeBoxSet *DeclarativeBoxPlotSeries::at(int index)
    address = self.uglySide.call(
        'ritual_ZN24DeclarativeBoxPlotSeries2atEi', index,
    )
    from . import DeclarativeBoxSet
    return DeclarativeBoxSet._cuteAt(address)

  @overload(str, QList[QVariant])
  def append(
      self,
      label: str,
      values: QList[QVariant],
  ) -> Optional[DeclarativeBoxSet]:
    """
    Calls Qt's 'DeclarativeBoxSet *DeclarativeBoxPlotSeries::append(const
    QString label, QVariantList values)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativeboxplotseries.html#append

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

    Optional[DeclarativeBoxSet]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DeclarativeBoxSet *DeclarativeBoxPlotSeries::append(const QString
    #      label, QVariantList values)
    address = self.uglySide.call(
        'ritual_ZN24DeclarativeBoxPlotSeries6appendE7QString5QListI8QVarian'
        'tE',
        label, self._valueOf(values),
    )
    from . import DeclarativeBoxSet
    return DeclarativeBoxSet._cuteAt(address)

  @overload(DeclarativeBoxSet)
  @overload(NoneType)
  def append(self, box: Optional[DeclarativeBoxSet]) -> None:
    """
    Calls Qt's 'void DeclarativeBoxPlotSeries::append(DeclarativeBoxSet
    *box)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativeboxplotseries.html#append

    Parameters
    ----------

    box : Optional[DeclarativeBoxSet]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DeclarativeBoxPlotSeries::append(DeclarativeBoxSet *box)
    self.uglySide.call(
        'ritual_ZN24DeclarativeBoxPlotSeries6appendEP17DeclarativeBoxSet',
        self._addressOf(box),
    )

  @overload(int, str, QList[QVariant])
  def insert(
      self,
      index: int,
      label: str,
      values: QList[QVariant],
  ) -> Optional[DeclarativeBoxSet]:
    """
    Calls Qt's 'DeclarativeBoxSet *DeclarativeBoxPlotSeries::insert(int
    index, const QString label, QVariantList values)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativeboxplotseries.html#insert

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

    Optional[DeclarativeBoxSet]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DeclarativeBoxSet *DeclarativeBoxPlotSeries::insert(int index, const
    #      QString label, QVariantList values)
    address = self.uglySide.call(
        'ritual_ZN24DeclarativeBoxPlotSeries6insertEi7QString5QListI8QVaria'
        'ntE',
        index, label, self._valueOf(values),
    )
    from . import DeclarativeBoxSet
    return DeclarativeBoxSet._cuteAt(address)

  @overload(DeclarativeBoxSet)
  @overload(NoneType)
  def remove(self, box: Optional[DeclarativeBoxSet]) -> bool:
    """
    Calls Qt's 'bool DeclarativeBoxPlotSeries::remove(DeclarativeBoxSet
    *box)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativeboxplotseries.html#remove

    Parameters
    ----------

    box : Optional[DeclarativeBoxSet]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool DeclarativeBoxPlotSeries::remove(DeclarativeBoxSet *box)
    return self.uglySide.call(
        'ritual_ZN24DeclarativeBoxPlotSeries6removeEP17DeclarativeBoxSet',
        self._addressOf(box),
    )

  def clear(self) -> None:
    """
    Calls Qt's 'void DeclarativeBoxPlotSeries::clear()'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativeboxplotseries.html#clear
    """
    #  void DeclarativeBoxPlotSeries::clear()
    self.uglySide.call('ritual_ZN24DeclarativeBoxPlotSeries5clearEv')

  def classBegin(self) -> None:
    """
    Calls Qt's 'void DeclarativeBoxPlotSeries::classBegin()'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativeboxplotseries.html#classBegin
    """
    #  void DeclarativeBoxPlotSeries::classBegin()
    ritual = 'ritual_ZN24DeclarativeBoxPlotSeries10classBeginEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN24DeclarativeBoxPlotSeries10classBeginEv'
    self.uglySide.call(ritual)

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void DeclarativeBoxPlotSeries::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativeboxplotseries.html#componentComplete
    """
    #  void DeclarativeBoxPlotSeries::componentComplete()
    ritual = 'ritual_ZN24DeclarativeBoxPlotSeries17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN24DeclarativeBoxPlotSeries17componentCompleteEv'
    self.uglySide.call(ritual)

  @overload(QAbstractAxis)
  @overload(NoneType)
  def axisXChanged(self, axis: Optional[QAbstractAxis]) -> None:
    """
    Calls Qt's 'void DeclarativeBoxPlotSeries::axisXChanged(QAbstractAxis
    *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativeboxplotseries.html#axisXChanged

    Parameters
    ----------

    axis : Optional[QAbstractAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DeclarativeBoxPlotSeries::axisXChanged(QAbstractAxis *axis)
    self.uglySide.call(
        'ritual_ZN24DeclarativeBoxPlotSeries12axisXChangedEP13QAbstractAxis',
        self._addressOf(axis),
    )

  @overload(QAbstractAxis)
  @overload(NoneType)
  def axisYChanged(self, axis: Optional[QAbstractAxis]) -> None:
    """
    Calls Qt's 'void DeclarativeBoxPlotSeries::axisYChanged(QAbstractAxis
    *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativeboxplotseries.html#axisYChanged

    Parameters
    ----------

    axis : Optional[QAbstractAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DeclarativeBoxPlotSeries::axisYChanged(QAbstractAxis *axis)
    self.uglySide.call(
        'ritual_ZN24DeclarativeBoxPlotSeries12axisYChangedEP13QAbstractAxis',
        self._addressOf(axis),
    )

  @overload(QAbstractAxis)
  @overload(NoneType)
  def axisXTopChanged(self, axis: Optional[QAbstractAxis]) -> None:
    """
    Calls Qt's 'void DeclarativeBoxPlotSeries::axisXTopChanged(QAbstractAxis
    *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativeboxplotseries.html#axisXTopChanged

    Parameters
    ----------

    axis : Optional[QAbstractAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DeclarativeBoxPlotSeries::axisXTopChanged(QAbstractAxis *axis)
    self.uglySide.call(
        'ritual_ZN24DeclarativeBoxPlotSeries15axisXTopChangedEP13QAbstractA'
        'xis',
        self._addressOf(axis),
    )

  @overload(QAbstractAxis)
  @overload(NoneType)
  def axisYRightChanged(self, axis: Optional[QAbstractAxis]) -> None:
    """
    Calls Qt's 'void
    DeclarativeBoxPlotSeries::axisYRightChanged(QAbstractAxis *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativeboxplotseries.html#axisYRightChanged

    Parameters
    ----------

    axis : Optional[QAbstractAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DeclarativeBoxPlotSeries::axisYRightChanged(QAbstractAxis *axis)
    self.uglySide.call(
        'ritual_ZN24DeclarativeBoxPlotSeries17axisYRightChangedEP13QAbstrac'
        'tAxis',
        self._addressOf(axis),
    )

  @overload(DeclarativeBoxSet)
  @overload(NoneType)
  def clicked(self, boxset: Optional[DeclarativeBoxSet]) -> None:
    """
    Calls Qt's 'void DeclarativeBoxPlotSeries::clicked(DeclarativeBoxSet
    *boxset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativeboxplotseries.html#clicked

    Parameters
    ----------

    boxset : Optional[DeclarativeBoxSet]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DeclarativeBoxPlotSeries::clicked(DeclarativeBoxSet *boxset)
    self.uglySide.call(
        'ritual_ZN24DeclarativeBoxPlotSeries7clickedEP17DeclarativeBoxSet',
        self._addressOf(boxset),
    )

  @overload(bool, DeclarativeBoxSet)
  @overload(bool, NoneType)
  def hovered(
      self,
      status: bool,
      boxset: Optional[DeclarativeBoxSet],
  ) -> None:
    """
    Calls Qt's 'void DeclarativeBoxPlotSeries::hovered(bool status,
    DeclarativeBoxSet *boxset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativeboxplotseries.html#hovered

    Parameters
    ----------

    status : bool
      Passed on as it is.

    boxset : Optional[DeclarativeBoxSet]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DeclarativeBoxPlotSeries::hovered(bool status, DeclarativeBoxSet
    #      *boxset)
    self.uglySide.call(
        'ritual_ZN24DeclarativeBoxPlotSeries7hoveredEbP17DeclarativeBoxSet',
        status, self._addressOf(boxset),
    )

  @overload(DeclarativeBoxSet)
  @overload(NoneType)
  def pressed(self, boxset: Optional[DeclarativeBoxSet]) -> None:
    """
    Calls Qt's 'void DeclarativeBoxPlotSeries::pressed(DeclarativeBoxSet
    *boxset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativeboxplotseries.html#pressed

    Parameters
    ----------

    boxset : Optional[DeclarativeBoxSet]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DeclarativeBoxPlotSeries::pressed(DeclarativeBoxSet *boxset)
    self.uglySide.call(
        'ritual_ZN24DeclarativeBoxPlotSeries7pressedEP17DeclarativeBoxSet',
        self._addressOf(boxset),
    )

  @overload(DeclarativeBoxSet)
  @overload(NoneType)
  def released(self, boxset: Optional[DeclarativeBoxSet]) -> None:
    """
    Calls Qt's 'void DeclarativeBoxPlotSeries::released(DeclarativeBoxSet
    *boxset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativeboxplotseries.html#released

    Parameters
    ----------

    boxset : Optional[DeclarativeBoxSet]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DeclarativeBoxPlotSeries::released(DeclarativeBoxSet *boxset)
    self.uglySide.call(
        'ritual_ZN24DeclarativeBoxPlotSeries8releasedEP17DeclarativeBoxSet',
        self._addressOf(boxset),
    )

  @overload(DeclarativeBoxSet)
  @overload(NoneType)
  def doubleClicked(self, boxset: Optional[DeclarativeBoxSet]) -> None:
    """
    Calls Qt's 'void
    DeclarativeBoxPlotSeries::doubleClicked(DeclarativeBoxSet *boxset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativeboxplotseries.html#doubleClicked

    Parameters
    ----------

    boxset : Optional[DeclarativeBoxSet]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DeclarativeBoxPlotSeries::doubleClicked(DeclarativeBoxSet
    #      *boxset)
    self.uglySide.call(
        'ritual_ZN24DeclarativeBoxPlotSeries13doubleClickedEP17DeclarativeB'
        'oxSet',
        self._addressOf(boxset),
    )

  @overload(str)
  def brushFilenameChanged(self, brushFilename: str) -> None:
    """
    Calls Qt's 'void DeclarativeBoxPlotSeries::brushFilenameChanged(const
    QString &brushFilename)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativeboxplotseries.html#brushFilenameChanged

    Parameters
    ----------

    brushFilename : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void DeclarativeBoxPlotSeries::brushFilenameChanged(const QString
    #      &brushFilename)
    self.uglySide.call(
        'ritual_ZN24DeclarativeBoxPlotSeries20brushFilenameChangedERK7QStri'
        'ng',
        brushFilename,
    )

  @overload(bool, QBoxSet)
  @overload(bool, NoneType)
  def onHovered(self, status: bool, boxset: Optional[QBoxSet]) -> None:
    """
    Calls Qt's 'void DeclarativeBoxPlotSeries::onHovered(bool status, QBoxSet
    *boxset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativeboxplotseries.html#onHovered

    Parameters
    ----------

    status : bool
      Passed on as it is.

    boxset : Optional[QBoxSet]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DeclarativeBoxPlotSeries::onHovered(bool status, QBoxSet *boxset)
    self.uglySide.call(
        'ritual_ZN24DeclarativeBoxPlotSeries9onHoveredEbP7QBoxSet',
        status, self._addressOf(boxset),
    )

  @overload(QBoxSet)
  @overload(NoneType)
  def onClicked(self, boxset: Optional[QBoxSet]) -> None:
    """
    Calls Qt's 'void DeclarativeBoxPlotSeries::onClicked(QBoxSet *boxset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativeboxplotseries.html#onClicked

    Parameters
    ----------

    boxset : Optional[QBoxSet]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DeclarativeBoxPlotSeries::onClicked(QBoxSet *boxset)
    self.uglySide.call(
        'ritual_ZN24DeclarativeBoxPlotSeries9onClickedEP7QBoxSet',
        self._addressOf(boxset),
    )

  @overload(QBoxSet)
  @overload(NoneType)
  def onPressed(self, boxset: Optional[QBoxSet]) -> None:
    """
    Calls Qt's 'void DeclarativeBoxPlotSeries::onPressed(QBoxSet *boxset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativeboxplotseries.html#onPressed

    Parameters
    ----------

    boxset : Optional[QBoxSet]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DeclarativeBoxPlotSeries::onPressed(QBoxSet *boxset)
    self.uglySide.call(
        'ritual_ZN24DeclarativeBoxPlotSeries9onPressedEP7QBoxSet',
        self._addressOf(boxset),
    )

  @overload(QBoxSet)
  @overload(NoneType)
  def onReleased(self, boxset: Optional[QBoxSet]) -> None:
    """
    Calls Qt's 'void DeclarativeBoxPlotSeries::onReleased(QBoxSet *boxset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativeboxplotseries.html#onReleased

    Parameters
    ----------

    boxset : Optional[QBoxSet]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DeclarativeBoxPlotSeries::onReleased(QBoxSet *boxset)
    self.uglySide.call(
        'ritual_ZN24DeclarativeBoxPlotSeries10onReleasedEP7QBoxSet',
        self._addressOf(boxset),
    )

  @overload(QBoxSet)
  @overload(NoneType)
  def onDoubleClicked(self, boxset: Optional[QBoxSet]) -> None:
    """
    Calls Qt's 'void DeclarativeBoxPlotSeries::onDoubleClicked(QBoxSet
    *boxset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativeboxplotseries.html#onDoubleClicked

    Parameters
    ----------

    boxset : Optional[QBoxSet]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DeclarativeBoxPlotSeries::onDoubleClicked(QBoxSet *boxset)
    self.uglySide.call(
        'ritual_ZN24DeclarativeBoxPlotSeries15onDoubleClickedEP7QBoxSet',
        self._addressOf(boxset),
    )

  def handleBrushChanged(self) -> None:
    """
    Calls Qt's 'void DeclarativeBoxPlotSeries::handleBrushChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativeboxplotseries.html#handleBrushChanged
    """
    #  void DeclarativeBoxPlotSeries::handleBrushChanged()
    self.uglySide.call(
        'ritual_ZN24DeclarativeBoxPlotSeries18handleBrushChangedEv',
    )

  @staticmethod
  def appendSeriesChildren(*__, **_) -> Never:
    """
    Qt's 'void
    DeclarativeBoxPlotSeries::appendSeriesChildren(QQmlListProperty<QObject>
    *list, QObject *element)': names 'QQmlListProperty<QObject>', which has
    no cute class yet.
    """
    raise NotImplementedError(
        "'DeclarativeBoxPlotSeries.appendSeriesChildren' has no cute "
        "function yet. Qt's 'void "
        "DeclarativeBoxPlotSeries::appendSeriesChildren(QQmlListProperty<QOb"
        "ject> *list, QObject *element)': names "
        "'QQmlListProperty<QObject>', which has no cute class yet.")

  @staticmethod
  def seriesChildren(*__, **_) -> Never:
    """
    Qt's 'QQmlListProperty<QObject>
    DeclarativeBoxPlotSeries::seriesChildren()': gives a type Python has no
    way to take yet.
    """
    raise NotImplementedError(
        "'DeclarativeBoxPlotSeries.seriesChildren' has no cute function "
        "yet. Qt's 'QQmlListProperty<QObject> "
        "DeclarativeBoxPlotSeries::seriesChildren()': gives a type Python "
        "has no way to take yet.")
