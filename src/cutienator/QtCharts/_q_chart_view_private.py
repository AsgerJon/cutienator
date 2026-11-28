"""
QChartViewPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCharts/6.12.0/QtCharts/private/qchartview_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QChartViewPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QChart, QChartView
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QChart = WAIT['QChart']
  QChartView = WAIT['QChartView']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QChartViewPrivate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QChartViewPrivate: a plain Python object standing in
  front of one C++ QChartViewPrivate.

  C++ hands a QChartViewPrivate around as a copy, so every C++
  QChartViewPrivate behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QChartViewPrivate that has a ritual and that Python
  can call so far, 2 names in all: 'setChart', 'resize'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QChartViewPrivate::~QChartViewPrivate()': the destructor: Python
    removes its C++ QChartViewPrivate by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QChartViewPrivate is created at the first use, not by
    'QChartViewPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QChartViewPrivate back gives a copy the ritual made
    for Python, in a new cute QChartViewPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QChartViewPrivate'

  #  Qt's '~QChartViewPrivate()'. Naming it makes this a value class: Python
  #  owns every C++ QChartViewPrivate behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN17QChartViewPrivateD1Ev'

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

  @overload(QChart)
  @overload(NoneType)
  def setChart(self, chart: Optional[QChart]) -> None:
    """
    Calls Qt's 'void QChartViewPrivate::setChart(QChart *chart)'.

    Qt's own words: https://doc.qt.io/qt-6/qchartviewprivate.html#setChart

    Parameters
    ----------

    chart : Optional[QChart]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QChartViewPrivate::setChart(QChart *chart)
    self.uglySide.call(
        'ritual_ZN17QChartViewPrivate8setChartEP6QChart',
        self._addressOf(chart),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QChartView)
  @overload(NoneType)
  @overload(QChartView, QChart)
  @overload(QChartView, NoneType)
  @overload(NoneType, QChart)
  @overload(NoneType, NoneType)
  def __init__(
      self,
      q: Optional[QChartView],
      chart: Optional[QChart] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QChartViewPrivate::QChartViewPrivate(QChartView *q, QChart *chart)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qchartviewprivate.html#QChartViewPrivate

    Parameters
    ----------

    q : Optional[QChartView]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    chart : Optional[QChart]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QChartViewPrivate::QChartViewPrivate(QChartView *q, QChart *chart)
    self._noteCreation(QChartViewPrivate, lambda: Rituals.call(
        'ritual_ZN17QChartViewPrivateC1EP10QChartViewP6QChart',
        self._addressOf(q), self._addressOf(chart),
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

  def resize(self) -> None:
    """
    Calls Qt's 'void QChartViewPrivate::resize()'.

    Qt's own words: https://doc.qt.io/qt-6/qchartviewprivate.html#resize
    """
    #  void QChartViewPrivate::resize()
    self.uglySide.call('ritual_ZN17QChartViewPrivate6resizeEv')
