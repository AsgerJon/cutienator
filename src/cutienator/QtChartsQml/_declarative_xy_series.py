"""
DeclarativeXySeries binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtChartsQml/6.12.0/QtChartsQml/private/declarativexyseries_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means DeclarativeXySeries to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QPointF
  from ..QtCharts import QXYSeries


class DeclarativeXySeries(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's DeclarativeXySeries: a plain Python object standing
  in front of one C++ DeclarativeXySeries.

  What exists
  -----------

  Every function of Qt's DeclarativeXySeries that has a ritual and that
  Python can call so far, 10 names in all: 'classBegin', 'componentComplete',
  'xySeries', 'append', 'replace', 'remove', 'removePoints', 'insert',
  'clear', 'at'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'DeclarativeXySeries::~DeclarativeXySeries()': the destructor:
    Python never removes a C++ DeclarativeXySeries.

  What to expect
  --------------

  - The C++ DeclarativeXySeries is created at the first use, not by
    'DeclarativeXySeries(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ DeclarativeXySeries.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'DeclarativeXySeries'

  #  A C++ DeclarativeXySeries Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_DeclarativeXySeries'

  #  The functions Qt calls itself that DeclarativeXySeries is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'xySeries': (
          ('_ZN19DeclarativeXySeries8xySeriesEv',
           ('address', 'address', 'QtCharts:QXYSeries'),
           ()),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'DeclarativeXySeries::DeclarativeXySeries()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativexyseries.html#DeclarativeXySeries
    """
    #  DeclarativeXySeries::DeclarativeXySeries()
    self._noteCreation(DeclarativeXySeries, lambda: Rituals.call(
        'ritual_ZN19DeclarativeXySeriesC1Ev',
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

  def classBegin(self) -> None:
    """
    Calls Qt's 'void DeclarativeXySeries::classBegin()'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativexyseries.html#classBegin
    """
    #  void DeclarativeXySeries::classBegin()
    self._callAs(
        'DeclarativeXySeries',
        'ritual_ZN19DeclarativeXySeries10classBeginEv',
    )

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void DeclarativeXySeries::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativexyseries.html#componentComplete
    """
    #  void DeclarativeXySeries::componentComplete()
    self._callAs(
        'DeclarativeXySeries',
        'ritual_ZN19DeclarativeXySeries17componentCompleteEv',
    )

  def xySeries(self) -> Optional[QXYSeries]:
    """
    Calls Qt's 'QXYSeries *DeclarativeXySeries::xySeries()'.

    Qt's own words: https://doc.qt.io/qt-6/declarativexyseries.html#xySeries

    Returns
    -------

    Optional[QXYSeries]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QXYSeries *DeclarativeXySeries::xySeries()
    address = self._callAs(
        'DeclarativeXySeries', 'ritual_ZN19DeclarativeXySeries8xySeriesEv',
    )
    from ..QtCharts import QXYSeries
    return QXYSeries._cuteAt(address)

  @overload(float, float)
  def append(self, x: float, y: float) -> None:
    """
    Calls Qt's 'void DeclarativeXySeries::append(qreal x, qreal y)'.

    Qt's own words: https://doc.qt.io/qt-6/declarativexyseries.html#append

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.
    """
    #  void DeclarativeXySeries::append(qreal x, qreal y)
    self._callAs(
        'DeclarativeXySeries', 'ritual_ZN19DeclarativeXySeries6appendEdd',
        x, y,
    )

  @overload(float, float, float, float)
  def replace(
      self,
      oldX: float,
      oldY: float,
      newX: float,
      newY: float,
  ) -> None:
    """
    Calls Qt's 'void DeclarativeXySeries::replace(qreal oldX, qreal oldY,
    qreal newX, qreal newY)'.

    Qt's own words: https://doc.qt.io/qt-6/declarativexyseries.html#replace

    Parameters
    ----------

    oldX : float
      Passed on as it is.

    oldY : float
      Passed on as it is.

    newX : float
      Passed on as it is.

    newY : float
      Passed on as it is.
    """
    #  void DeclarativeXySeries::replace(qreal oldX, qreal oldY, qreal newX,
    #      qreal newY)
    self._callAs(
        'DeclarativeXySeries', 'ritual_ZN19DeclarativeXySeries7replaceEdddd',
        oldX, oldY, newX, newY,
    )

  @overload(int, float, float)
  def replace(self, index: int, newX: float, newY: float) -> None:
    """
    Calls Qt's 'void DeclarativeXySeries::replace(int index, qreal newX,
    qreal newY)'.

    Qt's own words: https://doc.qt.io/qt-6/declarativexyseries.html#replace

    Parameters
    ----------

    index : int
      Passed on as it is.

    newX : float
      Passed on as it is.

    newY : float
      Passed on as it is.
    """
    #  void DeclarativeXySeries::replace(int index, qreal newX, qreal newY)
    self._callAs(
        'DeclarativeXySeries', 'ritual_ZN19DeclarativeXySeries7replaceEidd',
        index, newX, newY,
    )

  @overload(float, float)
  def remove(self, x: float, y: float) -> None:
    """
    Calls Qt's 'void DeclarativeXySeries::remove(qreal x, qreal y)'.

    Qt's own words: https://doc.qt.io/qt-6/declarativexyseries.html#remove

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.
    """
    #  void DeclarativeXySeries::remove(qreal x, qreal y)
    self._callAs(
        'DeclarativeXySeries', 'ritual_ZN19DeclarativeXySeries6removeEdd',
        x, y,
    )

  @overload(int)
  def remove(self, index: int) -> None:
    """
    Calls Qt's 'void DeclarativeXySeries::remove(int index)'.

    Qt's own words: https://doc.qt.io/qt-6/declarativexyseries.html#remove

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void DeclarativeXySeries::remove(int index)
    self._callAs(
        'DeclarativeXySeries', 'ritual_ZN19DeclarativeXySeries6removeEi',
        index,
    )

  @overload(int, int)
  def removePoints(self, index: int, count: int) -> None:
    """
    Calls Qt's 'void DeclarativeXySeries::removePoints(int index, int
    count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativexyseries.html#removePoints

    Parameters
    ----------

    index : int
      Passed on as it is.

    count : int
      Passed on as it is.
    """
    #  void DeclarativeXySeries::removePoints(int index, int count)
    self._callAs(
        'DeclarativeXySeries',
        'ritual_ZN19DeclarativeXySeries12removePointsEii',
        index, count,
    )

  @overload(int, float, float)
  def insert(self, index: int, x: float, y: float) -> None:
    """
    Calls Qt's 'void DeclarativeXySeries::insert(int index, qreal x, qreal
    y)'.

    Qt's own words: https://doc.qt.io/qt-6/declarativexyseries.html#insert

    Parameters
    ----------

    index : int
      Passed on as it is.

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.
    """
    #  void DeclarativeXySeries::insert(int index, qreal x, qreal y)
    self._callAs(
        'DeclarativeXySeries', 'ritual_ZN19DeclarativeXySeries6insertEidd',
        index, x, y,
    )

  def clear(self) -> None:
    """
    Calls Qt's 'void DeclarativeXySeries::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/declarativexyseries.html#clear
    """
    #  void DeclarativeXySeries::clear()
    self._callAs(
        'DeclarativeXySeries', 'ritual_ZN19DeclarativeXySeries5clearEv',
    )

  @overload(int)
  def at(self, index: int) -> QPointF:
    """
    Calls Qt's 'QPointF DeclarativeXySeries::at(int index)'.

    Qt's own words: https://doc.qt.io/qt-6/declarativexyseries.html#at

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF DeclarativeXySeries::at(int index)
    address = self._callAs(
        'DeclarativeXySeries', 'ritual_ZN19DeclarativeXySeries2atEi', index,
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)
