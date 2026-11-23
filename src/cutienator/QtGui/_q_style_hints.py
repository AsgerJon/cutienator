"""
QStyleHints binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/qstylehints.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtCore import Qt, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QChar, QMetaObject
  from . import QAccessibilityHints

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QStyleHints(QObject):
  """
  The cute side of Qt's QStyleHints: a plain Python object standing in front
  of one C++ QStyleHints.

  It is built on the cute 'QObject', as Qt's QStyleHints is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QStyleHints that has a ritual and that Python can
  call so far, 45 names in all: 'metaObject', 'tr',
  'setMouseDoubleClickInterval', 'mouseDoubleClickInterval',
  'mouseDoubleClickDistance', 'touchDoubleTapDistance',
  'setMousePressAndHoldInterval', 'mousePressAndHoldInterval',
  'setStartDragDistance', 'startDragDistance', 'setStartDragTime',
  'startDragTime', 'startDragVelocity', 'setKeyboardInputInterval',
  'keyboardInputInterval', 'keyboardAutoRepeatRate',
  'keyboardAutoRepeatRateF', 'setCursorFlashTime', 'cursorFlashTime',
  'showIsFullScreen', 'showIsMaximized', 'showShortcutsInContextMenus',
  'setShowShortcutsInContextMenus', 'contextMenuTrigger',
  'setContextMenuTrigger', 'menuSelectionWraps', 'passwordMaskDelay',
  'passwordMaskCharacter', 'fontSmoothingGamma', 'useRtlExtensions',
  'setFocusOnTouchRelease', 'tabFocusBehavior', 'setTabFocusBehavior',
  'singleClickActivation', 'useHoverEffects', 'setUseHoverEffects',
  'wheelScrollLines', 'setWheelScrollLines',
  'setMouseQuickSelectionThreshold', 'mouseQuickSelectionThreshold',
  'colorScheme', 'setColorScheme', 'unsetColorScheme', 'accessibility',
  'toolTipWakeUpDelayAsMSec'. It can be made from Python, in 1 way; see
  '__init__'.

  What has no ritual
  ------------------

  23 of the 69 functions Qt declares: 15 a signal; 6 takes or gives a type
  that cannot be passed yet; 1 a template; 1 declared and nowhere to be
  found.

  What to expect
  --------------

  - The C++ QStyleHints is created at the first use, not by
    'QStyleHints(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QStyleHints.
  - Qt tells when it has removed the C++ QStyleHints. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
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
    Calls Qt's 'QString QStyleHints::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qstylehints.html#tr

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
    #  QString QStyleHints::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN11QStyleHints2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QStyleHints'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QStyleHints::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstylehints.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QStyleHints::metaObject() const
    address = self.uglySide.call('ritual_ZNK11QStyleHints10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def mouseDoubleClickInterval(self) -> int:
    """
    Calls Qt's 'int QStyleHints::mouseDoubleClickInterval() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstylehints.html#mouseDoubleClickInterval
    """
    #  int QStyleHints::mouseDoubleClickInterval() const
    return self.uglySide.call(
        'ritual_ZNK11QStyleHints24mouseDoubleClickIntervalEv',
    )

  def mouseDoubleClickDistance(self) -> int:
    """
    Calls Qt's 'int QStyleHints::mouseDoubleClickDistance() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstylehints.html#mouseDoubleClickDistance
    """
    #  int QStyleHints::mouseDoubleClickDistance() const
    return self.uglySide.call(
        'ritual_ZNK11QStyleHints24mouseDoubleClickDistanceEv',
    )

  def touchDoubleTapDistance(self) -> int:
    """
    Calls Qt's 'int QStyleHints::touchDoubleTapDistance() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstylehints.html#touchDoubleTapDistance
    """
    #  int QStyleHints::touchDoubleTapDistance() const
    return self.uglySide.call(
        'ritual_ZNK11QStyleHints22touchDoubleTapDistanceEv',
    )

  def mousePressAndHoldInterval(self) -> int:
    """
    Calls Qt's 'int QStyleHints::mousePressAndHoldInterval() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstylehints.html#mousePressAndHoldInterval
    """
    #  int QStyleHints::mousePressAndHoldInterval() const
    return self.uglySide.call(
        'ritual_ZNK11QStyleHints25mousePressAndHoldIntervalEv',
    )

  def startDragDistance(self) -> int:
    """
    Calls Qt's 'int QStyleHints::startDragDistance() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstylehints.html#startDragDistance
    """
    #  int QStyleHints::startDragDistance() const
    return self.uglySide.call('ritual_ZNK11QStyleHints17startDragDistanceEv')

  def startDragTime(self) -> int:
    """
    Calls Qt's 'int QStyleHints::startDragTime() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstylehints.html#startDragTime
    """
    #  int QStyleHints::startDragTime() const
    return self.uglySide.call('ritual_ZNK11QStyleHints13startDragTimeEv')

  def startDragVelocity(self) -> int:
    """
    Calls Qt's 'int QStyleHints::startDragVelocity() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstylehints.html#startDragVelocity
    """
    #  int QStyleHints::startDragVelocity() const
    return self.uglySide.call('ritual_ZNK11QStyleHints17startDragVelocityEv')

  def keyboardInputInterval(self) -> int:
    """
    Calls Qt's 'int QStyleHints::keyboardInputInterval() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstylehints.html#keyboardInputInterval
    """
    #  int QStyleHints::keyboardInputInterval() const
    return self.uglySide.call(
        'ritual_ZNK11QStyleHints21keyboardInputIntervalEv',
    )

  def keyboardAutoRepeatRate(self) -> int:
    """
    Calls Qt's 'int QStyleHints::keyboardAutoRepeatRate() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstylehints.html#keyboardAutoRepeatRate
    """
    #  int QStyleHints::keyboardAutoRepeatRate() const
    return self.uglySide.call(
        'ritual_ZNK11QStyleHints22keyboardAutoRepeatRateEv',
    )

  def keyboardAutoRepeatRateF(self) -> float:
    """
    Calls Qt's 'qreal QStyleHints::keyboardAutoRepeatRateF() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstylehints.html#keyboardAutoRepeatRateF
    """
    #  qreal QStyleHints::keyboardAutoRepeatRateF() const
    return self.uglySide.call(
        'ritual_ZNK11QStyleHints23keyboardAutoRepeatRateFEv',
    )

  def cursorFlashTime(self) -> int:
    """
    Calls Qt's 'int QStyleHints::cursorFlashTime() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstylehints.html#cursorFlashTime
    """
    #  int QStyleHints::cursorFlashTime() const
    return self.uglySide.call('ritual_ZNK11QStyleHints15cursorFlashTimeEv')

  def showIsFullScreen(self) -> bool:
    """
    Calls Qt's 'bool QStyleHints::showIsFullScreen() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstylehints.html#showIsFullScreen
    """
    #  bool QStyleHints::showIsFullScreen() const
    return self.uglySide.call('ritual_ZNK11QStyleHints16showIsFullScreenEv')

  def showIsMaximized(self) -> bool:
    """
    Calls Qt's 'bool QStyleHints::showIsMaximized() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstylehints.html#showIsMaximized
    """
    #  bool QStyleHints::showIsMaximized() const
    return self.uglySide.call('ritual_ZNK11QStyleHints15showIsMaximizedEv')

  def showShortcutsInContextMenus(self) -> bool:
    """
    Calls Qt's 'bool QStyleHints::showShortcutsInContextMenus() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstylehints.html#showShortcutsInContextMenus
    """
    #  bool QStyleHints::showShortcutsInContextMenus() const
    return self.uglySide.call(
        'ritual_ZNK11QStyleHints27showShortcutsInContextMenusEv',
    )

  def contextMenuTrigger(self) -> Qt.ContextMenuTrigger:
    """
    Calls Qt's 'Qt::ContextMenuTrigger QStyleHints::contextMenuTrigger()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstylehints.html#contextMenuTrigger

    Returns
    -------

    Qt.ContextMenuTrigger
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt.ContextMenuTrigger(number)' gives.
    """
    #  Qt::ContextMenuTrigger QStyleHints::contextMenuTrigger() const
    return Qt.ContextMenuTrigger(self.uglySide.call(
        'ritual_ZNK11QStyleHints18contextMenuTriggerEv',
    ))

  def menuSelectionWraps(self) -> bool:
    """
    Calls Qt's 'bool QStyleHints::menuSelectionWraps() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstylehints.html#menuSelectionWraps
    """
    #  bool QStyleHints::menuSelectionWraps() const
    return self.uglySide.call(
        'ritual_ZNK11QStyleHints18menuSelectionWrapsEv',
    )

  def passwordMaskDelay(self) -> int:
    """
    Calls Qt's 'int QStyleHints::passwordMaskDelay() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstylehints.html#passwordMaskDelay
    """
    #  int QStyleHints::passwordMaskDelay() const
    return self.uglySide.call('ritual_ZNK11QStyleHints17passwordMaskDelayEv')

  def passwordMaskCharacter(self) -> QChar:
    """
    Calls Qt's 'QChar QStyleHints::passwordMaskCharacter() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstylehints.html#passwordMaskCharacter

    Returns
    -------

    QChar
      A new cute QChar around the copy Qt gave back. Python owns it.
    """
    #  QChar QStyleHints::passwordMaskCharacter() const
    address = self.uglySide.call(
        'ritual_ZNK11QStyleHints21passwordMaskCharacterEv',
    )
    from ..QtCore import QChar
    return QChar._cuteOwning(address)

  def fontSmoothingGamma(self) -> float:
    """
    Calls Qt's 'qreal QStyleHints::fontSmoothingGamma() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstylehints.html#fontSmoothingGamma
    """
    #  qreal QStyleHints::fontSmoothingGamma() const
    return self.uglySide.call(
        'ritual_ZNK11QStyleHints18fontSmoothingGammaEv',
    )

  def useRtlExtensions(self) -> bool:
    """
    Calls Qt's 'bool QStyleHints::useRtlExtensions() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstylehints.html#useRtlExtensions
    """
    #  bool QStyleHints::useRtlExtensions() const
    return self.uglySide.call('ritual_ZNK11QStyleHints16useRtlExtensionsEv')

  def tabFocusBehavior(self) -> Qt.TabFocusBehavior:
    """
    Calls Qt's 'Qt::TabFocusBehavior QStyleHints::tabFocusBehavior() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstylehints.html#tabFocusBehavior

    Returns
    -------

    Qt.TabFocusBehavior
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt.TabFocusBehavior(number)' gives.
    """
    #  Qt::TabFocusBehavior QStyleHints::tabFocusBehavior() const
    return Qt.TabFocusBehavior(self.uglySide.call(
        'ritual_ZNK11QStyleHints16tabFocusBehaviorEv',
    ))

  def singleClickActivation(self) -> bool:
    """
    Calls Qt's 'bool QStyleHints::singleClickActivation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstylehints.html#singleClickActivation
    """
    #  bool QStyleHints::singleClickActivation() const
    return self.uglySide.call(
        'ritual_ZNK11QStyleHints21singleClickActivationEv',
    )

  def useHoverEffects(self) -> bool:
    """
    Calls Qt's 'bool QStyleHints::useHoverEffects() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstylehints.html#useHoverEffects
    """
    #  bool QStyleHints::useHoverEffects() const
    return self.uglySide.call('ritual_ZNK11QStyleHints15useHoverEffectsEv')

  def wheelScrollLines(self) -> int:
    """
    Calls Qt's 'int QStyleHints::wheelScrollLines() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstylehints.html#wheelScrollLines
    """
    #  int QStyleHints::wheelScrollLines() const
    return self.uglySide.call('ritual_ZNK11QStyleHints16wheelScrollLinesEv')

  def mouseQuickSelectionThreshold(self) -> int:
    """
    Calls Qt's 'int QStyleHints::mouseQuickSelectionThreshold() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstylehints.html#mouseQuickSelectionThreshold
    """
    #  int QStyleHints::mouseQuickSelectionThreshold() const
    return self.uglySide.call(
        'ritual_ZNK11QStyleHints28mouseQuickSelectionThresholdEv',
    )

  def colorScheme(self) -> Qt.ColorScheme:
    """
    Calls Qt's 'Qt::ColorScheme QStyleHints::colorScheme() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstylehints.html#colorScheme

    Returns
    -------

    Qt.ColorScheme
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.ColorScheme(number)'
      gives.
    """
    #  Qt::ColorScheme QStyleHints::colorScheme() const
    return Qt.ColorScheme(self.uglySide.call(
        'ritual_ZNK11QStyleHints11colorSchemeEv',
    ))

  def accessibility(self) -> Optional[QAccessibilityHints]:
    """
    Calls Qt's 'const QAccessibilityHints *QStyleHints::accessibility()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qstylehints.html#accessibility

    Returns
    -------

    Optional[QAccessibilityHints]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QAccessibilityHints *QStyleHints::accessibility() const
    address = self.uglySide.call('ritual_ZNK11QStyleHints13accessibilityEv')
    from . import QAccessibilityHints
    return QAccessibilityHints._cuteAt(address)

  def toolTipWakeUpDelayAsMSec(self) -> int:
    """
    Calls Qt's 'int QStyleHints::toolTipWakeUpDelayAsMSec() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstylehints.html#toolTipWakeUpDelayAsMSec
    """
    #  int QStyleHints::toolTipWakeUpDelayAsMSec() const
    return self.uglySide.call(
        'ritual_ZNK11QStyleHints24toolTipWakeUpDelayAsMSecEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setMouseDoubleClickInterval(
      self,
      mouseDoubleClickInterval: int,
  ) -> None:
    """
    Calls Qt's 'void QStyleHints::setMouseDoubleClickInterval(int
    mouseDoubleClickInterval)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstylehints.html#setMouseDoubleClickInterval

    Parameters
    ----------

    mouseDoubleClickInterval : int
      Passed on as it is.
    """
    #  void QStyleHints::setMouseDoubleClickInterval(int
    #      mouseDoubleClickInterval)
    self.uglySide.call(
        'ritual_ZN11QStyleHints27setMouseDoubleClickIntervalEi',
        mouseDoubleClickInterval,
    )

  @overload(int)
  def setMousePressAndHoldInterval(
      self,
      mousePressAndHoldInterval: int,
  ) -> None:
    """
    Calls Qt's 'void QStyleHints::setMousePressAndHoldInterval(int
    mousePressAndHoldInterval)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstylehints.html#setMousePressAndHoldInterval

    Parameters
    ----------

    mousePressAndHoldInterval : int
      Passed on as it is.
    """
    #  void QStyleHints::setMousePressAndHoldInterval(int
    #      mousePressAndHoldInterval)
    self.uglySide.call(
        'ritual_ZN11QStyleHints28setMousePressAndHoldIntervalEi',
        mousePressAndHoldInterval,
    )

  @overload(int)
  def setStartDragDistance(self, startDragDistance: int) -> None:
    """
    Calls Qt's 'void QStyleHints::setStartDragDistance(int
    startDragDistance)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstylehints.html#setStartDragDistance

    Parameters
    ----------

    startDragDistance : int
      Passed on as it is.
    """
    #  void QStyleHints::setStartDragDistance(int startDragDistance)
    self.uglySide.call(
        'ritual_ZN11QStyleHints20setStartDragDistanceEi', startDragDistance,
    )

  @overload(int)
  def setStartDragTime(self, startDragTime: int) -> None:
    """
    Calls Qt's 'void QStyleHints::setStartDragTime(int startDragTime)'.

    Qt's own words: https://doc.qt.io/qt-6/qstylehints.html#setStartDragTime

    Parameters
    ----------

    startDragTime : int
      Passed on as it is.
    """
    #  void QStyleHints::setStartDragTime(int startDragTime)
    self.uglySide.call(
        'ritual_ZN11QStyleHints16setStartDragTimeEi', startDragTime,
    )

  @overload(int)
  def setKeyboardInputInterval(self, keyboardInputInterval: int) -> None:
    """
    Calls Qt's 'void QStyleHints::setKeyboardInputInterval(int
    keyboardInputInterval)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstylehints.html#setKeyboardInputInterval

    Parameters
    ----------

    keyboardInputInterval : int
      Passed on as it is.
    """
    #  void QStyleHints::setKeyboardInputInterval(int keyboardInputInterval)
    self.uglySide.call(
        'ritual_ZN11QStyleHints24setKeyboardInputIntervalEi',
        keyboardInputInterval,
    )

  @overload(int)
  def setCursorFlashTime(self, cursorFlashTime: int) -> None:
    """
    Calls Qt's 'void QStyleHints::setCursorFlashTime(int cursorFlashTime)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstylehints.html#setCursorFlashTime

    Parameters
    ----------

    cursorFlashTime : int
      Passed on as it is.
    """
    #  void QStyleHints::setCursorFlashTime(int cursorFlashTime)
    self.uglySide.call(
        'ritual_ZN11QStyleHints18setCursorFlashTimeEi', cursorFlashTime,
    )

  @overload(bool)
  def setShowShortcutsInContextMenus(
      self,
      showShortcutsInContextMenus: bool,
  ) -> None:
    """
    Calls Qt's 'void QStyleHints::setShowShortcutsInContextMenus(bool
    showShortcutsInContextMenus)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstylehints.html#setShowShortcutsInContextMenus

    Parameters
    ----------

    showShortcutsInContextMenus : bool
      Passed on as it is.
    """
    #  void QStyleHints::setShowShortcutsInContextMenus(bool
    #      showShortcutsInContextMenus)
    self.uglySide.call(
        'ritual_ZN11QStyleHints30setShowShortcutsInContextMenusEb',
        showShortcutsInContextMenus,
    )

  @overload(Qt.ContextMenuTrigger)
  def setContextMenuTrigger(
      self,
      contextMenuTrigger: Qt.ContextMenuTrigger,
  ) -> None:
    """
    Calls Qt's 'void
    QStyleHints::setContextMenuTrigger(Qt::ContextMenuTrigger
    contextMenuTrigger)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstylehints.html#setContextMenuTrigger

    Parameters
    ----------

    contextMenuTrigger : Qt.ContextMenuTrigger
      Passed on as its number.
    """
    #  void QStyleHints::setContextMenuTrigger(Qt::ContextMenuTrigger
    #      contextMenuTrigger)
    self.uglySide.call(
        'ritual_ZN11QStyleHints21setContextMenuTriggerEN2Qt18ContextMenuTri'
        'ggerE',
        contextMenuTrigger.value,
    )

  def setFocusOnTouchRelease(self) -> bool:
    """
    Calls Qt's 'bool QStyleHints::setFocusOnTouchRelease() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstylehints.html#setFocusOnTouchRelease
    """
    #  bool QStyleHints::setFocusOnTouchRelease() const
    return self.uglySide.call(
        'ritual_ZNK11QStyleHints22setFocusOnTouchReleaseEv',
    )

  @overload(Qt.TabFocusBehavior)
  def setTabFocusBehavior(
      self,
      tabFocusBehavior: Qt.TabFocusBehavior,
  ) -> None:
    """
    Calls Qt's 'void QStyleHints::setTabFocusBehavior(Qt::TabFocusBehavior
    tabFocusBehavior)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstylehints.html#setTabFocusBehavior

    Parameters
    ----------

    tabFocusBehavior : Qt.TabFocusBehavior
      Passed on as its number.
    """
    #  void QStyleHints::setTabFocusBehavior(Qt::TabFocusBehavior
    #      tabFocusBehavior)
    self.uglySide.call(
        'ritual_ZN11QStyleHints19setTabFocusBehaviorEN2Qt16TabFocusBehavior'
        'E',
        tabFocusBehavior.value,
    )

  @overload(bool)
  def setUseHoverEffects(self, useHoverEffects: bool) -> None:
    """
    Calls Qt's 'void QStyleHints::setUseHoverEffects(bool useHoverEffects)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstylehints.html#setUseHoverEffects

    Parameters
    ----------

    useHoverEffects : bool
      Passed on as it is.
    """
    #  void QStyleHints::setUseHoverEffects(bool useHoverEffects)
    self.uglySide.call(
        'ritual_ZN11QStyleHints18setUseHoverEffectsEb', useHoverEffects,
    )

  @overload(int)
  def setWheelScrollLines(self, scrollLines: int) -> None:
    """
    Calls Qt's 'void QStyleHints::setWheelScrollLines(int scrollLines)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstylehints.html#setWheelScrollLines

    Parameters
    ----------

    scrollLines : int
      Passed on as it is.
    """
    #  void QStyleHints::setWheelScrollLines(int scrollLines)
    self.uglySide.call(
        'ritual_ZN11QStyleHints19setWheelScrollLinesEi', scrollLines,
    )

  @overload(int)
  def setMouseQuickSelectionThreshold(self, threshold: int) -> None:
    """
    Calls Qt's 'void QStyleHints::setMouseQuickSelectionThreshold(int
    threshold)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstylehints.html#setMouseQuickSelectionThreshold

    Parameters
    ----------

    threshold : int
      Passed on as it is.
    """
    #  void QStyleHints::setMouseQuickSelectionThreshold(int threshold)
    self.uglySide.call(
        'ritual_ZN11QStyleHints31setMouseQuickSelectionThresholdEi',
        threshold,
    )

  @overload(Qt.ColorScheme)
  def setColorScheme(self, scheme: Qt.ColorScheme) -> None:
    """
    Calls Qt's 'void QStyleHints::setColorScheme(Qt::ColorScheme scheme)'.

    Qt's own words: https://doc.qt.io/qt-6/qstylehints.html#setColorScheme

    Parameters
    ----------

    scheme : Qt.ColorScheme
      Passed on as its number.
    """
    #  void QStyleHints::setColorScheme(Qt::ColorScheme scheme)
    self.uglySide.call(
        'ritual_ZN11QStyleHints14setColorSchemeEN2Qt11ColorSchemeE',
        scheme.value,
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
    Notes what was given, for Qt's 'QStyleHints::QStyleHints()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qstylehints.html#QStyleHints
    """
    #  QStyleHints::QStyleHints()
    self._noteCreation(QStyleHints, lambda: Rituals.call(
        'ritual_ZN11QStyleHintsC1Ev',
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

  def unsetColorScheme(self) -> None:
    """
    Calls Qt's 'void QStyleHints::unsetColorScheme()'.

    Qt's own words: https://doc.qt.io/qt-6/qstylehints.html#unsetColorScheme
    """
    #  void QStyleHints::unsetColorScheme()
    self.uglySide.call('ritual_ZN11QStyleHints16unsetColorSchemeEv')
