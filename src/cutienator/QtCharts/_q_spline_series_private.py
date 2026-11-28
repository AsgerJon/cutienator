"""
QSplineSeriesPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCharts/6.12.0/QtCharts/private/qsplineseries_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QSplineSeriesPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QChart, QLineSeriesPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtWidgets import QGraphicsItem
  from . import ChartTheme, QSplineSeries
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  ChartTheme = WAIT['ChartTheme']
  QGraphicsItem = WAIT['QGraphicsItem']
  QSplineSeries = WAIT['QtCharts:QSplineSeries']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSplineSeriesPrivate(QLineSeriesPrivate):
  """
  The cute side of Qt's QSplineSeriesPrivate: a plain Python object standing
  in front of one C++ QSplineSeriesPrivate.

  It is built on the cute 'QLineSeriesPrivate', as Qt's QSplineSeriesPrivate
  is built on Qt's QLineSeriesPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSplineSeriesPrivate that has a ritual and that
  Python can call so far, 5 names in all: 'metaObject', 'tr',
  'initializeTheme', 'initializeGraphics', 'q_func'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QSplineSeriesPrivate::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QSplineSeriesPrivate::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'void
    QSplineSeriesPrivate::initializeAnimations(QChart::AnimationOptions
    options, int duration, QEasingCurve &curve)': takes a type Python has no
    way to hand over yet.
  - Qt's 'const QSplineSeries *QSplineSeriesPrivate::q_func() const': takes
    in Python what 'QSplineSeries *QSplineSeriesPrivate::q_func()' takes.

  What has no ritual
  ------------------

  2 of the 12 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QSplineSeriesPrivate is created at the first use, not by
    'QSplineSeriesPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSplineSeriesPrivate.
  - Qt tells when it has removed the C++ QSplineSeriesPrivate. Every call on
    the cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QSplineSeriesPrivate::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qsplineseriesprivate.html#tr

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
    #  QString QSplineSeriesPrivate::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN20QSplineSeriesPrivate2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSplineSeriesPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QSplineSeriesPrivate::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsplineseriesprivate.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QSplineSeriesPrivate::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK20QSplineSeriesPrivate10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

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

  @overload(QSplineSeries)
  @overload(NoneType)
  def __init__(self, q: Optional[QSplineSeries]) -> None:
    """
    Notes what was given, for Qt's
    'QSplineSeriesPrivate::QSplineSeriesPrivate(QSplineSeries *q)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsplineseriesprivate.html#QSplineSeriesPrivate

    Parameters
    ----------

    q : Optional[QSplineSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QSplineSeriesPrivate::QSplineSeriesPrivate(QSplineSeries *q)
    self._noteCreation(QSplineSeriesPrivate, lambda: Rituals.call(
        'ritual_ZN20QSplineSeriesPrivateC1EP13QSplineSeries',
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
    Calls Qt's 'void QSplineSeriesPrivate::initializeTheme(int index,
    ChartTheme *theme, bool forced)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsplineseriesprivate.html#initializeTheme

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
    #  void QSplineSeriesPrivate::initializeTheme(int index, ChartTheme
    #      *theme, bool forced)
    ritual = (
        'ritual_ZN20QSplineSeriesPrivate15initializeThemeEiP10ChartThemeb')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QSplineSeriesPrivate15initializeThemeEiP10ChartTh'
          'emeb')
    self.uglySide.call(ritual, index, self._addressOf(theme), forced)

  @overload(QGraphicsItem)
  @overload(NoneType)
  def initializeGraphics(self, parent: Optional[QGraphicsItem]) -> None:
    """
    Calls Qt's 'void QSplineSeriesPrivate::initializeGraphics(QGraphicsItem
    *parent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsplineseriesprivate.html#initializeGraphics

    Parameters
    ----------

    parent : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSplineSeriesPrivate::initializeGraphics(QGraphicsItem *parent)
    ritual = (
        'ritual_ZN20QSplineSeriesPrivate18initializeGraphicsEP13QGraphicsIt'
        'em')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QSplineSeriesPrivate18initializeGraphicsEP13QGrap'
          'hicsItem')
    self.uglySide.call(ritual, self._addressOf(parent, 'QGraphicsItem'))

  def q_func(self) -> Optional[QSplineSeries]:
    """
    Calls Qt's 'QSplineSeries *QSplineSeriesPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qsplineseriesprivate.html#q_func

    Returns
    -------

    Optional[QSplineSeries]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSplineSeries *QSplineSeriesPrivate::q_func()
    address = self.uglySide.call('ritual_ZN20QSplineSeriesPrivate6q_funcEv')
    from . import QSplineSeries
    return QSplineSeries._cuteAt(address)
