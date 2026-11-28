"""
QBarLegendMarker binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCharts/qbarlegendmarker.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QLegendMarker

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from . import QAbstractBarSeries, QBarLegendMarkerPrivate, QBarSet, QLegend
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAbstractBarSeries = WAIT['QAbstractBarSeries']
  QBarSet = WAIT['QtCharts:QBarSet']
  QLegend = WAIT['QLegend']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QBarLegendMarker(QLegendMarker):
  """
  The cute side of Qt's QBarLegendMarker: a plain Python object standing in
  front of one C++ QBarLegendMarker.

  It is built on the cute 'QLegendMarker', as Qt's QBarLegendMarker is built
  on Qt's QLegendMarker, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QBarLegendMarker that has a ritual and that Python
  can call so far, 6 names in all: 'metaObject', 'tr', 'type', 'series',
  'barset', 'd_func'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QBarLegendMarker::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QBarLegendMarker::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QBarLegendMarker::~QBarLegendMarker()': the destructor: Python
    never removes a C++ QBarLegendMarker.
  - Qt's 'QBarLegendMarker::QBarLegendMarker(QBarLegendMarkerPrivate &d,
    QObject *parent)': takes a type Python has no way to hand over yet.
  - Qt's 'const QBarLegendMarkerPrivate *QBarLegendMarker::d_func() const':
    takes in Python what 'QBarLegendMarkerPrivate
    *QBarLegendMarker::d_func()' takes.

  What has no ritual
  ------------------

  4 of the 16 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QBarLegendMarker is created at the first use, not by
    'QBarLegendMarker(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QBarLegendMarker.
  - Qt tells when it has removed the C++ QBarLegendMarker. Every call on the
    cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QBarLegendMarker::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qbarlegendmarker.html#tr

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
    #  QString QBarLegendMarker::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN16QBarLegendMarker2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QBarLegendMarker'

  #  A C++ QBarLegendMarker Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QBarLegendMarker'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QBarLegendMarker::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbarlegendmarker.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QBarLegendMarker::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK16QBarLegendMarker10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QAbstractBarSeries, QBarSet, QLegend)
  @overload(QAbstractBarSeries, QBarSet, NoneType)
  @overload(QAbstractBarSeries, NoneType, QLegend)
  @overload(QAbstractBarSeries, NoneType, NoneType)
  @overload(NoneType, QBarSet, QLegend)
  @overload(NoneType, QBarSet, NoneType)
  @overload(NoneType, NoneType, QLegend)
  @overload(NoneType, NoneType, NoneType)
  @overload(QAbstractBarSeries, QBarSet, QLegend, QObject)
  @overload(QAbstractBarSeries, QBarSet, QLegend, NoneType)
  @overload(QAbstractBarSeries, QBarSet, NoneType, QObject)
  @overload(QAbstractBarSeries, QBarSet, NoneType, NoneType)
  @overload(QAbstractBarSeries, NoneType, QLegend, QObject)
  @overload(QAbstractBarSeries, NoneType, QLegend, NoneType)
  @overload(QAbstractBarSeries, NoneType, NoneType, QObject)
  @overload(QAbstractBarSeries, NoneType, NoneType, NoneType)
  @overload(NoneType, QBarSet, QLegend, QObject)
  @overload(NoneType, QBarSet, QLegend, NoneType)
  @overload(NoneType, QBarSet, NoneType, QObject)
  @overload(NoneType, QBarSet, NoneType, NoneType)
  @overload(NoneType, NoneType, QLegend, QObject)
  @overload(NoneType, NoneType, QLegend, NoneType)
  @overload(NoneType, NoneType, NoneType, QObject)
  @overload(NoneType, NoneType, NoneType, NoneType)
  def __init__(
      self,
      series: Optional[QAbstractBarSeries],
      barset: Optional[QBarSet],
      legend: Optional[QLegend],
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QBarLegendMarker::QBarLegendMarker(QAbstractBarSeries *series, QBarSet
    *barset, QLegend *legend, QObject *parent)', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qbarlegendmarker.html#QBarLegendMarker

    Parameters
    ----------

    series : Optional[QAbstractBarSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    barset : Optional[QBarSet]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    legend : Optional[QLegend]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QBarLegendMarker::QBarLegendMarker(QAbstractBarSeries *series, QBarSet
    #      *barset, QLegend *legend, QObject *parent)
    self._noteCreation(QBarLegendMarker, lambda: Rituals.call(
        'ritual_ZN16QBarLegendMarkerC1EP18QAbstractBarSeriesP7QBarSetP7QLeg'
        'endP7QObject',
        self._addressOf(series), self._addressOf(barset),
        self._addressOf(legend), self._addressOf(parent, 'QObject'),
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

  def type(self) -> QLegendMarker.LegendMarkerType:
    """
    Calls Qt's 'LegendMarkerType QBarLegendMarker::type()'.

    Qt's own words: https://doc.qt.io/qt-6/qbarlegendmarker.html#type

    Returns
    -------

    QLegendMarker.LegendMarkerType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QLegendMarker.LegendMarkerType(number)' gives.
    """
    #  LegendMarkerType QBarLegendMarker::type()
    ritual = 'ritual_ZN16QBarLegendMarker4typeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QBarLegendMarker4typeEv'
    return QLegendMarker.LegendMarkerType(self.uglySide.call(ritual))

  def series(self) -> Optional[QAbstractBarSeries]:
    """
    Calls Qt's 'QAbstractBarSeries *QBarLegendMarker::series()'.

    Qt's own words: https://doc.qt.io/qt-6/qbarlegendmarker.html#series

    Returns
    -------

    Optional[QAbstractBarSeries]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractBarSeries *QBarLegendMarker::series()
    ritual = 'ritual_ZN16QBarLegendMarker6seriesEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QBarLegendMarker6seriesEv'
    address = self.uglySide.call(ritual)
    from . import QAbstractBarSeries
    return QAbstractBarSeries._cuteAt(address)

  def barset(self) -> Optional[QBarSet]:
    """
    Calls Qt's 'QBarSet *QBarLegendMarker::barset()'.

    Qt's own words: https://doc.qt.io/qt-6/qbarlegendmarker.html#barset

    Returns
    -------

    Optional[QBarSet]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QBarSet *QBarLegendMarker::barset()
    address = self.uglySide.call('ritual_ZN16QBarLegendMarker6barsetEv')
    from . import QBarSet
    return QBarSet._cuteAt(address)

  def d_func(self) -> Optional[QBarLegendMarkerPrivate]:
    """
    Calls Qt's 'QBarLegendMarkerPrivate *QBarLegendMarker::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qbarlegendmarker.html#d_func

    Returns
    -------

    Optional[QBarLegendMarkerPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QBarLegendMarkerPrivate *QBarLegendMarker::d_func()
    address = self.uglySide.call('ritual_ZN16QBarLegendMarker6d_funcEv')
    from . import QBarLegendMarkerPrivate
    return QBarLegendMarkerPrivate._cuteAt(address)
