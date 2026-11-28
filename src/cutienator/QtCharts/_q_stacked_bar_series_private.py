"""
QStackedBarSeriesPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCharts/6.12.0/QtCharts/private/qstackedbarseries_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QStackedBarSeriesPrivate to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QAbstractBarSeriesPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtWidgets import QGraphicsItem
  from . import QStackedBarSeries
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QGraphicsItem = WAIT['QGraphicsItem']
  QStackedBarSeries = WAIT['QStackedBarSeries']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QStackedBarSeriesPrivate(QAbstractBarSeriesPrivate):
  """
  The cute side of Qt's QStackedBarSeriesPrivate: a plain Python object
  standing in front of one C++ QStackedBarSeriesPrivate.

  It is built on the cute 'QAbstractBarSeriesPrivate', as Qt's
  QStackedBarSeriesPrivate is built on Qt's QAbstractBarSeriesPrivate, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's QStackedBarSeriesPrivate that has a ritual and that
  Python can call so far, 3 names in all: 'initializeGraphics',
  'initializeDomain', 'q_func'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QStackedBarSeries *QStackedBarSeriesPrivate::q_func() const':
    takes in Python what 'QStackedBarSeries
    *QStackedBarSeriesPrivate::q_func()' takes.

  What to expect
  --------------

  - The C++ QStackedBarSeriesPrivate is created at the first use, not by
    'QStackedBarSeriesPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QStackedBarSeriesPrivate.
  - Qt tells when it has removed the C++ QStackedBarSeriesPrivate. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QStackedBarSeriesPrivate'

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

  @overload(QStackedBarSeries)
  @overload(NoneType)
  def __init__(self, q: Optional[QStackedBarSeries]) -> None:
    """
    Notes what was given, for Qt's
    'QStackedBarSeriesPrivate::QStackedBarSeriesPrivate(QStackedBarSeries
    *q)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qstackedbarseriesprivate.html

    Parameters
    ----------

    q : Optional[QStackedBarSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QStackedBarSeriesPrivate::QStackedBarSeriesPrivate(QStackedBarSeries
    #      *q)
    self._noteCreation(QStackedBarSeriesPrivate, lambda: Rituals.call(
        'ritual_ZN24QStackedBarSeriesPrivateC1EP17QStackedBarSeries',
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
    QStackedBarSeriesPrivate::initializeGraphics(QGraphicsItem *parent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstackedbarseriesprivate.html#initializeGraphics

    Parameters
    ----------

    parent : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QStackedBarSeriesPrivate::initializeGraphics(QGraphicsItem
    #      *parent)
    ritual = (
        'ritual_ZN24QStackedBarSeriesPrivate18initializeGraphicsEP13QGraphi'
        'csItem')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN24QStackedBarSeriesPrivate18initializeGraphicsEP13Q'
          'GraphicsItem')
    self.uglySide.call(ritual, self._addressOf(parent, 'QGraphicsItem'))

  def initializeDomain(self) -> None:
    """
    Calls Qt's 'void QStackedBarSeriesPrivate::initializeDomain()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstackedbarseriesprivate.html#initializeDomain
    """
    #  void QStackedBarSeriesPrivate::initializeDomain()
    ritual = 'ritual_ZN24QStackedBarSeriesPrivate16initializeDomainEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN24QStackedBarSeriesPrivate16initializeDomainEv'
    self.uglySide.call(ritual)

  def q_func(self) -> Optional[QStackedBarSeries]:
    """
    Calls Qt's 'QStackedBarSeries *QStackedBarSeriesPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstackedbarseriesprivate.html#q_func

    Returns
    -------

    Optional[QStackedBarSeries]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QStackedBarSeries *QStackedBarSeriesPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN24QStackedBarSeriesPrivate6q_funcEv',
    )
    from . import QStackedBarSeries
    return QStackedBarSeries._cuteAt(address)
