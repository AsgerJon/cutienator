"""
ThemeManager binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDataVisualization/6.12.0/QtDataVisualization/private/thememanager_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means ThemeManager to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject
from . import Q3DTheme

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QColor, QFont, QLinearGradient
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']
  QFont = WAIT['QFont']
  QLinearGradient = WAIT['QLinearGradient']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class ThemeManager(QObject):
  """
  The cute side of Qt's ThemeManager: a plain Python object standing in front
  of one C++ ThemeManager.

  It is built on the cute 'QObject', as Qt's ThemeManager is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's ThemeManager that has a ritual and that Python can
  call so far, 26 names in all: 'metaObject', 'activeTheme', 'themes',
  'connectThemeSignals', 'createGradient', 'setBaseColors',
  'setBackgroundColor', 'setWindowColor', 'setTextColor',
  'setTextBackgroundColor', 'setGridLineColor', 'setSingleHighlightColor',
  'setMultiHighlightColor', 'setLightColor', 'setBaseGradients',
  'setSingleHighlightGradient', 'setMultiHighlightGradient',
  'setLightStrength', 'setAmbientLightStrength', 'setHighlightLightStrength',
  'setLabelBorderEnabled', 'setFont', 'setBackgroundEnabled',
  'setGridEnabled', 'setLabelBackgroundEnabled', 'setColorStyle'. None can be
  made from Python: one comes out of a function of another class that gives
  one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *ThemeManager::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int ThemeManager::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'ThemeManager::~ThemeManager()': the destructor: Python never
    removes a C++ ThemeManager.

  What has no ritual
  ------------------

  8 of the 37 functions Qt declares: 5 leans on 'ThemeManager; 2 not a gap; 1
  Qt's library has no name for it, and its code in Qt's source does not
  compile apart from its file.

  What to expect
  --------------

  - The C++ ThemeManager is created at the first use, not by
    'ThemeManager(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ ThemeManager.
  - Qt tells when it has removed the C++ ThemeManager. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  - Each name of Qt's ThemeManager that has no cute function yet, '__init__',
    'addTheme', 'releaseTheme', 'setActiveTheme',
    'setPredefinedPropertiesToTheme', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QColor, float)
  def createGradient(color: QColor, colorLevel: float) -> QLinearGradient:
    """
    Calls Qt's 'QLinearGradient ThemeManager::createGradient(const QColor
    &color, float colorLevel)'.

    Qt's own words: https://doc.qt.io/qt-6/thememanager.html#createGradient

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.

    colorLevel : float
      Passed on as it is.

    Returns
    -------

    QLinearGradient
      A new cute QLinearGradient around the copy Qt gave back. Python owns
      it.
    """
    #  QLinearGradient ThemeManager::createGradient(const QColor &color,
    #      float colorLevel)
    address = Rituals.call(
        'ritual_ZN12ThemeManager14createGradientERK6QColorf',
        CuteMixin._valueOf(color), colorLevel,
    )
    from ..QtGui import QLinearGradient
    return QLinearGradient._cuteOwning(address)

  @staticmethod
  @overload(Q3DTheme, QList[QColor])
  @overload(NoneType, QList[QColor])
  def setBaseColors(
      theme: Optional[Q3DTheme],
      colors: QList[QColor],
  ) -> None:
    """
    Calls Qt's 'void ThemeManager::setBaseColors(Q3DTheme *theme, const
    QList<QColor> &colors)'.

    Qt's own words: https://doc.qt.io/qt-6/thememanager.html#setBaseColors

    Parameters
    ----------

    theme : Optional[Q3DTheme]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    colors : QList[QColor]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void ThemeManager::setBaseColors(Q3DTheme *theme, const QList<QColor>
    #      &colors)
    Rituals.call(
        'ritual_ZN12ThemeManager13setBaseColorsEP8Q3DThemeRK5QListI6QColorE',
        CuteMixin._addressOf(theme), CuteMixin._valueOf(colors),
    )

  @staticmethod
  @overload(Q3DTheme, QColor)
  @overload(NoneType, QColor)
  def setBackgroundColor(theme: Optional[Q3DTheme], color: QColor) -> None:
    """
    Calls Qt's 'void ThemeManager::setBackgroundColor(Q3DTheme *theme, const
    QColor &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/thememanager.html#setBackgroundColor

    Parameters
    ----------

    theme : Optional[Q3DTheme]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void ThemeManager::setBackgroundColor(Q3DTheme *theme, const QColor
    #      &color)
    Rituals.call(
        'ritual_ZN12ThemeManager18setBackgroundColorEP8Q3DThemeRK6QColor',
        CuteMixin._addressOf(theme), CuteMixin._valueOf(color),
    )

  @staticmethod
  @overload(Q3DTheme, QColor)
  @overload(NoneType, QColor)
  def setWindowColor(theme: Optional[Q3DTheme], color: QColor) -> None:
    """
    Calls Qt's 'void ThemeManager::setWindowColor(Q3DTheme *theme, const
    QColor &color)'.

    Qt's own words: https://doc.qt.io/qt-6/thememanager.html#setWindowColor

    Parameters
    ----------

    theme : Optional[Q3DTheme]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void ThemeManager::setWindowColor(Q3DTheme *theme, const QColor
    #      &color)
    Rituals.call(
        'ritual_ZN12ThemeManager14setWindowColorEP8Q3DThemeRK6QColor',
        CuteMixin._addressOf(theme), CuteMixin._valueOf(color),
    )

  @staticmethod
  @overload(Q3DTheme, QColor)
  @overload(NoneType, QColor)
  def setTextColor(theme: Optional[Q3DTheme], color: QColor) -> None:
    """
    Calls Qt's 'void ThemeManager::setTextColor(Q3DTheme *theme, const QColor
    &color)'.

    Qt's own words: https://doc.qt.io/qt-6/thememanager.html#setTextColor

    Parameters
    ----------

    theme : Optional[Q3DTheme]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void ThemeManager::setTextColor(Q3DTheme *theme, const QColor &color)
    Rituals.call(
        'ritual_ZN12ThemeManager12setTextColorEP8Q3DThemeRK6QColor',
        CuteMixin._addressOf(theme), CuteMixin._valueOf(color),
    )

  @staticmethod
  @overload(Q3DTheme, QColor)
  @overload(NoneType, QColor)
  def setTextBackgroundColor(
      theme: Optional[Q3DTheme],
      color: QColor,
  ) -> None:
    """
    Calls Qt's 'void ThemeManager::setTextBackgroundColor(Q3DTheme *theme,
    const QColor &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/thememanager.html#setTextBackgroundColor

    Parameters
    ----------

    theme : Optional[Q3DTheme]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void ThemeManager::setTextBackgroundColor(Q3DTheme *theme, const
    #      QColor &color)
    Rituals.call(
        'ritual_ZN12ThemeManager22setTextBackgroundColorEP8Q3DThemeRK6QColo'
        'r',
        CuteMixin._addressOf(theme), CuteMixin._valueOf(color),
    )

  @staticmethod
  @overload(Q3DTheme, QColor)
  @overload(NoneType, QColor)
  def setGridLineColor(theme: Optional[Q3DTheme], color: QColor) -> None:
    """
    Calls Qt's 'void ThemeManager::setGridLineColor(Q3DTheme *theme, const
    QColor &color)'.

    Qt's own words: https://doc.qt.io/qt-6/thememanager.html#setGridLineColor

    Parameters
    ----------

    theme : Optional[Q3DTheme]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void ThemeManager::setGridLineColor(Q3DTheme *theme, const QColor
    #      &color)
    Rituals.call(
        'ritual_ZN12ThemeManager16setGridLineColorEP8Q3DThemeRK6QColor',
        CuteMixin._addressOf(theme), CuteMixin._valueOf(color),
    )

  @staticmethod
  @overload(Q3DTheme, QColor)
  @overload(NoneType, QColor)
  def setSingleHighlightColor(
      theme: Optional[Q3DTheme],
      color: QColor,
  ) -> None:
    """
    Calls Qt's 'void ThemeManager::setSingleHighlightColor(Q3DTheme *theme,
    const QColor &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/thememanager.html#setSingleHighlightColor

    Parameters
    ----------

    theme : Optional[Q3DTheme]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void ThemeManager::setSingleHighlightColor(Q3DTheme *theme, const
    #      QColor &color)
    Rituals.call(
        'ritual_ZN12ThemeManager23setSingleHighlightColorEP8Q3DThemeRK6QCol'
        'or',
        CuteMixin._addressOf(theme), CuteMixin._valueOf(color),
    )

  @staticmethod
  @overload(Q3DTheme, QColor)
  @overload(NoneType, QColor)
  def setMultiHighlightColor(
      theme: Optional[Q3DTheme],
      color: QColor,
  ) -> None:
    """
    Calls Qt's 'void ThemeManager::setMultiHighlightColor(Q3DTheme *theme,
    const QColor &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/thememanager.html#setMultiHighlightColor

    Parameters
    ----------

    theme : Optional[Q3DTheme]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void ThemeManager::setMultiHighlightColor(Q3DTheme *theme, const
    #      QColor &color)
    Rituals.call(
        'ritual_ZN12ThemeManager22setMultiHighlightColorEP8Q3DThemeRK6QColo'
        'r',
        CuteMixin._addressOf(theme), CuteMixin._valueOf(color),
    )

  @staticmethod
  @overload(Q3DTheme, QColor)
  @overload(NoneType, QColor)
  def setLightColor(theme: Optional[Q3DTheme], color: QColor) -> None:
    """
    Calls Qt's 'void ThemeManager::setLightColor(Q3DTheme *theme, const
    QColor &color)'.

    Qt's own words: https://doc.qt.io/qt-6/thememanager.html#setLightColor

    Parameters
    ----------

    theme : Optional[Q3DTheme]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void ThemeManager::setLightColor(Q3DTheme *theme, const QColor &color)
    Rituals.call(
        'ritual_ZN12ThemeManager13setLightColorEP8Q3DThemeRK6QColor',
        CuteMixin._addressOf(theme), CuteMixin._valueOf(color),
    )

  @staticmethod
  @overload(Q3DTheme, QList[QLinearGradient])
  @overload(NoneType, QList[QLinearGradient])
  def setBaseGradients(
      theme: Optional[Q3DTheme],
      gradients: QList[QLinearGradient],
  ) -> None:
    """
    Calls Qt's 'void ThemeManager::setBaseGradients(Q3DTheme *theme, const
    QList<QLinearGradient> &gradients)'.

    Qt's own words: https://doc.qt.io/qt-6/thememanager.html#setBaseGradients

    Parameters
    ----------

    theme : Optional[Q3DTheme]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    gradients : QList[QLinearGradient]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void ThemeManager::setBaseGradients(Q3DTheme *theme, const
    #      QList<QLinearGradient> &gradients)
    Rituals.call(
        'ritual_ZN12ThemeManager16setBaseGradientsEP8Q3DThemeRK5QListI15QLi'
        'nearGradientE',
        CuteMixin._addressOf(theme), CuteMixin._valueOf(gradients),
    )

  @staticmethod
  @overload(Q3DTheme, QLinearGradient)
  @overload(NoneType, QLinearGradient)
  def setSingleHighlightGradient(
      theme: Optional[Q3DTheme],
      gradient: QLinearGradient,
  ) -> None:
    """
    Calls Qt's 'void ThemeManager::setSingleHighlightGradient(Q3DTheme
    *theme, const QLinearGradient &gradient)'.

    Qt's own words:
    https://doc.qt.io/qt-6/thememanager.html#setSingleHighlightGradient

    Parameters
    ----------

    theme : Optional[Q3DTheme]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    gradient : QLinearGradient
      Passed on as a value: Qt reads the C++ QLinearGradient, which stays
      Python's own.
    """
    #  void ThemeManager::setSingleHighlightGradient(Q3DTheme *theme, const
    #      QLinearGradient &gradient)
    Rituals.call(
        'ritual_ZN12ThemeManager26setSingleHighlightGradientEP8Q3DThemeRK15'
        'QLinearGradient',
        CuteMixin._addressOf(theme), CuteMixin._valueOf(gradient),
    )

  @staticmethod
  @overload(Q3DTheme, QLinearGradient)
  @overload(NoneType, QLinearGradient)
  def setMultiHighlightGradient(
      theme: Optional[Q3DTheme],
      gradient: QLinearGradient,
  ) -> None:
    """
    Calls Qt's 'void ThemeManager::setMultiHighlightGradient(Q3DTheme *theme,
    const QLinearGradient &gradient)'.

    Qt's own words:
    https://doc.qt.io/qt-6/thememanager.html#setMultiHighlightGradient

    Parameters
    ----------

    theme : Optional[Q3DTheme]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    gradient : QLinearGradient
      Passed on as a value: Qt reads the C++ QLinearGradient, which stays
      Python's own.
    """
    #  void ThemeManager::setMultiHighlightGradient(Q3DTheme *theme, const
    #      QLinearGradient &gradient)
    Rituals.call(
        'ritual_ZN12ThemeManager25setMultiHighlightGradientEP8Q3DThemeRK15Q'
        'LinearGradient',
        CuteMixin._addressOf(theme), CuteMixin._valueOf(gradient),
    )

  @staticmethod
  @overload(Q3DTheme, float)
  @overload(NoneType, float)
  def setLightStrength(theme: Optional[Q3DTheme], strength: float) -> None:
    """
    Calls Qt's 'void ThemeManager::setLightStrength(Q3DTheme *theme, float
    strength)'.

    Qt's own words: https://doc.qt.io/qt-6/thememanager.html#setLightStrength

    Parameters
    ----------

    theme : Optional[Q3DTheme]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    strength : float
      Passed on as it is.
    """
    #  void ThemeManager::setLightStrength(Q3DTheme *theme, float strength)
    Rituals.call(
        'ritual_ZN12ThemeManager16setLightStrengthEP8Q3DThemef',
        CuteMixin._addressOf(theme), strength,
    )

  @staticmethod
  @overload(Q3DTheme, float)
  @overload(NoneType, float)
  def setAmbientLightStrength(
      theme: Optional[Q3DTheme],
      strength: float,
  ) -> None:
    """
    Calls Qt's 'void ThemeManager::setAmbientLightStrength(Q3DTheme *theme,
    float strength)'.

    Qt's own words:
    https://doc.qt.io/qt-6/thememanager.html#setAmbientLightStrength

    Parameters
    ----------

    theme : Optional[Q3DTheme]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    strength : float
      Passed on as it is.
    """
    #  void ThemeManager::setAmbientLightStrength(Q3DTheme *theme, float
    #      strength)
    Rituals.call(
        'ritual_ZN12ThemeManager23setAmbientLightStrengthEP8Q3DThemef',
        CuteMixin._addressOf(theme), strength,
    )

  @staticmethod
  @overload(Q3DTheme, float)
  @overload(NoneType, float)
  def setHighlightLightStrength(
      theme: Optional[Q3DTheme],
      strength: float,
  ) -> None:
    """
    Calls Qt's 'void ThemeManager::setHighlightLightStrength(Q3DTheme *theme,
    float strength)'.

    Qt's own words:
    https://doc.qt.io/qt-6/thememanager.html#setHighlightLightStrength

    Parameters
    ----------

    theme : Optional[Q3DTheme]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    strength : float
      Passed on as it is.
    """
    #  void ThemeManager::setHighlightLightStrength(Q3DTheme *theme, float
    #      strength)
    Rituals.call(
        'ritual_ZN12ThemeManager25setHighlightLightStrengthEP8Q3DThemef',
        CuteMixin._addressOf(theme), strength,
    )

  @staticmethod
  @overload(Q3DTheme, bool)
  @overload(NoneType, bool)
  def setLabelBorderEnabled(
      theme: Optional[Q3DTheme],
      enabled: bool,
  ) -> None:
    """
    Calls Qt's 'void ThemeManager::setLabelBorderEnabled(Q3DTheme *theme,
    bool enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/thememanager.html#setLabelBorderEnabled

    Parameters
    ----------

    theme : Optional[Q3DTheme]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    enabled : bool
      Passed on as it is.
    """
    #  void ThemeManager::setLabelBorderEnabled(Q3DTheme *theme, bool
    #      enabled)
    Rituals.call(
        'ritual_ZN12ThemeManager21setLabelBorderEnabledEP8Q3DThemeb',
        CuteMixin._addressOf(theme), enabled,
    )

  @staticmethod
  @overload(Q3DTheme, QFont)
  @overload(NoneType, QFont)
  def setFont(theme: Optional[Q3DTheme], font: QFont) -> None:
    """
    Calls Qt's 'void ThemeManager::setFont(Q3DTheme *theme, const QFont
    &font)'.

    Qt's own words: https://doc.qt.io/qt-6/thememanager.html#setFont

    Parameters
    ----------

    theme : Optional[Q3DTheme]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    font : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.
    """
    #  void ThemeManager::setFont(Q3DTheme *theme, const QFont &font)
    Rituals.call(
        'ritual_ZN12ThemeManager7setFontEP8Q3DThemeRK5QFont',
        CuteMixin._addressOf(theme), CuteMixin._valueOf(font),
    )

  @staticmethod
  @overload(Q3DTheme, bool)
  @overload(NoneType, bool)
  def setBackgroundEnabled(theme: Optional[Q3DTheme], enabled: bool) -> None:
    """
    Calls Qt's 'void ThemeManager::setBackgroundEnabled(Q3DTheme *theme, bool
    enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/thememanager.html#setBackgroundEnabled

    Parameters
    ----------

    theme : Optional[Q3DTheme]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    enabled : bool
      Passed on as it is.
    """
    #  void ThemeManager::setBackgroundEnabled(Q3DTheme *theme, bool enabled)
    Rituals.call(
        'ritual_ZN12ThemeManager20setBackgroundEnabledEP8Q3DThemeb',
        CuteMixin._addressOf(theme), enabled,
    )

  @staticmethod
  @overload(Q3DTheme, bool)
  @overload(NoneType, bool)
  def setGridEnabled(theme: Optional[Q3DTheme], enabled: bool) -> None:
    """
    Calls Qt's 'void ThemeManager::setGridEnabled(Q3DTheme *theme, bool
    enabled)'.

    Qt's own words: https://doc.qt.io/qt-6/thememanager.html#setGridEnabled

    Parameters
    ----------

    theme : Optional[Q3DTheme]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    enabled : bool
      Passed on as it is.
    """
    #  void ThemeManager::setGridEnabled(Q3DTheme *theme, bool enabled)
    Rituals.call(
        'ritual_ZN12ThemeManager14setGridEnabledEP8Q3DThemeb',
        CuteMixin._addressOf(theme), enabled,
    )

  @staticmethod
  @overload(Q3DTheme, bool)
  @overload(NoneType, bool)
  def setLabelBackgroundEnabled(
      theme: Optional[Q3DTheme],
      enabled: bool,
  ) -> None:
    """
    Calls Qt's 'void ThemeManager::setLabelBackgroundEnabled(Q3DTheme *theme,
    bool enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/thememanager.html#setLabelBackgroundEnabled

    Parameters
    ----------

    theme : Optional[Q3DTheme]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    enabled : bool
      Passed on as it is.
    """
    #  void ThemeManager::setLabelBackgroundEnabled(Q3DTheme *theme, bool
    #      enabled)
    Rituals.call(
        'ritual_ZN12ThemeManager25setLabelBackgroundEnabledEP8Q3DThemeb',
        CuteMixin._addressOf(theme), enabled,
    )

  @staticmethod
  @overload(Q3DTheme, Q3DTheme.ColorStyle)
  @overload(NoneType, Q3DTheme.ColorStyle)
  def setColorStyle(
      theme: Optional[Q3DTheme],
      style: Q3DTheme.ColorStyle,
  ) -> None:
    """
    Calls Qt's 'void ThemeManager::setColorStyle(Q3DTheme *theme,
    Q3DTheme::ColorStyle style)'.

    Qt's own words: https://doc.qt.io/qt-6/thememanager.html#setColorStyle

    Parameters
    ----------

    theme : Optional[Q3DTheme]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    style : Q3DTheme.ColorStyle
      Passed on as its number.
    """
    #  void ThemeManager::setColorStyle(Q3DTheme *theme, Q3DTheme::ColorStyle
    #      style)
    Rituals.call(
        'ritual_ZN12ThemeManager13setColorStyleEP8Q3DThemeNS0_10ColorStyleE',
        CuteMixin._addressOf(theme), style.value,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'ThemeManager'

  #  A C++ ThemeManager Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_ThemeManager'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *ThemeManager::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/thememanager.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *ThemeManager::metaObject() const
    address = self.uglySide.call('ritual_ZNK12ThemeManager10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def activeTheme(self) -> Optional[Q3DTheme]:
    """
    Calls Qt's 'Q3DTheme *ThemeManager::activeTheme() const'.

    Qt's own words: https://doc.qt.io/qt-6/thememanager.html#activeTheme

    Returns
    -------

    Optional[Q3DTheme]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Q3DTheme *ThemeManager::activeTheme() const
    address = self.uglySide.call('ritual_ZNK12ThemeManager11activeThemeEv')
    return Q3DTheme._cuteAt(address)

  def themes(self) -> QList[Q3DTheme]:
    """
    Calls Qt's 'QList<Q3DTheme *> ThemeManager::themes() const'.

    Qt's own words: https://doc.qt.io/qt-6/thememanager.html#themes

    Returns
    -------

    QList[Q3DTheme]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<Q3DTheme *> ThemeManager::themes() const
    address = self.uglySide.call('ritual_ZNK12ThemeManager6themesEv')
    return QList[Q3DTheme]._cuteOwning(address)

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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'ThemeManager::ThemeManager(Abstract3DController *controller)':
    leans on 'ThemeManager::qt_metacall(QMetaObject::Call, int, void**)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'ThemeManager.__init__' has no cute function yet. Qt's "
        "'ThemeManager::ThemeManager(Abstract3DController *controller)': "
        "leans on 'ThemeManager::qt_metacall(QMetaObject::Call, int, "
        "void**)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

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

  def connectThemeSignals(self) -> None:
    """
    Calls Qt's 'void ThemeManager::connectThemeSignals()'.

    Qt's own words:
    https://doc.qt.io/qt-6/thememanager.html#connectThemeSignals
    """
    #  void ThemeManager::connectThemeSignals()
    self.uglySide.call('ritual_ZN12ThemeManager19connectThemeSignalsEv')

  @staticmethod
  def addTheme(*__, **_) -> Never:
    """
    Qt's 'void ThemeManager::addTheme(Q3DTheme *theme)': leans on
    'ThemeManager::staticMetaObject', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'ThemeManager.addTheme' has no cute function yet. Qt's 'void "
        "ThemeManager::addTheme(Q3DTheme *theme)': leans on "
        "'ThemeManager::staticMetaObject', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def releaseTheme(*__, **_) -> Never:
    """
    Qt's 'void ThemeManager::releaseTheme(Q3DTheme *theme)': leans on
    'ThemeManager::staticMetaObject', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'ThemeManager.releaseTheme' has no cute function yet. Qt's 'void "
        "ThemeManager::releaseTheme(Q3DTheme *theme)': leans on "
        "'ThemeManager::staticMetaObject', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def setActiveTheme(*__, **_) -> Never:
    """
    Qt's 'void ThemeManager::setActiveTheme(Q3DTheme *theme)': leans on
    'ThemeManager::staticMetaObject', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'ThemeManager.setActiveTheme' has no cute function yet. Qt's 'void "
        "ThemeManager::setActiveTheme(Q3DTheme *theme)': leans on "
        "'ThemeManager::staticMetaObject', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def setPredefinedPropertiesToTheme(*__, **_) -> Never:
    """
    Qt's 'void ThemeManager::setPredefinedPropertiesToTheme(Q3DTheme *theme,
    Q3DTheme::Theme type)': Qt's library has no name for it, and its code in
    Qt's source does not compile apart from its file: use of undeclared
    identifier 'defaultColorLevel'.
    """
    raise NotImplementedError(
        "'ThemeManager.setPredefinedPropertiesToTheme' has no cute function "
        "yet. Qt's 'void "
        "ThemeManager::setPredefinedPropertiesToTheme(Q3DTheme *theme, "
        "Q3DTheme::Theme type)': Qt's library has no name for it, and its "
        "code in Qt's source does not compile apart from its file: use of "
        "undeclared identifier 'defaultColorLevel'.")
