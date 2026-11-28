"""
QIconLoader binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qiconloader_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QIconLoader to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals
from ..QtCore import QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QIconEngine, QIconTheme, QThemeIconInfo


class QIconLoader(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QIconLoader: a plain Python object standing in front
  of one C++ QIconLoader.

  C++ hands a QIconLoader around as a copy, so every C++ QIconLoader behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QIconLoader that has a ritual and that Python can
  call so far, 18 names in all: 'loadIcon', 'themeKey', 'themeName',
  'setThemeName', 'fallbackThemeName', 'setFallbackThemeName', 'theme',
  'setThemeSearchPath', 'themeSearchPaths', 'setFallbackSearchPaths',
  'fallbackSearchPaths', 'instance', 'updateSystemTheme', 'invalidateKey',
  'ensureInitialized', 'hasUserTheme', 'iconEngine', 'lookupFallbackIcon'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QThemeIconInfo QIconLoader::findIconHelper(const QString
    &themeName, const QString &iconName, QStringList &visited, DashRule rule)
    const': takes a type Python has no way to hand over yet.
  - Qt's 'QIconLoader::~QIconLoader()': the destructor: Python removes its
    C++ QIconLoader by it, and has no other use for it.

  What has no ritual
  ------------------

  1 of the 22 functions Qt declares: 1 cannot be called and cannot be called
  through the meta-object and cannot be copied.

  What to expect
  --------------

  - The C++ QIconLoader is created at the first use, not by
    'QIconLoader(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QIconLoader back gives a copy the ritual made for
    Python, in a new cute QIconLoader.
  - Each name of Qt's QIconLoader that has no cute function yet, 'dirInfo',
    'findIconHelper', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def instance() -> Optional[QIconLoader]:
    """
    Calls Qt's 'QIconLoader *QIconLoader::instance()'.

    Qt's own words: https://doc.qt.io/qt-6/qiconloader.html#instance

    Returns
    -------

    Optional[QIconLoader]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QIconLoader *QIconLoader::instance()
    address = Rituals.call('ritual_ZN11QIconLoader8instanceEv')
    return QIconLoader._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QIconLoader'

  #  Qt's '~QIconLoader()'. Naming it makes this a value class: Python owns
  #  every C++ QIconLoader behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN11QIconLoaderD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def loadIcon(self, iconName: str) -> QThemeIconInfo:
    """
    Calls Qt's 'QThemeIconInfo QIconLoader::loadIcon(const QString &iconName)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qiconloader.html#loadIcon

    Parameters
    ----------

    iconName : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QThemeIconInfo
      A new cute QThemeIconInfo around the copy Qt gave back. Python owns it.
    """
    #  QThemeIconInfo QIconLoader::loadIcon(const QString &iconName) const
    address = self.uglySide.call(
        'ritual_ZNK11QIconLoader8loadIconERK7QString', iconName,
    )
    from . import QThemeIconInfo
    return QThemeIconInfo._cuteOwning(address)

  def themeKey(self) -> int:
    """
    Calls Qt's 'uint QIconLoader::themeKey() const'.

    Qt's own words: https://doc.qt.io/qt-6/qiconloader.html#themeKey
    """
    #  uint QIconLoader::themeKey() const
    return self.uglySide.call('ritual_ZNK11QIconLoader8themeKeyEv')

  def themeName(self) -> str:
    """
    Calls Qt's 'QString QIconLoader::themeName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qiconloader.html#themeName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QIconLoader::themeName() const
    return self.uglySide.call('ritual_ZNK11QIconLoader9themeNameEv')

  def fallbackThemeName(self) -> str:
    """
    Calls Qt's 'QString QIconLoader::fallbackThemeName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qiconloader.html#fallbackThemeName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QIconLoader::fallbackThemeName() const
    return self.uglySide.call('ritual_ZNK11QIconLoader17fallbackThemeNameEv')

  def themeSearchPaths(self) -> QStringList:
    """
    Calls Qt's 'QStringList QIconLoader::themeSearchPaths() const'.

    Qt's own words: https://doc.qt.io/qt-6/qiconloader.html#themeSearchPaths

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QIconLoader::themeSearchPaths() const
    address = self.uglySide.call(
        'ritual_ZNK11QIconLoader16themeSearchPathsEv',
    )
    return QStringList._cuteOwning(address)

  def fallbackSearchPaths(self) -> QStringList:
    """
    Calls Qt's 'QStringList QIconLoader::fallbackSearchPaths() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qiconloader.html#fallbackSearchPaths

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QIconLoader::fallbackSearchPaths() const
    address = self.uglySide.call(
        'ritual_ZNK11QIconLoader19fallbackSearchPathsEv',
    )
    return QStringList._cuteOwning(address)

  def hasUserTheme(self) -> bool:
    """
    Calls Qt's 'bool QIconLoader::hasUserTheme() const'.

    Qt's own words: https://doc.qt.io/qt-6/qiconloader.html#hasUserTheme
    """
    #  bool QIconLoader::hasUserTheme() const
    return self.uglySide.call('ritual_ZNK11QIconLoader12hasUserThemeEv')

  @overload(str)
  def iconEngine(self, iconName: str) -> Optional[QIconEngine]:
    """
    Calls Qt's 'QIconEngine *QIconLoader::iconEngine(const QString &iconName)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qiconloader.html#iconEngine

    Parameters
    ----------

    iconName : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    Optional[QIconEngine]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QIconEngine *QIconLoader::iconEngine(const QString &iconName) const
    address = self.uglySide.call(
        'ritual_ZNK11QIconLoader10iconEngineERK7QString', iconName,
    )
    from . import QIconEngine
    return QIconEngine._cuteAt(address)

  @overload(str)
  def lookupFallbackIcon(self, iconName: str) -> QThemeIconInfo:
    """
    Calls Qt's 'QThemeIconInfo QIconLoader::lookupFallbackIcon(const QString
    &iconName) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qiconloader.html#lookupFallbackIcon

    Parameters
    ----------

    iconName : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QThemeIconInfo
      A new cute QThemeIconInfo around the copy Qt gave back. Python owns it.
    """
    #  QThemeIconInfo QIconLoader::lookupFallbackIcon(const QString
    #      &iconName) const
    address = self.uglySide.call(
        'ritual_ZNK11QIconLoader18lookupFallbackIconERK7QString', iconName,
    )
    from . import QThemeIconInfo
    return QThemeIconInfo._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setThemeName(self, themeName: str) -> None:
    """
    Calls Qt's 'void QIconLoader::setThemeName(const QString &themeName)'.

    Qt's own words: https://doc.qt.io/qt-6/qiconloader.html#setThemeName

    Parameters
    ----------

    themeName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QIconLoader::setThemeName(const QString &themeName)
    self.uglySide.call(
        'ritual_ZN11QIconLoader12setThemeNameERK7QString', themeName,
    )

  @overload(str)
  def setFallbackThemeName(self, themeName: str) -> None:
    """
    Calls Qt's 'void QIconLoader::setFallbackThemeName(const QString
    &themeName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qiconloader.html#setFallbackThemeName

    Parameters
    ----------

    themeName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QIconLoader::setFallbackThemeName(const QString &themeName)
    self.uglySide.call(
        'ritual_ZN11QIconLoader20setFallbackThemeNameERK7QString', themeName,
    )

  @overload(QStringList)
  def setThemeSearchPath(self, searchPaths: QStringList) -> None:
    """
    Calls Qt's 'void QIconLoader::setThemeSearchPath(const QStringList
    &searchPaths)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qiconloader.html#setThemeSearchPath

    Parameters
    ----------

    searchPaths : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QIconLoader::setThemeSearchPath(const QStringList &searchPaths)
    self.uglySide.call(
        'ritual_ZN11QIconLoader18setThemeSearchPathERK5QListI7QStringE',
        self._valueOf(searchPaths),
    )

  @overload(QStringList)
  def setFallbackSearchPaths(self, searchPaths: QStringList) -> None:
    """
    Calls Qt's 'void QIconLoader::setFallbackSearchPaths(const QStringList
    &searchPaths)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qiconloader.html#setFallbackSearchPaths

    Parameters
    ----------

    searchPaths : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QIconLoader::setFallbackSearchPaths(const QStringList
    #      &searchPaths)
    self.uglySide.call(
        'ritual_ZN11QIconLoader22setFallbackSearchPathsERK5QListI7QStringE',
        self._valueOf(searchPaths),
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
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QIconLoader::QIconLoader()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qiconloader.html#QIconLoader
    """
    #  QIconLoader::QIconLoader()
    self._noteCreation(QIconLoader, lambda: Rituals.call(
        'ritual_ZN11QIconLoaderC1Ev',
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

  def theme(self) -> QIconTheme:
    """
    Calls Qt's 'QIconTheme QIconLoader::theme()'.

    Qt's own words: https://doc.qt.io/qt-6/qiconloader.html#theme

    Returns
    -------

    QIconTheme
      A new cute QIconTheme around the copy Qt gave back. Python owns it.
    """
    #  QIconTheme QIconLoader::theme()
    address = self.uglySide.call('ritual_ZN11QIconLoader5themeEv')
    from . import QIconTheme
    return QIconTheme._cuteOwning(address)

  def updateSystemTheme(self) -> None:
    """
    Calls Qt's 'void QIconLoader::updateSystemTheme()'.

    Qt's own words: https://doc.qt.io/qt-6/qiconloader.html#updateSystemTheme
    """
    #  void QIconLoader::updateSystemTheme()
    self.uglySide.call('ritual_ZN11QIconLoader17updateSystemThemeEv')

  def invalidateKey(self) -> None:
    """
    Calls Qt's 'void QIconLoader::invalidateKey()'.

    Qt's own words: https://doc.qt.io/qt-6/qiconloader.html#invalidateKey
    """
    #  void QIconLoader::invalidateKey()
    self.uglySide.call('ritual_ZN11QIconLoader13invalidateKeyEv')

  def ensureInitialized(self) -> None:
    """
    Calls Qt's 'void QIconLoader::ensureInitialized()'.

    Qt's own words: https://doc.qt.io/qt-6/qiconloader.html#ensureInitialized
    """
    #  void QIconLoader::ensureInitialized()
    self.uglySide.call('ritual_ZN11QIconLoader17ensureInitializedEv')

  @staticmethod
  def dirInfo(*__, **_) -> Never:
    """
    Qt's 'QIconDirInfo QIconLoader::dirInfo(int dirindex)': cannot be called
    and cannot be called through the meta-object and cannot be copied: no
    header file has its code, Qt's source does not mark it or its class for
    use from outside Qt or writes it 'inline' or nowhere, and it is no
    signal, slot or invokable function giving back nothing, of a class built
    on QObject, and Qt's source has no code for it that could be told from
    the rest.
    """
    raise NotImplementedError(
        "'QIconLoader.dirInfo' has no cute function yet. Qt's 'QIconDirInfo "
        "QIconLoader::dirInfo(int dirindex)': cannot be called and cannot "
        "be called through the meta-object and cannot be copied: no header "
        "file has its code, Qt's source does not mark it or its class for "
        "use from outside Qt or writes it 'inline' or nowhere, and it is no "
        "signal, slot or invokable function giving back nothing, of a class "
        "built on QObject, and Qt's source has no code for it that could be "
        "told from the rest.")

  @staticmethod
  def findIconHelper(*__, **_) -> Never:
    """
    Qt's 'QThemeIconInfo QIconLoader::findIconHelper(const QString
    &themeName, const QString &iconName, QStringList &visited, DashRule rule)
    const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QIconLoader.findIconHelper' has no cute function yet. Qt's "
        "'QThemeIconInfo QIconLoader::findIconHelper(const QString "
        "&themeName, const QString &iconName, QStringList &visited, "
        "DashRule rule) const': takes a type Python has no way to hand over "
        "yet.")
