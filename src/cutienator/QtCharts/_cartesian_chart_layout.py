"""
CartesianChartLayout binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCharts/6.12.0/QtCharts/private/cartesianchartlayout_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means CartesianChartLayout to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import QList
from . import AbstractChartLayout

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QRectF
  from . import ChartAxisElement, ChartPresenter
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  ChartAxisElement = WAIT['ChartAxisElement']
  ChartPresenter = WAIT['ChartPresenter']
  QRectF = WAIT['QRectF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class CartesianChartLayout(AbstractChartLayout):
  """
  The cute side of Qt's CartesianChartLayout: a plain Python object standing
  in front of one C++ CartesianChartLayout.

  It is built on the cute 'AbstractChartLayout', as Qt's CartesianChartLayout
  is built on Qt's AbstractChartLayout, and has everything that class has.

  What exists
  -----------

  Every function of Qt's CartesianChartLayout that has a ritual and that
  Python can call so far, 2 names in all: 'calculateAxisMinimum',
  'calculateAxisGeometry'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'CartesianChartLayout::~CartesianChartLayout()': the destructor:
    Python never removes a C++ CartesianChartLayout.

  What to expect
  --------------

  - The C++ CartesianChartLayout is created at the first use, not by
    'CartesianChartLayout(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ CartesianChartLayout.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'CartesianChartLayout'

  #  A C++ CartesianChartLayout Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_CartesianChartLayout'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QRectF, QList[ChartAxisElement])
  def calculateAxisMinimum(
      self,
      minimum: QRectF,
      axes: QList[ChartAxisElement],
  ) -> QRectF:
    """
    Calls Qt's 'QRectF CartesianChartLayout::calculateAxisMinimum(const
    QRectF &minimum, const QList<ChartAxisElement *> &axes) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/cartesianchartlayout.html#calculateAxisMinimum

    Parameters
    ----------

    minimum : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    axes : QList[ChartAxisElement]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF CartesianChartLayout::calculateAxisMinimum(const QRectF
    #      &minimum, const QList<ChartAxisElement *> &axes) const
    address = self.uglySide.call(
        'ritual_ZNK20CartesianChartLayout20calculateAxisMinimumERK6QRectFRK'
        '5QListIP16ChartAxisElementE',
        self._valueOf(minimum), self._valueOf(axes),
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  @overload(QRectF, QList[ChartAxisElement])
  @overload(QRectF, QList[ChartAxisElement], bool)
  def calculateAxisGeometry(
      self,
      geometry: QRectF,
      axes: QList[ChartAxisElement],
      update: bool = True,
  ) -> QRectF:
    """
    Calls Qt's 'QRectF CartesianChartLayout::calculateAxisGeometry(const
    QRectF &geometry, const QList<ChartAxisElement *> &axes, bool update)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/cartesianchartlayout.html#calculateAxisGeometry

    Parameters
    ----------

    geometry : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    axes : QList[ChartAxisElement]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    update : bool
      Passed on as it is. May be left out, as in Qt: it is then True.

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF CartesianChartLayout::calculateAxisGeometry(const QRectF
    #      &geometry, const QList<ChartAxisElement *> &axes, bool update)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK20CartesianChartLayout21calculateAxisGeometryERK6QRectFR'
        'K5QListIP16ChartAxisElementEb',
        self._valueOf(geometry), self._valueOf(axes), update,
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

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

  @overload(ChartPresenter)
  @overload(NoneType)
  def __init__(self, presenter: Optional[ChartPresenter]) -> None:
    """
    Notes what was given, for Qt's
    'CartesianChartLayout::CartesianChartLayout(ChartPresenter *presenter)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/cartesianchartlayout.html#CartesianChartLayout

    Parameters
    ----------

    presenter : Optional[ChartPresenter]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  CartesianChartLayout::CartesianChartLayout(ChartPresenter *presenter)
    self._noteCreation(CartesianChartLayout, lambda: Rituals.call(
        'ritual_ZN20CartesianChartLayoutC1EP14ChartPresenter',
        self._addressOf(presenter),
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
