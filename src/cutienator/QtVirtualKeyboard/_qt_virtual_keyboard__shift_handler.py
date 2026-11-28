"""
QtVirtualKeyboard::ShiftHandler binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtVirtualKeyboard/6.12.0/QtVirtualKeyboard/private/shifthandler_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QtVirtualKeyboard::ShiftHandler to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from . import QVirtualKeyboardInputContext
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QVirtualKeyboardInputContext = WAIT['QVirtualKeyboardInputContext']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class ShiftHandler(QObject):
  """
  The cute side of Qt's QtVirtualKeyboard::ShiftHandler: a plain Python
  object standing in front of one C++ QtVirtualKeyboard::ShiftHandler.

  It is built on the cute 'QObject', as Qt's QtVirtualKeyboard::ShiftHandler
  is built on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QtVirtualKeyboard::ShiftHandler that has a ritual
  and that Python can call so far, 27 names in all: 'metaObject', 'tr',
  'init', 'sentenceEndingCharacters', 'setSentenceEndingCharacters',
  'isAutoCapitalizationEnabled', 'isToggleShiftEnabled', 'isShiftActive',
  'setShiftActive', 'isCapsLockActive', 'setCapsLockActive', 'isUppercase',
  'toggleShift', 'clearToggleShiftTimer', 'sentenceEndingCharactersChanged',
  'toggleShiftEnabledChanged', 'autoCapitalizationEnabledChanged',
  'shiftActiveChanged', 'capsLockActiveChanged', 'uppercaseChanged', 'reset',
  'autoCapitalize', 'restart', 'localeChanged', 'inputMethodVisibleChanged',
  'setAutoCapitalizationEnabled', 'setToggleShiftEnabled'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QtVirtualKeyboard::ShiftHandler::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int QtVirtualKeyboard::ShiftHandler::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'void QtVirtualKeyboard::ShiftHandler::qt_qmlMarker_uncreatable()':
    one of Qt's own inner workings.
  - Qt's 'QtVirtualKeyboard::ShiftHandler::~ShiftHandler()': the destructor:
    Python never removes a C++ QtVirtualKeyboard::ShiftHandler.

  What has no ritual
  ------------------

  6 of the 38 functions Qt declares: 2 not a gap; 2 forbidden; 2 the compiler
  refuses its ritual as it would be written here.

  What to expect
  --------------

  - The C++ QtVirtualKeyboard::ShiftHandler is created at the first use, not
    by 'QtVirtualKeyboard::ShiftHandler(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QtVirtualKeyboard::ShiftHandler.
  - Qt tells when it has removed the C++ QtVirtualKeyboard::ShiftHandler.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
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
    Calls Qt's 'QString QtVirtualKeyboard::ShiftHandler::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-shifthandler.html#tr

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
    #  QString QtVirtualKeyboard::ShiftHandler::tr(const char *s, const char
    #      *c, int n)
    return Rituals.call(
        'ritual_ZN17QtVirtualKeyboard12ShiftHandler2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QtVirtualKeyboard::ShiftHandler'

  #  A C++ QtVirtualKeyboard::ShiftHandler Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QtVirtualKeyboard_ShiftHandler'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject
    *QtVirtualKeyboard::ShiftHandler::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-shifthandler.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QtVirtualKeyboard::ShiftHandler::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK17QtVirtualKeyboard12ShiftHandler10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def sentenceEndingCharacters(self) -> str:
    """
    Calls Qt's 'QString
    QtVirtualKeyboard::ShiftHandler::sentenceEndingCharacters() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-shifthandler.html

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QtVirtualKeyboard::ShiftHandler::sentenceEndingCharacters()
    #      const
    return self.uglySide.call(
        'ritual_ZNK17QtVirtualKeyboard12ShiftHandler24sentenceEndingCharact'
        'ersEv',
    )

  def isAutoCapitalizationEnabled(self) -> bool:
    """
    Calls Qt's 'bool
    QtVirtualKeyboard::ShiftHandler::isAutoCapitalizationEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-shifthandler.html
    """
    #  bool QtVirtualKeyboard::ShiftHandler::isAutoCapitalizationEnabled()
    #      const
    return self.uglySide.call(
        'ritual_ZNK17QtVirtualKeyboard12ShiftHandler27isAutoCapitalizationE'
        'nabledEv',
    )

  def isToggleShiftEnabled(self) -> bool:
    """
    Calls Qt's 'bool QtVirtualKeyboard::ShiftHandler::isToggleShiftEnabled()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-shifthandler.html
    """
    #  bool QtVirtualKeyboard::ShiftHandler::isToggleShiftEnabled() const
    return self.uglySide.call(
        'ritual_ZNK17QtVirtualKeyboard12ShiftHandler20isToggleShiftEnabledE'
        'v',
    )

  def isShiftActive(self) -> bool:
    """
    Calls Qt's 'bool QtVirtualKeyboard::ShiftHandler::isShiftActive() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-shifthandler.html#isShiftActive
    """
    #  bool QtVirtualKeyboard::ShiftHandler::isShiftActive() const
    return self.uglySide.call(
        'ritual_ZNK17QtVirtualKeyboard12ShiftHandler13isShiftActiveEv',
    )

  def isCapsLockActive(self) -> bool:
    """
    Calls Qt's 'bool QtVirtualKeyboard::ShiftHandler::isCapsLockActive()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-shifthandler.html
    """
    #  bool QtVirtualKeyboard::ShiftHandler::isCapsLockActive() const
    return self.uglySide.call(
        'ritual_ZNK17QtVirtualKeyboard12ShiftHandler16isCapsLockActiveEv',
    )

  def isUppercase(self) -> bool:
    """
    Calls Qt's 'bool QtVirtualKeyboard::ShiftHandler::isUppercase() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-shifthandler.html#isUppercase
    """
    #  bool QtVirtualKeyboard::ShiftHandler::isUppercase() const
    return self.uglySide.call(
        'ritual_ZNK17QtVirtualKeyboard12ShiftHandler11isUppercaseEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setSentenceEndingCharacters(self, value: str) -> None:
    """
    Calls Qt's 'void
    QtVirtualKeyboard::ShiftHandler::setSentenceEndingCharacters(const
    QString &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-shifthandler.html

    Parameters
    ----------

    value : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void
    #      QtVirtualKeyboard::ShiftHandler::setSentenceEndingCharacters(const
    #      QString &value)
    self.uglySide.call(
        'ritual_ZN17QtVirtualKeyboard12ShiftHandler27setSentenceEndingChara'
        'ctersERK7QString',
        value,
    )

  @overload(bool)
  def setShiftActive(self, active: bool) -> None:
    """
    Calls Qt's 'void QtVirtualKeyboard::ShiftHandler::setShiftActive(bool
    active)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-shifthandler.html#setShiftActive

    Parameters
    ----------

    active : bool
      Passed on as it is.
    """
    #  void QtVirtualKeyboard::ShiftHandler::setShiftActive(bool active)
    self.uglySide.call(
        'ritual_ZN17QtVirtualKeyboard12ShiftHandler14setShiftActiveEb',
        active,
    )

  @overload(bool)
  def setCapsLockActive(self, active: bool) -> None:
    """
    Calls Qt's 'void QtVirtualKeyboard::ShiftHandler::setCapsLockActive(bool
    active)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-shifthandler.html

    Parameters
    ----------

    active : bool
      Passed on as it is.
    """
    #  void QtVirtualKeyboard::ShiftHandler::setCapsLockActive(bool active)
    self.uglySide.call(
        'ritual_ZN17QtVirtualKeyboard12ShiftHandler17setCapsLockActiveEb',
        active,
    )

  @overload(bool)
  def setAutoCapitalizationEnabled(self, enabled: bool) -> None:
    """
    Calls Qt's 'void
    QtVirtualKeyboard::ShiftHandler::setAutoCapitalizationEnabled(bool
    enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-shifthandler.html

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void
    #      QtVirtualKeyboard::ShiftHandler::setAutoCapitalizationEnabled(bool
    #      enabled)
    self.uglySide.call(
        'ritual_ZN17QtVirtualKeyboard12ShiftHandler28setAutoCapitalizationE'
        'nabledEb',
        enabled,
    )

  @overload(bool)
  def setToggleShiftEnabled(self, enabled: bool) -> None:
    """
    Calls Qt's 'void
    QtVirtualKeyboard::ShiftHandler::setToggleShiftEnabled(bool enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-shifthandler.html

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QtVirtualKeyboard::ShiftHandler::setToggleShiftEnabled(bool
    #      enabled)
    self.uglySide.call(
        'ritual_ZN17QtVirtualKeyboard12ShiftHandler21setToggleShiftEnabledE'
        'b',
        enabled,
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
  @overload(QVirtualKeyboardInputContext)
  @overload(NoneType)
  def __init__(
      self,
      parent: Optional[QVirtualKeyboardInputContext] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QtVirtualKeyboard::ShiftHandler::ShiftHandler(
    QVirtualKeyboardInputContext *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-shifthandler.html#ShiftHandler

    Parameters
    ----------

    parent : Optional[QVirtualKeyboardInputContext]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QtVirtualKeyboard::ShiftHandler::ShiftHandler(
    #      QVirtualKeyboardInputContext *parent)
    self._noteCreation(ShiftHandler, lambda: Rituals.call(
        'ritual_ZN17QtVirtualKeyboard12ShiftHandlerC1EP28QVirtualKeyboardIn'
        'putContext',
        self._addressOf(parent),
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

  def init(self) -> None:
    """
    Calls Qt's 'void QtVirtualKeyboard::ShiftHandler::init()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-shifthandler.html#init
    """
    #  void QtVirtualKeyboard::ShiftHandler::init()
    self.uglySide.call('ritual_ZN17QtVirtualKeyboard12ShiftHandler4initEv')

  def toggleShift(self) -> None:
    """
    Calls Qt's 'void QtVirtualKeyboard::ShiftHandler::toggleShift()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-shifthandler.html#toggleShift
    """
    #  void QtVirtualKeyboard::ShiftHandler::toggleShift()
    self.uglySide.call(
        'ritual_ZN17QtVirtualKeyboard12ShiftHandler11toggleShiftEv',
    )

  def clearToggleShiftTimer(self) -> None:
    """
    Calls Qt's 'void
    QtVirtualKeyboard::ShiftHandler::clearToggleShiftTimer()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-shifthandler.html
    """
    #  void QtVirtualKeyboard::ShiftHandler::clearToggleShiftTimer()
    self.uglySide.call(
        'ritual_ZN17QtVirtualKeyboard12ShiftHandler21clearToggleShiftTimerE'
        'v',
    )

  def sentenceEndingCharactersChanged(self) -> None:
    """
    Calls Qt's 'void
    QtVirtualKeyboard::ShiftHandler::sentenceEndingCharactersChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-shifthandler.html
    """
    #  void
    #      QtVirtualKeyboard::ShiftHandler::sentenceEndingCharactersChanged()
    self.uglySide.call(
        'ritual_ZN17QtVirtualKeyboard12ShiftHandler31sentenceEndingCharacte'
        'rsChangedEv',
    )

  def toggleShiftEnabledChanged(self) -> None:
    """
    Calls Qt's 'void
    QtVirtualKeyboard::ShiftHandler::toggleShiftEnabledChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-shifthandler.html
    """
    #  void QtVirtualKeyboard::ShiftHandler::toggleShiftEnabledChanged()
    self.uglySide.call(
        'ritual_ZN17QtVirtualKeyboard12ShiftHandler25toggleShiftEnabledChan'
        'gedEv',
    )

  def autoCapitalizationEnabledChanged(self) -> None:
    """
    Calls Qt's 'void
    QtVirtualKeyboard::ShiftHandler::autoCapitalizationEnabledChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-shifthandler.html
    """
    #  void
    #      QtVirtualKeyboard::ShiftHandler::autoCapitalizationEnabledChanged(
    #      )
    self.uglySide.call(
        'ritual_ZN17QtVirtualKeyboard12ShiftHandler32autoCapitalizationEnab'
        'ledChangedEv',
    )

  def shiftActiveChanged(self) -> None:
    """
    Calls Qt's 'void QtVirtualKeyboard::ShiftHandler::shiftActiveChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-shifthandler.html
    """
    #  void QtVirtualKeyboard::ShiftHandler::shiftActiveChanged()
    self.uglySide.call(
        'ritual_ZN17QtVirtualKeyboard12ShiftHandler18shiftActiveChangedEv',
    )

  def capsLockActiveChanged(self) -> None:
    """
    Calls Qt's 'void
    QtVirtualKeyboard::ShiftHandler::capsLockActiveChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-shifthandler.html
    """
    #  void QtVirtualKeyboard::ShiftHandler::capsLockActiveChanged()
    self.uglySide.call(
        'ritual_ZN17QtVirtualKeyboard12ShiftHandler21capsLockActiveChangedE'
        'v',
    )

  def uppercaseChanged(self) -> None:
    """
    Calls Qt's 'void QtVirtualKeyboard::ShiftHandler::uppercaseChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-shifthandler.html
    """
    #  void QtVirtualKeyboard::ShiftHandler::uppercaseChanged()
    self.uglySide.call(
        'ritual_ZN17QtVirtualKeyboard12ShiftHandler16uppercaseChangedEv',
    )

  def reset(self) -> None:
    """
    Calls Qt's 'void QtVirtualKeyboard::ShiftHandler::reset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-shifthandler.html#reset
    """
    #  void QtVirtualKeyboard::ShiftHandler::reset()
    self.uglySide.call('ritual_ZN17QtVirtualKeyboard12ShiftHandler5resetEv')

  def autoCapitalize(self) -> None:
    """
    Calls Qt's 'void QtVirtualKeyboard::ShiftHandler::autoCapitalize()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-shifthandler.html#autoCapitalize
    """
    #  void QtVirtualKeyboard::ShiftHandler::autoCapitalize()
    self.uglySide.call(
        'ritual_ZN17QtVirtualKeyboard12ShiftHandler14autoCapitalizeEv',
    )

  def restart(self) -> None:
    """
    Calls Qt's 'void QtVirtualKeyboard::ShiftHandler::restart()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-shifthandler.html#restart
    """
    #  void QtVirtualKeyboard::ShiftHandler::restart()
    self.uglySide.call(
        'ritual_ZN17QtVirtualKeyboard12ShiftHandler7restartEv',
    )

  def localeChanged(self) -> None:
    """
    Calls Qt's 'void QtVirtualKeyboard::ShiftHandler::localeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-shifthandler.html#localeChanged
    """
    #  void QtVirtualKeyboard::ShiftHandler::localeChanged()
    self.uglySide.call(
        'ritual_ZN17QtVirtualKeyboard12ShiftHandler13localeChangedEv',
    )

  def inputMethodVisibleChanged(self) -> None:
    """
    Calls Qt's 'void
    QtVirtualKeyboard::ShiftHandler::inputMethodVisibleChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-shifthandler.html
    """
    #  void QtVirtualKeyboard::ShiftHandler::inputMethodVisibleChanged()
    self.uglySide.call(
        'ritual_ZN17QtVirtualKeyboard12ShiftHandler25inputMethodVisibleChan'
        'gedEv',
    )
