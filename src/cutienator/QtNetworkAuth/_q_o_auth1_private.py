"""
QOAuth1Private binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetworkAuth/6.12.0/QtNetworkAuth/private/qoauth1_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QOAuth1Private to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..QtNetwork import QNetworkReply
from . import QAbstractOAuthPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray
  from . import QOAuth1, QOAuth1Signature
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QOAuth1Signature = WAIT['QOAuth1Signature']


class QOAuth1Private(QAbstractOAuthPrivate):
  """
  The cute side of Qt's QOAuth1Private: a plain Python object standing in
  front of one C++ QOAuth1Private.

  It is built on the cute 'QAbstractOAuthPrivate', as Qt's QOAuth1Private is
  built on Qt's QAbstractOAuthPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QOAuth1Private that has a ritual and that Python can
  call so far, 4 names in all: 'q_func', 'signatureMethodString',
  'formatSignature', '_q_onTokenRequestError'. None can be made from Python:
  one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QOAuth1 *QOAuth1Private::q_func() const': takes in Python
    what 'QOAuth1 *QOAuth1Private::q_func()' takes.
  - Qt's 'QOAuth1Private::QOAuth1Private(const std::pair<QString, QString>
    &clientCredentials, QNetworkAccessManager *networkAccessManager)': takes
    a type Python has no way to hand over yet.
  - Qt's 'QByteArray QOAuth1Private::generateSignature(const
    QMultiMap<QString, QVariant> &parameters, const QUrl &url,
    QNetworkAccessManager::Operation operation) const': takes a type Python
    has no way to hand over yet.
  - Qt's 'QByteArray QOAuth1Private::generateSignature(const
    QMultiMap<QString, QVariant> &parameters, const QUrl &url, const
    QByteArray &verb) const': takes a type Python has no way to hand over
    yet.

  What has no ritual
  ------------------

  5 of the 13 functions Qt declares: 5 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QOAuth1Private is created at the first use, not by
    'QOAuth1Private(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QOAuth1Private.
  - Each name of Qt's QOAuth1Private that has no cute function yet,
    '__init__', '_q_tokensReceived', 'appendCommonHeaders',
    'appendSignature', 'createOAuthBaseParams', 'generateSignature',
    'requestToken', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  #  The classes Qt writes inside QOAuth1Private, each a class in here as in
  #  C++.

  class OAuth1KeyString(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QOAuth1Private::OAuth1KeyString: a plain Python
    object standing in front of one C++ QOAuth1Private::OAuth1KeyString.

    C++ hands a QOAuth1Private::OAuth1KeyString around as a copy, so every
    C++ QOAuth1Private::OAuth1KeyString behind a cute one is Python's own: it
    is removed, by the ritual named in '__delete_ritual__', when the cute
    object goes.

    What exists
    -----------

    No function of Qt's QOAuth1Private::OAuth1KeyString yet. None can be made
    from Python: one comes out of a function of another class that gives one
    back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QOAuth1Private::OAuth1KeyString::~OAuth1KeyString()': the
      destructor: Python removes its C++ QOAuth1Private::OAuth1KeyString by
      it, and has no other use for it.

    What to expect
    --------------

    - The C++ QOAuth1Private::OAuth1KeyString is created at the first use,
      not by 'QOAuth1Private::OAuth1KeyString(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QOAuth1Private::OAuth1KeyString back gives a copy
      the ritual made for Python, in a new cute
      QOAuth1Private::OAuth1KeyString.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QOAuth1Private::OAuth1KeyString'

    #  Qt's '~QOAuth1Private::OAuth1KeyString()'. Naming it makes this a
    #  value class: Python owns every C++ QOAuth1Private::OAuth1KeyString
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN14QOAuth1Private15OAuth1KeyStringD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
  __qt_class__ = 'QOAuth1Private'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def signatureMethodString(self) -> str:
    """
    Calls Qt's 'QString QOAuth1Private::signatureMethodString() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qoauth1private.html#signatureMethodString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QOAuth1Private::signatureMethodString() const
    return self.uglySide.call(
        'ritual_ZNK14QOAuth1Private21signatureMethodStringEv',
    )

  @overload(QOAuth1Signature)
  def formatSignature(self, signature: QOAuth1Signature) -> QByteArray:
    """
    Calls Qt's 'QByteArray QOAuth1Private::formatSignature(const
    QOAuth1Signature &signature) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qoauth1private.html#formatSignature

    Parameters
    ----------

    signature : QOAuth1Signature
      Passed on as a value: Qt reads the C++ QOAuth1Signature, which stays
      Python's own.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QOAuth1Private::formatSignature(const QOAuth1Signature
    #      &signature) const
    address = self.uglySide.call(
        'ritual_ZNK14QOAuth1Private15formatSignatureERK16QOAuth1Signature',
        self._valueOf(signature),
    )
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QOAuth1Private::QOAuth1Private(const std::pair<QString, QString>
    &clientCredentials, QNetworkAccessManager *networkAccessManager)': takes
    a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QOAuth1Private.__init__' has no cute function yet. Qt's "
        "'QOAuth1Private::QOAuth1Private(const std::pair<QString, QString> "
        "&clientCredentials, QNetworkAccessManager *networkAccessManager)': "
        "takes a type Python has no way to hand over yet.")

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

  def q_func(self) -> Optional[QOAuth1]:
    """
    Calls Qt's 'QOAuth1 *QOAuth1Private::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qoauth1private.html#q_func

    Returns
    -------

    Optional[QOAuth1]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QOAuth1 *QOAuth1Private::q_func()
    address = self.uglySide.call('ritual_ZN14QOAuth1Private6q_funcEv')
    from . import QOAuth1
    return QOAuth1._cuteAt(address)

  @overload(QNetworkReply.NetworkError)
  def _q_onTokenRequestError(
      self,
      error: QNetworkReply.NetworkError,
  ) -> None:
    """
    Calls Qt's 'void
    QOAuth1Private::_q_onTokenRequestError(QNetworkReply::NetworkError
    error)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qoauth1private.html#_q_onTokenRequestError

    Parameters
    ----------

    error : QNetworkReply.NetworkError
      Passed on as its number.
    """
    #  void
    #      QOAuth1Private::_q_onTokenRequestError(QNetworkReply::NetworkError
    #      error)
    self.uglySide.call(
        'ritual_ZN14QOAuth1Private22_q_onTokenRequestErrorEN13QNetworkReply'
        '12NetworkErrorE',
        error.value,
    )

  @staticmethod
  def _q_tokensReceived(*__, **_) -> Never:
    """
    Qt's 'void QOAuth1Private::_q_tokensReceived(const QVariantMap &tokens)':
    Qt's library has no name for it, and its code in Qt's source does not
    compile apart from its file: use of undeclared identifier 'OAuth1'; did
    you mean 'QOAuth1'?.
    """
    raise NotImplementedError(
        "'QOAuth1Private._q_tokensReceived' has no cute function yet. Qt's "
        "'void QOAuth1Private::_q_tokensReceived(const QVariantMap "
        "&tokens)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'OAuth1'; did you mean 'QOAuth1'?.")

  @staticmethod
  def appendCommonHeaders(*__, **_) -> Never:
    """
    Qt's 'void QOAuth1Private::appendCommonHeaders(QVariantMap *headers)':
    Qt's library has no name for it, and its code in Qt's source does not
    compile apart from its file: use of undeclared identifier 'OAuth1'; did
    you mean 'QOAuth1'?.
    """
    raise NotImplementedError(
        "'QOAuth1Private.appendCommonHeaders' has no cute function yet. "
        "Qt's 'void QOAuth1Private::appendCommonHeaders(QVariantMap "
        "*headers)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'OAuth1'; did you mean 'QOAuth1'?.")

  @staticmethod
  def appendSignature(*__, **_) -> Never:
    """
    Qt's 'void QOAuth1Private::appendSignature(QAbstractOAuth::Stage stage,
    QVariantMap *headers, const QUrl &url, QNetworkAccessManager::Operation
    operation, const QMultiMap<QString, QVariant> parameters)': Qt's library
    has no name for it, and its code in Qt's source does not compile apart
    from its file: use of undeclared identifier 'OAuth1'; did you mean
    'QOAuth1'?.
    """
    raise NotImplementedError(
        "'QOAuth1Private.appendSignature' has no cute function yet. Qt's "
        "'void QOAuth1Private::appendSignature(QAbstractOAuth::Stage stage, "
        "QVariantMap *headers, const QUrl &url, "
        "QNetworkAccessManager::Operation operation, const "
        "QMultiMap<QString, QVariant> parameters)': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: use of undeclared identifier 'OAuth1'; did you mean "
        "'QOAuth1'?.")

  @staticmethod
  def createOAuthBaseParams(*__, **_) -> Never:
    """
    Qt's 'QVariantMap QOAuth1Private::createOAuthBaseParams() const': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier 'OAuth1'; did you mean
    'QOAuth1'?.
    """
    raise NotImplementedError(
        "'QOAuth1Private.createOAuthBaseParams' has no cute function yet. "
        "Qt's 'QVariantMap QOAuth1Private::createOAuthBaseParams() const': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: use of undeclared identifier "
        "'OAuth1'; did you mean 'QOAuth1'?.")

  @staticmethod
  def generateSignature(*__, **_) -> Never:
    """
    - Qt's 'QByteArray QOAuth1Private::generateSignature(const
      QMultiMap<QString, QVariant> &parameters, const QUrl &url,
      QNetworkAccessManager::Operation operation) const': takes a type Python
      has no way to hand over yet.
    - Qt's 'QByteArray QOAuth1Private::generateSignature(const
      QMultiMap<QString, QVariant> &parameters, const QUrl &url, const
      QByteArray &verb) const': takes a type Python has no way to hand over
      yet.
    """
    raise NotImplementedError(
        "'QOAuth1Private.generateSignature' has no cute function yet. Qt's "
        "'QByteArray QOAuth1Private::generateSignature(const "
        "QMultiMap<QString, QVariant> &parameters, const QUrl &url, "
        "QNetworkAccessManager::Operation operation) const': takes a type "
        "Python has no way to hand over yet. Qt's 'QByteArray "
        "QOAuth1Private::generateSignature(const QMultiMap<QString, "
        "QVariant> &parameters, const QUrl &url, const QByteArray &verb) "
        "const': takes a type Python has no way to hand over yet.")

  @staticmethod
  def requestToken(*__, **_) -> Never:
    """
    Qt's 'QNetworkReply
    *QOAuth1Private::requestToken(QNetworkAccessManager::Operation operation,
    const QUrl &url, const std::pair<QString, QString> &token, const
    QVariantMap &additionalParameters)': Qt's library has no name for it, and
    its code in Qt's source does not compile apart from its file: use of
    undeclared identifier 'OAuth1'; did you mean 'QOAuth1'?.
    """
    raise NotImplementedError(
        "'QOAuth1Private.requestToken' has no cute function yet. Qt's "
        "'QNetworkReply "
        "*QOAuth1Private::requestToken(QNetworkAccessManager::Operation "
        "operation, const QUrl &url, const std::pair<QString, QString> "
        "&token, const QVariantMap &additionalParameters)': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: use of undeclared identifier 'OAuth1'; did "
        "you mean 'QOAuth1'?.")
