"""
QResource binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qresource.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from . import QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QByteArray, QDateTime, QLocale
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QLocale = WAIT['QLocale']


class QResource(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QResource: a plain Python object standing in front of
  one C++ QResource.

  What exists
  -----------

  Every function of Qt's QResource that has a ritual and that Python can call
  so far, 16 names in all: 'setFileName', 'fileName', 'absoluteFilePath',
  'setLocale', 'locale', 'isValid', 'compressionAlgorithm', 'size',
  'uncompressedSize', 'uncompressedData', 'lastModified', 'registerResource',
  'unregisterResource', 'isDir', 'isFile', 'children'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QResource::~QResource()': the destructor: Python never removes a
    C++ QResource.
  - Qt's 'const uchar *QResource::data() const': gives 'unsigned char', which
    has no cute class yet.
  - Qt's 'bool QResource::registerResource(const uchar *rccData, const
    QString &resourceRoot)': names 'uchar', which has no cute class yet.
  - Qt's 'bool QResource::unregisterResource(const uchar *rccData, const
    QString &resourceRoot)': names 'uchar', which has no cute class yet.
  - Qt's 'QResourcePrivate *QResource::d_func()': gives 'QResourcePrivate',
    which has no cute class yet.
  - Qt's 'const QResourcePrivate *QResource::d_func() const': gives
    'QResourcePrivate', which has no cute class yet.

  What to expect
  --------------

  - The C++ QResource is created at the first use, not by 'QResource(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QResource.
  - Each name of Qt's QResource that has no cute function yet, 'd_func',
    'data', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  #  The enums Qt writes inside QResource, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class Compression(CuteNum):
    """
    The enum 'QResource::Compression' of Qt, with the 3 names Qt gives in it.
    """

    NoCompression = Kee[int](0)
    ZlibCompression = Kee[int](1)
    ZstdCompression = Kee[int](2)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  @overload(str, str)
  def registerResource(rccFilename: str, resourceRoot: str = '') -> bool:
    """
    Calls Qt's 'bool QResource::registerResource(const QString &rccFilename,
    const QString &resourceRoot)'.

    Qt's own words: https://doc.qt.io/qt-6/qresource.html#registerResource

    Parameters
    ----------

    rccFilename : str
      Passed on as it is: a QString is made of it for the call.

    resourceRoot : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.
    """
    #  bool QResource::registerResource(const QString &rccFilename, const
    #      QString &resourceRoot)
    return Rituals.call(
        'ritual_ZN9QResource16registerResourceERK7QStringS2_',
        rccFilename, resourceRoot,
    )

  @staticmethod
  @overload(str)
  @overload(str, str)
  def unregisterResource(rccFilename: str, resourceRoot: str = '') -> bool:
    """
    Calls Qt's 'bool QResource::unregisterResource(const QString
    &rccFilename, const QString &resourceRoot)'.

    Qt's own words: https://doc.qt.io/qt-6/qresource.html#unregisterResource

    Parameters
    ----------

    rccFilename : str
      Passed on as it is: a QString is made of it for the call.

    resourceRoot : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.
    """
    #  bool QResource::unregisterResource(const QString &rccFilename, const
    #      QString &resourceRoot)
    return Rituals.call(
        'ritual_ZN9QResource18unregisterResourceERK7QStringS2_',
        rccFilename, resourceRoot,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QResource'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def fileName(self) -> str:
    """
    Calls Qt's 'QString QResource::fileName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qresource.html#fileName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QResource::fileName() const
    return self.uglySide.call('ritual_ZNK9QResource8fileNameEv')

  def absoluteFilePath(self) -> str:
    """
    Calls Qt's 'QString QResource::absoluteFilePath() const'.

    Qt's own words: https://doc.qt.io/qt-6/qresource.html#absoluteFilePath

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QResource::absoluteFilePath() const
    return self.uglySide.call('ritual_ZNK9QResource16absoluteFilePathEv')

  def locale(self) -> QLocale:
    """
    Calls Qt's 'QLocale QResource::locale() const'.

    Qt's own words: https://doc.qt.io/qt-6/qresource.html#locale

    Returns
    -------

    QLocale
      A new cute QLocale around the copy Qt gave back. Python owns it.
    """
    #  QLocale QResource::locale() const
    address = self.uglySide.call('ritual_ZNK9QResource6localeEv')
    from . import QLocale
    return QLocale._cuteOwning(address)

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QResource::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qresource.html#isValid
    """
    #  bool QResource::isValid() const
    return self.uglySide.call('ritual_ZNK9QResource7isValidEv')

  def compressionAlgorithm(self) -> Compression:
    """
    Calls Qt's 'Compression QResource::compressionAlgorithm() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qresource.html#compressionAlgorithm

    Returns
    -------

    Compression
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Compression(number)'
      gives.
    """
    #  Compression QResource::compressionAlgorithm() const
    return QResource.Compression(self.uglySide.call(
        'ritual_ZNK9QResource20compressionAlgorithmEv',
    ))

  def size(self) -> int:
    """
    Calls Qt's 'qint64 QResource::size() const'.

    Qt's own words: https://doc.qt.io/qt-6/qresource.html#size
    """
    #  qint64 QResource::size() const
    return self.uglySide.call('ritual_ZNK9QResource4sizeEv')

  def uncompressedSize(self) -> int:
    """
    Calls Qt's 'qint64 QResource::uncompressedSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qresource.html#uncompressedSize
    """
    #  qint64 QResource::uncompressedSize() const
    return self.uglySide.call('ritual_ZNK9QResource16uncompressedSizeEv')

  def uncompressedData(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QResource::uncompressedData() const'.

    Qt's own words: https://doc.qt.io/qt-6/qresource.html#uncompressedData

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QResource::uncompressedData() const
    address = self.uglySide.call('ritual_ZNK9QResource16uncompressedDataEv')
    from . import QByteArray
    return QByteArray._cuteOwning(address)

  def lastModified(self) -> QDateTime:
    """
    Calls Qt's 'QDateTime QResource::lastModified() const'.

    Qt's own words: https://doc.qt.io/qt-6/qresource.html#lastModified

    Returns
    -------

    QDateTime
      A new cute QDateTime around the copy Qt gave back. Python owns it.
    """
    #  QDateTime QResource::lastModified() const
    address = self.uglySide.call('ritual_ZNK9QResource12lastModifiedEv')
    from . import QDateTime
    return QDateTime._cuteOwning(address)

  def isDir(self) -> bool:
    """
    Calls Qt's 'bool QResource::isDir() const'.

    Qt's own words: https://doc.qt.io/qt-6/qresource.html#isDir
    """
    #  bool QResource::isDir() const
    return self.uglySide.call('ritual_ZNK9QResource5isDirEv')

  def isFile(self) -> bool:
    """
    Calls Qt's 'bool QResource::isFile() const'.

    Qt's own words: https://doc.qt.io/qt-6/qresource.html#isFile
    """
    #  bool QResource::isFile() const
    return self.uglySide.call('ritual_ZNK9QResource6isFileEv')

  def children(self) -> QStringList:
    """
    Calls Qt's 'QStringList QResource::children() const'.

    Qt's own words: https://doc.qt.io/qt-6/qresource.html#children

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QResource::children() const
    address = self.uglySide.call('ritual_ZNK9QResource8childrenEv')
    return QStringList._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setFileName(self, file: str) -> None:
    """
    Calls Qt's 'void QResource::setFileName(const QString &file)'.

    Qt's own words: https://doc.qt.io/qt-6/qresource.html#setFileName

    Parameters
    ----------

    file : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QResource::setFileName(const QString &file)
    self.uglySide.call('ritual_ZN9QResource11setFileNameERK7QString', file)

  @overload(QLocale)
  def setLocale(self, locale: QLocale) -> None:
    """
    Calls Qt's 'void QResource::setLocale(const QLocale &locale)'.

    Qt's own words: https://doc.qt.io/qt-6/qresource.html#setLocale

    Parameters
    ----------

    locale : QLocale
      Passed on as a value: Qt reads the C++ QLocale, which stays Python's
      own.
    """
    #  void QResource::setLocale(const QLocale &locale)
    self.uglySide.call(
        'ritual_ZN9QResource9setLocaleERK7QLocale', self._valueOf(locale),
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
  @overload(str)
  @overload(str, QLocale)
  def __init__(
      self,
      file: str = '',
      locale: Optional[QLocale] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'QResource::QResource(const QString &file,
    const QLocale &locale)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qresource.html#QResource

    Parameters
    ----------

    file : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    locale : Optional[QLocale]
      Passed on as a value: Qt reads the C++ QLocale, which stays Python's
      own. May be left out, as in Qt: a new 'QLocale()' is then passed on.
    """
    #  QResource::QResource(const QString &file, const QLocale &locale)
    if locale is None:
      from . import QLocale
      locale = QLocale()
    self._noteCreation(QResource, lambda: Rituals.call(
        'ritual_ZN9QResourceC1ERK7QStringRK7QLocale',
        file, self._valueOf(locale),
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

  @staticmethod
  def d_func(*__, **_) -> Never:
    """
    - Qt's 'QResourcePrivate *QResource::d_func()': gives 'QResourcePrivate',
      which has no cute class yet.
    - Qt's 'const QResourcePrivate *QResource::d_func() const': gives
      'QResourcePrivate', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QResource.d_func' has no cute function yet. Qt's "
        "'QResourcePrivate *QResource::d_func()': gives 'QResourcePrivate', "
        "which has no cute class yet. Qt's 'const QResourcePrivate "
        "*QResource::d_func() const': gives 'QResourcePrivate', which has "
        "no cute class yet.")

  @staticmethod
  def data(*__, **_) -> Never:
    """
    Qt's 'const uchar *QResource::data() const': gives 'unsigned char', which
    has no cute class yet.
    """
    raise NotImplementedError(
        "'QResource.data' has no cute function yet. Qt's 'const uchar "
        "*QResource::data() const': gives 'unsigned char', which has no "
        "cute class yet.")
