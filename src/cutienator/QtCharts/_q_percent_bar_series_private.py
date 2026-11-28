"""
QPercentBarSeriesPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCharts/6.12.0/QtCharts/private/qpercentbarseries_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QPercentBarSeriesPrivate to be private: it declares the class in
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
  from . import QPercentBarSeries
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QGraphicsItem = WAIT['QGraphicsItem']
  QPercentBarSeries = WAIT['QPercentBarSeries']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPercentBarSeriesPrivate(QAbstractBarSeriesPrivate):
  """
  The cute side of Qt's QPercentBarSeriesPrivate: a plain Python object
  standing in front of one C++ QPercentBarSeriesPrivate.

  It is built on the cute 'QAbstractBarSeriesPrivate', as Qt's
  QPercentBarSeriesPrivate is built on Qt's QAbstractBarSeriesPrivate, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's QPercentBarSeriesPrivate that has a ritual and that
  Python can call so far, 3 names in all: 'initializeDomain',
  'initializeGraphics', 'q_func'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QPercentBarSeries *QPercentBarSeriesPrivate::q_func() const':
    takes in Python what 'QPercentBarSeries
    *QPercentBarSeriesPrivate::q_func()' takes.

  What to expect
  --------------

  - The C++ QPercentBarSeriesPrivate is created at the first use, not by
    'QPercentBarSeriesPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QPercentBarSeriesPrivate.
  - Qt tells when it has removed the C++ QPercentBarSeriesPrivate. Every call
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
  __qt_class__ = 'QPercentBarSeriesPrivate'

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

  @overload(QPercentBarSeries)
  @overload(NoneType)
  def __init__(self, q: Optional[QPercentBarSeries]) -> None:
    """
    Notes what was given, for Qt's
    'QPercentBarSeriesPrivate::QPercentBarSeriesPrivate(QPercentBarSeries
    *q)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qpercentbarseriesprivate.html

    Parameters
    ----------

    q : Optional[QPercentBarSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QPercentBarSeriesPrivate::QPercentBarSeriesPrivate(QPercentBarSeries
    #      *q)
    self._noteCreation(QPercentBarSeriesPrivate, lambda: Rituals.call(
        'ritual_ZN24QPercentBarSeriesPrivateC1EP17QPercentBarSeries',
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

  def initializeDomain(self) -> None:
    """
    Calls Qt's 'void QPercentBarSeriesPrivate::initializeDomain()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpercentbarseriesprivate.html#initializeDomain
    """
    #  void QPercentBarSeriesPrivate::initializeDomain()
    ritual = 'ritual_ZN24QPercentBarSeriesPrivate16initializeDomainEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN24QPercentBarSeriesPrivate16initializeDomainEv'
    self.uglySide.call(ritual)

  @overload(QGraphicsItem)
  @overload(NoneType)
  def initializeGraphics(self, parent: Optional[QGraphicsItem]) -> None:
    """
    Calls Qt's 'void
    QPercentBarSeriesPrivate::initializeGraphics(QGraphicsItem *parent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpercentbarseriesprivate.html#initializeGraphics

    Parameters
    ----------

    parent : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPercentBarSeriesPrivate::initializeGraphics(QGraphicsItem
    #      *parent)
    ritual = (
        'ritual_ZN24QPercentBarSeriesPrivate18initializeGraphicsEP13QGraphi'
        'csItem')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN24QPercentBarSeriesPrivate18initializeGraphicsEP13Q'
          'GraphicsItem')
    self.uglySide.call(ritual, self._addressOf(parent, 'QGraphicsItem'))

  def q_func(self) -> Optional[QPercentBarSeries]:
    """
    Calls Qt's 'QPercentBarSeries *QPercentBarSeriesPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpercentbarseriesprivate.html#q_func

    Returns
    -------

    Optional[QPercentBarSeries]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPercentBarSeries *QPercentBarSeriesPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN24QPercentBarSeriesPrivate6q_funcEv',
    )
    from . import QPercentBarSeries
    return QPercentBarSeries._cuteAt(address)
