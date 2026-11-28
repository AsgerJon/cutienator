"""
QBoxPlotSeriesPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCharts/6.12.0/QtCharts/private/qboxplotseries_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QBoxPlotSeriesPrivate to be private: it declares the class in a
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
  from . import ChartTheme, QAbstractSeries, QBarCategoryAxis, QBoxPlotSeries
  from . import QBoxSet, QLegend, QLegendMarker
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  ChartTheme = WAIT['ChartTheme']
  QAbstractSeries = WAIT['QtCharts:QAbstractSeries']
  QBarCategoryAxis = WAIT['QtCharts:QBarCategoryAxis']
  QBoxPlotSeries = WAIT['QBoxPlotSeries']
  QBoxSet = WAIT['QBoxSet']
  QGraphicsItem = WAIT['QGraphicsItem']
  QLegend = WAIT['QLegend']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QBoxPlotSeriesPrivate(QAbstractSeriesPrivate):
  """
  The cute side of Qt's QBoxPlotSeriesPrivate: a plain Python object standing
  in front of one C++ QBoxPlotSeriesPrivate.

  It is built on the cute 'QAbstractSeriesPrivate', as Qt's
  QBoxPlotSeriesPrivate is built on Qt's QAbstractSeriesPrivate, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QBoxPlotSeriesPrivate that has a ritual and that
  Python can call so far, 27 names in all: 'metaObject', 'tr',
  'initializeGraphics', 'initializeDomain', 'initializeAxes',
  'initializeTheme', 'createLegendMarkers', 'defaultAxisType',
  'createDefaultAxis', 'append', 'remove', 'insert', 'boxSetAt', 'max',
  'min', 'populateCategories', 'updated', 'clicked', 'pressed', 'released',
  'doubleClicked', 'updatedBoxes', 'updatedLayout', 'restructuredBoxes',
  'handleSeriesChange', 'handleSeriesRemove', 'q_func'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QBoxPlotSeriesPrivate::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QBoxPlotSeriesPrivate::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QBoxPlotSeriesPrivate::~QBoxPlotSeriesPrivate()': the destructor:
    Python never removes a C++ QBoxPlotSeriesPrivate.
  - Qt's 'void
    QBoxPlotSeriesPrivate::initializeAnimations(QChart::AnimationOptions
    options, int duration, QEasingCurve &curve)': takes a type Python has no
    way to hand over yet.
  - Qt's 'const QBoxPlotSeries *QBoxPlotSeriesPrivate::q_func() const': takes
    in Python what 'QBoxPlotSeries *QBoxPlotSeriesPrivate::q_func()' takes.

  What has no ritual
  ------------------

  2 of the 37 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QBoxPlotSeriesPrivate is created at the first use, not by
    'QBoxPlotSeriesPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QBoxPlotSeriesPrivate.
  - Qt tells when it has removed the C++ QBoxPlotSeriesPrivate. Every call on
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
    Calls Qt's 'QString QBoxPlotSeriesPrivate::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qboxplotseriesprivate.html#tr

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
    #  QString QBoxPlotSeriesPrivate::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN21QBoxPlotSeriesPrivate2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QBoxPlotSeriesPrivate'

  #  A C++ QBoxPlotSeriesPrivate Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QBoxPlotSeriesPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QBoxPlotSeriesPrivate::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qboxplotseriesprivate.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QBoxPlotSeriesPrivate::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK21QBoxPlotSeriesPrivate10metaObjectEv',
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
    QBoxPlotSeriesPrivate::defaultAxisType(Qt::Orientation orientation)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qboxplotseriesprivate.html#defaultAxisType

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
    #      QBoxPlotSeriesPrivate::defaultAxisType(Qt::Orientation
    #      orientation) const
    ritual = (
        'ritual_ZNK21QBoxPlotSeriesPrivate15defaultAxisTypeEN2Qt11Orientati'
        'onE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK21QBoxPlotSeriesPrivate15defaultAxisTypeEN2Qt11Ori'
          'entationE')
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
    *QBoxPlotSeriesPrivate::createDefaultAxis(Qt::Orientation orientation)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qboxplotseriesprivate.html#createDefaultAxis

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
    #  QAbstractAxis
    #      *QBoxPlotSeriesPrivate::createDefaultAxis(Qt::Orientation
    #      orientation) const
    ritual = (
        'ritual_ZNK21QBoxPlotSeriesPrivate17createDefaultAxisEN2Qt11Orienta'
        'tionE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK21QBoxPlotSeriesPrivate17createDefaultAxisEN2Qt11O'
          'rientationE')
    address = self.uglySide.call(ritual, orientation.value)
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

  @overload(QBoxPlotSeries)
  @overload(NoneType)
  def __init__(self, q: Optional[QBoxPlotSeries]) -> None:
    """
    Notes what was given, for Qt's
    'QBoxPlotSeriesPrivate::QBoxPlotSeriesPrivate(QBoxPlotSeries *q)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qboxplotseriesprivate.html#QBoxPlotSeriesPrivate

    Parameters
    ----------

    q : Optional[QBoxPlotSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QBoxPlotSeriesPrivate::QBoxPlotSeriesPrivate(QBoxPlotSeries *q)
    self._noteCreation(QBoxPlotSeriesPrivate, lambda: Rituals.call(
        'ritual_ZN21QBoxPlotSeriesPrivateC1EP14QBoxPlotSeries',
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
    Calls Qt's 'void QBoxPlotSeriesPrivate::initializeGraphics(QGraphicsItem
    *parent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qboxplotseriesprivate.html#initializeGraphics

    Parameters
    ----------

    parent : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QBoxPlotSeriesPrivate::initializeGraphics(QGraphicsItem *parent)
    ritual = (
        'ritual_ZN21QBoxPlotSeriesPrivate18initializeGraphicsEP13QGraphicsI'
        'tem')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN21QBoxPlotSeriesPrivate18initializeGraphicsEP13QGra'
          'phicsItem')
    self.uglySide.call(ritual, self._addressOf(parent, 'QGraphicsItem'))

  def initializeDomain(self) -> None:
    """
    Calls Qt's 'void QBoxPlotSeriesPrivate::initializeDomain()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qboxplotseriesprivate.html#initializeDomain
    """
    #  void QBoxPlotSeriesPrivate::initializeDomain()
    ritual = 'ritual_ZN21QBoxPlotSeriesPrivate16initializeDomainEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QBoxPlotSeriesPrivate16initializeDomainEv'
    self.uglySide.call(ritual)

  def initializeAxes(self) -> None:
    """
    Calls Qt's 'void QBoxPlotSeriesPrivate::initializeAxes()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qboxplotseriesprivate.html#initializeAxes
    """
    #  void QBoxPlotSeriesPrivate::initializeAxes()
    ritual = 'ritual_ZN21QBoxPlotSeriesPrivate14initializeAxesEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QBoxPlotSeriesPrivate14initializeAxesEv'
    self.uglySide.call(ritual)

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
    Calls Qt's 'void QBoxPlotSeriesPrivate::initializeTheme(int index,
    ChartTheme *theme, bool forced)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qboxplotseriesprivate.html#initializeTheme

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
    #  void QBoxPlotSeriesPrivate::initializeTheme(int index, ChartTheme
    #      *theme, bool forced)
    ritual = (
        'ritual_ZN21QBoxPlotSeriesPrivate15initializeThemeEiP10ChartThemeb')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN21QBoxPlotSeriesPrivate15initializeThemeEiP10ChartT'
          'hemeb')
    self.uglySide.call(ritual, index, self._addressOf(theme), forced)

  @overload(QLegend)
  @overload(NoneType)
  def createLegendMarkers(
      self,
      legend: Optional[QLegend],
  ) -> QList[QLegendMarker]:
    """
    Calls Qt's 'QList<QLegendMarker *>
    QBoxPlotSeriesPrivate::createLegendMarkers(QLegend *legend)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qboxplotseriesprivate.html#createLegendMarkers

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
    #  QList<QLegendMarker *>
    #      QBoxPlotSeriesPrivate::createLegendMarkers(QLegend *legend)
    address = self.uglySide.call(
        'ritual_ZN21QBoxPlotSeriesPrivate19createLegendMarkersEP7QLegend',
        self._addressOf(legend),
    )
    from . import QLegendMarker
    return QList[QLegendMarker]._cuteOwning(address)

  @overload(QBoxSet)
  @overload(NoneType)
  def append(self, set: Optional[QBoxSet]) -> bool:
    """
    Calls Qt's 'bool QBoxPlotSeriesPrivate::append(QBoxSet *set)'.

    Qt's own words: https://doc.qt.io/qt-6/qboxplotseriesprivate.html#append

    Parameters
    ----------

    set : Optional[QBoxSet]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QBoxPlotSeriesPrivate::append(QBoxSet *set)
    return self.uglySide.call(
        'ritual_ZN21QBoxPlotSeriesPrivate6appendEP7QBoxSet',
        self._addressOf(set),
    )

  @overload(QList[QBoxSet])
  def append(self, sets: QList[QBoxSet]) -> bool:
    """
    Calls Qt's 'bool QBoxPlotSeriesPrivate::append(const QList<QBoxSet *>
    &sets)'.

    Qt's own words: https://doc.qt.io/qt-6/qboxplotseriesprivate.html#append

    Parameters
    ----------

    sets : QList[QBoxSet]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  bool QBoxPlotSeriesPrivate::append(const QList<QBoxSet *> &sets)
    return self.uglySide.call(
        'ritual_ZN21QBoxPlotSeriesPrivate6appendERK5QListIP7QBoxSetE',
        self._valueOf(sets),
    )

  @overload(QBoxSet)
  @overload(NoneType)
  def remove(self, set: Optional[QBoxSet]) -> bool:
    """
    Calls Qt's 'bool QBoxPlotSeriesPrivate::remove(QBoxSet *set)'.

    Qt's own words: https://doc.qt.io/qt-6/qboxplotseriesprivate.html#remove

    Parameters
    ----------

    set : Optional[QBoxSet]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QBoxPlotSeriesPrivate::remove(QBoxSet *set)
    return self.uglySide.call(
        'ritual_ZN21QBoxPlotSeriesPrivate6removeEP7QBoxSet',
        self._addressOf(set),
    )

  @overload(QList[QBoxSet])
  def remove(self, sets: QList[QBoxSet]) -> bool:
    """
    Calls Qt's 'bool QBoxPlotSeriesPrivate::remove(const QList<QBoxSet *>
    &sets)'.

    Qt's own words: https://doc.qt.io/qt-6/qboxplotseriesprivate.html#remove

    Parameters
    ----------

    sets : QList[QBoxSet]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  bool QBoxPlotSeriesPrivate::remove(const QList<QBoxSet *> &sets)
    return self.uglySide.call(
        'ritual_ZN21QBoxPlotSeriesPrivate6removeERK5QListIP7QBoxSetE',
        self._valueOf(sets),
    )

  @overload(int, QBoxSet)
  @overload(int, NoneType)
  def insert(self, index: int, set: Optional[QBoxSet]) -> bool:
    """
    Calls Qt's 'bool QBoxPlotSeriesPrivate::insert(int index, QBoxSet *set)'.

    Qt's own words: https://doc.qt.io/qt-6/qboxplotseriesprivate.html#insert

    Parameters
    ----------

    index : int
      Passed on as it is.

    set : Optional[QBoxSet]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QBoxPlotSeriesPrivate::insert(int index, QBoxSet *set)
    return self.uglySide.call(
        'ritual_ZN21QBoxPlotSeriesPrivate6insertEiP7QBoxSet',
        index, self._addressOf(set),
    )

  @overload(int)
  def boxSetAt(self, index: int) -> Optional[QBoxSet]:
    """
    Calls Qt's 'QBoxSet *QBoxPlotSeriesPrivate::boxSetAt(int index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qboxplotseriesprivate.html#boxSetAt

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    Optional[QBoxSet]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QBoxSet *QBoxPlotSeriesPrivate::boxSetAt(int index)
    address = self.uglySide.call(
        'ritual_ZN21QBoxPlotSeriesPrivate8boxSetAtEi', index,
    )
    from . import QBoxSet
    return QBoxSet._cuteAt(address)

  def max(self) -> float:
    """
    Calls Qt's 'qreal QBoxPlotSeriesPrivate::max()'.

    Qt's own words: https://doc.qt.io/qt-6/qboxplotseriesprivate.html#max
    """
    #  qreal QBoxPlotSeriesPrivate::max()
    return self.uglySide.call('ritual_ZN21QBoxPlotSeriesPrivate3maxEv')

  def min(self) -> float:
    """
    Calls Qt's 'qreal QBoxPlotSeriesPrivate::min()'.

    Qt's own words: https://doc.qt.io/qt-6/qboxplotseriesprivate.html#min
    """
    #  qreal QBoxPlotSeriesPrivate::min()
    return self.uglySide.call('ritual_ZN21QBoxPlotSeriesPrivate3minEv')

  @overload(QBarCategoryAxis)
  @overload(NoneType)
  def populateCategories(self, axis: Optional[QBarCategoryAxis]) -> None:
    """
    Calls Qt's 'void
    QBoxPlotSeriesPrivate::populateCategories(QBarCategoryAxis *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qboxplotseriesprivate.html#populateCategories

    Parameters
    ----------

    axis : Optional[QBarCategoryAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QBoxPlotSeriesPrivate::populateCategories(QBarCategoryAxis *axis)
    self.uglySide.call(
        'ritual_ZN21QBoxPlotSeriesPrivate18populateCategoriesEP16QBarCatego'
        'ryAxis',
        self._addressOf(axis),
    )

  def updated(self) -> None:
    """
    Calls Qt's 'void QBoxPlotSeriesPrivate::updated()'.

    Qt's own words: https://doc.qt.io/qt-6/qboxplotseriesprivate.html#updated
    """
    #  void QBoxPlotSeriesPrivate::updated()
    self.uglySide.call('ritual_ZN21QBoxPlotSeriesPrivate7updatedEv')

  @overload(int, QBoxSet)
  @overload(int, NoneType)
  def clicked(self, index: int, barset: Optional[QBoxSet]) -> None:
    """
    Calls Qt's 'void QBoxPlotSeriesPrivate::clicked(int index, QBoxSet
    *barset)'.

    Qt's own words: https://doc.qt.io/qt-6/qboxplotseriesprivate.html#clicked

    Parameters
    ----------

    index : int
      Passed on as it is.

    barset : Optional[QBoxSet]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QBoxPlotSeriesPrivate::clicked(int index, QBoxSet *barset)
    self.uglySide.call(
        'ritual_ZN21QBoxPlotSeriesPrivate7clickedEiP7QBoxSet',
        index, self._addressOf(barset),
    )

  @overload(int, QBoxSet)
  @overload(int, NoneType)
  def pressed(self, index: int, barset: Optional[QBoxSet]) -> None:
    """
    Calls Qt's 'void QBoxPlotSeriesPrivate::pressed(int index, QBoxSet
    *barset)'.

    Qt's own words: https://doc.qt.io/qt-6/qboxplotseriesprivate.html#pressed

    Parameters
    ----------

    index : int
      Passed on as it is.

    barset : Optional[QBoxSet]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QBoxPlotSeriesPrivate::pressed(int index, QBoxSet *barset)
    self.uglySide.call(
        'ritual_ZN21QBoxPlotSeriesPrivate7pressedEiP7QBoxSet',
        index, self._addressOf(barset),
    )

  @overload(int, QBoxSet)
  @overload(int, NoneType)
  def released(self, index: int, barset: Optional[QBoxSet]) -> None:
    """
    Calls Qt's 'void QBoxPlotSeriesPrivate::released(int index, QBoxSet
    *barset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qboxplotseriesprivate.html#released

    Parameters
    ----------

    index : int
      Passed on as it is.

    barset : Optional[QBoxSet]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QBoxPlotSeriesPrivate::released(int index, QBoxSet *barset)
    self.uglySide.call(
        'ritual_ZN21QBoxPlotSeriesPrivate8releasedEiP7QBoxSet',
        index, self._addressOf(barset),
    )

  @overload(int, QBoxSet)
  @overload(int, NoneType)
  def doubleClicked(self, index: int, barset: Optional[QBoxSet]) -> None:
    """
    Calls Qt's 'void QBoxPlotSeriesPrivate::doubleClicked(int index, QBoxSet
    *barset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qboxplotseriesprivate.html#doubleClicked

    Parameters
    ----------

    index : int
      Passed on as it is.

    barset : Optional[QBoxSet]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QBoxPlotSeriesPrivate::doubleClicked(int index, QBoxSet *barset)
    self.uglySide.call(
        'ritual_ZN21QBoxPlotSeriesPrivate13doubleClickedEiP7QBoxSet',
        index, self._addressOf(barset),
    )

  def updatedBoxes(self) -> None:
    """
    Calls Qt's 'void QBoxPlotSeriesPrivate::updatedBoxes()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qboxplotseriesprivate.html#updatedBoxes
    """
    #  void QBoxPlotSeriesPrivate::updatedBoxes()
    self.uglySide.call('ritual_ZN21QBoxPlotSeriesPrivate12updatedBoxesEv')

  def updatedLayout(self) -> None:
    """
    Calls Qt's 'void QBoxPlotSeriesPrivate::updatedLayout()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qboxplotseriesprivate.html#updatedLayout
    """
    #  void QBoxPlotSeriesPrivate::updatedLayout()
    self.uglySide.call('ritual_ZN21QBoxPlotSeriesPrivate13updatedLayoutEv')

  def restructuredBoxes(self) -> None:
    """
    Calls Qt's 'void QBoxPlotSeriesPrivate::restructuredBoxes()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qboxplotseriesprivate.html#restructuredBoxes
    """
    #  void QBoxPlotSeriesPrivate::restructuredBoxes()
    self.uglySide.call(
        'ritual_ZN21QBoxPlotSeriesPrivate17restructuredBoxesEv',
    )

  @overload(QAbstractSeries)
  @overload(NoneType)
  def handleSeriesChange(self, series: Optional[QAbstractSeries]) -> None:
    """
    Calls Qt's 'void
    QBoxPlotSeriesPrivate::handleSeriesChange(QAbstractSeries *series)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qboxplotseriesprivate.html#handleSeriesChange

    Parameters
    ----------

    series : Optional[QAbstractSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QBoxPlotSeriesPrivate::handleSeriesChange(QAbstractSeries
    #      *series)
    self.uglySide.call(
        'ritual_ZN21QBoxPlotSeriesPrivate18handleSeriesChangeEP15QAbstractS'
        'eries',
        self._addressOf(series),
    )

  @overload(QAbstractSeries)
  @overload(NoneType)
  def handleSeriesRemove(self, series: Optional[QAbstractSeries]) -> None:
    """
    Calls Qt's 'void
    QBoxPlotSeriesPrivate::handleSeriesRemove(QAbstractSeries *series)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qboxplotseriesprivate.html#handleSeriesRemove

    Parameters
    ----------

    series : Optional[QAbstractSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QBoxPlotSeriesPrivate::handleSeriesRemove(QAbstractSeries
    #      *series)
    self.uglySide.call(
        'ritual_ZN21QBoxPlotSeriesPrivate18handleSeriesRemoveEP15QAbstractS'
        'eries',
        self._addressOf(series),
    )

  def q_func(self) -> Optional[QBoxPlotSeries]:
    """
    Calls Qt's 'QBoxPlotSeries *QBoxPlotSeriesPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qboxplotseriesprivate.html#q_func

    Returns
    -------

    Optional[QBoxPlotSeries]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QBoxPlotSeries *QBoxPlotSeriesPrivate::q_func()
    address = self.uglySide.call('ritual_ZN21QBoxPlotSeriesPrivate6q_funcEv')
    from . import QBoxPlotSeries
    return QBoxPlotSeries._cuteAt(address)
