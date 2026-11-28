"""
QPieLegendMarker binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCharts/qpielegendmarker.h, Qt 6.12.0. Changes made here are lost.
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
  from . import QLegend, QPieLegendMarkerPrivate, QPieSeries, QPieSlice
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QLegend = WAIT['QLegend']
  QPieSeries = WAIT['QtCharts:QPieSeries']
  QPieSlice = WAIT['QtCharts:QPieSlice']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPieLegendMarker(QLegendMarker):
  """
  The cute side of Qt's QPieLegendMarker: a plain Python object standing in
  front of one C++ QPieLegendMarker.

  It is built on the cute 'QLegendMarker', as Qt's QPieLegendMarker is built
  on Qt's QLegendMarker, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QPieLegendMarker that has a ritual and that Python
  can call so far, 6 names in all: 'metaObject', 'tr', 'type', 'series',
  'slice', 'd_func'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QPieLegendMarker::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QPieLegendMarker::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QPieLegendMarker::~QPieLegendMarker()': the destructor: Python
    never removes a C++ QPieLegendMarker.
  - Qt's 'QPieLegendMarker::QPieLegendMarker(QPieLegendMarkerPrivate &d,
    QObject *parent)': takes a type Python has no way to hand over yet.
  - Qt's 'const QPieLegendMarkerPrivate *QPieLegendMarker::d_func() const':
    takes in Python what 'QPieLegendMarkerPrivate
    *QPieLegendMarker::d_func()' takes.

  What has no ritual
  ------------------

  4 of the 16 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QPieLegendMarker is created at the first use, not by
    'QPieLegendMarker(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QPieLegendMarker.
  - Qt tells when it has removed the C++ QPieLegendMarker. Every call on the
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
    Calls Qt's 'QString QPieLegendMarker::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qpielegendmarker.html#tr

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
    #  QString QPieLegendMarker::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN16QPieLegendMarker2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPieLegendMarker'

  #  A C++ QPieLegendMarker Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QPieLegendMarker'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QPieLegendMarker::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpielegendmarker.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QPieLegendMarker::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK16QPieLegendMarker10metaObjectEv',
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

  @overload(QPieSeries, QPieSlice, QLegend)
  @overload(QPieSeries, QPieSlice, NoneType)
  @overload(QPieSeries, NoneType, QLegend)
  @overload(QPieSeries, NoneType, NoneType)
  @overload(NoneType, QPieSlice, QLegend)
  @overload(NoneType, QPieSlice, NoneType)
  @overload(NoneType, NoneType, QLegend)
  @overload(NoneType, NoneType, NoneType)
  @overload(QPieSeries, QPieSlice, QLegend, QObject)
  @overload(QPieSeries, QPieSlice, QLegend, NoneType)
  @overload(QPieSeries, QPieSlice, NoneType, QObject)
  @overload(QPieSeries, QPieSlice, NoneType, NoneType)
  @overload(QPieSeries, NoneType, QLegend, QObject)
  @overload(QPieSeries, NoneType, QLegend, NoneType)
  @overload(QPieSeries, NoneType, NoneType, QObject)
  @overload(QPieSeries, NoneType, NoneType, NoneType)
  @overload(NoneType, QPieSlice, QLegend, QObject)
  @overload(NoneType, QPieSlice, QLegend, NoneType)
  @overload(NoneType, QPieSlice, NoneType, QObject)
  @overload(NoneType, QPieSlice, NoneType, NoneType)
  @overload(NoneType, NoneType, QLegend, QObject)
  @overload(NoneType, NoneType, QLegend, NoneType)
  @overload(NoneType, NoneType, NoneType, QObject)
  @overload(NoneType, NoneType, NoneType, NoneType)
  def __init__(
      self,
      series: Optional[QPieSeries],
      slice: Optional[QPieSlice],
      legend: Optional[QLegend],
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QPieLegendMarker::QPieLegendMarker(QPieSeries *series, QPieSlice *slice,
    QLegend *legend, QObject *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qpielegendmarker.html#QPieLegendMarker

    Parameters
    ----------

    series : Optional[QPieSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    slice : Optional[QPieSlice]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    legend : Optional[QLegend]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QPieLegendMarker::QPieLegendMarker(QPieSeries *series, QPieSlice
    #      *slice, QLegend *legend, QObject *parent)
    self._noteCreation(QPieLegendMarker, lambda: Rituals.call(
        'ritual_ZN16QPieLegendMarkerC1EP10QPieSeriesP9QPieSliceP7QLegendP7Q'
        'Object',
        self._addressOf(series), self._addressOf(slice),
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
    Calls Qt's 'LegendMarkerType QPieLegendMarker::type()'.

    Qt's own words: https://doc.qt.io/qt-6/qpielegendmarker.html#type

    Returns
    -------

    QLegendMarker.LegendMarkerType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QLegendMarker.LegendMarkerType(number)' gives.
    """
    #  LegendMarkerType QPieLegendMarker::type()
    ritual = 'ritual_ZN16QPieLegendMarker4typeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QPieLegendMarker4typeEv'
    return QLegendMarker.LegendMarkerType(self.uglySide.call(ritual))

  def series(self) -> Optional[QPieSeries]:
    """
    Calls Qt's 'QPieSeries *QPieLegendMarker::series()'.

    Qt's own words: https://doc.qt.io/qt-6/qpielegendmarker.html#series

    Returns
    -------

    Optional[QPieSeries]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPieSeries *QPieLegendMarker::series()
    ritual = 'ritual_ZN16QPieLegendMarker6seriesEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QPieLegendMarker6seriesEv'
    address = self.uglySide.call(ritual)
    from . import QPieSeries
    return QPieSeries._cuteAt(address)

  def slice(self) -> Optional[QPieSlice]:
    """
    Calls Qt's 'QPieSlice *QPieLegendMarker::slice()'.

    Qt's own words: https://doc.qt.io/qt-6/qpielegendmarker.html#slice

    Returns
    -------

    Optional[QPieSlice]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPieSlice *QPieLegendMarker::slice()
    address = self.uglySide.call('ritual_ZN16QPieLegendMarker5sliceEv')
    from . import QPieSlice
    return QPieSlice._cuteAt(address)

  def d_func(self) -> Optional[QPieLegendMarkerPrivate]:
    """
    Calls Qt's 'QPieLegendMarkerPrivate *QPieLegendMarker::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qpielegendmarker.html#d_func

    Returns
    -------

    Optional[QPieLegendMarkerPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPieLegendMarkerPrivate *QPieLegendMarker::d_func()
    address = self.uglySide.call('ritual_ZN16QPieLegendMarker6d_funcEv')
    from . import QPieLegendMarkerPrivate
    return QPieLegendMarkerPrivate._cuteAt(address)
