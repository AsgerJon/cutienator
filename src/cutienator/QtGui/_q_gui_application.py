"""
QGuiApplication binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/qguiapplication.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QCoreApplication, QList, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QEvent, QMetaObject, QPoint
  from . import QClipboard, QCursor, QFont, QIcon, QInputMethod, QPalette
  from . import QScreen, QStyleHints, QWindow
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QCursor = WAIT['QCursor']
  QEvent = WAIT['QEvent']
  QFont = WAIT['QFont']
  QIcon = WAIT['QIcon']
  QPalette = WAIT['QPalette']
  QPoint = WAIT['QPoint']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QGuiApplication(QCoreApplication):
  """
  The cute side of Qt's QGuiApplication: a plain Python object standing in
  front of one C++ QGuiApplication.

  It is built on the cute 'QCoreApplication', as Qt's QGuiApplication is
  built on Qt's QCoreApplication, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QGuiApplication that has a ritual and that Python
  can call so far, 53 names in all: 'metaObject', 'tr',
  'setApplicationDisplayName', 'applicationDisplayName', 'setBadgeNumber',
  'setDesktopFileName', 'desktopFileName', 'allWindows', 'topLevelWindows',
  'topLevelAt', 'setWindowIcon', 'windowIcon', 'platformName', 'modalWindow',
  'focusWindow', 'focusObject', 'primaryScreen', 'screens', 'screenAt',
  'devicePixelRatio', 'overrideCursor', 'setOverrideCursor',
  'changeOverrideCursor', 'restoreOverrideCursor', 'font', 'setFont',
  'clipboard', 'palette', 'setPalette', 'keyboardModifiers',
  'queryKeyboardModifiers', 'mouseButtons', 'setLayoutDirection',
  'layoutDirection', 'isRightToLeft', 'isLeftToRight', 'styleHints',
  'setDesktopSettingsAware', 'desktopSettingsAware', 'inputMethod',
  'setQuitOnLastWindowClosed', 'quitOnLastWindowClosed', 'applicationState',
  'setHighDpiScaleFactorRoundingPolicy', 'highDpiScaleFactorRoundingPolicy',
  'exec', 'notify', 'isSessionRestored', 'sessionId', 'sessionKey',
  'isSavingSession', 'sync', 'event'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QGuiApplication::~QGuiApplication()': the destructor: Python never
    removes a C++ QGuiApplication.

  What has no ritual
  ------------------

  28 of the 83 functions Qt declares: 14 a signal; 9 takes or gives a type
  that cannot be passed yet; 2 a template; 2 forbidden; 1 declared and
  nowhere to be found.

  What to expect
  --------------

  - The C++ QGuiApplication is created by 'QGuiApplication(...)' at once,
    since nearly every other object of Qt can only be made after it.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGuiApplication.
  - Qt tells when it has removed the C++ QGuiApplication. Every call on the
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
    Calls Qt's 'QString QGuiApplication::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qguiapplication.html#tr

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
    #  QString QGuiApplication::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN15QGuiApplication2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(str)
  def setApplicationDisplayName(name: str) -> None:
    """
    Calls Qt's 'void QGuiApplication::setApplicationDisplayName(const QString
    &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qguiapplication.html#setApplicationDisplayName

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QGuiApplication::setApplicationDisplayName(const QString &name)
    Rituals.call(
        'ritual_ZN15QGuiApplication25setApplicationDisplayNameERK7QString',
        name,
    )

  @staticmethod
  def applicationDisplayName() -> str:
    """
    Calls Qt's 'QString QGuiApplication::applicationDisplayName()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qguiapplication.html#applicationDisplayName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QGuiApplication::applicationDisplayName()
    return Rituals.call(
        'ritual_ZN15QGuiApplication22applicationDisplayNameEv',
    )

  @staticmethod
  @overload(str)
  def setDesktopFileName(name: str) -> None:
    """
    Calls Qt's 'void QGuiApplication::setDesktopFileName(const QString
    &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qguiapplication.html#setDesktopFileName

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QGuiApplication::setDesktopFileName(const QString &name)
    Rituals.call(
        'ritual_ZN15QGuiApplication18setDesktopFileNameERK7QString', name,
    )

  @staticmethod
  def desktopFileName() -> str:
    """
    Calls Qt's 'QString QGuiApplication::desktopFileName()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qguiapplication.html#desktopFileName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QGuiApplication::desktopFileName()
    return Rituals.call('ritual_ZN15QGuiApplication15desktopFileNameEv')

  @staticmethod
  def allWindows() -> QList[QWindow]:
    """
    Calls Qt's 'QWindowList QGuiApplication::allWindows()'.

    Qt's own words: https://doc.qt.io/qt-6/qguiapplication.html#allWindows

    Returns
    -------

    QList[QWindow]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QWindowList QGuiApplication::allWindows()
    address = Rituals.call('ritual_ZN15QGuiApplication10allWindowsEv')
    from . import QWindow
    return QList[QWindow]._cuteOwning(address)

  @staticmethod
  def topLevelWindows() -> QList[QWindow]:
    """
    Calls Qt's 'QWindowList QGuiApplication::topLevelWindows()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qguiapplication.html#topLevelWindows

    Returns
    -------

    QList[QWindow]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QWindowList QGuiApplication::topLevelWindows()
    address = Rituals.call('ritual_ZN15QGuiApplication15topLevelWindowsEv')
    from . import QWindow
    return QList[QWindow]._cuteOwning(address)

  @staticmethod
  @overload(QPoint)
  def topLevelAt(pos: QPoint) -> Optional[QWindow]:
    """
    Calls Qt's 'QWindow *QGuiApplication::topLevelAt(const QPoint &pos)'.

    Qt's own words: https://doc.qt.io/qt-6/qguiapplication.html#topLevelAt

    Parameters
    ----------

    pos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    Returns
    -------

    Optional[QWindow]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWindow *QGuiApplication::topLevelAt(const QPoint &pos)
    address = Rituals.call(
        'ritual_ZN15QGuiApplication10topLevelAtERK6QPoint',
        CuteMixin._valueOf(pos),
    )
    from . import QWindow
    return QWindow._cuteAt(address)

  @staticmethod
  @overload(QIcon)
  def setWindowIcon(icon: QIcon) -> None:
    """
    Calls Qt's 'void QGuiApplication::setWindowIcon(const QIcon &icon)'.

    Qt's own words: https://doc.qt.io/qt-6/qguiapplication.html#setWindowIcon

    Parameters
    ----------

    icon : QIcon
      Passed on as a value: Qt reads the C++ QIcon, which stays Python's own.
    """
    #  void QGuiApplication::setWindowIcon(const QIcon &icon)
    Rituals.call(
        'ritual_ZN15QGuiApplication13setWindowIconERK5QIcon',
        CuteMixin._valueOf(icon),
    )

  @staticmethod
  def windowIcon() -> QIcon:
    """
    Calls Qt's 'QIcon QGuiApplication::windowIcon()'.

    Qt's own words: https://doc.qt.io/qt-6/qguiapplication.html#windowIcon

    Returns
    -------

    QIcon
      A new cute QIcon around the copy Qt gave back. Python owns it.
    """
    #  QIcon QGuiApplication::windowIcon()
    address = Rituals.call('ritual_ZN15QGuiApplication10windowIconEv')
    from . import QIcon
    return QIcon._cuteOwning(address)

  @staticmethod
  def platformName() -> str:
    """
    Calls Qt's 'QString QGuiApplication::platformName()'.

    Qt's own words: https://doc.qt.io/qt-6/qguiapplication.html#platformName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QGuiApplication::platformName()
    return Rituals.call('ritual_ZN15QGuiApplication12platformNameEv')

  @staticmethod
  def modalWindow() -> Optional[QWindow]:
    """
    Calls Qt's 'QWindow *QGuiApplication::modalWindow()'.

    Qt's own words: https://doc.qt.io/qt-6/qguiapplication.html#modalWindow

    Returns
    -------

    Optional[QWindow]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWindow *QGuiApplication::modalWindow()
    address = Rituals.call('ritual_ZN15QGuiApplication11modalWindowEv')
    from . import QWindow
    return QWindow._cuteAt(address)

  @staticmethod
  def focusWindow() -> Optional[QWindow]:
    """
    Calls Qt's 'QWindow *QGuiApplication::focusWindow()'.

    Qt's own words: https://doc.qt.io/qt-6/qguiapplication.html#focusWindow

    Returns
    -------

    Optional[QWindow]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWindow *QGuiApplication::focusWindow()
    address = Rituals.call('ritual_ZN15QGuiApplication11focusWindowEv')
    from . import QWindow
    return QWindow._cuteAt(address)

  @staticmethod
  def focusObject() -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QGuiApplication::focusObject()'.

    Qt's own words: https://doc.qt.io/qt-6/qguiapplication.html#focusObject

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QGuiApplication::focusObject()
    address = Rituals.call('ritual_ZN15QGuiApplication11focusObjectEv')
    return QObject._cuteAt(address)

  @staticmethod
  def primaryScreen() -> Optional[QScreen]:
    """
    Calls Qt's 'QScreen *QGuiApplication::primaryScreen()'.

    Qt's own words: https://doc.qt.io/qt-6/qguiapplication.html#primaryScreen

    Returns
    -------

    Optional[QScreen]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QScreen *QGuiApplication::primaryScreen()
    address = Rituals.call('ritual_ZN15QGuiApplication13primaryScreenEv')
    from . import QScreen
    return QScreen._cuteAt(address)

  @staticmethod
  def screens() -> QList[QScreen]:
    """
    Calls Qt's 'QList<QScreen *> QGuiApplication::screens()'.

    Qt's own words: https://doc.qt.io/qt-6/qguiapplication.html#screens

    Returns
    -------

    QList[QScreen]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QScreen *> QGuiApplication::screens()
    address = Rituals.call('ritual_ZN15QGuiApplication7screensEv')
    from . import QScreen
    return QList[QScreen]._cuteOwning(address)

  @staticmethod
  @overload(QPoint)
  def screenAt(point: QPoint) -> Optional[QScreen]:
    """
    Calls Qt's 'QScreen *QGuiApplication::screenAt(const QPoint &point)'.

    Qt's own words: https://doc.qt.io/qt-6/qguiapplication.html#screenAt

    Parameters
    ----------

    point : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    Returns
    -------

    Optional[QScreen]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QScreen *QGuiApplication::screenAt(const QPoint &point)
    address = Rituals.call(
        'ritual_ZN15QGuiApplication8screenAtERK6QPoint',
        CuteMixin._valueOf(point),
    )
    from . import QScreen
    return QScreen._cuteAt(address)

  @staticmethod
  def overrideCursor() -> Optional[QCursor]:
    """
    Calls Qt's 'QCursor *QGuiApplication::overrideCursor()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qguiapplication.html#overrideCursor

    Returns
    -------

    Optional[QCursor]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCursor *QGuiApplication::overrideCursor()
    address = Rituals.call('ritual_ZN15QGuiApplication14overrideCursorEv')
    from . import QCursor
    return QCursor._cuteAt(address)

  @staticmethod
  @overload(QCursor)
  def setOverrideCursor(a0: QCursor) -> None:
    """
    Calls Qt's 'void QGuiApplication::setOverrideCursor(const QCursor &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qguiapplication.html#setOverrideCursor

    Parameters
    ----------

    a0 : QCursor
      Passed on as a value: Qt reads the C++ QCursor, which stays Python's
      own.
    """
    #  void QGuiApplication::setOverrideCursor(const QCursor &a0)
    Rituals.call(
        'ritual_ZN15QGuiApplication17setOverrideCursorERK7QCursor',
        CuteMixin._valueOf(a0),
    )

  @staticmethod
  @overload(QCursor)
  def changeOverrideCursor(a0: QCursor) -> None:
    """
    Calls Qt's 'void QGuiApplication::changeOverrideCursor(const QCursor
    &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qguiapplication.html#changeOverrideCursor

    Parameters
    ----------

    a0 : QCursor
      Passed on as a value: Qt reads the C++ QCursor, which stays Python's
      own.
    """
    #  void QGuiApplication::changeOverrideCursor(const QCursor &a0)
    Rituals.call(
        'ritual_ZN15QGuiApplication20changeOverrideCursorERK7QCursor',
        CuteMixin._valueOf(a0),
    )

  @staticmethod
  def restoreOverrideCursor() -> None:
    """
    Calls Qt's 'void QGuiApplication::restoreOverrideCursor()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qguiapplication.html#restoreOverrideCursor
    """
    #  void QGuiApplication::restoreOverrideCursor()
    Rituals.call('ritual_ZN15QGuiApplication21restoreOverrideCursorEv')

  @staticmethod
  def font() -> QFont:
    """
    Calls Qt's 'QFont QGuiApplication::font()'.

    Qt's own words: https://doc.qt.io/qt-6/qguiapplication.html#font

    Returns
    -------

    QFont
      A new cute QFont around the copy Qt gave back. Python owns it.
    """
    #  QFont QGuiApplication::font()
    address = Rituals.call('ritual_ZN15QGuiApplication4fontEv')
    from . import QFont
    return QFont._cuteOwning(address)

  @staticmethod
  @overload(QFont)
  def setFont(a0: QFont) -> None:
    """
    Calls Qt's 'void QGuiApplication::setFont(const QFont &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qguiapplication.html#setFont

    Parameters
    ----------

    a0 : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.
    """
    #  void QGuiApplication::setFont(const QFont &a0)
    Rituals.call(
        'ritual_ZN15QGuiApplication7setFontERK5QFont',
        CuteMixin._valueOf(a0),
    )

  @staticmethod
  def clipboard() -> Optional[QClipboard]:
    """
    Calls Qt's 'QClipboard *QGuiApplication::clipboard()'.

    Qt's own words: https://doc.qt.io/qt-6/qguiapplication.html#clipboard

    Returns
    -------

    Optional[QClipboard]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QClipboard *QGuiApplication::clipboard()
    address = Rituals.call('ritual_ZN15QGuiApplication9clipboardEv')
    from . import QClipboard
    return QClipboard._cuteAt(address)

  @staticmethod
  def palette() -> QPalette:
    """
    Calls Qt's 'QPalette QGuiApplication::palette()'.

    Qt's own words: https://doc.qt.io/qt-6/qguiapplication.html#palette

    Returns
    -------

    QPalette
      A new cute QPalette around the copy Qt gave back. Python owns it.
    """
    #  QPalette QGuiApplication::palette()
    address = Rituals.call('ritual_ZN15QGuiApplication7paletteEv')
    from . import QPalette
    return QPalette._cuteOwning(address)

  @staticmethod
  @overload(QPalette)
  def setPalette(pal: QPalette) -> None:
    """
    Calls Qt's 'void QGuiApplication::setPalette(const QPalette &pal)'.

    Qt's own words: https://doc.qt.io/qt-6/qguiapplication.html#setPalette

    Parameters
    ----------

    pal : QPalette
      Passed on as a value: Qt reads the C++ QPalette, which stays Python's
      own.
    """
    #  void QGuiApplication::setPalette(const QPalette &pal)
    Rituals.call(
        'ritual_ZN15QGuiApplication10setPaletteERK8QPalette',
        CuteMixin._valueOf(pal),
    )

  @staticmethod
  def keyboardModifiers() -> Qt.KeyboardModifiers:
    """
    Calls Qt's 'Qt::KeyboardModifiers QGuiApplication::keyboardModifiers()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qguiapplication.html#keyboardModifiers

    Returns
    -------

    Qt.KeyboardModifiers
      The value standing for the combination Qt gave back.
    """
    #  Qt::KeyboardModifiers QGuiApplication::keyboardModifiers()
    return Qt.KeyboardModifiers(Rituals.call(
        'ritual_ZN15QGuiApplication17keyboardModifiersEv',
    ))

  @staticmethod
  def queryKeyboardModifiers() -> Qt.KeyboardModifiers:
    """
    Calls Qt's 'Qt::KeyboardModifiers
    QGuiApplication::queryKeyboardModifiers()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qguiapplication.html#queryKeyboardModifiers

    Returns
    -------

    Qt.KeyboardModifiers
      The value standing for the combination Qt gave back.
    """
    #  Qt::KeyboardModifiers QGuiApplication::queryKeyboardModifiers()
    return Qt.KeyboardModifiers(Rituals.call(
        'ritual_ZN15QGuiApplication22queryKeyboardModifiersEv',
    ))

  @staticmethod
  def mouseButtons() -> Qt.MouseButtons:
    """
    Calls Qt's 'Qt::MouseButtons QGuiApplication::mouseButtons()'.

    Qt's own words: https://doc.qt.io/qt-6/qguiapplication.html#mouseButtons

    Returns
    -------

    Qt.MouseButtons
      The value standing for the combination Qt gave back.
    """
    #  Qt::MouseButtons QGuiApplication::mouseButtons()
    return Qt.MouseButtons(Rituals.call(
        'ritual_ZN15QGuiApplication12mouseButtonsEv',
    ))

  @staticmethod
  @overload(Qt.LayoutDirection)
  def setLayoutDirection(direction: Qt.LayoutDirection) -> None:
    """
    Calls Qt's 'void QGuiApplication::setLayoutDirection(Qt::LayoutDirection
    direction)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qguiapplication.html#setLayoutDirection

    Parameters
    ----------

    direction : Qt.LayoutDirection
      Passed on as its number.
    """
    #  void QGuiApplication::setLayoutDirection(Qt::LayoutDirection
    #      direction)
    Rituals.call(
        'ritual_ZN15QGuiApplication18setLayoutDirectionEN2Qt15LayoutDirecti'
        'onE',
        direction.value,
    )

  @staticmethod
  def layoutDirection() -> Qt.LayoutDirection:
    """
    Calls Qt's 'Qt::LayoutDirection QGuiApplication::layoutDirection()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qguiapplication.html#layoutDirection

    Returns
    -------

    Qt.LayoutDirection
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt.LayoutDirection(number)' gives.
    """
    #  Qt::LayoutDirection QGuiApplication::layoutDirection()
    return Qt.LayoutDirection(Rituals.call(
        'ritual_ZN15QGuiApplication15layoutDirectionEv',
    ))

  @staticmethod
  def isRightToLeft() -> bool:
    """
    Calls Qt's 'bool QGuiApplication::isRightToLeft()'.

    Qt's own words: https://doc.qt.io/qt-6/qguiapplication.html#isRightToLeft
    """
    #  bool QGuiApplication::isRightToLeft()
    return Rituals.call('ritual_ZN15QGuiApplication13isRightToLeftEv')

  @staticmethod
  def isLeftToRight() -> bool:
    """
    Calls Qt's 'bool QGuiApplication::isLeftToRight()'.

    Qt's own words: https://doc.qt.io/qt-6/qguiapplication.html#isLeftToRight
    """
    #  bool QGuiApplication::isLeftToRight()
    return Rituals.call('ritual_ZN15QGuiApplication13isLeftToRightEv')

  @staticmethod
  def styleHints() -> Optional[QStyleHints]:
    """
    Calls Qt's 'QStyleHints *QGuiApplication::styleHints()'.

    Qt's own words: https://doc.qt.io/qt-6/qguiapplication.html#styleHints

    Returns
    -------

    Optional[QStyleHints]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QStyleHints *QGuiApplication::styleHints()
    address = Rituals.call('ritual_ZN15QGuiApplication10styleHintsEv')
    from . import QStyleHints
    return QStyleHints._cuteAt(address)

  @staticmethod
  @overload(bool)
  def setDesktopSettingsAware(on: bool) -> None:
    """
    Calls Qt's 'void QGuiApplication::setDesktopSettingsAware(bool on)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qguiapplication.html#setDesktopSettingsAware

    Parameters
    ----------

    on : bool
      Passed on as it is.
    """
    #  void QGuiApplication::setDesktopSettingsAware(bool on)
    Rituals.call('ritual_ZN15QGuiApplication23setDesktopSettingsAwareEb', on)

  @staticmethod
  def desktopSettingsAware() -> bool:
    """
    Calls Qt's 'bool QGuiApplication::desktopSettingsAware()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qguiapplication.html#desktopSettingsAware
    """
    #  bool QGuiApplication::desktopSettingsAware()
    return Rituals.call('ritual_ZN15QGuiApplication20desktopSettingsAwareEv')

  @staticmethod
  def inputMethod() -> Optional[QInputMethod]:
    """
    Calls Qt's 'QInputMethod *QGuiApplication::inputMethod()'.

    Qt's own words: https://doc.qt.io/qt-6/qguiapplication.html#inputMethod

    Returns
    -------

    Optional[QInputMethod]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QInputMethod *QGuiApplication::inputMethod()
    address = Rituals.call('ritual_ZN15QGuiApplication11inputMethodEv')
    from . import QInputMethod
    return QInputMethod._cuteAt(address)

  @staticmethod
  @overload(bool)
  def setQuitOnLastWindowClosed(quit: bool) -> None:
    """
    Calls Qt's 'void QGuiApplication::setQuitOnLastWindowClosed(bool quit)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qguiapplication.html#setQuitOnLastWindowClosed

    Parameters
    ----------

    quit : bool
      Passed on as it is.
    """
    #  void QGuiApplication::setQuitOnLastWindowClosed(bool quit)
    Rituals.call(
        'ritual_ZN15QGuiApplication25setQuitOnLastWindowClosedEb', quit,
    )

  @staticmethod
  def quitOnLastWindowClosed() -> bool:
    """
    Calls Qt's 'bool QGuiApplication::quitOnLastWindowClosed()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qguiapplication.html#quitOnLastWindowClosed
    """
    #  bool QGuiApplication::quitOnLastWindowClosed()
    return Rituals.call(
        'ritual_ZN15QGuiApplication22quitOnLastWindowClosedEv',
    )

  @staticmethod
  def applicationState() -> Qt.ApplicationState:
    """
    Calls Qt's 'Qt::ApplicationState QGuiApplication::applicationState()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qguiapplication.html#applicationState

    Returns
    -------

    Qt.ApplicationState
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt.ApplicationState(number)' gives.
    """
    #  Qt::ApplicationState QGuiApplication::applicationState()
    return Qt.ApplicationState(Rituals.call(
        'ritual_ZN15QGuiApplication16applicationStateEv',
    ))

  @staticmethod
  @overload(Qt.HighDpiScaleFactorRoundingPolicy)
  def setHighDpiScaleFactorRoundingPolicy(
      policy: Qt.HighDpiScaleFactorRoundingPolicy,
  ) -> None:
    """
    Calls Qt's 'void
    QGuiApplication::setHighDpiScaleFactorRoundingPolicy(Qt::
    HighDpiScaleFactorRoundingPolicy policy)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qguiapplication.html

    Parameters
    ----------

    policy : Qt.HighDpiScaleFactorRoundingPolicy
      Passed on as its number.
    """
    #  void QGuiApplication::setHighDpiScaleFactorRoundingPolicy(Qt::
    #      HighDpiScaleFactorRoundingPolicy policy)
    Rituals.call(
        'ritual_ZN15QGuiApplication35setHighDpiScaleFactorRoundingPolicyEN2'
        'Qt32HighDpiScaleFactorRoundingPolicyE',
        policy.value,
    )

  @staticmethod
  def highDpiScaleFactorRoundingPolicy(
  ) -> Qt.HighDpiScaleFactorRoundingPolicy:
    """
    Calls Qt's 'Qt::HighDpiScaleFactorRoundingPolicy
    QGuiApplication::highDpiScaleFactorRoundingPolicy()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qguiapplication.html

    Returns
    -------

    Qt.HighDpiScaleFactorRoundingPolicy
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt.HighDpiScaleFactorRoundingPolicy(number)' gives.
    """
    #  Qt::HighDpiScaleFactorRoundingPolicy
    #      QGuiApplication::highDpiScaleFactorRoundingPolicy()
    return Qt.HighDpiScaleFactorRoundingPolicy(Rituals.call(
        'ritual_ZN15QGuiApplication32highDpiScaleFactorRoundingPolicyEv',
    ))

  @staticmethod
  def exec() -> int:
    """
    Calls Qt's 'int QGuiApplication::exec()'.

    Qt's own words: https://doc.qt.io/qt-6/qguiapplication.html#exec
    """
    #  int QGuiApplication::exec()
    return Rituals.call('ritual_ZN15QGuiApplication4execEv')

  @staticmethod
  def sync() -> None:
    """
    Calls Qt's 'void QGuiApplication::sync()'.

    Qt's own words: https://doc.qt.io/qt-6/qguiapplication.html#sync
    """
    #  void QGuiApplication::sync()
    Rituals.call('ritual_ZN15QGuiApplication4syncEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGuiApplication'

  #  A C++ QGuiApplication Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QGuiApplication'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QGuiApplication::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qguiapplication.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QGuiApplication::metaObject() const
    address = self.uglySide.call('ritual_ZNK15QGuiApplication10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def devicePixelRatio(self) -> float:
    """
    Calls Qt's 'qreal QGuiApplication::devicePixelRatio() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qguiapplication.html#devicePixelRatio
    """
    #  qreal QGuiApplication::devicePixelRatio() const
    return self.uglySide.call(
        'ritual_ZNK15QGuiApplication16devicePixelRatioEv',
    )

  def isSessionRestored(self) -> bool:
    """
    Calls Qt's 'bool QGuiApplication::isSessionRestored() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qguiapplication.html#isSessionRestored
    """
    #  bool QGuiApplication::isSessionRestored() const
    return self.uglySide.call(
        'ritual_ZNK15QGuiApplication17isSessionRestoredEv',
    )

  def sessionId(self) -> str:
    """
    Calls Qt's 'QString QGuiApplication::sessionId() const'.

    Qt's own words: https://doc.qt.io/qt-6/qguiapplication.html#sessionId

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QGuiApplication::sessionId() const
    return self.uglySide.call('ritual_ZNK15QGuiApplication9sessionIdEv')

  def sessionKey(self) -> str:
    """
    Calls Qt's 'QString QGuiApplication::sessionKey() const'.

    Qt's own words: https://doc.qt.io/qt-6/qguiapplication.html#sessionKey

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QGuiApplication::sessionKey() const
    return self.uglySide.call('ritual_ZNK15QGuiApplication10sessionKeyEv')

  def isSavingSession(self) -> bool:
    """
    Calls Qt's 'bool QGuiApplication::isSavingSession() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qguiapplication.html#isSavingSession
    """
    #  bool QGuiApplication::isSavingSession() const
    return self.uglySide.call(
        'ritual_ZNK15QGuiApplication15isSavingSessionEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setBadgeNumber(self, number: int) -> None:
    """
    Calls Qt's 'void QGuiApplication::setBadgeNumber(qint64 number)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qguiapplication.html#setBadgeNumber

    Parameters
    ----------

    number : int
      Passed on as it is.
    """
    #  void QGuiApplication::setBadgeNumber(qint64 number)
    self.uglySide.call(
        'ritual_ZN15QGuiApplication14setBadgeNumberEx', number,
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

  @overload(list)
  @overload(list, int)
  def __init__(self, argv: list, a2: int = 396288) -> None:
    """
    Calls Qt's 'QGuiApplication::QGuiApplication(int &argc, char **argv, int
    a2)' at once: nearly every other object of Qt can only be made after the
    application.

    Qt's own words:
    https://doc.qt.io/qt-6/qguiapplication.html#QGuiApplication

    Parameters
    ----------

    argv : list
      The texts the program was started with, as 'sys.argv'. Passed on as Qt
      takes them: how many they are, and where the first one is.

    a2 : int
      Passed on as it is. May be left out, as in Qt: it is then 396288.
    """
    #  QGuiApplication::QGuiApplication(int &argc, char **argv, int a2)
    self._noteCreation(QGuiApplication, lambda: Rituals.call(
        'ritual_ZN15QGuiApplicationC1ERiPPci', *self._startTextsOf(argv), a2,
    ))
    self._getUglySide()

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

  @overload(QObject, QEvent)
  @overload(QObject, NoneType)
  @overload(NoneType, QEvent)
  @overload(NoneType, NoneType)
  def notify(self, a0: Optional[QObject], a1: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QGuiApplication::notify(QObject *a0, QEvent *a1)'.

    Qt's own words: https://doc.qt.io/qt-6/qguiapplication.html#notify

    Parameters
    ----------

    a0 : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QGuiApplication::notify(QObject *a0, QEvent *a1)
    ritual = 'ritual_ZN15QGuiApplication6notifyEP7QObjectP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QGuiApplication6notifyEP7QObjectP6QEvent'
    return self.uglySide.call(
        ritual, self._addressOf(a0), self._addressOf(a1),
    )

  @overload(QEvent)
  @overload(NoneType)
  def event(self, a0: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QGuiApplication::event(QEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qguiapplication.html#event

    Parameters
    ----------

    a0 : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QGuiApplication::event(QEvent *a0)
    ritual = 'ritual_ZN15QGuiApplication5eventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QGuiApplication5eventEP6QEvent'
    return self.uglySide.call(ritual, self._addressOf(a0))
