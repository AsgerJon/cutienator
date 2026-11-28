"""
QWebEngineUrlRequestJob binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWebEngineCore/qwebengineurlrequestjob.h, Qt 6.12.0. Changes made here
#  are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QIODevice, QMetaObject, QUrl
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QIODevice = WAIT['QIODevice']
  QUrl = WAIT['QUrl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QWebEngineUrlRequestJob(QObject):
  """
  The cute side of Qt's QWebEngineUrlRequestJob: a plain Python object
  standing in front of one C++ QWebEngineUrlRequestJob.

  It is built on the cute 'QObject', as Qt's QWebEngineUrlRequestJob is built
  on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QWebEngineUrlRequestJob that has a ritual and that
  Python can call so far, 9 names in all: 'metaObject', 'tr', 'requestUrl',
  'requestMethod', 'initiator', 'requestBody', 'reply', 'fail', 'redirect'.
  None can be made from Python: one comes out of a function of another class
  that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QWebEngineUrlRequestJob::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QWebEngineUrlRequestJob::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QWebEngineUrlRequestJob::~QWebEngineUrlRequestJob()': the
    destructor: Python never removes a C++ QWebEngineUrlRequestJob.
  - Qt's 'QMap<QByteArray, QByteArray>
    QWebEngineUrlRequestJob::requestHeaders() const': gives a type Python has
    no way to take yet.
  - Qt's 'void QWebEngineUrlRequestJob::setAdditionalResponseHeaders(const
    QMultiMap<QByteArray, QByteArray> &additionalResponseHeaders) const':
    takes a type Python has no way to hand over yet.
  - Qt's 'QWebEngineUrlRequestJob::QWebEngineUrlRequestJob(QtWebEngineCore::
    URLRequestCustomJobDelegate *a0)': names
    'QtWebEngineCore::URLRequestCustomJobDelegate', which has no cute class
    yet.

  What has no ritual
  ------------------

  2 of the 17 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QWebEngineUrlRequestJob is created at the first use, not by
    'QWebEngineUrlRequestJob(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QWebEngineUrlRequestJob.
  - Qt tells when it has removed the C++ QWebEngineUrlRequestJob. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QWebEngineUrlRequestJob that has no cute function yet,
    '__init__', 'requestHeaders', 'setAdditionalResponseHeaders', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QWebEngineUrlRequestJob, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class Error(CuteNum):
    """
    The enum 'QWebEngineUrlRequestJob::Error' of Qt, with the 6 names Qt
    gives in it.
    """

    NoError = Kee[int](0)
    UrlNotFound = Kee[int](1)
    UrlInvalid = Kee[int](2)
    RequestAborted = Kee[int](3)
    RequestDenied = Kee[int](4)
    RequestFailed = Kee[int](5)

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
    Calls Qt's 'QString QWebEngineUrlRequestJob::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebengineurlrequestjob.html#tr

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
    #  QString QWebEngineUrlRequestJob::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN23QWebEngineUrlRequestJob2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWebEngineUrlRequestJob'

  #  A C++ QWebEngineUrlRequestJob Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QWebEngineUrlRequestJob'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QWebEngineUrlRequestJob::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineurlrequestjob.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QWebEngineUrlRequestJob::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK23QWebEngineUrlRequestJob10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def requestUrl(self) -> QUrl:
    """
    Calls Qt's 'QUrl QWebEngineUrlRequestJob::requestUrl() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineurlrequestjob.html#requestUrl

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QWebEngineUrlRequestJob::requestUrl() const
    address = self.uglySide.call(
        'ritual_ZNK23QWebEngineUrlRequestJob10requestUrlEv',
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def requestMethod(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QWebEngineUrlRequestJob::requestMethod() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineurlrequestjob.html#requestMethod

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QWebEngineUrlRequestJob::requestMethod() const
    address = self.uglySide.call(
        'ritual_ZNK23QWebEngineUrlRequestJob13requestMethodEv',
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def initiator(self) -> QUrl:
    """
    Calls Qt's 'QUrl QWebEngineUrlRequestJob::initiator() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineurlrequestjob.html#initiator

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QWebEngineUrlRequestJob::initiator() const
    address = self.uglySide.call(
        'ritual_ZNK23QWebEngineUrlRequestJob9initiatorEv',
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def requestBody(self) -> Optional[QIODevice]:
    """
    Calls Qt's 'QIODevice *QWebEngineUrlRequestJob::requestBody() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineurlrequestjob.html#requestBody

    Returns
    -------

    Optional[QIODevice]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QIODevice *QWebEngineUrlRequestJob::requestBody() const
    address = self.uglySide.call(
        'ritual_ZNK23QWebEngineUrlRequestJob11requestBodyEv',
    )
    from ..QtCore import QIODevice
    return QIODevice._cuteAt(address)

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
    Qt's 'QWebEngineUrlRequestJob::QWebEngineUrlRequestJob(QtWebEngineCore::
    URLRequestCustomJobDelegate *a0)': names
    'QtWebEngineCore::URLRequestCustomJobDelegate', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QWebEngineUrlRequestJob.__init__' has no cute function yet. Qt's "
        "'QWebEngineUrlRequestJob::QWebEngineUrlRequestJob(QtWebEngineCore::"
        "URLRequestCustomJobDelegate *a0)': names "
        "'QtWebEngineCore::URLRequestCustomJobDelegate', which has no cute "
        "class yet.")

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

  @overload(QByteArray, QIODevice)
  @overload(QByteArray, NoneType)
  def reply(
      self,
      contentType: QByteArray,
      device: Optional[QIODevice],
  ) -> None:
    """
    Calls Qt's 'void QWebEngineUrlRequestJob::reply(const QByteArray
    &contentType, QIODevice *device)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebengineurlrequestjob.html#reply

    Parameters
    ----------

    contentType : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    device : Optional[QIODevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWebEngineUrlRequestJob::reply(const QByteArray &contentType,
    #      QIODevice *device)
    self.uglySide.call(
        'ritual_ZN23QWebEngineUrlRequestJob5replyERK10QByteArrayP9QIODevice',
        self._valueOf(contentType), self._addressOf(device),
    )

  @overload(Error)
  def fail(self, error: Error) -> None:
    """
    Calls Qt's 'void QWebEngineUrlRequestJob::fail(Error error)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebengineurlrequestjob.html#fail

    Parameters
    ----------

    error : Error
      Passed on as its number.
    """
    #  void QWebEngineUrlRequestJob::fail(Error error)
    self.uglySide.call(
        'ritual_ZN23QWebEngineUrlRequestJob4failENS_5ErrorE', error.value,
    )

  @overload(QUrl)
  def redirect(self, url: QUrl) -> None:
    """
    Calls Qt's 'void QWebEngineUrlRequestJob::redirect(const QUrl &url)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineurlrequestjob.html#redirect

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QWebEngineUrlRequestJob::redirect(const QUrl &url)
    self.uglySide.call(
        'ritual_ZN23QWebEngineUrlRequestJob8redirectERK4QUrl',
        self._valueOf(url),
    )

  @staticmethod
  def requestHeaders(*__, **_) -> Never:
    """
    Qt's 'QMap<QByteArray, QByteArray>
    QWebEngineUrlRequestJob::requestHeaders() const': gives a type Python has
    no way to take yet.
    """
    raise NotImplementedError(
        "'QWebEngineUrlRequestJob.requestHeaders' has no cute function yet. "
        "Qt's 'QMap<QByteArray, QByteArray> "
        "QWebEngineUrlRequestJob::requestHeaders() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def setAdditionalResponseHeaders(*__, **_) -> Never:
    """
    Qt's 'void QWebEngineUrlRequestJob::setAdditionalResponseHeaders(const
    QMultiMap<QByteArray, QByteArray> &additionalResponseHeaders) const':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QWebEngineUrlRequestJob.setAdditionalResponseHeaders' has no cute "
        "function yet. Qt's 'void "
        "QWebEngineUrlRequestJob::setAdditionalResponseHeaders(const "
        "QMultiMap<QByteArray, QByteArray> &additionalResponseHeaders) "
        "const': takes a type Python has no way to hand over yet.")
