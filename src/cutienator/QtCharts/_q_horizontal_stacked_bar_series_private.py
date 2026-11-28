"""
QHorizontalStackedBarSeriesPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCharts/6.12.0/QtCharts/private/qhorizontalstackedbarseries_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QHorizontalStackedBarSeriesPrivate to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QAbstractBarSeriesPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtWidgets import QGraphicsItem
  from . import QHorizontalStackedBarSeries
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QGraphicsItem = WAIT['QGraphicsItem']
  QHorizontalStackedBarSeries = WAIT['QHorizontalStackedBarSeries']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QHorizontalStackedBarSeriesPrivate(QAbstractBarSeriesPrivate):
  """
  The cute side of Qt's QHorizontalStackedBarSeriesPrivate: a plain Python
  object standing in front of one C++ QHorizontalStackedBarSeriesPrivate.

  It is built on the cute 'QAbstractBarSeriesPrivate', as Qt's
  QHorizontalStackedBarSeriesPrivate is built on Qt's
  QAbstractBarSeriesPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QHorizontalStackedBarSeriesPrivate that has a ritual
  and that Python can call so far, 3 names in all: 'initializeGraphics',
  'initializeDomain', 'q_func'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QHorizontalStackedBarSeries
    *QHorizontalStackedBarSeriesPrivate::q_func() const': takes in Python
    what 'QHorizontalStackedBarSeries
    *QHorizontalStackedBarSeriesPrivate::q_func()' takes.

  What to expect
  --------------

  - The C++ QHorizontalStackedBarSeriesPrivate is created at the first use,
    not by 'QHorizontalStackedBarSeriesPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QHorizontalStackedBarSeriesPrivate.
  - Qt tells when it has removed the C++ QHorizontalStackedBarSeriesPrivate.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QHorizontalStackedBarSeriesPrivate'

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

  @overload(QHorizontalStackedBarSeries)
  @overload(NoneType)
  def __init__(self, q: Optional[QHorizontalStackedBarSeries]) -> None:
    """
    Notes what was given, for Qt's
    'QHorizontalStackedBarSeriesPrivate::QHorizontalStackedBarSeriesPrivate(
    QHorizontalStackedBarSeries *q)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qhorizontalstackedbarseriesprivate.html

    Parameters
    ----------

    q : Optional[QHorizontalStackedBarSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QHorizontalStackedBarSeriesPrivate::
    #      QHorizontalStackedBarSeriesPrivate(QHorizontalStackedBarSeries *q)
    self._noteCreation(
        QHorizontalStackedBarSeriesPrivate, lambda: Rituals.call(
            'ritual_ZN34QHorizontalStackedBarSeriesPrivateC1EP27QHorizontal'
            'StackedBarSeries',
            self._addressOf(q),
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

  @overload(QGraphicsItem)
  @overload(NoneType)
  def initializeGraphics(self, parent: Optional[QGraphicsItem]) -> None:
    """
    Calls Qt's 'void
    QHorizontalStackedBarSeriesPrivate::initializeGraphics(QGraphicsItem
    *parent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhorizontalstackedbarseriesprivate.html

    Parameters
    ----------

    parent : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QHorizontalStackedBarSeriesPrivate::initializeGraphics(
    #      QGraphicsItem *parent)
    ritual = (
        'ritual_ZN34QHorizontalStackedBarSeriesPrivate18initializeGraphicsE'
        'P13QGraphicsItem')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN34QHorizontalStackedBarSeriesPrivate18initializeGra'
          'phicsEP13QGraphicsItem')
    self.uglySide.call(ritual, self._addressOf(parent, 'QGraphicsItem'))

  def initializeDomain(self) -> None:
    """
    Calls Qt's 'void QHorizontalStackedBarSeriesPrivate::initializeDomain()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhorizontalstackedbarseriesprivate.html
    """
    #  void QHorizontalStackedBarSeriesPrivate::initializeDomain()
    ritual = (
        'ritual_ZN34QHorizontalStackedBarSeriesPrivate16initializeDomainEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN34QHorizontalStackedBarSeriesPrivate16initializeDom'
          'ainEv')
    self.uglySide.call(ritual)

  def q_func(self) -> Optional[QHorizontalStackedBarSeries]:
    """
    Calls Qt's 'QHorizontalStackedBarSeries
    *QHorizontalStackedBarSeriesPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhorizontalstackedbarseriesprivate.html#q_func

    Returns
    -------

    Optional[QHorizontalStackedBarSeries]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QHorizontalStackedBarSeries
    #      *QHorizontalStackedBarSeriesPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN34QHorizontalStackedBarSeriesPrivate6q_funcEv',
    )
    from . import QHorizontalStackedBarSeries
    return QHorizontalStackedBarSeries._cuteAt(address)
