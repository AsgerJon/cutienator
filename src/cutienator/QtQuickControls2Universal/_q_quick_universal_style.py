"""
QQuickUniversalStyle binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickControls2Universal/6.12.0/QtQuickControls2Universal/private/qquickuniversalstyle_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickUniversalStyle to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QObject, QVariant
  from ..QtGui import QColor
  from ..QtQuickControls2 import QQuickAttachedPropertyPropagator
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QObject = WAIT['QObject']
  QQuickAttachedPropertyPropagator = WAIT['QQuickAttachedPropertyPropagator']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickUniversalStyle(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuickUniversalStyle: a plain Python object standing
  in front of one C++ QQuickUniversalStyle.

  What exists
  -----------

  Every function of Qt's QQuickUniversalStyle that has a ritual and that
  Python can call so far, 56 names in all: 'metaObject', 'tr',
  'qmlAttachedProperties', 'theme', 'setTheme', 'inheritTheme',
  'propagateTheme', 'resetTheme', 'accent', 'setAccent', 'inheritAccent',
  'propagateAccent', 'resetAccent', 'foreground', 'setForeground',
  'inheritForeground', 'propagateForeground', 'resetForeground',
  'background', 'setBackground', 'inheritBackground', 'propagateBackground',
  'resetBackground', 'color', 'altHighColor', 'altLowColor',
  'altMediumColor', 'altMediumHighColor', 'altMediumLowColor',
  'baseHighColor', 'baseLowColor', 'baseMediumColor', 'baseMediumHighColor',
  'baseMediumLowColor', 'chromeAltLowColor', 'chromeBlackHighColor',
  'chromeBlackLowColor', 'chromeBlackMediumLowColor',
  'chromeBlackMediumColor', 'chromeDisabledHighColor',
  'chromeDisabledLowColor', 'chromeHighColor', 'chromeLowColor',
  'chromeMediumColor', 'chromeMediumLowColor', 'chromeWhiteColor',
  'listLowColor', 'listMediumColor', 'systemColor', 'initGlobals',
  'themeChanged', 'accentChanged', 'foregroundChanged', 'backgroundChanged',
  'paletteChanged', 'attachedParentChange'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickUniversalStyle::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuickUniversalStyle::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuickUniversalStyle::qt_qmlMarker_attached()': one of Qt's
    own inner workings.
  - Qt's 'void QQuickUniversalStyle::qt_qmlMarker_uncreatable()': one of Qt's
    own inner workings.
  - Qt's 'bool QQuickUniversalStyle::variantToRgba(const QVariant &var, const
    char *name, QRgb *rgba) const': takes a number to change where it is.

  What has no ritual
  ------------------

  2 of the 64 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickUniversalStyle is created at the first use, not by
    'QQuickUniversalStyle(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickUniversalStyle.
  - Qt tells when it has removed the C++ QQuickUniversalStyle. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickUniversalStyle that has no cute function yet,
    'variantToRgba', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  #  The enums Qt writes inside QQuickUniversalStyle, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class Color(CuteNum):
    """
    The enum 'QQuickUniversalStyle::Color' of Qt, with the 20 names Qt gives
    in it.
    """

    Lime = Kee[int](0)
    Green = Kee[int](1)
    Emerald = Kee[int](2)
    Teal = Kee[int](3)
    Cyan = Kee[int](4)
    Cobalt = Kee[int](5)
    Indigo = Kee[int](6)
    Violet = Kee[int](7)
    Pink = Kee[int](8)
    Magenta = Kee[int](9)
    Crimson = Kee[int](10)
    Red = Kee[int](11)
    Orange = Kee[int](12)
    Amber = Kee[int](13)
    Yellow = Kee[int](14)
    Brown = Kee[int](15)
    Olive = Kee[int](16)
    Steel = Kee[int](17)
    Mauve = Kee[int](18)
    Taupe = Kee[int](19)

  class SystemColor(CuteNum):
    """
    The enum 'QQuickUniversalStyle::SystemColor' of Qt, with the 24 names Qt
    gives in it.
    """

    AltHigh = Kee[int](0)
    AltLow = Kee[int](1)
    AltMedium = Kee[int](2)
    AltMediumHigh = Kee[int](3)
    AltMediumLow = Kee[int](4)
    BaseHigh = Kee[int](5)
    BaseLow = Kee[int](6)
    BaseMedium = Kee[int](7)
    BaseMediumHigh = Kee[int](8)
    BaseMediumLow = Kee[int](9)
    ChromeAltLow = Kee[int](10)
    ChromeBlackHigh = Kee[int](11)
    ChromeBlackLow = Kee[int](12)
    ChromeBlackMediumLow = Kee[int](13)
    ChromeBlackMedium = Kee[int](14)
    ChromeDisabledHigh = Kee[int](15)
    ChromeDisabledLow = Kee[int](16)
    ChromeHigh = Kee[int](17)
    ChromeLow = Kee[int](18)
    ChromeMedium = Kee[int](19)
    ChromeMediumLow = Kee[int](20)
    ChromeWhite = Kee[int](21)
    ListLow = Kee[int](22)
    ListMedium = Kee[int](23)

  class Theme(CuteNum):
    """
    The enum 'QQuickUniversalStyle::Theme' of Qt, with the 3 names Qt gives
    in it.
    """

    Light = Kee[int](0)
    Dark = Kee[int](1)
    System = Kee[int](2)

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
    Calls Qt's 'QString QQuickUniversalStyle::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickuniversalstyle.html#tr

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
    #  QString QQuickUniversalStyle::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN20QQuickUniversalStyle2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(QObject)
  @overload(NoneType)
  def qmlAttachedProperties(
      object: Optional[QObject],
  ) -> Optional[QQuickUniversalStyle]:
    """
    Calls Qt's 'QQuickUniversalStyle
    *QQuickUniversalStyle::qmlAttachedProperties(QObject *object)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickuniversalstyle.html#qmlAttachedProperties

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQuickUniversalStyle]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickUniversalStyle
    #      *QQuickUniversalStyle::qmlAttachedProperties(QObject *object)
    address = Rituals.call(
        'ritual_ZN20QQuickUniversalStyle21qmlAttachedPropertiesEP7QObject',
        CuteMixin._addressOf(object, 'QObject'),
    )
    return QQuickUniversalStyle._cuteAt(address)

  @staticmethod
  def initGlobals() -> None:
    """
    Calls Qt's 'void QQuickUniversalStyle::initGlobals()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickuniversalstyle.html#initGlobals
    """
    #  void QQuickUniversalStyle::initGlobals()
    Rituals.call('ritual_ZN20QQuickUniversalStyle11initGlobalsEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickUniversalStyle'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickUniversalStyle::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickuniversalstyle.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickUniversalStyle::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK20QQuickUniversalStyle10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def theme(self) -> Theme:
    """
    Calls Qt's 'Theme QQuickUniversalStyle::theme() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickuniversalstyle.html#theme

    Returns
    -------

    Theme
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Theme(number)' gives.
    """
    #  Theme QQuickUniversalStyle::theme() const
    return QQuickUniversalStyle.Theme(self.uglySide.call(
        'ritual_ZNK20QQuickUniversalStyle5themeEv',
    ))

  def accent(self) -> QVariant:
    """
    Calls Qt's 'QVariant QQuickUniversalStyle::accent() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickuniversalstyle.html#accent

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QQuickUniversalStyle::accent() const
    address = self.uglySide.call('ritual_ZNK20QQuickUniversalStyle6accentEv')
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def foreground(self) -> QVariant:
    """
    Calls Qt's 'QVariant QQuickUniversalStyle::foreground() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickuniversalstyle.html#foreground

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QQuickUniversalStyle::foreground() const
    address = self.uglySide.call(
        'ritual_ZNK20QQuickUniversalStyle10foregroundEv',
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def background(self) -> QVariant:
    """
    Calls Qt's 'QVariant QQuickUniversalStyle::background() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickuniversalstyle.html#background

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QQuickUniversalStyle::background() const
    address = self.uglySide.call(
        'ritual_ZNK20QQuickUniversalStyle10backgroundEv',
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(Color)
  def color(self, color: Color) -> QColor:
    """
    Calls Qt's 'QColor QQuickUniversalStyle::color(Color color) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickuniversalstyle.html#color

    Parameters
    ----------

    color : Color
      Passed on as its number.

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickUniversalStyle::color(Color color) const
    address = self.uglySide.call(
        'ritual_ZNK20QQuickUniversalStyle5colorENS_5ColorE', color.value,
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def altHighColor(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickUniversalStyle::altHighColor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickuniversalstyle.html#altHighColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickUniversalStyle::altHighColor() const
    address = self.uglySide.call(
        'ritual_ZNK20QQuickUniversalStyle12altHighColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def altLowColor(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickUniversalStyle::altLowColor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickuniversalstyle.html#altLowColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickUniversalStyle::altLowColor() const
    address = self.uglySide.call(
        'ritual_ZNK20QQuickUniversalStyle11altLowColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def altMediumColor(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickUniversalStyle::altMediumColor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickuniversalstyle.html#altMediumColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickUniversalStyle::altMediumColor() const
    address = self.uglySide.call(
        'ritual_ZNK20QQuickUniversalStyle14altMediumColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def altMediumHighColor(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickUniversalStyle::altMediumHighColor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickuniversalstyle.html#altMediumHighColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickUniversalStyle::altMediumHighColor() const
    address = self.uglySide.call(
        'ritual_ZNK20QQuickUniversalStyle18altMediumHighColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def altMediumLowColor(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickUniversalStyle::altMediumLowColor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickuniversalstyle.html#altMediumLowColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickUniversalStyle::altMediumLowColor() const
    address = self.uglySide.call(
        'ritual_ZNK20QQuickUniversalStyle17altMediumLowColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def baseHighColor(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickUniversalStyle::baseHighColor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickuniversalstyle.html#baseHighColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickUniversalStyle::baseHighColor() const
    address = self.uglySide.call(
        'ritual_ZNK20QQuickUniversalStyle13baseHighColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def baseLowColor(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickUniversalStyle::baseLowColor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickuniversalstyle.html#baseLowColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickUniversalStyle::baseLowColor() const
    address = self.uglySide.call(
        'ritual_ZNK20QQuickUniversalStyle12baseLowColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def baseMediumColor(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickUniversalStyle::baseMediumColor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickuniversalstyle.html#baseMediumColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickUniversalStyle::baseMediumColor() const
    address = self.uglySide.call(
        'ritual_ZNK20QQuickUniversalStyle15baseMediumColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def baseMediumHighColor(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickUniversalStyle::baseMediumHighColor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickuniversalstyle.html#baseMediumHighColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickUniversalStyle::baseMediumHighColor() const
    address = self.uglySide.call(
        'ritual_ZNK20QQuickUniversalStyle19baseMediumHighColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def baseMediumLowColor(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickUniversalStyle::baseMediumLowColor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickuniversalstyle.html#baseMediumLowColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickUniversalStyle::baseMediumLowColor() const
    address = self.uglySide.call(
        'ritual_ZNK20QQuickUniversalStyle18baseMediumLowColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def chromeAltLowColor(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickUniversalStyle::chromeAltLowColor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickuniversalstyle.html#chromeAltLowColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickUniversalStyle::chromeAltLowColor() const
    address = self.uglySide.call(
        'ritual_ZNK20QQuickUniversalStyle17chromeAltLowColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def chromeBlackHighColor(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickUniversalStyle::chromeBlackHighColor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickuniversalstyle.html#chromeBlackHighColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickUniversalStyle::chromeBlackHighColor() const
    address = self.uglySide.call(
        'ritual_ZNK20QQuickUniversalStyle20chromeBlackHighColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def chromeBlackLowColor(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickUniversalStyle::chromeBlackLowColor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickuniversalstyle.html#chromeBlackLowColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickUniversalStyle::chromeBlackLowColor() const
    address = self.uglySide.call(
        'ritual_ZNK20QQuickUniversalStyle19chromeBlackLowColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def chromeBlackMediumLowColor(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickUniversalStyle::chromeBlackMediumLowColor()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickuniversalstyle.html

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickUniversalStyle::chromeBlackMediumLowColor() const
    address = self.uglySide.call(
        'ritual_ZNK20QQuickUniversalStyle25chromeBlackMediumLowColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def chromeBlackMediumColor(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickUniversalStyle::chromeBlackMediumColor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickuniversalstyle.html#chromeBlackMediumColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickUniversalStyle::chromeBlackMediumColor() const
    address = self.uglySide.call(
        'ritual_ZNK20QQuickUniversalStyle22chromeBlackMediumColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def chromeDisabledHighColor(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickUniversalStyle::chromeDisabledHighColor()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickuniversalstyle.html#chromeDisabledHighColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickUniversalStyle::chromeDisabledHighColor() const
    address = self.uglySide.call(
        'ritual_ZNK20QQuickUniversalStyle23chromeDisabledHighColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def chromeDisabledLowColor(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickUniversalStyle::chromeDisabledLowColor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickuniversalstyle.html#chromeDisabledLowColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickUniversalStyle::chromeDisabledLowColor() const
    address = self.uglySide.call(
        'ritual_ZNK20QQuickUniversalStyle22chromeDisabledLowColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def chromeHighColor(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickUniversalStyle::chromeHighColor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickuniversalstyle.html#chromeHighColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickUniversalStyle::chromeHighColor() const
    address = self.uglySide.call(
        'ritual_ZNK20QQuickUniversalStyle15chromeHighColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def chromeLowColor(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickUniversalStyle::chromeLowColor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickuniversalstyle.html#chromeLowColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickUniversalStyle::chromeLowColor() const
    address = self.uglySide.call(
        'ritual_ZNK20QQuickUniversalStyle14chromeLowColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def chromeMediumColor(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickUniversalStyle::chromeMediumColor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickuniversalstyle.html#chromeMediumColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickUniversalStyle::chromeMediumColor() const
    address = self.uglySide.call(
        'ritual_ZNK20QQuickUniversalStyle17chromeMediumColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def chromeMediumLowColor(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickUniversalStyle::chromeMediumLowColor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickuniversalstyle.html#chromeMediumLowColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickUniversalStyle::chromeMediumLowColor() const
    address = self.uglySide.call(
        'ritual_ZNK20QQuickUniversalStyle20chromeMediumLowColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def chromeWhiteColor(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickUniversalStyle::chromeWhiteColor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickuniversalstyle.html#chromeWhiteColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickUniversalStyle::chromeWhiteColor() const
    address = self.uglySide.call(
        'ritual_ZNK20QQuickUniversalStyle16chromeWhiteColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def listLowColor(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickUniversalStyle::listLowColor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickuniversalstyle.html#listLowColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickUniversalStyle::listLowColor() const
    address = self.uglySide.call(
        'ritual_ZNK20QQuickUniversalStyle12listLowColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def listMediumColor(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickUniversalStyle::listMediumColor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickuniversalstyle.html#listMediumColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickUniversalStyle::listMediumColor() const
    address = self.uglySide.call(
        'ritual_ZNK20QQuickUniversalStyle15listMediumColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  @overload(SystemColor)
  def systemColor(self, role: SystemColor) -> QColor:
    """
    Calls Qt's 'QColor QQuickUniversalStyle::systemColor(SystemColor role)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickuniversalstyle.html#systemColor

    Parameters
    ----------

    role : SystemColor
      Passed on as its number.

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickUniversalStyle::systemColor(SystemColor role) const
    address = self.uglySide.call(
        'ritual_ZNK20QQuickUniversalStyle11systemColorENS_11SystemColorE',
        role.value,
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Theme)
  def setTheme(self, theme: Theme) -> None:
    """
    Calls Qt's 'void QQuickUniversalStyle::setTheme(Theme theme)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickuniversalstyle.html#setTheme

    Parameters
    ----------

    theme : Theme
      Passed on as its number.
    """
    #  void QQuickUniversalStyle::setTheme(Theme theme)
    self.uglySide.call(
        'ritual_ZN20QQuickUniversalStyle8setThemeENS_5ThemeE', theme.value,
    )

  @overload(QVariant)
  def setAccent(self, accent: QVariant) -> None:
    """
    Calls Qt's 'void QQuickUniversalStyle::setAccent(const QVariant
    &accent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickuniversalstyle.html#setAccent

    Parameters
    ----------

    accent : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QQuickUniversalStyle::setAccent(const QVariant &accent)
    self.uglySide.call(
        'ritual_ZN20QQuickUniversalStyle9setAccentERK8QVariant',
        self._valueOf(accent),
    )

  @overload(QVariant)
  def setForeground(self, foreground: QVariant) -> None:
    """
    Calls Qt's 'void QQuickUniversalStyle::setForeground(const QVariant
    &foreground)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickuniversalstyle.html#setForeground

    Parameters
    ----------

    foreground : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QQuickUniversalStyle::setForeground(const QVariant &foreground)
    self.uglySide.call(
        'ritual_ZN20QQuickUniversalStyle13setForegroundERK8QVariant',
        self._valueOf(foreground),
    )

  @overload(QVariant)
  def setBackground(self, background: QVariant) -> None:
    """
    Calls Qt's 'void QQuickUniversalStyle::setBackground(const QVariant
    &background)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickuniversalstyle.html#setBackground

    Parameters
    ----------

    background : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QQuickUniversalStyle::setBackground(const QVariant &background)
    self.uglySide.call(
        'ritual_ZN20QQuickUniversalStyle13setBackgroundERK8QVariant',
        self._valueOf(background),
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

  @overload()
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QQuickUniversalStyle::QQuickUniversalStyle(QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickuniversalstyle.html#QQuickUniversalStyle

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickUniversalStyle::QQuickUniversalStyle(QObject *parent)
    self._noteCreation(QQuickUniversalStyle, lambda: Rituals.call(
        'ritual_ZN20QQuickUniversalStyleC1EP7QObject',
        self._addressOf(parent, 'QObject'),
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

  @overload(Theme)
  def inheritTheme(self, theme: Theme) -> None:
    """
    Calls Qt's 'void QQuickUniversalStyle::inheritTheme(Theme theme)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickuniversalstyle.html#inheritTheme

    Parameters
    ----------

    theme : Theme
      Passed on as its number.
    """
    #  void QQuickUniversalStyle::inheritTheme(Theme theme)
    self.uglySide.call(
        'ritual_ZN20QQuickUniversalStyle12inheritThemeENS_5ThemeE',
        theme.value,
    )

  def propagateTheme(self) -> None:
    """
    Calls Qt's 'void QQuickUniversalStyle::propagateTheme()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickuniversalstyle.html#propagateTheme
    """
    #  void QQuickUniversalStyle::propagateTheme()
    self.uglySide.call('ritual_ZN20QQuickUniversalStyle14propagateThemeEv')

  def resetTheme(self) -> None:
    """
    Calls Qt's 'void QQuickUniversalStyle::resetTheme()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickuniversalstyle.html#resetTheme
    """
    #  void QQuickUniversalStyle::resetTheme()
    self.uglySide.call('ritual_ZN20QQuickUniversalStyle10resetThemeEv')

  @overload(int)
  def inheritAccent(self, accent: int) -> None:
    """
    Calls Qt's 'void QQuickUniversalStyle::inheritAccent(QRgb accent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickuniversalstyle.html#inheritAccent

    Parameters
    ----------

    accent : int
      Passed on as it is.
    """
    #  void QQuickUniversalStyle::inheritAccent(QRgb accent)
    self.uglySide.call(
        'ritual_ZN20QQuickUniversalStyle13inheritAccentEj', accent,
    )

  def propagateAccent(self) -> None:
    """
    Calls Qt's 'void QQuickUniversalStyle::propagateAccent()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickuniversalstyle.html#propagateAccent
    """
    #  void QQuickUniversalStyle::propagateAccent()
    self.uglySide.call('ritual_ZN20QQuickUniversalStyle15propagateAccentEv')

  def resetAccent(self) -> None:
    """
    Calls Qt's 'void QQuickUniversalStyle::resetAccent()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickuniversalstyle.html#resetAccent
    """
    #  void QQuickUniversalStyle::resetAccent()
    self.uglySide.call('ritual_ZN20QQuickUniversalStyle11resetAccentEv')

  @overload(int, bool)
  def inheritForeground(self, foreground: int, has: bool) -> None:
    """
    Calls Qt's 'void QQuickUniversalStyle::inheritForeground(QRgb foreground,
    bool has)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickuniversalstyle.html#inheritForeground

    Parameters
    ----------

    foreground : int
      Passed on as it is.

    has : bool
      Passed on as it is.
    """
    #  void QQuickUniversalStyle::inheritForeground(QRgb foreground, bool
    #      has)
    self.uglySide.call(
        'ritual_ZN20QQuickUniversalStyle17inheritForegroundEjb',
        foreground, has,
    )

  def propagateForeground(self) -> None:
    """
    Calls Qt's 'void QQuickUniversalStyle::propagateForeground()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickuniversalstyle.html#propagateForeground
    """
    #  void QQuickUniversalStyle::propagateForeground()
    self.uglySide.call(
        'ritual_ZN20QQuickUniversalStyle19propagateForegroundEv',
    )

  def resetForeground(self) -> None:
    """
    Calls Qt's 'void QQuickUniversalStyle::resetForeground()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickuniversalstyle.html#resetForeground
    """
    #  void QQuickUniversalStyle::resetForeground()
    self.uglySide.call('ritual_ZN20QQuickUniversalStyle15resetForegroundEv')

  @overload(int, bool)
  def inheritBackground(self, background: int, has: bool) -> None:
    """
    Calls Qt's 'void QQuickUniversalStyle::inheritBackground(QRgb background,
    bool has)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickuniversalstyle.html#inheritBackground

    Parameters
    ----------

    background : int
      Passed on as it is.

    has : bool
      Passed on as it is.
    """
    #  void QQuickUniversalStyle::inheritBackground(QRgb background, bool
    #      has)
    self.uglySide.call(
        'ritual_ZN20QQuickUniversalStyle17inheritBackgroundEjb',
        background, has,
    )

  def propagateBackground(self) -> None:
    """
    Calls Qt's 'void QQuickUniversalStyle::propagateBackground()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickuniversalstyle.html#propagateBackground
    """
    #  void QQuickUniversalStyle::propagateBackground()
    self.uglySide.call(
        'ritual_ZN20QQuickUniversalStyle19propagateBackgroundEv',
    )

  def resetBackground(self) -> None:
    """
    Calls Qt's 'void QQuickUniversalStyle::resetBackground()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickuniversalstyle.html#resetBackground
    """
    #  void QQuickUniversalStyle::resetBackground()
    self.uglySide.call('ritual_ZN20QQuickUniversalStyle15resetBackgroundEv')

  def themeChanged(self) -> None:
    """
    Calls Qt's 'void QQuickUniversalStyle::themeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickuniversalstyle.html#themeChanged
    """
    #  void QQuickUniversalStyle::themeChanged()
    self.uglySide.call('ritual_ZN20QQuickUniversalStyle12themeChangedEv')

  def accentChanged(self) -> None:
    """
    Calls Qt's 'void QQuickUniversalStyle::accentChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickuniversalstyle.html#accentChanged
    """
    #  void QQuickUniversalStyle::accentChanged()
    self.uglySide.call('ritual_ZN20QQuickUniversalStyle13accentChangedEv')

  def foregroundChanged(self) -> None:
    """
    Calls Qt's 'void QQuickUniversalStyle::foregroundChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickuniversalstyle.html#foregroundChanged
    """
    #  void QQuickUniversalStyle::foregroundChanged()
    self.uglySide.call(
        'ritual_ZN20QQuickUniversalStyle17foregroundChangedEv',
    )

  def backgroundChanged(self) -> None:
    """
    Calls Qt's 'void QQuickUniversalStyle::backgroundChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickuniversalstyle.html#backgroundChanged
    """
    #  void QQuickUniversalStyle::backgroundChanged()
    self.uglySide.call(
        'ritual_ZN20QQuickUniversalStyle17backgroundChangedEv',
    )

  def paletteChanged(self) -> None:
    """
    Calls Qt's 'void QQuickUniversalStyle::paletteChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickuniversalstyle.html#paletteChanged
    """
    #  void QQuickUniversalStyle::paletteChanged()
    self.uglySide.call('ritual_ZN20QQuickUniversalStyle14paletteChangedEv')

  @overload(
      QQuickAttachedPropertyPropagator, QQuickAttachedPropertyPropagator,
  )
  @overload(QQuickAttachedPropertyPropagator, NoneType)
  @overload(NoneType, QQuickAttachedPropertyPropagator)
  @overload(NoneType, NoneType)
  def attachedParentChange(
      self,
      newParent: Optional[QQuickAttachedPropertyPropagator],
      oldParent: Optional[QQuickAttachedPropertyPropagator],
  ) -> None:
    """
    Calls Qt's 'void QQuickUniversalStyle::attachedParentChange(
    QQuickAttachedPropertyPropagator *newParent,
    QQuickAttachedPropertyPropagator *oldParent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickuniversalstyle.html#attachedParentChange

    Parameters
    ----------

    newParent : Optional[QQuickAttachedPropertyPropagator]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    oldParent : Optional[QQuickAttachedPropertyPropagator]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickUniversalStyle::attachedParentChange(
    #      QQuickAttachedPropertyPropagator *newParent,
    #      QQuickAttachedPropertyPropagator *oldParent)
    ritual = (
        'ritual_ZN20QQuickUniversalStyle20attachedParentChangeEP32QQuickAtt'
        'achedPropertyPropagatorS1_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QQuickUniversalStyle20attachedParentChangeEP32QQu'
          'ickAttachedPropertyPropagatorS1_')
    self.uglySide.call(
        ritual, self._addressOf(newParent), self._addressOf(oldParent),
    )

  @staticmethod
  def variantToRgba(*__, **_) -> Never:
    """
    Qt's 'bool QQuickUniversalStyle::variantToRgba(const QVariant &var, const
    char *name, QRgb *rgba) const': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QQuickUniversalStyle.variantToRgba' has no cute function yet. "
        "Qt's 'bool QQuickUniversalStyle::variantToRgba(const QVariant "
        "&var, const char *name, QRgb *rgba) const': takes a number to "
        "change where it is.")
