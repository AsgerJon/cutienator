"""
QCandlestickLegendMarker binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCharts/qcandlesticklegendmarker.h, Qt 6.12.0. Changes made here are
#  lost.
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
  from . import QCandlestickLegendMarkerPrivate, QCandlestickSeries, QLegend
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QCandlestickSeries = WAIT['QCandlestickSeries']
  QLegend = WAIT['QLegend']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QCandlestickLegendMarker(QLegendMarker):
  """
  The cute side of Qt's QCandlestickLegendMarker: a plain Python object
  standing in front of one C++ QCandlestickLegendMarker.

  It is built on the cute 'QLegendMarker', as Qt's QCandlestickLegendMarker
  is built on Qt's QLegendMarker, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QCandlestickLegendMarker that has a ritual and that
  Python can call so far, 5 names in all: 'metaObject', 'tr', 'type',
  'series', 'd_func'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QCandlestickLegendMarker::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QCandlestickLegendMarker::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QCandlestickLegendMarker::~QCandlestickLegendMarker()': the
    destructor: Python never removes a C++ QCandlestickLegendMarker.
  - Qt's 'const QCandlestickLegendMarkerPrivate
    *QCandlestickLegendMarker::d_func() const': takes in Python what
    'QCandlestickLegendMarkerPrivate *QCandlestickLegendMarker::d_func()'
    takes.

  What has no ritual
  ------------------

  4 of the 14 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QCandlestickLegendMarker is created at the first use, not by
    'QCandlestickLegendMarker(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QCandlestickLegendMarker.
  - Qt tells when it has removed the C++ QCandlestickLegendMarker. Every call
    on the cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QCandlestickLegendMarker::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qcandlesticklegendmarker.html#tr

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
    #  QString QCandlestickLegendMarker::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN24QCandlestickLegendMarker2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCandlestickLegendMarker'

  #  A C++ QCandlestickLegendMarker Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QCandlestickLegendMarker'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QCandlestickLegendMarker::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcandlesticklegendmarker.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QCandlestickLegendMarker::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK24QCandlestickLegendMarker10metaObjectEv',
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

  @overload(QCandlestickSeries, QLegend)
  @overload(QCandlestickSeries, NoneType)
  @overload(NoneType, QLegend)
  @overload(NoneType, NoneType)
  @overload(QCandlestickSeries, QLegend, QObject)
  @overload(QCandlestickSeries, QLegend, NoneType)
  @overload(QCandlestickSeries, NoneType, QObject)
  @overload(QCandlestickSeries, NoneType, NoneType)
  @overload(NoneType, QLegend, QObject)
  @overload(NoneType, QLegend, NoneType)
  @overload(NoneType, NoneType, QObject)
  @overload(NoneType, NoneType, NoneType)
  def __init__(
      self,
      series: Optional[QCandlestickSeries],
      legend: Optional[QLegend],
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QCandlestickLegendMarker::QCandlestickLegendMarker(QCandlestickSeries
    *series, QLegend *legend, QObject *parent)', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcandlesticklegendmarker.html

    Parameters
    ----------

    series : Optional[QCandlestickSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    legend : Optional[QLegend]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QCandlestickLegendMarker::QCandlestickLegendMarker(QCandlestickSeries
    #      *series, QLegend *legend, QObject *parent)
    self._noteCreation(QCandlestickLegendMarker, lambda: Rituals.call(
        'ritual_ZN24QCandlestickLegendMarkerC1EP18QCandlestickSeriesP7QLege'
        'ndP7QObject',
        self._addressOf(series), self._addressOf(legend),
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

  def type(self) -> QLegendMarker.LegendMarkerType:
    """
    Calls Qt's 'LegendMarkerType QCandlestickLegendMarker::type()'.

    Qt's own words: https://doc.qt.io/qt-6/qcandlesticklegendmarker.html#type

    Returns
    -------

    QLegendMarker.LegendMarkerType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QLegendMarker.LegendMarkerType(number)' gives.
    """
    #  LegendMarkerType QCandlestickLegendMarker::type()
    ritual = 'ritual_ZN24QCandlestickLegendMarker4typeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN24QCandlestickLegendMarker4typeEv'
    return QLegendMarker.LegendMarkerType(self.uglySide.call(ritual))

  def series(self) -> Optional[QCandlestickSeries]:
    """
    Calls Qt's 'QCandlestickSeries *QCandlestickLegendMarker::series()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcandlesticklegendmarker.html#series

    Returns
    -------

    Optional[QCandlestickSeries]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCandlestickSeries *QCandlestickLegendMarker::series()
    ritual = 'ritual_ZN24QCandlestickLegendMarker6seriesEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN24QCandlestickLegendMarker6seriesEv'
    address = self.uglySide.call(ritual)
    from . import QCandlestickSeries
    return QCandlestickSeries._cuteAt(address)

  def d_func(self) -> Optional[QCandlestickLegendMarkerPrivate]:
    """
    Calls Qt's 'QCandlestickLegendMarkerPrivate
    *QCandlestickLegendMarker::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcandlesticklegendmarker.html#d_func

    Returns
    -------

    Optional[QCandlestickLegendMarkerPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCandlestickLegendMarkerPrivate *QCandlestickLegendMarker::d_func()
    address = self.uglySide.call(
        'ritual_ZN24QCandlestickLegendMarker6d_funcEv',
    )
    from . import QCandlestickLegendMarkerPrivate
    return QCandlestickLegendMarkerPrivate._cuteAt(address)
