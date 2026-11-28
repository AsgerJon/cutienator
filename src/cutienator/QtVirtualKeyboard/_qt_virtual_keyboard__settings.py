"""
QtVirtualKeyboard::Settings binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtVirtualKeyboard/6.12.0/QtVirtualKeyboard/private/settings_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QtVirtualKeyboard::Settings to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QObject, QStringList
from . import QtVirtualKeyboard

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QUrl
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QUrl = WAIT['QUrl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class Settings(QObject):
  """
  The cute side of Qt's QtVirtualKeyboard::Settings: a plain Python object
  standing in front of one C++ QtVirtualKeyboard::Settings.

  It is built on the cute 'QObject', as Qt's QtVirtualKeyboard::Settings is
  built on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QtVirtualKeyboard::Settings that has a ritual and
  that Python can call so far, 86 names in all: 'metaObject', 'tr',
  'instance', 'style', 'setStyle', 'styleName', 'setStyleName',
  'resetStyleName', 'locale', 'setLocale', 'resetLocale', 'availableLocales',
  'setAvailableLocales', 'activeLocales', 'setActiveLocales',
  'resetActiveLocales', 'layoutPath', 'setLayoutPath', 'resetLayoutPath',
  'wclAutoHideDelay', 'setWclAutoHideDelay', 'resetWclAutoHideDelay',
  'wclAlwaysVisible', 'setWclAlwaysVisible', 'resetWclAlwaysVisible',
  'wclAutoCommitWord', 'setWclAutoCommitWord', 'resetWclAutoCommitWord',
  'fullScreenMode', 'setFullScreenMode', 'resetFullScreenMode',
  'userDataPath', 'setUserDataPath', 'resetUserDataPath',
  'hwrTimeoutForAlphabetic', 'setHwrTimeoutForAlphabetic',
  'resetHwrTimeoutForAlphabetic', 'hwrTimeoutForCjk', 'setHwrTimeoutForCjk',
  'resetHwrTimeoutForCjk', 'inputMethodHints', 'resetInputMethodHints',
  'isHandwritingModeDisabled', 'setHandwritingModeDisabled',
  'resetHandwritingModeDisabled', 'isDefaultInputMethodDisabled',
  'setDefaultInputMethodDisabled', 'resetDefaultInputMethodDisabled',
  'isDefaultDictionaryDisabled', 'setDefaultDictionaryDisabled',
  'resetDefaultDictionaryDisabled', 'visibleFunctionKeys',
  'setVisibleFunctionKeys', 'resetVisibleFunctionKeys', 'closeOnReturn',
  'setCloseOnReturn', 'resetCloseOnReturn', 'keySoundVolume',
  'setKeySoundVolume', 'resetKeySoundVolume', 'arrowKeyNavigationEnabled',
  'setArrowKeyNavigationEnabled', 'resetArrowKeyNavigationEnabled',
  'styleChanged', 'styleNameChanged', 'requestResetStyle', 'localeChanged',
  'availableLocalesChanged', 'activeLocalesChanged', 'layoutPathChanged',
  'wclAutoHideDelayChanged', 'wclAlwaysVisibleChanged',
  'wclAutoCommitWordChanged', 'fullScreenModeChanged', 'userDataPathChanged',
  'userDataReset', 'hwrTimeoutForAlphabeticChanged',
  'hwrTimeoutForCjkChanged', 'inputMethodHintsChanged',
  'handwritingModeDisabledChanged', 'defaultInputMethodDisabledChanged',
  'defaultDictionaryDisabledChanged', 'visibleFunctionKeysChanged',
  'closeOnReturnChanged', 'keySoundVolumeChanged',
  'arrowKeyNavigationEnabledChanged'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QtVirtualKeyboard::Settings::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int QtVirtualKeyboard::Settings::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'void QtVirtualKeyboard::Settings::setInputMethodHints(const
    Qt::InputMethodHints &inputMethodHints)': takes a type Python has no way
    to hand over yet.

  What has no ritual
  ------------------

  6 of the 96 functions Qt declares: 2 not a gap; 2 forbidden; 2 the compiler
  refuses its ritual as it would be written here.

  What to expect
  --------------

  - The C++ QtVirtualKeyboard::Settings is created at the first use, not by
    'QtVirtualKeyboard::Settings(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QtVirtualKeyboard::Settings.
  - Qt tells when it has removed the C++ QtVirtualKeyboard::Settings. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QtVirtualKeyboard::Settings that has no cute function
    yet, 'setInputMethodHints', holds a function that raises
    'NotImplementedError', and its docstring says why.
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
    Calls Qt's 'QString QtVirtualKeyboard::Settings::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qtvirtualkeyboard-settings.html#tr

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
    #  QString QtVirtualKeyboard::Settings::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN17QtVirtualKeyboard8Settings2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  def instance() -> Optional[Settings]:
    """
    Calls Qt's 'Settings *QtVirtualKeyboard::Settings::instance()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-settings.html#instance

    Returns
    -------

    Optional[Settings]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Settings *QtVirtualKeyboard::Settings::instance()
    address = Rituals.call(
        'ritual_ZN17QtVirtualKeyboard8Settings8instanceEv',
    )
    return Settings._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QtVirtualKeyboard::Settings'

  #  A C++ QtVirtualKeyboard::Settings Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QtVirtualKeyboard_Settings'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QtVirtualKeyboard::Settings::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-settings.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QtVirtualKeyboard::Settings::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK17QtVirtualKeyboard8Settings10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def style(self) -> str:
    """
    Calls Qt's 'QString QtVirtualKeyboard::Settings::style() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-settings.html#style

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QtVirtualKeyboard::Settings::style() const
    return self.uglySide.call(
        'ritual_ZNK17QtVirtualKeyboard8Settings5styleEv',
    )

  def styleName(self) -> str:
    """
    Calls Qt's 'QString QtVirtualKeyboard::Settings::styleName() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-settings.html#styleName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QtVirtualKeyboard::Settings::styleName() const
    return self.uglySide.call(
        'ritual_ZNK17QtVirtualKeyboard8Settings9styleNameEv',
    )

  def locale(self) -> str:
    """
    Calls Qt's 'QString QtVirtualKeyboard::Settings::locale() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-settings.html#locale

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QtVirtualKeyboard::Settings::locale() const
    return self.uglySide.call(
        'ritual_ZNK17QtVirtualKeyboard8Settings6localeEv',
    )

  def availableLocales(self) -> QStringList:
    """
    Calls Qt's 'QStringList QtVirtualKeyboard::Settings::availableLocales()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-settings.html#availableLocales

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QtVirtualKeyboard::Settings::availableLocales() const
    address = self.uglySide.call(
        'ritual_ZNK17QtVirtualKeyboard8Settings16availableLocalesEv',
    )
    return QStringList._cuteOwning(address)

  def activeLocales(self) -> QStringList:
    """
    Calls Qt's 'QStringList QtVirtualKeyboard::Settings::activeLocales()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-settings.html#activeLocales

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QtVirtualKeyboard::Settings::activeLocales() const
    address = self.uglySide.call(
        'ritual_ZNK17QtVirtualKeyboard8Settings13activeLocalesEv',
    )
    return QStringList._cuteOwning(address)

  def layoutPath(self) -> QUrl:
    """
    Calls Qt's 'QUrl QtVirtualKeyboard::Settings::layoutPath() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-settings.html#layoutPath

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QtVirtualKeyboard::Settings::layoutPath() const
    address = self.uglySide.call(
        'ritual_ZNK17QtVirtualKeyboard8Settings10layoutPathEv',
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def wclAutoHideDelay(self) -> int:
    """
    Calls Qt's 'int QtVirtualKeyboard::Settings::wclAutoHideDelay() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-settings.html#wclAutoHideDelay
    """
    #  int QtVirtualKeyboard::Settings::wclAutoHideDelay() const
    return self.uglySide.call(
        'ritual_ZNK17QtVirtualKeyboard8Settings16wclAutoHideDelayEv',
    )

  def wclAlwaysVisible(self) -> bool:
    """
    Calls Qt's 'bool QtVirtualKeyboard::Settings::wclAlwaysVisible() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-settings.html#wclAlwaysVisible
    """
    #  bool QtVirtualKeyboard::Settings::wclAlwaysVisible() const
    return self.uglySide.call(
        'ritual_ZNK17QtVirtualKeyboard8Settings16wclAlwaysVisibleEv',
    )

  def wclAutoCommitWord(self) -> bool:
    """
    Calls Qt's 'bool QtVirtualKeyboard::Settings::wclAutoCommitWord() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-settings.html#wclAutoCommitWord
    """
    #  bool QtVirtualKeyboard::Settings::wclAutoCommitWord() const
    return self.uglySide.call(
        'ritual_ZNK17QtVirtualKeyboard8Settings17wclAutoCommitWordEv',
    )

  def fullScreenMode(self) -> bool:
    """
    Calls Qt's 'bool QtVirtualKeyboard::Settings::fullScreenMode() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-settings.html#fullScreenMode
    """
    #  bool QtVirtualKeyboard::Settings::fullScreenMode() const
    return self.uglySide.call(
        'ritual_ZNK17QtVirtualKeyboard8Settings14fullScreenModeEv',
    )

  def userDataPath(self) -> str:
    """
    Calls Qt's 'QString QtVirtualKeyboard::Settings::userDataPath() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-settings.html#userDataPath

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QtVirtualKeyboard::Settings::userDataPath() const
    return self.uglySide.call(
        'ritual_ZNK17QtVirtualKeyboard8Settings12userDataPathEv',
    )

  def hwrTimeoutForAlphabetic(self) -> int:
    """
    Calls Qt's 'int QtVirtualKeyboard::Settings::hwrTimeoutForAlphabetic()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-settings.html
    """
    #  int QtVirtualKeyboard::Settings::hwrTimeoutForAlphabetic() const
    return self.uglySide.call(
        'ritual_ZNK17QtVirtualKeyboard8Settings23hwrTimeoutForAlphabeticEv',
    )

  def hwrTimeoutForCjk(self) -> int:
    """
    Calls Qt's 'int QtVirtualKeyboard::Settings::hwrTimeoutForCjk() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-settings.html#hwrTimeoutForCjk
    """
    #  int QtVirtualKeyboard::Settings::hwrTimeoutForCjk() const
    return self.uglySide.call(
        'ritual_ZNK17QtVirtualKeyboard8Settings16hwrTimeoutForCjkEv',
    )

  def inputMethodHints(self) -> Qt.InputMethodHints:
    """
    Calls Qt's 'Qt::InputMethodHints
    QtVirtualKeyboard::Settings::inputMethodHints() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-settings.html#inputMethodHints

    Returns
    -------

    Qt.InputMethodHints
      The value standing for the combination Qt gave back.
    """
    #  Qt::InputMethodHints QtVirtualKeyboard::Settings::inputMethodHints()
    #      const
    return Qt.InputMethodHints(self.uglySide.call(
        'ritual_ZNK17QtVirtualKeyboard8Settings16inputMethodHintsEv',
    ))

  def isHandwritingModeDisabled(self) -> bool:
    """
    Calls Qt's 'bool QtVirtualKeyboard::Settings::isHandwritingModeDisabled()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-settings.html
    """
    #  bool QtVirtualKeyboard::Settings::isHandwritingModeDisabled() const
    return self.uglySide.call(
        'ritual_ZNK17QtVirtualKeyboard8Settings25isHandwritingModeDisabledE'
        'v',
    )

  def isDefaultInputMethodDisabled(self) -> bool:
    """
    Calls Qt's 'bool
    QtVirtualKeyboard::Settings::isDefaultInputMethodDisabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-settings.html
    """
    #  bool QtVirtualKeyboard::Settings::isDefaultInputMethodDisabled() const
    return self.uglySide.call(
        'ritual_ZNK17QtVirtualKeyboard8Settings28isDefaultInputMethodDisabl'
        'edEv',
    )

  def isDefaultDictionaryDisabled(self) -> bool:
    """
    Calls Qt's 'bool
    QtVirtualKeyboard::Settings::isDefaultDictionaryDisabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-settings.html
    """
    #  bool QtVirtualKeyboard::Settings::isDefaultDictionaryDisabled() const
    return self.uglySide.call(
        'ritual_ZNK17QtVirtualKeyboard8Settings27isDefaultDictionaryDisable'
        'dEv',
    )

  def visibleFunctionKeys(self) -> QtVirtualKeyboard.KeyboardFunctionKeys:
    """
    Calls Qt's 'QtVirtualKeyboard::KeyboardFunctionKeys
    QtVirtualKeyboard::Settings::visibleFunctionKeys() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-settings.html

    Returns
    -------

    QtVirtualKeyboard.KeyboardFunctionKeys
      The value standing for the combination Qt gave back.
    """
    #  QtVirtualKeyboard::KeyboardFunctionKeys
    #      QtVirtualKeyboard::Settings::visibleFunctionKeys() const
    return QtVirtualKeyboard.KeyboardFunctionKeys(self.uglySide.call(
        'ritual_ZNK17QtVirtualKeyboard8Settings19visibleFunctionKeysEv',
    ))

  def closeOnReturn(self) -> bool:
    """
    Calls Qt's 'bool QtVirtualKeyboard::Settings::closeOnReturn() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-settings.html#closeOnReturn
    """
    #  bool QtVirtualKeyboard::Settings::closeOnReturn() const
    return self.uglySide.call(
        'ritual_ZNK17QtVirtualKeyboard8Settings13closeOnReturnEv',
    )

  def keySoundVolume(self) -> float:
    """
    Calls Qt's 'qreal QtVirtualKeyboard::Settings::keySoundVolume() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-settings.html#keySoundVolume
    """
    #  qreal QtVirtualKeyboard::Settings::keySoundVolume() const
    return self.uglySide.call(
        'ritual_ZNK17QtVirtualKeyboard8Settings14keySoundVolumeEv',
    )

  def arrowKeyNavigationEnabled(self) -> bool:
    """
    Calls Qt's 'bool QtVirtualKeyboard::Settings::arrowKeyNavigationEnabled()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-settings.html
    """
    #  bool QtVirtualKeyboard::Settings::arrowKeyNavigationEnabled() const
    return self.uglySide.call(
        'ritual_ZNK17QtVirtualKeyboard8Settings25arrowKeyNavigationEnabledE'
        'v',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setStyle(self, style: str) -> None:
    """
    Calls Qt's 'void QtVirtualKeyboard::Settings::setStyle(const QString
    &style)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-settings.html#setStyle

    Parameters
    ----------

    style : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QtVirtualKeyboard::Settings::setStyle(const QString &style)
    self.uglySide.call(
        'ritual_ZN17QtVirtualKeyboard8Settings8setStyleERK7QString', style,
    )

  @overload(str)
  def setStyleName(self, name: str) -> None:
    """
    Calls Qt's 'void QtVirtualKeyboard::Settings::setStyleName(const QString
    &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-settings.html#setStyleName

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QtVirtualKeyboard::Settings::setStyleName(const QString &name)
    self.uglySide.call(
        'ritual_ZN17QtVirtualKeyboard8Settings12setStyleNameERK7QString',
        name,
    )

  @overload(str)
  def setLocale(self, locale: str) -> None:
    """
    Calls Qt's 'void QtVirtualKeyboard::Settings::setLocale(const QString
    &locale)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-settings.html#setLocale

    Parameters
    ----------

    locale : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QtVirtualKeyboard::Settings::setLocale(const QString &locale)
    self.uglySide.call(
        'ritual_ZN17QtVirtualKeyboard8Settings9setLocaleERK7QString', locale,
    )

  @overload(QStringList)
  def setAvailableLocales(self, availableLocales: QStringList) -> None:
    """
    Calls Qt's 'void QtVirtualKeyboard::Settings::setAvailableLocales(const
    QStringList &availableLocales)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-settings.html

    Parameters
    ----------

    availableLocales : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QtVirtualKeyboard::Settings::setAvailableLocales(const
    #      QStringList &availableLocales)
    self.uglySide.call(
        'ritual_ZN17QtVirtualKeyboard8Settings19setAvailableLocalesERK5QLis'
        'tI7QStringE',
        self._valueOf(availableLocales),
    )

  @overload(QStringList)
  def setActiveLocales(self, activeLocales: QStringList) -> None:
    """
    Calls Qt's 'void QtVirtualKeyboard::Settings::setActiveLocales(const
    QStringList &activeLocales)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-settings.html#setActiveLocales

    Parameters
    ----------

    activeLocales : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QtVirtualKeyboard::Settings::setActiveLocales(const QStringList
    #      &activeLocales)
    self.uglySide.call(
        'ritual_ZN17QtVirtualKeyboard8Settings16setActiveLocalesERK5QListI7'
        'QStringE',
        self._valueOf(activeLocales),
    )

  @overload(QUrl)
  def setLayoutPath(self, layoutPath: QUrl) -> None:
    """
    Calls Qt's 'void QtVirtualKeyboard::Settings::setLayoutPath(const QUrl
    &layoutPath)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-settings.html#setLayoutPath

    Parameters
    ----------

    layoutPath : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QtVirtualKeyboard::Settings::setLayoutPath(const QUrl
    #      &layoutPath)
    self.uglySide.call(
        'ritual_ZN17QtVirtualKeyboard8Settings13setLayoutPathERK4QUrl',
        self._valueOf(layoutPath),
    )

  @overload(int)
  def setWclAutoHideDelay(self, wclAutoHideDelay: int) -> None:
    """
    Calls Qt's 'void QtVirtualKeyboard::Settings::setWclAutoHideDelay(int
    wclAutoHideDelay)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-settings.html

    Parameters
    ----------

    wclAutoHideDelay : int
      Passed on as it is.
    """
    #  void QtVirtualKeyboard::Settings::setWclAutoHideDelay(int
    #      wclAutoHideDelay)
    self.uglySide.call(
        'ritual_ZN17QtVirtualKeyboard8Settings19setWclAutoHideDelayEi',
        wclAutoHideDelay,
    )

  @overload(bool)
  def setWclAlwaysVisible(self, wclAlwaysVisible: bool) -> None:
    """
    Calls Qt's 'void QtVirtualKeyboard::Settings::setWclAlwaysVisible(bool
    wclAlwaysVisible)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-settings.html

    Parameters
    ----------

    wclAlwaysVisible : bool
      Passed on as it is.
    """
    #  void QtVirtualKeyboard::Settings::setWclAlwaysVisible(bool
    #      wclAlwaysVisible)
    self.uglySide.call(
        'ritual_ZN17QtVirtualKeyboard8Settings19setWclAlwaysVisibleEb',
        wclAlwaysVisible,
    )

  @overload(bool)
  def setWclAutoCommitWord(self, wclAutoCommitWord: bool) -> None:
    """
    Calls Qt's 'void QtVirtualKeyboard::Settings::setWclAutoCommitWord(bool
    wclAutoCommitWord)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-settings.html

    Parameters
    ----------

    wclAutoCommitWord : bool
      Passed on as it is.
    """
    #  void QtVirtualKeyboard::Settings::setWclAutoCommitWord(bool
    #      wclAutoCommitWord)
    self.uglySide.call(
        'ritual_ZN17QtVirtualKeyboard8Settings20setWclAutoCommitWordEb',
        wclAutoCommitWord,
    )

  @overload(bool)
  def setFullScreenMode(self, fullScreenMode: bool) -> None:
    """
    Calls Qt's 'void QtVirtualKeyboard::Settings::setFullScreenMode(bool
    fullScreenMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-settings.html#setFullScreenMode

    Parameters
    ----------

    fullScreenMode : bool
      Passed on as it is.
    """
    #  void QtVirtualKeyboard::Settings::setFullScreenMode(bool
    #      fullScreenMode)
    self.uglySide.call(
        'ritual_ZN17QtVirtualKeyboard8Settings17setFullScreenModeEb',
        fullScreenMode,
    )

  @overload(str)
  def setUserDataPath(self, userDataPath: str) -> None:
    """
    Calls Qt's 'void QtVirtualKeyboard::Settings::setUserDataPath(const
    QString &userDataPath)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-settings.html#setUserDataPath

    Parameters
    ----------

    userDataPath : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QtVirtualKeyboard::Settings::setUserDataPath(const QString
    #      &userDataPath)
    self.uglySide.call(
        'ritual_ZN17QtVirtualKeyboard8Settings15setUserDataPathERK7QString',
        userDataPath,
    )

  @overload(int)
  def setHwrTimeoutForAlphabetic(self, hwrTimeoutForAlphabetic: int) -> None:
    """
    Calls Qt's 'void
    QtVirtualKeyboard::Settings::setHwrTimeoutForAlphabetic(int
    hwrTimeoutForAlphabetic)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-settings.html

    Parameters
    ----------

    hwrTimeoutForAlphabetic : int
      Passed on as it is.
    """
    #  void QtVirtualKeyboard::Settings::setHwrTimeoutForAlphabetic(int
    #      hwrTimeoutForAlphabetic)
    self.uglySide.call(
        'ritual_ZN17QtVirtualKeyboard8Settings26setHwrTimeoutForAlphabeticE'
        'i',
        hwrTimeoutForAlphabetic,
    )

  @overload(int)
  def setHwrTimeoutForCjk(self, hwrTimeoutForCjk: int) -> None:
    """
    Calls Qt's 'void QtVirtualKeyboard::Settings::setHwrTimeoutForCjk(int
    hwrTimeoutForCjk)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-settings.html

    Parameters
    ----------

    hwrTimeoutForCjk : int
      Passed on as it is.
    """
    #  void QtVirtualKeyboard::Settings::setHwrTimeoutForCjk(int
    #      hwrTimeoutForCjk)
    self.uglySide.call(
        'ritual_ZN17QtVirtualKeyboard8Settings19setHwrTimeoutForCjkEi',
        hwrTimeoutForCjk,
    )

  @overload(bool)
  def setHandwritingModeDisabled(
      self,
      handwritingModeDisabled: bool,
  ) -> None:
    """
    Calls Qt's 'void
    QtVirtualKeyboard::Settings::setHandwritingModeDisabled(bool
    handwritingModeDisabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-settings.html

    Parameters
    ----------

    handwritingModeDisabled : bool
      Passed on as it is.
    """
    #  void QtVirtualKeyboard::Settings::setHandwritingModeDisabled(bool
    #      handwritingModeDisabled)
    self.uglySide.call(
        'ritual_ZN17QtVirtualKeyboard8Settings26setHandwritingModeDisabledE'
        'b',
        handwritingModeDisabled,
    )

  @overload(bool)
  def setDefaultInputMethodDisabled(
      self,
      defaultInputMethodDisabled: bool,
  ) -> None:
    """
    Calls Qt's 'void
    QtVirtualKeyboard::Settings::setDefaultInputMethodDisabled(bool
    defaultInputMethodDisabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-settings.html

    Parameters
    ----------

    defaultInputMethodDisabled : bool
      Passed on as it is.
    """
    #  void QtVirtualKeyboard::Settings::setDefaultInputMethodDisabled(bool
    #      defaultInputMethodDisabled)
    self.uglySide.call(
        'ritual_ZN17QtVirtualKeyboard8Settings29setDefaultInputMethodDisabl'
        'edEb',
        defaultInputMethodDisabled,
    )

  @overload(bool)
  def setDefaultDictionaryDisabled(
      self,
      defaultDictionaryDisabled: bool,
  ) -> None:
    """
    Calls Qt's 'void
    QtVirtualKeyboard::Settings::setDefaultDictionaryDisabled(bool
    defaultDictionaryDisabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-settings.html

    Parameters
    ----------

    defaultDictionaryDisabled : bool
      Passed on as it is.
    """
    #  void QtVirtualKeyboard::Settings::setDefaultDictionaryDisabled(bool
    #      defaultDictionaryDisabled)
    self.uglySide.call(
        'ritual_ZN17QtVirtualKeyboard8Settings28setDefaultDictionaryDisable'
        'dEb',
        defaultDictionaryDisabled,
    )

  @overload(QtVirtualKeyboard.KeyboardFunctionKeys)
  def setVisibleFunctionKeys(
      self,
      newVisibleFunctionKeys: QtVirtualKeyboard.KeyboardFunctionKeys,
  ) -> None:
    """
    Calls Qt's 'void
    QtVirtualKeyboard::Settings::setVisibleFunctionKeys(QtVirtualKeyboard::
    KeyboardFunctionKeys newVisibleFunctionKeys)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-settings.html

    Parameters
    ----------

    newVisibleFunctionKeys : QtVirtualKeyboard.KeyboardFunctionKeys
      Passed on as its number.
    """
    #  void QtVirtualKeyboard::Settings::setVisibleFunctionKeys(
    #      QtVirtualKeyboard::KeyboardFunctionKeys newVisibleFunctionKeys)
    self.uglySide.call(
        'ritual_ZN17QtVirtualKeyboard8Settings22setVisibleFunctionKeysE6QFl'
        'agsINS_19KeyboardFunctionKeyEE',
        newVisibleFunctionKeys.value,
    )

  @overload(bool)
  def setCloseOnReturn(self, enable: bool) -> None:
    """
    Calls Qt's 'void QtVirtualKeyboard::Settings::setCloseOnReturn(bool
    enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-settings.html#setCloseOnReturn

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QtVirtualKeyboard::Settings::setCloseOnReturn(bool enable)
    self.uglySide.call(
        'ritual_ZN17QtVirtualKeyboard8Settings16setCloseOnReturnEb', enable,
    )

  @overload(float)
  def setKeySoundVolume(self, volume: float) -> None:
    """
    Calls Qt's 'void QtVirtualKeyboard::Settings::setKeySoundVolume(qreal
    volume)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-settings.html#setKeySoundVolume

    Parameters
    ----------

    volume : float
      Passed on as it is.
    """
    #  void QtVirtualKeyboard::Settings::setKeySoundVolume(qreal volume)
    self.uglySide.call(
        'ritual_ZN17QtVirtualKeyboard8Settings17setKeySoundVolumeEd', volume,
    )

  @overload(bool)
  def setArrowKeyNavigationEnabled(
      self,
      arrowKeyNavigationEnabled: bool,
  ) -> None:
    """
    Calls Qt's 'void
    QtVirtualKeyboard::Settings::setArrowKeyNavigationEnabled(bool
    arrowKeyNavigationEnabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-settings.html

    Parameters
    ----------

    arrowKeyNavigationEnabled : bool
      Passed on as it is.
    """
    #  void QtVirtualKeyboard::Settings::setArrowKeyNavigationEnabled(bool
    #      arrowKeyNavigationEnabled)
    self.uglySide.call(
        'ritual_ZN17QtVirtualKeyboard8Settings28setArrowKeyNavigationEnable'
        'dEb',
        arrowKeyNavigationEnabled,
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
    'QtVirtualKeyboard::Settings::Settings(QObject *parent)', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-settings.html#Settings

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QtVirtualKeyboard::Settings::Settings(QObject *parent)
    self._noteCreation(Settings, lambda: Rituals.call(
        'ritual_ZN17QtVirtualKeyboard8SettingsC1EP7QObject',
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

  def resetStyleName(self) -> None:
    """
    Calls Qt's 'void QtVirtualKeyboard::Settings::resetStyleName()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-settings.html#resetStyleName
    """
    #  void QtVirtualKeyboard::Settings::resetStyleName()
    self.uglySide.call(
        'ritual_ZN17QtVirtualKeyboard8Settings14resetStyleNameEv',
    )

  def resetLocale(self) -> None:
    """
    Calls Qt's 'void QtVirtualKeyboard::Settings::resetLocale()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-settings.html#resetLocale
    """
    #  void QtVirtualKeyboard::Settings::resetLocale()
    self.uglySide.call(
        'ritual_ZN17QtVirtualKeyboard8Settings11resetLocaleEv',
    )

  def resetActiveLocales(self) -> None:
    """
    Calls Qt's 'void QtVirtualKeyboard::Settings::resetActiveLocales()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-settings.html#resetActiveLocales
    """
    #  void QtVirtualKeyboard::Settings::resetActiveLocales()
    self.uglySide.call(
        'ritual_ZN17QtVirtualKeyboard8Settings18resetActiveLocalesEv',
    )

  def resetLayoutPath(self) -> None:
    """
    Calls Qt's 'void QtVirtualKeyboard::Settings::resetLayoutPath()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-settings.html#resetLayoutPath
    """
    #  void QtVirtualKeyboard::Settings::resetLayoutPath()
    self.uglySide.call(
        'ritual_ZN17QtVirtualKeyboard8Settings15resetLayoutPathEv',
    )

  def resetWclAutoHideDelay(self) -> None:
    """
    Calls Qt's 'void QtVirtualKeyboard::Settings::resetWclAutoHideDelay()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-settings.html
    """
    #  void QtVirtualKeyboard::Settings::resetWclAutoHideDelay()
    self.uglySide.call(
        'ritual_ZN17QtVirtualKeyboard8Settings21resetWclAutoHideDelayEv',
    )

  def resetWclAlwaysVisible(self) -> None:
    """
    Calls Qt's 'void QtVirtualKeyboard::Settings::resetWclAlwaysVisible()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-settings.html
    """
    #  void QtVirtualKeyboard::Settings::resetWclAlwaysVisible()
    self.uglySide.call(
        'ritual_ZN17QtVirtualKeyboard8Settings21resetWclAlwaysVisibleEv',
    )

  def resetWclAutoCommitWord(self) -> None:
    """
    Calls Qt's 'void QtVirtualKeyboard::Settings::resetWclAutoCommitWord()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-settings.html
    """
    #  void QtVirtualKeyboard::Settings::resetWclAutoCommitWord()
    self.uglySide.call(
        'ritual_ZN17QtVirtualKeyboard8Settings22resetWclAutoCommitWordEv',
    )

  def resetFullScreenMode(self) -> None:
    """
    Calls Qt's 'void QtVirtualKeyboard::Settings::resetFullScreenMode()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-settings.html
    """
    #  void QtVirtualKeyboard::Settings::resetFullScreenMode()
    self.uglySide.call(
        'ritual_ZN17QtVirtualKeyboard8Settings19resetFullScreenModeEv',
    )

  def resetUserDataPath(self) -> None:
    """
    Calls Qt's 'void QtVirtualKeyboard::Settings::resetUserDataPath()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-settings.html#resetUserDataPath
    """
    #  void QtVirtualKeyboard::Settings::resetUserDataPath()
    self.uglySide.call(
        'ritual_ZN17QtVirtualKeyboard8Settings17resetUserDataPathEv',
    )

  def resetHwrTimeoutForAlphabetic(self) -> None:
    """
    Calls Qt's 'void
    QtVirtualKeyboard::Settings::resetHwrTimeoutForAlphabetic()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-settings.html
    """
    #  void QtVirtualKeyboard::Settings::resetHwrTimeoutForAlphabetic()
    self.uglySide.call(
        'ritual_ZN17QtVirtualKeyboard8Settings28resetHwrTimeoutForAlphabeti'
        'cEv',
    )

  def resetHwrTimeoutForCjk(self) -> None:
    """
    Calls Qt's 'void QtVirtualKeyboard::Settings::resetHwrTimeoutForCjk()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-settings.html
    """
    #  void QtVirtualKeyboard::Settings::resetHwrTimeoutForCjk()
    self.uglySide.call(
        'ritual_ZN17QtVirtualKeyboard8Settings21resetHwrTimeoutForCjkEv',
    )

  def resetInputMethodHints(self) -> None:
    """
    Calls Qt's 'void QtVirtualKeyboard::Settings::resetInputMethodHints()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-settings.html
    """
    #  void QtVirtualKeyboard::Settings::resetInputMethodHints()
    self.uglySide.call(
        'ritual_ZN17QtVirtualKeyboard8Settings21resetInputMethodHintsEv',
    )

  def resetHandwritingModeDisabled(self) -> None:
    """
    Calls Qt's 'void
    QtVirtualKeyboard::Settings::resetHandwritingModeDisabled()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-settings.html
    """
    #  void QtVirtualKeyboard::Settings::resetHandwritingModeDisabled()
    self.uglySide.call(
        'ritual_ZN17QtVirtualKeyboard8Settings28resetHandwritingModeDisable'
        'dEv',
    )

  def resetDefaultInputMethodDisabled(self) -> None:
    """
    Calls Qt's 'void
    QtVirtualKeyboard::Settings::resetDefaultInputMethodDisabled()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-settings.html
    """
    #  void QtVirtualKeyboard::Settings::resetDefaultInputMethodDisabled()
    self.uglySide.call(
        'ritual_ZN17QtVirtualKeyboard8Settings31resetDefaultInputMethodDisa'
        'bledEv',
    )

  def resetDefaultDictionaryDisabled(self) -> None:
    """
    Calls Qt's 'void
    QtVirtualKeyboard::Settings::resetDefaultDictionaryDisabled()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-settings.html
    """
    #  void QtVirtualKeyboard::Settings::resetDefaultDictionaryDisabled()
    self.uglySide.call(
        'ritual_ZN17QtVirtualKeyboard8Settings30resetDefaultDictionaryDisab'
        'ledEv',
    )

  def resetVisibleFunctionKeys(self) -> None:
    """
    Calls Qt's 'void
    QtVirtualKeyboard::Settings::resetVisibleFunctionKeys()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-settings.html
    """
    #  void QtVirtualKeyboard::Settings::resetVisibleFunctionKeys()
    self.uglySide.call(
        'ritual_ZN17QtVirtualKeyboard8Settings24resetVisibleFunctionKeysEv',
    )

  def resetCloseOnReturn(self) -> None:
    """
    Calls Qt's 'void QtVirtualKeyboard::Settings::resetCloseOnReturn()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-settings.html#resetCloseOnReturn
    """
    #  void QtVirtualKeyboard::Settings::resetCloseOnReturn()
    self.uglySide.call(
        'ritual_ZN17QtVirtualKeyboard8Settings18resetCloseOnReturnEv',
    )

  def resetKeySoundVolume(self) -> None:
    """
    Calls Qt's 'void QtVirtualKeyboard::Settings::resetKeySoundVolume()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-settings.html
    """
    #  void QtVirtualKeyboard::Settings::resetKeySoundVolume()
    self.uglySide.call(
        'ritual_ZN17QtVirtualKeyboard8Settings19resetKeySoundVolumeEv',
    )

  def resetArrowKeyNavigationEnabled(self) -> None:
    """
    Calls Qt's 'void
    QtVirtualKeyboard::Settings::resetArrowKeyNavigationEnabled()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-settings.html
    """
    #  void QtVirtualKeyboard::Settings::resetArrowKeyNavigationEnabled()
    self.uglySide.call(
        'ritual_ZN17QtVirtualKeyboard8Settings30resetArrowKeyNavigationEnab'
        'ledEv',
    )

  def styleChanged(self) -> None:
    """
    Calls Qt's 'void QtVirtualKeyboard::Settings::styleChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-settings.html#styleChanged
    """
    #  void QtVirtualKeyboard::Settings::styleChanged()
    self.uglySide.call(
        'ritual_ZN17QtVirtualKeyboard8Settings12styleChangedEv',
    )

  def styleNameChanged(self) -> None:
    """
    Calls Qt's 'void QtVirtualKeyboard::Settings::styleNameChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-settings.html#styleNameChanged
    """
    #  void QtVirtualKeyboard::Settings::styleNameChanged()
    self.uglySide.call(
        'ritual_ZN17QtVirtualKeyboard8Settings16styleNameChangedEv',
    )

  def requestResetStyle(self) -> None:
    """
    Calls Qt's 'void QtVirtualKeyboard::Settings::requestResetStyle()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-settings.html#requestResetStyle
    """
    #  void QtVirtualKeyboard::Settings::requestResetStyle()
    self.uglySide.call(
        'ritual_ZN17QtVirtualKeyboard8Settings17requestResetStyleEv',
    )

  def localeChanged(self) -> None:
    """
    Calls Qt's 'void QtVirtualKeyboard::Settings::localeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-settings.html#localeChanged
    """
    #  void QtVirtualKeyboard::Settings::localeChanged()
    self.uglySide.call(
        'ritual_ZN17QtVirtualKeyboard8Settings13localeChangedEv',
    )

  def availableLocalesChanged(self) -> None:
    """
    Calls Qt's 'void QtVirtualKeyboard::Settings::availableLocalesChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-settings.html
    """
    #  void QtVirtualKeyboard::Settings::availableLocalesChanged()
    self.uglySide.call(
        'ritual_ZN17QtVirtualKeyboard8Settings23availableLocalesChangedEv',
    )

  def activeLocalesChanged(self) -> None:
    """
    Calls Qt's 'void QtVirtualKeyboard::Settings::activeLocalesChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-settings.html
    """
    #  void QtVirtualKeyboard::Settings::activeLocalesChanged()
    self.uglySide.call(
        'ritual_ZN17QtVirtualKeyboard8Settings20activeLocalesChangedEv',
    )

  def layoutPathChanged(self) -> None:
    """
    Calls Qt's 'void QtVirtualKeyboard::Settings::layoutPathChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-settings.html#layoutPathChanged
    """
    #  void QtVirtualKeyboard::Settings::layoutPathChanged()
    self.uglySide.call(
        'ritual_ZN17QtVirtualKeyboard8Settings17layoutPathChangedEv',
    )

  def wclAutoHideDelayChanged(self) -> None:
    """
    Calls Qt's 'void QtVirtualKeyboard::Settings::wclAutoHideDelayChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-settings.html
    """
    #  void QtVirtualKeyboard::Settings::wclAutoHideDelayChanged()
    self.uglySide.call(
        'ritual_ZN17QtVirtualKeyboard8Settings23wclAutoHideDelayChangedEv',
    )

  def wclAlwaysVisibleChanged(self) -> None:
    """
    Calls Qt's 'void QtVirtualKeyboard::Settings::wclAlwaysVisibleChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-settings.html
    """
    #  void QtVirtualKeyboard::Settings::wclAlwaysVisibleChanged()
    self.uglySide.call(
        'ritual_ZN17QtVirtualKeyboard8Settings23wclAlwaysVisibleChangedEv',
    )

  def wclAutoCommitWordChanged(self) -> None:
    """
    Calls Qt's 'void
    QtVirtualKeyboard::Settings::wclAutoCommitWordChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-settings.html
    """
    #  void QtVirtualKeyboard::Settings::wclAutoCommitWordChanged()
    self.uglySide.call(
        'ritual_ZN17QtVirtualKeyboard8Settings24wclAutoCommitWordChangedEv',
    )

  def fullScreenModeChanged(self) -> None:
    """
    Calls Qt's 'void QtVirtualKeyboard::Settings::fullScreenModeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-settings.html
    """
    #  void QtVirtualKeyboard::Settings::fullScreenModeChanged()
    self.uglySide.call(
        'ritual_ZN17QtVirtualKeyboard8Settings21fullScreenModeChangedEv',
    )

  def userDataPathChanged(self) -> None:
    """
    Calls Qt's 'void QtVirtualKeyboard::Settings::userDataPathChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-settings.html
    """
    #  void QtVirtualKeyboard::Settings::userDataPathChanged()
    self.uglySide.call(
        'ritual_ZN17QtVirtualKeyboard8Settings19userDataPathChangedEv',
    )

  def userDataReset(self) -> None:
    """
    Calls Qt's 'void QtVirtualKeyboard::Settings::userDataReset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-settings.html#userDataReset
    """
    #  void QtVirtualKeyboard::Settings::userDataReset()
    self.uglySide.call(
        'ritual_ZN17QtVirtualKeyboard8Settings13userDataResetEv',
    )

  def hwrTimeoutForAlphabeticChanged(self) -> None:
    """
    Calls Qt's 'void
    QtVirtualKeyboard::Settings::hwrTimeoutForAlphabeticChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-settings.html
    """
    #  void QtVirtualKeyboard::Settings::hwrTimeoutForAlphabeticChanged()
    self.uglySide.call(
        'ritual_ZN17QtVirtualKeyboard8Settings30hwrTimeoutForAlphabeticChan'
        'gedEv',
    )

  def hwrTimeoutForCjkChanged(self) -> None:
    """
    Calls Qt's 'void QtVirtualKeyboard::Settings::hwrTimeoutForCjkChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-settings.html
    """
    #  void QtVirtualKeyboard::Settings::hwrTimeoutForCjkChanged()
    self.uglySide.call(
        'ritual_ZN17QtVirtualKeyboard8Settings23hwrTimeoutForCjkChangedEv',
    )

  def inputMethodHintsChanged(self) -> None:
    """
    Calls Qt's 'void QtVirtualKeyboard::Settings::inputMethodHintsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-settings.html
    """
    #  void QtVirtualKeyboard::Settings::inputMethodHintsChanged()
    self.uglySide.call(
        'ritual_ZN17QtVirtualKeyboard8Settings23inputMethodHintsChangedEv',
    )

  def handwritingModeDisabledChanged(self) -> None:
    """
    Calls Qt's 'void
    QtVirtualKeyboard::Settings::handwritingModeDisabledChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-settings.html
    """
    #  void QtVirtualKeyboard::Settings::handwritingModeDisabledChanged()
    self.uglySide.call(
        'ritual_ZN17QtVirtualKeyboard8Settings30handwritingModeDisabledChan'
        'gedEv',
    )

  def defaultInputMethodDisabledChanged(self) -> None:
    """
    Calls Qt's 'void
    QtVirtualKeyboard::Settings::defaultInputMethodDisabledChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-settings.html
    """
    #  void QtVirtualKeyboard::Settings::defaultInputMethodDisabledChanged()
    self.uglySide.call(
        'ritual_ZN17QtVirtualKeyboard8Settings33defaultInputMethodDisabledC'
        'hangedEv',
    )

  def defaultDictionaryDisabledChanged(self) -> None:
    """
    Calls Qt's 'void
    QtVirtualKeyboard::Settings::defaultDictionaryDisabledChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-settings.html
    """
    #  void QtVirtualKeyboard::Settings::defaultDictionaryDisabledChanged()
    self.uglySide.call(
        'ritual_ZN17QtVirtualKeyboard8Settings32defaultDictionaryDisabledCh'
        'angedEv',
    )

  def visibleFunctionKeysChanged(self) -> None:
    """
    Calls Qt's 'void
    QtVirtualKeyboard::Settings::visibleFunctionKeysChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-settings.html
    """
    #  void QtVirtualKeyboard::Settings::visibleFunctionKeysChanged()
    self.uglySide.call(
        'ritual_ZN17QtVirtualKeyboard8Settings26visibleFunctionKeysChangedE'
        'v',
    )

  def closeOnReturnChanged(self) -> None:
    """
    Calls Qt's 'void QtVirtualKeyboard::Settings::closeOnReturnChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-settings.html
    """
    #  void QtVirtualKeyboard::Settings::closeOnReturnChanged()
    self.uglySide.call(
        'ritual_ZN17QtVirtualKeyboard8Settings20closeOnReturnChangedEv',
    )

  def keySoundVolumeChanged(self) -> None:
    """
    Calls Qt's 'void QtVirtualKeyboard::Settings::keySoundVolumeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-settings.html
    """
    #  void QtVirtualKeyboard::Settings::keySoundVolumeChanged()
    self.uglySide.call(
        'ritual_ZN17QtVirtualKeyboard8Settings21keySoundVolumeChangedEv',
    )

  def arrowKeyNavigationEnabledChanged(self) -> None:
    """
    Calls Qt's 'void
    QtVirtualKeyboard::Settings::arrowKeyNavigationEnabledChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-settings.html
    """
    #  void QtVirtualKeyboard::Settings::arrowKeyNavigationEnabledChanged()
    self.uglySide.call(
        'ritual_ZN17QtVirtualKeyboard8Settings32arrowKeyNavigationEnabledCh'
        'angedEv',
    )

  @staticmethod
  def setInputMethodHints(*__, **_) -> Never:
    """
    Qt's 'void QtVirtualKeyboard::Settings::setInputMethodHints(const
    Qt::InputMethodHints &inputMethodHints)': takes a type Python has no way
    to hand over yet.
    """
    raise NotImplementedError(
        "'QtVirtualKeyboard.Settings.setInputMethodHints' has no cute "
        "function yet. Qt's 'void "
        "QtVirtualKeyboard::Settings::setInputMethodHints(const "
        "Qt::InputMethodHints &inputMethodHints)': takes a type Python has "
        "no way to hand over yet.")
