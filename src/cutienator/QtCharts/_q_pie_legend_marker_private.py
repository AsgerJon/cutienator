"""
QPieLegendMarkerPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCharts/6.12.0/QtCharts/private/qpielegendmarker_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QPieLegendMarkerPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QLegendMarkerPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from . import QLegend, QPieLegendMarker, QPieSeries, QPieSlice
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QLegend = WAIT['QLegend']
  QPieLegendMarker = WAIT['QPieLegendMarker']
  QPieSeries = WAIT['QtCharts:QPieSeries']
  QPieSlice = WAIT['QtCharts:QPieSlice']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPieLegendMarkerPrivate(QLegendMarkerPrivate):
  """
  The cute side of Qt's QPieLegendMarkerPrivate: a plain Python object
  standing in front of one C++ QPieLegendMarkerPrivate.

  It is built on the cute 'QLegendMarkerPrivate', as Qt's
  QPieLegendMarkerPrivate is built on Qt's QLegendMarkerPrivate, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QPieLegendMarkerPrivate that has a ritual and that
  Python can call so far, 6 names in all: 'metaObject', 'tr', 'series',
  'relatedObject', 'updated', 'q_func'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QPieLegendMarkerPrivate::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QPieLegendMarkerPrivate::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QPieLegendMarkerPrivate::~QPieLegendMarkerPrivate()': the
    destructor: Python never removes a C++ QPieLegendMarkerPrivate.
  - Qt's 'const QPieLegendMarker *QPieLegendMarkerPrivate::q_func() const':
    takes in Python what 'QPieLegendMarker
    *QPieLegendMarkerPrivate::q_func()' takes.

  What has no ritual
  ------------------

  2 of the 13 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QPieLegendMarkerPrivate is created at the first use, not by
    'QPieLegendMarkerPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QPieLegendMarkerPrivate.
  - Qt tells when it has removed the C++ QPieLegendMarkerPrivate. Every call
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
    Calls Qt's 'QString QPieLegendMarkerPrivate::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qpielegendmarkerprivate.html#tr

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
    #  QString QPieLegendMarkerPrivate::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN23QPieLegendMarkerPrivate2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPieLegendMarkerPrivate'

  #  A C++ QPieLegendMarkerPrivate Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QPieLegendMarkerPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QPieLegendMarkerPrivate::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpielegendmarkerprivate.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QPieLegendMarkerPrivate::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK23QPieLegendMarkerPrivate10metaObjectEv',
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

  @overload(QPieLegendMarker, QPieSeries, QPieSlice, QLegend)
  @overload(QPieLegendMarker, QPieSeries, QPieSlice, NoneType)
  @overload(QPieLegendMarker, QPieSeries, NoneType, QLegend)
  @overload(QPieLegendMarker, QPieSeries, NoneType, NoneType)
  @overload(QPieLegendMarker, NoneType, QPieSlice, QLegend)
  @overload(QPieLegendMarker, NoneType, QPieSlice, NoneType)
  @overload(QPieLegendMarker, NoneType, NoneType, QLegend)
  @overload(QPieLegendMarker, NoneType, NoneType, NoneType)
  @overload(NoneType, QPieSeries, QPieSlice, QLegend)
  @overload(NoneType, QPieSeries, QPieSlice, NoneType)
  @overload(NoneType, QPieSeries, NoneType, QLegend)
  @overload(NoneType, QPieSeries, NoneType, NoneType)
  @overload(NoneType, NoneType, QPieSlice, QLegend)
  @overload(NoneType, NoneType, QPieSlice, NoneType)
  @overload(NoneType, NoneType, NoneType, QLegend)
  @overload(NoneType, NoneType, NoneType, NoneType)
  def __init__(
      self,
      q: Optional[QPieLegendMarker],
      series: Optional[QPieSeries],
      slice: Optional[QPieSlice],
      legend: Optional[QLegend],
  ) -> None:
    """
    Notes what was given, for Qt's
    'QPieLegendMarkerPrivate::QPieLegendMarkerPrivate(QPieLegendMarker *q,
    QPieSeries *series, QPieSlice *slice, QLegend *legend)', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qpielegendmarkerprivate.html

    Parameters
    ----------

    q : Optional[QPieLegendMarker]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    series : Optional[QPieSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    slice : Optional[QPieSlice]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    legend : Optional[QLegend]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QPieLegendMarkerPrivate::QPieLegendMarkerPrivate(QPieLegendMarker *q,
    #      QPieSeries *series, QPieSlice *slice, QLegend *legend)
    self._noteCreation(QPieLegendMarkerPrivate, lambda: Rituals.call(
        'ritual_ZN23QPieLegendMarkerPrivateC1EP16QPieLegendMarkerP10QPieSer'
        'iesP9QPieSliceP7QLegend',
        self._addressOf(q), self._addressOf(series), self._addressOf(slice),
        self._addressOf(legend),
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

  def series(self) -> Optional[QPieSeries]:
    """
    Calls Qt's 'QPieSeries *QPieLegendMarkerPrivate::series()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpielegendmarkerprivate.html#series

    Returns
    -------

    Optional[QPieSeries]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPieSeries *QPieLegendMarkerPrivate::series()
    ritual = 'ritual_ZN23QPieLegendMarkerPrivate6seriesEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN23QPieLegendMarkerPrivate6seriesEv'
    address = self.uglySide.call(ritual)
    from . import QPieSeries
    return QPieSeries._cuteAt(address)

  def relatedObject(self) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QPieLegendMarkerPrivate::relatedObject()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpielegendmarkerprivate.html#relatedObject

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QPieLegendMarkerPrivate::relatedObject()
    ritual = 'ritual_ZN23QPieLegendMarkerPrivate13relatedObjectEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN23QPieLegendMarkerPrivate13relatedObjectEv'
    address = self.uglySide.call(ritual)
    return QObject._cuteAt(address)

  def updated(self) -> None:
    """
    Calls Qt's 'void QPieLegendMarkerPrivate::updated()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpielegendmarkerprivate.html#updated
    """
    #  void QPieLegendMarkerPrivate::updated()
    ritual = 'ritual_ZN23QPieLegendMarkerPrivate7updatedEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN23QPieLegendMarkerPrivate7updatedEv'
    self.uglySide.call(ritual)

  def q_func(self) -> Optional[QPieLegendMarker]:
    """
    Calls Qt's 'QPieLegendMarker *QPieLegendMarkerPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpielegendmarkerprivate.html#q_func

    Returns
    -------

    Optional[QPieLegendMarker]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPieLegendMarker *QPieLegendMarkerPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN23QPieLegendMarkerPrivate6q_funcEv',
    )
    from . import QPieLegendMarker
    return QPieLegendMarker._cuteAt(address)
