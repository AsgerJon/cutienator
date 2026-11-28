"""
QAbstractBarSeriesPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCharts/6.12.0/QtCharts/private/qabstractbarseries_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QAbstractBarSeriesPrivate to be private: it declares the class in
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
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from . import ChartTheme, QAbstractBarSeries, QBarCategoryAxis, QBarSet
  from . import QLegend, QLegendMarker
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  ChartTheme = WAIT['ChartTheme']
  QBarCategoryAxis = WAIT['QtCharts:QBarCategoryAxis']
  QBarSet = WAIT['QtCharts:QBarSet']
  QLegend = WAIT['QLegend']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAbstractBarSeriesPrivate(QAbstractSeriesPrivate):
  """
  The cute side of Qt's QAbstractBarSeriesPrivate: a plain Python object
  standing in front of one C++ QAbstractBarSeriesPrivate.

  It is built on the cute 'QAbstractSeriesPrivate', as Qt's
  QAbstractBarSeriesPrivate is built on Qt's QAbstractSeriesPrivate, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QAbstractBarSeriesPrivate that has a ritual and that
  Python can call so far, 53 names in all: 'metaObject', 'tr',
  'categoryCount', 'setBarWidth', 'barWidth', 'setVisible',
  'setLabelsVisible', 'initializeDomain', 'initializeAxes',
  'initializeTheme', 'createLegendMarkers', 'defaultAxisType',
  'createDefaultAxis', 'append', 'remove', 'insert', 'barsetAt', 'min',
  'max', 'valueAt', 'percentageAt', 'categorySum', 'absoluteCategorySum',
  'maxCategorySum', 'minX', 'maxX', 'categoryTop', 'categoryBottom', 'top',
  'bottom', 'blockBarUpdate', 'labelsAngle', 'setVisualsDirty',
  'visualsDirty', 'setLabelsDirty', 'labelsDirty', 'clicked', 'pressed',
  'released', 'doubleClicked', 'updatedBars', 'updatedLayout',
  'restructuredBars', 'labelsVisibleChanged', 'visibleChanged',
  'setValueChanged', 'setValueAdded', 'setValueRemoved',
  'handleSetValueChange', 'handleSetValueAdd', 'handleSetValueRemove',
  'populateCategories', 'q_func'. None can be made from Python: one comes out
  of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QAbstractBarSeriesPrivate::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QAbstractBarSeriesPrivate::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'void
    QAbstractBarSeriesPrivate::initializeAnimations(QChart::AnimationOptions
    options, int duration, QEasingCurve &curve)': takes a type Python has no
    way to hand over yet.
  - Qt's 'const QAbstractBarSeries *QAbstractBarSeriesPrivate::q_func()
    const': takes in Python what 'QAbstractBarSeries
    *QAbstractBarSeriesPrivate::q_func()' takes.

  What has no ritual
  ------------------

  3 of the 62 functions Qt declares: 2 not a gap; 1 the class is abstract, so
  C++ cannot make one, and the C++ class of ours does not fill in every
  function it leaves open.

  What to expect
  --------------

  - The C++ QAbstractBarSeriesPrivate is created at the first use, not by
    'QAbstractBarSeriesPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAbstractBarSeriesPrivate.
  - Qt tells when it has removed the C++ QAbstractBarSeriesPrivate. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QAbstractBarSeriesPrivate that has no cute function
    yet, '__init__', holds a function that raises 'NotImplementedError', and
    its docstring says why.
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
    Calls Qt's 'QString QAbstractBarSeriesPrivate::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractbarseriesprivate.html#tr

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
    #  QString QAbstractBarSeriesPrivate::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN25QAbstractBarSeriesPrivate2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAbstractBarSeriesPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QAbstractBarSeriesPrivate::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractbarseriesprivate.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QAbstractBarSeriesPrivate::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK25QAbstractBarSeriesPrivate10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def categoryCount(self) -> int:
    """
    Calls Qt's 'int QAbstractBarSeriesPrivate::categoryCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractbarseriesprivate.html#categoryCount
    """
    #  int QAbstractBarSeriesPrivate::categoryCount() const
    return self.uglySide.call(
        'ritual_ZNK25QAbstractBarSeriesPrivate13categoryCountEv',
    )

  def barWidth(self) -> float:
    """
    Calls Qt's 'qreal QAbstractBarSeriesPrivate::barWidth() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractbarseriesprivate.html#barWidth
    """
    #  qreal QAbstractBarSeriesPrivate::barWidth() const
    return self.uglySide.call(
        'ritual_ZNK25QAbstractBarSeriesPrivate8barWidthEv',
    )

  @overload(Qt.Orientation)
  def defaultAxisType(
      self,
      orientation: Qt.Orientation,
  ) -> QAbstractAxis.AxisType:
    """
    Calls Qt's 'QAbstractAxis::AxisType
    QAbstractBarSeriesPrivate::defaultAxisType(Qt::Orientation orientation)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractbarseriesprivate.html#defaultAxisType

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
    #      QAbstractBarSeriesPrivate::defaultAxisType(Qt::Orientation
    #      orientation) const
    ritual = (
        'ritual_ZNK25QAbstractBarSeriesPrivate15defaultAxisTypeEN2Qt11Orien'
        'tationE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK25QAbstractBarSeriesPrivate15defaultAxisTypeEN2Qt1'
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
    *QAbstractBarSeriesPrivate::createDefaultAxis(Qt::Orientation
    orientation) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractbarseriesprivate.html#createDefaultAxis

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
    #      *QAbstractBarSeriesPrivate::createDefaultAxis(Qt::Orientation
    #      orientation) const
    ritual = (
        'ritual_ZNK25QAbstractBarSeriesPrivate17createDefaultAxisEN2Qt11Ori'
        'entationE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK25QAbstractBarSeriesPrivate17createDefaultAxisEN2Q'
          't11OrientationE')
    address = self.uglySide.call(ritual, orientation.value)
    return QAbstractAxis._cuteAt(address)

  def labelsAngle(self) -> float:
    """
    Calls Qt's 'qreal QAbstractBarSeriesPrivate::labelsAngle() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractbarseriesprivate.html#labelsAngle
    """
    #  qreal QAbstractBarSeriesPrivate::labelsAngle() const
    return self.uglySide.call(
        'ritual_ZNK25QAbstractBarSeriesPrivate11labelsAngleEv',
    )

  def visualsDirty(self) -> bool:
    """
    Calls Qt's 'bool QAbstractBarSeriesPrivate::visualsDirty() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractbarseriesprivate.html#visualsDirty
    """
    #  bool QAbstractBarSeriesPrivate::visualsDirty() const
    return self.uglySide.call(
        'ritual_ZNK25QAbstractBarSeriesPrivate12visualsDirtyEv',
    )

  def labelsDirty(self) -> bool:
    """
    Calls Qt's 'bool QAbstractBarSeriesPrivate::labelsDirty() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractbarseriesprivate.html#labelsDirty
    """
    #  bool QAbstractBarSeriesPrivate::labelsDirty() const
    return self.uglySide.call(
        'ritual_ZNK25QAbstractBarSeriesPrivate11labelsDirtyEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setBarWidth(self, width: float) -> None:
    """
    Calls Qt's 'void QAbstractBarSeriesPrivate::setBarWidth(qreal width)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractbarseriesprivate.html#setBarWidth

    Parameters
    ----------

    width : float
      Passed on as it is.
    """
    #  void QAbstractBarSeriesPrivate::setBarWidth(qreal width)
    self.uglySide.call(
        'ritual_ZN25QAbstractBarSeriesPrivate11setBarWidthEd', width,
    )

  @overload(bool)
  def setVisible(self, visible: bool) -> None:
    """
    Calls Qt's 'void QAbstractBarSeriesPrivate::setVisible(bool visible)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractbarseriesprivate.html#setVisible

    Parameters
    ----------

    visible : bool
      Passed on as it is.
    """
    #  void QAbstractBarSeriesPrivate::setVisible(bool visible)
    self.uglySide.call(
        'ritual_ZN25QAbstractBarSeriesPrivate10setVisibleEb', visible,
    )

  @overload(bool)
  def setLabelsVisible(self, visible: bool) -> None:
    """
    Calls Qt's 'void QAbstractBarSeriesPrivate::setLabelsVisible(bool
    visible)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractbarseriesprivate.html#setLabelsVisible

    Parameters
    ----------

    visible : bool
      Passed on as it is.
    """
    #  void QAbstractBarSeriesPrivate::setLabelsVisible(bool visible)
    self.uglySide.call(
        'ritual_ZN25QAbstractBarSeriesPrivate16setLabelsVisibleEb', visible,
    )

  @overload(bool)
  def setVisualsDirty(self, dirty: bool) -> None:
    """
    Calls Qt's 'void QAbstractBarSeriesPrivate::setVisualsDirty(bool dirty)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractbarseriesprivate.html#setVisualsDirty

    Parameters
    ----------

    dirty : bool
      Passed on as it is.
    """
    #  void QAbstractBarSeriesPrivate::setVisualsDirty(bool dirty)
    self.uglySide.call(
        'ritual_ZN25QAbstractBarSeriesPrivate15setVisualsDirtyEb', dirty,
    )

  @overload(bool)
  def setLabelsDirty(self, dirty: bool) -> None:
    """
    Calls Qt's 'void QAbstractBarSeriesPrivate::setLabelsDirty(bool dirty)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractbarseriesprivate.html#setLabelsDirty

    Parameters
    ----------

    dirty : bool
      Passed on as it is.
    """
    #  void QAbstractBarSeriesPrivate::setLabelsDirty(bool dirty)
    self.uglySide.call(
        'ritual_ZN25QAbstractBarSeriesPrivate14setLabelsDirtyEb', dirty,
    )

  @overload(int, QBarSet)
  @overload(int, NoneType)
  def setValueChanged(self, index: int, barset: Optional[QBarSet]) -> None:
    """
    Calls Qt's 'void QAbstractBarSeriesPrivate::setValueChanged(int index,
    QBarSet *barset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractbarseriesprivate.html#setValueChanged

    Parameters
    ----------

    index : int
      Passed on as it is.

    barset : Optional[QBarSet]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractBarSeriesPrivate::setValueChanged(int index, QBarSet
    #      *barset)
    self.uglySide.call(
        'ritual_ZN25QAbstractBarSeriesPrivate15setValueChangedEiP7QBarSet',
        index, self._addressOf(barset),
    )

  @overload(int, int, QBarSet)
  @overload(int, int, NoneType)
  def setValueAdded(
      self,
      index: int,
      count: int,
      barset: Optional[QBarSet],
  ) -> None:
    """
    Calls Qt's 'void QAbstractBarSeriesPrivate::setValueAdded(int index, int
    count, QBarSet *barset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractbarseriesprivate.html#setValueAdded

    Parameters
    ----------

    index : int
      Passed on as it is.

    count : int
      Passed on as it is.

    barset : Optional[QBarSet]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractBarSeriesPrivate::setValueAdded(int index, int count,
    #      QBarSet *barset)
    self.uglySide.call(
        'ritual_ZN25QAbstractBarSeriesPrivate13setValueAddedEiiP7QBarSet',
        index, count, self._addressOf(barset),
    )

  @overload(int, int, QBarSet)
  @overload(int, int, NoneType)
  def setValueRemoved(
      self,
      index: int,
      count: int,
      barset: Optional[QBarSet],
  ) -> None:
    """
    Calls Qt's 'void QAbstractBarSeriesPrivate::setValueRemoved(int index,
    int count, QBarSet *barset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractbarseriesprivate.html#setValueRemoved

    Parameters
    ----------

    index : int
      Passed on as it is.

    count : int
      Passed on as it is.

    barset : Optional[QBarSet]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractBarSeriesPrivate::setValueRemoved(int index, int count,
    #      QBarSet *barset)
    self.uglySide.call(
        'ritual_ZN25QAbstractBarSeriesPrivate15setValueRemovedEiiP7QBarSet',
        index, count, self._addressOf(barset),
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's
    'QAbstractBarSeriesPrivate::QAbstractBarSeriesPrivate(QAbstractBarSeries
    *parent)': the class is abstract, so C++ cannot make one, and the C++
    class of ours does not fill in every function it leaves open.
    """
    raise NotImplementedError(
        "'QAbstractBarSeriesPrivate.__init__' has no cute function yet. "
        "Qt's "
        "'QAbstractBarSeriesPrivate::QAbstractBarSeriesPrivate(QAbstractBarS"
        "eries *parent)': the class is abstract, so C++ cannot make one, "
        "and the C++ class of ours does not fill in every function it "
        "leaves open.")

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
    Calls Qt's 'void QAbstractBarSeriesPrivate::initializeDomain()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractbarseriesprivate.html#initializeDomain
    """
    #  void QAbstractBarSeriesPrivate::initializeDomain()
    ritual = 'ritual_ZN25QAbstractBarSeriesPrivate16initializeDomainEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN25QAbstractBarSeriesPrivate16initializeDomainEv'
    self.uglySide.call(ritual)

  def initializeAxes(self) -> None:
    """
    Calls Qt's 'void QAbstractBarSeriesPrivate::initializeAxes()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractbarseriesprivate.html#initializeAxes
    """
    #  void QAbstractBarSeriesPrivate::initializeAxes()
    ritual = 'ritual_ZN25QAbstractBarSeriesPrivate14initializeAxesEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN25QAbstractBarSeriesPrivate14initializeAxesEv'
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
    Calls Qt's 'void QAbstractBarSeriesPrivate::initializeTheme(int index,
    ChartTheme *theme, bool forced)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractbarseriesprivate.html#initializeTheme

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
    #  void QAbstractBarSeriesPrivate::initializeTheme(int index, ChartTheme
    #      *theme, bool forced)
    ritual = (
        'ritual_ZN25QAbstractBarSeriesPrivate15initializeThemeEiP10ChartThe'
        'meb')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN25QAbstractBarSeriesPrivate15initializeThemeEiP10Ch'
          'artThemeb')
    self.uglySide.call(ritual, index, self._addressOf(theme), forced)

  @overload(QLegend)
  @overload(NoneType)
  def createLegendMarkers(
      self,
      legend: Optional[QLegend],
  ) -> QList[QLegendMarker]:
    """
    Calls Qt's 'QList<QLegendMarker *>
    QAbstractBarSeriesPrivate::createLegendMarkers(QLegend *legend)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractbarseriesprivate.html#createLegendMarkers

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
    #      QAbstractBarSeriesPrivate::createLegendMarkers(QLegend *legend)
    address = self.uglySide.call(
        'ritual_ZN25QAbstractBarSeriesPrivate19createLegendMarkersEP7QLegen'
        'd',
        self._addressOf(legend),
    )
    from . import QLegendMarker
    return QList[QLegendMarker]._cuteOwning(address)

  @overload(QBarSet)
  @overload(NoneType)
  def append(self, set: Optional[QBarSet]) -> bool:
    """
    Calls Qt's 'bool QAbstractBarSeriesPrivate::append(QBarSet *set)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractbarseriesprivate.html#append

    Parameters
    ----------

    set : Optional[QBarSet]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QAbstractBarSeriesPrivate::append(QBarSet *set)
    return self.uglySide.call(
        'ritual_ZN25QAbstractBarSeriesPrivate6appendEP7QBarSet',
        self._addressOf(set),
    )

  @overload(QList[QBarSet])
  def append(self, sets: QList[QBarSet]) -> bool:
    """
    Calls Qt's 'bool QAbstractBarSeriesPrivate::append(const QList<QBarSet *>
    &sets)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractbarseriesprivate.html#append

    Parameters
    ----------

    sets : QList[QBarSet]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  bool QAbstractBarSeriesPrivate::append(const QList<QBarSet *> &sets)
    return self.uglySide.call(
        'ritual_ZN25QAbstractBarSeriesPrivate6appendERK5QListIP7QBarSetE',
        self._valueOf(sets),
    )

  @overload(QBarSet)
  @overload(NoneType)
  def remove(self, set: Optional[QBarSet]) -> bool:
    """
    Calls Qt's 'bool QAbstractBarSeriesPrivate::remove(QBarSet *set)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractbarseriesprivate.html#remove

    Parameters
    ----------

    set : Optional[QBarSet]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QAbstractBarSeriesPrivate::remove(QBarSet *set)
    return self.uglySide.call(
        'ritual_ZN25QAbstractBarSeriesPrivate6removeEP7QBarSet',
        self._addressOf(set),
    )

  @overload(QList[QBarSet])
  def remove(self, sets: QList[QBarSet]) -> bool:
    """
    Calls Qt's 'bool QAbstractBarSeriesPrivate::remove(const QList<QBarSet *>
    &sets)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractbarseriesprivate.html#remove

    Parameters
    ----------

    sets : QList[QBarSet]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  bool QAbstractBarSeriesPrivate::remove(const QList<QBarSet *> &sets)
    return self.uglySide.call(
        'ritual_ZN25QAbstractBarSeriesPrivate6removeERK5QListIP7QBarSetE',
        self._valueOf(sets),
    )

  @overload(int, QBarSet)
  @overload(int, NoneType)
  def insert(self, index: int, set: Optional[QBarSet]) -> bool:
    """
    Calls Qt's 'bool QAbstractBarSeriesPrivate::insert(int index, QBarSet
    *set)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractbarseriesprivate.html#insert

    Parameters
    ----------

    index : int
      Passed on as it is.

    set : Optional[QBarSet]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QAbstractBarSeriesPrivate::insert(int index, QBarSet *set)
    return self.uglySide.call(
        'ritual_ZN25QAbstractBarSeriesPrivate6insertEiP7QBarSet',
        index, self._addressOf(set),
    )

  @overload(int)
  def barsetAt(self, index: int) -> Optional[QBarSet]:
    """
    Calls Qt's 'QBarSet *QAbstractBarSeriesPrivate::barsetAt(int index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractbarseriesprivate.html#barsetAt

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    Optional[QBarSet]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QBarSet *QAbstractBarSeriesPrivate::barsetAt(int index)
    address = self.uglySide.call(
        'ritual_ZN25QAbstractBarSeriesPrivate8barsetAtEi', index,
    )
    from . import QBarSet
    return QBarSet._cuteAt(address)

  def min(self) -> float:
    """
    Calls Qt's 'qreal QAbstractBarSeriesPrivate::min()'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractbarseriesprivate.html#min
    """
    #  qreal QAbstractBarSeriesPrivate::min()
    return self.uglySide.call('ritual_ZN25QAbstractBarSeriesPrivate3minEv')

  def max(self) -> float:
    """
    Calls Qt's 'qreal QAbstractBarSeriesPrivate::max()'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractbarseriesprivate.html#max
    """
    #  qreal QAbstractBarSeriesPrivate::max()
    return self.uglySide.call('ritual_ZN25QAbstractBarSeriesPrivate3maxEv')

  @overload(int, int)
  def valueAt(self, set: int, category: int) -> float:
    """
    Calls Qt's 'qreal QAbstractBarSeriesPrivate::valueAt(int set, int
    category)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractbarseriesprivate.html#valueAt

    Parameters
    ----------

    set : int
      Passed on as it is.

    category : int
      Passed on as it is.
    """
    #  qreal QAbstractBarSeriesPrivate::valueAt(int set, int category)
    return self.uglySide.call(
        'ritual_ZN25QAbstractBarSeriesPrivate7valueAtEii', set, category,
    )

  @overload(int, int)
  def percentageAt(self, set: int, category: int) -> float:
    """
    Calls Qt's 'qreal QAbstractBarSeriesPrivate::percentageAt(int set, int
    category)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractbarseriesprivate.html#percentageAt

    Parameters
    ----------

    set : int
      Passed on as it is.

    category : int
      Passed on as it is.
    """
    #  qreal QAbstractBarSeriesPrivate::percentageAt(int set, int category)
    return self.uglySide.call(
        'ritual_ZN25QAbstractBarSeriesPrivate12percentageAtEii',
        set, category,
    )

  @overload(int)
  def categorySum(self, category: int) -> float:
    """
    Calls Qt's 'qreal QAbstractBarSeriesPrivate::categorySum(int category)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractbarseriesprivate.html#categorySum

    Parameters
    ----------

    category : int
      Passed on as it is.
    """
    #  qreal QAbstractBarSeriesPrivate::categorySum(int category)
    return self.uglySide.call(
        'ritual_ZN25QAbstractBarSeriesPrivate11categorySumEi', category,
    )

  @overload(int)
  def absoluteCategorySum(self, category: int) -> float:
    """
    Calls Qt's 'qreal QAbstractBarSeriesPrivate::absoluteCategorySum(int
    category)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractbarseriesprivate.html#absoluteCategorySum

    Parameters
    ----------

    category : int
      Passed on as it is.
    """
    #  qreal QAbstractBarSeriesPrivate::absoluteCategorySum(int category)
    return self.uglySide.call(
        'ritual_ZN25QAbstractBarSeriesPrivate19absoluteCategorySumEi',
        category,
    )

  def maxCategorySum(self) -> float:
    """
    Calls Qt's 'qreal QAbstractBarSeriesPrivate::maxCategorySum()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractbarseriesprivate.html#maxCategorySum
    """
    #  qreal QAbstractBarSeriesPrivate::maxCategorySum()
    return self.uglySide.call(
        'ritual_ZN25QAbstractBarSeriesPrivate14maxCategorySumEv',
    )

  def minX(self) -> float:
    """
    Calls Qt's 'qreal QAbstractBarSeriesPrivate::minX()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractbarseriesprivate.html#minX
    """
    #  qreal QAbstractBarSeriesPrivate::minX()
    return self.uglySide.call('ritual_ZN25QAbstractBarSeriesPrivate4minXEv')

  def maxX(self) -> float:
    """
    Calls Qt's 'qreal QAbstractBarSeriesPrivate::maxX()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractbarseriesprivate.html#maxX
    """
    #  qreal QAbstractBarSeriesPrivate::maxX()
    return self.uglySide.call('ritual_ZN25QAbstractBarSeriesPrivate4maxXEv')

  @overload(int)
  def categoryTop(self, category: int) -> float:
    """
    Calls Qt's 'qreal QAbstractBarSeriesPrivate::categoryTop(int category)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractbarseriesprivate.html#categoryTop

    Parameters
    ----------

    category : int
      Passed on as it is.
    """
    #  qreal QAbstractBarSeriesPrivate::categoryTop(int category)
    return self.uglySide.call(
        'ritual_ZN25QAbstractBarSeriesPrivate11categoryTopEi', category,
    )

  @overload(int)
  def categoryBottom(self, category: int) -> float:
    """
    Calls Qt's 'qreal QAbstractBarSeriesPrivate::categoryBottom(int
    category)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractbarseriesprivate.html#categoryBottom

    Parameters
    ----------

    category : int
      Passed on as it is.
    """
    #  qreal QAbstractBarSeriesPrivate::categoryBottom(int category)
    return self.uglySide.call(
        'ritual_ZN25QAbstractBarSeriesPrivate14categoryBottomEi', category,
    )

  def top(self) -> float:
    """
    Calls Qt's 'qreal QAbstractBarSeriesPrivate::top()'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractbarseriesprivate.html#top
    """
    #  qreal QAbstractBarSeriesPrivate::top()
    return self.uglySide.call('ritual_ZN25QAbstractBarSeriesPrivate3topEv')

  def bottom(self) -> float:
    """
    Calls Qt's 'qreal QAbstractBarSeriesPrivate::bottom()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractbarseriesprivate.html#bottom
    """
    #  qreal QAbstractBarSeriesPrivate::bottom()
    return self.uglySide.call(
        'ritual_ZN25QAbstractBarSeriesPrivate6bottomEv',
    )

  def blockBarUpdate(self) -> bool:
    """
    Calls Qt's 'bool QAbstractBarSeriesPrivate::blockBarUpdate()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractbarseriesprivate.html#blockBarUpdate
    """
    #  bool QAbstractBarSeriesPrivate::blockBarUpdate()
    return self.uglySide.call(
        'ritual_ZN25QAbstractBarSeriesPrivate14blockBarUpdateEv',
    )

  @overload(int, QBarSet)
  @overload(int, NoneType)
  def clicked(self, index: int, barset: Optional[QBarSet]) -> None:
    """
    Calls Qt's 'void QAbstractBarSeriesPrivate::clicked(int index, QBarSet
    *barset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractbarseriesprivate.html#clicked

    Parameters
    ----------

    index : int
      Passed on as it is.

    barset : Optional[QBarSet]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractBarSeriesPrivate::clicked(int index, QBarSet *barset)
    self.uglySide.call(
        'ritual_ZN25QAbstractBarSeriesPrivate7clickedEiP7QBarSet',
        index, self._addressOf(barset),
    )

  @overload(int, QBarSet)
  @overload(int, NoneType)
  def pressed(self, index: int, barset: Optional[QBarSet]) -> None:
    """
    Calls Qt's 'void QAbstractBarSeriesPrivate::pressed(int index, QBarSet
    *barset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractbarseriesprivate.html#pressed

    Parameters
    ----------

    index : int
      Passed on as it is.

    barset : Optional[QBarSet]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractBarSeriesPrivate::pressed(int index, QBarSet *barset)
    self.uglySide.call(
        'ritual_ZN25QAbstractBarSeriesPrivate7pressedEiP7QBarSet',
        index, self._addressOf(barset),
    )

  @overload(int, QBarSet)
  @overload(int, NoneType)
  def released(self, index: int, barset: Optional[QBarSet]) -> None:
    """
    Calls Qt's 'void QAbstractBarSeriesPrivate::released(int index, QBarSet
    *barset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractbarseriesprivate.html#released

    Parameters
    ----------

    index : int
      Passed on as it is.

    barset : Optional[QBarSet]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractBarSeriesPrivate::released(int index, QBarSet *barset)
    self.uglySide.call(
        'ritual_ZN25QAbstractBarSeriesPrivate8releasedEiP7QBarSet',
        index, self._addressOf(barset),
    )

  @overload(int, QBarSet)
  @overload(int, NoneType)
  def doubleClicked(self, index: int, barset: Optional[QBarSet]) -> None:
    """
    Calls Qt's 'void QAbstractBarSeriesPrivate::doubleClicked(int index,
    QBarSet *barset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractbarseriesprivate.html#doubleClicked

    Parameters
    ----------

    index : int
      Passed on as it is.

    barset : Optional[QBarSet]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractBarSeriesPrivate::doubleClicked(int index, QBarSet
    #      *barset)
    self.uglySide.call(
        'ritual_ZN25QAbstractBarSeriesPrivate13doubleClickedEiP7QBarSet',
        index, self._addressOf(barset),
    )

  def updatedBars(self) -> None:
    """
    Calls Qt's 'void QAbstractBarSeriesPrivate::updatedBars()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractbarseriesprivate.html#updatedBars
    """
    #  void QAbstractBarSeriesPrivate::updatedBars()
    self.uglySide.call('ritual_ZN25QAbstractBarSeriesPrivate11updatedBarsEv')

  def updatedLayout(self) -> None:
    """
    Calls Qt's 'void QAbstractBarSeriesPrivate::updatedLayout()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractbarseriesprivate.html#updatedLayout
    """
    #  void QAbstractBarSeriesPrivate::updatedLayout()
    self.uglySide.call(
        'ritual_ZN25QAbstractBarSeriesPrivate13updatedLayoutEv',
    )

  def restructuredBars(self) -> None:
    """
    Calls Qt's 'void QAbstractBarSeriesPrivate::restructuredBars()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractbarseriesprivate.html#restructuredBars
    """
    #  void QAbstractBarSeriesPrivate::restructuredBars()
    self.uglySide.call(
        'ritual_ZN25QAbstractBarSeriesPrivate16restructuredBarsEv',
    )

  @overload(bool)
  def labelsVisibleChanged(self, visible: bool) -> None:
    """
    Calls Qt's 'void QAbstractBarSeriesPrivate::labelsVisibleChanged(bool
    visible)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractbarseriesprivate.html

    Parameters
    ----------

    visible : bool
      Passed on as it is.
    """
    #  void QAbstractBarSeriesPrivate::labelsVisibleChanged(bool visible)
    self.uglySide.call(
        'ritual_ZN25QAbstractBarSeriesPrivate20labelsVisibleChangedEb',
        visible,
    )

  def visibleChanged(self) -> None:
    """
    Calls Qt's 'void QAbstractBarSeriesPrivate::visibleChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractbarseriesprivate.html#visibleChanged
    """
    #  void QAbstractBarSeriesPrivate::visibleChanged()
    self.uglySide.call(
        'ritual_ZN25QAbstractBarSeriesPrivate14visibleChangedEv',
    )

  @overload(int)
  def handleSetValueChange(self, index: int) -> None:
    """
    Calls Qt's 'void QAbstractBarSeriesPrivate::handleSetValueChange(int
    index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractbarseriesprivate.html

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QAbstractBarSeriesPrivate::handleSetValueChange(int index)
    self.uglySide.call(
        'ritual_ZN25QAbstractBarSeriesPrivate20handleSetValueChangeEi',
        index,
    )

  @overload(int, int)
  def handleSetValueAdd(self, index: int, count: int) -> None:
    """
    Calls Qt's 'void QAbstractBarSeriesPrivate::handleSetValueAdd(int index,
    int count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractbarseriesprivate.html#handleSetValueAdd

    Parameters
    ----------

    index : int
      Passed on as it is.

    count : int
      Passed on as it is.
    """
    #  void QAbstractBarSeriesPrivate::handleSetValueAdd(int index, int
    #      count)
    self.uglySide.call(
        'ritual_ZN25QAbstractBarSeriesPrivate17handleSetValueAddEii',
        index, count,
    )

  @overload(int, int)
  def handleSetValueRemove(self, index: int, count: int) -> None:
    """
    Calls Qt's 'void QAbstractBarSeriesPrivate::handleSetValueRemove(int
    index, int count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractbarseriesprivate.html

    Parameters
    ----------

    index : int
      Passed on as it is.

    count : int
      Passed on as it is.
    """
    #  void QAbstractBarSeriesPrivate::handleSetValueRemove(int index, int
    #      count)
    self.uglySide.call(
        'ritual_ZN25QAbstractBarSeriesPrivate20handleSetValueRemoveEii',
        index, count,
    )

  @overload(QBarCategoryAxis)
  @overload(NoneType)
  def populateCategories(self, axis: Optional[QBarCategoryAxis]) -> None:
    """
    Calls Qt's 'void
    QAbstractBarSeriesPrivate::populateCategories(QBarCategoryAxis *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractbarseriesprivate.html#populateCategories

    Parameters
    ----------

    axis : Optional[QBarCategoryAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractBarSeriesPrivate::populateCategories(QBarCategoryAxis
    #      *axis)
    self.uglySide.call(
        'ritual_ZN25QAbstractBarSeriesPrivate18populateCategoriesEP16QBarCa'
        'tegoryAxis',
        self._addressOf(axis),
    )

  def q_func(self) -> Optional[QAbstractBarSeries]:
    """
    Calls Qt's 'QAbstractBarSeries *QAbstractBarSeriesPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractbarseriesprivate.html#q_func

    Returns
    -------

    Optional[QAbstractBarSeries]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractBarSeries *QAbstractBarSeriesPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN25QAbstractBarSeriesPrivate6q_funcEv',
    )
    from . import QAbstractBarSeries
    return QAbstractBarSeries._cuteAt(address)
