"""
QScatterSeriesPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCharts/6.12.0/QtCharts/private/qscatterseries_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QScatterSeriesPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QChart, QXYSeriesPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtWidgets import QGraphicsItem
  from . import ChartTheme, QScatterSeries
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  ChartTheme = WAIT['ChartTheme']
  QGraphicsItem = WAIT['QGraphicsItem']
  QScatterSeries = WAIT['QtCharts:QScatterSeries']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QScatterSeriesPrivate(QXYSeriesPrivate):
  """
  The cute side of Qt's QScatterSeriesPrivate: a plain Python object standing
  in front of one C++ QScatterSeriesPrivate.

  It is built on the cute 'QXYSeriesPrivate', as Qt's QScatterSeriesPrivate
  is built on Qt's QXYSeriesPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QScatterSeriesPrivate that has a ritual and that
  Python can call so far, 3 names in all: 'initializeGraphics',
  'initializeTheme', 'q_func'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void
    QScatterSeriesPrivate::initializeAnimations(QChart::AnimationOptions
    options, int duration, QEasingCurve &curve)': takes a type Python has no
    way to hand over yet.
  - Qt's 'const QScatterSeries *QScatterSeriesPrivate::q_func() const': takes
    in Python what 'QScatterSeries *QScatterSeriesPrivate::q_func()' takes.

  What to expect
  --------------

  - The C++ QScatterSeriesPrivate is created at the first use, not by
    'QScatterSeriesPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QScatterSeriesPrivate.
  - Qt tells when it has removed the C++ QScatterSeriesPrivate. Every call on
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
  __qt_class__ = 'QScatterSeriesPrivate'

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

  @overload(QScatterSeries)
  @overload(NoneType)
  def __init__(self, q: Optional[QScatterSeries]) -> None:
    """
    Notes what was given, for Qt's
    'QScatterSeriesPrivate::QScatterSeriesPrivate(QScatterSeries *q)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qscatterseriesprivate.html#QScatterSeriesPrivate

    Parameters
    ----------

    q : Optional[QScatterSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QScatterSeriesPrivate::QScatterSeriesPrivate(QScatterSeries *q)
    self._noteCreation(QScatterSeriesPrivate, lambda: Rituals.call(
        'ritual_ZN21QScatterSeriesPrivateC1EP14QScatterSeries',
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
    Calls Qt's 'void QScatterSeriesPrivate::initializeGraphics(QGraphicsItem
    *parent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscatterseriesprivate.html#initializeGraphics

    Parameters
    ----------

    parent : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QScatterSeriesPrivate::initializeGraphics(QGraphicsItem *parent)
    ritual = (
        'ritual_ZN21QScatterSeriesPrivate18initializeGraphicsEP13QGraphicsI'
        'tem')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN21QScatterSeriesPrivate18initializeGraphicsEP13QGra'
          'phicsItem')
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
    Calls Qt's 'void QScatterSeriesPrivate::initializeTheme(int index,
    ChartTheme *theme, bool forced)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscatterseriesprivate.html#initializeTheme

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
    #  void QScatterSeriesPrivate::initializeTheme(int index, ChartTheme
    #      *theme, bool forced)
    ritual = (
        'ritual_ZN21QScatterSeriesPrivate15initializeThemeEiP10ChartThemeb')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN21QScatterSeriesPrivate15initializeThemeEiP10ChartT'
          'hemeb')
    self.uglySide.call(ritual, index, self._addressOf(theme), forced)

  def q_func(self) -> Optional[QScatterSeries]:
    """
    Calls Qt's 'QScatterSeries *QScatterSeriesPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qscatterseriesprivate.html#q_func

    Returns
    -------

    Optional[QScatterSeries]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QScatterSeries *QScatterSeriesPrivate::q_func()
    address = self.uglySide.call('ritual_ZN21QScatterSeriesPrivate6q_funcEv')
    from . import QScatterSeries
    return QScatterSeries._cuteAt(address)
