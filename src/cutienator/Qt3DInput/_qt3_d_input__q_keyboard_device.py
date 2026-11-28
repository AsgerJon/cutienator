"""
Qt3DInput::QKeyboardDevice binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DInput/qkeyboarddevice.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QStringList
from ..Qt3DCore import Qt3DCore
from . import Qt3DInput

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QKeyboardDevice(Qt3DInput.QAbstractPhysicalDevice):
  """
  The cute side of Qt's Qt3DInput::QKeyboardDevice: a plain Python object
  standing in front of one C++ Qt3DInput::QKeyboardDevice.

  It is built on the cute 'Qt3DInput::QAbstractPhysicalDevice', as Qt's
  Qt3DInput::QKeyboardDevice is built on Qt's
  Qt3DInput::QAbstractPhysicalDevice, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DInput::QKeyboardDevice that has a ritual and
  that Python can call so far, 12 names in all: 'metaObject', 'tr',
  'activeInput', 'axisCount', 'buttonCount', 'axisNames', 'buttonNames',
  'axisIdentifier', 'buttonIdentifier', 'activeInputChanged', 'd_func',
  'setActiveInput'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DInput::QKeyboardDevice::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int Qt3DInput::QKeyboardDevice::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DInput::QKeyboardDevice::~QKeyboardDevice()': the destructor:
    Python never removes a C++ Qt3DInput::QKeyboardDevice.
  - Qt's 'Qt3DInput::QKeyboardDevice::QKeyboardDevice(QKeyboardDevicePrivate
    &dd, QNode *parent)': takes a type Python has no way to hand over yet.
  - Qt's 'const QKeyboardDevicePrivate *Qt3DInput::QKeyboardDevice::d_func()
    const': takes in Python what 'QKeyboardDevicePrivate
    *Qt3DInput::QKeyboardDevice::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 20 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DInput::QKeyboardDevice is created at the first use, not by
    'Qt3DInput::QKeyboardDevice(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DInput::QKeyboardDevice.
  - Qt tells when it has removed the C++ Qt3DInput::QKeyboardDevice. Every
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
    Calls Qt's 'QString Qt3DInput::QKeyboardDevice::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dinput-qkeyboarddevice.html#tr

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
    #  QString Qt3DInput::QKeyboardDevice::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN9Qt3DInput15QKeyboardDevice2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DInput::QKeyboardDevice'

  #  A C++ Qt3DInput::QKeyboardDevice Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DInput_QKeyboardDevice'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *Qt3DInput::QKeyboardDevice::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qkeyboarddevice.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DInput::QKeyboardDevice::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK9Qt3DInput15QKeyboardDevice10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def activeInput(self) -> Optional[Qt3DInput.QKeyboardHandler]:
    """
    Calls Qt's 'QKeyboardHandler *Qt3DInput::QKeyboardDevice::activeInput()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qkeyboarddevice.html#activeInput

    Returns
    -------

    Optional[Qt3DInput.QKeyboardHandler]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QKeyboardHandler *Qt3DInput::QKeyboardDevice::activeInput() const
    address = self.uglySide.call(
        'ritual_ZNK9Qt3DInput15QKeyboardDevice11activeInputEv',
    )
    return Qt3DInput.QKeyboardHandler._cuteAt(address)

  def axisCount(self) -> int:
    """
    Calls Qt's 'int Qt3DInput::QKeyboardDevice::axisCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qkeyboarddevice.html#axisCount
    """
    #  int Qt3DInput::QKeyboardDevice::axisCount() const
    return self.uglySide.call(
        'ritual_ZNK9Qt3DInput15QKeyboardDevice9axisCountEv',
    )

  def buttonCount(self) -> int:
    """
    Calls Qt's 'int Qt3DInput::QKeyboardDevice::buttonCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qkeyboarddevice.html#buttonCount
    """
    #  int Qt3DInput::QKeyboardDevice::buttonCount() const
    return self.uglySide.call(
        'ritual_ZNK9Qt3DInput15QKeyboardDevice11buttonCountEv',
    )

  def axisNames(self) -> QStringList:
    """
    Calls Qt's 'QStringList Qt3DInput::QKeyboardDevice::axisNames() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qkeyboarddevice.html#axisNames

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList Qt3DInput::QKeyboardDevice::axisNames() const
    address = self.uglySide.call(
        'ritual_ZNK9Qt3DInput15QKeyboardDevice9axisNamesEv',
    )
    return QStringList._cuteOwning(address)

  def buttonNames(self) -> QStringList:
    """
    Calls Qt's 'QStringList Qt3DInput::QKeyboardDevice::buttonNames() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qkeyboarddevice.html#buttonNames

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList Qt3DInput::QKeyboardDevice::buttonNames() const
    address = self.uglySide.call(
        'ritual_ZNK9Qt3DInput15QKeyboardDevice11buttonNamesEv',
    )
    return QStringList._cuteOwning(address)

  @overload(str)
  def axisIdentifier(self, name: str) -> int:
    """
    Calls Qt's 'int Qt3DInput::QKeyboardDevice::axisIdentifier(const QString
    &name) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qkeyboarddevice.html#axisIdentifier

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  int Qt3DInput::QKeyboardDevice::axisIdentifier(const QString &name)
    #      const
    return self.uglySide.call(
        'ritual_ZNK9Qt3DInput15QKeyboardDevice14axisIdentifierERK7QString',
        name,
    )

  @overload(str)
  def buttonIdentifier(self, name: str) -> int:
    """
    Calls Qt's 'int Qt3DInput::QKeyboardDevice::buttonIdentifier(const
    QString &name) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qkeyboarddevice.html#buttonIdentifier

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  int Qt3DInput::QKeyboardDevice::buttonIdentifier(const QString &name)
    #      const
    return self.uglySide.call(
        'ritual_ZNK9Qt3DInput15QKeyboardDevice16buttonIdentifierERK7QString',
        name,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(WAIT['Qt3DInput.QKeyboardHandler'])
  @overload(NoneType)
  def setActiveInput(
      self,
      activeInput: Optional[Qt3DInput.QKeyboardHandler],
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DInput::QKeyboardDevice::setActiveInput(QKeyboardHandler
    *activeInput)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qkeyboarddevice.html#setActiveInput

    Parameters
    ----------

    activeInput : Optional[Qt3DInput.QKeyboardHandler]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DInput::QKeyboardDevice::setActiveInput(QKeyboardHandler
    #      *activeInput)
    self.uglySide.call(
        'ritual_ZN9Qt3DInput15QKeyboardDevice14setActiveInputEPNS_16QKeyboa'
        'rdHandlerE',
        self._addressOf(activeInput),
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
    'Qt3DInput::QKeyboardDevice::QKeyboardDevice(QNode *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qkeyboarddevice.html#QKeyboardDevice

    Parameters
    ----------

    parent : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DInput::QKeyboardDevice::QKeyboardDevice(QNode *parent)
    self._noteCreation(QKeyboardDevice, lambda: Rituals.call(
        'ritual_ZN9Qt3DInput15QKeyboardDeviceC1EPN8Qt3DCore5QNodeE',
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

  @overload(WAIT['Qt3DInput.QKeyboardHandler'])
  @overload(NoneType)
  def activeInputChanged(
      self,
      activeInput: Optional[Qt3DInput.QKeyboardHandler],
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DInput::QKeyboardDevice::activeInputChanged(QKeyboardHandler
    *activeInput)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qkeyboarddevice.html#activeInputChanged

    Parameters
    ----------

    activeInput : Optional[Qt3DInput.QKeyboardHandler]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DInput::QKeyboardDevice::activeInputChanged(QKeyboardHandler
    #      *activeInput)
    self.uglySide.call(
        'ritual_ZN9Qt3DInput15QKeyboardDevice18activeInputChangedEPNS_16QKe'
        'yboardHandlerE',
        self._addressOf(activeInput),
    )

  def d_func(self) -> Optional[Qt3DInput.QKeyboardDevicePrivate]:
    """
    Calls Qt's 'QKeyboardDevicePrivate
    *Qt3DInput::QKeyboardDevice::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qkeyboarddevice.html#d_func

    Returns
    -------

    Optional[Qt3DInput.QKeyboardDevicePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QKeyboardDevicePrivate *Qt3DInput::QKeyboardDevice::d_func()
    address = self.uglySide.call(
        'ritual_ZN9Qt3DInput15QKeyboardDevice6d_funcEv',
    )
    return Qt3DInput.QKeyboardDevicePrivate._cuteAt(address)
