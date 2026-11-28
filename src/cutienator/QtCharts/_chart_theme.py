"""
ChartTheme binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCharts/6.12.0/QtCharts/private/charttheme_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means ChartTheme to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute
from ..occult import Rituals
from ..QtCore import QList
from . import QChart

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtGui import QBrush, QColor, QFont, QGradient, QLinearGradient, QPen


class ChartTheme(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's ChartTheme: a plain Python object standing in front
  of one C++ ChartTheme.

  C++ hands a ChartTheme around as a copy, so every C++ ChartTheme behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's ChartTheme that has a ritual and that Python can
  call so far, 15 names in all: 'id', 'seriesGradients', 'seriesColors',
  'chartBackgroundGradient', 'masterFont', 'labelFont', 'labelBrush',
  'axisLinePen', 'backgroundShadesPen', 'outlinePen',
  'backgroundShadesBrush', 'backgroundShades',
  'isBackgroundDropShadowEnabled', 'gridLinePen', 'minorGridLinePen'. It can
  be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'ChartTheme::~ChartTheme()': the destructor: Python removes its C++
    ChartTheme by it, and has no other use for it.

  What to expect
  --------------

  - The C++ ChartTheme is created at the first use, not by 'ChartTheme(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a ChartTheme back gives a copy the ritual made for
    Python, in a new cute ChartTheme.
  """

  #  The enums Qt writes inside ChartTheme, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class BackgroundShadesMode(CuteNum):
    """
    The enum 'ChartTheme::BackgroundShadesMode' of Qt, with the 4 names Qt
    gives in it.
    """

    BackgroundShadesNone = Kee[int](0)
    BackgroundShadesVertical = Kee[int](1)
    BackgroundShadesHorizontal = Kee[int](2)
    BackgroundShadesBoth = Kee[int](3)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'ChartTheme'

  #  Qt's '~ChartTheme()'. Naming it makes this a value class: Python owns
  #  every C++ ChartTheme behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN10ChartThemeD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def id(self) -> QChart.ChartTheme:
    """
    Calls Qt's 'QChart::ChartTheme ChartTheme::id() const'.

    Qt's own words: https://doc.qt.io/qt-6/charttheme.html#id

    Returns
    -------

    QChart.ChartTheme
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QChart.ChartTheme(number)' gives.
    """
    #  QChart::ChartTheme ChartTheme::id() const
    return QChart.ChartTheme(self.uglySide.call(
        'ritual_ZNK10ChartTheme2idEv',
    ))

  def seriesGradients(self) -> QList[QGradient]:
    """
    Calls Qt's 'QList<QGradient> ChartTheme::seriesGradients() const'.

    Qt's own words: https://doc.qt.io/qt-6/charttheme.html#seriesGradients

    Returns
    -------

    QList[QGradient]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QGradient> ChartTheme::seriesGradients() const
    address = self.uglySide.call('ritual_ZNK10ChartTheme15seriesGradientsEv')
    from ..QtGui import QGradient
    return QList[QGradient]._cuteOwning(address)

  def seriesColors(self) -> QList[QColor]:
    """
    Calls Qt's 'QList<QColor> ChartTheme::seriesColors() const'.

    Qt's own words: https://doc.qt.io/qt-6/charttheme.html#seriesColors

    Returns
    -------

    QList[QColor]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QColor> ChartTheme::seriesColors() const
    address = self.uglySide.call('ritual_ZNK10ChartTheme12seriesColorsEv')
    from ..QtGui import QColor
    return QList[QColor]._cuteOwning(address)

  def chartBackgroundGradient(self) -> QLinearGradient:
    """
    Calls Qt's 'QLinearGradient ChartTheme::chartBackgroundGradient() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/charttheme.html#chartBackgroundGradient

    Returns
    -------

    QLinearGradient
      A new cute QLinearGradient around the copy Qt gave back. Python owns
      it.
    """
    #  QLinearGradient ChartTheme::chartBackgroundGradient() const
    address = self.uglySide.call(
        'ritual_ZNK10ChartTheme23chartBackgroundGradientEv',
    )
    from ..QtGui import QLinearGradient
    return QLinearGradient._cuteOwning(address)

  def masterFont(self) -> QFont:
    """
    Calls Qt's 'QFont ChartTheme::masterFont() const'.

    Qt's own words: https://doc.qt.io/qt-6/charttheme.html#masterFont

    Returns
    -------

    QFont
      A new cute QFont around the copy Qt gave back. Python owns it.
    """
    #  QFont ChartTheme::masterFont() const
    address = self.uglySide.call('ritual_ZNK10ChartTheme10masterFontEv')
    from ..QtGui import QFont
    return QFont._cuteOwning(address)

  def labelFont(self) -> QFont:
    """
    Calls Qt's 'QFont ChartTheme::labelFont() const'.

    Qt's own words: https://doc.qt.io/qt-6/charttheme.html#labelFont

    Returns
    -------

    QFont
      A new cute QFont around the copy Qt gave back. Python owns it.
    """
    #  QFont ChartTheme::labelFont() const
    address = self.uglySide.call('ritual_ZNK10ChartTheme9labelFontEv')
    from ..QtGui import QFont
    return QFont._cuteOwning(address)

  def labelBrush(self) -> QBrush:
    """
    Calls Qt's 'QBrush ChartTheme::labelBrush() const'.

    Qt's own words: https://doc.qt.io/qt-6/charttheme.html#labelBrush

    Returns
    -------

    QBrush
      A new cute QBrush around the copy Qt gave back. Python owns it.
    """
    #  QBrush ChartTheme::labelBrush() const
    address = self.uglySide.call('ritual_ZNK10ChartTheme10labelBrushEv')
    from ..QtGui import QBrush
    return QBrush._cuteOwning(address)

  def axisLinePen(self) -> QPen:
    """
    Calls Qt's 'QPen ChartTheme::axisLinePen() const'.

    Qt's own words: https://doc.qt.io/qt-6/charttheme.html#axisLinePen

    Returns
    -------

    QPen
      A new cute QPen around the copy Qt gave back. Python owns it.
    """
    #  QPen ChartTheme::axisLinePen() const
    address = self.uglySide.call('ritual_ZNK10ChartTheme11axisLinePenEv')
    from ..QtGui import QPen
    return QPen._cuteOwning(address)

  def backgroundShadesPen(self) -> QPen:
    """
    Calls Qt's 'QPen ChartTheme::backgroundShadesPen() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/charttheme.html#backgroundShadesPen

    Returns
    -------

    QPen
      A new cute QPen around the copy Qt gave back. Python owns it.
    """
    #  QPen ChartTheme::backgroundShadesPen() const
    address = self.uglySide.call(
        'ritual_ZNK10ChartTheme19backgroundShadesPenEv',
    )
    from ..QtGui import QPen
    return QPen._cuteOwning(address)

  def outlinePen(self) -> QPen:
    """
    Calls Qt's 'QPen ChartTheme::outlinePen() const'.

    Qt's own words: https://doc.qt.io/qt-6/charttheme.html#outlinePen

    Returns
    -------

    QPen
      A new cute QPen around the copy Qt gave back. Python owns it.
    """
    #  QPen ChartTheme::outlinePen() const
    address = self.uglySide.call('ritual_ZNK10ChartTheme10outlinePenEv')
    from ..QtGui import QPen
    return QPen._cuteOwning(address)

  def backgroundShadesBrush(self) -> QBrush:
    """
    Calls Qt's 'QBrush ChartTheme::backgroundShadesBrush() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/charttheme.html#backgroundShadesBrush

    Returns
    -------

    QBrush
      A new cute QBrush around the copy Qt gave back. Python owns it.
    """
    #  QBrush ChartTheme::backgroundShadesBrush() const
    address = self.uglySide.call(
        'ritual_ZNK10ChartTheme21backgroundShadesBrushEv',
    )
    from ..QtGui import QBrush
    return QBrush._cuteOwning(address)

  def backgroundShades(self) -> BackgroundShadesMode:
    """
    Calls Qt's 'BackgroundShadesMode ChartTheme::backgroundShades() const'.

    Qt's own words: https://doc.qt.io/qt-6/charttheme.html#backgroundShades

    Returns
    -------

    BackgroundShadesMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'BackgroundShadesMode(number)' gives.
    """
    #  BackgroundShadesMode ChartTheme::backgroundShades() const
    return ChartTheme.BackgroundShadesMode(self.uglySide.call(
        'ritual_ZNK10ChartTheme16backgroundShadesEv',
    ))

  def isBackgroundDropShadowEnabled(self) -> bool:
    """
    Calls Qt's 'bool ChartTheme::isBackgroundDropShadowEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/charttheme.html#isBackgroundDropShadowEnabled
    """
    #  bool ChartTheme::isBackgroundDropShadowEnabled() const
    return self.uglySide.call(
        'ritual_ZNK10ChartTheme29isBackgroundDropShadowEnabledEv',
    )

  def gridLinePen(self) -> QPen:
    """
    Calls Qt's 'QPen ChartTheme::gridLinePen() const'.

    Qt's own words: https://doc.qt.io/qt-6/charttheme.html#gridLinePen

    Returns
    -------

    QPen
      A new cute QPen around the copy Qt gave back. Python owns it.
    """
    #  QPen ChartTheme::gridLinePen() const
    address = self.uglySide.call('ritual_ZNK10ChartTheme11gridLinePenEv')
    from ..QtGui import QPen
    return QPen._cuteOwning(address)

  def minorGridLinePen(self) -> QPen:
    """
    Calls Qt's 'QPen ChartTheme::minorGridLinePen() const'.

    Qt's own words: https://doc.qt.io/qt-6/charttheme.html#minorGridLinePen

    Returns
    -------

    QPen
      A new cute QPen around the copy Qt gave back. Python owns it.
    """
    #  QPen ChartTheme::minorGridLinePen() const
    address = self.uglySide.call(
        'ritual_ZNK10ChartTheme16minorGridLinePenEv',
    )
    from ..QtGui import QPen
    return QPen._cuteOwning(address)

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

  @overload()
  @overload(QChart.ChartTheme)
  def __init__(
      self,
      id: QChart.ChartTheme = QChart.ChartTheme.ChartThemeLight,
  ) -> None:
    """
    Notes what was given, for Qt's 'ChartTheme::ChartTheme(QChart::ChartTheme
    id)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/charttheme.html#ChartTheme

    Parameters
    ----------

    id : QChart.ChartTheme
      Passed on as its number. May be left out, as in Qt: it is then
      QChart.ChartTheme.ChartThemeLight.
    """
    #  ChartTheme::ChartTheme(QChart::ChartTheme id)
    self._noteCreation(ChartTheme, lambda: Rituals.call(
        'ritual_ZN10ChartThemeC1EN6QChart10ChartThemeE', id.value,
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
