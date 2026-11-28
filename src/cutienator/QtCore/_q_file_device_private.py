"""
QFileDevicePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qfiledevice_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QFileDevicePrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..occult import Rituals
from . import QFileDevice, QIODevicePrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QAbstractFileEngine


class QFileDevicePrivate(QIODevicePrivate):
  """
  The cute side of Qt's QFileDevicePrivate: a plain Python object standing in
  front of one C++ QFileDevicePrivate.

  It is built on the cute 'QIODevicePrivate', as Qt's QFileDevicePrivate is
  built on Qt's QIODevicePrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QFileDevicePrivate that has a ritual and that Python
  can call so far, 6 names in all: 'q_func', 'engine', 'permissions',
  'setPermissions', 'ensureFlushed', 'setError'. It can be made from Python,
  in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QFileDevice *QFileDevicePrivate::q_func() const': takes in
    Python what 'QFileDevice *QFileDevicePrivate::q_func()' takes.
  - Qt's 'QFileDevicePrivate::~QFileDevicePrivate()': the destructor: Python
    never removes a C++ QFileDevicePrivate.
  - Qt's 'bool QFileDevicePrivate::putCharHelper(char c)': takes a single
    letter as C has it.

  What to expect
  --------------

  - The C++ QFileDevicePrivate is created at the first use, not by
    'QFileDevicePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QFileDevicePrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QFileDevicePrivate'

  #  A C++ QFileDevicePrivate Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QFileDevicePrivate'

  #  The functions Qt calls itself that QFileDevicePrivate is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'engine': (
          ('_ZNK18QFileDevicePrivate6engineEv',
           ('address', 'address', 'QtCore:QAbstractFileEngine'),
           ()),
      ),
      'permissions': (
          ('_ZNK18QFileDevicePrivate11permissionsEv',
           ('int', 'flags', 'QtCore:QFileDevice.Permission'),
           ()),
      ),
      'setPermissions': (
          ('_ZN18QFileDevicePrivate14setPermissionsE6QFlagsIN11QFileDevice1'
           '0PermissionEE',
           ('bool', 'number', ''),
           (
               ('int', 'flags', 'QtCore:QFileDevice.Permission'),
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

  def engine(self) -> Optional[QAbstractFileEngine]:
    """
    Calls Qt's 'QAbstractFileEngine *QFileDevicePrivate::engine() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfiledeviceprivate.html#engine

    Returns
    -------

    Optional[QAbstractFileEngine]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractFileEngine *QFileDevicePrivate::engine() const
    ritual = 'ritual_ZNK18QFileDevicePrivate6engineEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK18QFileDevicePrivate6engineEv'
    address = self.uglySide.call(ritual)
    from . import QAbstractFileEngine
    return QAbstractFileEngine._cuteAt(address)

  def permissions(self) -> QFileDevice.Permissions:
    """
    Calls Qt's 'QFileDevice::Permissions QFileDevicePrivate::permissions()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfiledeviceprivate.html#permissions

    Returns
    -------

    QFileDevice.Permissions
      The value standing for the combination Qt gave back.
    """
    #  QFileDevice::Permissions QFileDevicePrivate::permissions() const
    ritual = 'ritual_ZNK18QFileDevicePrivate11permissionsEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK18QFileDevicePrivate11permissionsEv'
    return QFileDevice.Permissions(self.uglySide.call(ritual))

  def ensureFlushed(self) -> bool:
    """
    Calls Qt's 'bool QFileDevicePrivate::ensureFlushed() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfiledeviceprivate.html#ensureFlushed
    """
    #  bool QFileDevicePrivate::ensureFlushed() const
    return self.uglySide.call(
        'ritual_ZNK18QFileDevicePrivate13ensureFlushedEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QFileDevice.Permissions)
  def setPermissions(self, perms: QFileDevice.Permissions) -> bool:
    """
    Calls Qt's 'bool
    QFileDevicePrivate::setPermissions(QFileDevice::Permissions perms)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfiledeviceprivate.html#setPermissions

    Parameters
    ----------

    perms : QFileDevice.Permissions
      Passed on as its number.
    """
    #  bool QFileDevicePrivate::setPermissions(QFileDevice::Permissions
    #      perms)
    ritual = (
        'ritual_ZN18QFileDevicePrivate14setPermissionsE6QFlagsIN11QFileDevi'
        'ce10PermissionEE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QFileDevicePrivate14setPermissionsE6QFlagsIN11QFi'
          'leDevice10PermissionEE')
    return self.uglySide.call(ritual, perms.value)

  @overload(QFileDevice.FileError)
  def setError(self, err: QFileDevice.FileError) -> None:
    """
    Calls Qt's 'void QFileDevicePrivate::setError(QFileDevice::FileError
    err)'.

    Qt's own words: https://doc.qt.io/qt-6/qfiledeviceprivate.html#setError

    Parameters
    ----------

    err : QFileDevice.FileError
      Passed on as its number.
    """
    #  void QFileDevicePrivate::setError(QFileDevice::FileError err)
    self.uglySide.call(
        'ritual_ZN18QFileDevicePrivate8setErrorEN11QFileDevice9FileErrorE',
        err.value,
    )

  @overload(QFileDevice.FileError, str)
  def setError(self, err: QFileDevice.FileError, errorString: str) -> None:
    """
    Calls Qt's 'void QFileDevicePrivate::setError(QFileDevice::FileError err,
    QString errorString)'.

    Qt's own words: https://doc.qt.io/qt-6/qfiledeviceprivate.html#setError

    Parameters
    ----------

    err : QFileDevice.FileError
      Passed on as its number.

    errorString : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QFileDevicePrivate::setError(QFileDevice::FileError err, QString
    #      errorString)
    self.uglySide.call(
        'ritual_ZN18QFileDevicePrivate8setErrorEN11QFileDevice9FileErrorE7Q'
        'String',
        err.value, errorString,
    )

  @overload(QFileDevice.FileError, int)
  def setError(self, err: QFileDevice.FileError, errNum: int) -> None:
    """
    Calls Qt's 'void QFileDevicePrivate::setError(QFileDevice::FileError err,
    int errNum)'.

    Qt's own words: https://doc.qt.io/qt-6/qfiledeviceprivate.html#setError

    Parameters
    ----------

    err : QFileDevice.FileError
      Passed on as its number.

    errNum : int
      Passed on as it is.
    """
    #  void QFileDevicePrivate::setError(QFileDevice::FileError err, int
    #      errNum)
    self.uglySide.call(
        'ritual_ZN18QFileDevicePrivate8setErrorEN11QFileDevice9FileErrorEi',
        err.value, errNum,
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
    Notes what was given, for Qt's
    'QFileDevicePrivate::QFileDevicePrivate()', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qfiledeviceprivate.html#QFileDevicePrivate
    """
    #  QFileDevicePrivate::QFileDevicePrivate()
    self._noteCreation(QFileDevicePrivate, lambda: Rituals.call(
        'ritual_ZN18QFileDevicePrivateC1Ev',
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

  def q_func(self) -> Optional[QFileDevice]:
    """
    Calls Qt's 'QFileDevice *QFileDevicePrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qfiledeviceprivate.html#q_func

    Returns
    -------

    Optional[QFileDevice]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QFileDevice *QFileDevicePrivate::q_func()
    address = self.uglySide.call('ritual_ZN18QFileDevicePrivate6q_funcEv')
    return QFileDevice._cuteAt(address)
