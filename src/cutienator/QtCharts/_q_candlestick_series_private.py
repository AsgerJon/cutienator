"""
QCandlestickSeriesPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCharts/6.12.0/QtCharts/private/qcandlestickseries_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QCandlestickSeriesPrivate to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
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
  from . import ChartTheme, QAbstractSeries, QBarCategoryAxis
  from . import QCandlestickSeries, QCandlestickSet, QLegend, QLegendMarker
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  ChartTheme = WAIT['ChartTheme']
  QAbstractSeries = WAIT['QtCharts:QAbstractSeries']
  QBarCategoryAxis = WAIT['QtCharts:QBarCategoryAxis']
  QCandlestickSeries = WAIT['QCandlestickSeries']
  QCandlestickSet = WAIT['QCandlestickSet']
  QGraphicsItem = WAIT['QGraphicsItem']
  QLegend = WAIT['QLegend']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QCandlestickSeriesPrivate(QAbstractSeriesPrivate):
  """
  The cute side of Qt's QCandlestickSeriesPrivate: a plain Python object
  standing in front of one C++ QCandlestickSeriesPrivate.

  It is built on the cute 'QAbstractSeriesPrivate', as Qt's
  QCandlestickSeriesPrivate is built on Qt's QAbstractSeriesPrivate, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QCandlestickSeriesPrivate that has a ritual and that
  Python can call so far, 23 names in all: 'metaObject', 'tr',
  'initializeDomain', 'initializeAxes', 'initializeTheme',
  'initializeGraphics', 'createLegendMarkers', 'defaultAxisType',
  'createDefaultAxis', 'append', 'remove', 'insert', 'clicked', 'pressed',
  'released', 'doubleClicked', 'updated', 'updatedLayout',
  'updatedCandlesticks', 'handleSeriesChange', 'handleSeriesRemove',
  'populateBarCategories', 'q_func'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QCandlestickSeriesPrivate::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QCandlestickSeriesPrivate::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QCandlestickSeriesPrivate::~QCandlestickSeriesPrivate()': the
    destructor: Python never removes a C++ QCandlestickSeriesPrivate.
  - Qt's 'void
    QCandlestickSeriesPrivate::initializeAnimations(QChart::AnimationOptions
    options, int duration, QEasingCurve &curve)': takes a type Python has no
    way to hand over yet.
  - Qt's 'const QCandlestickSeries *QCandlestickSeriesPrivate::q_func()
    const': takes in Python what 'QCandlestickSeries
    *QCandlestickSeriesPrivate::q_func()' takes.

  What has no ritual
  ------------------

  2 of the 31 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QCandlestickSeriesPrivate is created at the first use, not by
    'QCandlestickSeriesPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QCandlestickSeriesPrivate.
  - Qt tells when it has removed the C++ QCandlestickSeriesPrivate. Every
    call on the cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QCandlestickSeriesPrivate::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qcandlestickseriesprivate.html#tr

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
    #  QString QCandlestickSeriesPrivate::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN25QCandlestickSeriesPrivate2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCandlestickSeriesPrivate'

  #  A C++ QCandlestickSeriesPrivate Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QCandlestickSeriesPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QCandlestickSeriesPrivate::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcandlestickseriesprivate.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QCandlestickSeriesPrivate::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK25QCandlestickSeriesPrivate10metaObjectEv',
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
    QCandlestickSeriesPrivate::defaultAxisType(Qt::Orientation orientation)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcandlestickseriesprivate.html#defaultAxisType

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
    #      QCandlestickSeriesPrivate::defaultAxisType(Qt::Orientation
    #      orientation) const
    ritual = (
        'ritual_ZNK25QCandlestickSeriesPrivate15defaultAxisTypeEN2Qt11Orien'
        'tationE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK25QCandlestickSeriesPrivate15defaultAxisTypeEN2Qt1'
          '1OrientationE')
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
    *QCandlestickSeriesPrivate::createDefaultAxis(Qt::Orientation
    orientation) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcandlestickseriesprivate.html#createDefaultAxis

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
    #      *QCandlestickSeriesPrivate::createDefaultAxis(Qt::Orientation
    #      orientation) const
    ritual = (
        'ritual_ZNK25QCandlestickSeriesPrivate17createDefaultAxisEN2Qt11Ori'
        'entationE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK25QCandlestickSeriesPrivate17createDefaultAxisEN2Q'
          't11OrientationE')
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

  @overload(QCandlestickSeries)
  @overload(NoneType)
  def __init__(self, q: Optional[QCandlestickSeries]) -> None:
    """
    Notes what was given, for Qt's
    'QCandlestickSeriesPrivate::QCandlestickSeriesPrivate(QCandlestickSeries
    *q)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcandlestickseriesprivate.html

    Parameters
    ----------

    q : Optional[QCandlestickSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QCandlestickSeriesPrivate::QCandlestickSeriesPrivate(
    #      QCandlestickSeries *q)
    self._noteCreation(QCandlestickSeriesPrivate, lambda: Rituals.call(
        'ritual_ZN25QCandlestickSeriesPrivateC1EP18QCandlestickSeries',
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
    Calls Qt's 'void QCandlestickSeriesPrivate::initializeDomain()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcandlestickseriesprivate.html#initializeDomain
    """
    #  void QCandlestickSeriesPrivate::initializeDomain()
    ritual = 'ritual_ZN25QCandlestickSeriesPrivate16initializeDomainEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN25QCandlestickSeriesPrivate16initializeDomainEv'
    self.uglySide.call(ritual)

  def initializeAxes(self) -> None:
    """
    Calls Qt's 'void QCandlestickSeriesPrivate::initializeAxes()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcandlestickseriesprivate.html#initializeAxes
    """
    #  void QCandlestickSeriesPrivate::initializeAxes()
    ritual = 'ritual_ZN25QCandlestickSeriesPrivate14initializeAxesEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN25QCandlestickSeriesPrivate14initializeAxesEv'
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
    Calls Qt's 'void QCandlestickSeriesPrivate::initializeTheme(int index,
    ChartTheme *theme, bool forced)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcandlestickseriesprivate.html#initializeTheme

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
    #  void QCandlestickSeriesPrivate::initializeTheme(int index, ChartTheme
    #      *theme, bool forced)
    ritual = (
        'ritual_ZN25QCandlestickSeriesPrivate15initializeThemeEiP10ChartThe'
        'meb')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN25QCandlestickSeriesPrivate15initializeThemeEiP10Ch'
          'artThemeb')
    self.uglySide.call(ritual, index, self._addressOf(theme), forced)

  @overload(QGraphicsItem)
  @overload(NoneType)
  def initializeGraphics(self, parent: Optional[QGraphicsItem]) -> None:
    """
    Calls Qt's 'void
    QCandlestickSeriesPrivate::initializeGraphics(QGraphicsItem *parent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcandlestickseriesprivate.html#initializeGraphics

    Parameters
    ----------

    parent : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QCandlestickSeriesPrivate::initializeGraphics(QGraphicsItem
    #      *parent)
    ritual = (
        'ritual_ZN25QCandlestickSeriesPrivate18initializeGraphicsEP13QGraph'
        'icsItem')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN25QCandlestickSeriesPrivate18initializeGraphicsEP13'
          'QGraphicsItem')
    self.uglySide.call(ritual, self._addressOf(parent, 'QGraphicsItem'))

  @overload(QLegend)
  @overload(NoneType)
  def createLegendMarkers(
      self,
      legend: Optional[QLegend],
  ) -> QList[QLegendMarker]:
    """
    Calls Qt's 'QList<QLegendMarker *>
    QCandlestickSeriesPrivate::createLegendMarkers(QLegend *legend)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcandlestickseriesprivate.html#createLegendMarkers

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
    #      QCandlestickSeriesPrivate::createLegendMarkers(QLegend *legend)
    address = self.uglySide.call(
        'ritual_ZN25QCandlestickSeriesPrivate19createLegendMarkersEP7QLegen'
        'd',
        self._addressOf(legend),
    )
    from . import QLegendMarker
    return QList[QLegendMarker]._cuteOwning(address)

  @overload(QList[QCandlestickSet])
  def append(self, sets: QList[QCandlestickSet]) -> bool:
    """
    Calls Qt's 'bool QCandlestickSeriesPrivate::append(const
    QList<QCandlestickSet *> &sets)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcandlestickseriesprivate.html#append

    Parameters
    ----------

    sets : QList[QCandlestickSet]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  bool QCandlestickSeriesPrivate::append(const QList<QCandlestickSet *>
    #      &sets)
    return self.uglySide.call(
        'ritual_ZN25QCandlestickSeriesPrivate6appendERK5QListIP15QCandlesti'
        'ckSetE',
        self._valueOf(sets),
    )

  @overload(QList[QCandlestickSet])
  def remove(self, sets: QList[QCandlestickSet]) -> bool:
    """
    Calls Qt's 'bool QCandlestickSeriesPrivate::remove(const
    QList<QCandlestickSet *> &sets)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcandlestickseriesprivate.html#remove

    Parameters
    ----------

    sets : QList[QCandlestickSet]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  bool QCandlestickSeriesPrivate::remove(const QList<QCandlestickSet *>
    #      &sets)
    return self.uglySide.call(
        'ritual_ZN25QCandlestickSeriesPrivate6removeERK5QListIP15QCandlesti'
        'ckSetE',
        self._valueOf(sets),
    )

  @overload(int, QCandlestickSet)
  @overload(int, NoneType)
  def insert(self, index: int, set: Optional[QCandlestickSet]) -> bool:
    """
    Calls Qt's 'bool QCandlestickSeriesPrivate::insert(int index,
    QCandlestickSet *set)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcandlestickseriesprivate.html#insert

    Parameters
    ----------

    index : int
      Passed on as it is.

    set : Optional[QCandlestickSet]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QCandlestickSeriesPrivate::insert(int index, QCandlestickSet
    #      *set)
    return self.uglySide.call(
        'ritual_ZN25QCandlestickSeriesPrivate6insertEiP15QCandlestickSet',
        index, self._addressOf(set),
    )

  @overload(int, QCandlestickSet)
  @overload(int, NoneType)
  def clicked(self, index: int, set: Optional[QCandlestickSet]) -> None:
    """
    Calls Qt's 'void QCandlestickSeriesPrivate::clicked(int index,
    QCandlestickSet *set)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcandlestickseriesprivate.html#clicked

    Parameters
    ----------

    index : int
      Passed on as it is.

    set : Optional[QCandlestickSet]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QCandlestickSeriesPrivate::clicked(int index, QCandlestickSet
    #      *set)
    self.uglySide.call(
        'ritual_ZN25QCandlestickSeriesPrivate7clickedEiP15QCandlestickSet',
        index, self._addressOf(set),
    )

  @overload(int, QCandlestickSet)
  @overload(int, NoneType)
  def pressed(self, index: int, set: Optional[QCandlestickSet]) -> None:
    """
    Calls Qt's 'void QCandlestickSeriesPrivate::pressed(int index,
    QCandlestickSet *set)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcandlestickseriesprivate.html#pressed

    Parameters
    ----------

    index : int
      Passed on as it is.

    set : Optional[QCandlestickSet]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QCandlestickSeriesPrivate::pressed(int index, QCandlestickSet
    #      *set)
    self.uglySide.call(
        'ritual_ZN25QCandlestickSeriesPrivate7pressedEiP15QCandlestickSet',
        index, self._addressOf(set),
    )

  @overload(int, QCandlestickSet)
  @overload(int, NoneType)
  def released(self, index: int, set: Optional[QCandlestickSet]) -> None:
    """
    Calls Qt's 'void QCandlestickSeriesPrivate::released(int index,
    QCandlestickSet *set)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcandlestickseriesprivate.html#released

    Parameters
    ----------

    index : int
      Passed on as it is.

    set : Optional[QCandlestickSet]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QCandlestickSeriesPrivate::released(int index, QCandlestickSet
    #      *set)
    self.uglySide.call(
        'ritual_ZN25QCandlestickSeriesPrivate8releasedEiP15QCandlestickSet',
        index, self._addressOf(set),
    )

  @overload(int, QCandlestickSet)
  @overload(int, NoneType)
  def doubleClicked(
      self,
      index: int,
      set: Optional[QCandlestickSet],
  ) -> None:
    """
    Calls Qt's 'void QCandlestickSeriesPrivate::doubleClicked(int index,
    QCandlestickSet *set)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcandlestickseriesprivate.html#doubleClicked

    Parameters
    ----------

    index : int
      Passed on as it is.

    set : Optional[QCandlestickSet]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QCandlestickSeriesPrivate::doubleClicked(int index,
    #      QCandlestickSet *set)
    self.uglySide.call(
        'ritual_ZN25QCandlestickSeriesPrivate13doubleClickedEiP15QCandlesti'
        'ckSet',
        index, self._addressOf(set),
    )

  def updated(self) -> None:
    """
    Calls Qt's 'void QCandlestickSeriesPrivate::updated()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcandlestickseriesprivate.html#updated
    """
    #  void QCandlestickSeriesPrivate::updated()
    self.uglySide.call('ritual_ZN25QCandlestickSeriesPrivate7updatedEv')

  def updatedLayout(self) -> None:
    """
    Calls Qt's 'void QCandlestickSeriesPrivate::updatedLayout()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcandlestickseriesprivate.html#updatedLayout
    """
    #  void QCandlestickSeriesPrivate::updatedLayout()
    self.uglySide.call(
        'ritual_ZN25QCandlestickSeriesPrivate13updatedLayoutEv',
    )

  def updatedCandlesticks(self) -> None:
    """
    Calls Qt's 'void QCandlestickSeriesPrivate::updatedCandlesticks()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcandlestickseriesprivate.html#updatedCandlesticks
    """
    #  void QCandlestickSeriesPrivate::updatedCandlesticks()
    self.uglySide.call(
        'ritual_ZN25QCandlestickSeriesPrivate19updatedCandlesticksEv',
    )

  @overload(QAbstractSeries)
  @overload(NoneType)
  def handleSeriesChange(self, series: Optional[QAbstractSeries]) -> None:
    """
    Calls Qt's 'void
    QCandlestickSeriesPrivate::handleSeriesChange(QAbstractSeries *series)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcandlestickseriesprivate.html#handleSeriesChange

    Parameters
    ----------

    series : Optional[QAbstractSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QCandlestickSeriesPrivate::handleSeriesChange(QAbstractSeries
    #      *series)
    self.uglySide.call(
        'ritual_ZN25QCandlestickSeriesPrivate18handleSeriesChangeEP15QAbstr'
        'actSeries',
        self._addressOf(series),
    )

  @overload(QAbstractSeries)
  @overload(NoneType)
  def handleSeriesRemove(self, series: Optional[QAbstractSeries]) -> None:
    """
    Calls Qt's 'void
    QCandlestickSeriesPrivate::handleSeriesRemove(QAbstractSeries *series)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcandlestickseriesprivate.html#handleSeriesRemove

    Parameters
    ----------

    series : Optional[QAbstractSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QCandlestickSeriesPrivate::handleSeriesRemove(QAbstractSeries
    #      *series)
    self.uglySide.call(
        'ritual_ZN25QCandlestickSeriesPrivate18handleSeriesRemoveEP15QAbstr'
        'actSeries',
        self._addressOf(series),
    )

  @overload(QBarCategoryAxis)
  @overload(NoneType)
  def populateBarCategories(self, axis: Optional[QBarCategoryAxis]) -> None:
    """
    Calls Qt's 'void
    QCandlestickSeriesPrivate::populateBarCategories(QBarCategoryAxis
    *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcandlestickseriesprivate.html

    Parameters
    ----------

    axis : Optional[QBarCategoryAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QCandlestickSeriesPrivate::populateBarCategories(QBarCategoryAxis
    #      *axis)
    self.uglySide.call(
        'ritual_ZN25QCandlestickSeriesPrivate21populateBarCategoriesEP16QBa'
        'rCategoryAxis',
        self._addressOf(axis),
    )

  def q_func(self) -> Optional[QCandlestickSeries]:
    """
    Calls Qt's 'QCandlestickSeries *QCandlestickSeriesPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcandlestickseriesprivate.html#q_func

    Returns
    -------

    Optional[QCandlestickSeries]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCandlestickSeries *QCandlestickSeriesPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN25QCandlestickSeriesPrivate6q_funcEv',
    )
    from . import QCandlestickSeries
    return QCandlestickSeries._cuteAt(address)
