"""
QPieSeriesPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCharts/6.12.0/QtCharts/private/qpieseries_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QPieSeriesPrivate to be private: it declares the class in a
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
  from . import ChartTheme, QLegend, QLegendMarker, QPieSeries
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  ChartTheme = WAIT['ChartTheme']
  QGraphicsItem = WAIT['QGraphicsItem']
  QLegend = WAIT['QLegend']
  QPieSeries = WAIT['QtCharts:QPieSeries']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPieSeriesPrivate(QAbstractSeriesPrivate):
  """
  The cute side of Qt's QPieSeriesPrivate: a plain Python object standing in
  front of one C++ QPieSeriesPrivate.

  It is built on the cute 'QAbstractSeriesPrivate', as Qt's QPieSeriesPrivate
  is built on Qt's QAbstractSeriesPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QPieSeriesPrivate that has a ritual and that Python
  can call so far, 25 names in all: 'metaObject', 'tr', 'initializeDomain',
  'initializeAxes', 'initializeGraphics', 'initializeTheme',
  'createLegendMarkers', 'defaultAxisType', 'createDefaultAxis',
  'updateDerivativeData', 'setSizes', 'fromSeries', 'calculatedDataChanged',
  'pieSizeChanged', 'pieStartAngleChanged', 'pieEndAngleChanged',
  'horizontalPositionChanged', 'verticalPositionChanged',
  'sliceValueChanged', 'sliceClicked', 'sliceHovered', 'slicePressed',
  'sliceReleased', 'sliceDoubleClicked', 'q_func'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QPieSeriesPrivate::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QPieSeriesPrivate::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QPieSeriesPrivate::~QPieSeriesPrivate()': the destructor: Python
    never removes a C++ QPieSeriesPrivate.
  - Qt's 'void
    QPieSeriesPrivate::initializeAnimations(QChart::AnimationOptions options,
    int duration, QEasingCurve &curve)': takes a type Python has no way to
    hand over yet.
  - Qt's 'const QPieSeries *QPieSeriesPrivate::q_func() const': takes in
    Python what 'QPieSeries *QPieSeriesPrivate::q_func()' takes.

  What has no ritual
  ------------------

  2 of the 33 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QPieSeriesPrivate is created at the first use, not by
    'QPieSeriesPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QPieSeriesPrivate.
  - Qt tells when it has removed the C++ QPieSeriesPrivate. Every call on the
    cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QPieSeriesPrivate::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qpieseriesprivate.html#tr

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
    #  QString QPieSeriesPrivate::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN17QPieSeriesPrivate2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(QPieSeries)
  @overload(NoneType)
  def fromSeries(
      series: Optional[QPieSeries],
  ) -> Optional[QPieSeriesPrivate]:
    """
    Calls Qt's 'QPieSeriesPrivate *QPieSeriesPrivate::fromSeries(QPieSeries
    *series)'.

    Qt's own words: https://doc.qt.io/qt-6/qpieseriesprivate.html#fromSeries

    Parameters
    ----------

    series : Optional[QPieSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QPieSeriesPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPieSeriesPrivate *QPieSeriesPrivate::fromSeries(QPieSeries *series)
    address = Rituals.call(
        'ritual_ZN17QPieSeriesPrivate10fromSeriesEP10QPieSeries',
        CuteMixin._addressOf(series),
    )
    return QPieSeriesPrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPieSeriesPrivate'

  #  A C++ QPieSeriesPrivate Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QPieSeriesPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QPieSeriesPrivate::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpieseriesprivate.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QPieSeriesPrivate::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK17QPieSeriesPrivate10metaObjectEv',
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
    QPieSeriesPrivate::defaultAxisType(Qt::Orientation orientation) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpieseriesprivate.html#defaultAxisType

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
    #      QPieSeriesPrivate::defaultAxisType(Qt::Orientation orientation)
    #      const
    ritual = (
        'ritual_ZNK17QPieSeriesPrivate15defaultAxisTypeEN2Qt11OrientationE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK17QPieSeriesPrivate15defaultAxisTypeEN2Qt11Orienta'
          'tionE')
    return QAbstractAxis.AxisType(self.uglySide.call(
        ritual, orientation.value,
    ))

  @overload(Qt.Orientation)
  def createDefaultAxis(
      self,
      orientation: Qt.Orientation,
  ) -> Optional[QAbstractAxis]:
    """
    Calls Qt's 'QAbstractAxis
    *QPieSeriesPrivate::createDefaultAxis(Qt::Orientation orientation)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpieseriesprivate.html#createDefaultAxis

    Parameters
    ----------

    orientation : Qt.Orientation
      Passed on as its number.

    Returns
    -------

    Optional[QAbstractAxis]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractAxis *QPieSeriesPrivate::createDefaultAxis(Qt::Orientation
    #      orientation) const
    ritual = (
        'ritual_ZNK17QPieSeriesPrivate17createDefaultAxisEN2Qt11Orientation'
        'E')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK17QPieSeriesPrivate17createDefaultAxisEN2Qt11Orien'
          'tationE')
    address = self.uglySide.call(ritual, orientation.value)
    return QAbstractAxis._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float, float)
  def setSizes(self, innerSize: float, outerSize: float) -> None:
    """
    Calls Qt's 'void QPieSeriesPrivate::setSizes(qreal innerSize, qreal
    outerSize)'.

    Qt's own words: https://doc.qt.io/qt-6/qpieseriesprivate.html#setSizes

    Parameters
    ----------

    innerSize : float
      Passed on as it is.

    outerSize : float
      Passed on as it is.
    """
    #  void QPieSeriesPrivate::setSizes(qreal innerSize, qreal outerSize)
    self.uglySide.call(
        'ritual_ZN17QPieSeriesPrivate8setSizesEdd', innerSize, outerSize,
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

  @overload(QPieSeries)
  @overload(NoneType)
  def __init__(self, parent: Optional[QPieSeries]) -> None:
    """
    Notes what was given, for Qt's
    'QPieSeriesPrivate::QPieSeriesPrivate(QPieSeries *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qpieseriesprivate.html#QPieSeriesPrivate

    Parameters
    ----------

    parent : Optional[QPieSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QPieSeriesPrivate::QPieSeriesPrivate(QPieSeries *parent)
    self._noteCreation(QPieSeriesPrivate, lambda: Rituals.call(
        'ritual_ZN17QPieSeriesPrivateC1EP10QPieSeries',
        self._addressOf(parent),
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
    Calls Qt's 'void QPieSeriesPrivate::initializeDomain()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpieseriesprivate.html#initializeDomain
    """
    #  void QPieSeriesPrivate::initializeDomain()
    ritual = 'ritual_ZN17QPieSeriesPrivate16initializeDomainEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QPieSeriesPrivate16initializeDomainEv'
    self.uglySide.call(ritual)

  def initializeAxes(self) -> None:
    """
    Calls Qt's 'void QPieSeriesPrivate::initializeAxes()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpieseriesprivate.html#initializeAxes
    """
    #  void QPieSeriesPrivate::initializeAxes()
    ritual = 'ritual_ZN17QPieSeriesPrivate14initializeAxesEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QPieSeriesPrivate14initializeAxesEv'
    self.uglySide.call(ritual)

  @overload(QGraphicsItem)
  @overload(NoneType)
  def initializeGraphics(self, parent: Optional[QGraphicsItem]) -> None:
    """
    Calls Qt's 'void QPieSeriesPrivate::initializeGraphics(QGraphicsItem
    *parent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpieseriesprivate.html#initializeGraphics

    Parameters
    ----------

    parent : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPieSeriesPrivate::initializeGraphics(QGraphicsItem *parent)
    ritual = (
        'ritual_ZN17QPieSeriesPrivate18initializeGraphicsEP13QGraphicsItem')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QPieSeriesPrivate18initializeGraphicsEP13QGraphic'
          'sItem')
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
    Calls Qt's 'void QPieSeriesPrivate::initializeTheme(int index, ChartTheme
    *theme, bool forced)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpieseriesprivate.html#initializeTheme

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
    #  void QPieSeriesPrivate::initializeTheme(int index, ChartTheme *theme,
    #      bool forced)
    ritual = 'ritual_ZN17QPieSeriesPrivate15initializeThemeEiP10ChartThemeb'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QPieSeriesPrivate15initializeThemeEiP10ChartTheme'
          'b')
    self.uglySide.call(ritual, index, self._addressOf(theme), forced)

  @overload(QLegend)
  @overload(NoneType)
  def createLegendMarkers(
      self,
      legend: Optional[QLegend],
  ) -> QList[QLegendMarker]:
    """
    Calls Qt's 'QList<QLegendMarker *>
    QPieSeriesPrivate::createLegendMarkers(QLegend *legend)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpieseriesprivate.html#createLegendMarkers

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
    #  QList<QLegendMarker *> QPieSeriesPrivate::createLegendMarkers(QLegend
    #      *legend)
    address = self.uglySide.call(
        'ritual_ZN17QPieSeriesPrivate19createLegendMarkersEP7QLegend',
        self._addressOf(legend),
    )
    from . import QLegendMarker
    return QList[QLegendMarker]._cuteOwning(address)

  def updateDerivativeData(self) -> None:
    """
    Calls Qt's 'void QPieSeriesPrivate::updateDerivativeData()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpieseriesprivate.html#updateDerivativeData
    """
    #  void QPieSeriesPrivate::updateDerivativeData()
    self.uglySide.call(
        'ritual_ZN17QPieSeriesPrivate20updateDerivativeDataEv',
    )

  def calculatedDataChanged(self) -> None:
    """
    Calls Qt's 'void QPieSeriesPrivate::calculatedDataChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpieseriesprivate.html#calculatedDataChanged
    """
    #  void QPieSeriesPrivate::calculatedDataChanged()
    self.uglySide.call(
        'ritual_ZN17QPieSeriesPrivate21calculatedDataChangedEv',
    )

  def pieSizeChanged(self) -> None:
    """
    Calls Qt's 'void QPieSeriesPrivate::pieSizeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpieseriesprivate.html#pieSizeChanged
    """
    #  void QPieSeriesPrivate::pieSizeChanged()
    self.uglySide.call('ritual_ZN17QPieSeriesPrivate14pieSizeChangedEv')

  def pieStartAngleChanged(self) -> None:
    """
    Calls Qt's 'void QPieSeriesPrivate::pieStartAngleChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpieseriesprivate.html#pieStartAngleChanged
    """
    #  void QPieSeriesPrivate::pieStartAngleChanged()
    self.uglySide.call(
        'ritual_ZN17QPieSeriesPrivate20pieStartAngleChangedEv',
    )

  def pieEndAngleChanged(self) -> None:
    """
    Calls Qt's 'void QPieSeriesPrivate::pieEndAngleChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpieseriesprivate.html#pieEndAngleChanged
    """
    #  void QPieSeriesPrivate::pieEndAngleChanged()
    self.uglySide.call('ritual_ZN17QPieSeriesPrivate18pieEndAngleChangedEv')

  def horizontalPositionChanged(self) -> None:
    """
    Calls Qt's 'void QPieSeriesPrivate::horizontalPositionChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpieseriesprivate.html#horizontalPositionChanged
    """
    #  void QPieSeriesPrivate::horizontalPositionChanged()
    self.uglySide.call(
        'ritual_ZN17QPieSeriesPrivate25horizontalPositionChangedEv',
    )

  def verticalPositionChanged(self) -> None:
    """
    Calls Qt's 'void QPieSeriesPrivate::verticalPositionChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpieseriesprivate.html#verticalPositionChanged
    """
    #  void QPieSeriesPrivate::verticalPositionChanged()
    self.uglySide.call(
        'ritual_ZN17QPieSeriesPrivate23verticalPositionChangedEv',
    )

  def sliceValueChanged(self) -> None:
    """
    Calls Qt's 'void QPieSeriesPrivate::sliceValueChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpieseriesprivate.html#sliceValueChanged
    """
    #  void QPieSeriesPrivate::sliceValueChanged()
    self.uglySide.call('ritual_ZN17QPieSeriesPrivate17sliceValueChangedEv')

  def sliceClicked(self) -> None:
    """
    Calls Qt's 'void QPieSeriesPrivate::sliceClicked()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpieseriesprivate.html#sliceClicked
    """
    #  void QPieSeriesPrivate::sliceClicked()
    self.uglySide.call('ritual_ZN17QPieSeriesPrivate12sliceClickedEv')

  @overload(bool)
  def sliceHovered(self, state: bool) -> None:
    """
    Calls Qt's 'void QPieSeriesPrivate::sliceHovered(bool state)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpieseriesprivate.html#sliceHovered

    Parameters
    ----------

    state : bool
      Passed on as it is.
    """
    #  void QPieSeriesPrivate::sliceHovered(bool state)
    self.uglySide.call('ritual_ZN17QPieSeriesPrivate12sliceHoveredEb', state)

  def slicePressed(self) -> None:
    """
    Calls Qt's 'void QPieSeriesPrivate::slicePressed()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpieseriesprivate.html#slicePressed
    """
    #  void QPieSeriesPrivate::slicePressed()
    self.uglySide.call('ritual_ZN17QPieSeriesPrivate12slicePressedEv')

  def sliceReleased(self) -> None:
    """
    Calls Qt's 'void QPieSeriesPrivate::sliceReleased()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpieseriesprivate.html#sliceReleased
    """
    #  void QPieSeriesPrivate::sliceReleased()
    self.uglySide.call('ritual_ZN17QPieSeriesPrivate13sliceReleasedEv')

  def sliceDoubleClicked(self) -> None:
    """
    Calls Qt's 'void QPieSeriesPrivate::sliceDoubleClicked()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpieseriesprivate.html#sliceDoubleClicked
    """
    #  void QPieSeriesPrivate::sliceDoubleClicked()
    self.uglySide.call('ritual_ZN17QPieSeriesPrivate18sliceDoubleClickedEv')

  def q_func(self) -> Optional[QPieSeries]:
    """
    Calls Qt's 'QPieSeries *QPieSeriesPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qpieseriesprivate.html#q_func

    Returns
    -------

    Optional[QPieSeries]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPieSeries *QPieSeriesPrivate::q_func()
    address = self.uglySide.call('ritual_ZN17QPieSeriesPrivate6q_funcEv')
    from . import QPieSeries
    return QPieSeries._cuteAt(address)
