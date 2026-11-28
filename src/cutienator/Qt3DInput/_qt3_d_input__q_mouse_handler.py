"""
Qt3DInput::QMouseHandler binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DInput/qmousehandler.h, Qt 6.12.0. Changes made here are lost.
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


class QMouseHandler(Qt3DCore.QComponent):
  """
  The cute side of Qt's Qt3DInput::QMouseHandler: a plain Python object
  standing in front of one C++ Qt3DInput::QMouseHandler.

  It is built on the cute 'Qt3DCore::QComponent', as Qt's
  Qt3DInput::QMouseHandler is built on Qt's Qt3DCore::QComponent, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DInput::QMouseHandler that has a ritual and that
  Python can call so far, 18 names in all: 'metaObject', 'tr',
  'sourceDevice', 'containsMouse', 'setSourceDevice', 'sourceDeviceChanged',
  'containsMouseChanged', 'clicked', 'doubleClicked', 'entered', 'exited',
  'pressed', 'released', 'pressAndHold', 'positionChanged', 'wheel',
  'setContainsMouse', 'd_func'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DInput::QMouseHandler::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int Qt3DInput::QMouseHandler::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DInput::QMouseHandler::~QMouseHandler()': the destructor: Python
    never removes a C++ Qt3DInput::QMouseHandler.
  - Qt's 'const QMouseHandlerPrivate *Qt3DInput::QMouseHandler::d_func()
    const': takes in Python what 'QMouseHandlerPrivate
    *Qt3DInput::QMouseHandler::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 25 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DInput::QMouseHandler is created at the first use, not by
    'Qt3DInput::QMouseHandler(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DInput::QMouseHandler.
  - Qt tells when it has removed the C++ Qt3DInput::QMouseHandler. Every call
    on the cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString Qt3DInput::QMouseHandler::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dinput-qmousehandler.html#tr

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
    #  QString Qt3DInput::QMouseHandler::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN9Qt3DInput13QMouseHandler2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DInput::QMouseHandler'

  #  A C++ Qt3DInput::QMouseHandler Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DInput_QMouseHandler'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *Qt3DInput::QMouseHandler::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qmousehandler.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DInput::QMouseHandler::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK9Qt3DInput13QMouseHandler10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def sourceDevice(self) -> Optional[Qt3DInput.QMouseDevice]:
    """
    Calls Qt's 'QMouseDevice *Qt3DInput::QMouseHandler::sourceDevice()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qmousehandler.html#sourceDevice

    Returns
    -------

    Optional[Qt3DInput.QMouseDevice]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QMouseDevice *Qt3DInput::QMouseHandler::sourceDevice() const
    address = self.uglySide.call(
        'ritual_ZNK9Qt3DInput13QMouseHandler12sourceDeviceEv',
    )
    return Qt3DInput.QMouseDevice._cuteAt(address)

  def containsMouse(self) -> bool:
    """
    Calls Qt's 'bool Qt3DInput::QMouseHandler::containsMouse() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qmousehandler.html#containsMouse
    """
    #  bool Qt3DInput::QMouseHandler::containsMouse() const
    return self.uglySide.call(
        'ritual_ZNK9Qt3DInput13QMouseHandler13containsMouseEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(WAIT['Qt3DInput.QMouseDevice'])
  @overload(NoneType)
  def setSourceDevice(
      self,
      mouseDevice: Optional[Qt3DInput.QMouseDevice],
  ) -> None:
    """
    Calls Qt's 'void Qt3DInput::QMouseHandler::setSourceDevice(QMouseDevice
    *mouseDevice)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qmousehandler.html#setSourceDevice

    Parameters
    ----------

    mouseDevice : Optional[Qt3DInput.QMouseDevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DInput::QMouseHandler::setSourceDevice(QMouseDevice
    #      *mouseDevice)
    self.uglySide.call(
        'ritual_ZN9Qt3DInput13QMouseHandler15setSourceDeviceEPNS_12QMouseDe'
        'viceE',
        self._addressOf(mouseDevice),
    )

  @overload(bool)
  def setContainsMouse(self, contains: bool) -> None:
    """
    Calls Qt's 'void Qt3DInput::QMouseHandler::setContainsMouse(bool
    contains)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qmousehandler.html#setContainsMouse

    Parameters
    ----------

    contains : bool
      Passed on as it is.
    """
    #  void Qt3DInput::QMouseHandler::setContainsMouse(bool contains)
    self.uglySide.call(
        'ritual_ZN9Qt3DInput13QMouseHandler16setContainsMouseEb', contains,
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
    'Qt3DInput::QMouseHandler::QMouseHandler(QNode *parent)', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qmousehandler.html#QMouseHandler

    Parameters
    ----------

    parent : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DInput::QMouseHandler::QMouseHandler(QNode *parent)
    self._noteCreation(QMouseHandler, lambda: Rituals.call(
        'ritual_ZN9Qt3DInput13QMouseHandlerC1EPN8Qt3DCore5QNodeE',
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

  @overload(WAIT['Qt3DInput.QMouseDevice'])
  @overload(NoneType)
  def sourceDeviceChanged(
      self,
      mouseDevice: Optional[Qt3DInput.QMouseDevice],
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DInput::QMouseHandler::sourceDeviceChanged(QMouseDevice
    *mouseDevice)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qmousehandler.html#sourceDeviceChanged

    Parameters
    ----------

    mouseDevice : Optional[Qt3DInput.QMouseDevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DInput::QMouseHandler::sourceDeviceChanged(QMouseDevice
    #      *mouseDevice)
    self.uglySide.call(
        'ritual_ZN9Qt3DInput13QMouseHandler19sourceDeviceChangedEPNS_12QMou'
        'seDeviceE',
        self._addressOf(mouseDevice),
    )

  @overload(bool)
  def containsMouseChanged(self, containsMouse: bool) -> None:
    """
    Calls Qt's 'void Qt3DInput::QMouseHandler::containsMouseChanged(bool
    containsMouse)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qmousehandler.html#containsMouseChanged

    Parameters
    ----------

    containsMouse : bool
      Passed on as it is.
    """
    #  void Qt3DInput::QMouseHandler::containsMouseChanged(bool
    #      containsMouse)
    self.uglySide.call(
        'ritual_ZN9Qt3DInput13QMouseHandler20containsMouseChangedEb',
        containsMouse,
    )

  @overload(WAIT['Qt3DInput.QMouseEvent'])
  @overload(NoneType)
  def clicked(self, mouse: Optional[Qt3DInput.QMouseEvent]) -> None:
    """
    Calls Qt's 'void Qt3DInput::QMouseHandler::clicked(Qt3DInput::QMouseEvent
    *mouse)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qmousehandler.html#clicked

    Parameters
    ----------

    mouse : Optional[Qt3DInput.QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DInput::QMouseHandler::clicked(Qt3DInput::QMouseEvent *mouse)
    self.uglySide.call(
        'ritual_ZN9Qt3DInput13QMouseHandler7clickedEPNS_11QMouseEventE',
        self._addressOf(mouse),
    )

  @overload(WAIT['Qt3DInput.QMouseEvent'])
  @overload(NoneType)
  def doubleClicked(self, mouse: Optional[Qt3DInput.QMouseEvent]) -> None:
    """
    Calls Qt's 'void
    Qt3DInput::QMouseHandler::doubleClicked(Qt3DInput::QMouseEvent *mouse)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qmousehandler.html#doubleClicked

    Parameters
    ----------

    mouse : Optional[Qt3DInput.QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DInput::QMouseHandler::doubleClicked(Qt3DInput::QMouseEvent
    #      *mouse)
    self.uglySide.call(
        'ritual_ZN9Qt3DInput13QMouseHandler13doubleClickedEPNS_11QMouseEven'
        'tE',
        self._addressOf(mouse),
    )

  def entered(self) -> None:
    """
    Calls Qt's 'void Qt3DInput::QMouseHandler::entered()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qmousehandler.html#entered
    """
    #  void Qt3DInput::QMouseHandler::entered()
    self.uglySide.call('ritual_ZN9Qt3DInput13QMouseHandler7enteredEv')

  def exited(self) -> None:
    """
    Calls Qt's 'void Qt3DInput::QMouseHandler::exited()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qmousehandler.html#exited
    """
    #  void Qt3DInput::QMouseHandler::exited()
    self.uglySide.call('ritual_ZN9Qt3DInput13QMouseHandler6exitedEv')

  @overload(WAIT['Qt3DInput.QMouseEvent'])
  @overload(NoneType)
  def pressed(self, mouse: Optional[Qt3DInput.QMouseEvent]) -> None:
    """
    Calls Qt's 'void Qt3DInput::QMouseHandler::pressed(Qt3DInput::QMouseEvent
    *mouse)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qmousehandler.html#pressed

    Parameters
    ----------

    mouse : Optional[Qt3DInput.QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DInput::QMouseHandler::pressed(Qt3DInput::QMouseEvent *mouse)
    self.uglySide.call(
        'ritual_ZN9Qt3DInput13QMouseHandler7pressedEPNS_11QMouseEventE',
        self._addressOf(mouse),
    )

  @overload(WAIT['Qt3DInput.QMouseEvent'])
  @overload(NoneType)
  def released(self, mouse: Optional[Qt3DInput.QMouseEvent]) -> None:
    """
    Calls Qt's 'void
    Qt3DInput::QMouseHandler::released(Qt3DInput::QMouseEvent *mouse)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qmousehandler.html#released

    Parameters
    ----------

    mouse : Optional[Qt3DInput.QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DInput::QMouseHandler::released(Qt3DInput::QMouseEvent *mouse)
    self.uglySide.call(
        'ritual_ZN9Qt3DInput13QMouseHandler8releasedEPNS_11QMouseEventE',
        self._addressOf(mouse),
    )

  @overload(WAIT['Qt3DInput.QMouseEvent'])
  @overload(NoneType)
  def pressAndHold(self, mouse: Optional[Qt3DInput.QMouseEvent]) -> None:
    """
    Calls Qt's 'void
    Qt3DInput::QMouseHandler::pressAndHold(Qt3DInput::QMouseEvent *mouse)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qmousehandler.html#pressAndHold

    Parameters
    ----------

    mouse : Optional[Qt3DInput.QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DInput::QMouseHandler::pressAndHold(Qt3DInput::QMouseEvent
    #      *mouse)
    self.uglySide.call(
        'ritual_ZN9Qt3DInput13QMouseHandler12pressAndHoldEPNS_11QMouseEvent'
        'E',
        self._addressOf(mouse),
    )

  @overload(WAIT['Qt3DInput.QMouseEvent'])
  @overload(NoneType)
  def positionChanged(self, mouse: Optional[Qt3DInput.QMouseEvent]) -> None:
    """
    Calls Qt's 'void
    Qt3DInput::QMouseHandler::positionChanged(Qt3DInput::QMouseEvent
    *mouse)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qmousehandler.html#positionChanged

    Parameters
    ----------

    mouse : Optional[Qt3DInput.QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DInput::QMouseHandler::positionChanged(Qt3DInput::QMouseEvent
    #      *mouse)
    self.uglySide.call(
        'ritual_ZN9Qt3DInput13QMouseHandler15positionChangedEPNS_11QMouseEv'
        'entE',
        self._addressOf(mouse),
    )

  @overload(WAIT['Qt3DInput.QWheelEvent'])
  @overload(NoneType)
  def wheel(self, wheel: Optional[Qt3DInput.QWheelEvent]) -> None:
    """
    Calls Qt's 'void Qt3DInput::QMouseHandler::wheel(Qt3DInput::QWheelEvent
    *wheel)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dinput-qmousehandler.html#wheel

    Parameters
    ----------

    wheel : Optional[Qt3DInput.QWheelEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DInput::QMouseHandler::wheel(Qt3DInput::QWheelEvent *wheel)
    self.uglySide.call(
        'ritual_ZN9Qt3DInput13QMouseHandler5wheelEPNS_11QWheelEventE',
        self._addressOf(wheel),
    )

  def d_func(self) -> Optional[Qt3DInput.QMouseHandlerPrivate]:
    """
    Calls Qt's 'QMouseHandlerPrivate *Qt3DInput::QMouseHandler::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qmousehandler.html#d_func

    Returns
    -------

    Optional[Qt3DInput.QMouseHandlerPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QMouseHandlerPrivate *Qt3DInput::QMouseHandler::d_func()
    address = self.uglySide.call(
        'ritual_ZN9Qt3DInput13QMouseHandler6d_funcEv',
    )
    return Qt3DInput.QMouseHandlerPrivate._cuteAt(address)
