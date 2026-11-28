"""
QWebEngineHttpRequest binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWebEngineCore/qwebenginehttprequest.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QByteArray, QUrl
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QUrl = WAIT['QUrl']


class QWebEngineHttpRequest(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QWebEngineHttpRequest: a plain Python object standing
  in front of one C++ QWebEngineHttpRequest.

  C++ hands a QWebEngineHttpRequest around as a copy, so every C++
  QWebEngineHttpRequest behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QWebEngineHttpRequest that has a ritual and that
  Python can call so far, 13 names in all: '__eq__', '__ne__', 'method',
  'setMethod', 'url', 'setUrl', 'postData', 'setPostData', 'hasHeader',
  'headers', 'header', 'setHeader', 'unsetHeader'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QWebEngineHttpRequest::QWebEngineHttpRequest(const QUrl &url, const
    QWebEngineHttpRequest::Method &method)': takes a type Python has no way
    to hand over yet.
  - Qt's 'QWebEngineHttpRequest::~QWebEngineHttpRequest()': the destructor:
    Python removes its C++ QWebEngineHttpRequest by it, and has no other use
    for it.
  - Qt's 'QWebEngineHttpRequest
    &QWebEngineHttpRequest::operator=(QWebEngineHttpRequest &&other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'QWebEngineHttpRequest &QWebEngineHttpRequest::operator=(const
    QWebEngineHttpRequest &other)': assignment: Python binds a name and has
    no operator for it.
  - Qt's 'QWebEngineHttpRequest QWebEngineHttpRequest::postRequest(const QUrl
    &url, const QMap<QString, QString> &postData)': takes a type Python has
    no way to hand over yet.
  - Qt's 'void QWebEngineHttpRequest::swap(QWebEngineHttpRequest &other)':
    takes a type Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ QWebEngineHttpRequest is created at the first use, not by
    'QWebEngineHttpRequest(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QWebEngineHttpRequest back gives a copy the ritual
    made for Python, in a new cute QWebEngineHttpRequest.
  - Each name of Qt's QWebEngineHttpRequest that has no cute function yet,
    'postRequest', 'swap', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QWebEngineHttpRequest, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class Method(CuteNum):
    """
    The enum 'QWebEngineHttpRequest::Method' of Qt, with the 2 names Qt gives
    in it.
    """

    Get = Kee[int](0)
    Post = Kee[int](1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWebEngineHttpRequest'

  #  Qt's '~QWebEngineHttpRequest()'. Naming it makes this a value class:
  #  Python owns every C++ QWebEngineHttpRequest behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN21QWebEngineHttpRequestD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def method(self) -> Method:
    """
    Calls Qt's 'Method QWebEngineHttpRequest::method() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebenginehttprequest.html#method

    Returns
    -------

    Method
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Method(number)' gives.
    """
    #  Method QWebEngineHttpRequest::method() const
    return QWebEngineHttpRequest.Method(self.uglySide.call(
        'ritual_ZNK21QWebEngineHttpRequest6methodEv',
    ))

  def url(self) -> QUrl:
    """
    Calls Qt's 'QUrl QWebEngineHttpRequest::url() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebenginehttprequest.html#url

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QWebEngineHttpRequest::url() const
    address = self.uglySide.call('ritual_ZNK21QWebEngineHttpRequest3urlEv')
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def postData(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QWebEngineHttpRequest::postData() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginehttprequest.html#postData

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QWebEngineHttpRequest::postData() const
    address = self.uglySide.call(
        'ritual_ZNK21QWebEngineHttpRequest8postDataEv',
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  @overload(QByteArray)
  def hasHeader(self, headerName: QByteArray) -> bool:
    """
    Calls Qt's 'bool QWebEngineHttpRequest::hasHeader(const QByteArray
    &headerName) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginehttprequest.html#hasHeader

    Parameters
    ----------

    headerName : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  bool QWebEngineHttpRequest::hasHeader(const QByteArray &headerName)
    #      const
    return self.uglySide.call(
        'ritual_ZNK21QWebEngineHttpRequest9hasHeaderERK10QByteArray',
        self._valueOf(headerName),
    )

  def headers(self) -> QList[QByteArray]:
    """
    Calls Qt's 'QList<QByteArray> QWebEngineHttpRequest::headers() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebenginehttprequest.html#headers

    Returns
    -------

    QList[QByteArray]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QByteArray> QWebEngineHttpRequest::headers() const
    address = self.uglySide.call(
        'ritual_ZNK21QWebEngineHttpRequest7headersEv',
    )
    from ..QtCore import QByteArray
    return QList[QByteArray]._cuteOwning(address)

  @overload(QByteArray)
  def header(self, headerName: QByteArray) -> QByteArray:
    """
    Calls Qt's 'QByteArray QWebEngineHttpRequest::header(const QByteArray
    &headerName) const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebenginehttprequest.html#header

    Parameters
    ----------

    headerName : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QWebEngineHttpRequest::header(const QByteArray &headerName)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK21QWebEngineHttpRequest6headerERK10QByteArray',
        self._valueOf(headerName),
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Method)
  def setMethod(self, method: Method) -> None:
    """
    Calls Qt's 'void
    QWebEngineHttpRequest::setMethod(QWebEngineHttpRequest::Method method)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginehttprequest.html#setMethod

    Parameters
    ----------

    method : Method
      Passed on as its number.
    """
    #  void QWebEngineHttpRequest::setMethod(QWebEngineHttpRequest::Method
    #      method)
    self.uglySide.call(
        'ritual_ZN21QWebEngineHttpRequest9setMethodENS_6MethodE',
        method.value,
    )

  @overload(QUrl)
  def setUrl(self, url: QUrl) -> None:
    """
    Calls Qt's 'void QWebEngineHttpRequest::setUrl(const QUrl &url)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebenginehttprequest.html#setUrl

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QWebEngineHttpRequest::setUrl(const QUrl &url)
    self.uglySide.call(
        'ritual_ZN21QWebEngineHttpRequest6setUrlERK4QUrl',
        self._valueOf(url),
    )

  @overload(QByteArray)
  def setPostData(self, postData: QByteArray) -> None:
    """
    Calls Qt's 'void QWebEngineHttpRequest::setPostData(const QByteArray
    &postData)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginehttprequest.html#setPostData

    Parameters
    ----------

    postData : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QWebEngineHttpRequest::setPostData(const QByteArray &postData)
    self.uglySide.call(
        'ritual_ZN21QWebEngineHttpRequest11setPostDataERK10QByteArray',
        self._valueOf(postData),
    )

  @overload(QByteArray, QByteArray)
  def setHeader(self, headerName: QByteArray, value: QByteArray) -> None:
    """
    Calls Qt's 'void QWebEngineHttpRequest::setHeader(const QByteArray
    &headerName, const QByteArray &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginehttprequest.html#setHeader

    Parameters
    ----------

    headerName : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    value : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QWebEngineHttpRequest::setHeader(const QByteArray &headerName,
    #      const QByteArray &value)
    self.uglySide.call(
        'ritual_ZN21QWebEngineHttpRequest9setHeaderERK10QByteArrayS2_',
        self._valueOf(headerName), self._valueOf(value),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, other: QWebEngineHttpRequest) -> bool:
    """
    Calls Qt's 'bool QWebEngineHttpRequest::operator==(const
    QWebEngineHttpRequest &other) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginehttprequest.html#operator==

    Parameters
    ----------

    other : QWebEngineHttpRequest
      Passed on as a value: Qt reads the C++ QWebEngineHttpRequest, which
      stays Python's own.
    """
    #  bool QWebEngineHttpRequest::operator==(const QWebEngineHttpRequest
    #      &other) const
    return self.uglySide.call(
        'ritual_ZNK21QWebEngineHttpRequesteqERKS_', self._valueOf(other),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __ne__(self, other: QWebEngineHttpRequest) -> bool:
    """
    Calls Qt's 'bool QWebEngineHttpRequest::operator!=(const
    QWebEngineHttpRequest &other) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginehttprequest.html#operator!=

    Parameters
    ----------

    other : QWebEngineHttpRequest
      Passed on as a value: Qt reads the C++ QWebEngineHttpRequest, which
      stays Python's own.
    """
    #  bool QWebEngineHttpRequest::operator!=(const QWebEngineHttpRequest
    #      &other) const
    return self.uglySide.call(
        'ritual_ZNK21QWebEngineHttpRequestneERKS_', self._valueOf(other),
    )

  @overload.fallback
  def __ne__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __init__(self, other: QWebEngineHttpRequest) -> None:
    """
    Notes what was given, for Qt's
    'QWebEngineHttpRequest::QWebEngineHttpRequest(const QWebEngineHttpRequest
    &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginehttprequest.html#QWebEngineHttpRequest

    Parameters
    ----------

    other : QWebEngineHttpRequest
      Passed on as a value: Qt reads the C++ QWebEngineHttpRequest, which
      stays Python's own.
    """
    #  QWebEngineHttpRequest::QWebEngineHttpRequest(const
    #      QWebEngineHttpRequest &other)
    self._noteCreation(QWebEngineHttpRequest, lambda: Rituals.call(
        'ritual_ZN21QWebEngineHttpRequestC1ERKS_', self._valueOf(other),
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

  @overload(QByteArray)
  def unsetHeader(self, headerName: QByteArray) -> None:
    """
    Calls Qt's 'void QWebEngineHttpRequest::unsetHeader(const QByteArray
    &headerName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginehttprequest.html#unsetHeader

    Parameters
    ----------

    headerName : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QWebEngineHttpRequest::unsetHeader(const QByteArray &headerName)
    self.uglySide.call(
        'ritual_ZN21QWebEngineHttpRequest11unsetHeaderERK10QByteArray',
        self._valueOf(headerName),
    )

  @staticmethod
  def postRequest(*__, **_) -> Never:
    """
    Qt's 'QWebEngineHttpRequest QWebEngineHttpRequest::postRequest(const QUrl
    &url, const QMap<QString, QString> &postData)': takes a type Python has
    no way to hand over yet.
    """
    raise NotImplementedError(
        "'QWebEngineHttpRequest.postRequest' has no cute function yet. Qt's "
        "'QWebEngineHttpRequest QWebEngineHttpRequest::postRequest(const "
        "QUrl &url, const QMap<QString, QString> &postData)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QWebEngineHttpRequest::swap(QWebEngineHttpRequest &other)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QWebEngineHttpRequest.swap' has no cute function yet. Qt's 'void "
        "QWebEngineHttpRequest::swap(QWebEngineHttpRequest &other)': takes "
        "a type Python has no way to hand over yet.")
