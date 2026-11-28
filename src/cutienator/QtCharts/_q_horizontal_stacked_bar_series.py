"""
QHorizontalStackedBarSeries binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCharts/qhorizontalstackedbarseries.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtCore import QObject
from . import QAbstractBarSeries, QAbstractSeries

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from . import QHorizontalStackedBarSeriesPrivate

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QHorizontalStackedBarSeries(QAbstractBarSeries):
  """
  The cute side of Qt's QHorizontalStackedBarSeries: a plain Python object
  standing in front of one C++ QHorizontalStackedBarSeries.

  It is built on the cute 'QAbstractBarSeries', as Qt's
  QHorizontalStackedBarSeries is built on Qt's QAbstractBarSeries, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QHorizontalStackedBarSeries that has a ritual and
  that Python can call so far, 4 names in all: 'metaObject', 'tr', 'type',
  'd_func'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QHorizontalStackedBarSeries::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int QHorizontalStackedBarSeries::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QHorizontalStackedBarSeries::~QHorizontalStackedBarSeries()': the
    destructor: Python never removes a C++ QHorizontalStackedBarSeries.
  - Qt's 'const QHorizontalStackedBarSeriesPrivate
    *QHorizontalStackedBarSeries::d_func() const': takes in Python what
    'QHorizontalStackedBarSeriesPrivate
    *QHorizontalStackedBarSeries::d_func()' takes.

  What has no ritual
  ------------------

  4 of the 13 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QHorizontalStackedBarSeries is created at the first use, not by
    'QHorizontalStackedBarSeries(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QHorizontalStackedBarSeries.
  - Qt tells when it has removed the C++ QHorizontalStackedBarSeries. Every
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
    Calls Qt's 'QString QHorizontalStackedBarSeries::tr(const char *s, const
    char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhorizontalstackedbarseries.html#tr

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
    #  QString QHorizontalStackedBarSeries::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN27QHorizontalStackedBarSeries2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QHorizontalStackedBarSeries'

  #  A C++ QHorizontalStackedBarSeries Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QHorizontalStackedBarSeries'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QHorizontalStackedBarSeries::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhorizontalstackedbarseries.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QHorizontalStackedBarSeries::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK27QHorizontalStackedBarSeries10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def type(self) -> QAbstractSeries.SeriesType:
    """
    Calls Qt's 'QAbstractSeries::SeriesType
    QHorizontalStackedBarSeries::type() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhorizontalstackedbarseries.html#type

    Returns
    -------

    QAbstractSeries.SeriesType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QAbstractSeries.SeriesType(number)' gives.
    """
    #  QAbstractSeries::SeriesType QHorizontalStackedBarSeries::type() const
    ritual = 'ritual_ZNK27QHorizontalStackedBarSeries4typeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK27QHorizontalStackedBarSeries4typeEv'
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
    Notes what was given, for Qt's
    'QHorizontalStackedBarSeries::QHorizontalStackedBarSeries(QObject
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qhorizontalstackedbarseries.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QHorizontalStackedBarSeries::QHorizontalStackedBarSeries(QObject
    #      *parent)
    self._noteCreation(QHorizontalStackedBarSeries, lambda: Rituals.call(
        'ritual_ZN27QHorizontalStackedBarSeriesC1EP7QObject',
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

  def d_func(self) -> Optional[QHorizontalStackedBarSeriesPrivate]:
    """
    Calls Qt's 'QHorizontalStackedBarSeriesPrivate
    *QHorizontalStackedBarSeries::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhorizontalstackedbarseries.html#d_func

    Returns
    -------

    Optional[QHorizontalStackedBarSeriesPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QHorizontalStackedBarSeriesPrivate
    #      *QHorizontalStackedBarSeries::d_func()
    address = self.uglySide.call(
        'ritual_ZN27QHorizontalStackedBarSeries6d_funcEv',
    )
    from . import QHorizontalStackedBarSeriesPrivate
    return QHorizontalStackedBarSeriesPrivate._cuteAt(address)
