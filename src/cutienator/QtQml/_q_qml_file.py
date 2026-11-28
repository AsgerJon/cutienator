"""
QQmlFile binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/qqmlfile.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QByteArray, QObject, QUrl
  from . import QQmlEngine
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QObject = WAIT['QObject']
  QQmlEngine = WAIT['QQmlEngine']
  QUrl = WAIT['QUrl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlFile(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlFile: a plain Python object standing in front of
  one C++ QQmlFile.

  What exists
  -----------

  Every function of Qt's QQmlFile that has a ritual and that Python can call
  so far, 17 names in all: 'isNull', 'isReady', 'isError', 'isLoading',
  'url', 'status', 'error', 'size', 'data', 'dataByteArray', 'load', 'clear',
  'connectFinished', 'connectDownloadProgress', 'isSynchronous',
  'isLocalFile', 'urlToLocalFileOrQrc'. It can be made from Python, in 3
  ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQmlFile::~QQmlFile()': the destructor: Python never removes a C++
    QQmlFile.

  What has no ritual
  ------------------

  2 of the 30 functions Qt declares: 2 forbidden.

  What to expect
  --------------

  - The C++ QQmlFile is created at the first use, not by 'QQmlFile(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlFile.
  """

  #  The enums Qt writes inside QQmlFile, each a class in here as in C++, and
  #  the names Qt has for the combinations of its flags enums.

  class Status(CuteNum):
    """The enum 'QQmlFile::Status' of Qt, with the 4 names Qt gives in it."""

    Null = Kee[int](0)
    Ready = Kee[int](1)
    Error = Kee[int](2)
    Loading = Kee[int](3)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  def isSynchronous(url: str) -> bool:
    """
    Calls Qt's 'bool QQmlFile::isSynchronous(const QString &url)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlfile.html#isSynchronous

    Parameters
    ----------

    url : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QQmlFile::isSynchronous(const QString &url)
    return Rituals.call('ritual_ZN8QQmlFile13isSynchronousERK7QString', url)

  @staticmethod
  @overload(QUrl)
  def isSynchronous(url: QUrl) -> bool:
    """
    Calls Qt's 'bool QQmlFile::isSynchronous(const QUrl &url)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlfile.html#isSynchronous

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  bool QQmlFile::isSynchronous(const QUrl &url)
    return Rituals.call(
        'ritual_ZN8QQmlFile13isSynchronousERK4QUrl', CuteMixin._valueOf(url),
    )

  @staticmethod
  @overload(str)
  def isLocalFile(url: str) -> bool:
    """
    Calls Qt's 'bool QQmlFile::isLocalFile(const QString &url)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlfile.html#isLocalFile

    Parameters
    ----------

    url : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QQmlFile::isLocalFile(const QString &url)
    return Rituals.call('ritual_ZN8QQmlFile11isLocalFileERK7QString', url)

  @staticmethod
  @overload(QUrl)
  def isLocalFile(url: QUrl) -> bool:
    """
    Calls Qt's 'bool QQmlFile::isLocalFile(const QUrl &url)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlfile.html#isLocalFile

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  bool QQmlFile::isLocalFile(const QUrl &url)
    return Rituals.call(
        'ritual_ZN8QQmlFile11isLocalFileERK4QUrl', CuteMixin._valueOf(url),
    )

  @staticmethod
  @overload(str)
  def urlToLocalFileOrQrc(a0: str) -> str:
    """
    Calls Qt's 'QString QQmlFile::urlToLocalFileOrQrc(const QString &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlfile.html#urlToLocalFileOrQrc

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlFile::urlToLocalFileOrQrc(const QString &a0)
    return Rituals.call(
        'ritual_ZN8QQmlFile19urlToLocalFileOrQrcERK7QString', a0,
    )

  @staticmethod
  @overload(QUrl)
  def urlToLocalFileOrQrc(a0: QUrl) -> str:
    """
    Calls Qt's 'QString QQmlFile::urlToLocalFileOrQrc(const QUrl &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlfile.html#urlToLocalFileOrQrc

    Parameters
    ----------

    a0 : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlFile::urlToLocalFileOrQrc(const QUrl &a0)
    return Rituals.call(
        'ritual_ZN8QQmlFile19urlToLocalFileOrQrcERK4QUrl',
        CuteMixin._valueOf(a0),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlFile'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isNull(self) -> bool:
    """
    Calls Qt's 'bool QQmlFile::isNull() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlfile.html#isNull
    """
    #  bool QQmlFile::isNull() const
    return self.uglySide.call('ritual_ZNK8QQmlFile6isNullEv')

  def isReady(self) -> bool:
    """
    Calls Qt's 'bool QQmlFile::isReady() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlfile.html#isReady
    """
    #  bool QQmlFile::isReady() const
    return self.uglySide.call('ritual_ZNK8QQmlFile7isReadyEv')

  def isError(self) -> bool:
    """
    Calls Qt's 'bool QQmlFile::isError() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlfile.html#isError
    """
    #  bool QQmlFile::isError() const
    return self.uglySide.call('ritual_ZNK8QQmlFile7isErrorEv')

  def isLoading(self) -> bool:
    """
    Calls Qt's 'bool QQmlFile::isLoading() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlfile.html#isLoading
    """
    #  bool QQmlFile::isLoading() const
    return self.uglySide.call('ritual_ZNK8QQmlFile9isLoadingEv')

  def url(self) -> QUrl:
    """
    Calls Qt's 'QUrl QQmlFile::url() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlfile.html#url

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QQmlFile::url() const
    address = self.uglySide.call('ritual_ZNK8QQmlFile3urlEv')
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def status(self) -> Status:
    """
    Calls Qt's 'Status QQmlFile::status() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlfile.html#status

    Returns
    -------

    Status
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Status(number)' gives.
    """
    #  Status QQmlFile::status() const
    return QQmlFile.Status(self.uglySide.call(
        'ritual_ZNK8QQmlFile6statusEv',
    ))

  def error(self) -> str:
    """
    Calls Qt's 'QString QQmlFile::error() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlfile.html#error

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlFile::error() const
    return self.uglySide.call('ritual_ZNK8QQmlFile5errorEv')

  def size(self) -> int:
    """
    Calls Qt's 'qint64 QQmlFile::size() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlfile.html#size
    """
    #  qint64 QQmlFile::size() const
    return self.uglySide.call('ritual_ZNK8QQmlFile4sizeEv')

  def data(self) -> Optional[str]:
    """
    Calls Qt's 'const char *QQmlFile::data() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlfile.html#data

    Returns
    -------

    Optional[str]
      The text Qt gave back. None when Qt gave back no text.
    """
    #  const char *QQmlFile::data() const
    chars = self.uglySide.call('ritual_ZNK8QQmlFile4dataEv')
    return None if chars is None else chars.decode()

  def dataByteArray(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QQmlFile::dataByteArray() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlfile.html#dataByteArray

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QQmlFile::dataByteArray() const
    address = self.uglySide.call('ritual_ZNK8QQmlFile13dataByteArrayEv')
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

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
    Notes what was given, for Qt's 'QQmlFile::QQmlFile()', which is called at
    the first use.

    Qt's own words: https://doc.qt.io/qt-6/qqmlfile.html#QQmlFile
    """
    #  QQmlFile::QQmlFile()
    self._noteCreation(QQmlFile, lambda: Rituals.call(
        'ritual_ZN8QQmlFileC1Ev',
    ))

  @overload(QQmlEngine, QUrl)
  @overload(NoneType, QUrl)
  def __init__(self, engine: Optional[QQmlEngine], url: QUrl) -> None:
    """
    Notes what was given, for Qt's 'QQmlFile::QQmlFile(QQmlEngine *engine,
    const QUrl &url)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qqmlfile.html#QQmlFile

    Parameters
    ----------

    engine : Optional[QQmlEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  QQmlFile::QQmlFile(QQmlEngine *engine, const QUrl &url)
    self._noteCreation(QQmlFile, lambda: Rituals.call(
        'ritual_ZN8QQmlFileC1EP10QQmlEngineRK4QUrl',
        self._addressOf(engine), self._valueOf(url),
    ))

  @overload(QQmlEngine, str)
  @overload(NoneType, str)
  def __init__(self, engine: Optional[QQmlEngine], url: str) -> None:
    """
    Notes what was given, for Qt's 'QQmlFile::QQmlFile(QQmlEngine *engine,
    const QString &url)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qqmlfile.html#QQmlFile

    Parameters
    ----------

    engine : Optional[QQmlEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    url : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  QQmlFile::QQmlFile(QQmlEngine *engine, const QString &url)
    self._noteCreation(QQmlFile, lambda: Rituals.call(
        'ritual_ZN8QQmlFileC1EP10QQmlEngineRK7QString',
        self._addressOf(engine), url,
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

  @overload(QQmlEngine, QUrl)
  @overload(NoneType, QUrl)
  def load(self, a0: Optional[QQmlEngine], a1: QUrl) -> None:
    """
    Calls Qt's 'void QQmlFile::load(QQmlEngine *a0, const QUrl &a1)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlfile.html#load

    Parameters
    ----------

    a0 : Optional[QQmlEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QQmlFile::load(QQmlEngine *a0, const QUrl &a1)
    self.uglySide.call(
        'ritual_ZN8QQmlFile4loadEP10QQmlEngineRK4QUrl',
        self._addressOf(a0), self._valueOf(a1),
    )

  @overload(QQmlEngine, str)
  @overload(NoneType, str)
  def load(self, a0: Optional[QQmlEngine], a1: str) -> None:
    """
    Calls Qt's 'void QQmlFile::load(QQmlEngine *a0, const QString &a1)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlfile.html#load

    Parameters
    ----------

    a0 : Optional[QQmlEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQmlFile::load(QQmlEngine *a0, const QString &a1)
    self.uglySide.call(
        'ritual_ZN8QQmlFile4loadEP10QQmlEngineRK7QString',
        self._addressOf(a0), a1,
    )

  @overload()
  def clear(self) -> None:
    """
    Calls Qt's 'void QQmlFile::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlfile.html#clear
    """
    #  void QQmlFile::clear()
    self.uglySide.call('ritual_ZN8QQmlFile5clearEv')

  @overload(QObject)
  @overload(NoneType)
  def clear(self, object: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QQmlFile::clear(QObject *object)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlfile.html#clear

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlFile::clear(QObject *object)
    self.uglySide.call(
        'ritual_ZN8QQmlFile5clearEP7QObject',
        self._addressOf(object, 'QObject'),
    )

  @overload(QObject, str)
  @overload(QObject, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  def connectFinished(
      self,
      a0: Optional[QObject],
      a1: Optional[str],
  ) -> bool:
    """
    Calls Qt's 'bool QQmlFile::connectFinished(QObject *a0, const char *a1)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlfile.html#connectFinished

    Parameters
    ----------

    a0 : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.
    """
    #  bool QQmlFile::connectFinished(QObject *a0, const char *a1)
    return self.uglySide.call(
        'ritual_ZN8QQmlFile15connectFinishedEP7QObjectPKc',
        self._addressOf(a0, 'QObject'), self._bytesOf(a1),
    )

  @overload(QObject, int)
  @overload(NoneType, int)
  def connectFinished(self, a0: Optional[QObject], a1: int) -> bool:
    """
    Calls Qt's 'bool QQmlFile::connectFinished(QObject *a0, int a1)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlfile.html#connectFinished

    Parameters
    ----------

    a0 : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : int
      Passed on as it is.
    """
    #  bool QQmlFile::connectFinished(QObject *a0, int a1)
    return self.uglySide.call(
        'ritual_ZN8QQmlFile15connectFinishedEP7QObjecti',
        self._addressOf(a0, 'QObject'), a1,
    )

  @overload(QObject, str)
  @overload(QObject, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  def connectDownloadProgress(
      self,
      a0: Optional[QObject],
      a1: Optional[str],
  ) -> bool:
    """
    Calls Qt's 'bool QQmlFile::connectDownloadProgress(QObject *a0, const
    char *a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlfile.html#connectDownloadProgress

    Parameters
    ----------

    a0 : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.
    """
    #  bool QQmlFile::connectDownloadProgress(QObject *a0, const char *a1)
    return self.uglySide.call(
        'ritual_ZN8QQmlFile23connectDownloadProgressEP7QObjectPKc',
        self._addressOf(a0, 'QObject'), self._bytesOf(a1),
    )

  @overload(QObject, int)
  @overload(NoneType, int)
  def connectDownloadProgress(self, a0: Optional[QObject], a1: int) -> bool:
    """
    Calls Qt's 'bool QQmlFile::connectDownloadProgress(QObject *a0, int a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlfile.html#connectDownloadProgress

    Parameters
    ----------

    a0 : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : int
      Passed on as it is.
    """
    #  bool QQmlFile::connectDownloadProgress(QObject *a0, int a1)
    return self.uglySide.call(
        'ritual_ZN8QQmlFile23connectDownloadProgressEP7QObjecti',
        self._addressOf(a0, 'QObject'), a1,
    )
