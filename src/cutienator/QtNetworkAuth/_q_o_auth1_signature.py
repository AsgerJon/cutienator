"""
QOAuth1Signature binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetworkAuth/qoauth1signature.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QUrl, QUrlQuery, QVariant
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QUrl = WAIT['QUrl']
  QUrlQuery = WAIT['QUrlQuery']
  QVariant = WAIT['QVariant']


class QOAuth1Signature(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QOAuth1Signature: a plain Python object standing in
  front of one C++ QOAuth1Signature.

  C++ hands a QOAuth1Signature around as a copy, so every C++
  QOAuth1Signature behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QOAuth1Signature that has a ritual and that Python
  can call so far, 18 names in all: 'httpRequestMethod',
  'setHttpRequestMethod', 'customMethodString', 'setCustomMethodString',
  'url', 'setUrl', 'addRequestBody', 'insert', 'keys', 'take', 'value',
  'clientSharedKey', 'setClientSharedKey', 'tokenSecret', 'setTokenSecret',
  'hmacSha1', 'rsaSha1', 'plainText'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QOAuth1Signature::QOAuth1Signature(const QUrl &url,
    HttpRequestMethod method, const QMultiMap<QString, QVariant>
    &parameters)': takes a type Python has no way to hand over yet.
  - Qt's 'QOAuth1Signature::QOAuth1Signature(const QUrl &url, const QString
    &clientSharedKey, const QString &tokenSecret, HttpRequestMethod method,
    const QMultiMap<QString, QVariant> &parameters)': takes a type Python has
    no way to hand over yet.
  - Qt's 'QOAuth1Signature::QOAuth1Signature(QOAuth1Signature &&other)':
    takes a type Python has no way to hand over yet.
  - Qt's 'QOAuth1Signature::~QOAuth1Signature()': the destructor: Python
    removes its C++ QOAuth1Signature by it, and has no other use for it.
  - Qt's 'QMultiMap<QString, QVariant> QOAuth1Signature::parameters() const':
    gives a type Python has no way to take yet.
  - Qt's 'void QOAuth1Signature::setParameters(const QMultiMap<QString,
    QVariant> &parameters)': takes a type Python has no way to hand over yet.
  - Qt's 'void QOAuth1Signature::swap(QOAuth1Signature &other)': takes a type
    Python has no way to hand over yet.
  - Qt's 'QOAuth1Signature &QOAuth1Signature::operator=(const
    QOAuth1Signature &other)': assignment: Python binds a name and has no
    operator for it.
  - Qt's 'QOAuth1Signature &QOAuth1Signature::operator=(QOAuth1Signature
    &&other)': assignment: Python binds a name and has no operator for it.

  What to expect
  --------------

  - The C++ QOAuth1Signature is created at the first use, not by
    'QOAuth1Signature(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QOAuth1Signature back gives a copy the ritual made
    for Python, in a new cute QOAuth1Signature.
  - Each name of Qt's QOAuth1Signature that has no cute function yet,
    'parameters', 'setParameters', 'swap', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QOAuth1Signature, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class HttpRequestMethod(CuteNum, scoped=True):
    """
    The enum 'QOAuth1Signature::HttpRequestMethod' of Qt, with the 7 names Qt
    gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    Head = Kee[int](1)
    Get = Kee[int](2)
    Put = Kee[int](3)
    Post = Kee[int](4)
    Delete = Kee[int](5)
    Custom = Kee[int](6)
    Unknown = Kee[int](0)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOAuth1Signature'

  #  Qt's '~QOAuth1Signature()'. Naming it makes this a value class: Python
  #  owns every C++ QOAuth1Signature behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN16QOAuth1SignatureD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def httpRequestMethod(self) -> HttpRequestMethod:
    """
    Calls Qt's 'HttpRequestMethod QOAuth1Signature::httpRequestMethod()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qoauth1signature.html#httpRequestMethod

    Returns
    -------

    HttpRequestMethod
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'HttpRequestMethod(number)' gives.
    """
    #  HttpRequestMethod QOAuth1Signature::httpRequestMethod() const
    return QOAuth1Signature.HttpRequestMethod(self.uglySide.call(
        'ritual_ZNK16QOAuth1Signature17httpRequestMethodEv',
    ))

  def customMethodString(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QOAuth1Signature::customMethodString() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qoauth1signature.html#customMethodString

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QOAuth1Signature::customMethodString() const
    address = self.uglySide.call(
        'ritual_ZNK16QOAuth1Signature18customMethodStringEv',
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def url(self) -> QUrl:
    """
    Calls Qt's 'QUrl QOAuth1Signature::url() const'.

    Qt's own words: https://doc.qt.io/qt-6/qoauth1signature.html#url

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QOAuth1Signature::url() const
    address = self.uglySide.call('ritual_ZNK16QOAuth1Signature3urlEv')
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def keys(self) -> QStringList:
    """
    Calls Qt's 'QList<QString> QOAuth1Signature::keys() const'.

    Qt's own words: https://doc.qt.io/qt-6/qoauth1signature.html#keys

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QString> QOAuth1Signature::keys() const
    address = self.uglySide.call('ritual_ZNK16QOAuth1Signature4keysEv')
    return QStringList._cuteOwning(address)

  @overload(str)
  @overload(str, QVariant)
  def value(
      self,
      key: str,
      defaultValue: Optional[QVariant] = None,
  ) -> QVariant:
    """
    Calls Qt's 'QVariant QOAuth1Signature::value(const QString &key, const
    QVariant &defaultValue) const'.

    Qt's own words: https://doc.qt.io/qt-6/qoauth1signature.html#value

    Parameters
    ----------

    key : str
      Passed on as it is: a QString is made of it for the call.

    defaultValue : Optional[QVariant]
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own. May be left out, as in Qt: a new 'QVariant()' is then passed on.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QOAuth1Signature::value(const QString &key, const QVariant
    #      &defaultValue) const
    if defaultValue is None:
      from ..QtCore import QVariant
      defaultValue = QVariant()
    address = self.uglySide.call(
        'ritual_ZNK16QOAuth1Signature5valueERK7QStringRK8QVariant',
        key, self._valueOf(defaultValue),
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def clientSharedKey(self) -> str:
    """
    Calls Qt's 'QString QOAuth1Signature::clientSharedKey() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qoauth1signature.html#clientSharedKey

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QOAuth1Signature::clientSharedKey() const
    return self.uglySide.call(
        'ritual_ZNK16QOAuth1Signature15clientSharedKeyEv',
    )

  def tokenSecret(self) -> str:
    """
    Calls Qt's 'QString QOAuth1Signature::tokenSecret() const'.

    Qt's own words: https://doc.qt.io/qt-6/qoauth1signature.html#tokenSecret

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QOAuth1Signature::tokenSecret() const
    return self.uglySide.call('ritual_ZNK16QOAuth1Signature11tokenSecretEv')

  def hmacSha1(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QOAuth1Signature::hmacSha1() const'.

    Qt's own words: https://doc.qt.io/qt-6/qoauth1signature.html#hmacSha1

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QOAuth1Signature::hmacSha1() const
    address = self.uglySide.call('ritual_ZNK16QOAuth1Signature8hmacSha1Ev')
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def rsaSha1(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QOAuth1Signature::rsaSha1() const'.

    Qt's own words: https://doc.qt.io/qt-6/qoauth1signature.html#rsaSha1

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QOAuth1Signature::rsaSha1() const
    address = self.uglySide.call('ritual_ZNK16QOAuth1Signature7rsaSha1Ev')
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  @overload()
  def plainText(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QOAuth1Signature::plainText() const'.

    Qt's own words: https://doc.qt.io/qt-6/qoauth1signature.html#plainText

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QOAuth1Signature::plainText() const
    address = self.uglySide.call('ritual_ZNK16QOAuth1Signature9plainTextEv')
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  @staticmethod
  @overload(str, str)
  def plainText(clientSharedSecret: str, tokenSecret: str) -> QByteArray:
    """
    Calls Qt's 'QByteArray QOAuth1Signature::plainText(const QString
    &clientSharedSecret, const QString &tokenSecret)'.

    Qt's own words: https://doc.qt.io/qt-6/qoauth1signature.html#plainText

    Parameters
    ----------

    clientSharedSecret : str
      Passed on as it is: a QString is made of it for the call.

    tokenSecret : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QOAuth1Signature::plainText(const QString
    #      &clientSharedSecret, const QString &tokenSecret)
    address = Rituals.call(
        'ritual_ZN16QOAuth1Signature9plainTextERK7QStringS2_',
        clientSharedSecret, tokenSecret,
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(HttpRequestMethod)
  def setHttpRequestMethod(self, method: HttpRequestMethod) -> None:
    """
    Calls Qt's 'void QOAuth1Signature::setHttpRequestMethod(HttpRequestMethod
    method)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qoauth1signature.html#setHttpRequestMethod

    Parameters
    ----------

    method : HttpRequestMethod
      Passed on as its number.
    """
    #  void QOAuth1Signature::setHttpRequestMethod(HttpRequestMethod method)
    self.uglySide.call(
        'ritual_ZN16QOAuth1Signature20setHttpRequestMethodENS_17HttpRequest'
        'MethodE',
        method.value,
    )

  @overload(QByteArray)
  def setCustomMethodString(self, verb: QByteArray) -> None:
    """
    Calls Qt's 'void QOAuth1Signature::setCustomMethodString(const QByteArray
    &verb)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qoauth1signature.html#setCustomMethodString

    Parameters
    ----------

    verb : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QOAuth1Signature::setCustomMethodString(const QByteArray &verb)
    self.uglySide.call(
        'ritual_ZN16QOAuth1Signature21setCustomMethodStringERK10QByteArray',
        self._valueOf(verb),
    )

  @overload(QUrl)
  def setUrl(self, url: QUrl) -> None:
    """
    Calls Qt's 'void QOAuth1Signature::setUrl(const QUrl &url)'.

    Qt's own words: https://doc.qt.io/qt-6/qoauth1signature.html#setUrl

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QOAuth1Signature::setUrl(const QUrl &url)
    self.uglySide.call(
        'ritual_ZN16QOAuth1Signature6setUrlERK4QUrl', self._valueOf(url),
    )

  @overload(str)
  def setClientSharedKey(self, secret: str) -> None:
    """
    Calls Qt's 'void QOAuth1Signature::setClientSharedKey(const QString
    &secret)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qoauth1signature.html#setClientSharedKey

    Parameters
    ----------

    secret : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QOAuth1Signature::setClientSharedKey(const QString &secret)
    self.uglySide.call(
        'ritual_ZN16QOAuth1Signature18setClientSharedKeyERK7QString', secret,
    )

  @overload(str)
  def setTokenSecret(self, secret: str) -> None:
    """
    Calls Qt's 'void QOAuth1Signature::setTokenSecret(const QString
    &secret)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qoauth1signature.html#setTokenSecret

    Parameters
    ----------

    secret : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QOAuth1Signature::setTokenSecret(const QString &secret)
    self.uglySide.call(
        'ritual_ZN16QOAuth1Signature14setTokenSecretERK7QString', secret,
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

  @overload(THIS)
  def __init__(self, other: QOAuth1Signature) -> None:
    """
    Notes what was given, for Qt's 'QOAuth1Signature::QOAuth1Signature(const
    QOAuth1Signature &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qoauth1signature.html#QOAuth1Signature

    Parameters
    ----------

    other : QOAuth1Signature
      Passed on as a value: Qt reads the C++ QOAuth1Signature, which stays
      Python's own.
    """
    #  QOAuth1Signature::QOAuth1Signature(const QOAuth1Signature &other)
    self._noteCreation(QOAuth1Signature, lambda: Rituals.call(
        'ritual_ZN16QOAuth1SignatureC1ERKS_', self._valueOf(other),
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

  @overload(QUrlQuery)
  def addRequestBody(self, body: QUrlQuery) -> None:
    """
    Calls Qt's 'void QOAuth1Signature::addRequestBody(const QUrlQuery
    &body)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qoauth1signature.html#addRequestBody

    Parameters
    ----------

    body : QUrlQuery
      Passed on as a value: Qt reads the C++ QUrlQuery, which stays Python's
      own.
    """
    #  void QOAuth1Signature::addRequestBody(const QUrlQuery &body)
    self.uglySide.call(
        'ritual_ZN16QOAuth1Signature14addRequestBodyERK9QUrlQuery',
        self._valueOf(body),
    )

  @overload(str, QVariant)
  def insert(self, key: str, value: QVariant) -> None:
    """
    Calls Qt's 'void QOAuth1Signature::insert(const QString &key, const
    QVariant &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qoauth1signature.html#insert

    Parameters
    ----------

    key : str
      Passed on as it is: a QString is made of it for the call.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QOAuth1Signature::insert(const QString &key, const QVariant
    #      &value)
    self.uglySide.call(
        'ritual_ZN16QOAuth1Signature6insertERK7QStringRK8QVariant',
        key, self._valueOf(value),
    )

  @overload(str)
  def take(self, key: str) -> QVariant:
    """
    Calls Qt's 'QVariant QOAuth1Signature::take(const QString &key)'.

    Qt's own words: https://doc.qt.io/qt-6/qoauth1signature.html#take

    Parameters
    ----------

    key : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QOAuth1Signature::take(const QString &key)
    address = self.uglySide.call(
        'ritual_ZN16QOAuth1Signature4takeERK7QString', key,
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @staticmethod
  def parameters(*__, **_) -> Never:
    """
    Qt's 'QMultiMap<QString, QVariant> QOAuth1Signature::parameters() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QOAuth1Signature.parameters' has no cute function yet. Qt's "
        "'QMultiMap<QString, QVariant> QOAuth1Signature::parameters() "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def setParameters(*__, **_) -> Never:
    """
    Qt's 'void QOAuth1Signature::setParameters(const QMultiMap<QString,
    QVariant> &parameters)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QOAuth1Signature.setParameters' has no cute function yet. Qt's "
        "'void QOAuth1Signature::setParameters(const QMultiMap<QString, "
        "QVariant> &parameters)': takes a type Python has no way to hand "
        "over yet.")

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QOAuth1Signature::swap(QOAuth1Signature &other)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QOAuth1Signature.swap' has no cute function yet. Qt's 'void "
        "QOAuth1Signature::swap(QOAuth1Signature &other)': takes a type "
        "Python has no way to hand over yet.")
