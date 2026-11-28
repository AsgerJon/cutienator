"""
QBoxPlotLegendMarker binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCharts/qboxplotlegendmarker.h, Qt 6.12.0. Changes made here are lost.
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
  from . import QBoxPlotLegendMarkerPrivate, QBoxPlotSeries, QLegend
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QBoxPlotSeries = WAIT['QBoxPlotSeries']
  QLegend = WAIT['QLegend']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QBoxPlotLegendMarker(QLegendMarker):
  """
  The cute side of Qt's QBoxPlotLegendMarker: a plain Python object standing
  in front of one C++ QBoxPlotLegendMarker.

  It is built on the cute 'QLegendMarker', as Qt's QBoxPlotLegendMarker is
  built on Qt's QLegendMarker, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QBoxPlotLegendMarker that has a ritual and that
  Python can call so far, 5 names in all: 'metaObject', 'tr', 'type',
  'series', 'd_func'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QBoxPlotLegendMarker::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QBoxPlotLegendMarker::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QBoxPlotLegendMarker::~QBoxPlotLegendMarker()': the destructor:
    Python never removes a C++ QBoxPlotLegendMarker.
  - Qt's
    'QBoxPlotLegendMarker::QBoxPlotLegendMarker(QBoxPlotLegendMarkerPrivate
    &d, QObject *parent)': takes a type Python has no way to hand over yet.
  - Qt's 'const QBoxPlotLegendMarkerPrivate *QBoxPlotLegendMarker::d_func()
    const': takes in Python what 'QBoxPlotLegendMarkerPrivate
    *QBoxPlotLegendMarker::d_func()' takes.

  What has no ritual
  ------------------

  4 of the 15 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QBoxPlotLegendMarker is created at the first use, not by
    'QBoxPlotLegendMarker(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QBoxPlotLegendMarker.
  - Qt tells when it has removed the C++ QBoxPlotLegendMarker. Every call on
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
    Calls Qt's 'QString QBoxPlotLegendMarker::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qboxplotlegendmarker.html#tr

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
    #  QString QBoxPlotLegendMarker::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN20QBoxPlotLegendMarker2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QBoxPlotLegendMarker'

  #  A C++ QBoxPlotLegendMarker Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QBoxPlotLegendMarker'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QBoxPlotLegendMarker::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qboxplotlegendmarker.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QBoxPlotLegendMarker::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK20QBoxPlotLegendMarker10metaObjectEv',
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

  @overload(QBoxPlotSeries, QLegend)
  @overload(QBoxPlotSeries, NoneType)
  @overload(NoneType, QLegend)
  @overload(NoneType, NoneType)
  @overload(QBoxPlotSeries, QLegend, QObject)
  @overload(QBoxPlotSeries, QLegend, NoneType)
  @overload(QBoxPlotSeries, NoneType, QObject)
  @overload(QBoxPlotSeries, NoneType, NoneType)
  @overload(NoneType, QLegend, QObject)
  @overload(NoneType, QLegend, NoneType)
  @overload(NoneType, NoneType, QObject)
  @overload(NoneType, NoneType, NoneType)
  def __init__(
      self,
      series: Optional[QBoxPlotSeries],
      legend: Optional[QLegend],
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QBoxPlotLegendMarker::QBoxPlotLegendMarker(QBoxPlotSeries *series,
    QLegend *legend, QObject *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qboxplotlegendmarker.html#QBoxPlotLegendMarker

    Parameters
    ----------

    series : Optional[QBoxPlotSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    legend : Optional[QLegend]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QBoxPlotLegendMarker::QBoxPlotLegendMarker(QBoxPlotSeries *series,
    #      QLegend *legend, QObject *parent)
    self._noteCreation(QBoxPlotLegendMarker, lambda: Rituals.call(
        'ritual_ZN20QBoxPlotLegendMarkerC1EP14QBoxPlotSeriesP7QLegendP7QObj'
        'ect',
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
    Calls Qt's 'LegendMarkerType QBoxPlotLegendMarker::type()'.

    Qt's own words: https://doc.qt.io/qt-6/qboxplotlegendmarker.html#type

    Returns
    -------

    QLegendMarker.LegendMarkerType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QLegendMarker.LegendMarkerType(number)' gives.
    """
    #  LegendMarkerType QBoxPlotLegendMarker::type()
    ritual = 'ritual_ZN20QBoxPlotLegendMarker4typeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QBoxPlotLegendMarker4typeEv'
    return QLegendMarker.LegendMarkerType(self.uglySide.call(ritual))

  def series(self) -> Optional[QBoxPlotSeries]:
    """
    Calls Qt's 'QBoxPlotSeries *QBoxPlotLegendMarker::series()'.

    Qt's own words: https://doc.qt.io/qt-6/qboxplotlegendmarker.html#series

    Returns
    -------

    Optional[QBoxPlotSeries]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QBoxPlotSeries *QBoxPlotLegendMarker::series()
    ritual = 'ritual_ZN20QBoxPlotLegendMarker6seriesEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QBoxPlotLegendMarker6seriesEv'
    address = self.uglySide.call(ritual)
    from . import QBoxPlotSeries
    return QBoxPlotSeries._cuteAt(address)

  def d_func(self) -> Optional[QBoxPlotLegendMarkerPrivate]:
    """
    Calls Qt's 'QBoxPlotLegendMarkerPrivate *QBoxPlotLegendMarker::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qboxplotlegendmarker.html#d_func

    Returns
    -------

    Optional[QBoxPlotLegendMarkerPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QBoxPlotLegendMarkerPrivate *QBoxPlotLegendMarker::d_func()
    address = self.uglySide.call('ritual_ZN20QBoxPlotLegendMarker6d_funcEv')
    from . import QBoxPlotLegendMarkerPrivate
    return QBoxPlotLegendMarkerPrivate._cuteAt(address)
