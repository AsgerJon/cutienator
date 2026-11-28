"""
Qt3DInput::QLogicalDevice binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DInput/qlogicaldevice.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore
from . import Qt3DInput

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QLogicalDevice(Qt3DCore.QComponent):
  """
  The cute side of Qt's Qt3DInput::QLogicalDevice: a plain Python object
  standing in front of one C++ Qt3DInput::QLogicalDevice.

  It is built on the cute 'Qt3DCore::QComponent', as Qt's
  Qt3DInput::QLogicalDevice is built on Qt's Qt3DCore::QComponent, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DInput::QLogicalDevice that has a ritual and that
  Python can call so far, 7 names in all: 'metaObject', 'tr', 'addAction',
  'removeAction', 'addAxis', 'removeAxis', 'd_func'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DInput::QLogicalDevice::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int Qt3DInput::QLogicalDevice::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DInput::QLogicalDevice::~QLogicalDevice()': the destructor:
    Python never removes a C++ Qt3DInput::QLogicalDevice.
  - Qt's 'QList<QAction *> Qt3DInput::QLogicalDevice::actions() const': gives
    a type Python has no way to take yet.
  - Qt's 'QList<QAxis *> Qt3DInput::QLogicalDevice::axes() const': gives a
    type Python has no way to take yet.
  - Qt's 'const QLogicalDevicePrivate *Qt3DInput::QLogicalDevice::d_func()
    const': takes in Python what 'QLogicalDevicePrivate
    *Qt3DInput::QLogicalDevice::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 16 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DInput::QLogicalDevice is created at the first use, not by
    'Qt3DInput::QLogicalDevice(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DInput::QLogicalDevice.
  - Qt tells when it has removed the C++ Qt3DInput::QLogicalDevice. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's Qt3DInput::QLogicalDevice that has no cute function
    yet, 'actions', 'axes', holds a function that raises
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
    Calls Qt's 'QString Qt3DInput::QLogicalDevice::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dinput-qlogicaldevice.html#tr

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
    #  QString Qt3DInput::QLogicalDevice::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN9Qt3DInput14QLogicalDevice2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DInput::QLogicalDevice'

  #  A C++ Qt3DInput::QLogicalDevice Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DInput_QLogicalDevice'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *Qt3DInput::QLogicalDevice::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qlogicaldevice.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DInput::QLogicalDevice::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK9Qt3DInput14QLogicalDevice10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
    'Qt3DInput::QLogicalDevice::QLogicalDevice(Qt3DCore::QNode *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qlogicaldevice.html#QLogicalDevice

    Parameters
    ----------

    parent : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DInput::QLogicalDevice::QLogicalDevice(Qt3DCore::QNode *parent)
    self._noteCreation(QLogicalDevice, lambda: Rituals.call(
        'ritual_ZN9Qt3DInput14QLogicalDeviceC1EPN8Qt3DCore5QNodeE',
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

  @overload(WAIT['Qt3DInput.QAction'])
  @overload(NoneType)
  def addAction(self, action: Optional[Qt3DInput.QAction]) -> None:
    """
    Calls Qt's 'void Qt3DInput::QLogicalDevice::addAction(QAction *action)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qlogicaldevice.html#addAction

    Parameters
    ----------

    action : Optional[Qt3DInput.QAction]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DInput::QLogicalDevice::addAction(QAction *action)
    self.uglySide.call(
        'ritual_ZN9Qt3DInput14QLogicalDevice9addActionEPNS_7QActionE',
        self._addressOf(action),
    )

  @overload(WAIT['Qt3DInput.QAction'])
  @overload(NoneType)
  def removeAction(self, action: Optional[Qt3DInput.QAction]) -> None:
    """
    Calls Qt's 'void Qt3DInput::QLogicalDevice::removeAction(QAction
    *action)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qlogicaldevice.html#removeAction

    Parameters
    ----------

    action : Optional[Qt3DInput.QAction]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DInput::QLogicalDevice::removeAction(QAction *action)
    self.uglySide.call(
        'ritual_ZN9Qt3DInput14QLogicalDevice12removeActionEPNS_7QActionE',
        self._addressOf(action),
    )

  @overload(WAIT['Qt3DInput.QAxis'])
  @overload(NoneType)
  def addAxis(self, axis: Optional[Qt3DInput.QAxis]) -> None:
    """
    Calls Qt's 'void Qt3DInput::QLogicalDevice::addAxis(QAxis *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qlogicaldevice.html#addAxis

    Parameters
    ----------

    axis : Optional[Qt3DInput.QAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DInput::QLogicalDevice::addAxis(QAxis *axis)
    self.uglySide.call(
        'ritual_ZN9Qt3DInput14QLogicalDevice7addAxisEPNS_5QAxisE',
        self._addressOf(axis),
    )

  @overload(WAIT['Qt3DInput.QAxis'])
  @overload(NoneType)
  def removeAxis(self, axis: Optional[Qt3DInput.QAxis]) -> None:
    """
    Calls Qt's 'void Qt3DInput::QLogicalDevice::removeAxis(QAxis *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qlogicaldevice.html#removeAxis

    Parameters
    ----------

    axis : Optional[Qt3DInput.QAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DInput::QLogicalDevice::removeAxis(QAxis *axis)
    self.uglySide.call(
        'ritual_ZN9Qt3DInput14QLogicalDevice10removeAxisEPNS_5QAxisE',
        self._addressOf(axis),
    )

  def d_func(self) -> Optional[Qt3DInput.QLogicalDevicePrivate]:
    """
    Calls Qt's 'QLogicalDevicePrivate *Qt3DInput::QLogicalDevice::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qlogicaldevice.html#d_func

    Returns
    -------

    Optional[Qt3DInput.QLogicalDevicePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QLogicalDevicePrivate *Qt3DInput::QLogicalDevice::d_func()
    address = self.uglySide.call(
        'ritual_ZN9Qt3DInput14QLogicalDevice6d_funcEv',
    )
    return Qt3DInput.QLogicalDevicePrivate._cuteAt(address)

  @staticmethod
  def actions(*__, **_) -> Never:
    """
    Qt's 'QList<QAction *> Qt3DInput::QLogicalDevice::actions() const': gives
    a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DInput.QLogicalDevice.actions' has no cute function yet. Qt's "
        "'QList<QAction *> Qt3DInput::QLogicalDevice::actions() const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def axes(*__, **_) -> Never:
    """
    Qt's 'QList<QAxis *> Qt3DInput::QLogicalDevice::axes() const': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DInput.QLogicalDevice.axes' has no cute function yet. Qt's "
        "'QList<QAxis *> Qt3DInput::QLogicalDevice::axes() const': gives a "
        "type Python has no way to take yet.")
