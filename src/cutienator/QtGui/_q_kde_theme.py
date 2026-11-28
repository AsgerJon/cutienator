"""
QKdeTheme binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qkdetheme_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QKdeTheme to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import Qt, QStringList
from . import QGenericUnixTheme, QPlatformTheme

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QFileInfo, QVariant
  from . import QFont, QIcon, QPalette, QPlatformMenuBar
  from . import QPlatformSystemTrayIcon
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QFileInfo = WAIT['QFileInfo']


class QKdeTheme(QGenericUnixTheme):
  """
  The cute side of Qt's QKdeTheme: a plain Python object standing in front of
  one C++ QKdeTheme.

  It is built on the cute 'QGenericUnixTheme', as Qt's QKdeTheme is built on
  Qt's QGenericUnixTheme, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QKdeTheme that has a ritual and that Python can call
  so far, 9 names in all: 'createKdeTheme', 'themeHint', 'fileIcon',
  'palette', 'colorScheme', 'requestColorScheme', 'font',
  'createPlatformMenuBar', 'createPlatformSystemTrayIcon'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QKdeThemePrivate *QKdeTheme::d_func()': gives 'QKdeThemePrivate',
    which has no cute class yet.
  - Qt's 'const QKdeThemePrivate *QKdeTheme::d_func() const': gives
    'QKdeThemePrivate', which has no cute class yet.
  - Qt's 'QKdeTheme::~QKdeTheme()': the destructor: Python never removes a
    C++ QKdeTheme.

  What to expect
  --------------

  - The C++ QKdeTheme is created at the first use, not by 'QKdeTheme(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QKdeTheme.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def createKdeTheme() -> Optional[QPlatformTheme]:
    """
    Calls Qt's 'QPlatformTheme *QKdeTheme::createKdeTheme()'.

    Qt's own words: https://doc.qt.io/qt-6/qkdetheme.html#createKdeTheme

    Returns
    -------

    Optional[QPlatformTheme]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlatformTheme *QKdeTheme::createKdeTheme()
    address = Rituals.call('ritual_ZN9QKdeTheme14createKdeThemeEv')
    return QPlatformTheme._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QKdeTheme'

  #  A C++ QKdeTheme Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QKdeTheme'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QPlatformTheme.ThemeHint)
  def themeHint(self, hint: QPlatformTheme.ThemeHint) -> QVariant:
    """
    Calls Qt's 'QVariant QKdeTheme::themeHint(ThemeHint hint) const'.

    Qt's own words: https://doc.qt.io/qt-6/qkdetheme.html#themeHint

    Parameters
    ----------

    hint : QPlatformTheme.ThemeHint
      Passed on as its number.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QKdeTheme::themeHint(ThemeHint hint) const
    ritual = 'ritual_ZNK9QKdeTheme9themeHintEN14QPlatformTheme9ThemeHintE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK9QKdeTheme9themeHintEN14QPlatformTheme9ThemeHintE')
    address = self.uglySide.call(ritual, hint.value)
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(QFileInfo)
  @overload(QFileInfo, QPlatformTheme.IconOptions)
  def fileIcon(
      self,
      fileInfo: QFileInfo,
      iconOptions: QPlatformTheme.IconOptions = QPlatformTheme.IconOptions(),
  ) -> QIcon:
    """
    Calls Qt's 'QIcon QKdeTheme::fileIcon(const QFileInfo &fileInfo,
    QPlatformTheme::IconOptions iconOptions) const'.

    Qt's own words: https://doc.qt.io/qt-6/qkdetheme.html#fileIcon

    Parameters
    ----------

    fileInfo : QFileInfo
      Passed on as a value: Qt reads the C++ QFileInfo, which stays Python's
      own.

    iconOptions : QPlatformTheme.IconOptions
      Passed on as its number. May be left out, as in Qt: it is then
      QPlatformTheme.IconOptions().

    Returns
    -------

    QIcon
      A new cute QIcon around the copy Qt gave back. Python owns it.
    """
    #  QIcon QKdeTheme::fileIcon(const QFileInfo &fileInfo,
    #      QPlatformTheme::IconOptions iconOptions) const
    ritual = (
        'ritual_ZNK9QKdeTheme8fileIconERK9QFileInfo6QFlagsIN14QPlatformThem'
        'e10IconOptionEE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK9QKdeTheme8fileIconERK9QFileInfo6QFlagsIN14QPlatfo'
          'rmTheme10IconOptionEE')
    address = self.uglySide.call(
        ritual, self._valueOf(fileInfo), iconOptions.value,
    )
    from . import QIcon
    return QIcon._cuteOwning(address)

  @overload()
  @overload(QPlatformTheme.Palette)
  def palette(
      self,
      type: QPlatformTheme.Palette = QPlatformTheme.Palette.SystemPalette,
  ) -> Optional[QPalette]:
    """
    Calls Qt's 'const QPalette *QKdeTheme::palette(Palette type) const'.

    Qt's own words: https://doc.qt.io/qt-6/qkdetheme.html#palette

    Parameters
    ----------

    type : QPlatformTheme.Palette
      Passed on as its number. May be left out, as in Qt: it is then
      QPlatformTheme.Palette.SystemPalette.

    Returns
    -------

    Optional[QPalette]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QPalette *QKdeTheme::palette(Palette type) const
    ritual = 'ritual_ZNK9QKdeTheme7paletteEN14QPlatformTheme7PaletteE'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK9QKdeTheme7paletteEN14QPlatformTheme7PaletteE'
    address = self.uglySide.call(ritual, type.value)
    from . import QPalette
    return QPalette._cuteAt(address)

  def colorScheme(self) -> Qt.ColorScheme:
    """
    Calls Qt's 'Qt::ColorScheme QKdeTheme::colorScheme() const'.

    Qt's own words: https://doc.qt.io/qt-6/qkdetheme.html#colorScheme

    Returns
    -------

    Qt.ColorScheme
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.ColorScheme(number)'
      gives.
    """
    #  Qt::ColorScheme QKdeTheme::colorScheme() const
    ritual = 'ritual_ZNK9QKdeTheme11colorSchemeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK9QKdeTheme11colorSchemeEv'
    return Qt.ColorScheme(self.uglySide.call(ritual))

  @overload(QPlatformTheme.Font)
  def font(self, type: QPlatformTheme.Font) -> Optional[QFont]:
    """
    Calls Qt's 'const QFont *QKdeTheme::font(Font type) const'.

    Qt's own words: https://doc.qt.io/qt-6/qkdetheme.html#font

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
    #  const QFont *QKdeTheme::font(Font type) const
    ritual = 'ritual_ZNK9QKdeTheme4fontEN14QPlatformTheme4FontE'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK9QKdeTheme4fontEN14QPlatformTheme4FontE'
    address = self.uglySide.call(ritual, type.value)
    from . import QFont
    return QFont._cuteAt(address)

  def createPlatformMenuBar(self) -> Optional[QPlatformMenuBar]:
    """
    Calls Qt's 'QPlatformMenuBar *QKdeTheme::createPlatformMenuBar() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qkdetheme.html#createPlatformMenuBar

    Returns
    -------

    Optional[QPlatformMenuBar]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlatformMenuBar *QKdeTheme::createPlatformMenuBar() const
    ritual = 'ritual_ZNK9QKdeTheme21createPlatformMenuBarEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK9QKdeTheme21createPlatformMenuBarEv'
    address = self.uglySide.call(ritual)
    from . import QPlatformMenuBar
    return QPlatformMenuBar._cuteAt(address)

  def createPlatformSystemTrayIcon(
      self,
  ) -> Optional[QPlatformSystemTrayIcon]:
    """
    Calls Qt's 'QPlatformSystemTrayIcon
    *QKdeTheme::createPlatformSystemTrayIcon() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qkdetheme.html#createPlatformSystemTrayIcon

    Returns
    -------

    Optional[QPlatformSystemTrayIcon]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlatformSystemTrayIcon *QKdeTheme::createPlatformSystemTrayIcon()
    #      const
    ritual = 'ritual_ZNK9QKdeTheme28createPlatformSystemTrayIconEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK9QKdeTheme28createPlatformSystemTrayIconEv'
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

  @overload(QStringList, int)
  def __init__(self, kdeDirs: QStringList, kdeVersion: int) -> None:
    """
    Notes what was given, for Qt's 'QKdeTheme::QKdeTheme(const QStringList
    &kdeDirs, int kdeVersion)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qkdetheme.html#QKdeTheme

    Parameters
    ----------

    kdeDirs : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    kdeVersion : int
      Passed on as it is.
    """
    #  QKdeTheme::QKdeTheme(const QStringList &kdeDirs, int kdeVersion)
    self._noteCreation(QKdeTheme, lambda: Rituals.call(
        'ritual_ZN9QKdeThemeC1ERK5QListI7QStringEi',
        self._valueOf(kdeDirs), kdeVersion,
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

  @overload(Qt.ColorScheme)
  def requestColorScheme(self, scheme: Qt.ColorScheme) -> None:
    """
    Calls Qt's 'void QKdeTheme::requestColorScheme(Qt::ColorScheme scheme)'.

    Qt's own words: https://doc.qt.io/qt-6/qkdetheme.html#requestColorScheme

    Parameters
    ----------

    scheme : Qt.ColorScheme
      Passed on as its number.
    """
    #  void QKdeTheme::requestColorScheme(Qt::ColorScheme scheme)
    ritual = 'ritual_ZN9QKdeTheme18requestColorSchemeEN2Qt11ColorSchemeE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN9QKdeTheme18requestColorSchemeEN2Qt11ColorSchemeE')
    self.uglySide.call(ritual, scheme.value)
