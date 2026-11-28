"""
Qt3DInput::QGamepadInput binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DInput/6.12.0/Qt3DInput/private/qgamepadinput_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means Qt3DInput::QGamepadInput to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore
from . import Qt3DInput

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QGamepadInput(Qt3DInput.QAbstractPhysicalDevice):
  """
  The cute side of Qt's Qt3DInput::QGamepadInput: a plain Python object
  standing in front of one C++ Qt3DInput::QGamepadInput.

  It is built on the cute 'Qt3DInput::QAbstractPhysicalDevice', as Qt's
  Qt3DInput::QGamepadInput is built on Qt's
  Qt3DInput::QAbstractPhysicalDevice, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DInput::QGamepadInput that has a ritual and that
  Python can call so far, 5 names in all: 'metaObject', 'tr', 'deviceId',
  'setDeviceId', 'deviceIdChanged'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DInput::QGamepadInput::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int Qt3DInput::QGamepadInput::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QGamepadInputPrivate *Qt3DInput::QGamepadInput::d_func()': gives
    'QGamepadInputPrivate', which has no cute class yet.
  - Qt's 'const QGamepadInputPrivate *Qt3DInput::QGamepadInput::d_func()
    const': gives 'QGamepadInputPrivate', which has no cute class yet.

  What has no ritual
  ------------------

  2 of the 12 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DInput::QGamepadInput is created at the first use, not by
    'Qt3DInput::QGamepadInput(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DInput::QGamepadInput.
  - Qt tells when it has removed the C++ Qt3DInput::QGamepadInput. Every call
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
    Calls Qt's 'QString Qt3DInput::QGamepadInput::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dinput-qgamepadinput.html#tr

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
    #  QString Qt3DInput::QGamepadInput::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN9Qt3DInput13QGamepadInput2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DInput::QGamepadInput'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *Qt3DInput::QGamepadInput::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qgamepadinput.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DInput::QGamepadInput::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK9Qt3DInput13QGamepadInput10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def deviceId(self) -> int:
    """
    Calls Qt's 'int Qt3DInput::QGamepadInput::deviceId() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qgamepadinput.html#deviceId
    """
    #  int Qt3DInput::QGamepadInput::deviceId() const
    return self.uglySide.call(
        'ritual_ZNK9Qt3DInput13QGamepadInput8deviceIdEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setDeviceId(self, deviceId: int) -> None:
    """
    Calls Qt's 'void Qt3DInput::QGamepadInput::setDeviceId(int deviceId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qgamepadinput.html#setDeviceId

    Parameters
    ----------

    deviceId : int
      Passed on as it is.
    """
    #  void Qt3DInput::QGamepadInput::setDeviceId(int deviceId)
    self.uglySide.call(
        'ritual_ZN9Qt3DInput13QGamepadInput11setDeviceIdEi', deviceId,
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
    'Qt3DInput::QGamepadInput::QGamepadInput(Qt3DCore::QNode *parent)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qgamepadinput.html#QGamepadInput

    Parameters
    ----------

    parent : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DInput::QGamepadInput::QGamepadInput(Qt3DCore::QNode *parent)
    self._noteCreation(QGamepadInput, lambda: Rituals.call(
        'ritual_ZN9Qt3DInput13QGamepadInputC1EPN8Qt3DCore5QNodeE',
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

  def deviceIdChanged(self) -> None:
    """
    Calls Qt's 'void Qt3DInput::QGamepadInput::deviceIdChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qgamepadinput.html#deviceIdChanged
    """
    #  void Qt3DInput::QGamepadInput::deviceIdChanged()
    self.uglySide.call(
        'ritual_ZN9Qt3DInput13QGamepadInput15deviceIdChangedEv',
    )
