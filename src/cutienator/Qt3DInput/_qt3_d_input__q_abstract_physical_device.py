"""
Qt3DInput::QAbstractPhysicalDevice binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DInput/qabstractphysicaldevice.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QStringList
from ..Qt3DCore import Qt3DCore
from . import Qt3DInput

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAbstractPhysicalDevice(Qt3DCore.QNode):
  """
  The cute side of Qt's Qt3DInput::QAbstractPhysicalDevice: a plain Python
  object standing in front of one C++ Qt3DInput::QAbstractPhysicalDevice.

  It is built on the cute 'Qt3DCore::QNode', as Qt's
  Qt3DInput::QAbstractPhysicalDevice is built on Qt's Qt3DCore::QNode, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DInput::QAbstractPhysicalDevice that has a ritual
  and that Python can call so far, 11 names in all: 'metaObject', 'tr',
  'axisCount', 'buttonCount', 'axisNames', 'buttonNames', 'axisIdentifier',
  'buttonIdentifier', 'addAxisSetting', 'removeAxisSetting', 'd_func'. It can
  be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DInput::QAbstractPhysicalDevice::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int
    Qt3DInput::QAbstractPhysicalDevice::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DInput::QAbstractPhysicalDevice::~QAbstractPhysicalDevice()':
    the destructor: Python never removes a C++
    Qt3DInput::QAbstractPhysicalDevice.
  - Qt's 'QList<QAxisSetting *>
    Qt3DInput::QAbstractPhysicalDevice::axisSettings() const': gives a type
    Python has no way to take yet.
  - Qt's 'Qt3DInput::QAbstractPhysicalDevice::QAbstractPhysicalDevice(
    QAbstractPhysicalDevicePrivate &dd, Qt3DCore::QNode *parent)': takes a
    type Python has no way to hand over yet.
  - Qt's 'const QAbstractPhysicalDevicePrivate
    *Qt3DInput::QAbstractPhysicalDevice::d_func() const': takes in Python
    what 'QAbstractPhysicalDevicePrivate
    *Qt3DInput::QAbstractPhysicalDevice::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 20 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DInput::QAbstractPhysicalDevice is created at the first use,
    not by 'Qt3DInput::QAbstractPhysicalDevice(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DInput::QAbstractPhysicalDevice.
  - Qt tells when it has removed the C++ Qt3DInput::QAbstractPhysicalDevice.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
  - Each name of Qt's Qt3DInput::QAbstractPhysicalDevice that has no cute
    function yet, 'axisSettings', holds a function that raises
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
    Calls Qt's 'QString Qt3DInput::QAbstractPhysicalDevice::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qabstractphysicaldevice.html#tr

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
    #  QString Qt3DInput::QAbstractPhysicalDevice::tr(const char *s, const
    #      char *c, int n)
    return Rituals.call(
        'ritual_ZN9Qt3DInput23QAbstractPhysicalDevice2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DInput::QAbstractPhysicalDevice'

  #  A C++ Qt3DInput::QAbstractPhysicalDevice Python makes is of a C++ class
  #  of ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DInput_QAbstractPhysicalDevice'

  #  The functions Qt calls itself that Qt3DInput::QAbstractPhysicalDevice is
  #  the first to declare and that cannot be handed to Python yet, each as Qt
  #  declares it. A class of a program that writes one of them anew is
  #  refused, since Qt would never call what it wrote; see
  #  'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'axisNames': (
          'QStringList Qt3DInput::QAbstractPhysicalDevice::axisNames() '
          'const',
      ),
      'buttonNames': (
          'QStringList Qt3DInput::QAbstractPhysicalDevice::buttonNames() '
          'const',
      ),
  }

  #  The functions Qt calls itself that Qt3DInput::QAbstractPhysicalDevice is
  #  the first to declare. A class of a program built on it can write one
  #  anew, and Qt then calls that. For each name: the key C++ knows the
  #  function by, what it gives, and what it takes.
  __virtual_functions__ = {
      'axisCount': (
          ('_ZNK9Qt3DInput23QAbstractPhysicalDevice9axisCountEv',
           ('int', 'number', ''),
           ()),
      ),
      'buttonCount': (
          ('_ZNK9Qt3DInput23QAbstractPhysicalDevice11buttonCountEv',
           ('int', 'number', ''),
           ()),
      ),
      'axisIdentifier': (
          ('_ZNK9Qt3DInput23QAbstractPhysicalDevice14axisIdentifierERK7QStr'
           'ing',
           ('int', 'number', ''),
           (
               ('address', 'text', ''),
           )),
      ),
      'buttonIdentifier': (
          ('_ZNK9Qt3DInput23QAbstractPhysicalDevice16buttonIdentifierERK7QS'
           'tring',
           ('int', 'number', ''),
           (
               ('address', 'text', ''),
           )),
      ),
  }

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
    *Qt3DInput::QAbstractPhysicalDevice::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qabstractphysicaldevice.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DInput::QAbstractPhysicalDevice::metaObject()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK9Qt3DInput23QAbstractPhysicalDevice10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def axisCount(self) -> int:
    """
    Calls Qt's 'int Qt3DInput::QAbstractPhysicalDevice::axisCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qabstractphysicaldevice.html#axisCount
    """
    #  int Qt3DInput::QAbstractPhysicalDevice::axisCount() const
    ritual = 'ritual_ZNK9Qt3DInput23QAbstractPhysicalDevice9axisCountEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK9Qt3DInput23QAbstractPhysicalDevice9axisCountEv')
    return self.uglySide.call(ritual)

  def buttonCount(self) -> int:
    """
    Calls Qt's 'int Qt3DInput::QAbstractPhysicalDevice::buttonCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qabstractphysicaldevice.html#buttonCount
    """
    #  int Qt3DInput::QAbstractPhysicalDevice::buttonCount() const
    ritual = 'ritual_ZNK9Qt3DInput23QAbstractPhysicalDevice11buttonCountEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK9Qt3DInput23QAbstractPhysicalDevice11buttonCountEv')
    return self.uglySide.call(ritual)

  def axisNames(self) -> QStringList:
    """
    Calls Qt's 'QStringList Qt3DInput::QAbstractPhysicalDevice::axisNames()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qabstractphysicaldevice.html#axisNames

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList Qt3DInput::QAbstractPhysicalDevice::axisNames() const
    address = self.uglySide.call(
        'ritual_ZNK9Qt3DInput23QAbstractPhysicalDevice9axisNamesEv',
    )
    return QStringList._cuteOwning(address)

  def buttonNames(self) -> QStringList:
    """
    Calls Qt's 'QStringList Qt3DInput::QAbstractPhysicalDevice::buttonNames()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qabstractphysicaldevice.html#buttonNames

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList Qt3DInput::QAbstractPhysicalDevice::buttonNames() const
    address = self.uglySide.call(
        'ritual_ZNK9Qt3DInput23QAbstractPhysicalDevice11buttonNamesEv',
    )
    return QStringList._cuteOwning(address)

  @overload(str)
  def axisIdentifier(self, name: str) -> int:
    """
    Calls Qt's 'int Qt3DInput::QAbstractPhysicalDevice::axisIdentifier(const
    QString &name) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qabstractphysicaldevice.html

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  int Qt3DInput::QAbstractPhysicalDevice::axisIdentifier(const QString
    #      &name) const
    ritual = (
        'ritual_ZNK9Qt3DInput23QAbstractPhysicalDevice14axisIdentifierERK7Q'
        'String')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK9Qt3DInput23QAbstractPhysicalDevice14axisIdentifie'
          'rERK7QString')
    return self.uglySide.call(ritual, name)

  @overload(str)
  def buttonIdentifier(self, name: str) -> int:
    """
    Calls Qt's 'int
    Qt3DInput::QAbstractPhysicalDevice::buttonIdentifier(const QString &name)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qabstractphysicaldevice.html

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  int Qt3DInput::QAbstractPhysicalDevice::buttonIdentifier(const QString
    #      &name) const
    ritual = (
        'ritual_ZNK9Qt3DInput23QAbstractPhysicalDevice16buttonIdentifierERK'
        '7QString')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK9Qt3DInput23QAbstractPhysicalDevice16buttonIdentif'
          'ierERK7QString')
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

  @overload()
  @overload(Qt3DCore.QNode)
  @overload(NoneType)
  def __init__(self, parent: Optional[Qt3DCore.QNode] = None) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DInput::QAbstractPhysicalDevice::QAbstractPhysicalDevice(Qt3DCore::
    QNode *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qabstractphysicaldevice.html

    Parameters
    ----------

    parent : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DInput::QAbstractPhysicalDevice::QAbstractPhysicalDevice(
    #      Qt3DCore::QNode *parent)
    self._noteCreation(QAbstractPhysicalDevice, lambda: Rituals.call(
        'ritual_ZN9Qt3DInput23QAbstractPhysicalDeviceC1EPN8Qt3DCore5QNodeE',
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

  @overload(WAIT['Qt3DInput.QAxisSetting'])
  @overload(NoneType)
  def addAxisSetting(
      self,
      axisSetting: Optional[Qt3DInput.QAxisSetting],
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DInput::QAbstractPhysicalDevice::addAxisSetting(QAxisSetting
    *axisSetting)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qabstractphysicaldevice.html

    Parameters
    ----------

    axisSetting : Optional[Qt3DInput.QAxisSetting]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DInput::QAbstractPhysicalDevice::addAxisSetting(QAxisSetting
    #      *axisSetting)
    self.uglySide.call(
        'ritual_ZN9Qt3DInput23QAbstractPhysicalDevice14addAxisSettingEPNS_1'
        '2QAxisSettingE',
        self._addressOf(axisSetting),
    )

  @overload(WAIT['Qt3DInput.QAxisSetting'])
  @overload(NoneType)
  def removeAxisSetting(
      self,
      axisSetting: Optional[Qt3DInput.QAxisSetting],
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DInput::QAbstractPhysicalDevice::removeAxisSetting(QAxisSetting
    *axisSetting)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qabstractphysicaldevice.html

    Parameters
    ----------

    axisSetting : Optional[Qt3DInput.QAxisSetting]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void
    #      Qt3DInput::QAbstractPhysicalDevice::removeAxisSetting(QAxisSetting
    #      *axisSetting)
    self.uglySide.call(
        'ritual_ZN9Qt3DInput23QAbstractPhysicalDevice17removeAxisSettingEPN'
        'S_12QAxisSettingE',
        self._addressOf(axisSetting),
    )

  def d_func(self) -> Optional[Qt3DInput.QAbstractPhysicalDevicePrivate]:
    """
    Calls Qt's 'QAbstractPhysicalDevicePrivate
    *Qt3DInput::QAbstractPhysicalDevice::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qabstractphysicaldevice.html#d_func

    Returns
    -------

    Optional[Qt3DInput.QAbstractPhysicalDevicePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractPhysicalDevicePrivate
    #      *Qt3DInput::QAbstractPhysicalDevice::d_func()
    address = self.uglySide.call(
        'ritual_ZN9Qt3DInput23QAbstractPhysicalDevice6d_funcEv',
    )
    return Qt3DInput.QAbstractPhysicalDevicePrivate._cuteAt(address)

  @staticmethod
  def axisSettings(*__, **_) -> Never:
    """
    Qt's 'QList<QAxisSetting *>
    Qt3DInput::QAbstractPhysicalDevice::axisSettings() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DInput.QAbstractPhysicalDevice.axisSettings' has no cute "
        "function yet. Qt's 'QList<QAxisSetting *> "
        "Qt3DInput::QAbstractPhysicalDevice::axisSettings() const': gives a "
        "type Python has no way to take yet.")
