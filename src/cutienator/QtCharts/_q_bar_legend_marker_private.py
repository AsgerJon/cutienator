"""
QBarLegendMarkerPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCharts/6.12.0/QtCharts/private/qbarlegendmarker_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QBarLegendMarkerPrivate to be private: it declares the class in a
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
  from . import QAbstractBarSeries, QBarLegendMarker, QBarSet, QLegend
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAbstractBarSeries = WAIT['QAbstractBarSeries']
  QBarLegendMarker = WAIT['QBarLegendMarker']
  QBarSet = WAIT['QtCharts:QBarSet']
  QLegend = WAIT['QLegend']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QBarLegendMarkerPrivate(QLegendMarkerPrivate):
  """
  The cute side of Qt's QBarLegendMarkerPrivate: a plain Python object
  standing in front of one C++ QBarLegendMarkerPrivate.

  It is built on the cute 'QLegendMarkerPrivate', as Qt's
  QBarLegendMarkerPrivate is built on Qt's QLegendMarkerPrivate, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QBarLegendMarkerPrivate that has a ritual and that
  Python can call so far, 6 names in all: 'metaObject', 'tr', 'series',
  'relatedObject', 'updated', 'q_func'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QBarLegendMarkerPrivate::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QBarLegendMarkerPrivate::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QBarLegendMarkerPrivate::~QBarLegendMarkerPrivate()': the
    destructor: Python never removes a C++ QBarLegendMarkerPrivate.
  - Qt's 'const QBarLegendMarker *QBarLegendMarkerPrivate::q_func() const':
    takes in Python what 'QBarLegendMarker
    *QBarLegendMarkerPrivate::q_func()' takes.

  What has no ritual
  ------------------

  2 of the 13 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QBarLegendMarkerPrivate is created at the first use, not by
    'QBarLegendMarkerPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QBarLegendMarkerPrivate.
  - Qt tells when it has removed the C++ QBarLegendMarkerPrivate. Every call
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
    Calls Qt's 'QString QBarLegendMarkerPrivate::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qbarlegendmarkerprivate.html#tr

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
    #  QString QBarLegendMarkerPrivate::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN23QBarLegendMarkerPrivate2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QBarLegendMarkerPrivate'

  #  A C++ QBarLegendMarkerPrivate Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QBarLegendMarkerPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QBarLegendMarkerPrivate::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbarlegendmarkerprivate.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QBarLegendMarkerPrivate::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK23QBarLegendMarkerPrivate10metaObjectEv',
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

  @overload(QBarLegendMarker, QAbstractBarSeries, QBarSet, QLegend)
  @overload(QBarLegendMarker, QAbstractBarSeries, QBarSet, NoneType)
  @overload(QBarLegendMarker, QAbstractBarSeries, NoneType, QLegend)
  @overload(QBarLegendMarker, QAbstractBarSeries, NoneType, NoneType)
  @overload(QBarLegendMarker, NoneType, QBarSet, QLegend)
  @overload(QBarLegendMarker, NoneType, QBarSet, NoneType)
  @overload(QBarLegendMarker, NoneType, NoneType, QLegend)
  @overload(QBarLegendMarker, NoneType, NoneType, NoneType)
  @overload(NoneType, QAbstractBarSeries, QBarSet, QLegend)
  @overload(NoneType, QAbstractBarSeries, QBarSet, NoneType)
  @overload(NoneType, QAbstractBarSeries, NoneType, QLegend)
  @overload(NoneType, QAbstractBarSeries, NoneType, NoneType)
  @overload(NoneType, NoneType, QBarSet, QLegend)
  @overload(NoneType, NoneType, QBarSet, NoneType)
  @overload(NoneType, NoneType, NoneType, QLegend)
  @overload(NoneType, NoneType, NoneType, NoneType)
  def __init__(
      self,
      q: Optional[QBarLegendMarker],
      series: Optional[QAbstractBarSeries],
      barset: Optional[QBarSet],
      legend: Optional[QLegend],
  ) -> None:
    """
    Notes what was given, for Qt's
    'QBarLegendMarkerPrivate::QBarLegendMarkerPrivate(QBarLegendMarker *q,
    QAbstractBarSeries *series, QBarSet *barset, QLegend *legend)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qbarlegendmarkerprivate.html

    Parameters
    ----------

    q : Optional[QBarLegendMarker]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    series : Optional[QAbstractBarSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    barset : Optional[QBarSet]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    legend : Optional[QLegend]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QBarLegendMarkerPrivate::QBarLegendMarkerPrivate(QBarLegendMarker *q,
    #      QAbstractBarSeries *series, QBarSet *barset, QLegend *legend)
    self._noteCreation(QBarLegendMarkerPrivate, lambda: Rituals.call(
        'ritual_ZN23QBarLegendMarkerPrivateC1EP16QBarLegendMarkerP18QAbstra'
        'ctBarSeriesP7QBarSetP7QLegend',
        self._addressOf(q), self._addressOf(series), self._addressOf(barset),
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

  def series(self) -> Optional[QAbstractBarSeries]:
    """
    Calls Qt's 'QAbstractBarSeries *QBarLegendMarkerPrivate::series()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbarlegendmarkerprivate.html#series

    Returns
    -------

    Optional[QAbstractBarSeries]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractBarSeries *QBarLegendMarkerPrivate::series()
    ritual = 'ritual_ZN23QBarLegendMarkerPrivate6seriesEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN23QBarLegendMarkerPrivate6seriesEv'
    address = self.uglySide.call(ritual)
    from . import QAbstractBarSeries
    return QAbstractBarSeries._cuteAt(address)

  def relatedObject(self) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QBarLegendMarkerPrivate::relatedObject()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbarlegendmarkerprivate.html#relatedObject

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QBarLegendMarkerPrivate::relatedObject()
    ritual = 'ritual_ZN23QBarLegendMarkerPrivate13relatedObjectEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN23QBarLegendMarkerPrivate13relatedObjectEv'
    address = self.uglySide.call(ritual)
    return QObject._cuteAt(address)

  def updated(self) -> None:
    """
    Calls Qt's 'void QBarLegendMarkerPrivate::updated()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbarlegendmarkerprivate.html#updated
    """
    #  void QBarLegendMarkerPrivate::updated()
    ritual = 'ritual_ZN23QBarLegendMarkerPrivate7updatedEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN23QBarLegendMarkerPrivate7updatedEv'
    self.uglySide.call(ritual)

  def q_func(self) -> Optional[QBarLegendMarker]:
    """
    Calls Qt's 'QBarLegendMarker *QBarLegendMarkerPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbarlegendmarkerprivate.html#q_func

    Returns
    -------

    Optional[QBarLegendMarker]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QBarLegendMarker *QBarLegendMarkerPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN23QBarLegendMarkerPrivate6q_funcEv',
    )
    from . import QBarLegendMarker
    return QBarLegendMarker._cuteAt(address)
