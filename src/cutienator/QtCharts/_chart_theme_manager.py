"""
ChartThemeManager binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCharts/6.12.0/QtCharts/private/chartthememanager_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means ChartThemeManager to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject
from . import QAbstractSeries, QChart

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QColor, QGradient
  from . import ChartTheme, QAbstractAxis, QLegend
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  ChartTheme = WAIT['ChartTheme']
  QAbstractAxis = WAIT['QtCharts:QAbstractAxis']
  QColor = WAIT['QColor']
  QGradient = WAIT['QGradient']
  QLegend = WAIT['QLegend']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class ChartThemeManager(QObject):
  """
  The cute side of Qt's ChartThemeManager: a plain Python object standing in
  front of one C++ ChartThemeManager.

  It is built on the cute 'QObject', as Qt's ChartThemeManager is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's ChartThemeManager that has a ritual and that Python
  can call so far, 14 names in all: 'metaObject', 'tr', 'setTheme', 'theme',
  'decorateChart', 'decorateLegend', 'updateSeries',
  'generateSeriesGradients', 'colorAt', 'seriesCount', 'handleSeriesAdded',
  'handleSeriesRemoved', 'handleAxisAdded', 'handleAxisRemoved'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *ChartThemeManager::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int ChartThemeManager::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QHash<QAbstractSeries *, int> ChartThemeManager::seriesMap()
    const': gives a type Python has no way to take yet.
  - Qt's 'int ChartThemeManager::createIndexKey(const QList<int> &keys)
    const': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  2 of the 22 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ ChartThemeManager is created at the first use, not by
    'ChartThemeManager(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ ChartThemeManager.
  - Qt tells when it has removed the C++ ChartThemeManager. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's ChartThemeManager that has no cute function yet,
    'createIndexKey', 'seriesMap', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside ChartThemeManager, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class BackgroundShadesMode(CuteNum):
    """
    The enum 'ChartThemeManager::BackgroundShadesMode' of Qt, with the 4
    names Qt gives in it.
    """

    BackgroundShadesNone = Kee[int](0)
    BackgroundShadesVertical = Kee[int](1)
    BackgroundShadesHorizontal = Kee[int](2)
    BackgroundShadesBoth = Kee[int](3)

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
    Calls Qt's 'QString ChartThemeManager::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/chartthememanager.html#tr

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
    #  QString ChartThemeManager::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN17ChartThemeManager2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(QList[QColor])
  def generateSeriesGradients(colors: QList[QColor]) -> QList[QGradient]:
    """
    Calls Qt's 'QList<QGradient>
    ChartThemeManager::generateSeriesGradients(const QList<QColor> &colors)'.

    Qt's own words:
    https://doc.qt.io/qt-6/chartthememanager.html#generateSeriesGradients

    Parameters
    ----------

    colors : QList[QColor]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    Returns
    -------

    QList[QGradient]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QGradient> ChartThemeManager::generateSeriesGradients(const
    #      QList<QColor> &colors)
    address = Rituals.call(
        'ritual_ZN17ChartThemeManager23generateSeriesGradientsERK5QListI6QC'
        'olorE',
        CuteMixin._valueOf(colors),
    )
    from ..QtGui import QGradient
    return QList[QGradient]._cuteOwning(address)

  @staticmethod
  @overload(QColor, QColor, float)
  def colorAt(start: QColor, end: QColor, pos: float) -> QColor:
    """
    Calls Qt's 'QColor ChartThemeManager::colorAt(const QColor &start, const
    QColor &end, qreal pos)'.

    Qt's own words: https://doc.qt.io/qt-6/chartthememanager.html#colorAt

    Parameters
    ----------

    start : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.

    end : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.

    pos : float
      Passed on as it is.

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor ChartThemeManager::colorAt(const QColor &start, const QColor
    #      &end, qreal pos)
    address = Rituals.call(
        'ritual_ZN17ChartThemeManager7colorAtERK6QColorS2_d',
        CuteMixin._valueOf(start), CuteMixin._valueOf(end), pos,
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  @staticmethod
  @overload(QGradient, float)
  def colorAt(gradient: QGradient, pos: float) -> QColor:
    """
    Calls Qt's 'QColor ChartThemeManager::colorAt(const QGradient &gradient,
    qreal pos)'.

    Qt's own words: https://doc.qt.io/qt-6/chartthememanager.html#colorAt

    Parameters
    ----------

    gradient : QGradient
      Passed on as a value: Qt reads the C++ QGradient, which stays Python's
      own.

    pos : float
      Passed on as it is.

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor ChartThemeManager::colorAt(const QGradient &gradient, qreal
    #      pos)
    address = Rituals.call(
        'ritual_ZN17ChartThemeManager7colorAtERK9QGradientd',
        CuteMixin._valueOf(gradient), pos,
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'ChartThemeManager'

  #  A C++ ChartThemeManager Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_ChartThemeManager'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *ChartThemeManager::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/chartthememanager.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *ChartThemeManager::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK17ChartThemeManager10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def theme(self) -> Optional[ChartTheme]:
    """
    Calls Qt's 'ChartTheme *ChartThemeManager::theme() const'.

    Qt's own words: https://doc.qt.io/qt-6/chartthememanager.html#theme

    Returns
    -------

    Optional[ChartTheme]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  ChartTheme *ChartThemeManager::theme() const
    address = self.uglySide.call('ritual_ZNK17ChartThemeManager5themeEv')
    from . import ChartTheme
    return ChartTheme._cuteAt(address)

  @overload(QAbstractSeries.SeriesType)
  def seriesCount(self, type: QAbstractSeries.SeriesType) -> int:
    """
    Calls Qt's 'int
    ChartThemeManager::seriesCount(QAbstractSeries::SeriesType type) const'.

    Qt's own words: https://doc.qt.io/qt-6/chartthememanager.html#seriesCount

    Parameters
    ----------

    type : QAbstractSeries.SeriesType
      Passed on as its number.
    """
    #  int ChartThemeManager::seriesCount(QAbstractSeries::SeriesType type)
    #      const
    return self.uglySide.call(
        'ritual_ZNK17ChartThemeManager11seriesCountEN15QAbstractSeries10Ser'
        'iesTypeE',
        type.value,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QChart.ChartTheme)
  def setTheme(self, theme: QChart.ChartTheme) -> None:
    """
    Calls Qt's 'void ChartThemeManager::setTheme(QChart::ChartTheme theme)'.

    Qt's own words: https://doc.qt.io/qt-6/chartthememanager.html#setTheme

    Parameters
    ----------

    theme : QChart.ChartTheme
      Passed on as its number.
    """
    #  void ChartThemeManager::setTheme(QChart::ChartTheme theme)
    self.uglySide.call(
        'ritual_ZN17ChartThemeManager8setThemeEN6QChart10ChartThemeE',
        theme.value,
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

  @overload(QChart)
  @overload(NoneType)
  def __init__(self, chart: Optional[QChart]) -> None:
    """
    Notes what was given, for Qt's
    'ChartThemeManager::ChartThemeManager(QChart *chart)', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/chartthememanager.html#ChartThemeManager

    Parameters
    ----------

    chart : Optional[QChart]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  ChartThemeManager::ChartThemeManager(QChart *chart)
    self._noteCreation(ChartThemeManager, lambda: Rituals.call(
        'ritual_ZN17ChartThemeManagerC1EP6QChart', self._addressOf(chart),
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

  @overload(QChart, ChartTheme)
  @overload(QChart, NoneType)
  @overload(NoneType, ChartTheme)
  @overload(NoneType, NoneType)
  def decorateChart(
      self,
      chart: Optional[QChart],
      theme: Optional[ChartTheme],
  ) -> None:
    """
    Calls Qt's 'void ChartThemeManager::decorateChart(QChart *chart,
    ChartTheme *theme) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/chartthememanager.html#decorateChart

    Parameters
    ----------

    chart : Optional[QChart]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    theme : Optional[ChartTheme]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void ChartThemeManager::decorateChart(QChart *chart, ChartTheme
    #      *theme) const
    self.uglySide.call(
        'ritual_ZNK17ChartThemeManager13decorateChartEP6QChartP10ChartTheme',
        self._addressOf(chart), self._addressOf(theme),
    )

  @overload(QLegend, ChartTheme)
  @overload(QLegend, NoneType)
  @overload(NoneType, ChartTheme)
  @overload(NoneType, NoneType)
  def decorateLegend(
      self,
      legend: Optional[QLegend],
      theme: Optional[ChartTheme],
  ) -> None:
    """
    Calls Qt's 'void ChartThemeManager::decorateLegend(QLegend *legend,
    ChartTheme *theme) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/chartthememanager.html#decorateLegend

    Parameters
    ----------

    legend : Optional[QLegend]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    theme : Optional[ChartTheme]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void ChartThemeManager::decorateLegend(QLegend *legend, ChartTheme
    #      *theme) const
    self.uglySide.call(
        'ritual_ZNK17ChartThemeManager14decorateLegendEP7QLegendP10ChartThe'
        'me',
        self._addressOf(legend), self._addressOf(theme),
    )

  @overload(QAbstractSeries)
  @overload(NoneType)
  def updateSeries(self, series: Optional[QAbstractSeries]) -> None:
    """
    Calls Qt's 'void ChartThemeManager::updateSeries(QAbstractSeries
    *series)'.

    Qt's own words:
    https://doc.qt.io/qt-6/chartthememanager.html#updateSeries

    Parameters
    ----------

    series : Optional[QAbstractSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void ChartThemeManager::updateSeries(QAbstractSeries *series)
    self.uglySide.call(
        'ritual_ZN17ChartThemeManager12updateSeriesEP15QAbstractSeries',
        self._addressOf(series),
    )

  @overload(QAbstractSeries)
  @overload(NoneType)
  def handleSeriesAdded(self, series: Optional[QAbstractSeries]) -> None:
    """
    Calls Qt's 'void ChartThemeManager::handleSeriesAdded(QAbstractSeries
    *series)'.

    Qt's own words:
    https://doc.qt.io/qt-6/chartthememanager.html#handleSeriesAdded

    Parameters
    ----------

    series : Optional[QAbstractSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void ChartThemeManager::handleSeriesAdded(QAbstractSeries *series)
    self.uglySide.call(
        'ritual_ZN17ChartThemeManager17handleSeriesAddedEP15QAbstractSeries',
        self._addressOf(series),
    )

  @overload(QAbstractSeries)
  @overload(NoneType)
  def handleSeriesRemoved(self, series: Optional[QAbstractSeries]) -> None:
    """
    Calls Qt's 'void ChartThemeManager::handleSeriesRemoved(QAbstractSeries
    *series)'.

    Qt's own words:
    https://doc.qt.io/qt-6/chartthememanager.html#handleSeriesRemoved

    Parameters
    ----------

    series : Optional[QAbstractSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void ChartThemeManager::handleSeriesRemoved(QAbstractSeries *series)
    self.uglySide.call(
        'ritual_ZN17ChartThemeManager19handleSeriesRemovedEP15QAbstractSeri'
        'es',
        self._addressOf(series),
    )

  @overload(QAbstractAxis)
  @overload(NoneType)
  def handleAxisAdded(self, axis: Optional[QAbstractAxis]) -> None:
    """
    Calls Qt's 'void ChartThemeManager::handleAxisAdded(QAbstractAxis
    *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/chartthememanager.html#handleAxisAdded

    Parameters
    ----------

    axis : Optional[QAbstractAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void ChartThemeManager::handleAxisAdded(QAbstractAxis *axis)
    self.uglySide.call(
        'ritual_ZN17ChartThemeManager15handleAxisAddedEP13QAbstractAxis',
        self._addressOf(axis),
    )

  @overload(QAbstractAxis)
  @overload(NoneType)
  def handleAxisRemoved(self, axis: Optional[QAbstractAxis]) -> None:
    """
    Calls Qt's 'void ChartThemeManager::handleAxisRemoved(QAbstractAxis
    *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/chartthememanager.html#handleAxisRemoved

    Parameters
    ----------

    axis : Optional[QAbstractAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void ChartThemeManager::handleAxisRemoved(QAbstractAxis *axis)
    self.uglySide.call(
        'ritual_ZN17ChartThemeManager17handleAxisRemovedEP13QAbstractAxis',
        self._addressOf(axis),
    )

  @staticmethod
  def createIndexKey(*__, **_) -> Never:
    """
    Qt's 'int ChartThemeManager::createIndexKey(const QList<int> &keys)
    const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'ChartThemeManager.createIndexKey' has no cute function yet. Qt's "
        "'int ChartThemeManager::createIndexKey(const QList<int> &keys) "
        "const': takes a type Python has no way to hand over yet.")

  @staticmethod
  def seriesMap(*__, **_) -> Never:
    """
    Qt's 'QHash<QAbstractSeries *, int> ChartThemeManager::seriesMap()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'ChartThemeManager.seriesMap' has no cute function yet. Qt's "
        "'QHash<QAbstractSeries *, int> ChartThemeManager::seriesMap() "
        "const': gives a type Python has no way to take yet.")
