"""
QSaveFilePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qsavefile_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QSaveFilePrivate to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from . import QFileDevice, QFileDevicePrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QSaveFile


class QSaveFilePrivate(QFileDevicePrivate):
  """
  The cute side of Qt's QSaveFilePrivate: a plain Python object standing in
  front of one C++ QSaveFilePrivate.

  It is built on the cute 'QFileDevicePrivate', as Qt's QSaveFilePrivate is
  built on Qt's QFileDevicePrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSaveFilePrivate that has a ritual and that Python
  can call so far, 3 names in all: 'q_func', 'permissions', 'setPermissions'.
  None can be made from Python: one comes out of a function of another class
  that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QSaveFile *QSaveFilePrivate::q_func() const': takes in Python
    what 'QSaveFile *QSaveFilePrivate::q_func()' takes.
  - Qt's 'QSaveFilePrivate::~QSaveFilePrivate()': the destructor: Python
    never removes a C++ QSaveFilePrivate.

  What has no ritual
  ------------------

  2 of the 7 functions Qt declares: 2 leans on 'QFileDevicePrivate.

  What to expect
  --------------

  - The C++ QSaveFilePrivate is created at the first use, not by
    'QSaveFilePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSaveFilePrivate.
  - Each name of Qt's QSaveFilePrivate that has no cute function yet,
    '__init__', 'open', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSaveFilePrivate'

  #  A C++ QSaveFilePrivate Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSaveFilePrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def permissions(self) -> QFileDevice.Permissions:
    """
    Calls Qt's 'QFileDevice::Permissions QSaveFilePrivate::permissions()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qsavefileprivate.html#permissions

    Returns
    -------

    QFileDevice.Permissions
      The value standing for the combination Qt gave back.
    """
    #  QFileDevice::Permissions QSaveFilePrivate::permissions() const
    ritual = 'ritual_ZNK16QSaveFilePrivate11permissionsEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK16QSaveFilePrivate11permissionsEv'
    return QFileDevice.Permissions(self.uglySide.call(ritual))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QFileDevice.Permissions)
  def setPermissions(self, perms: QFileDevice.Permissions) -> bool:
    """
    Calls Qt's 'bool
    QSaveFilePrivate::setPermissions(QFileDevice::Permissions perms)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsavefileprivate.html#setPermissions

    Parameters
    ----------

    perms : QFileDevice.Permissions
      Passed on as its number.
    """
    #  bool QSaveFilePrivate::setPermissions(QFileDevice::Permissions perms)
    ritual = (
        'ritual_ZN16QSaveFilePrivate14setPermissionsE6QFlagsIN11QFileDevice'
        '10PermissionEE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QSaveFilePrivate14setPermissionsE6QFlagsIN11QFile'
          'Device10PermissionEE')
    return self.uglySide.call(ritual, perms.value)

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
    Qt's 'QSaveFilePrivate::QSaveFilePrivate()': leans on
    'QFileDevicePrivate::setError(QFileDevice::FileError, QString)', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QSaveFilePrivate.__init__' has no cute function yet. Qt's "
        "'QSaveFilePrivate::QSaveFilePrivate()': leans on "
        "'QFileDevicePrivate::setError(QFileDevice::FileError, QString)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

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

  def q_func(self) -> Optional[QSaveFile]:
    """
    Calls Qt's 'QSaveFile *QSaveFilePrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qsavefileprivate.html#q_func

    Returns
    -------

    Optional[QSaveFile]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSaveFile *QSaveFilePrivate::q_func()
    address = self.uglySide.call('ritual_ZN16QSaveFilePrivate6q_funcEv')
    from . import QSaveFile
    return QSaveFile._cuteAt(address)

  @staticmethod
  def open(*__, **_) -> Never:
    """
    Qt's 'bool QSaveFilePrivate::open(QIODevice::OpenMode mode)': leans on
    'QFileDevicePrivate::setError(QFileDevice::FileError, QString)', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QSaveFilePrivate.open' has no cute function yet. Qt's 'bool "
        "QSaveFilePrivate::open(QIODevice::OpenMode mode)': leans on "
        "'QFileDevicePrivate::setError(QFileDevice::FileError, QString)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")
