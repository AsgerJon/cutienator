"""
QFile binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of QtCore/qfile.h,
#  Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QFileDevice, QIODeviceBase, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QByteArray, QMetaObject
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QFile(QFileDevice):
  """
  The cute side of Qt's QFile: a plain Python object standing in front of one
  C++ QFile.

  It is built on the cute 'QFileDevice', as Qt's QFile is built on Qt's
  QFileDevice, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QFile that has a ritual and that Python can call so
  far, 18 names in all: 'metaObject', 'tr', 'fileName', 'setFileName',
  'encodeName', 'decodeName', 'exists', 'symLinkTarget', 'remove',
  'supportsMoveToTrash', 'moveToTrash', 'rename', 'link', 'open', 'size',
  'resize', 'permissions', 'setPermissions'. It can be made from Python, in 4
  ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QFile::~QFile()': the destructor: Python never removes a C++ QFile.
  - Qt's 'bool QFile::moveToTrash(const QString &fileName, QString
    *pathInTrash)': names 'QString', which has no cute class yet.

  What has no ritual
  ------------------

  29 of the 64 functions Qt declares: 16 a template; 7 takes or gives a type
  that cannot be passed yet; 3 private; 2 forbidden; 1 protected.

  What to expect
  --------------

  - The C++ QFile is created at the first use, not by 'QFile(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QFile.
  - Qt tells when it has removed the C++ QFile. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
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
    Calls Qt's 'QString QFile::tr(const char *s, const char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qfile.html#tr

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
    #  QString QFile::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN5QFile2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(str)
  def encodeName(fileName: str) -> QByteArray:
    """
    Calls Qt's 'QByteArray QFile::encodeName(const QString &fileName)'.

    Qt's own words: https://doc.qt.io/qt-6/qfile.html#encodeName

    Parameters
    ----------

    fileName : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QFile::encodeName(const QString &fileName)
    address = Rituals.call(
        'ritual_ZN5QFile10encodeNameERK7QString', fileName,
    )
    from . import QByteArray
    return QByteArray._cuteOwning(address)

  @staticmethod
  @overload(QByteArray)
  def decodeName(localFileName: QByteArray) -> str:
    """
    Calls Qt's 'QString QFile::decodeName(const QByteArray &localFileName)'.

    Qt's own words: https://doc.qt.io/qt-6/qfile.html#decodeName

    Parameters
    ----------

    localFileName : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QFile::decodeName(const QByteArray &localFileName)
    return Rituals.call(
        'ritual_ZN5QFile10decodeNameERK10QByteArray',
        CuteMixin._valueOf(localFileName),
    )

  @staticmethod
  @overload(str)
  @overload(NoneType)
  def decodeName(localFileName: Optional[str]) -> str:
    """
    Calls Qt's 'QString QFile::decodeName(const char *localFileName)'.

    Qt's own words: https://doc.qt.io/qt-6/qfile.html#decodeName

    Parameters
    ----------

    localFileName : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QFile::decodeName(const char *localFileName)
    return Rituals.call(
        'ritual_ZN5QFile10decodeNameEPKc', CuteMixin._bytesOf(localFileName),
    )

  @staticmethod
  def supportsMoveToTrash() -> bool:
    """
    Calls Qt's 'bool QFile::supportsMoveToTrash()'.

    Qt's own words: https://doc.qt.io/qt-6/qfile.html#supportsMoveToTrash
    """
    #  bool QFile::supportsMoveToTrash()
    return Rituals.call('ritual_ZN5QFile19supportsMoveToTrashEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QFile'

  #  A C++ QFile Python makes is of a C++ class of ours, in which Python can
  #  take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QFile'

  #  The functions Qt calls itself that QFile is the first to declare and
  #  that cannot be handed to Python yet, each as Qt declares it. A class of
  #  a program that writes one of them anew is refused, since Qt would never
  #  call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'open': (
          'bool QFile::open(OpenMode)',
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
    Calls Qt's 'const QMetaObject *QFile::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfile.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QFile::metaObject() const
    address = self.uglySide.call('ritual_ZNK5QFile10metaObjectEv')
    from . import QMetaObject
    return QMetaObject._cuteAt(address)

  def fileName(self) -> str:
    """
    Calls Qt's 'QString QFile::fileName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfile.html#fileName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QFile::fileName() const
    return self.uglySide.call('ritual_ZNK5QFile8fileNameEv')

  @overload()
  def exists(self) -> bool:
    """
    Calls Qt's 'bool QFile::exists() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfile.html#exists
    """
    #  bool QFile::exists() const
    return self.uglySide.call('ritual_ZNK5QFile6existsEv')

  @staticmethod
  @overload(str)
  def exists(fileName: str) -> bool:
    """
    Calls Qt's 'bool QFile::exists(const QString &fileName)'.

    Qt's own words: https://doc.qt.io/qt-6/qfile.html#exists

    Parameters
    ----------

    fileName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QFile::exists(const QString &fileName)
    return Rituals.call('ritual_ZN5QFile6existsERK7QString', fileName)

  @overload()
  def symLinkTarget(self) -> str:
    """
    Calls Qt's 'QString QFile::symLinkTarget() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfile.html#symLinkTarget

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QFile::symLinkTarget() const
    return self.uglySide.call('ritual_ZNK5QFile13symLinkTargetEv')

  @staticmethod
  @overload(str)
  def symLinkTarget(fileName: str) -> str:
    """
    Calls Qt's 'QString QFile::symLinkTarget(const QString &fileName)'.

    Qt's own words: https://doc.qt.io/qt-6/qfile.html#symLinkTarget

    Parameters
    ----------

    fileName : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QFile::symLinkTarget(const QString &fileName)
    return Rituals.call(
        'ritual_ZN5QFile13symLinkTargetERK7QString', fileName,
    )

  def size(self) -> int:
    """
    Calls Qt's 'qint64 QFile::size() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfile.html#size
    """
    #  qint64 QFile::size() const
    ritual = 'ritual_ZNK5QFile4sizeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK5QFile4sizeEv'
    return self.uglySide.call(ritual)

  @overload()
  def permissions(self) -> QFileDevice.Permissions:
    """
    Calls Qt's 'Permissions QFile::permissions() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfile.html#permissions

    Returns
    -------

    QFileDevice.Permissions
      The value standing for the combination Qt gave back.
    """
    #  Permissions QFile::permissions() const
    return QFileDevice.Permissions(self.uglySide.call(
        'ritual_ZNK5QFile11permissionsEv',
    ))

  @staticmethod
  @overload(str)
  def permissions(filename: str) -> QFileDevice.Permissions:
    """
    Calls Qt's 'Permissions QFile::permissions(const QString &filename)'.

    Qt's own words: https://doc.qt.io/qt-6/qfile.html#permissions

    Parameters
    ----------

    filename : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QFileDevice.Permissions
      The value standing for the combination Qt gave back.
    """
    #  Permissions QFile::permissions(const QString &filename)
    return QFileDevice.Permissions(Rituals.call(
        'ritual_ZN5QFile11permissionsERK7QString', filename,
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setFileName(self, name: str) -> None:
    """
    Calls Qt's 'void QFile::setFileName(const QString &name)'.

    Qt's own words: https://doc.qt.io/qt-6/qfile.html#setFileName

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QFile::setFileName(const QString &name)
    self.uglySide.call('ritual_ZN5QFile11setFileNameERK7QString', name)

  @overload(QFileDevice.Permissions)
  def setPermissions(self, permissionSpec: QFileDevice.Permissions) -> bool:
    """
    Calls Qt's 'bool QFile::setPermissions(Permissions permissionSpec)'.

    Qt's own words: https://doc.qt.io/qt-6/qfile.html#setPermissions

    Parameters
    ----------

    permissionSpec : QFileDevice.Permissions
      Passed on as its number.
    """
    #  bool QFile::setPermissions(Permissions permissionSpec)
    return self.uglySide.call(
        'ritual_ZN5QFile14setPermissionsE6QFlagsIN11QFileDevice10Permission'
        'EE',
        permissionSpec.value,
    )

  @staticmethod
  @overload(str, QFileDevice.Permissions)
  def setPermissions(
      filename: str,
      permissionSpec: QFileDevice.Permissions,
  ) -> bool:
    """
    Calls Qt's 'bool QFile::setPermissions(const QString &filename,
    Permissions permissionSpec)'.

    Qt's own words: https://doc.qt.io/qt-6/qfile.html#setPermissions

    Parameters
    ----------

    filename : str
      Passed on as it is: a QString is made of it for the call.

    permissionSpec : QFileDevice.Permissions
      Passed on as its number.
    """
    #  bool QFile::setPermissions(const QString &filename, Permissions
    #      permissionSpec)
    return Rituals.call(
        'ritual_ZN5QFile14setPermissionsERK7QString6QFlagsIN11QFileDevice10'
        'PermissionEE',
        filename, permissionSpec.value,
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
    Notes what was given, for Qt's 'QFile::QFile()', which is called at the
    first use.

    Qt's own words: https://doc.qt.io/qt-6/qfile.html#QFile
    """
    #  QFile::QFile()
    self._noteCreation(QFile, lambda: Rituals.call('ritual_ZN5QFileC1Ev'))

  @overload(str)
  def __init__(self, name: str) -> None:
    """
    Notes what was given, for Qt's 'QFile::QFile(const QString &name)', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qfile.html#QFile

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  QFile::QFile(const QString &name)
    self._noteCreation(QFile, lambda: Rituals.call(
        'ritual_ZN5QFileC1ERK7QString', name,
    ))

  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject]) -> None:
    """
    Notes what was given, for Qt's 'QFile::QFile(QObject *parent)', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qfile.html#QFile

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QFile::QFile(QObject *parent)
    self._noteCreation(QFile, lambda: Rituals.call(
        'ritual_ZN5QFileC1EP7QObject', self._addressOf(parent),
    ))

  @overload(str, QObject)
  @overload(str, NoneType)
  def __init__(self, name: str, parent: Optional[QObject]) -> None:
    """
    Notes what was given, for Qt's 'QFile::QFile(const QString &name, QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qfile.html#QFile

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QFile::QFile(const QString &name, QObject *parent)
    self._noteCreation(QFile, lambda: Rituals.call(
        'ritual_ZN5QFileC1ERK7QStringP7QObject',
        name, self._addressOf(parent),
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

  @overload()
  def remove(self) -> bool:
    """
    Calls Qt's 'bool QFile::remove()'.

    Qt's own words: https://doc.qt.io/qt-6/qfile.html#remove
    """
    #  bool QFile::remove()
    return self.uglySide.call('ritual_ZN5QFile6removeEv')

  @staticmethod
  @overload(str)
  def remove(fileName: str) -> bool:
    """
    Calls Qt's 'bool QFile::remove(const QString &fileName)'.

    Qt's own words: https://doc.qt.io/qt-6/qfile.html#remove

    Parameters
    ----------

    fileName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QFile::remove(const QString &fileName)
    return Rituals.call('ritual_ZN5QFile6removeERK7QString', fileName)

  def moveToTrash(self) -> bool:
    """
    Calls Qt's 'bool QFile::moveToTrash()'.

    Qt's own words: https://doc.qt.io/qt-6/qfile.html#moveToTrash
    """
    #  bool QFile::moveToTrash()
    return self.uglySide.call('ritual_ZN5QFile11moveToTrashEv')

  @overload(str)
  def rename(self, newName: str) -> bool:
    """
    Calls Qt's 'bool QFile::rename(const QString &newName)'.

    Qt's own words: https://doc.qt.io/qt-6/qfile.html#rename

    Parameters
    ----------

    newName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QFile::rename(const QString &newName)
    return self.uglySide.call('ritual_ZN5QFile6renameERK7QString', newName)

  @staticmethod
  @overload(str, str)
  def rename(oldName: str, newName: str) -> bool:
    """
    Calls Qt's 'bool QFile::rename(const QString &oldName, const QString
    &newName)'.

    Qt's own words: https://doc.qt.io/qt-6/qfile.html#rename

    Parameters
    ----------

    oldName : str
      Passed on as it is: a QString is made of it for the call.

    newName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QFile::rename(const QString &oldName, const QString &newName)
    return Rituals.call(
        'ritual_ZN5QFile6renameERK7QStringS2_', oldName, newName,
    )

  @overload(str)
  def link(self, newName: str) -> bool:
    """
    Calls Qt's 'bool QFile::link(const QString &newName)'.

    Qt's own words: https://doc.qt.io/qt-6/qfile.html#link

    Parameters
    ----------

    newName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QFile::link(const QString &newName)
    return self.uglySide.call('ritual_ZN5QFile4linkERK7QString', newName)

  @staticmethod
  @overload(str, str)
  def link(fileName: str, newName: str) -> bool:
    """
    Calls Qt's 'bool QFile::link(const QString &fileName, const QString
    &newName)'.

    Qt's own words: https://doc.qt.io/qt-6/qfile.html#link

    Parameters
    ----------

    fileName : str
      Passed on as it is: a QString is made of it for the call.

    newName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QFile::link(const QString &fileName, const QString &newName)
    return Rituals.call(
        'ritual_ZN5QFile4linkERK7QStringS2_', fileName, newName,
    )

  @overload(QIODeviceBase.OpenMode)
  def open(self, flags: QIODeviceBase.OpenMode) -> bool:
    """
    Calls Qt's 'bool QFile::open(OpenMode flags)'.

    Qt's own words: https://doc.qt.io/qt-6/qfile.html#open

    Parameters
    ----------

    flags : QIODeviceBase.OpenMode
      Passed on as its number.
    """
    #  bool QFile::open(OpenMode flags)
    return self.uglySide.call(
        'ritual_ZN5QFile4openE6QFlagsIN13QIODeviceBase12OpenModeFlagEE',
        flags.value,
    )

  @overload(QIODeviceBase.OpenMode, QFileDevice.Permissions)
  def open(
      self,
      flags: QIODeviceBase.OpenMode,
      permissions: QFileDevice.Permissions,
  ) -> bool:
    """
    Calls Qt's 'bool QFile::open(OpenMode flags, Permissions permissions)'.

    Qt's own words: https://doc.qt.io/qt-6/qfile.html#open

    Parameters
    ----------

    flags : QIODeviceBase.OpenMode
      Passed on as its number.

    permissions : QFileDevice.Permissions
      Passed on as its number.
    """
    #  bool QFile::open(OpenMode flags, Permissions permissions)
    return self.uglySide.call(
        'ritual_ZN5QFile4openE6QFlagsIN13QIODeviceBase12OpenModeFlagEES0_IN'
        '11QFileDevice10PermissionEE',
        flags.value, permissions.value,
    )

  @overload(int, QIODeviceBase.OpenMode)
  @overload(int, QIODeviceBase.OpenMode, QFileDevice.FileHandleFlags)
  def open(
      self,
      fd: int,
      ioFlags: QIODeviceBase.OpenMode,
      handleFlags: QFileDevice.FileHandleFlags = (
          QFileDevice.FileHandleFlags.DontCloseHandle),
  ) -> bool:
    """
    Calls Qt's 'bool QFile::open(int fd, OpenMode ioFlags, FileHandleFlags
    handleFlags)'.

    Qt's own words: https://doc.qt.io/qt-6/qfile.html#open

    Parameters
    ----------

    fd : int
      Passed on as it is.

    ioFlags : QIODeviceBase.OpenMode
      Passed on as its number.

    handleFlags : QFileDevice.FileHandleFlags
      Passed on as its number. May be left out, as in Qt: it is then
      QFileDevice.FileHandleFlags.DontCloseHandle.
    """
    #  bool QFile::open(int fd, OpenMode ioFlags, FileHandleFlags
    #      handleFlags)
    return self.uglySide.call(
        'ritual_ZN5QFile4openEi6QFlagsIN13QIODeviceBase12OpenModeFlagEES0_I'
        'N11QFileDevice14FileHandleFlagEE',
        fd, ioFlags.value, handleFlags.value,
    )

  @overload(int)
  def resize(self, sz: int) -> bool:
    """
    Calls Qt's 'bool QFile::resize(qint64 sz)'.

    Qt's own words: https://doc.qt.io/qt-6/qfile.html#resize

    Parameters
    ----------

    sz : int
      Passed on as it is.
    """
    #  bool QFile::resize(qint64 sz)
    ritual = 'ritual_ZN5QFile6resizeEx'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN5QFile6resizeEx'
    return self.uglySide.call(ritual, sz)

  @staticmethod
  @overload(str, int)
  def resize(filename: str, sz: int) -> bool:
    """
    Calls Qt's 'bool QFile::resize(const QString &filename, qint64 sz)'.

    Qt's own words: https://doc.qt.io/qt-6/qfile.html#resize

    Parameters
    ----------

    filename : str
      Passed on as it is: a QString is made of it for the call.

    sz : int
      Passed on as it is.
    """
    #  bool QFile::resize(const QString &filename, qint64 sz)
    return Rituals.call('ritual_ZN5QFile6resizeERK7QStringx', filename, sz)
