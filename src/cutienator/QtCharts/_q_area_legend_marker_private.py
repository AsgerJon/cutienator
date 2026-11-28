"""
QAreaLegendMarkerPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCharts/6.12.0/QtCharts/private/qarealegendmarker_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QAreaLegendMarkerPrivate to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
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
  from . import QAreaLegendMarker, QAreaSeries, QLegend
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAreaLegendMarker = WAIT['QAreaLegendMarker']
  QAreaSeries = WAIT['QtCharts:QAreaSeries']
  QLegend = WAIT['QLegend']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAreaLegendMarkerPrivate(QLegendMarkerPrivate):
  """
  The cute side of Qt's QAreaLegendMarkerPrivate: a plain Python object
  standing in front of one C++ QAreaLegendMarkerPrivate.

  It is built on the cute 'QLegendMarkerPrivate', as Qt's
  QAreaLegendMarkerPrivate is built on Qt's QLegendMarkerPrivate, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QAreaLegendMarkerPrivate that has a ritual and that
  Python can call so far, 6 names in all: 'metaObject', 'tr', 'series',
  'relatedObject', 'updated', 'q_func'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QAreaLegendMarkerPrivate::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QAreaLegendMarkerPrivate::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QAreaLegendMarkerPrivate::~QAreaLegendMarkerPrivate()': the
    destructor: Python never removes a C++ QAreaLegendMarkerPrivate.
  - Qt's 'const QAreaLegendMarker *QAreaLegendMarkerPrivate::q_func() const':
    takes in Python what 'QAreaLegendMarker
    *QAreaLegendMarkerPrivate::q_func()' takes.

  What has no ritual
  ------------------

  2 of the 13 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QAreaLegendMarkerPrivate is created at the first use, not by
    'QAreaLegendMarkerPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAreaLegendMarkerPrivate.
  - Qt tells when it has removed the C++ QAreaLegendMarkerPrivate. Every call
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
    Calls Qt's 'QString QAreaLegendMarkerPrivate::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qarealegendmarkerprivate.html#tr

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
    #  QString QAreaLegendMarkerPrivate::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN24QAreaLegendMarkerPrivate2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAreaLegendMarkerPrivate'

  #  A C++ QAreaLegendMarkerPrivate Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QAreaLegendMarkerPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QAreaLegendMarkerPrivate::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qarealegendmarkerprivate.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QAreaLegendMarkerPrivate::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK24QAreaLegendMarkerPrivate10metaObjectEv',
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

  @overload(QAreaLegendMarker, QAreaSeries, QLegend)
  @overload(QAreaLegendMarker, QAreaSeries, NoneType)
  @overload(QAreaLegendMarker, NoneType, QLegend)
  @overload(QAreaLegendMarker, NoneType, NoneType)
  @overload(NoneType, QAreaSeries, QLegend)
  @overload(NoneType, QAreaSeries, NoneType)
  @overload(NoneType, NoneType, QLegend)
  @overload(NoneType, NoneType, NoneType)
  def __init__(
      self,
      q: Optional[QAreaLegendMarker],
      series: Optional[QAreaSeries],
      legend: Optional[QLegend],
  ) -> None:
    """
    Notes what was given, for Qt's
    'QAreaLegendMarkerPrivate::QAreaLegendMarkerPrivate(QAreaLegendMarker *q,
    QAreaSeries *series, QLegend *legend)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qarealegendmarkerprivate.html

    Parameters
    ----------

    q : Optional[QAreaLegendMarker]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    series : Optional[QAreaSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    legend : Optional[QLegend]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QAreaLegendMarkerPrivate::QAreaLegendMarkerPrivate(QAreaLegendMarker
    #      *q, QAreaSeries *series, QLegend *legend)
    self._noteCreation(QAreaLegendMarkerPrivate, lambda: Rituals.call(
        'ritual_ZN24QAreaLegendMarkerPrivateC1EP17QAreaLegendMarkerP11QArea'
        'SeriesP7QLegend',
        self._addressOf(q), self._addressOf(series), self._addressOf(legend),
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

  def series(self) -> Optional[QAreaSeries]:
    """
    Calls Qt's 'QAreaSeries *QAreaLegendMarkerPrivate::series()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qarealegendmarkerprivate.html#series

    Returns
    -------

    Optional[QAreaSeries]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAreaSeries *QAreaLegendMarkerPrivate::series()
    ritual = 'ritual_ZN24QAreaLegendMarkerPrivate6seriesEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN24QAreaLegendMarkerPrivate6seriesEv'
    address = self.uglySide.call(ritual)
    from . import QAreaSeries
    return QAreaSeries._cuteAt(address)

  def relatedObject(self) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QAreaLegendMarkerPrivate::relatedObject()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qarealegendmarkerprivate.html#relatedObject

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QAreaLegendMarkerPrivate::relatedObject()
    ritual = 'ritual_ZN24QAreaLegendMarkerPrivate13relatedObjectEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN24QAreaLegendMarkerPrivate13relatedObjectEv'
    address = self.uglySide.call(ritual)
    return QObject._cuteAt(address)

  def updated(self) -> None:
    """
    Calls Qt's 'void QAreaLegendMarkerPrivate::updated()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qarealegendmarkerprivate.html#updated
    """
    #  void QAreaLegendMarkerPrivate::updated()
    ritual = 'ritual_ZN24QAreaLegendMarkerPrivate7updatedEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN24QAreaLegendMarkerPrivate7updatedEv'
    self.uglySide.call(ritual)

  def q_func(self) -> Optional[QAreaLegendMarker]:
    """
    Calls Qt's 'QAreaLegendMarker *QAreaLegendMarkerPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qarealegendmarkerprivate.html#q_func

    Returns
    -------

    Optional[QAreaLegendMarker]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAreaLegendMarker *QAreaLegendMarkerPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN24QAreaLegendMarkerPrivate6q_funcEv',
    )
    from . import QAreaLegendMarker
    return QAreaLegendMarker._cuteAt(address)
