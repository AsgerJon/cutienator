"""
Qt3DInput::QAbstractPhysicalDeviceProxy binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DInput/6.12.0/Qt3DInput/private/qabstractphysicaldeviceproxy_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means Qt3DInput::QAbstractPhysicalDeviceProxy to be private: it
#  declares the class in a header it calls private. cutienator does not care.
#  Qt hands objects of the class out all the same, and a class we are handed
#  is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QStringList
from . import Qt3DInput

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAbstractPhysicalDeviceProxy(Qt3DInput.QAbstractPhysicalDevice):
  """
  The cute side of Qt's Qt3DInput::QAbstractPhysicalDeviceProxy: a plain
  Python object standing in front of one C++
  Qt3DInput::QAbstractPhysicalDeviceProxy.

  It is built on the cute 'Qt3DInput::QAbstractPhysicalDevice', as Qt's
  Qt3DInput::QAbstractPhysicalDeviceProxy is built on Qt's
  Qt3DInput::QAbstractPhysicalDevice, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DInput::QAbstractPhysicalDeviceProxy that has a
  ritual and that Python can call so far, 12 names in all: 'metaObject',
  'tr', 'deviceName', 'status', 'axisCount', 'buttonCount', 'axisNames',
  'buttonNames', 'axisIdentifier', 'buttonIdentifier', 'statusChanged',
  'd_func'. None can be made from Python: one comes out of a function of
  another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DInput::QAbstractPhysicalDeviceProxy::qt_metacast(const
    char *a0)': one of Qt's own inner workings.
  - Qt's 'int
    Qt3DInput::QAbstractPhysicalDeviceProxy::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's
    'Qt3DInput::QAbstractPhysicalDeviceProxy::QAbstractPhysicalDeviceProxy(
    QAbstractPhysicalDeviceProxyPrivate &dd, Qt3DCore::QNode *parent)': takes
    a type Python has no way to hand over yet.
  - Qt's 'const QAbstractPhysicalDeviceProxyPrivate
    *Qt3DInput::QAbstractPhysicalDeviceProxy::d_func() const': takes in
    Python what 'QAbstractPhysicalDeviceProxyPrivate
    *Qt3DInput::QAbstractPhysicalDeviceProxy::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 18 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DInput::QAbstractPhysicalDeviceProxy is created at the first
    use, not by 'Qt3DInput::QAbstractPhysicalDeviceProxy(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DInput::QAbstractPhysicalDeviceProxy.
  - Qt tells when it has removed the C++
    Qt3DInput::QAbstractPhysicalDeviceProxy. Every call on the cute object,
    and every use of it as an argument, then raises 'RuntimeError', and
    nothing reaches C++.
  - Each name of Qt's Qt3DInput::QAbstractPhysicalDeviceProxy that has no
    cute function yet, '__init__', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside Qt3DInput::QAbstractPhysicalDeviceProxy, each
  #  a class in here as in C++, and the names Qt has for the combinations of
  #  its flags enums.

  class DeviceStatus(CuteNum):
    """
    The enum 'Qt3DInput::QAbstractPhysicalDeviceProxy::DeviceStatus' of Qt,
    with the 2 names Qt gives in it.
    """

    Ready = Kee[int](0)
    NotFound = Kee[int](1)

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
    Calls Qt's 'QString Qt3DInput::QAbstractPhysicalDeviceProxy::tr(const
    char *s, const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qabstractphysicaldeviceproxy.html#tr

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
    #  QString Qt3DInput::QAbstractPhysicalDeviceProxy::tr(const char *s,
    #      const char *c, int n)
    return Rituals.call(
        'ritual_ZN9Qt3DInput28QAbstractPhysicalDeviceProxy2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DInput::QAbstractPhysicalDeviceProxy'

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
    *Qt3DInput::QAbstractPhysicalDeviceProxy::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qabstractphysicaldeviceproxy.html

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject
    #      *Qt3DInput::QAbstractPhysicalDeviceProxy::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK9Qt3DInput28QAbstractPhysicalDeviceProxy10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def deviceName(self) -> str:
    """
    Calls Qt's 'QString Qt3DInput::QAbstractPhysicalDeviceProxy::deviceName()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qabstractphysicaldeviceproxy.html

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString Qt3DInput::QAbstractPhysicalDeviceProxy::deviceName() const
    return self.uglySide.call(
        'ritual_ZNK9Qt3DInput28QAbstractPhysicalDeviceProxy10deviceNameEv',
    )

  def status(self) -> DeviceStatus:
    """
    Calls Qt's 'DeviceStatus
    Qt3DInput::QAbstractPhysicalDeviceProxy::status() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qabstractphysicaldeviceproxy.html#status

    Returns
    -------

    DeviceStatus
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'DeviceStatus(number)'
      gives.
    """
    #  DeviceStatus Qt3DInput::QAbstractPhysicalDeviceProxy::status() const
    return QAbstractPhysicalDeviceProxy.DeviceStatus(self.uglySide.call(
        'ritual_ZNK9Qt3DInput28QAbstractPhysicalDeviceProxy6statusEv',
    ))

  def axisCount(self) -> int:
    """
    Calls Qt's 'int Qt3DInput::QAbstractPhysicalDeviceProxy::axisCount()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qabstractphysicaldeviceproxy.html
    """
    #  int Qt3DInput::QAbstractPhysicalDeviceProxy::axisCount() const
    ritual = 'ritual_ZNK9Qt3DInput28QAbstractPhysicalDeviceProxy9axisCountEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK9Qt3DInput28QAbstractPhysicalDeviceProxy9axisCount'
          'Ev')
    return self.uglySide.call(ritual)

  def buttonCount(self) -> int:
    """
    Calls Qt's 'int Qt3DInput::QAbstractPhysicalDeviceProxy::buttonCount()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qabstractphysicaldeviceproxy.html
    """
    #  int Qt3DInput::QAbstractPhysicalDeviceProxy::buttonCount() const
    ritual = (
        'ritual_ZNK9Qt3DInput28QAbstractPhysicalDeviceProxy11buttonCountEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK9Qt3DInput28QAbstractPhysicalDeviceProxy11buttonCo'
          'untEv')
    return self.uglySide.call(ritual)

  def axisNames(self) -> QStringList:
    """
    Calls Qt's 'QStringList
    Qt3DInput::QAbstractPhysicalDeviceProxy::axisNames() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qabstractphysicaldeviceproxy.html

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList Qt3DInput::QAbstractPhysicalDeviceProxy::axisNames() const
    address = self.uglySide.call(
        'ritual_ZNK9Qt3DInput28QAbstractPhysicalDeviceProxy9axisNamesEv',
    )
    return QStringList._cuteOwning(address)

  def buttonNames(self) -> QStringList:
    """
    Calls Qt's 'QStringList
    Qt3DInput::QAbstractPhysicalDeviceProxy::buttonNames() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qabstractphysicaldeviceproxy.html

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList Qt3DInput::QAbstractPhysicalDeviceProxy::buttonNames()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK9Qt3DInput28QAbstractPhysicalDeviceProxy11buttonNamesEv',
    )
    return QStringList._cuteOwning(address)

  @overload(str)
  def axisIdentifier(self, name: str) -> int:
    """
    Calls Qt's 'int
    Qt3DInput::QAbstractPhysicalDeviceProxy::axisIdentifier(const QString
    &name) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qabstractphysicaldeviceproxy.html

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  int Qt3DInput::QAbstractPhysicalDeviceProxy::axisIdentifier(const
    #      QString &name) const
    ritual = (
        'ritual_ZNK9Qt3DInput28QAbstractPhysicalDeviceProxy14axisIdentifier'
        'ERK7QString')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK9Qt3DInput28QAbstractPhysicalDeviceProxy14axisIden'
          'tifierERK7QString')
    return self.uglySide.call(ritual, name)

  @overload(str)
  def buttonIdentifier(self, name: str) -> int:
    """
    Calls Qt's 'int
    Qt3DInput::QAbstractPhysicalDeviceProxy::buttonIdentifier(const QString
    &name) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qabstractphysicaldeviceproxy.html

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  int Qt3DInput::QAbstractPhysicalDeviceProxy::buttonIdentifier(const
    #      QString &name) const
    ritual = (
        'ritual_ZNK9Qt3DInput28QAbstractPhysicalDeviceProxy16buttonIdentifi'
        'erERK7QString')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK9Qt3DInput28QAbstractPhysicalDeviceProxy16buttonId'
          'entifierERK7QString')
    return self.uglySide.call(ritual, name)

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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's
    'Qt3DInput::QAbstractPhysicalDeviceProxy::QAbstractPhysicalDeviceProxy(
    QAbstractPhysicalDeviceProxyPrivate &dd, Qt3DCore::QNode *parent)': takes
    a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'Qt3DInput.QAbstractPhysicalDeviceProxy.__init__' has no cute "
        "function yet. Qt's "
        "'Qt3DInput::QAbstractPhysicalDeviceProxy::QAbstractPhysicalDevicePr"
        "oxy(QAbstractPhysicalDeviceProxyPrivate &dd, Qt3DCore::QNode "
        "*parent)': takes a type Python has no way to hand over yet.")

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

  @overload(DeviceStatus)
  def statusChanged(self, status: DeviceStatus) -> None:
    """
    Calls Qt's 'void Qt3DInput::QAbstractPhysicalDeviceProxy::statusChanged(
    QAbstractPhysicalDeviceProxy::DeviceStatus status)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qabstractphysicaldeviceproxy.html

    Parameters
    ----------

    status : DeviceStatus
      Passed on as its number.
    """
    #  void Qt3DInput::QAbstractPhysicalDeviceProxy::statusChanged(
    #      QAbstractPhysicalDeviceProxy::DeviceStatus status)
    self.uglySide.call(
        'ritual_ZN9Qt3DInput28QAbstractPhysicalDeviceProxy13statusChangedEN'
        'S0_12DeviceStatusE',
        status.value,
    )

  def d_func(
      self,
  ) -> Optional[Qt3DInput.QAbstractPhysicalDeviceProxyPrivate]:
    """
    Calls Qt's 'QAbstractPhysicalDeviceProxyPrivate
    *Qt3DInput::QAbstractPhysicalDeviceProxy::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qabstractphysicaldeviceproxy.html#d_func

    Returns
    -------

    Optional[Qt3DInput.QAbstractPhysicalDeviceProxyPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractPhysicalDeviceProxyPrivate
    #      *Qt3DInput::QAbstractPhysicalDeviceProxy::d_func()
    address = self.uglySide.call(
        'ritual_ZN9Qt3DInput28QAbstractPhysicalDeviceProxy6d_funcEv',
    )
    return Qt3DInput.QAbstractPhysicalDeviceProxyPrivate._cuteAt(address)
