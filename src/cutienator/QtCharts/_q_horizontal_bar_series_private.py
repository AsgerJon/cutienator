"""
QHorizontalBarSeriesPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCharts/6.12.0/QtCharts/private/qhorizontalbarseries_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QHorizontalBarSeriesPrivate to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QAbstractBarSeriesPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtWidgets import QGraphicsItem
  from . import QHorizontalBarSeries
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QGraphicsItem = WAIT['QGraphicsItem']
  QHorizontalBarSeries = WAIT['QHorizontalBarSeries']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QHorizontalBarSeriesPrivate(QAbstractBarSeriesPrivate):
  """
  The cute side of Qt's QHorizontalBarSeriesPrivate: a plain Python object
  standing in front of one C++ QHorizontalBarSeriesPrivate.

  It is built on the cute 'QAbstractBarSeriesPrivate', as Qt's
  QHorizontalBarSeriesPrivate is built on Qt's QAbstractBarSeriesPrivate, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's QHorizontalBarSeriesPrivate that has a ritual and
  that Python can call so far, 3 names in all: 'initializeGraphics',
  'initializeDomain', 'q_func'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QHorizontalBarSeries *QHorizontalBarSeriesPrivate::q_func()
    const': takes in Python what 'QHorizontalBarSeries
    *QHorizontalBarSeriesPrivate::q_func()' takes.

  What to expect
  --------------

  - The C++ QHorizontalBarSeriesPrivate is created at the first use, not by
    'QHorizontalBarSeriesPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QHorizontalBarSeriesPrivate.
  - Qt tells when it has removed the C++ QHorizontalBarSeriesPrivate. Every
    call on the cute object, and every use of it as an argument, then raises
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
  __qt_class__ = 'QHorizontalBarSeriesPrivate'

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

  @overload(QHorizontalBarSeries)
  @overload(NoneType)
  def __init__(self, q: Optional[QHorizontalBarSeries]) -> None:
    """
    Notes what was given, for Qt's
    'QHorizontalBarSeriesPrivate::QHorizontalBarSeriesPrivate(
    QHorizontalBarSeries *q)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qhorizontalbarseriesprivate.html

    Parameters
    ----------

    q : Optional[QHorizontalBarSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QHorizontalBarSeriesPrivate::QHorizontalBarSeriesPrivate(
    #      QHorizontalBarSeries *q)
    self._noteCreation(QHorizontalBarSeriesPrivate, lambda: Rituals.call(
        'ritual_ZN27QHorizontalBarSeriesPrivateC1EP20QHorizontalBarSeries',
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
    QHorizontalBarSeriesPrivate::initializeGraphics(QGraphicsItem *parent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhorizontalbarseriesprivate.html

    Parameters
    ----------

    parent : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QHorizontalBarSeriesPrivate::initializeGraphics(QGraphicsItem
    #      *parent)
    ritual = (
        'ritual_ZN27QHorizontalBarSeriesPrivate18initializeGraphicsEP13QGra'
        'phicsItem')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN27QHorizontalBarSeriesPrivate18initializeGraphicsEP'
          '13QGraphicsItem')
    self.uglySide.call(ritual, self._addressOf(parent, 'QGraphicsItem'))

  def initializeDomain(self) -> None:
    """
    Calls Qt's 'void QHorizontalBarSeriesPrivate::initializeDomain()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhorizontalbarseriesprivate.html#initializeDomain
    """
    #  void QHorizontalBarSeriesPrivate::initializeDomain()
    ritual = 'ritual_ZN27QHorizontalBarSeriesPrivate16initializeDomainEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN27QHorizontalBarSeriesPrivate16initializeDomainEv')
    self.uglySide.call(ritual)

  def q_func(self) -> Optional[QHorizontalBarSeries]:
    """
    Calls Qt's 'QHorizontalBarSeries *QHorizontalBarSeriesPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhorizontalbarseriesprivate.html#q_func

    Returns
    -------

    Optional[QHorizontalBarSeries]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QHorizontalBarSeries *QHorizontalBarSeriesPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN27QHorizontalBarSeriesPrivate6q_funcEv',
    )
    from . import QHorizontalBarSeries
    return QHorizontalBarSeries._cuteAt(address)
