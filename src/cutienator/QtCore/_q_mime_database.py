"""
QMimeDatabase binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qmimedatabase.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QMimeDatabaseMatchMode

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QByteArray, QFileInfo, QIODevice, QMimeType, QUrl
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QFileInfo = WAIT['QFileInfo']
  QIODevice = WAIT['QIODevice']
  QUrl = WAIT['QUrl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QMimeDatabase(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QMimeDatabase: a plain Python object standing in
  front of one C++ QMimeDatabase.

  What exists
  -----------

  Every function of Qt's QMimeDatabase that has a ritual and that Python can
  call so far, 6 names in all: 'mimeTypeForName', 'mimeTypeForFile',
  'mimeTypeForData', 'mimeTypeForUrl', 'mimeTypeForFileNameAndData',
  'suffixForFileName'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QMimeDatabase::~QMimeDatabase()': the destructor: Python never
    removes a C++ QMimeDatabase.

  What has no ritual
  ------------------

  4 of the 15 functions Qt declares: 2 forbidden; 2 takes or gives a type
  that cannot be passed yet.

  What to expect
  --------------

  - The C++ QMimeDatabase is created at the first use, not by
    'QMimeDatabase(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QMimeDatabase.
  """

  #  The enums Qt writes inside QMimeDatabase, and the names Qt has for the
  #  combinations of its flags enums.
  MatchMode = QMimeDatabaseMatchMode

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QMimeDatabase'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def mimeTypeForName(self, nameOrAlias: str) -> QMimeType:
    """
    Calls Qt's 'QMimeType QMimeDatabase::mimeTypeForName(const QString
    &nameOrAlias) const'.

    Qt's own words: https://doc.qt.io/qt-6/qmimedatabase.html#mimeTypeForName

    Parameters
    ----------

    nameOrAlias : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QMimeType
      A new cute QMimeType around the copy Qt gave back. Python owns it.
    """
    #  QMimeType QMimeDatabase::mimeTypeForName(const QString &nameOrAlias)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK13QMimeDatabase15mimeTypeForNameERK7QString', nameOrAlias,
    )
    from . import QMimeType
    return QMimeType._cuteOwning(address)

  @overload(str)
  @overload(str, MatchMode)
  def mimeTypeForFile(
      self,
      fileName: str,
      mode: MatchMode = MatchMode.MatchDefault,
  ) -> QMimeType:
    """
    Calls Qt's 'QMimeType QMimeDatabase::mimeTypeForFile(const QString
    &fileName, MatchMode mode) const'.

    Qt's own words: https://doc.qt.io/qt-6/qmimedatabase.html#mimeTypeForFile

    Parameters
    ----------

    fileName : str
      Passed on as it is: a QString is made of it for the call.

    mode : MatchMode
      Passed on as its number. May be left out, as in Qt: it is then
      MatchMode.MatchDefault.

    Returns
    -------

    QMimeType
      A new cute QMimeType around the copy Qt gave back. Python owns it.
    """
    #  QMimeType QMimeDatabase::mimeTypeForFile(const QString &fileName,
    #      MatchMode mode) const
    address = self.uglySide.call(
        'ritual_ZNK13QMimeDatabase15mimeTypeForFileERK7QStringNS_9MatchMode'
        'E',
        fileName, mode.value,
    )
    from . import QMimeType
    return QMimeType._cuteOwning(address)

  @overload(QFileInfo)
  @overload(QFileInfo, MatchMode)
  def mimeTypeForFile(
      self,
      fileInfo: QFileInfo,
      mode: MatchMode = MatchMode.MatchDefault,
  ) -> QMimeType:
    """
    Calls Qt's 'QMimeType QMimeDatabase::mimeTypeForFile(const QFileInfo
    &fileInfo, MatchMode mode) const'.

    Qt's own words: https://doc.qt.io/qt-6/qmimedatabase.html#mimeTypeForFile

    Parameters
    ----------

    fileInfo : QFileInfo
      Passed on as a value: Qt reads the C++ QFileInfo, which stays Python's
      own.

    mode : MatchMode
      Passed on as its number. May be left out, as in Qt: it is then
      MatchMode.MatchDefault.

    Returns
    -------

    QMimeType
      A new cute QMimeType around the copy Qt gave back. Python owns it.
    """
    #  QMimeType QMimeDatabase::mimeTypeForFile(const QFileInfo &fileInfo,
    #      MatchMode mode) const
    address = self.uglySide.call(
        'ritual_ZNK13QMimeDatabase15mimeTypeForFileERK9QFileInfoNS_9MatchMo'
        'deE',
        self._valueOf(fileInfo), mode.value,
    )
    from . import QMimeType
    return QMimeType._cuteOwning(address)

  @overload(QByteArray)
  def mimeTypeForData(self, data: QByteArray) -> QMimeType:
    """
    Calls Qt's 'QMimeType QMimeDatabase::mimeTypeForData(const QByteArray
    &data) const'.

    Qt's own words: https://doc.qt.io/qt-6/qmimedatabase.html#mimeTypeForData

    Parameters
    ----------

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    Returns
    -------

    QMimeType
      A new cute QMimeType around the copy Qt gave back. Python owns it.
    """
    #  QMimeType QMimeDatabase::mimeTypeForData(const QByteArray &data) const
    address = self.uglySide.call(
        'ritual_ZNK13QMimeDatabase15mimeTypeForDataERK10QByteArray',
        self._valueOf(data),
    )
    from . import QMimeType
    return QMimeType._cuteOwning(address)

  @overload(QIODevice)
  @overload(NoneType)
  def mimeTypeForData(self, device: Optional[QIODevice]) -> QMimeType:
    """
    Calls Qt's 'QMimeType QMimeDatabase::mimeTypeForData(QIODevice *device)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qmimedatabase.html#mimeTypeForData

    Parameters
    ----------

    device : Optional[QIODevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QMimeType
      A new cute QMimeType around the copy Qt gave back. Python owns it.
    """
    #  QMimeType QMimeDatabase::mimeTypeForData(QIODevice *device) const
    address = self.uglySide.call(
        'ritual_ZNK13QMimeDatabase15mimeTypeForDataEP9QIODevice',
        self._addressOf(device),
    )
    from . import QMimeType
    return QMimeType._cuteOwning(address)

  @overload(QUrl)
  def mimeTypeForUrl(self, url: QUrl) -> QMimeType:
    """
    Calls Qt's 'QMimeType QMimeDatabase::mimeTypeForUrl(const QUrl &url)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qmimedatabase.html#mimeTypeForUrl

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    Returns
    -------

    QMimeType
      A new cute QMimeType around the copy Qt gave back. Python owns it.
    """
    #  QMimeType QMimeDatabase::mimeTypeForUrl(const QUrl &url) const
    address = self.uglySide.call(
        'ritual_ZNK13QMimeDatabase14mimeTypeForUrlERK4QUrl',
        self._valueOf(url),
    )
    from . import QMimeType
    return QMimeType._cuteOwning(address)

  @overload(str, QIODevice)
  @overload(str, NoneType)
  def mimeTypeForFileNameAndData(
      self,
      fileName: str,
      device: Optional[QIODevice],
  ) -> QMimeType:
    """
    Calls Qt's 'QMimeType QMimeDatabase::mimeTypeForFileNameAndData(const
    QString &fileName, QIODevice *device) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmimedatabase.html#mimeTypeForFileNameAndData

    Parameters
    ----------

    fileName : str
      Passed on as it is: a QString is made of it for the call.

    device : Optional[QIODevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QMimeType
      A new cute QMimeType around the copy Qt gave back. Python owns it.
    """
    #  QMimeType QMimeDatabase::mimeTypeForFileNameAndData(const QString
    #      &fileName, QIODevice *device) const
    address = self.uglySide.call(
        'ritual_ZNK13QMimeDatabase26mimeTypeForFileNameAndDataERK7QStringP9'
        'QIODevice',
        fileName, self._addressOf(device),
    )
    from . import QMimeType
    return QMimeType._cuteOwning(address)

  @overload(str, QByteArray)
  def mimeTypeForFileNameAndData(
      self,
      fileName: str,
      data: QByteArray,
  ) -> QMimeType:
    """
    Calls Qt's 'QMimeType QMimeDatabase::mimeTypeForFileNameAndData(const
    QString &fileName, const QByteArray &data) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmimedatabase.html#mimeTypeForFileNameAndData

    Parameters
    ----------

    fileName : str
      Passed on as it is: a QString is made of it for the call.

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    Returns
    -------

    QMimeType
      A new cute QMimeType around the copy Qt gave back. Python owns it.
    """
    #  QMimeType QMimeDatabase::mimeTypeForFileNameAndData(const QString
    #      &fileName, const QByteArray &data) const
    address = self.uglySide.call(
        'ritual_ZNK13QMimeDatabase26mimeTypeForFileNameAndDataERK7QStringRK'
        '10QByteArray',
        fileName, self._valueOf(data),
    )
    from . import QMimeType
    return QMimeType._cuteOwning(address)

  @overload(str)
  def suffixForFileName(self, fileName: str) -> str:
    """
    Calls Qt's 'QString QMimeDatabase::suffixForFileName(const QString
    &fileName) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmimedatabase.html#suffixForFileName

    Parameters
    ----------

    fileName : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QMimeDatabase::suffixForFileName(const QString &fileName)
    #      const
    return self.uglySide.call(
        'ritual_ZNK13QMimeDatabase17suffixForFileNameERK7QString', fileName,
    )

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
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QMimeDatabase::QMimeDatabase()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qmimedatabase.html#QMimeDatabase
    """
    #  QMimeDatabase::QMimeDatabase()
    self._noteCreation(QMimeDatabase, lambda: Rituals.call(
        'ritual_ZN13QMimeDatabaseC1Ev',
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
