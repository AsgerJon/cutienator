"""
Qt3DInput::QMouseDevice binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DInput/qmousedevice.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
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


class QMouseDevice(Qt3DInput.QAbstractPhysicalDevice):
  """
  The cute side of Qt's Qt3DInput::QMouseDevice: a plain Python object
  standing in front of one C++ Qt3DInput::QMouseDevice.

  It is built on the cute 'Qt3DInput::QAbstractPhysicalDevice', as Qt's
  Qt3DInput::QMouseDevice is built on Qt's
  Qt3DInput::QAbstractPhysicalDevice, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DInput::QMouseDevice that has a ritual and that
  Python can call so far, 15 names in all: 'metaObject', 'tr', 'axisCount',
  'buttonCount', 'axisNames', 'buttonNames', 'axisIdentifier',
  'buttonIdentifier', 'sensitivity', 'updateAxesContinuously',
  'setSensitivity', 'setUpdateAxesContinuously', 'sensitivityChanged',
  'updateAxesContinuouslyChanged', 'd_func'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DInput::QMouseDevice::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int Qt3DInput::QMouseDevice::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DInput::QMouseDevice::~QMouseDevice()': the destructor: Python
    never removes a C++ Qt3DInput::QMouseDevice.
  - Qt's 'const QMouseDevicePrivate *Qt3DInput::QMouseDevice::d_func()
    const': takes in Python what 'QMouseDevicePrivate
    *Qt3DInput::QMouseDevice::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 22 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DInput::QMouseDevice is created at the first use, not by
    'Qt3DInput::QMouseDevice(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DInput::QMouseDevice.
  - Qt tells when it has removed the C++ Qt3DInput::QMouseDevice. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside Qt3DInput::QMouseDevice, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class Axis(CuteNum):
    """
    The enum 'Qt3DInput::QMouseDevice::Axis' of Qt, with the 4 names Qt gives
    in it.
    """

    X = Kee[int](0)
    Y = Kee[int](1)
    WheelX = Kee[int](2)
    WheelY = Kee[int](3)

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
    Calls Qt's 'QString Qt3DInput::QMouseDevice::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dinput-qmousedevice.html#tr

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
    #  QString Qt3DInput::QMouseDevice::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN9Qt3DInput12QMouseDevice2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DInput::QMouseDevice'

  #  A C++ Qt3DInput::QMouseDevice Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DInput_QMouseDevice'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *Qt3DInput::QMouseDevice::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qmousedevice.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DInput::QMouseDevice::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK9Qt3DInput12QMouseDevice10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def axisCount(self) -> int:
    """
    Calls Qt's 'int Qt3DInput::QMouseDevice::axisCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qmousedevice.html#axisCount
    """
    #  int Qt3DInput::QMouseDevice::axisCount() const
    return self.uglySide.call(
        'ritual_ZNK9Qt3DInput12QMouseDevice9axisCountEv',
    )

  def buttonCount(self) -> int:
    """
    Calls Qt's 'int Qt3DInput::QMouseDevice::buttonCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qmousedevice.html#buttonCount
    """
    #  int Qt3DInput::QMouseDevice::buttonCount() const
    return self.uglySide.call(
        'ritual_ZNK9Qt3DInput12QMouseDevice11buttonCountEv',
    )

  def axisNames(self) -> QStringList:
    """
    Calls Qt's 'QStringList Qt3DInput::QMouseDevice::axisNames() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qmousedevice.html#axisNames

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList Qt3DInput::QMouseDevice::axisNames() const
    address = self.uglySide.call(
        'ritual_ZNK9Qt3DInput12QMouseDevice9axisNamesEv',
    )
    return QStringList._cuteOwning(address)

  def buttonNames(self) -> QStringList:
    """
    Calls Qt's 'QStringList Qt3DInput::QMouseDevice::buttonNames() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qmousedevice.html#buttonNames

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList Qt3DInput::QMouseDevice::buttonNames() const
    address = self.uglySide.call(
        'ritual_ZNK9Qt3DInput12QMouseDevice11buttonNamesEv',
    )
    return QStringList._cuteOwning(address)

  @overload(str)
  def axisIdentifier(self, name: str) -> int:
    """
    Calls Qt's 'int Qt3DInput::QMouseDevice::axisIdentifier(const QString
    &name) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qmousedevice.html#axisIdentifier

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  int Qt3DInput::QMouseDevice::axisIdentifier(const QString &name) const
    return self.uglySide.call(
        'ritual_ZNK9Qt3DInput12QMouseDevice14axisIdentifierERK7QString',
        name,
    )

  @overload(str)
  def buttonIdentifier(self, name: str) -> int:
    """
    Calls Qt's 'int Qt3DInput::QMouseDevice::buttonIdentifier(const QString
    &name) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qmousedevice.html#buttonIdentifier

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  int Qt3DInput::QMouseDevice::buttonIdentifier(const QString &name)
    #      const
    return self.uglySide.call(
        'ritual_ZNK9Qt3DInput12QMouseDevice16buttonIdentifierERK7QString',
        name,
    )

  def sensitivity(self) -> float:
    """
    Calls Qt's 'float Qt3DInput::QMouseDevice::sensitivity() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qmousedevice.html#sensitivity
    """
    #  float Qt3DInput::QMouseDevice::sensitivity() const
    return self.uglySide.call(
        'ritual_ZNK9Qt3DInput12QMouseDevice11sensitivityEv',
    )

  def updateAxesContinuously(self) -> bool:
    """
    Calls Qt's 'bool Qt3DInput::QMouseDevice::updateAxesContinuously()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qmousedevice.html#updateAxesContinuously
    """
    #  bool Qt3DInput::QMouseDevice::updateAxesContinuously() const
    return self.uglySide.call(
        'ritual_ZNK9Qt3DInput12QMouseDevice22updateAxesContinuouslyEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setSensitivity(self, value: float) -> None:
    """
    Calls Qt's 'void Qt3DInput::QMouseDevice::setSensitivity(float value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qmousedevice.html#setSensitivity

    Parameters
    ----------

    value : float
      Passed on as it is.
    """
    #  void Qt3DInput::QMouseDevice::setSensitivity(float value)
    self.uglySide.call(
        'ritual_ZN9Qt3DInput12QMouseDevice14setSensitivityEf', value,
    )

  @overload(bool)
  def setUpdateAxesContinuously(self, updateAxesContinuously: bool) -> None:
    """
    Calls Qt's 'void Qt3DInput::QMouseDevice::setUpdateAxesContinuously(bool
    updateAxesContinuously)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qmousedevice.html

    Parameters
    ----------

    updateAxesContinuously : bool
      Passed on as it is.
    """
    #  void Qt3DInput::QMouseDevice::setUpdateAxesContinuously(bool
    #      updateAxesContinuously)
    self.uglySide.call(
        'ritual_ZN9Qt3DInput12QMouseDevice25setUpdateAxesContinuouslyEb',
        updateAxesContinuously,
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
    'Qt3DInput::QMouseDevice::QMouseDevice(Qt3DCore::QNode *parent)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qmousedevice.html#QMouseDevice

    Parameters
    ----------

    parent : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DInput::QMouseDevice::QMouseDevice(Qt3DCore::QNode *parent)
    self._noteCreation(QMouseDevice, lambda: Rituals.call(
        'ritual_ZN9Qt3DInput12QMouseDeviceC1EPN8Qt3DCore5QNodeE',
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

  @overload(float)
  def sensitivityChanged(self, value: float) -> None:
    """
    Calls Qt's 'void Qt3DInput::QMouseDevice::sensitivityChanged(float
    value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qmousedevice.html#sensitivityChanged

    Parameters
    ----------

    value : float
      Passed on as it is.
    """
    #  void Qt3DInput::QMouseDevice::sensitivityChanged(float value)
    self.uglySide.call(
        'ritual_ZN9Qt3DInput12QMouseDevice18sensitivityChangedEf', value,
    )

  @overload(bool)
  def updateAxesContinuouslyChanged(
      self,
      updateAxesContinuously: bool,
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DInput::QMouseDevice::updateAxesContinuouslyChanged(bool
    updateAxesContinuously)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qmousedevice.html

    Parameters
    ----------

    updateAxesContinuously : bool
      Passed on as it is.
    """
    #  void Qt3DInput::QMouseDevice::updateAxesContinuouslyChanged(bool
    #      updateAxesContinuously)
    self.uglySide.call(
        'ritual_ZN9Qt3DInput12QMouseDevice29updateAxesContinuouslyChangedEb',
        updateAxesContinuously,
    )

  def d_func(self) -> Optional[Qt3DInput.QMouseDevicePrivate]:
    """
    Calls Qt's 'QMouseDevicePrivate *Qt3DInput::QMouseDevice::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dinput-qmousedevice.html#d_func

    Returns
    -------

    Optional[Qt3DInput.QMouseDevicePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QMouseDevicePrivate *Qt3DInput::QMouseDevice::d_func()
    address = self.uglySide.call(
        'ritual_ZN9Qt3DInput12QMouseDevice6d_funcEv',
    )
    return Qt3DInput.QMouseDevicePrivate._cuteAt(address)
