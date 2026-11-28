"""
QBoxPlotLegendMarkerPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCharts/6.12.0/QtCharts/private/qboxplotlegendmarker_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QBoxPlotLegendMarkerPrivate to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
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
  from . import QAbstractSeries, QBoxPlotLegendMarker, QBoxPlotSeries
  from . import QLegend
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QBoxPlotLegendMarker = WAIT['QBoxPlotLegendMarker']
  QBoxPlotSeries = WAIT['QBoxPlotSeries']
  QLegend = WAIT['QLegend']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QBoxPlotLegendMarkerPrivate(QLegendMarkerPrivate):
  """
  The cute side of Qt's QBoxPlotLegendMarkerPrivate: a plain Python object
  standing in front of one C++ QBoxPlotLegendMarkerPrivate.

  It is built on the cute 'QLegendMarkerPrivate', as Qt's
  QBoxPlotLegendMarkerPrivate is built on Qt's QLegendMarkerPrivate, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QBoxPlotLegendMarkerPrivate that has a ritual and
  that Python can call so far, 6 names in all: 'metaObject', 'tr', 'series',
  'relatedObject', 'updated', 'q_func'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QBoxPlotLegendMarkerPrivate::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int QBoxPlotLegendMarkerPrivate::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QBoxPlotLegendMarkerPrivate::~QBoxPlotLegendMarkerPrivate()': the
    destructor: Python never removes a C++ QBoxPlotLegendMarkerPrivate.
  - Qt's 'const QBoxPlotLegendMarker *QBoxPlotLegendMarkerPrivate::q_func()
    const': takes in Python what 'QBoxPlotLegendMarker
    *QBoxPlotLegendMarkerPrivate::q_func()' takes.

  What has no ritual
  ------------------

  2 of the 13 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QBoxPlotLegendMarkerPrivate is created at the first use, not by
    'QBoxPlotLegendMarkerPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QBoxPlotLegendMarkerPrivate.
  - Qt tells when it has removed the C++ QBoxPlotLegendMarkerPrivate. Every
    call on the cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QBoxPlotLegendMarkerPrivate::tr(const char *s, const
    char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qboxplotlegendmarkerprivate.html#tr

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
    #  QString QBoxPlotLegendMarkerPrivate::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN27QBoxPlotLegendMarkerPrivate2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QBoxPlotLegendMarkerPrivate'

  #  A C++ QBoxPlotLegendMarkerPrivate Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QBoxPlotLegendMarkerPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QBoxPlotLegendMarkerPrivate::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qboxplotlegendmarkerprivate.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QBoxPlotLegendMarkerPrivate::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK27QBoxPlotLegendMarkerPrivate10metaObjectEv',
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

  @overload(QBoxPlotLegendMarker, QBoxPlotSeries, QLegend)
  @overload(QBoxPlotLegendMarker, QBoxPlotSeries, NoneType)
  @overload(QBoxPlotLegendMarker, NoneType, QLegend)
  @overload(QBoxPlotLegendMarker, NoneType, NoneType)
  @overload(NoneType, QBoxPlotSeries, QLegend)
  @overload(NoneType, QBoxPlotSeries, NoneType)
  @overload(NoneType, NoneType, QLegend)
  @overload(NoneType, NoneType, NoneType)
  def __init__(
      self,
      q: Optional[QBoxPlotLegendMarker],
      series: Optional[QBoxPlotSeries],
      legend: Optional[QLegend],
  ) -> None:
    """
    Notes what was given, for Qt's
    'QBoxPlotLegendMarkerPrivate::QBoxPlotLegendMarkerPrivate(
    QBoxPlotLegendMarker *q, QBoxPlotSeries *series, QLegend *legend)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qboxplotlegendmarkerprivate.html

    Parameters
    ----------

    q : Optional[QBoxPlotLegendMarker]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    series : Optional[QBoxPlotSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    legend : Optional[QLegend]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QBoxPlotLegendMarkerPrivate::QBoxPlotLegendMarkerPrivate(
    #      QBoxPlotLegendMarker *q, QBoxPlotSeries *series, QLegend *legend)
    self._noteCreation(QBoxPlotLegendMarkerPrivate, lambda: Rituals.call(
        'ritual_ZN27QBoxPlotLegendMarkerPrivateC1EP20QBoxPlotLegendMarkerP1'
        '4QBoxPlotSeriesP7QLegend',
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

  def series(self) -> Optional[QAbstractSeries]:
    """
    Calls Qt's 'QAbstractSeries *QBoxPlotLegendMarkerPrivate::series()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qboxplotlegendmarkerprivate.html#series

    Returns
    -------

    Optional[QAbstractSeries]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractSeries *QBoxPlotLegendMarkerPrivate::series()
    ritual = 'ritual_ZN27QBoxPlotLegendMarkerPrivate6seriesEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN27QBoxPlotLegendMarkerPrivate6seriesEv'
    address = self.uglySide.call(ritual)
    from . import QAbstractSeries
    return QAbstractSeries._cuteAt(address)

  def relatedObject(self) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QBoxPlotLegendMarkerPrivate::relatedObject()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qboxplotlegendmarkerprivate.html#relatedObject

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QBoxPlotLegendMarkerPrivate::relatedObject()
    ritual = 'ritual_ZN27QBoxPlotLegendMarkerPrivate13relatedObjectEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN27QBoxPlotLegendMarkerPrivate13relatedObjectEv'
    address = self.uglySide.call(ritual)
    return QObject._cuteAt(address)

  def updated(self) -> None:
    """
    Calls Qt's 'void QBoxPlotLegendMarkerPrivate::updated()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qboxplotlegendmarkerprivate.html#updated
    """
    #  void QBoxPlotLegendMarkerPrivate::updated()
    ritual = 'ritual_ZN27QBoxPlotLegendMarkerPrivate7updatedEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN27QBoxPlotLegendMarkerPrivate7updatedEv'
    self.uglySide.call(ritual)

  def q_func(self) -> Optional[QBoxPlotLegendMarker]:
    """
    Calls Qt's 'QBoxPlotLegendMarker *QBoxPlotLegendMarkerPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qboxplotlegendmarkerprivate.html#q_func

    Returns
    -------

    Optional[QBoxPlotLegendMarker]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QBoxPlotLegendMarker *QBoxPlotLegendMarkerPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN27QBoxPlotLegendMarkerPrivate6q_funcEv',
    )
    from . import QBoxPlotLegendMarker
    return QBoxPlotLegendMarker._cuteAt(address)
