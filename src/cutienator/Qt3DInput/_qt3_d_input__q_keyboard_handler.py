"""
Qt3DInput::QKeyboardHandler binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DInput/qkeyboardhandler.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore
from . import Qt3DInput

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QKeyboardHandler(Qt3DCore.QComponent):
  """
  The cute side of Qt's Qt3DInput::QKeyboardHandler: a plain Python object
  standing in front of one C++ Qt3DInput::QKeyboardHandler.

  It is built on the cute 'Qt3DCore::QComponent', as Qt's
  Qt3DInput::QKeyboardHandler is built on Qt's Qt3DCore::QComponent, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DInput::QKeyboardHandler that has a ritual and
  that Python can call so far, 49 names in all: 'metaObject', 'tr',
  'sourceDevice', 'focus', 'setSourceDevice', 'setFocus',
  'sourceDeviceChanged', 'focusChanged', 'digit0Pressed', 'digit1Pressed',
  'digit2Pressed', 'digit3Pressed', 'digit4Pressed', 'digit5Pressed',
  'digit6Pressed', 'digit7Pressed', 'digit8Pressed', 'digit9Pressed',
  'leftPressed', 'rightPressed', 'upPressed', 'downPressed', 'tabPressed',
  'backtabPressed', 'asteriskPressed', 'numberSignPressed', 'escapePressed',
  'returnPressed', 'enterPressed', 'deletePressed', 'spacePressed',
  'backPressed', 'cancelPressed', 'selectPressed', 'yesPressed', 'noPressed',
  'context1Pressed', 'context2Pressed', 'context3Pressed', 'context4Pressed',
  'callPressed', 'hangupPressed', 'flipPressed', 'menuPressed',
  'volumeUpPressed', 'volumeDownPressed', 'pressed', 'released', 'd_func'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DInput::QKeyboardHandler::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int Qt3DInput::QKeyboardHandler::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DInput::QKeyboardHandler::~QKeyboardHandler()': the destructor:
    Python never removes a C++ Qt3DInput::QKeyboardHandler.
  - Qt's 'const QKeyboardHandlerPrivate
    *Qt3DInput::QKeyboardHandler::d_func() const': takes in Python what
    'QKeyboardHandlerPrivate *Qt3DInput::QKeyboardHandler::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 56 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DInput::QKeyboardHandler is created at the first use, not by
    'Qt3DInput::QKeyboardHandler(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DInput::QKeyboardHandler.
  - Qt tells when it has removed the C++ Qt3DInput::QKeyboardHandler. Every
    call on the cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString Qt3DInput::QKeyboardHandler::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dinput-qkeyboardhandler.html#tr

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
    #  QString Qt3DInput::QKeyboardHandler::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN9Qt3DInput16QKeyboardHandler2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DInput::QKeyboardHandler'

  #  A C++ Qt3DInput::QKeyboardHandler Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DInput_QKeyboardHandler'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *Qt3DInput::QKeyboardHandler::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qkeyboardhandler.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DInput::QKeyboardHandler::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK9Qt3DInput16QKeyboardHandler10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def sourceDevice(self) -> Optional[Qt3DInput.QKeyboardDevice]:
    """
    Calls Qt's 'Qt3DInput::QKeyboardDevice
    *Qt3DInput::QKeyboardHandler::sourceDevice() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qkeyboardhandler.html#sourceDevice

    Returns
    -------

    Optional[Qt3DInput.QKeyboardDevice]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Qt3DInput::QKeyboardDevice
    #      *Qt3DInput::QKeyboardHandler::sourceDevice() const
    address = self.uglySide.call(
        'ritual_ZNK9Qt3DInput16QKeyboardHandler12sourceDeviceEv',
    )
    return Qt3DInput.QKeyboardDevice._cuteAt(address)

  def focus(self) -> bool:
    """
    Calls Qt's 'bool Qt3DInput::QKeyboardHandler::focus() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qkeyboardhandler.html#focus
    """
    #  bool Qt3DInput::QKeyboardHandler::focus() const
    return self.uglySide.call(
        'ritual_ZNK9Qt3DInput16QKeyboardHandler5focusEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(WAIT['Qt3DInput.QKeyboardDevice'])
  @overload(NoneType)
  def setSourceDevice(
      self,
      keyboardDevice: Optional[Qt3DInput.QKeyboardDevice],
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DInput::QKeyboardHandler::setSourceDevice(Qt3DInput::QKeyboardDevice
    *keyboardDevice)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qkeyboardhandler.html#setSourceDevice

    Parameters
    ----------

    keyboardDevice : Optional[Qt3DInput.QKeyboardDevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DInput::QKeyboardHandler::setSourceDevice(Qt3DInput::
    #      QKeyboardDevice *keyboardDevice)
    self.uglySide.call(
        'ritual_ZN9Qt3DInput16QKeyboardHandler15setSourceDeviceEPNS_15QKeyb'
        'oardDeviceE',
        self._addressOf(keyboardDevice),
    )

  @overload(bool)
  def setFocus(self, focus: bool) -> None:
    """
    Calls Qt's 'void Qt3DInput::QKeyboardHandler::setFocus(bool focus)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qkeyboardhandler.html#setFocus

    Parameters
    ----------

    focus : bool
      Passed on as it is.
    """
    #  void Qt3DInput::QKeyboardHandler::setFocus(bool focus)
    self.uglySide.call(
        'ritual_ZN9Qt3DInput16QKeyboardHandler8setFocusEb', focus,
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
  @overload(Qt3DCore.QNode)
  @overload(NoneType)
  def __init__(self, parent: Optional[Qt3DCore.QNode] = None) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DInput::QKeyboardHandler::QKeyboardHandler(QNode *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qkeyboardhandler.html#QKeyboardHandler

    Parameters
    ----------

    parent : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DInput::QKeyboardHandler::QKeyboardHandler(QNode *parent)
    self._noteCreation(QKeyboardHandler, lambda: Rituals.call(
        'ritual_ZN9Qt3DInput16QKeyboardHandlerC1EPN8Qt3DCore5QNodeE',
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

  @overload(WAIT['Qt3DInput.QKeyboardDevice'])
  @overload(NoneType)
  def sourceDeviceChanged(
      self,
      keyboardDevice: Optional[Qt3DInput.QKeyboardDevice],
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DInput::QKeyboardHandler::sourceDeviceChanged(QKeyboardDevice
    *keyboardDevice)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qkeyboardhandler.html

    Parameters
    ----------

    keyboardDevice : Optional[Qt3DInput.QKeyboardDevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DInput::QKeyboardHandler::sourceDeviceChanged(QKeyboardDevice
    #      *keyboardDevice)
    self.uglySide.call(
        'ritual_ZN9Qt3DInput16QKeyboardHandler19sourceDeviceChangedEPNS_15Q'
        'KeyboardDeviceE',
        self._addressOf(keyboardDevice),
    )

  @overload(bool)
  def focusChanged(self, focus: bool) -> None:
    """
    Calls Qt's 'void Qt3DInput::QKeyboardHandler::focusChanged(bool focus)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qkeyboardhandler.html#focusChanged

    Parameters
    ----------

    focus : bool
      Passed on as it is.
    """
    #  void Qt3DInput::QKeyboardHandler::focusChanged(bool focus)
    self.uglySide.call(
        'ritual_ZN9Qt3DInput16QKeyboardHandler12focusChangedEb', focus,
    )

  @overload(WAIT['Qt3DInput.QKeyEvent'])
  @overload(NoneType)
  def digit0Pressed(self, event: Optional[Qt3DInput.QKeyEvent]) -> None:
    """
    Calls Qt's 'void
    Qt3DInput::QKeyboardHandler::digit0Pressed(Qt3DInput::QKeyEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qkeyboardhandler.html#digit0Pressed

    Parameters
    ----------

    event : Optional[Qt3DInput.QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DInput::QKeyboardHandler::digit0Pressed(Qt3DInput::QKeyEvent
    #      *event)
    self.uglySide.call(
        'ritual_ZN9Qt3DInput16QKeyboardHandler13digit0PressedEPNS_9QKeyEven'
        'tE',
        self._addressOf(event),
    )

  @overload(WAIT['Qt3DInput.QKeyEvent'])
  @overload(NoneType)
  def digit1Pressed(self, event: Optional[Qt3DInput.QKeyEvent]) -> None:
    """
    Calls Qt's 'void
    Qt3DInput::QKeyboardHandler::digit1Pressed(Qt3DInput::QKeyEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qkeyboardhandler.html#digit1Pressed

    Parameters
    ----------

    event : Optional[Qt3DInput.QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DInput::QKeyboardHandler::digit1Pressed(Qt3DInput::QKeyEvent
    #      *event)
    self.uglySide.call(
        'ritual_ZN9Qt3DInput16QKeyboardHandler13digit1PressedEPNS_9QKeyEven'
        'tE',
        self._addressOf(event),
    )

  @overload(WAIT['Qt3DInput.QKeyEvent'])
  @overload(NoneType)
  def digit2Pressed(self, event: Optional[Qt3DInput.QKeyEvent]) -> None:
    """
    Calls Qt's 'void
    Qt3DInput::QKeyboardHandler::digit2Pressed(Qt3DInput::QKeyEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qkeyboardhandler.html#digit2Pressed

    Parameters
    ----------

    event : Optional[Qt3DInput.QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DInput::QKeyboardHandler::digit2Pressed(Qt3DInput::QKeyEvent
    #      *event)
    self.uglySide.call(
        'ritual_ZN9Qt3DInput16QKeyboardHandler13digit2PressedEPNS_9QKeyEven'
        'tE',
        self._addressOf(event),
    )

  @overload(WAIT['Qt3DInput.QKeyEvent'])
  @overload(NoneType)
  def digit3Pressed(self, event: Optional[Qt3DInput.QKeyEvent]) -> None:
    """
    Calls Qt's 'void
    Qt3DInput::QKeyboardHandler::digit3Pressed(Qt3DInput::QKeyEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qkeyboardhandler.html#digit3Pressed

    Parameters
    ----------

    event : Optional[Qt3DInput.QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DInput::QKeyboardHandler::digit3Pressed(Qt3DInput::QKeyEvent
    #      *event)
    self.uglySide.call(
        'ritual_ZN9Qt3DInput16QKeyboardHandler13digit3PressedEPNS_9QKeyEven'
        'tE',
        self._addressOf(event),
    )

  @overload(WAIT['Qt3DInput.QKeyEvent'])
  @overload(NoneType)
  def digit4Pressed(self, event: Optional[Qt3DInput.QKeyEvent]) -> None:
    """
    Calls Qt's 'void
    Qt3DInput::QKeyboardHandler::digit4Pressed(Qt3DInput::QKeyEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qkeyboardhandler.html#digit4Pressed

    Parameters
    ----------

    event : Optional[Qt3DInput.QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DInput::QKeyboardHandler::digit4Pressed(Qt3DInput::QKeyEvent
    #      *event)
    self.uglySide.call(
        'ritual_ZN9Qt3DInput16QKeyboardHandler13digit4PressedEPNS_9QKeyEven'
        'tE',
        self._addressOf(event),
    )

  @overload(WAIT['Qt3DInput.QKeyEvent'])
  @overload(NoneType)
  def digit5Pressed(self, event: Optional[Qt3DInput.QKeyEvent]) -> None:
    """
    Calls Qt's 'void
    Qt3DInput::QKeyboardHandler::digit5Pressed(Qt3DInput::QKeyEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qkeyboardhandler.html#digit5Pressed

    Parameters
    ----------

    event : Optional[Qt3DInput.QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DInput::QKeyboardHandler::digit5Pressed(Qt3DInput::QKeyEvent
    #      *event)
    self.uglySide.call(
        'ritual_ZN9Qt3DInput16QKeyboardHandler13digit5PressedEPNS_9QKeyEven'
        'tE',
        self._addressOf(event),
    )

  @overload(WAIT['Qt3DInput.QKeyEvent'])
  @overload(NoneType)
  def digit6Pressed(self, event: Optional[Qt3DInput.QKeyEvent]) -> None:
    """
    Calls Qt's 'void
    Qt3DInput::QKeyboardHandler::digit6Pressed(Qt3DInput::QKeyEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qkeyboardhandler.html#digit6Pressed

    Parameters
    ----------

    event : Optional[Qt3DInput.QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DInput::QKeyboardHandler::digit6Pressed(Qt3DInput::QKeyEvent
    #      *event)
    self.uglySide.call(
        'ritual_ZN9Qt3DInput16QKeyboardHandler13digit6PressedEPNS_9QKeyEven'
        'tE',
        self._addressOf(event),
    )

  @overload(WAIT['Qt3DInput.QKeyEvent'])
  @overload(NoneType)
  def digit7Pressed(self, event: Optional[Qt3DInput.QKeyEvent]) -> None:
    """
    Calls Qt's 'void
    Qt3DInput::QKeyboardHandler::digit7Pressed(Qt3DInput::QKeyEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qkeyboardhandler.html#digit7Pressed

    Parameters
    ----------

    event : Optional[Qt3DInput.QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DInput::QKeyboardHandler::digit7Pressed(Qt3DInput::QKeyEvent
    #      *event)
    self.uglySide.call(
        'ritual_ZN9Qt3DInput16QKeyboardHandler13digit7PressedEPNS_9QKeyEven'
        'tE',
        self._addressOf(event),
    )

  @overload(WAIT['Qt3DInput.QKeyEvent'])
  @overload(NoneType)
  def digit8Pressed(self, event: Optional[Qt3DInput.QKeyEvent]) -> None:
    """
    Calls Qt's 'void
    Qt3DInput::QKeyboardHandler::digit8Pressed(Qt3DInput::QKeyEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qkeyboardhandler.html#digit8Pressed

    Parameters
    ----------

    event : Optional[Qt3DInput.QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DInput::QKeyboardHandler::digit8Pressed(Qt3DInput::QKeyEvent
    #      *event)
    self.uglySide.call(
        'ritual_ZN9Qt3DInput16QKeyboardHandler13digit8PressedEPNS_9QKeyEven'
        'tE',
        self._addressOf(event),
    )

  @overload(WAIT['Qt3DInput.QKeyEvent'])
  @overload(NoneType)
  def digit9Pressed(self, event: Optional[Qt3DInput.QKeyEvent]) -> None:
    """
    Calls Qt's 'void
    Qt3DInput::QKeyboardHandler::digit9Pressed(Qt3DInput::QKeyEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qkeyboardhandler.html#digit9Pressed

    Parameters
    ----------

    event : Optional[Qt3DInput.QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DInput::QKeyboardHandler::digit9Pressed(Qt3DInput::QKeyEvent
    #      *event)
    self.uglySide.call(
        'ritual_ZN9Qt3DInput16QKeyboardHandler13digit9PressedEPNS_9QKeyEven'
        'tE',
        self._addressOf(event),
    )

  @overload(WAIT['Qt3DInput.QKeyEvent'])
  @overload(NoneType)
  def leftPressed(self, event: Optional[Qt3DInput.QKeyEvent]) -> None:
    """
    Calls Qt's 'void
    Qt3DInput::QKeyboardHandler::leftPressed(Qt3DInput::QKeyEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qkeyboardhandler.html#leftPressed

    Parameters
    ----------

    event : Optional[Qt3DInput.QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DInput::QKeyboardHandler::leftPressed(Qt3DInput::QKeyEvent
    #      *event)
    self.uglySide.call(
        'ritual_ZN9Qt3DInput16QKeyboardHandler11leftPressedEPNS_9QKeyEventE',
        self._addressOf(event),
    )

  @overload(WAIT['Qt3DInput.QKeyEvent'])
  @overload(NoneType)
  def rightPressed(self, event: Optional[Qt3DInput.QKeyEvent]) -> None:
    """
    Calls Qt's 'void
    Qt3DInput::QKeyboardHandler::rightPressed(Qt3DInput::QKeyEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qkeyboardhandler.html#rightPressed

    Parameters
    ----------

    event : Optional[Qt3DInput.QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DInput::QKeyboardHandler::rightPressed(Qt3DInput::QKeyEvent
    #      *event)
    self.uglySide.call(
        'ritual_ZN9Qt3DInput16QKeyboardHandler12rightPressedEPNS_9QKeyEvent'
        'E',
        self._addressOf(event),
    )

  @overload(WAIT['Qt3DInput.QKeyEvent'])
  @overload(NoneType)
  def upPressed(self, event: Optional[Qt3DInput.QKeyEvent]) -> None:
    """
    Calls Qt's 'void
    Qt3DInput::QKeyboardHandler::upPressed(Qt3DInput::QKeyEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qkeyboardhandler.html#upPressed

    Parameters
    ----------

    event : Optional[Qt3DInput.QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DInput::QKeyboardHandler::upPressed(Qt3DInput::QKeyEvent
    #      *event)
    self.uglySide.call(
        'ritual_ZN9Qt3DInput16QKeyboardHandler9upPressedEPNS_9QKeyEventE',
        self._addressOf(event),
    )

  @overload(WAIT['Qt3DInput.QKeyEvent'])
  @overload(NoneType)
  def downPressed(self, event: Optional[Qt3DInput.QKeyEvent]) -> None:
    """
    Calls Qt's 'void
    Qt3DInput::QKeyboardHandler::downPressed(Qt3DInput::QKeyEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qkeyboardhandler.html#downPressed

    Parameters
    ----------

    event : Optional[Qt3DInput.QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DInput::QKeyboardHandler::downPressed(Qt3DInput::QKeyEvent
    #      *event)
    self.uglySide.call(
        'ritual_ZN9Qt3DInput16QKeyboardHandler11downPressedEPNS_9QKeyEventE',
        self._addressOf(event),
    )

  @overload(WAIT['Qt3DInput.QKeyEvent'])
  @overload(NoneType)
  def tabPressed(self, event: Optional[Qt3DInput.QKeyEvent]) -> None:
    """
    Calls Qt's 'void
    Qt3DInput::QKeyboardHandler::tabPressed(Qt3DInput::QKeyEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qkeyboardhandler.html#tabPressed

    Parameters
    ----------

    event : Optional[Qt3DInput.QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DInput::QKeyboardHandler::tabPressed(Qt3DInput::QKeyEvent
    #      *event)
    self.uglySide.call(
        'ritual_ZN9Qt3DInput16QKeyboardHandler10tabPressedEPNS_9QKeyEventE',
        self._addressOf(event),
    )

  @overload(WAIT['Qt3DInput.QKeyEvent'])
  @overload(NoneType)
  def backtabPressed(self, event: Optional[Qt3DInput.QKeyEvent]) -> None:
    """
    Calls Qt's 'void
    Qt3DInput::QKeyboardHandler::backtabPressed(Qt3DInput::QKeyEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qkeyboardhandler.html#backtabPressed

    Parameters
    ----------

    event : Optional[Qt3DInput.QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DInput::QKeyboardHandler::backtabPressed(Qt3DInput::QKeyEvent
    #      *event)
    self.uglySide.call(
        'ritual_ZN9Qt3DInput16QKeyboardHandler14backtabPressedEPNS_9QKeyEve'
        'ntE',
        self._addressOf(event),
    )

  @overload(WAIT['Qt3DInput.QKeyEvent'])
  @overload(NoneType)
  def asteriskPressed(self, event: Optional[Qt3DInput.QKeyEvent]) -> None:
    """
    Calls Qt's 'void
    Qt3DInput::QKeyboardHandler::asteriskPressed(Qt3DInput::QKeyEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qkeyboardhandler.html#asteriskPressed

    Parameters
    ----------

    event : Optional[Qt3DInput.QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DInput::QKeyboardHandler::asteriskPressed(Qt3DInput::QKeyEvent
    #      *event)
    self.uglySide.call(
        'ritual_ZN9Qt3DInput16QKeyboardHandler15asteriskPressedEPNS_9QKeyEv'
        'entE',
        self._addressOf(event),
    )

  @overload(WAIT['Qt3DInput.QKeyEvent'])
  @overload(NoneType)
  def numberSignPressed(self, event: Optional[Qt3DInput.QKeyEvent]) -> None:
    """
    Calls Qt's 'void
    Qt3DInput::QKeyboardHandler::numberSignPressed(Qt3DInput::QKeyEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qkeyboardhandler.html#numberSignPressed

    Parameters
    ----------

    event : Optional[Qt3DInput.QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DInput::QKeyboardHandler::numberSignPressed(Qt3DInput::
    #      QKeyEvent *event)
    self.uglySide.call(
        'ritual_ZN9Qt3DInput16QKeyboardHandler17numberSignPressedEPNS_9QKey'
        'EventE',
        self._addressOf(event),
    )

  @overload(WAIT['Qt3DInput.QKeyEvent'])
  @overload(NoneType)
  def escapePressed(self, event: Optional[Qt3DInput.QKeyEvent]) -> None:
    """
    Calls Qt's 'void
    Qt3DInput::QKeyboardHandler::escapePressed(Qt3DInput::QKeyEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qkeyboardhandler.html#escapePressed

    Parameters
    ----------

    event : Optional[Qt3DInput.QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DInput::QKeyboardHandler::escapePressed(Qt3DInput::QKeyEvent
    #      *event)
    self.uglySide.call(
        'ritual_ZN9Qt3DInput16QKeyboardHandler13escapePressedEPNS_9QKeyEven'
        'tE',
        self._addressOf(event),
    )

  @overload(WAIT['Qt3DInput.QKeyEvent'])
  @overload(NoneType)
  def returnPressed(self, event: Optional[Qt3DInput.QKeyEvent]) -> None:
    """
    Calls Qt's 'void
    Qt3DInput::QKeyboardHandler::returnPressed(Qt3DInput::QKeyEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qkeyboardhandler.html#returnPressed

    Parameters
    ----------

    event : Optional[Qt3DInput.QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DInput::QKeyboardHandler::returnPressed(Qt3DInput::QKeyEvent
    #      *event)
    self.uglySide.call(
        'ritual_ZN9Qt3DInput16QKeyboardHandler13returnPressedEPNS_9QKeyEven'
        'tE',
        self._addressOf(event),
    )

  @overload(WAIT['Qt3DInput.QKeyEvent'])
  @overload(NoneType)
  def enterPressed(self, event: Optional[Qt3DInput.QKeyEvent]) -> None:
    """
    Calls Qt's 'void
    Qt3DInput::QKeyboardHandler::enterPressed(Qt3DInput::QKeyEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qkeyboardhandler.html#enterPressed

    Parameters
    ----------

    event : Optional[Qt3DInput.QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DInput::QKeyboardHandler::enterPressed(Qt3DInput::QKeyEvent
    #      *event)
    self.uglySide.call(
        'ritual_ZN9Qt3DInput16QKeyboardHandler12enterPressedEPNS_9QKeyEvent'
        'E',
        self._addressOf(event),
    )

  @overload(WAIT['Qt3DInput.QKeyEvent'])
  @overload(NoneType)
  def deletePressed(self, event: Optional[Qt3DInput.QKeyEvent]) -> None:
    """
    Calls Qt's 'void
    Qt3DInput::QKeyboardHandler::deletePressed(Qt3DInput::QKeyEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qkeyboardhandler.html#deletePressed

    Parameters
    ----------

    event : Optional[Qt3DInput.QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DInput::QKeyboardHandler::deletePressed(Qt3DInput::QKeyEvent
    #      *event)
    self.uglySide.call(
        'ritual_ZN9Qt3DInput16QKeyboardHandler13deletePressedEPNS_9QKeyEven'
        'tE',
        self._addressOf(event),
    )

  @overload(WAIT['Qt3DInput.QKeyEvent'])
  @overload(NoneType)
  def spacePressed(self, event: Optional[Qt3DInput.QKeyEvent]) -> None:
    """
    Calls Qt's 'void
    Qt3DInput::QKeyboardHandler::spacePressed(Qt3DInput::QKeyEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qkeyboardhandler.html#spacePressed

    Parameters
    ----------

    event : Optional[Qt3DInput.QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DInput::QKeyboardHandler::spacePressed(Qt3DInput::QKeyEvent
    #      *event)
    self.uglySide.call(
        'ritual_ZN9Qt3DInput16QKeyboardHandler12spacePressedEPNS_9QKeyEvent'
        'E',
        self._addressOf(event),
    )

  @overload(WAIT['Qt3DInput.QKeyEvent'])
  @overload(NoneType)
  def backPressed(self, event: Optional[Qt3DInput.QKeyEvent]) -> None:
    """
    Calls Qt's 'void
    Qt3DInput::QKeyboardHandler::backPressed(Qt3DInput::QKeyEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qkeyboardhandler.html#backPressed

    Parameters
    ----------

    event : Optional[Qt3DInput.QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DInput::QKeyboardHandler::backPressed(Qt3DInput::QKeyEvent
    #      *event)
    self.uglySide.call(
        'ritual_ZN9Qt3DInput16QKeyboardHandler11backPressedEPNS_9QKeyEventE',
        self._addressOf(event),
    )

  @overload(WAIT['Qt3DInput.QKeyEvent'])
  @overload(NoneType)
  def cancelPressed(self, event: Optional[Qt3DInput.QKeyEvent]) -> None:
    """
    Calls Qt's 'void
    Qt3DInput::QKeyboardHandler::cancelPressed(Qt3DInput::QKeyEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qkeyboardhandler.html#cancelPressed

    Parameters
    ----------

    event : Optional[Qt3DInput.QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DInput::QKeyboardHandler::cancelPressed(Qt3DInput::QKeyEvent
    #      *event)
    self.uglySide.call(
        'ritual_ZN9Qt3DInput16QKeyboardHandler13cancelPressedEPNS_9QKeyEven'
        'tE',
        self._addressOf(event),
    )

  @overload(WAIT['Qt3DInput.QKeyEvent'])
  @overload(NoneType)
  def selectPressed(self, event: Optional[Qt3DInput.QKeyEvent]) -> None:
    """
    Calls Qt's 'void
    Qt3DInput::QKeyboardHandler::selectPressed(Qt3DInput::QKeyEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qkeyboardhandler.html#selectPressed

    Parameters
    ----------

    event : Optional[Qt3DInput.QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DInput::QKeyboardHandler::selectPressed(Qt3DInput::QKeyEvent
    #      *event)
    self.uglySide.call(
        'ritual_ZN9Qt3DInput16QKeyboardHandler13selectPressedEPNS_9QKeyEven'
        'tE',
        self._addressOf(event),
    )

  @overload(WAIT['Qt3DInput.QKeyEvent'])
  @overload(NoneType)
  def yesPressed(self, event: Optional[Qt3DInput.QKeyEvent]) -> None:
    """
    Calls Qt's 'void
    Qt3DInput::QKeyboardHandler::yesPressed(Qt3DInput::QKeyEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qkeyboardhandler.html#yesPressed

    Parameters
    ----------

    event : Optional[Qt3DInput.QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DInput::QKeyboardHandler::yesPressed(Qt3DInput::QKeyEvent
    #      *event)
    self.uglySide.call(
        'ritual_ZN9Qt3DInput16QKeyboardHandler10yesPressedEPNS_9QKeyEventE',
        self._addressOf(event),
    )

  @overload(WAIT['Qt3DInput.QKeyEvent'])
  @overload(NoneType)
  def noPressed(self, event: Optional[Qt3DInput.QKeyEvent]) -> None:
    """
    Calls Qt's 'void
    Qt3DInput::QKeyboardHandler::noPressed(Qt3DInput::QKeyEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qkeyboardhandler.html#noPressed

    Parameters
    ----------

    event : Optional[Qt3DInput.QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DInput::QKeyboardHandler::noPressed(Qt3DInput::QKeyEvent
    #      *event)
    self.uglySide.call(
        'ritual_ZN9Qt3DInput16QKeyboardHandler9noPressedEPNS_9QKeyEventE',
        self._addressOf(event),
    )

  @overload(WAIT['Qt3DInput.QKeyEvent'])
  @overload(NoneType)
  def context1Pressed(self, event: Optional[Qt3DInput.QKeyEvent]) -> None:
    """
    Calls Qt's 'void
    Qt3DInput::QKeyboardHandler::context1Pressed(Qt3DInput::QKeyEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qkeyboardhandler.html#context1Pressed

    Parameters
    ----------

    event : Optional[Qt3DInput.QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DInput::QKeyboardHandler::context1Pressed(Qt3DInput::QKeyEvent
    #      *event)
    self.uglySide.call(
        'ritual_ZN9Qt3DInput16QKeyboardHandler15context1PressedEPNS_9QKeyEv'
        'entE',
        self._addressOf(event),
    )

  @overload(WAIT['Qt3DInput.QKeyEvent'])
  @overload(NoneType)
  def context2Pressed(self, event: Optional[Qt3DInput.QKeyEvent]) -> None:
    """
    Calls Qt's 'void
    Qt3DInput::QKeyboardHandler::context2Pressed(Qt3DInput::QKeyEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qkeyboardhandler.html#context2Pressed

    Parameters
    ----------

    event : Optional[Qt3DInput.QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DInput::QKeyboardHandler::context2Pressed(Qt3DInput::QKeyEvent
    #      *event)
    self.uglySide.call(
        'ritual_ZN9Qt3DInput16QKeyboardHandler15context2PressedEPNS_9QKeyEv'
        'entE',
        self._addressOf(event),
    )

  @overload(WAIT['Qt3DInput.QKeyEvent'])
  @overload(NoneType)
  def context3Pressed(self, event: Optional[Qt3DInput.QKeyEvent]) -> None:
    """
    Calls Qt's 'void
    Qt3DInput::QKeyboardHandler::context3Pressed(Qt3DInput::QKeyEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qkeyboardhandler.html#context3Pressed

    Parameters
    ----------

    event : Optional[Qt3DInput.QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DInput::QKeyboardHandler::context3Pressed(Qt3DInput::QKeyEvent
    #      *event)
    self.uglySide.call(
        'ritual_ZN9Qt3DInput16QKeyboardHandler15context3PressedEPNS_9QKeyEv'
        'entE',
        self._addressOf(event),
    )

  @overload(WAIT['Qt3DInput.QKeyEvent'])
  @overload(NoneType)
  def context4Pressed(self, event: Optional[Qt3DInput.QKeyEvent]) -> None:
    """
    Calls Qt's 'void
    Qt3DInput::QKeyboardHandler::context4Pressed(Qt3DInput::QKeyEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qkeyboardhandler.html#context4Pressed

    Parameters
    ----------

    event : Optional[Qt3DInput.QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DInput::QKeyboardHandler::context4Pressed(Qt3DInput::QKeyEvent
    #      *event)
    self.uglySide.call(
        'ritual_ZN9Qt3DInput16QKeyboardHandler15context4PressedEPNS_9QKeyEv'
        'entE',
        self._addressOf(event),
    )

  @overload(WAIT['Qt3DInput.QKeyEvent'])
  @overload(NoneType)
  def callPressed(self, event: Optional[Qt3DInput.QKeyEvent]) -> None:
    """
    Calls Qt's 'void
    Qt3DInput::QKeyboardHandler::callPressed(Qt3DInput::QKeyEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qkeyboardhandler.html#callPressed

    Parameters
    ----------

    event : Optional[Qt3DInput.QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DInput::QKeyboardHandler::callPressed(Qt3DInput::QKeyEvent
    #      *event)
    self.uglySide.call(
        'ritual_ZN9Qt3DInput16QKeyboardHandler11callPressedEPNS_9QKeyEventE',
        self._addressOf(event),
    )

  @overload(WAIT['Qt3DInput.QKeyEvent'])
  @overload(NoneType)
  def hangupPressed(self, event: Optional[Qt3DInput.QKeyEvent]) -> None:
    """
    Calls Qt's 'void
    Qt3DInput::QKeyboardHandler::hangupPressed(Qt3DInput::QKeyEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qkeyboardhandler.html#hangupPressed

    Parameters
    ----------

    event : Optional[Qt3DInput.QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DInput::QKeyboardHandler::hangupPressed(Qt3DInput::QKeyEvent
    #      *event)
    self.uglySide.call(
        'ritual_ZN9Qt3DInput16QKeyboardHandler13hangupPressedEPNS_9QKeyEven'
        'tE',
        self._addressOf(event),
    )

  @overload(WAIT['Qt3DInput.QKeyEvent'])
  @overload(NoneType)
  def flipPressed(self, event: Optional[Qt3DInput.QKeyEvent]) -> None:
    """
    Calls Qt's 'void
    Qt3DInput::QKeyboardHandler::flipPressed(Qt3DInput::QKeyEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qkeyboardhandler.html#flipPressed

    Parameters
    ----------

    event : Optional[Qt3DInput.QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DInput::QKeyboardHandler::flipPressed(Qt3DInput::QKeyEvent
    #      *event)
    self.uglySide.call(
        'ritual_ZN9Qt3DInput16QKeyboardHandler11flipPressedEPNS_9QKeyEventE',
        self._addressOf(event),
    )

  @overload(WAIT['Qt3DInput.QKeyEvent'])
  @overload(NoneType)
  def menuPressed(self, event: Optional[Qt3DInput.QKeyEvent]) -> None:
    """
    Calls Qt's 'void
    Qt3DInput::QKeyboardHandler::menuPressed(Qt3DInput::QKeyEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qkeyboardhandler.html#menuPressed

    Parameters
    ----------

    event : Optional[Qt3DInput.QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DInput::QKeyboardHandler::menuPressed(Qt3DInput::QKeyEvent
    #      *event)
    self.uglySide.call(
        'ritual_ZN9Qt3DInput16QKeyboardHandler11menuPressedEPNS_9QKeyEventE',
        self._addressOf(event),
    )

  @overload(WAIT['Qt3DInput.QKeyEvent'])
  @overload(NoneType)
  def volumeUpPressed(self, event: Optional[Qt3DInput.QKeyEvent]) -> None:
    """
    Calls Qt's 'void
    Qt3DInput::QKeyboardHandler::volumeUpPressed(Qt3DInput::QKeyEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qkeyboardhandler.html#volumeUpPressed

    Parameters
    ----------

    event : Optional[Qt3DInput.QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DInput::QKeyboardHandler::volumeUpPressed(Qt3DInput::QKeyEvent
    #      *event)
    self.uglySide.call(
        'ritual_ZN9Qt3DInput16QKeyboardHandler15volumeUpPressedEPNS_9QKeyEv'
        'entE',
        self._addressOf(event),
    )

  @overload(WAIT['Qt3DInput.QKeyEvent'])
  @overload(NoneType)
  def volumeDownPressed(self, event: Optional[Qt3DInput.QKeyEvent]) -> None:
    """
    Calls Qt's 'void
    Qt3DInput::QKeyboardHandler::volumeDownPressed(Qt3DInput::QKeyEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qkeyboardhandler.html#volumeDownPressed

    Parameters
    ----------

    event : Optional[Qt3DInput.QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DInput::QKeyboardHandler::volumeDownPressed(Qt3DInput::
    #      QKeyEvent *event)
    self.uglySide.call(
        'ritual_ZN9Qt3DInput16QKeyboardHandler17volumeDownPressedEPNS_9QKey'
        'EventE',
        self._addressOf(event),
    )

  @overload(WAIT['Qt3DInput.QKeyEvent'])
  @overload(NoneType)
  def pressed(self, event: Optional[Qt3DInput.QKeyEvent]) -> None:
    """
    Calls Qt's 'void
    Qt3DInput::QKeyboardHandler::pressed(Qt3DInput::QKeyEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qkeyboardhandler.html#pressed

    Parameters
    ----------

    event : Optional[Qt3DInput.QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DInput::QKeyboardHandler::pressed(Qt3DInput::QKeyEvent *event)
    self.uglySide.call(
        'ritual_ZN9Qt3DInput16QKeyboardHandler7pressedEPNS_9QKeyEventE',
        self._addressOf(event),
    )

  @overload(WAIT['Qt3DInput.QKeyEvent'])
  @overload(NoneType)
  def released(self, event: Optional[Qt3DInput.QKeyEvent]) -> None:
    """
    Calls Qt's 'void
    Qt3DInput::QKeyboardHandler::released(Qt3DInput::QKeyEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qkeyboardhandler.html#released

    Parameters
    ----------

    event : Optional[Qt3DInput.QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DInput::QKeyboardHandler::released(Qt3DInput::QKeyEvent
    #      *event)
    self.uglySide.call(
        'ritual_ZN9Qt3DInput16QKeyboardHandler8releasedEPNS_9QKeyEventE',
        self._addressOf(event),
    )

  def d_func(self) -> Optional[Qt3DInput.QKeyboardHandlerPrivate]:
    """
    Calls Qt's 'QKeyboardHandlerPrivate
    *Qt3DInput::QKeyboardHandler::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qkeyboardhandler.html#d_func

    Returns
    -------

    Optional[Qt3DInput.QKeyboardHandlerPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QKeyboardHandlerPrivate *Qt3DInput::QKeyboardHandler::d_func()
    address = self.uglySide.call(
        'ritual_ZN9Qt3DInput16QKeyboardHandler6d_funcEv',
    )
    return Qt3DInput.QKeyboardHandlerPrivate._cuteAt(address)
