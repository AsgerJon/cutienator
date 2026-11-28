"""
QLineSeriesPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCharts/6.12.0/QtCharts/private/qlineseries_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QLineSeriesPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QXYSeriesPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtWidgets import QGraphicsItem
  from . import ChartTheme, QLineSeries
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  ChartTheme = WAIT['ChartTheme']
  QGraphicsItem = WAIT['QGraphicsItem']
  QLineSeries = WAIT['QtCharts:QLineSeries']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QLineSeriesPrivate(QXYSeriesPrivate):
  """
  The cute side of Qt's QLineSeriesPrivate: a plain Python object standing in
  front of one C++ QLineSeriesPrivate.

  It is built on the cute 'QXYSeriesPrivate', as Qt's QLineSeriesPrivate is
  built on Qt's QXYSeriesPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QLineSeriesPrivate that has a ritual and that Python
  can call so far, 3 names in all: 'initializeGraphics', 'initializeTheme',
  'q_func'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QLineSeries *QLineSeriesPrivate::q_func() const': takes in
    Python what 'QLineSeries *QLineSeriesPrivate::q_func()' takes.

  What to expect
  --------------

  - The C++ QLineSeriesPrivate is created at the first use, not by
    'QLineSeriesPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QLineSeriesPrivate.
  - Qt tells when it has removed the C++ QLineSeriesPrivate. Every call on
    the cute object, and every use of it as an argument, then raises
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
  __qt_class__ = 'QLineSeriesPrivate'

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

  @overload(QLineSeries)
  @overload(NoneType)
  def __init__(self, q: Optional[QLineSeries]) -> None:
    """
    Notes what was given, for Qt's
    'QLineSeriesPrivate::QLineSeriesPrivate(QLineSeries *q)', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qlineseriesprivate.html#QLineSeriesPrivate

    Parameters
    ----------

    q : Optional[QLineSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QLineSeriesPrivate::QLineSeriesPrivate(QLineSeries *q)
    self._noteCreation(QLineSeriesPrivate, lambda: Rituals.call(
        'ritual_ZN18QLineSeriesPrivateC1EP11QLineSeries', self._addressOf(q),
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
    Calls Qt's 'void QLineSeriesPrivate::initializeGraphics(QGraphicsItem
    *parent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlineseriesprivate.html#initializeGraphics

    Parameters
    ----------

    parent : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QLineSeriesPrivate::initializeGraphics(QGraphicsItem *parent)
    ritual = (
        'ritual_ZN18QLineSeriesPrivate18initializeGraphicsEP13QGraphicsItem')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QLineSeriesPrivate18initializeGraphicsEP13QGraphi'
          'csItem')
    self.uglySide.call(ritual, self._addressOf(parent, 'QGraphicsItem'))

  @overload(int, ChartTheme)
  @overload(int, NoneType)
  @overload(int, ChartTheme, bool)
  @overload(int, NoneType, bool)
  def initializeTheme(
      self,
      index: int,
      theme: Optional[ChartTheme],
      forced: bool = False,
  ) -> None:
    """
    Calls Qt's 'void QLineSeriesPrivate::initializeTheme(int index,
    ChartTheme *theme, bool forced)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlineseriesprivate.html#initializeTheme

    Parameters
    ----------

    index : int
      Passed on as it is.

    theme : Optional[ChartTheme]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    forced : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QLineSeriesPrivate::initializeTheme(int index, ChartTheme *theme,
    #      bool forced)
    ritual = 'ritual_ZN18QLineSeriesPrivate15initializeThemeEiP10ChartThemeb'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QLineSeriesPrivate15initializeThemeEiP10ChartThem'
          'eb')
    self.uglySide.call(ritual, index, self._addressOf(theme), forced)

  def q_func(self) -> Optional[QLineSeries]:
    """
    Calls Qt's 'QLineSeries *QLineSeriesPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qlineseriesprivate.html#q_func

    Returns
    -------

    Optional[QLineSeries]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QLineSeries *QLineSeriesPrivate::q_func()
    address = self.uglySide.call('ritual_ZN18QLineSeriesPrivate6q_funcEv')
    from . import QLineSeries
    return QLineSeries._cuteAt(address)
