"""
QGenericUnixTheme binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qgenericunixtheme_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QGenericUnixTheme to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList, QStringList
from . import QPlatformTheme

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QFileInfo, QSize, QVariant
  from . import QFont, QGenericUnixThemePrivate, QIcon, QPlatformMenuBar
  from . import QPlatformSystemTrayIcon
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QFileInfo = WAIT['QFileInfo']
  QGenericUnixThemePrivate = WAIT['QGenericUnixThemePrivate']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QGenericUnixTheme(QPlatformTheme):
  """
  The cute side of Qt's QGenericUnixTheme: a plain Python object standing in
  front of one C++ QGenericUnixTheme.

  It is built on the cute 'QPlatformTheme', as Qt's QGenericUnixTheme is
  built on Qt's QPlatformTheme, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QGenericUnixTheme that has a ritual and that Python
  can call so far, 15 names in all: 'd_func', 'font', 'themeHint',
  'createPlatformMenuBar', 'createPlatformSystemTrayIcon',
  'xdgIconThemePaths', 'createUnixTheme', 'themeNames', 'iconFallbackPaths',
  'isDBusGlobalMenuAvailable', 'mouseCursorTheme', 'mouseCursorSize',
  'availableXdgFileIconSizes', 'shouldUseDBusTray', 'xdgFileIcon'. It can be
  made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QGenericUnixThemePrivate *QGenericUnixTheme::d_func() const':
    takes in Python what 'QGenericUnixThemePrivate
    *QGenericUnixTheme::d_func()' takes.

  What to expect
  --------------

  - The C++ QGenericUnixTheme is created at the first use, not by
    'QGenericUnixTheme(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGenericUnixTheme.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def xdgIconThemePaths() -> QStringList:
    """
    Calls Qt's 'QStringList QGenericUnixTheme::xdgIconThemePaths()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgenericunixtheme.html#xdgIconThemePaths

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QGenericUnixTheme::xdgIconThemePaths()
    address = Rituals.call(
        'ritual_ZN17QGenericUnixTheme17xdgIconThemePathsEv',
    )
    return QStringList._cuteOwning(address)

  @staticmethod
  @overload(str)
  def createUnixTheme(name: str) -> Optional[QPlatformTheme]:
    """
    Calls Qt's 'QPlatformTheme *QGenericUnixTheme::createUnixTheme(const
    QString &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgenericunixtheme.html#createUnixTheme

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    Optional[QPlatformTheme]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlatformTheme *QGenericUnixTheme::createUnixTheme(const QString
    #      &name)
    address = Rituals.call(
        'ritual_ZN17QGenericUnixTheme15createUnixThemeERK7QString', name,
    )
    return QPlatformTheme._cuteAt(address)

  @staticmethod
  def themeNames() -> QStringList:
    """
    Calls Qt's 'QStringList QGenericUnixTheme::themeNames()'.

    Qt's own words: https://doc.qt.io/qt-6/qgenericunixtheme.html#themeNames

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QGenericUnixTheme::themeNames()
    address = Rituals.call('ritual_ZN17QGenericUnixTheme10themeNamesEv')
    return QStringList._cuteOwning(address)

  @staticmethod
  def iconFallbackPaths() -> QStringList:
    """
    Calls Qt's 'QStringList QGenericUnixTheme::iconFallbackPaths()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgenericunixtheme.html#iconFallbackPaths

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QGenericUnixTheme::iconFallbackPaths()
    address = Rituals.call(
        'ritual_ZN17QGenericUnixTheme17iconFallbackPathsEv',
    )
    return QStringList._cuteOwning(address)

  @staticmethod
  def isDBusGlobalMenuAvailable() -> bool:
    """
    Calls Qt's 'bool QGenericUnixTheme::isDBusGlobalMenuAvailable()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgenericunixtheme.html#isDBusGlobalMenuAvailable
    """
    #  bool QGenericUnixTheme::isDBusGlobalMenuAvailable()
    return Rituals.call(
        'ritual_ZN17QGenericUnixTheme25isDBusGlobalMenuAvailableEv',
    )

  @staticmethod
  def mouseCursorTheme() -> str:
    """
    Calls Qt's 'QString QGenericUnixTheme::mouseCursorTheme()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgenericunixtheme.html#mouseCursorTheme

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QGenericUnixTheme::mouseCursorTheme()
    return Rituals.call('ritual_ZN17QGenericUnixTheme16mouseCursorThemeEv')

  @staticmethod
  def mouseCursorSize() -> QSize:
    """
    Calls Qt's 'QSize QGenericUnixTheme::mouseCursorSize()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgenericunixtheme.html#mouseCursorSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QGenericUnixTheme::mouseCursorSize()
    address = Rituals.call('ritual_ZN17QGenericUnixTheme15mouseCursorSizeEv')
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  @staticmethod
  def availableXdgFileIconSizes() -> QList[QSize]:
    """
    Calls Qt's 'QList<QSize> QGenericUnixTheme::availableXdgFileIconSizes()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgenericunixtheme.html#availableXdgFileIconSizes

    Returns
    -------

    QList[QSize]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QSize> QGenericUnixTheme::availableXdgFileIconSizes()
    address = Rituals.call(
        'ritual_ZN17QGenericUnixTheme25availableXdgFileIconSizesEv',
    )
    from ..QtCore import QSize
    return QList[QSize]._cuteOwning(address)

  @staticmethod
  def shouldUseDBusTray() -> bool:
    """
    Calls Qt's 'bool QGenericUnixTheme::shouldUseDBusTray()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgenericunixtheme.html#shouldUseDBusTray
    """
    #  bool QGenericUnixTheme::shouldUseDBusTray()
    return Rituals.call('ritual_ZN17QGenericUnixTheme17shouldUseDBusTrayEv')

  @staticmethod
  @overload(QFileInfo)
  def xdgFileIcon(fileInfo: QFileInfo) -> QIcon:
    """
    Calls Qt's 'QIcon QGenericUnixTheme::xdgFileIcon(const QFileInfo
    &fileInfo)'.

    Qt's own words: https://doc.qt.io/qt-6/qgenericunixtheme.html#xdgFileIcon

    Parameters
    ----------

    fileInfo : QFileInfo
      Passed on as a value: Qt reads the C++ QFileInfo, which stays Python's
      own.

    Returns
    -------

    QIcon
      A new cute QIcon around the copy Qt gave back. Python owns it.
    """
    #  QIcon QGenericUnixTheme::xdgFileIcon(const QFileInfo &fileInfo)
    address = Rituals.call(
        'ritual_ZN17QGenericUnixTheme11xdgFileIconERK9QFileInfo',
        CuteMixin._valueOf(fileInfo),
    )
    from . import QIcon
    return QIcon._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGenericUnixTheme'

  #  A C++ QGenericUnixTheme Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QGenericUnixTheme'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QPlatformTheme.Font)
  def font(self, type: QPlatformTheme.Font) -> Optional[QFont]:
    """
    Calls Qt's 'const QFont *QGenericUnixTheme::font(Font type) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgenericunixtheme.html#font

    Parameters
    ----------

    type : QPlatformTheme.Font
      Passed on as its number.

    Returns
    -------

    Optional[QFont]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QFont *QGenericUnixTheme::font(Font type) const
    ritual = 'ritual_ZNK17QGenericUnixTheme4fontEN14QPlatformTheme4FontE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK17QGenericUnixTheme4fontEN14QPlatformTheme4FontE')
    address = self.uglySide.call(ritual, type.value)
    from . import QFont
    return QFont._cuteAt(address)

  @overload(QPlatformTheme.ThemeHint)
  def themeHint(self, hint: QPlatformTheme.ThemeHint) -> QVariant:
    """
    Calls Qt's 'QVariant QGenericUnixTheme::themeHint(ThemeHint hint) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgenericunixtheme.html#themeHint

    Parameters
    ----------

    hint : QPlatformTheme.ThemeHint
      Passed on as its number.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QGenericUnixTheme::themeHint(ThemeHint hint) const
    ritual = (
        'ritual_ZNK17QGenericUnixTheme9themeHintEN14QPlatformTheme9ThemeHin'
        'tE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK17QGenericUnixTheme9themeHintEN14QPlatformTheme9Th'
          'emeHintE')
    address = self.uglySide.call(ritual, hint.value)
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def createPlatformMenuBar(self) -> Optional[QPlatformMenuBar]:
    """
    Calls Qt's 'QPlatformMenuBar *QGenericUnixTheme::createPlatformMenuBar()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgenericunixtheme.html#createPlatformMenuBar

    Returns
    -------

    Optional[QPlatformMenuBar]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlatformMenuBar *QGenericUnixTheme::createPlatformMenuBar() const
    ritual = 'ritual_ZNK17QGenericUnixTheme21createPlatformMenuBarEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QGenericUnixTheme21createPlatformMenuBarEv'
    address = self.uglySide.call(ritual)
    from . import QPlatformMenuBar
    return QPlatformMenuBar._cuteAt(address)

  def createPlatformSystemTrayIcon(
      self,
  ) -> Optional[QPlatformSystemTrayIcon]:
    """
    Calls Qt's 'QPlatformSystemTrayIcon
    *QGenericUnixTheme::createPlatformSystemTrayIcon() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgenericunixtheme.html

    Returns
    -------

    Optional[QPlatformSystemTrayIcon]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlatformSystemTrayIcon
    #      *QGenericUnixTheme::createPlatformSystemTrayIcon() const
    ritual = 'ritual_ZNK17QGenericUnixTheme28createPlatformSystemTrayIconEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK17QGenericUnixTheme28createPlatformSystemTrayIconE'
          'v')
    address = self.uglySide.call(ritual)
    from . import QPlatformSystemTrayIcon
    return QPlatformSystemTrayIcon._cuteAt(address)

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

  @overload(QGenericUnixThemePrivate)
  @overload(NoneType)
  def __init__(self, p: Optional[QGenericUnixThemePrivate]) -> None:
    """
    Notes what was given, for Qt's
    'QGenericUnixTheme::QGenericUnixTheme(QGenericUnixThemePrivate *p)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgenericunixtheme.html#QGenericUnixTheme

    Parameters
    ----------

    p : Optional[QGenericUnixThemePrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QGenericUnixTheme::QGenericUnixTheme(QGenericUnixThemePrivate *p)
    self._noteCreation(QGenericUnixTheme, lambda: Rituals.call(
        'ritual_ZN17QGenericUnixThemeC1EP24QGenericUnixThemePrivate',
        self._addressOf(p),
    ))

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QGenericUnixTheme::QGenericUnixTheme()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgenericunixtheme.html#QGenericUnixTheme
    """
    #  QGenericUnixTheme::QGenericUnixTheme()
    self._noteCreation(QGenericUnixTheme, lambda: Rituals.call(
        'ritual_ZN17QGenericUnixThemeC1Ev',
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

  def d_func(self) -> Optional[QGenericUnixThemePrivate]:
    """
    Calls Qt's 'QGenericUnixThemePrivate *QGenericUnixTheme::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qgenericunixtheme.html#d_func

    Returns
    -------

    Optional[QGenericUnixThemePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGenericUnixThemePrivate *QGenericUnixTheme::d_func()
    address = self.uglySide.call('ritual_ZN17QGenericUnixTheme6d_funcEv')
    from . import QGenericUnixThemePrivate
    return QGenericUnixThemePrivate._cuteAt(address)
