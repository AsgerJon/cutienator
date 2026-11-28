"""
QAreaSeriesPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCharts/6.12.0/QtCharts/private/qareaseries_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QAreaSeriesPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QList
from . import QAbstractAxis, QAbstractSeriesPrivate, QChart

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtWidgets import QGraphicsItem
  from . import ChartTheme, QAreaSeries, QLegend, QLegendMarker, QLineSeries
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  ChartTheme = WAIT['ChartTheme']
  QAreaSeries = WAIT['QtCharts:QAreaSeries']
  QGraphicsItem = WAIT['QGraphicsItem']
  QLegend = WAIT['QLegend']
  QLineSeries = WAIT['QtCharts:QLineSeries']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAreaSeriesPrivate(QAbstractSeriesPrivate):
  """
  The cute side of Qt's QAreaSeriesPrivate: a plain Python object standing in
  front of one C++ QAreaSeriesPrivate.

  It is built on the cute 'QAbstractSeriesPrivate', as Qt's
  QAreaSeriesPrivate is built on Qt's QAbstractSeriesPrivate, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QAreaSeriesPrivate that has a ritual and that Python
  can call so far, 11 names in all: 'metaObject', 'tr', 'initializeDomain',
  'initializeAxes', 'initializeGraphics', 'initializeTheme',
  'createLegendMarkers', 'defaultAxisType', 'createDefaultAxis', 'updated',
  'q_func'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QAreaSeriesPrivate::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QAreaSeriesPrivate::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'void
    QAreaSeriesPrivate::initializeAnimations(QChart::AnimationOptions
    options, int duration, QEasingCurve &curve)': takes a type Python has no
    way to hand over yet.
  - Qt's 'const QAreaSeries *QAreaSeriesPrivate::q_func() const': takes in
    Python what 'QAreaSeries *QAreaSeriesPrivate::q_func()' takes.

  What has no ritual
  ------------------

  2 of the 18 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QAreaSeriesPrivate is created at the first use, not by
    'QAreaSeriesPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAreaSeriesPrivate.
  - Qt tells when it has removed the C++ QAreaSeriesPrivate. Every call on
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
    Calls Qt's 'QString QAreaSeriesPrivate::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qareaseriesprivate.html#tr

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
    #  QString QAreaSeriesPrivate::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN18QAreaSeriesPrivate2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAreaSeriesPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QAreaSeriesPrivate::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qareaseriesprivate.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QAreaSeriesPrivate::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK18QAreaSeriesPrivate10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload(Qt.Orientation)
  def defaultAxisType(
      self,
      orientation: Qt.Orientation,
  ) -> QAbstractAxis.AxisType:
    """
    Calls Qt's 'QAbstractAxis::AxisType
    QAreaSeriesPrivate::defaultAxisType(Qt::Orientation orientation) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qareaseriesprivate.html#defaultAxisType

    Parameters
    ----------

    orientation : Qt.Orientation
      Passed on as its number.

    Returns
    -------

    QAbstractAxis.AxisType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QAbstractAxis.AxisType(number)' gives.
    """
    #  QAbstractAxis::AxisType
    #      QAreaSeriesPrivate::defaultAxisType(Qt::Orientation orientation)
    #      const
    ritual = (
        'ritual_ZNK18QAreaSeriesPrivate15defaultAxisTypeEN2Qt11OrientationE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK18QAreaSeriesPrivate15defaultAxisTypeEN2Qt11Orient'
          'ationE')
    return QAbstractAxis.AxisType(self.uglySide.call(
        ritual, orientation.value,
    ))

  @overload(Qt.Orientation)
  def createDefaultAxis(self, a0: Qt.Orientation) -> Optional[QAbstractAxis]:
    """
    Calls Qt's 'QAbstractAxis
    *QAreaSeriesPrivate::createDefaultAxis(Qt::Orientation a0) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qareaseriesprivate.html#createDefaultAxis

    Parameters
    ----------

    a0 : Qt.Orientation
      Passed on as its number.

    Returns
    -------

    Optional[QAbstractAxis]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractAxis *QAreaSeriesPrivate::createDefaultAxis(Qt::Orientation
    #      a0) const
    ritual = (
        'ritual_ZNK18QAreaSeriesPrivate17createDefaultAxisEN2Qt11Orientatio'
        'nE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK18QAreaSeriesPrivate17createDefaultAxisEN2Qt11Orie'
          'ntationE')
    address = self.uglySide.call(ritual, a0.value)
    return QAbstractAxis._cuteAt(address)

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

  @overload(QLineSeries, QLineSeries, QAreaSeries)
  @overload(QLineSeries, QLineSeries, NoneType)
  @overload(QLineSeries, NoneType, QAreaSeries)
  @overload(QLineSeries, NoneType, NoneType)
  @overload(NoneType, QLineSeries, QAreaSeries)
  @overload(NoneType, QLineSeries, NoneType)
  @overload(NoneType, NoneType, QAreaSeries)
  @overload(NoneType, NoneType, NoneType)
  def __init__(
      self,
      upperSeries: Optional[QLineSeries],
      lowerSeries: Optional[QLineSeries],
      q: Optional[QAreaSeries],
  ) -> None:
    """
    Notes what was given, for Qt's
    'QAreaSeriesPrivate::QAreaSeriesPrivate(QLineSeries *upperSeries,
    QLineSeries *lowerSeries, QAreaSeries *q)', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qareaseriesprivate.html#QAreaSeriesPrivate

    Parameters
    ----------

    upperSeries : Optional[QLineSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    lowerSeries : Optional[QLineSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    q : Optional[QAreaSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QAreaSeriesPrivate::QAreaSeriesPrivate(QLineSeries *upperSeries,
    #      QLineSeries *lowerSeries, QAreaSeries *q)
    self._noteCreation(QAreaSeriesPrivate, lambda: Rituals.call(
        'ritual_ZN18QAreaSeriesPrivateC1EP11QLineSeriesS1_P11QAreaSeries',
        self._addressOf(upperSeries), self._addressOf(lowerSeries),
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
    Calls Qt's 'void QAreaSeriesPrivate::initializeDomain()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qareaseriesprivate.html#initializeDomain
    """
    #  void QAreaSeriesPrivate::initializeDomain()
    ritual = 'ritual_ZN18QAreaSeriesPrivate16initializeDomainEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QAreaSeriesPrivate16initializeDomainEv'
    self.uglySide.call(ritual)

  def initializeAxes(self) -> None:
    """
    Calls Qt's 'void QAreaSeriesPrivate::initializeAxes()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qareaseriesprivate.html#initializeAxes
    """
    #  void QAreaSeriesPrivate::initializeAxes()
    ritual = 'ritual_ZN18QAreaSeriesPrivate14initializeAxesEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QAreaSeriesPrivate14initializeAxesEv'
    self.uglySide.call(ritual)

  @overload(QGraphicsItem)
  @overload(NoneType)
  def initializeGraphics(self, parent: Optional[QGraphicsItem]) -> None:
    """
    Calls Qt's 'void QAreaSeriesPrivate::initializeGraphics(QGraphicsItem
    *parent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qareaseriesprivate.html#initializeGraphics

    Parameters
    ----------

    parent : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAreaSeriesPrivate::initializeGraphics(QGraphicsItem *parent)
    ritual = (
        'ritual_ZN18QAreaSeriesPrivate18initializeGraphicsEP13QGraphicsItem')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QAreaSeriesPrivate18initializeGraphicsEP13QGraphi'
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
    Calls Qt's 'void QAreaSeriesPrivate::initializeTheme(int index,
    ChartTheme *theme, bool forced)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qareaseriesprivate.html#initializeTheme

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
    #  void QAreaSeriesPrivate::initializeTheme(int index, ChartTheme *theme,
    #      bool forced)
    ritual = 'ritual_ZN18QAreaSeriesPrivate15initializeThemeEiP10ChartThemeb'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QAreaSeriesPrivate15initializeThemeEiP10ChartThem'
          'eb')
    self.uglySide.call(ritual, index, self._addressOf(theme), forced)

  @overload(QLegend)
  @overload(NoneType)
  def createLegendMarkers(
      self,
      legend: Optional[QLegend],
  ) -> QList[QLegendMarker]:
    """
    Calls Qt's 'QList<QLegendMarker *>
    QAreaSeriesPrivate::createLegendMarkers(QLegend *legend)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qareaseriesprivate.html#createLegendMarkers

    Parameters
    ----------

    legend : Optional[QLegend]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QList[QLegendMarker]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QLegendMarker *> QAreaSeriesPrivate::createLegendMarkers(QLegend
    #      *legend)
    address = self.uglySide.call(
        'ritual_ZN18QAreaSeriesPrivate19createLegendMarkersEP7QLegend',
        self._addressOf(legend),
    )
    from . import QLegendMarker
    return QList[QLegendMarker]._cuteOwning(address)

  def updated(self) -> None:
    """
    Calls Qt's 'void QAreaSeriesPrivate::updated()'.

    Qt's own words: https://doc.qt.io/qt-6/qareaseriesprivate.html#updated
    """
    #  void QAreaSeriesPrivate::updated()
    self.uglySide.call('ritual_ZN18QAreaSeriesPrivate7updatedEv')

  def q_func(self) -> Optional[QAreaSeries]:
    """
    Calls Qt's 'QAreaSeries *QAreaSeriesPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qareaseriesprivate.html#q_func

    Returns
    -------

    Optional[QAreaSeries]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAreaSeries *QAreaSeriesPrivate::q_func()
    address = self.uglySide.call('ritual_ZN18QAreaSeriesPrivate6q_funcEv')
    from . import QAreaSeries
    return QAreaSeries._cuteAt(address)
