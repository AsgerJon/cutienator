"""
QZipWriter binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qzipwriter_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QZipWriter to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from . import QFileDevice, QIODeviceBase

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QByteArray, QIODevice
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QIODevice = WAIT['QIODevice']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QZipWriter(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QZipWriter: a plain Python object standing in front
  of one C++ QZipWriter.

  What exists
  -----------

  Every function of Qt's QZipWriter that has a ritual and that Python can
  call so far, 11 names in all: 'device', 'isWritable', 'exists', 'status',
  'setCompressionPolicy', 'compressionPolicy', 'setCreationPermissions',
  'addFile', 'addDirectory', 'addSymLink', 'close'. It can be made from
  Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QZipWriter::~QZipWriter()': the destructor: Python never removes a
    C++ QZipWriter.
  - Qt's 'QFile::Permissions QZipWriter::creationPermissions() const': gives
    a type Python has no way to take yet.

  What has no ritual
  ------------------

  4 of the 20 functions Qt declares: 4 forbidden.

  What to expect
  --------------

  - The C++ QZipWriter is created at the first use, not by 'QZipWriter(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QZipWriter.
  - Each name of Qt's QZipWriter that has no cute function yet,
    'creationPermissions', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QZipWriter, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class CompressionPolicy(CuteNum):
    """
    The enum 'QZipWriter::CompressionPolicy' of Qt, with the 3 names Qt gives
    in it.
    """

    AlwaysCompress = Kee[int](0)
    NeverCompress = Kee[int](1)
    AutoCompress = Kee[int](2)

  class Status(CuteNum):
    """
    The enum 'QZipWriter::Status' of Qt, with the 5 names Qt gives in it.
    """

    NoError = Kee[int](0)
    FileWriteError = Kee[int](1)
    FileOpenError = Kee[int](2)
    FilePermissionsError = Kee[int](3)
    FileError = Kee[int](4)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QZipWriter'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def device(self) -> Optional[QIODevice]:
    """
    Calls Qt's 'QIODevice *QZipWriter::device() const'.

    Qt's own words: https://doc.qt.io/qt-6/qzipwriter.html#device

    Returns
    -------

    Optional[QIODevice]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QIODevice *QZipWriter::device() const
    address = self.uglySide.call('ritual_ZNK10QZipWriter6deviceEv')
    from . import QIODevice
    return QIODevice._cuteAt(address)

  def isWritable(self) -> bool:
    """
    Calls Qt's 'bool QZipWriter::isWritable() const'.

    Qt's own words: https://doc.qt.io/qt-6/qzipwriter.html#isWritable
    """
    #  bool QZipWriter::isWritable() const
    return self.uglySide.call('ritual_ZNK10QZipWriter10isWritableEv')

  def exists(self) -> bool:
    """
    Calls Qt's 'bool QZipWriter::exists() const'.

    Qt's own words: https://doc.qt.io/qt-6/qzipwriter.html#exists
    """
    #  bool QZipWriter::exists() const
    return self.uglySide.call('ritual_ZNK10QZipWriter6existsEv')

  def status(self) -> Status:
    """
    Calls Qt's 'Status QZipWriter::status() const'.

    Qt's own words: https://doc.qt.io/qt-6/qzipwriter.html#status

    Returns
    -------

    Status
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Status(number)' gives.
    """
    #  Status QZipWriter::status() const
    return QZipWriter.Status(self.uglySide.call(
        'ritual_ZNK10QZipWriter6statusEv',
    ))

  def compressionPolicy(self) -> CompressionPolicy:
    """
    Calls Qt's 'CompressionPolicy QZipWriter::compressionPolicy() const'.

    Qt's own words: https://doc.qt.io/qt-6/qzipwriter.html#compressionPolicy

    Returns
    -------

    CompressionPolicy
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'CompressionPolicy(number)' gives.
    """
    #  CompressionPolicy QZipWriter::compressionPolicy() const
    return QZipWriter.CompressionPolicy(self.uglySide.call(
        'ritual_ZNK10QZipWriter17compressionPolicyEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(CompressionPolicy)
  def setCompressionPolicy(self, policy: CompressionPolicy) -> None:
    """
    Calls Qt's 'void QZipWriter::setCompressionPolicy(CompressionPolicy
    policy)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qzipwriter.html#setCompressionPolicy

    Parameters
    ----------

    policy : CompressionPolicy
      Passed on as its number.
    """
    #  void QZipWriter::setCompressionPolicy(CompressionPolicy policy)
    self.uglySide.call(
        'ritual_ZN10QZipWriter20setCompressionPolicyENS_17CompressionPolicy'
        'E',
        policy.value,
    )

  @overload(QFileDevice.Permissions)
  def setCreationPermissions(
      self,
      permissions: QFileDevice.Permissions,
  ) -> None:
    """
    Calls Qt's 'void QZipWriter::setCreationPermissions(QFile::Permissions
    permissions)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qzipwriter.html#setCreationPermissions

    Parameters
    ----------

    permissions : QFileDevice.Permissions
      Passed on as its number.
    """
    #  void QZipWriter::setCreationPermissions(QFile::Permissions
    #      permissions)
    self.uglySide.call(
        'ritual_ZN10QZipWriter22setCreationPermissionsE6QFlagsIN11QFileDevi'
        'ce10PermissionEE',
        permissions.value,
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

  @overload(str)
  @overload(str, QIODeviceBase.OpenMode)
  def __init__(
      self,
      fileName: str,
      mode: QIODeviceBase.OpenMode = (
          QIODeviceBase.OpenMode.WriteOnly |
          QIODeviceBase.OpenMode.Truncate),
  ) -> None:
    """
    Notes what was given, for Qt's 'QZipWriter::QZipWriter(const QString
    &fileName, QIODevice::OpenMode mode)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qzipwriter.html#QZipWriter

    Parameters
    ----------

    fileName : str
      Passed on as it is: a QString is made of it for the call.

    mode : QIODeviceBase.OpenMode
      Passed on as its number. May be left out, as in Qt: it is then
      QIODeviceBase.OpenMode.WriteOnly | QIODeviceBase.OpenMode.Truncate.
    """
    #  QZipWriter::QZipWriter(const QString &fileName, QIODevice::OpenMode
    #      mode)
    self._noteCreation(QZipWriter, lambda: Rituals.call(
        'ritual_ZN10QZipWriterC1ERK7QString6QFlagsIN13QIODeviceBase12OpenMo'
        'deFlagEE',
        fileName, mode.value,
    ))

  @overload(QIODevice)
  @overload(NoneType)
  def __init__(self, device: Optional[QIODevice]) -> None:
    """
    Notes what was given, for Qt's 'QZipWriter::QZipWriter(QIODevice
    *device)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qzipwriter.html#QZipWriter

    Parameters
    ----------

    device : Optional[QIODevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QZipWriter::QZipWriter(QIODevice *device)
    self._noteCreation(QZipWriter, lambda: Rituals.call(
        'ritual_ZN10QZipWriterC1EP9QIODevice', self._addressOf(device),
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

  @overload(str, QByteArray)
  def addFile(self, fileName: str, data: QByteArray) -> None:
    """
    Calls Qt's 'void QZipWriter::addFile(const QString &fileName, const
    QByteArray &data)'.

    Qt's own words: https://doc.qt.io/qt-6/qzipwriter.html#addFile

    Parameters
    ----------

    fileName : str
      Passed on as it is: a QString is made of it for the call.

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QZipWriter::addFile(const QString &fileName, const QByteArray
    #      &data)
    self.uglySide.call(
        'ritual_ZN10QZipWriter7addFileERK7QStringRK10QByteArray',
        fileName, self._valueOf(data),
    )

  @overload(str, QIODevice)
  @overload(str, NoneType)
  def addFile(self, fileName: str, device: Optional[QIODevice]) -> None:
    """
    Calls Qt's 'void QZipWriter::addFile(const QString &fileName, QIODevice
    *device)'.

    Qt's own words: https://doc.qt.io/qt-6/qzipwriter.html#addFile

    Parameters
    ----------

    fileName : str
      Passed on as it is: a QString is made of it for the call.

    device : Optional[QIODevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QZipWriter::addFile(const QString &fileName, QIODevice *device)
    self.uglySide.call(
        'ritual_ZN10QZipWriter7addFileERK7QStringP9QIODevice',
        fileName, self._addressOf(device),
    )

  @overload(str)
  def addDirectory(self, dirName: str) -> None:
    """
    Calls Qt's 'void QZipWriter::addDirectory(const QString &dirName)'.

    Qt's own words: https://doc.qt.io/qt-6/qzipwriter.html#addDirectory

    Parameters
    ----------

    dirName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QZipWriter::addDirectory(const QString &dirName)
    self.uglySide.call(
        'ritual_ZN10QZipWriter12addDirectoryERK7QString', dirName,
    )

  @overload(str, str)
  def addSymLink(self, fileName: str, destination: str) -> None:
    """
    Calls Qt's 'void QZipWriter::addSymLink(const QString &fileName, const
    QString &destination)'.

    Qt's own words: https://doc.qt.io/qt-6/qzipwriter.html#addSymLink

    Parameters
    ----------

    fileName : str
      Passed on as it is: a QString is made of it for the call.

    destination : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QZipWriter::addSymLink(const QString &fileName, const QString
    #      &destination)
    self.uglySide.call(
        'ritual_ZN10QZipWriter10addSymLinkERK7QStringS2_',
        fileName, destination,
    )

  def close(self) -> None:
    """
    Calls Qt's 'void QZipWriter::close()'.

    Qt's own words: https://doc.qt.io/qt-6/qzipwriter.html#close
    """
    #  void QZipWriter::close()
    self.uglySide.call('ritual_ZN10QZipWriter5closeEv')

  @staticmethod
  def creationPermissions(*__, **_) -> Never:
    """
    Qt's 'QFile::Permissions QZipWriter::creationPermissions() const': gives
    a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QZipWriter.creationPermissions' has no cute function yet. Qt's "
        "'QFile::Permissions QZipWriter::creationPermissions() const': "
        "gives a type Python has no way to take yet.")
