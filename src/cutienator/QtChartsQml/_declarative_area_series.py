"""
DeclarativeAreaSeries binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtChartsQml/6.12.0/QtChartsQml/private/declarativeareaseries_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means DeclarativeAreaSeries to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from ..QtCharts import QAreaSeries

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QBrush
  from ..QtCharts import QAbstractAxis
  from . import DeclarativeLineSeries
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  DeclarativeLineSeries = WAIT['DeclarativeLineSeries']
  QAbstractAxis = WAIT['QtCharts:QAbstractAxis']
  QBrush = WAIT['QBrush']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class DeclarativeAreaSeries(QAreaSeries):
  """
  The cute side of Qt's DeclarativeAreaSeries: a plain Python object standing
  in front of one C++ DeclarativeAreaSeries.

  It is built on the cute 'QAreaSeries', as Qt's DeclarativeAreaSeries is
  built on Qt's QAreaSeries, and has everything that class has.

  What exists
  -----------

  Every function of Qt's DeclarativeAreaSeries that has a ritual and that
  Python can call so far, 34 names in all: 'metaObject', 'tr',
  'setUpperSeries', 'upperSeries', 'setLowerSeries', 'lowerSeries', 'axisX',
  'setAxisX', 'axisY', 'setAxisY', 'axisXTop', 'setAxisXTop', 'axisYRight',
  'setAxisYRight', 'axisAngular', 'setAxisAngular', 'axisRadial',
  'setAxisRadial', 'borderWidth', 'setBorderWidth', 'brushFilename',
  'setBrushFilename', 'setBrush', 'brush', 'axisXChanged', 'axisYChanged',
  'borderWidthChanged', 'axisXTopChanged', 'axisYRightChanged',
  'axisAngularChanged', 'axisRadialChanged', 'brushChanged',
  'brushFilenameChanged', 'handleBrushChanged'. It can be made from Python,
  in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *DeclarativeAreaSeries::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int DeclarativeAreaSeries::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  2 of the 39 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ DeclarativeAreaSeries is created at the first use, not by
    'DeclarativeAreaSeries(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ DeclarativeAreaSeries.
  - Qt tells when it has removed the C++ DeclarativeAreaSeries. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
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
    Calls Qt's 'QString DeclarativeAreaSeries::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/declarativeareaseries.html#tr

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
    #  QString DeclarativeAreaSeries::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN21DeclarativeAreaSeries2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'DeclarativeAreaSeries'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *DeclarativeAreaSeries::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativeareaseries.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *DeclarativeAreaSeries::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK21DeclarativeAreaSeries10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def upperSeries(self) -> Optional[DeclarativeLineSeries]:
    """
    Calls Qt's 'DeclarativeLineSeries *DeclarativeAreaSeries::upperSeries()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativeareaseries.html#upperSeries

    Returns
    -------

    Optional[DeclarativeLineSeries]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DeclarativeLineSeries *DeclarativeAreaSeries::upperSeries() const
    address = self.uglySide.call(
        'ritual_ZNK21DeclarativeAreaSeries11upperSeriesEv',
    )
    from . import DeclarativeLineSeries
    return DeclarativeLineSeries._cuteAt(address)

  def lowerSeries(self) -> Optional[DeclarativeLineSeries]:
    """
    Calls Qt's 'DeclarativeLineSeries *DeclarativeAreaSeries::lowerSeries()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativeareaseries.html#lowerSeries

    Returns
    -------

    Optional[DeclarativeLineSeries]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DeclarativeLineSeries *DeclarativeAreaSeries::lowerSeries() const
    address = self.uglySide.call(
        'ritual_ZNK21DeclarativeAreaSeries11lowerSeriesEv',
    )
    from . import DeclarativeLineSeries
    return DeclarativeLineSeries._cuteAt(address)

  def borderWidth(self) -> float:
    """
    Calls Qt's 'qreal DeclarativeAreaSeries::borderWidth() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativeareaseries.html#borderWidth
    """
    #  qreal DeclarativeAreaSeries::borderWidth() const
    return self.uglySide.call(
        'ritual_ZNK21DeclarativeAreaSeries11borderWidthEv',
    )

  def brushFilename(self) -> str:
    """
    Calls Qt's 'QString DeclarativeAreaSeries::brushFilename() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativeareaseries.html#brushFilename

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString DeclarativeAreaSeries::brushFilename() const
    return self.uglySide.call(
        'ritual_ZNK21DeclarativeAreaSeries13brushFilenameEv',
    )

  def brush(self) -> QBrush:
    """
    Calls Qt's 'QBrush DeclarativeAreaSeries::brush() const'.

    Qt's own words: https://doc.qt.io/qt-6/declarativeareaseries.html#brush

    Returns
    -------

    QBrush
      A new cute QBrush around the copy Qt gave back. Python owns it.
    """
    #  QBrush DeclarativeAreaSeries::brush() const
    address = self.uglySide.call('ritual_ZNK21DeclarativeAreaSeries5brushEv')
    from ..QtGui import QBrush
    return QBrush._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(DeclarativeLineSeries)
  @overload(NoneType)
  def setUpperSeries(self, series: Optional[DeclarativeLineSeries]) -> None:
    """
    Calls Qt's 'void
    DeclarativeAreaSeries::setUpperSeries(DeclarativeLineSeries *series)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativeareaseries.html#setUpperSeries

    Parameters
    ----------

    series : Optional[DeclarativeLineSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DeclarativeAreaSeries::setUpperSeries(DeclarativeLineSeries
    #      *series)
    self.uglySide.call(
        'ritual_ZN21DeclarativeAreaSeries14setUpperSeriesEP21DeclarativeLin'
        'eSeries',
        self._addressOf(series),
    )

  @overload(DeclarativeLineSeries)
  @overload(NoneType)
  def setLowerSeries(self, series: Optional[DeclarativeLineSeries]) -> None:
    """
    Calls Qt's 'void
    DeclarativeAreaSeries::setLowerSeries(DeclarativeLineSeries *series)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativeareaseries.html#setLowerSeries

    Parameters
    ----------

    series : Optional[DeclarativeLineSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DeclarativeAreaSeries::setLowerSeries(DeclarativeLineSeries
    #      *series)
    self.uglySide.call(
        'ritual_ZN21DeclarativeAreaSeries14setLowerSeriesEP21DeclarativeLin'
        'eSeries',
        self._addressOf(series),
    )

  @overload(QAbstractAxis)
  @overload(NoneType)
  def setAxisX(self, axis: Optional[QAbstractAxis]) -> None:
    """
    Calls Qt's 'void DeclarativeAreaSeries::setAxisX(QAbstractAxis *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativeareaseries.html#setAxisX

    Parameters
    ----------

    axis : Optional[QAbstractAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DeclarativeAreaSeries::setAxisX(QAbstractAxis *axis)
    self.uglySide.call(
        'ritual_ZN21DeclarativeAreaSeries8setAxisXEP13QAbstractAxis',
        self._addressOf(axis),
    )

  @overload(QAbstractAxis)
  @overload(NoneType)
  def setAxisY(self, axis: Optional[QAbstractAxis]) -> None:
    """
    Calls Qt's 'void DeclarativeAreaSeries::setAxisY(QAbstractAxis *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativeareaseries.html#setAxisY

    Parameters
    ----------

    axis : Optional[QAbstractAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DeclarativeAreaSeries::setAxisY(QAbstractAxis *axis)
    self.uglySide.call(
        'ritual_ZN21DeclarativeAreaSeries8setAxisYEP13QAbstractAxis',
        self._addressOf(axis),
    )

  @overload(QAbstractAxis)
  @overload(NoneType)
  def setAxisXTop(self, axis: Optional[QAbstractAxis]) -> None:
    """
    Calls Qt's 'void DeclarativeAreaSeries::setAxisXTop(QAbstractAxis
    *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativeareaseries.html#setAxisXTop

    Parameters
    ----------

    axis : Optional[QAbstractAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DeclarativeAreaSeries::setAxisXTop(QAbstractAxis *axis)
    self.uglySide.call(
        'ritual_ZN21DeclarativeAreaSeries11setAxisXTopEP13QAbstractAxis',
        self._addressOf(axis),
    )

  @overload(QAbstractAxis)
  @overload(NoneType)
  def setAxisYRight(self, axis: Optional[QAbstractAxis]) -> None:
    """
    Calls Qt's 'void DeclarativeAreaSeries::setAxisYRight(QAbstractAxis
    *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativeareaseries.html#setAxisYRight

    Parameters
    ----------

    axis : Optional[QAbstractAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DeclarativeAreaSeries::setAxisYRight(QAbstractAxis *axis)
    self.uglySide.call(
        'ritual_ZN21DeclarativeAreaSeries13setAxisYRightEP13QAbstractAxis',
        self._addressOf(axis),
    )

  @overload(QAbstractAxis)
  @overload(NoneType)
  def setAxisAngular(self, axis: Optional[QAbstractAxis]) -> None:
    """
    Calls Qt's 'void DeclarativeAreaSeries::setAxisAngular(QAbstractAxis
    *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativeareaseries.html#setAxisAngular

    Parameters
    ----------

    axis : Optional[QAbstractAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DeclarativeAreaSeries::setAxisAngular(QAbstractAxis *axis)
    self.uglySide.call(
        'ritual_ZN21DeclarativeAreaSeries14setAxisAngularEP13QAbstractAxis',
        self._addressOf(axis),
    )

  @overload(QAbstractAxis)
  @overload(NoneType)
  def setAxisRadial(self, axis: Optional[QAbstractAxis]) -> None:
    """
    Calls Qt's 'void DeclarativeAreaSeries::setAxisRadial(QAbstractAxis
    *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativeareaseries.html#setAxisRadial

    Parameters
    ----------

    axis : Optional[QAbstractAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DeclarativeAreaSeries::setAxisRadial(QAbstractAxis *axis)
    self.uglySide.call(
        'ritual_ZN21DeclarativeAreaSeries13setAxisRadialEP13QAbstractAxis',
        self._addressOf(axis),
    )

  @overload(float)
  def setBorderWidth(self, borderWidth: float) -> None:
    """
    Calls Qt's 'void DeclarativeAreaSeries::setBorderWidth(qreal
    borderWidth)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativeareaseries.html#setBorderWidth

    Parameters
    ----------

    borderWidth : float
      Passed on as it is.
    """
    #  void DeclarativeAreaSeries::setBorderWidth(qreal borderWidth)
    self.uglySide.call(
        'ritual_ZN21DeclarativeAreaSeries14setBorderWidthEd', borderWidth,
    )

  @overload(str)
  def setBrushFilename(self, brushFilename: str) -> None:
    """
    Calls Qt's 'void DeclarativeAreaSeries::setBrushFilename(const QString
    &brushFilename)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativeareaseries.html#setBrushFilename

    Parameters
    ----------

    brushFilename : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void DeclarativeAreaSeries::setBrushFilename(const QString
    #      &brushFilename)
    self.uglySide.call(
        'ritual_ZN21DeclarativeAreaSeries16setBrushFilenameERK7QString',
        brushFilename,
    )

  @overload(QBrush)
  def setBrush(self, brush: QBrush) -> None:
    """
    Calls Qt's 'void DeclarativeAreaSeries::setBrush(const QBrush &brush)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativeareaseries.html#setBrush

    Parameters
    ----------

    brush : QBrush
      Passed on as a value: Qt reads the C++ QBrush, which stays Python's
      own.
    """
    #  void DeclarativeAreaSeries::setBrush(const QBrush &brush)
    self.uglySide.call(
        'ritual_ZN21DeclarativeAreaSeries8setBrushERK6QBrush',
        self._valueOf(brush),
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
    'DeclarativeAreaSeries::DeclarativeAreaSeries(QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativeareaseries.html#DeclarativeAreaSeries

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  DeclarativeAreaSeries::DeclarativeAreaSeries(QObject *parent)
    self._noteCreation(DeclarativeAreaSeries, lambda: Rituals.call(
        'ritual_ZN21DeclarativeAreaSeriesC1EP7QObject',
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

  def axisX(self) -> Optional[QAbstractAxis]:
    """
    Calls Qt's 'QAbstractAxis *DeclarativeAreaSeries::axisX()'.

    Qt's own words: https://doc.qt.io/qt-6/declarativeareaseries.html#axisX

    Returns
    -------

    Optional[QAbstractAxis]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractAxis *DeclarativeAreaSeries::axisX()
    address = self.uglySide.call('ritual_ZN21DeclarativeAreaSeries5axisXEv')
    from ..QtCharts import QAbstractAxis
    return QAbstractAxis._cuteAt(address)

  def axisY(self) -> Optional[QAbstractAxis]:
    """
    Calls Qt's 'QAbstractAxis *DeclarativeAreaSeries::axisY()'.

    Qt's own words: https://doc.qt.io/qt-6/declarativeareaseries.html#axisY

    Returns
    -------

    Optional[QAbstractAxis]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractAxis *DeclarativeAreaSeries::axisY()
    address = self.uglySide.call('ritual_ZN21DeclarativeAreaSeries5axisYEv')
    from ..QtCharts import QAbstractAxis
    return QAbstractAxis._cuteAt(address)

  def axisXTop(self) -> Optional[QAbstractAxis]:
    """
    Calls Qt's 'QAbstractAxis *DeclarativeAreaSeries::axisXTop()'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativeareaseries.html#axisXTop

    Returns
    -------

    Optional[QAbstractAxis]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractAxis *DeclarativeAreaSeries::axisXTop()
    address = self.uglySide.call(
        'ritual_ZN21DeclarativeAreaSeries8axisXTopEv',
    )
    from ..QtCharts import QAbstractAxis
    return QAbstractAxis._cuteAt(address)

  def axisYRight(self) -> Optional[QAbstractAxis]:
    """
    Calls Qt's 'QAbstractAxis *DeclarativeAreaSeries::axisYRight()'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativeareaseries.html#axisYRight

    Returns
    -------

    Optional[QAbstractAxis]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractAxis *DeclarativeAreaSeries::axisYRight()
    address = self.uglySide.call(
        'ritual_ZN21DeclarativeAreaSeries10axisYRightEv',
    )
    from ..QtCharts import QAbstractAxis
    return QAbstractAxis._cuteAt(address)

  def axisAngular(self) -> Optional[QAbstractAxis]:
    """
    Calls Qt's 'QAbstractAxis *DeclarativeAreaSeries::axisAngular()'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativeareaseries.html#axisAngular

    Returns
    -------

    Optional[QAbstractAxis]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractAxis *DeclarativeAreaSeries::axisAngular()
    address = self.uglySide.call(
        'ritual_ZN21DeclarativeAreaSeries11axisAngularEv',
    )
    from ..QtCharts import QAbstractAxis
    return QAbstractAxis._cuteAt(address)

  def axisRadial(self) -> Optional[QAbstractAxis]:
    """
    Calls Qt's 'QAbstractAxis *DeclarativeAreaSeries::axisRadial()'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativeareaseries.html#axisRadial

    Returns
    -------

    Optional[QAbstractAxis]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractAxis *DeclarativeAreaSeries::axisRadial()
    address = self.uglySide.call(
        'ritual_ZN21DeclarativeAreaSeries10axisRadialEv',
    )
    from ..QtCharts import QAbstractAxis
    return QAbstractAxis._cuteAt(address)

  @overload(QAbstractAxis)
  @overload(NoneType)
  def axisXChanged(self, axis: Optional[QAbstractAxis]) -> None:
    """
    Calls Qt's 'void DeclarativeAreaSeries::axisXChanged(QAbstractAxis
    *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativeareaseries.html#axisXChanged

    Parameters
    ----------

    axis : Optional[QAbstractAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DeclarativeAreaSeries::axisXChanged(QAbstractAxis *axis)
    self.uglySide.call(
        'ritual_ZN21DeclarativeAreaSeries12axisXChangedEP13QAbstractAxis',
        self._addressOf(axis),
    )

  @overload(QAbstractAxis)
  @overload(NoneType)
  def axisYChanged(self, axis: Optional[QAbstractAxis]) -> None:
    """
    Calls Qt's 'void DeclarativeAreaSeries::axisYChanged(QAbstractAxis
    *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativeareaseries.html#axisYChanged

    Parameters
    ----------

    axis : Optional[QAbstractAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DeclarativeAreaSeries::axisYChanged(QAbstractAxis *axis)
    self.uglySide.call(
        'ritual_ZN21DeclarativeAreaSeries12axisYChangedEP13QAbstractAxis',
        self._addressOf(axis),
    )

  @overload(float)
  def borderWidthChanged(self, width: float) -> None:
    """
    Calls Qt's 'void DeclarativeAreaSeries::borderWidthChanged(qreal width)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativeareaseries.html#borderWidthChanged

    Parameters
    ----------

    width : float
      Passed on as it is.
    """
    #  void DeclarativeAreaSeries::borderWidthChanged(qreal width)
    self.uglySide.call(
        'ritual_ZN21DeclarativeAreaSeries18borderWidthChangedEd', width,
    )

  @overload(QAbstractAxis)
  @overload(NoneType)
  def axisXTopChanged(self, axis: Optional[QAbstractAxis]) -> None:
    """
    Calls Qt's 'void DeclarativeAreaSeries::axisXTopChanged(QAbstractAxis
    *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativeareaseries.html#axisXTopChanged

    Parameters
    ----------

    axis : Optional[QAbstractAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DeclarativeAreaSeries::axisXTopChanged(QAbstractAxis *axis)
    self.uglySide.call(
        'ritual_ZN21DeclarativeAreaSeries15axisXTopChangedEP13QAbstractAxis',
        self._addressOf(axis),
    )

  @overload(QAbstractAxis)
  @overload(NoneType)
  def axisYRightChanged(self, axis: Optional[QAbstractAxis]) -> None:
    """
    Calls Qt's 'void DeclarativeAreaSeries::axisYRightChanged(QAbstractAxis
    *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativeareaseries.html#axisYRightChanged

    Parameters
    ----------

    axis : Optional[QAbstractAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DeclarativeAreaSeries::axisYRightChanged(QAbstractAxis *axis)
    self.uglySide.call(
        'ritual_ZN21DeclarativeAreaSeries17axisYRightChangedEP13QAbstractAx'
        'is',
        self._addressOf(axis),
    )

  @overload(QAbstractAxis)
  @overload(NoneType)
  def axisAngularChanged(self, axis: Optional[QAbstractAxis]) -> None:
    """
    Calls Qt's 'void DeclarativeAreaSeries::axisAngularChanged(QAbstractAxis
    *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativeareaseries.html#axisAngularChanged

    Parameters
    ----------

    axis : Optional[QAbstractAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DeclarativeAreaSeries::axisAngularChanged(QAbstractAxis *axis)
    self.uglySide.call(
        'ritual_ZN21DeclarativeAreaSeries18axisAngularChangedEP13QAbstractA'
        'xis',
        self._addressOf(axis),
    )

  @overload(QAbstractAxis)
  @overload(NoneType)
  def axisRadialChanged(self, axis: Optional[QAbstractAxis]) -> None:
    """
    Calls Qt's 'void DeclarativeAreaSeries::axisRadialChanged(QAbstractAxis
    *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativeareaseries.html#axisRadialChanged

    Parameters
    ----------

    axis : Optional[QAbstractAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DeclarativeAreaSeries::axisRadialChanged(QAbstractAxis *axis)
    self.uglySide.call(
        'ritual_ZN21DeclarativeAreaSeries17axisRadialChangedEP13QAbstractAx'
        'is',
        self._addressOf(axis),
    )

  def brushChanged(self) -> None:
    """
    Calls Qt's 'void DeclarativeAreaSeries::brushChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativeareaseries.html#brushChanged
    """
    #  void DeclarativeAreaSeries::brushChanged()
    self.uglySide.call('ritual_ZN21DeclarativeAreaSeries12brushChangedEv')

  @overload(str)
  def brushFilenameChanged(self, brushFilename: str) -> None:
    """
    Calls Qt's 'void DeclarativeAreaSeries::brushFilenameChanged(const
    QString &brushFilename)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativeareaseries.html#brushFilenameChanged

    Parameters
    ----------

    brushFilename : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void DeclarativeAreaSeries::brushFilenameChanged(const QString
    #      &brushFilename)
    self.uglySide.call(
        'ritual_ZN21DeclarativeAreaSeries20brushFilenameChangedERK7QString',
        brushFilename,
    )

  def handleBrushChanged(self) -> None:
    """
    Calls Qt's 'void DeclarativeAreaSeries::handleBrushChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativeareaseries.html#handleBrushChanged
    """
    #  void DeclarativeAreaSeries::handleBrushChanged()
    self.uglySide.call(
        'ritual_ZN21DeclarativeAreaSeries18handleBrushChangedEv',
    )
