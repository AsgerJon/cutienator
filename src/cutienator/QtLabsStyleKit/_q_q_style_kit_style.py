"""
QQStyleKitStyle binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekitstyle_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQStyleKitStyle to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject, QStringList
from . import QQStyleKitStyleAndThemeBase

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QFont, QPalette
  from . import QQStyleKitCustomTheme, QQStyleKitTheme
  from ..QtQml import QQmlComponent
  from ..QtQuick import QQuickPalette
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPalette = WAIT['QPalette']
  QQmlComponent = WAIT['QQmlComponent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQStyleKitStyle(QQStyleKitStyleAndThemeBase):
  """
  The cute side of Qt's QQStyleKitStyle: a plain Python object standing in
  front of one C++ QQStyleKitStyle.

  It is built on the cute 'QQStyleKitStyleAndThemeBase', as Qt's
  QQStyleKitStyle is built on Qt's QQStyleKitStyleAndThemeBase, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QQStyleKitStyle that has a ritual and that Python
  can call so far, 34 names in all: 'metaObject', 'tr', 'palette',
  'fallbackStyle', 'setFallbackStyle', 'light', 'setLight', 'dark',
  'setDark', 'customThemes', 'availableThemeNames', 'customThemeNames',
  'setThemeName', 'themeName', 'theme', 'recreateTheme', 'loaded', 'current',
  'paletteForControlType', 'fontForControlType', 'paletteChanged',
  'fallbackStyleChanged', 'lightChanged', 'darkChanged', 'themeChanged',
  'themeNameChanged', 'availableThemeNamesChanged',
  'customThemeNamesChanged', 'componentComplete', 'parseThemes',
  'reapplyStyle', 'executeFallbackStyle', 'syncFromQPalette',
  'effectivePalette'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQStyleKitStyle::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQStyleKitStyle::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QQStyleKitStyle::~QQStyleKitStyle()': the destructor: Python never
    removes a C++ QQStyleKitStyle.

  What has no ritual
  ------------------

  4 of the 42 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQStyleKitStyle is created at the first use, not by
    'QQStyleKitStyle(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQStyleKitStyle.
  - Qt tells when it has removed the C++ QQStyleKitStyle. Every call on the
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
    Calls Qt's 'QString QQStyleKitStyle::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qqstylekitstyle.html#tr

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
    #  QString QQStyleKitStyle::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN15QQStyleKitStyle2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  def current() -> Optional[QQStyleKitStyle]:
    """
    Calls Qt's 'QQStyleKitStyle *QQStyleKitStyle::current()'.

    Qt's own words: https://doc.qt.io/qt-6/qqstylekitstyle.html#current

    Returns
    -------

    Optional[QQStyleKitStyle]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQStyleKitStyle *QQStyleKitStyle::current()
    address = Rituals.call('ritual_ZN15QQStyleKitStyle7currentEv')
    return QQStyleKitStyle._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQStyleKitStyle'

  #  A C++ QQStyleKitStyle Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQStyleKitStyle'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQStyleKitStyle::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqstylekitstyle.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQStyleKitStyle::metaObject() const
    address = self.uglySide.call('ritual_ZNK15QQStyleKitStyle10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def palette(self) -> Optional[QQuickPalette]:
    """
    Calls Qt's 'QQuickPalette *QQStyleKitStyle::palette() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqstylekitstyle.html#palette

    Returns
    -------

    Optional[QQuickPalette]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickPalette *QQStyleKitStyle::palette() const
    address = self.uglySide.call('ritual_ZNK15QQStyleKitStyle7paletteEv')
    from ..QtQuick import QQuickPalette
    return QQuickPalette._cuteAt(address)

  def fallbackStyle(self) -> Optional[QQStyleKitStyle]:
    """
    Calls Qt's 'QQStyleKitStyle *QQStyleKitStyle::fallbackStyle() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqstylekitstyle.html#fallbackStyle

    Returns
    -------

    Optional[QQStyleKitStyle]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQStyleKitStyle *QQStyleKitStyle::fallbackStyle() const
    address = self.uglySide.call(
        'ritual_ZNK15QQStyleKitStyle13fallbackStyleEv',
    )
    return QQStyleKitStyle._cuteAt(address)

  def light(self) -> Optional[QQmlComponent]:
    """
    Calls Qt's 'QQmlComponent *QQStyleKitStyle::light() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqstylekitstyle.html#light

    Returns
    -------

    Optional[QQmlComponent]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlComponent *QQStyleKitStyle::light() const
    address = self.uglySide.call('ritual_ZNK15QQStyleKitStyle5lightEv')
    from ..QtQml import QQmlComponent
    return QQmlComponent._cuteAt(address)

  def dark(self) -> Optional[QQmlComponent]:
    """
    Calls Qt's 'QQmlComponent *QQStyleKitStyle::dark() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqstylekitstyle.html#dark

    Returns
    -------

    Optional[QQmlComponent]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlComponent *QQStyleKitStyle::dark() const
    address = self.uglySide.call('ritual_ZNK15QQStyleKitStyle4darkEv')
    from ..QtQml import QQmlComponent
    return QQmlComponent._cuteAt(address)

  def customThemes(self) -> QList[QQStyleKitCustomTheme]:
    """
    Calls Qt's 'QList<QQStyleKitCustomTheme *>
    QQStyleKitStyle::customThemes() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqstylekitstyle.html#customThemes

    Returns
    -------

    QList[QQStyleKitCustomTheme]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QQStyleKitCustomTheme *> QQStyleKitStyle::customThemes() const
    address = self.uglySide.call(
        'ritual_ZNK15QQStyleKitStyle12customThemesEv',
    )
    from . import QQStyleKitCustomTheme
    return QList[QQStyleKitCustomTheme]._cuteOwning(address)

  def availableThemeNames(self) -> QStringList:
    """
    Calls Qt's 'QStringList QQStyleKitStyle::availableThemeNames() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitstyle.html#availableThemeNames

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QQStyleKitStyle::availableThemeNames() const
    address = self.uglySide.call(
        'ritual_ZNK15QQStyleKitStyle19availableThemeNamesEv',
    )
    return QStringList._cuteOwning(address)

  def customThemeNames(self) -> QStringList:
    """
    Calls Qt's 'QStringList QQStyleKitStyle::customThemeNames() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitstyle.html#customThemeNames

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QQStyleKitStyle::customThemeNames() const
    address = self.uglySide.call(
        'ritual_ZNK15QQStyleKitStyle16customThemeNamesEv',
    )
    return QStringList._cuteOwning(address)

  def themeName(self) -> str:
    """
    Calls Qt's 'QString QQStyleKitStyle::themeName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqstylekitstyle.html#themeName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQStyleKitStyle::themeName() const
    return self.uglySide.call('ritual_ZNK15QQStyleKitStyle9themeNameEv')

  def theme(self) -> Optional[QQStyleKitTheme]:
    """
    Calls Qt's 'QQStyleKitTheme *QQStyleKitStyle::theme() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqstylekitstyle.html#theme

    Returns
    -------

    Optional[QQStyleKitTheme]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQStyleKitTheme *QQStyleKitStyle::theme() const
    address = self.uglySide.call('ritual_ZNK15QQStyleKitStyle5themeEv')
    from . import QQStyleKitTheme
    return QQStyleKitTheme._cuteAt(address)

  def loaded(self) -> bool:
    """
    Calls Qt's 'bool QQStyleKitStyle::loaded() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqstylekitstyle.html#loaded
    """
    #  bool QQStyleKitStyle::loaded() const
    return self.uglySide.call('ritual_ZNK15QQStyleKitStyle6loadedEv')

  @overload(int)
  def paletteForControlType(self, type: int) -> QPalette:
    """
    Calls Qt's 'QPalette
    QQStyleKitStyle::paletteForControlType(QQStyleKitExtendableControlType
    type) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitstyle.html#paletteForControlType

    Parameters
    ----------

    type : int
      Passed on as it is.

    Returns
    -------

    QPalette
      A new cute QPalette around the copy Qt gave back. Python owns it.
    """
    #  QPalette QQStyleKitStyle::paletteForControlType(
    #      QQStyleKitExtendableControlType type) const
    address = self.uglySide.call(
        'ritual_ZNK15QQStyleKitStyle21paletteForControlTypeEj', type,
    )
    from ..QtGui import QPalette
    return QPalette._cuteOwning(address)

  @overload(int)
  def fontForControlType(self, type: int) -> QFont:
    """
    Calls Qt's 'QFont
    QQStyleKitStyle::fontForControlType(QQStyleKitExtendableControlType type)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitstyle.html#fontForControlType

    Parameters
    ----------

    type : int
      Passed on as it is.

    Returns
    -------

    QFont
      A new cute QFont around the copy Qt gave back. Python owns it.
    """
    #  QFont QQStyleKitStyle::fontForControlType(
    #      QQStyleKitExtendableControlType type) const
    address = self.uglySide.call(
        'ritual_ZNK15QQStyleKitStyle18fontForControlTypeEj', type,
    )
    from ..QtGui import QFont
    return QFont._cuteOwning(address)

  def effectivePalette(self) -> QPalette:
    """
    Calls Qt's 'QPalette QQStyleKitStyle::effectivePalette() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitstyle.html#effectivePalette

    Returns
    -------

    QPalette
      A new cute QPalette around the copy Qt gave back. Python owns it.
    """
    #  QPalette QQStyleKitStyle::effectivePalette() const
    address = self.uglySide.call(
        'ritual_ZNK15QQStyleKitStyle16effectivePaletteEv',
    )
    from ..QtGui import QPalette
    return QPalette._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  @overload(NoneType)
  def setFallbackStyle(
      self,
      fallbackStyle: Optional[QQStyleKitStyle],
  ) -> None:
    """
    Calls Qt's 'void QQStyleKitStyle::setFallbackStyle(QQStyleKitStyle
    *fallbackStyle)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitstyle.html#setFallbackStyle

    Parameters
    ----------

    fallbackStyle : Optional[QQStyleKitStyle]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQStyleKitStyle::setFallbackStyle(QQStyleKitStyle *fallbackStyle)
    self.uglySide.call(
        'ritual_ZN15QQStyleKitStyle16setFallbackStyleEPS_',
        self._addressOf(fallbackStyle),
    )

  @overload(QQmlComponent)
  @overload(NoneType)
  def setLight(self, lightTheme: Optional[QQmlComponent]) -> None:
    """
    Calls Qt's 'void QQStyleKitStyle::setLight(QQmlComponent *lightTheme)'.

    Qt's own words: https://doc.qt.io/qt-6/qqstylekitstyle.html#setLight

    Parameters
    ----------

    lightTheme : Optional[QQmlComponent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQStyleKitStyle::setLight(QQmlComponent *lightTheme)
    self.uglySide.call(
        'ritual_ZN15QQStyleKitStyle8setLightEP13QQmlComponent',
        self._addressOf(lightTheme),
    )

  @overload(QQmlComponent)
  @overload(NoneType)
  def setDark(self, darkTheme: Optional[QQmlComponent]) -> None:
    """
    Calls Qt's 'void QQStyleKitStyle::setDark(QQmlComponent *darkTheme)'.

    Qt's own words: https://doc.qt.io/qt-6/qqstylekitstyle.html#setDark

    Parameters
    ----------

    darkTheme : Optional[QQmlComponent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQStyleKitStyle::setDark(QQmlComponent *darkTheme)
    self.uglySide.call(
        'ritual_ZN15QQStyleKitStyle7setDarkEP13QQmlComponent',
        self._addressOf(darkTheme),
    )

  @overload(str)
  def setThemeName(self, themeName: str) -> None:
    """
    Calls Qt's 'void QQStyleKitStyle::setThemeName(const QString
    &themeName)'.

    Qt's own words: https://doc.qt.io/qt-6/qqstylekitstyle.html#setThemeName

    Parameters
    ----------

    themeName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQStyleKitStyle::setThemeName(const QString &themeName)
    self.uglySide.call(
        'ritual_ZN15QQStyleKitStyle12setThemeNameERK7QString', themeName,
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
    Notes what was given, for Qt's 'QQStyleKitStyle::QQStyleKitStyle(QObject
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitstyle.html#QQStyleKitStyle

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQStyleKitStyle::QQStyleKitStyle(QObject *parent)
    self._noteCreation(QQStyleKitStyle, lambda: Rituals.call(
        'ritual_ZN15QQStyleKitStyleC1EP7QObject',
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

  def recreateTheme(self) -> None:
    """
    Calls Qt's 'void QQStyleKitStyle::recreateTheme()'.

    Qt's own words: https://doc.qt.io/qt-6/qqstylekitstyle.html#recreateTheme
    """
    #  void QQStyleKitStyle::recreateTheme()
    self.uglySide.call('ritual_ZN15QQStyleKitStyle13recreateThemeEv')

  def paletteChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitStyle::paletteChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitstyle.html#paletteChanged
    """
    #  void QQStyleKitStyle::paletteChanged()
    self.uglySide.call('ritual_ZN15QQStyleKitStyle14paletteChangedEv')

  def fallbackStyleChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitStyle::fallbackStyleChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitstyle.html#fallbackStyleChanged
    """
    #  void QQStyleKitStyle::fallbackStyleChanged()
    self.uglySide.call('ritual_ZN15QQStyleKitStyle20fallbackStyleChangedEv')

  def lightChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitStyle::lightChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qqstylekitstyle.html#lightChanged
    """
    #  void QQStyleKitStyle::lightChanged()
    self.uglySide.call('ritual_ZN15QQStyleKitStyle12lightChangedEv')

  def darkChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitStyle::darkChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qqstylekitstyle.html#darkChanged
    """
    #  void QQStyleKitStyle::darkChanged()
    self.uglySide.call('ritual_ZN15QQStyleKitStyle11darkChangedEv')

  def themeChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitStyle::themeChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qqstylekitstyle.html#themeChanged
    """
    #  void QQStyleKitStyle::themeChanged()
    self.uglySide.call('ritual_ZN15QQStyleKitStyle12themeChangedEv')

  def themeNameChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitStyle::themeNameChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitstyle.html#themeNameChanged
    """
    #  void QQStyleKitStyle::themeNameChanged()
    self.uglySide.call('ritual_ZN15QQStyleKitStyle16themeNameChangedEv')

  def availableThemeNamesChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitStyle::availableThemeNamesChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitstyle.html#availableThemeNamesChanged
    """
    #  void QQStyleKitStyle::availableThemeNamesChanged()
    self.uglySide.call(
        'ritual_ZN15QQStyleKitStyle26availableThemeNamesChangedEv',
    )

  def customThemeNamesChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitStyle::customThemeNamesChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitstyle.html#customThemeNamesChanged
    """
    #  void QQStyleKitStyle::customThemeNamesChanged()
    self.uglySide.call(
        'ritual_ZN15QQStyleKitStyle23customThemeNamesChangedEv',
    )

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQStyleKitStyle::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitstyle.html#componentComplete
    """
    #  void QQStyleKitStyle::componentComplete()
    ritual = 'ritual_ZN15QQStyleKitStyle17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QQStyleKitStyle17componentCompleteEv'
    self.uglySide.call(ritual)

  def parseThemes(self) -> None:
    """
    Calls Qt's 'void QQStyleKitStyle::parseThemes()'.

    Qt's own words: https://doc.qt.io/qt-6/qqstylekitstyle.html#parseThemes
    """
    #  void QQStyleKitStyle::parseThemes()
    self.uglySide.call('ritual_ZN15QQStyleKitStyle11parseThemesEv')

  def reapplyStyle(self) -> None:
    """
    Calls Qt's 'void QQStyleKitStyle::reapplyStyle()'.

    Qt's own words: https://doc.qt.io/qt-6/qqstylekitstyle.html#reapplyStyle
    """
    #  void QQStyleKitStyle::reapplyStyle()
    self.uglySide.call('ritual_ZN15QQStyleKitStyle12reapplyStyleEv')

  @overload()
  @overload(bool)
  def executeFallbackStyle(self, complete: bool = False) -> None:
    """
    Calls Qt's 'void QQStyleKitStyle::executeFallbackStyle(bool complete)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitstyle.html#executeFallbackStyle

    Parameters
    ----------

    complete : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QQStyleKitStyle::executeFallbackStyle(bool complete)
    self.uglySide.call(
        'ritual_ZN15QQStyleKitStyle20executeFallbackStyleEb', complete,
    )

  @overload(QPalette)
  def syncFromQPalette(self, palette: QPalette) -> None:
    """
    Calls Qt's 'void QQStyleKitStyle::syncFromQPalette(const QPalette
    &palette)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitstyle.html#syncFromQPalette

    Parameters
    ----------

    palette : QPalette
      Passed on as a value: Qt reads the C++ QPalette, which stays Python's
      own.
    """
    #  void QQStyleKitStyle::syncFromQPalette(const QPalette &palette)
    self.uglySide.call(
        'ritual_ZN15QQStyleKitStyle16syncFromQPaletteERK8QPalette',
        self._valueOf(palette),
    )
