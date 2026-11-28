"""
QZipReader binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qzipreader_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QZipReader to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from . import QIODeviceBase

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QByteArray, QIODevice
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QIODevice = WAIT['QIODevice']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QZipReader(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QZipReader: a plain Python object standing in front
  of one C++ QZipReader.

  What exists
  -----------

  Every function of Qt's QZipReader that has a ritual and that Python can
  call so far, 9 names in all: 'device', 'isReadable', 'exists', 'count',
  'entryInfoAt', 'fileData', 'extractAll', 'status', 'close'. It can be made
  from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QZipReader::~QZipReader()': the destructor: Python never removes a
    C++ QZipReader.
  - Qt's 'QList<FileInfo> QZipReader::fileInfoList() const': gives a type
    Python has no way to take yet.

  What has no ritual
  ------------------

  4 of the 17 functions Qt declares: 4 forbidden.

  What to expect
  --------------

  - The C++ QZipReader is created at the first use, not by 'QZipReader(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QZipReader.
  - Each name of Qt's QZipReader that has no cute function yet,
    'fileInfoList', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  #  The enums Qt writes inside QZipReader, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class Status(CuteNum):
    """
    The enum 'QZipReader::Status' of Qt, with the 5 names Qt gives in it.
    """

    NoError = Kee[int](0)
    FileReadError = Kee[int](1)
    FileOpenError = Kee[int](2)
    FilePermissionsError = Kee[int](3)
    FileError = Kee[int](4)

  #  The classes Qt writes inside QZipReader, each a class in here as in C++.

  class FileInfo(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QZipReader::FileInfo: a plain Python object
    standing in front of one C++ QZipReader::FileInfo.

    C++ hands a QZipReader::FileInfo around as a copy, so every C++
    QZipReader::FileInfo behind a cute one is Python's own: it is removed, by
    the ritual named in '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    Every function of Qt's QZipReader::FileInfo that has a ritual and that
    Python can call so far, 1 name in all: 'isValid'. It can be made from
    Python, in 1 way; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QZipReader::FileInfo::~FileInfo()': the destructor: Python
      removes its C++ QZipReader::FileInfo by it, and has no other use for
      it.

    What to expect
    --------------

    - The C++ QZipReader::FileInfo is created at the first use, not by
      'QZipReader::FileInfo(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QZipReader::FileInfo back gives a copy the ritual
      made for Python, in a new cute QZipReader::FileInfo.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QZipReader::FileInfo'

    #  Qt's '~QZipReader::FileInfo()'. Naming it makes this a value class:
    #  Python owns every C++ QZipReader::FileInfo behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN10QZipReader8FileInfoD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def isValid(self) -> bool:
      """
      Calls Qt's 'bool QZipReader::FileInfo::isValid() const'.

      Qt's own words: https://doc.qt.io/qt-6/qzipreader-fileinfo.html#isValid
      """
      #  bool QZipReader::FileInfo::isValid() const
      return self.uglySide.call('ritual_ZNK10QZipReader8FileInfo7isValidEv')

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload()
    def __init__(self) -> None:
      """
      Notes what was given, for Qt's 'QZipReader::FileInfo::FileInfo()',
      which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qzipreader-fileinfo.html#FileInfo
      """
      #  QZipReader::FileInfo::FileInfo()
      self._noteCreation(QZipReader.FileInfo, lambda: Rituals.call(
          'ritual_ZN10QZipReader8FileInfoC1Ev',
      ))

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QZipReader'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def device(self) -> Optional[QIODevice]:
    """
    Calls Qt's 'QIODevice *QZipReader::device() const'.

    Qt's own words: https://doc.qt.io/qt-6/qzipreader.html#device

    Returns
    -------

    Optional[QIODevice]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QIODevice *QZipReader::device() const
    address = self.uglySide.call('ritual_ZNK10QZipReader6deviceEv')
    from . import QIODevice
    return QIODevice._cuteAt(address)

  def isReadable(self) -> bool:
    """
    Calls Qt's 'bool QZipReader::isReadable() const'.

    Qt's own words: https://doc.qt.io/qt-6/qzipreader.html#isReadable
    """
    #  bool QZipReader::isReadable() const
    return self.uglySide.call('ritual_ZNK10QZipReader10isReadableEv')

  def exists(self) -> bool:
    """
    Calls Qt's 'bool QZipReader::exists() const'.

    Qt's own words: https://doc.qt.io/qt-6/qzipreader.html#exists
    """
    #  bool QZipReader::exists() const
    return self.uglySide.call('ritual_ZNK10QZipReader6existsEv')

  def count(self) -> int:
    """
    Calls Qt's 'int QZipReader::count() const'.

    Qt's own words: https://doc.qt.io/qt-6/qzipreader.html#count
    """
    #  int QZipReader::count() const
    return self.uglySide.call('ritual_ZNK10QZipReader5countEv')

  @overload(int)
  def entryInfoAt(self, index: int) -> FileInfo:
    """
    Calls Qt's 'FileInfo QZipReader::entryInfoAt(int index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qzipreader.html#entryInfoAt

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    FileInfo
      A new cute QZipReader::FileInfo around the copy Qt gave back. Python
      owns it.
    """
    #  FileInfo QZipReader::entryInfoAt(int index) const
    address = self.uglySide.call(
        'ritual_ZNK10QZipReader11entryInfoAtEi', index,
    )
    return QZipReader.FileInfo._cuteOwning(address)

  @overload(str)
  def fileData(self, fileName: str) -> QByteArray:
    """
    Calls Qt's 'QByteArray QZipReader::fileData(const QString &fileName)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qzipreader.html#fileData

    Parameters
    ----------

    fileName : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QZipReader::fileData(const QString &fileName) const
    address = self.uglySide.call(
        'ritual_ZNK10QZipReader8fileDataERK7QString', fileName,
    )
    from . import QByteArray
    return QByteArray._cuteOwning(address)

  @overload(str)
  def extractAll(self, destinationDir: str) -> bool:
    """
    Calls Qt's 'bool QZipReader::extractAll(const QString &destinationDir)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qzipreader.html#extractAll

    Parameters
    ----------

    destinationDir : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QZipReader::extractAll(const QString &destinationDir) const
    return self.uglySide.call(
        'ritual_ZNK10QZipReader10extractAllERK7QString', destinationDir,
    )

  def status(self) -> Status:
    """
    Calls Qt's 'Status QZipReader::status() const'.

    Qt's own words: https://doc.qt.io/qt-6/qzipreader.html#status

    Returns
    -------

    Status
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Status(number)' gives.
    """
    #  Status QZipReader::status() const
    return QZipReader.Status(self.uglySide.call(
        'ritual_ZNK10QZipReader6statusEv',
    ))

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

  @overload(str)
  @overload(str, QIODeviceBase.OpenMode)
  def __init__(
      self,
      fileName: str,
      mode: QIODeviceBase.OpenMode = QIODeviceBase.OpenMode.ReadOnly,
  ) -> None:
    """
    Notes what was given, for Qt's 'QZipReader::QZipReader(const QString
    &fileName, QIODevice::OpenMode mode)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qzipreader.html#QZipReader

    Parameters
    ----------

    fileName : str
      Passed on as it is: a QString is made of it for the call.

    mode : QIODeviceBase.OpenMode
      Passed on as its number. May be left out, as in Qt: it is then
      QIODeviceBase.OpenMode.ReadOnly.
    """
    #  QZipReader::QZipReader(const QString &fileName, QIODevice::OpenMode
    #      mode)
    self._noteCreation(QZipReader, lambda: Rituals.call(
        'ritual_ZN10QZipReaderC1ERK7QString6QFlagsIN13QIODeviceBase12OpenMo'
        'deFlagEE',
        fileName, mode.value,
    ))

  @overload(QIODevice)
  @overload(NoneType)
  def __init__(self, device: Optional[QIODevice]) -> None:
    """
    Notes what was given, for Qt's 'QZipReader::QZipReader(QIODevice
    *device)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qzipreader.html#QZipReader

    Parameters
    ----------

    device : Optional[QIODevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QZipReader::QZipReader(QIODevice *device)
    self._noteCreation(QZipReader, lambda: Rituals.call(
        'ritual_ZN10QZipReaderC1EP9QIODevice', self._addressOf(device),
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

  def close(self) -> None:
    """
    Calls Qt's 'void QZipReader::close()'.

    Qt's own words: https://doc.qt.io/qt-6/qzipreader.html#close
    """
    #  void QZipReader::close()
    self.uglySide.call('ritual_ZN10QZipReader5closeEv')

  @staticmethod
  def fileInfoList(*__, **_) -> Never:
    """
    Qt's 'QList<FileInfo> QZipReader::fileInfoList() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QZipReader.fileInfoList' has no cute function yet. Qt's "
        "'QList<FileInfo> QZipReader::fileInfoList() const': gives a type "
        "Python has no way to take yet.")
