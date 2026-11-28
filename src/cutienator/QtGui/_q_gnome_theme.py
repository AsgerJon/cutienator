"""
QGnomeTheme binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qgnometheme_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QGnomeTheme to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import Qt
from . import QGenericUnixTheme, QPlatformTheme

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QFileInfo, QVariant
  from . import QFont, QGnomeThemePrivate, QIcon, QPlatformMenuBar
  from . import QPlatformSystemTrayIcon
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QFileInfo = WAIT['QFileInfo']


class QGnomeTheme(QGenericUnixTheme):
  """
  The cute side of Qt's QGnomeTheme: a plain Python object standing in front
  of one C++ QGnomeTheme.

  It is built on the cute 'QGenericUnixTheme', as Qt's QGnomeTheme is built
  on Qt's QGenericUnixTheme, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QGnomeTheme that has a ritual and that Python can
  call so far, 15 names in all: 'd_func', 'themeHint', 'fileIcon', 'font',
  'standardButtonText', 'gtkFontName', 'requestColorScheme', 'colorScheme',
  'updateColorScheme', 'updateHighContrast', 'updateReducedMotion',
  'createPlatformMenuBar', 'contrastPreference', 'motionPreference',
  'createPlatformSystemTrayIcon'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QGnomeThemePrivate *QGnomeTheme::d_func() const': takes in
    Python what 'QGnomeThemePrivate *QGnomeTheme::d_func()' takes.

  What to expect
  --------------

  - The C++ QGnomeTheme is created at the first use, not by
    'QGnomeTheme(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGnomeTheme.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGnomeTheme'

  #  A C++ QGnomeTheme Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QGnomeTheme'

  #  The functions Qt calls itself that QGnomeTheme is the first to declare.
  #  A class of a program built on it can write one anew, and Qt then calls
  #  that. For each name: the key C++ knows the function by, what it gives,
  #  and what it takes.
  __virtual_functions__ = {
      'gtkFontName': (
          ('_ZNK11QGnomeTheme11gtkFontNameEv',
           ('address', 'text', ''),
           ()),
      ),
      'updateColorScheme': (
          ('_ZN11QGnomeTheme17updateColorSchemeEN2Qt11ColorSchemeE',
           ('nothing', 'nothing', ''),
           (
               ('int', 'enum', 'QtCore:Qt.ColorScheme'),
           )),
      ),
      'updateHighContrast': (
          ('_ZN11QGnomeTheme18updateHighContrastEN2Qt18ContrastPreferenceE',
           ('nothing', 'nothing', ''),
           (
               ('int', 'enum', 'QtCore:Qt.ContrastPreference'),
           )),
      ),
      'updateReducedMotion': (
          ('_ZN11QGnomeTheme19updateReducedMotionEN2Qt16MotionPreferenceE',
           ('nothing', 'nothing', ''),
           (
               ('int', 'enum', 'QtCore:Qt.MotionPreference'),
           )),
      ),
  }

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
    Calls Qt's 'QVariant QGnomeTheme::themeHint(ThemeHint hint) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgnometheme.html#themeHint

    Parameters
    ----------

    hint : QPlatformTheme.ThemeHint
      Passed on as its number.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QGnomeTheme::themeHint(ThemeHint hint) const
    ritual = 'ritual_ZNK11QGnomeTheme9themeHintEN14QPlatformTheme9ThemeHintE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK11QGnomeTheme9themeHintEN14QPlatformTheme9ThemeHin'
          'tE')
    address = self.uglySide.call(ritual, hint.value)
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(QFileInfo)
  @overload(QFileInfo, QPlatformTheme.IconOptions)
  def fileIcon(
      self,
      fileInfo: QFileInfo,
      a1: QPlatformTheme.IconOptions = QPlatformTheme.IconOptions(),
  ) -> QIcon:
    """
    Calls Qt's 'QIcon QGnomeTheme::fileIcon(const QFileInfo &fileInfo,
    QPlatformTheme::IconOptions a1) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgnometheme.html#fileIcon

    Parameters
    ----------

    fileInfo : QFileInfo
      Passed on as a value: Qt reads the C++ QFileInfo, which stays Python's
      own.

    a1 : QPlatformTheme.IconOptions
      Passed on as its number. May be left out, as in Qt: it is then
      QPlatformTheme.IconOptions().

    Returns
    -------

    QIcon
      A new cute QIcon around the copy Qt gave back. Python owns it.
    """
    #  QIcon QGnomeTheme::fileIcon(const QFileInfo &fileInfo,
    #      QPlatformTheme::IconOptions a1) const
    ritual = (
        'ritual_ZNK11QGnomeTheme8fileIconERK9QFileInfo6QFlagsIN14QPlatformT'
        'heme10IconOptionEE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK11QGnomeTheme8fileIconERK9QFileInfo6QFlagsIN14QPla'
          'tformTheme10IconOptionEE')
    address = self.uglySide.call(ritual, self._valueOf(fileInfo), a1.value)
    from . import QIcon
    return QIcon._cuteOwning(address)

  @overload(QPlatformTheme.Font)
  def font(self, type: QPlatformTheme.Font) -> Optional[QFont]:
    """
    Calls Qt's 'const QFont *QGnomeTheme::font(Font type) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgnometheme.html#font

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
    #  const QFont *QGnomeTheme::font(Font type) const
    ritual = 'ritual_ZNK11QGnomeTheme4fontEN14QPlatformTheme4FontE'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QGnomeTheme4fontEN14QPlatformTheme4FontE'
    address = self.uglySide.call(ritual, type.value)
    from . import QFont
    return QFont._cuteAt(address)

  @overload(int)
  def standardButtonText(self, button: int) -> str:
    """
    Calls Qt's 'QString QGnomeTheme::standardButtonText(int button) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgnometheme.html#standardButtonText

    Parameters
    ----------

    button : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QGnomeTheme::standardButtonText(int button) const
    ritual = 'ritual_ZNK11QGnomeTheme18standardButtonTextEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QGnomeTheme18standardButtonTextEi'
    return self.uglySide.call(ritual, button)

  def gtkFontName(self) -> str:
    """
    Calls Qt's 'QString QGnomeTheme::gtkFontName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgnometheme.html#gtkFontName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QGnomeTheme::gtkFontName() const
    ritual = 'ritual_ZNK11QGnomeTheme11gtkFontNameEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QGnomeTheme11gtkFontNameEv'
    return self.uglySide.call(ritual)

  def colorScheme(self) -> Qt.ColorScheme:
    """
    Calls Qt's 'Qt::ColorScheme QGnomeTheme::colorScheme() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgnometheme.html#colorScheme

    Returns
    -------

    Qt.ColorScheme
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.ColorScheme(number)'
      gives.
    """
    #  Qt::ColorScheme QGnomeTheme::colorScheme() const
    ritual = 'ritual_ZNK11QGnomeTheme11colorSchemeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QGnomeTheme11colorSchemeEv'
    return Qt.ColorScheme(self.uglySide.call(ritual))

  def createPlatformMenuBar(self) -> Optional[QPlatformMenuBar]:
    """
    Calls Qt's 'QPlatformMenuBar *QGnomeTheme::createPlatformMenuBar()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgnometheme.html#createPlatformMenuBar

    Returns
    -------

    Optional[QPlatformMenuBar]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlatformMenuBar *QGnomeTheme::createPlatformMenuBar() const
    ritual = 'ritual_ZNK11QGnomeTheme21createPlatformMenuBarEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QGnomeTheme21createPlatformMenuBarEv'
    address = self.uglySide.call(ritual)
    from . import QPlatformMenuBar
    return QPlatformMenuBar._cuteAt(address)

  def contrastPreference(self) -> Qt.ContrastPreference:
    """
    Calls Qt's 'Qt::ContrastPreference QGnomeTheme::contrastPreference()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgnometheme.html#contrastPreference

    Returns
    -------

    Qt.ContrastPreference
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt.ContrastPreference(number)' gives.
    """
    #  Qt::ContrastPreference QGnomeTheme::contrastPreference() const
    ritual = 'ritual_ZNK11QGnomeTheme18contrastPreferenceEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QGnomeTheme18contrastPreferenceEv'
    return Qt.ContrastPreference(self.uglySide.call(ritual))

  def motionPreference(self) -> Qt.MotionPreference:
    """
    Calls Qt's 'Qt::MotionPreference QGnomeTheme::motionPreference() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgnometheme.html#motionPreference

    Returns
    -------

    Qt.MotionPreference
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt.MotionPreference(number)' gives.
    """
    #  Qt::MotionPreference QGnomeTheme::motionPreference() const
    ritual = 'ritual_ZNK11QGnomeTheme16motionPreferenceEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QGnomeTheme16motionPreferenceEv'
    return Qt.MotionPreference(self.uglySide.call(ritual))

  def createPlatformSystemTrayIcon(
      self,
  ) -> Optional[QPlatformSystemTrayIcon]:
    """
    Calls Qt's 'QPlatformSystemTrayIcon
    *QGnomeTheme::createPlatformSystemTrayIcon() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgnometheme.html#createPlatformSystemTrayIcon

    Returns
    -------

    Optional[QPlatformSystemTrayIcon]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlatformSystemTrayIcon *QGnomeTheme::createPlatformSystemTrayIcon()
    #      const
    ritual = 'ritual_ZNK11QGnomeTheme28createPlatformSystemTrayIconEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QGnomeTheme28createPlatformSystemTrayIconEv'
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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QGnomeTheme::QGnomeTheme()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qgnometheme.html#QGnomeTheme
    """
    #  QGnomeTheme::QGnomeTheme()
    self._noteCreation(QGnomeTheme, lambda: Rituals.call(
        'ritual_ZN11QGnomeThemeC1Ev',
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

  def d_func(self) -> Optional[QGnomeThemePrivate]:
    """
    Calls Qt's 'QGnomeThemePrivate *QGnomeTheme::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qgnometheme.html#d_func

    Returns
    -------

    Optional[QGnomeThemePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGnomeThemePrivate *QGnomeTheme::d_func()
    address = self.uglySide.call('ritual_ZN11QGnomeTheme6d_funcEv')
    from . import QGnomeThemePrivate
    return QGnomeThemePrivate._cuteAt(address)

  @overload(Qt.ColorScheme)
  def requestColorScheme(self, a0: Qt.ColorScheme) -> None:
    """
    Calls Qt's 'void QGnomeTheme::requestColorScheme(Qt::ColorScheme a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgnometheme.html#requestColorScheme

    Parameters
    ----------

    a0 : Qt.ColorScheme
      Passed on as its number.
    """
    #  void QGnomeTheme::requestColorScheme(Qt::ColorScheme a0)
    ritual = 'ritual_ZN11QGnomeTheme18requestColorSchemeEN2Qt11ColorSchemeE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN11QGnomeTheme18requestColorSchemeEN2Qt11ColorScheme'
          'E')
    self.uglySide.call(ritual, a0.value)

  @overload(Qt.ColorScheme)
  def updateColorScheme(self, a0: Qt.ColorScheme) -> None:
    """
    Calls Qt's 'void QGnomeTheme::updateColorScheme(Qt::ColorScheme a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qgnometheme.html#updateColorScheme

    Parameters
    ----------

    a0 : Qt.ColorScheme
      Passed on as its number.
    """
    #  void QGnomeTheme::updateColorScheme(Qt::ColorScheme a0)
    ritual = 'ritual_ZN11QGnomeTheme17updateColorSchemeEN2Qt11ColorSchemeE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN11QGnomeTheme17updateColorSchemeEN2Qt11ColorSchemeE')
    self.uglySide.call(ritual, a0.value)

  @overload(Qt.ContrastPreference)
  def updateHighContrast(self, a0: Qt.ContrastPreference) -> None:
    """
    Calls Qt's 'void QGnomeTheme::updateHighContrast(Qt::ContrastPreference
    a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgnometheme.html#updateHighContrast

    Parameters
    ----------

    a0 : Qt.ContrastPreference
      Passed on as its number.
    """
    #  void QGnomeTheme::updateHighContrast(Qt::ContrastPreference a0)
    ritual = (
        'ritual_ZN11QGnomeTheme18updateHighContrastEN2Qt18ContrastPreferenc'
        'eE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN11QGnomeTheme18updateHighContrastEN2Qt18ContrastPre'
          'ferenceE')
    self.uglySide.call(ritual, a0.value)

  @overload(Qt.MotionPreference)
  def updateReducedMotion(self, a0: Qt.MotionPreference) -> None:
    """
    Calls Qt's 'void QGnomeTheme::updateReducedMotion(Qt::MotionPreference
    a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgnometheme.html#updateReducedMotion

    Parameters
    ----------

    a0 : Qt.MotionPreference
      Passed on as its number.
    """
    #  void QGnomeTheme::updateReducedMotion(Qt::MotionPreference a0)
    ritual = (
        'ritual_ZN11QGnomeTheme19updateReducedMotionEN2Qt16MotionPreference'
        'E')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN11QGnomeTheme19updateReducedMotionEN2Qt16MotionPref'
          'erenceE')
    self.uglySide.call(ritual, a0.value)
