"""
QAuthenticatorPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/6.12.0/QtNetwork/private/qauthenticator_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QAuthenticatorPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QByteArrayView
  from . import QAuthenticator, QHttpHeaders
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAuthenticator = WAIT['QAuthenticator']
  QByteArrayView = WAIT['QByteArrayView']
  QHttpHeaders = WAIT['QHttpHeaders']


class QAuthenticatorPrivate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QAuthenticatorPrivate: a plain Python object standing
  in front of one C++ QAuthenticatorPrivate.

  What exists
  -----------

  Every function of Qt's QAuthenticatorPrivate that has a ritual and that
  Python can call so far, 6 names in all: 'calculateResponse', 'getPrivate',
  'digestMd5Response', 'parseHttpResponse', 'updateCredentials',
  'isMethodSupported'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QAuthenticatorPrivate
    &QAuthenticatorPrivate::operator=(QAuthenticatorPrivate &&other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'void QAuthenticatorPrivate::swap(QAuthenticatorPrivate &other)':
    takes a type Python has no way to hand over yet.
  - Qt's 'QAuthenticatorPrivate::~QAuthenticatorPrivate()': the destructor:
    Python never removes a C++ QAuthenticatorPrivate.
  - Qt's 'QAuthenticatorPrivate
    *QAuthenticatorPrivate::getPrivate(QAuthenticator &auth)': takes a type
    Python has no way to hand over yet.
  - Qt's 'QHash<QByteArray, QByteArray>
    QAuthenticatorPrivate::parseDigestAuthenticationChallenge(QByteArrayView
    challenge)': gives a type Python has no way to take yet.

  What to expect
  --------------

  - The C++ QAuthenticatorPrivate is created at the first use, not by
    'QAuthenticatorPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAuthenticatorPrivate.
  - Each name of Qt's QAuthenticatorPrivate that has no cute function yet,
    'parseDigestAuthenticationChallenge', 'swap', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QAuthenticatorPrivate, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class Method(CuteNum):
    """
    The enum 'QAuthenticatorPrivate::Method' of Qt, with the 5 names Qt gives
    in it.
    """

    NULL = Kee[int](0)
    Basic = Kee[int](1)
    Negotiate = Kee[int](2)
    Ntlm = Kee[int](3)
    DigestMd5 = Kee[int](4)

  class Phase(CuteNum):
    """
    The enum 'QAuthenticatorPrivate::Phase' of Qt, with the 5 names Qt gives
    in it.
    """

    Start = Kee[int](0)
    Phase1 = Kee[int](1)
    Phase2 = Kee[int](2)
    Done = Kee[int](3)
    Invalid = Kee[int](4)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QAuthenticator)
  def getPrivate(auth: QAuthenticator) -> Optional[QAuthenticatorPrivate]:
    """
    Calls Qt's 'const QAuthenticatorPrivate
    *QAuthenticatorPrivate::getPrivate(const QAuthenticator &auth)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qauthenticatorprivate.html#getPrivate

    Parameters
    ----------

    auth : QAuthenticator
      Passed on as a value: Qt reads the C++ QAuthenticator, which stays
      Python's own.

    Returns
    -------

    Optional[QAuthenticatorPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QAuthenticatorPrivate *QAuthenticatorPrivate::getPrivate(const
    #      QAuthenticator &auth)
    address = Rituals.call(
        'ritual_ZN21QAuthenticatorPrivate10getPrivateERK14QAuthenticator',
        CuteMixin._valueOf(auth),
    )
    return QAuthenticatorPrivate._cuteAt(address)

  @staticmethod
  @overload(QByteArrayView)
  def isMethodSupported(method: QByteArrayView) -> bool:
    """
    Calls Qt's 'bool QAuthenticatorPrivate::isMethodSupported(QByteArrayView
    method)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qauthenticatorprivate.html#isMethodSupported

    Parameters
    ----------

    method : QByteArrayView
      Passed on as a value: Qt reads the C++ QByteArrayView, which stays
      Python's own.
    """
    #  bool QAuthenticatorPrivate::isMethodSupported(QByteArrayView method)
    return Rituals.call(
        'ritual_ZN21QAuthenticatorPrivate17isMethodSupportedE14QByteArrayVi'
        'ew',
        CuteMixin._valueOf(method),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAuthenticatorPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
    Notes what was given, for Qt's
    'QAuthenticatorPrivate::QAuthenticatorPrivate()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qauthenticatorprivate.html#QAuthenticatorPrivate
    """
    #  QAuthenticatorPrivate::QAuthenticatorPrivate()
    self._noteCreation(QAuthenticatorPrivate, lambda: Rituals.call(
        'ritual_ZN21QAuthenticatorPrivateC1Ev',
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

  @overload(QByteArrayView, QByteArrayView, str)
  def calculateResponse(
      self,
      method: QByteArrayView,
      path: QByteArrayView,
      host: str,
  ) -> QByteArray:
    """
    Calls Qt's 'QByteArray
    QAuthenticatorPrivate::calculateResponse(QByteArrayView method,
    QByteArrayView path, QStringView host)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qauthenticatorprivate.html#calculateResponse

    Parameters
    ----------

    method : QByteArrayView
      Passed on as a value: Qt reads the C++ QByteArrayView, which stays
      Python's own.

    path : QByteArrayView
      Passed on as a value: Qt reads the C++ QByteArrayView, which stays
      Python's own.

    host : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QAuthenticatorPrivate::calculateResponse(QByteArrayView
    #      method, QByteArrayView path, QStringView host)
    address = self.uglySide.call(
        'ritual_ZN21QAuthenticatorPrivate17calculateResponseE14QByteArrayVi'
        'ewS0_11QStringView',
        self._valueOf(method), self._valueOf(path), host,
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  @overload(QByteArrayView, QByteArrayView, QByteArrayView)
  def digestMd5Response(
      self,
      challenge: QByteArrayView,
      method: QByteArrayView,
      path: QByteArrayView,
  ) -> QByteArray:
    """
    Calls Qt's 'QByteArray
    QAuthenticatorPrivate::digestMd5Response(QByteArrayView challenge,
    QByteArrayView method, QByteArrayView path)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qauthenticatorprivate.html#digestMd5Response

    Parameters
    ----------

    challenge : QByteArrayView
      Passed on as a value: Qt reads the C++ QByteArrayView, which stays
      Python's own.

    method : QByteArrayView
      Passed on as a value: Qt reads the C++ QByteArrayView, which stays
      Python's own.

    path : QByteArrayView
      Passed on as a value: Qt reads the C++ QByteArrayView, which stays
      Python's own.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QAuthenticatorPrivate::digestMd5Response(QByteArrayView
    #      challenge, QByteArrayView method, QByteArrayView path)
    address = self.uglySide.call(
        'ritual_ZN21QAuthenticatorPrivate17digestMd5ResponseE14QByteArrayVi'
        'ewS0_S0_',
        self._valueOf(challenge), self._valueOf(method), self._valueOf(path),
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  @overload(QHttpHeaders, bool, str)
  def parseHttpResponse(
      self,
      headers: QHttpHeaders,
      isProxy: bool,
      host: str,
  ) -> None:
    """
    Calls Qt's 'void QAuthenticatorPrivate::parseHttpResponse(const
    QHttpHeaders &headers, bool isProxy, QStringView host)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qauthenticatorprivate.html#parseHttpResponse

    Parameters
    ----------

    headers : QHttpHeaders
      Passed on as a value: Qt reads the C++ QHttpHeaders, which stays
      Python's own.

    isProxy : bool
      Passed on as it is.

    host : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QAuthenticatorPrivate::parseHttpResponse(const QHttpHeaders
    #      &headers, bool isProxy, QStringView host)
    self.uglySide.call(
        'ritual_ZN21QAuthenticatorPrivate17parseHttpResponseERK12QHttpHeade'
        'rsb11QStringView',
        self._valueOf(headers), isProxy, host,
    )

  def updateCredentials(self) -> None:
    """
    Calls Qt's 'void QAuthenticatorPrivate::updateCredentials()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qauthenticatorprivate.html#updateCredentials
    """
    #  void QAuthenticatorPrivate::updateCredentials()
    self.uglySide.call(
        'ritual_ZN21QAuthenticatorPrivate17updateCredentialsEv',
    )

  @staticmethod
  def parseDigestAuthenticationChallenge(*__, **_) -> Never:
    """
    Qt's 'QHash<QByteArray, QByteArray>
    QAuthenticatorPrivate::parseDigestAuthenticationChallenge(QByteArrayView
    challenge)': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QAuthenticatorPrivate.parseDigestAuthenticationChallenge' has no "
        "cute function yet. Qt's 'QHash<QByteArray, QByteArray> "
        "QAuthenticatorPrivate::parseDigestAuthenticationChallenge(QByteArra"
        "yView challenge)': gives a type Python has no way to take yet.")

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QAuthenticatorPrivate::swap(QAuthenticatorPrivate &other)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QAuthenticatorPrivate.swap' has no cute function yet. Qt's 'void "
        "QAuthenticatorPrivate::swap(QAuthenticatorPrivate &other)': takes "
        "a type Python has no way to hand over yet.")
