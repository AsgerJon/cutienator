"""
QSplineSeries binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGraphs/qsplineseries.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtCore import Qt, QObject
from . import QAbstractSeries, QXYSeries

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from ..QtCharts import QSplineSeriesPrivate

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSplineSeries(QXYSeries):
  """
  The cute side of Qt's QSplineSeries: a plain Python object standing in
  front of one C++ QSplineSeries.

  It is built on the cute 'QXYSeries', as Qt's QSplineSeries is built on Qt's
  QXYSeries, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSplineSeries that has a ritual and that Python can
  call so far, 14 names in all: 'metaObject', 'tr', 'type', 'width',
  'setWidth', 'capStyle', 'setCapStyle', 'isOptimized', 'setOptimized',
  'widthChanged', 'capStyleChanged', 'optimizedChanged', 'componentComplete',
  'd_func'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QSplineSeries::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QSplineSeries::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QSplineSeries::~QSplineSeries()': the destructor: Python never
    removes a C++ QSplineSeries.
  - Qt's 'QList<QPointF> &QSplineSeries::getControlPoints()': gives a type
    Python has no way to take yet.
  - Qt's 'QSplineSeries::QSplineSeries(QSplineSeriesPrivate &dd, QObject
    *parent)': takes a type Python has no way to hand over yet.
  - Qt's 'const QSplineSeriesPrivate *QSplineSeries::d_func() const': takes
    in Python what 'QSplineSeriesPrivate *QSplineSeries::d_func()' takes.

  What has no ritual
  ------------------

  4 of the 25 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QSplineSeries is created at the first use, not by
    'QSplineSeries(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSplineSeries.
  - Qt tells when it has removed the C++ QSplineSeries. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QSplineSeries that has no cute function yet,
    'getControlPoints', holds a function that raises 'NotImplementedError',
    and its docstring says why.
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
    Calls Qt's 'QString QSplineSeries::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qsplineseries.html#tr

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
    #  QString QSplineSeries::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN13QSplineSeries2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSplineSeries'
  #  The part of Qt it is of, as another part has a class of its name too.
  __qt_part__ = 'QtGraphs'

  #  A C++ QSplineSeries Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSplineSeries'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QSplineSeries::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsplineseries.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QSplineSeries::metaObject() const
    address = self.uglySide.call('ritual_ZNK13QSplineSeries10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def type(self) -> QAbstractSeries.SeriesType:
    """
    Calls Qt's 'QAbstractSeries::SeriesType QSplineSeries::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsplineseries.html#type

    Returns
    -------

    QAbstractSeries.SeriesType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QAbstractSeries.SeriesType(number)' gives.
    """
    #  QAbstractSeries::SeriesType QSplineSeries::type() const
    ritual = 'ritual_ZNK13QSplineSeries4typeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK13QSplineSeries4typeEv'
    return QAbstractSeries.SeriesType(self.uglySide.call(ritual))

  def width(self) -> float:
    """
    Calls Qt's 'qreal QSplineSeries::width() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsplineseries.html#width
    """
    #  qreal QSplineSeries::width() const
    return self.uglySide.call('ritual_ZNK13QSplineSeries5widthEv')

  def capStyle(self) -> Qt.PenCapStyle:
    """
    Calls Qt's 'Qt::PenCapStyle QSplineSeries::capStyle() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsplineseries.html#capStyle

    Returns
    -------

    Qt.PenCapStyle
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.PenCapStyle(number)'
      gives.
    """
    #  Qt::PenCapStyle QSplineSeries::capStyle() const
    return Qt.PenCapStyle(self.uglySide.call(
        'ritual_ZNK13QSplineSeries8capStyleEv',
    ))

  def isOptimized(self) -> bool:
    """
    Calls Qt's 'bool QSplineSeries::isOptimized() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsplineseries.html#isOptimized
    """
    #  bool QSplineSeries::isOptimized() const
    return self.uglySide.call('ritual_ZNK13QSplineSeries11isOptimizedEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setWidth(self, newWidth: float) -> None:
    """
    Calls Qt's 'void QSplineSeries::setWidth(qreal newWidth)'.

    Qt's own words: https://doc.qt.io/qt-6/qsplineseries.html#setWidth

    Parameters
    ----------

    newWidth : float
      Passed on as it is.
    """
    #  void QSplineSeries::setWidth(qreal newWidth)
    self.uglySide.call('ritual_ZN13QSplineSeries8setWidthEd', newWidth)

  @overload(Qt.PenCapStyle)
  def setCapStyle(self, newCapStyle: Qt.PenCapStyle) -> None:
    """
    Calls Qt's 'void QSplineSeries::setCapStyle(Qt::PenCapStyle
    newCapStyle)'.

    Qt's own words: https://doc.qt.io/qt-6/qsplineseries.html#setCapStyle

    Parameters
    ----------

    newCapStyle : Qt.PenCapStyle
      Passed on as its number.
    """
    #  void QSplineSeries::setCapStyle(Qt::PenCapStyle newCapStyle)
    self.uglySide.call(
        'ritual_ZN13QSplineSeries11setCapStyleEN2Qt11PenCapStyleE',
        newCapStyle.value,
    )

  @overload(bool)
  def setOptimized(self, optimized: bool) -> None:
    """
    Calls Qt's 'void QSplineSeries::setOptimized(bool optimized)'.

    Qt's own words: https://doc.qt.io/qt-6/qsplineseries.html#setOptimized

    Parameters
    ----------

    optimized : bool
      Passed on as it is.
    """
    #  void QSplineSeries::setOptimized(bool optimized)
    self.uglySide.call('ritual_ZN13QSplineSeries12setOptimizedEb', optimized)

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
    Notes what was given, for Qt's 'QSplineSeries::QSplineSeries(QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qsplineseries.html#QSplineSeries

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QSplineSeries::QSplineSeries(QObject *parent)
    self._noteCreation(QSplineSeries, lambda: Rituals.call(
        'ritual_ZN13QSplineSeriesC1EP7QObject',
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

  def widthChanged(self) -> None:
    """
    Calls Qt's 'void QSplineSeries::widthChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qsplineseries.html#widthChanged
    """
    #  void QSplineSeries::widthChanged()
    self.uglySide.call('ritual_ZN13QSplineSeries12widthChangedEv')

  def capStyleChanged(self) -> None:
    """
    Calls Qt's 'void QSplineSeries::capStyleChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qsplineseries.html#capStyleChanged
    """
    #  void QSplineSeries::capStyleChanged()
    self.uglySide.call('ritual_ZN13QSplineSeries15capStyleChangedEv')

  @overload(bool)
  def optimizedChanged(self, newOptimized: bool) -> None:
    """
    Calls Qt's 'void QSplineSeries::optimizedChanged(bool newOptimized)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsplineseries.html#optimizedChanged

    Parameters
    ----------

    newOptimized : bool
      Passed on as it is.
    """
    #  void QSplineSeries::optimizedChanged(bool newOptimized)
    self.uglySide.call(
        'ritual_ZN13QSplineSeries16optimizedChangedEb', newOptimized,
    )

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QSplineSeries::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsplineseries.html#componentComplete
    """
    #  void QSplineSeries::componentComplete()
    ritual = 'ritual_ZN13QSplineSeries17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QSplineSeries17componentCompleteEv'
    self.uglySide.call(ritual)

  def d_func(self) -> Optional[QSplineSeriesPrivate]:
    """
    Calls Qt's 'QSplineSeriesPrivate *QSplineSeries::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qsplineseries.html#d_func

    Returns
    -------

    Optional[QSplineSeriesPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSplineSeriesPrivate *QSplineSeries::d_func()
    address = self.uglySide.call('ritual_ZN13QSplineSeries6d_funcEv')
    from ..QtCharts import QSplineSeriesPrivate
    return QSplineSeriesPrivate._cuteAt(address)

  @staticmethod
  def getControlPoints(*__, **_) -> Never:
    """
    Qt's 'QList<QPointF> &QSplineSeries::getControlPoints()': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QSplineSeries.getControlPoints' has no cute function yet. Qt's "
        "'QList<QPointF> &QSplineSeries::getControlPoints()': gives a type "
        "Python has no way to take yet.")
