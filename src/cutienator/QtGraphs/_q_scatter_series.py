"""
QScatterSeries binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGraphs/qscatterseries.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtCore import QObject
from . import QAbstractSeries, QXYSeries

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtCharts import QScatterSeriesPrivate

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QScatterSeries(QXYSeries):
  """
  The cute side of Qt's QScatterSeries: a plain Python object standing in
  front of one C++ QScatterSeries.

  It is built on the cute 'QXYSeries', as Qt's QScatterSeries is built on
  Qt's QXYSeries, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QScatterSeries that has a ritual and that Python can
  call so far, 5 names in all: 'metaObject', 'tr', 'type',
  'componentComplete', 'd_func'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QScatterSeries::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QScatterSeries::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QScatterSeries::~QScatterSeries()': the destructor: Python never
    removes a C++ QScatterSeries.
  - Qt's 'QScatterSeries::QScatterSeries(QScatterSeriesPrivate &dd, QObject
    *parent)': takes a type Python has no way to hand over yet.
  - Qt's 'const QScatterSeriesPrivate *QScatterSeries::d_func() const': takes
    in Python what 'QScatterSeriesPrivate *QScatterSeries::d_func()' takes.

  What has no ritual
  ------------------

  4 of the 15 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QScatterSeries is created at the first use, not by
    'QScatterSeries(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QScatterSeries.
  - Qt tells when it has removed the C++ QScatterSeries. Every call on the
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
    Calls Qt's 'QString QScatterSeries::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qscatterseries.html#tr

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
    #  QString QScatterSeries::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN14QScatterSeries2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QScatterSeries'
  #  The part of Qt it is of, as another part has a class of its name too.
  __qt_part__ = 'QtGraphs'

  #  A C++ QScatterSeries Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QScatterSeries'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QScatterSeries::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qscatterseries.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QScatterSeries::metaObject() const
    address = self.uglySide.call('ritual_ZNK14QScatterSeries10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def type(self) -> QAbstractSeries.SeriesType:
    """
    Calls Qt's 'QAbstractSeries::SeriesType QScatterSeries::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qscatterseries.html#type

    Returns
    -------

    QAbstractSeries.SeriesType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QAbstractSeries.SeriesType(number)' gives.
    """
    #  QAbstractSeries::SeriesType QScatterSeries::type() const
    ritual = 'ritual_ZNK14QScatterSeries4typeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14QScatterSeries4typeEv'
    return QAbstractSeries.SeriesType(self.uglySide.call(ritual))

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

  @overload()
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's 'QScatterSeries::QScatterSeries(QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qscatterseries.html#QScatterSeries

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QScatterSeries::QScatterSeries(QObject *parent)
    self._noteCreation(QScatterSeries, lambda: Rituals.call(
        'ritual_ZN14QScatterSeriesC1EP7QObject',
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

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QScatterSeries::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscatterseries.html#componentComplete
    """
    #  void QScatterSeries::componentComplete()
    ritual = 'ritual_ZN14QScatterSeries17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QScatterSeries17componentCompleteEv'
    self.uglySide.call(ritual)

  def d_func(self) -> Optional[QScatterSeriesPrivate]:
    """
    Calls Qt's 'QScatterSeriesPrivate *QScatterSeries::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qscatterseries.html#d_func

    Returns
    -------

    Optional[QScatterSeriesPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QScatterSeriesPrivate *QScatterSeries::d_func()
    address = self.uglySide.call('ritual_ZN14QScatterSeries6d_funcEv')
    from ..QtCharts import QScatterSeriesPrivate
    return QScatterSeriesPrivate._cuteAt(address)
