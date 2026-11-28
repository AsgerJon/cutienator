"""
QWebEngineWebAuthUxRequest binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWebEngineCore/qwebenginewebauthuxrequest.h, Qt 6.12.0. Changes made here
#  are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QObject, QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from . import QWebEngineWebAuthPinRequest
  from . import QWebEngineWebAuthUxRequestPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QWebEngineWebAuthUxRequestPrivate = WAIT['QWebEngineWebAuthUxRequestPrivate']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QWebEngineWebAuthUxRequest(QObject):
  """
  The cute side of Qt's QWebEngineWebAuthUxRequest: a plain Python object
  standing in front of one C++ QWebEngineWebAuthUxRequest.

  It is built on the cute 'QObject', as Qt's QWebEngineWebAuthUxRequest is
  built on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QWebEngineWebAuthUxRequest that has a ritual and
  that Python can call so far, 13 names in all: 'metaObject', 'tr',
  'userNames', 'relyingPartyId', 'pinRequest', 'state',
  'requestFailureReason', 'stateChanged', 'cancel', 'retry',
  'setSelectedAccount', 'setPin', 'd_func'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QWebEngineWebAuthUxRequest::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QWebEngineWebAuthUxRequest::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QWebEngineWebAuthUxRequest::~QWebEngineWebAuthUxRequest()': the
    destructor: Python never removes a C++ QWebEngineWebAuthUxRequest.
  - Qt's 'const QWebEngineWebAuthUxRequestPrivate
    *QWebEngineWebAuthUxRequest::d_func() const': takes in Python what
    'QWebEngineWebAuthUxRequestPrivate *QWebEngineWebAuthUxRequest::d_func()'
    takes.

  What has no ritual
  ------------------

  2 of the 20 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QWebEngineWebAuthUxRequest is created at the first use, not by
    'QWebEngineWebAuthUxRequest(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QWebEngineWebAuthUxRequest.
  - Qt tells when it has removed the C++ QWebEngineWebAuthUxRequest. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QWebEngineWebAuthUxRequest, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class PinEntryError(CuteNum, scoped=True):
    """
    The enum 'QWebEngineWebAuthUxRequest::PinEntryError' of Qt, with the 6
    names Qt gives in it. C++ keeps these names inside the enum, so the class
    that holds the enum does not have them.
    """

    NoError = Kee[int](0)
    InternalUvLocked = Kee[int](1)
    WrongPin = Kee[int](2)
    TooShort = Kee[int](3)
    InvalidCharacters = Kee[int](4)
    SameAsCurrentPin = Kee[int](5)

  class PinEntryReason(CuteNum, scoped=True):
    """
    The enum 'QWebEngineWebAuthUxRequest::PinEntryReason' of Qt, with the 3
    names Qt gives in it. C++ keeps these names inside the enum, so the class
    that holds the enum does not have them.
    """

    Set = Kee[int](0)
    Change = Kee[int](1)
    Challenge = Kee[int](2)

  class RequestFailureReason(CuteNum, scoped=True):
    """
    The enum 'QWebEngineWebAuthUxRequest::RequestFailureReason' of Qt, with
    the 13 names Qt gives in it. C++ keeps these names inside the enum, so
    the class that holds the enum does not have them.
    """

    Timeout = Kee[int](0)
    KeyNotRegistered = Kee[int](1)
    KeyAlreadyRegistered = Kee[int](2)
    SoftPinBlock = Kee[int](3)
    HardPinBlock = Kee[int](4)
    AuthenticatorRemovedDuringPinEntry = Kee[int](5)
    AuthenticatorMissingResidentKeys = Kee[int](6)
    AuthenticatorMissingUserVerification = Kee[int](7)
    AuthenticatorMissingLargeBlob = Kee[int](8)
    NoCommonAlgorithms = Kee[int](9)
    StorageFull = Kee[int](10)
    UserConsentDenied = Kee[int](11)
    WinUserCancelled = Kee[int](12)

  class WebAuthUxState(CuteNum, scoped=True):
    """
    The enum 'QWebEngineWebAuthUxRequest::WebAuthUxState' of Qt, with the 8
    names Qt gives in it. C++ keeps these names inside the enum, so the class
    that holds the enum does not have them.
    """

    NotStarted = Kee[int](0)
    SelectAccount = Kee[int](1)
    CollectPin = Kee[int](2)
    FinishTokenCollection = Kee[int](3)
    RequestFailed = Kee[int](4)
    Cancelled = Kee[int](5)
    Completed = Kee[int](6)
    Discovery = Kee[int](7)

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
    Calls Qt's 'QString QWebEngineWebAuthUxRequest::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebenginewebauthuxrequest.html#tr

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
    #  QString QWebEngineWebAuthUxRequest::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN26QWebEngineWebAuthUxRequest2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWebEngineWebAuthUxRequest'

  #  A C++ QWebEngineWebAuthUxRequest Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QWebEngineWebAuthUxRequest'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QWebEngineWebAuthUxRequest::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginewebauthuxrequest.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QWebEngineWebAuthUxRequest::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK26QWebEngineWebAuthUxRequest10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def userNames(self) -> QStringList:
    """
    Calls Qt's 'QStringList QWebEngineWebAuthUxRequest::userNames() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginewebauthuxrequest.html#userNames

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QWebEngineWebAuthUxRequest::userNames() const
    address = self.uglySide.call(
        'ritual_ZNK26QWebEngineWebAuthUxRequest9userNamesEv',
    )
    return QStringList._cuteOwning(address)

  def relyingPartyId(self) -> str:
    """
    Calls Qt's 'QString QWebEngineWebAuthUxRequest::relyingPartyId() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginewebauthuxrequest.html#relyingPartyId

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWebEngineWebAuthUxRequest::relyingPartyId() const
    return self.uglySide.call(
        'ritual_ZNK26QWebEngineWebAuthUxRequest14relyingPartyIdEv',
    )

  def pinRequest(self) -> QWebEngineWebAuthPinRequest:
    """
    Calls Qt's 'QWebEngineWebAuthPinRequest
    QWebEngineWebAuthUxRequest::pinRequest() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginewebauthuxrequest.html#pinRequest

    Returns
    -------

    QWebEngineWebAuthPinRequest
      A new cute QWebEngineWebAuthPinRequest around the copy Qt gave back.
      Python owns it.
    """
    #  QWebEngineWebAuthPinRequest QWebEngineWebAuthUxRequest::pinRequest()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK26QWebEngineWebAuthUxRequest10pinRequestEv',
    )
    from . import QWebEngineWebAuthPinRequest
    return QWebEngineWebAuthPinRequest._cuteOwning(address)

  def state(self) -> WebAuthUxState:
    """
    Calls Qt's 'WebAuthUxState QWebEngineWebAuthUxRequest::state() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginewebauthuxrequest.html#state

    Returns
    -------

    WebAuthUxState
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'WebAuthUxState(number)'
      gives.
    """
    #  WebAuthUxState QWebEngineWebAuthUxRequest::state() const
    return QWebEngineWebAuthUxRequest.WebAuthUxState(self.uglySide.call(
        'ritual_ZNK26QWebEngineWebAuthUxRequest5stateEv',
    ))

  def requestFailureReason(self) -> RequestFailureReason:
    """
    Calls Qt's 'RequestFailureReason
    QWebEngineWebAuthUxRequest::requestFailureReason() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginewebauthuxrequest.html

    Returns
    -------

    RequestFailureReason
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'RequestFailureReason(number)' gives.
    """
    #  RequestFailureReason
    #      QWebEngineWebAuthUxRequest::requestFailureReason() const
    return QWebEngineWebAuthUxRequest.RequestFailureReason(
        self.uglySide.call(
            'ritual_ZNK26QWebEngineWebAuthUxRequest20requestFailureReasonEv',
        ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setSelectedAccount(self, selectedAccount: str) -> None:
    """
    Calls Qt's 'void QWebEngineWebAuthUxRequest::setSelectedAccount(const
    QString &selectedAccount)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginewebauthuxrequest.html#setSelectedAccount

    Parameters
    ----------

    selectedAccount : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QWebEngineWebAuthUxRequest::setSelectedAccount(const QString
    #      &selectedAccount)
    self.uglySide.call(
        'ritual_ZN26QWebEngineWebAuthUxRequest18setSelectedAccountERK7QStri'
        'ng',
        selectedAccount,
    )

  @overload(str)
  def setPin(self, pin: str) -> None:
    """
    Calls Qt's 'void QWebEngineWebAuthUxRequest::setPin(const QString &pin)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginewebauthuxrequest.html#setPin

    Parameters
    ----------

    pin : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QWebEngineWebAuthUxRequest::setPin(const QString &pin)
    self.uglySide.call(
        'ritual_ZN26QWebEngineWebAuthUxRequest6setPinERK7QString', pin,
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

  @overload(QWebEngineWebAuthUxRequestPrivate)
  @overload(NoneType)
  def __init__(
      self,
      a0: Optional[QWebEngineWebAuthUxRequestPrivate],
  ) -> None:
    """
    Notes what was given, for Qt's
    'QWebEngineWebAuthUxRequest::QWebEngineWebAuthUxRequest(
    QWebEngineWebAuthUxRequestPrivate *a0)', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginewebauthuxrequest.html

    Parameters
    ----------

    a0 : Optional[QWebEngineWebAuthUxRequestPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QWebEngineWebAuthUxRequest::QWebEngineWebAuthUxRequest(
    #      QWebEngineWebAuthUxRequestPrivate *a0)
    self._noteCreation(QWebEngineWebAuthUxRequest, lambda: Rituals.call(
        'ritual_ZN26QWebEngineWebAuthUxRequestC1EP33QWebEngineWebAuthUxRequ'
        'estPrivate',
        self._addressOf(a0),
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

  @overload(WebAuthUxState)
  def stateChanged(self, state: WebAuthUxState) -> None:
    """
    Calls Qt's 'void
    QWebEngineWebAuthUxRequest::stateChanged(QWebEngineWebAuthUxRequest::
    WebAuthUxState state)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginewebauthuxrequest.html#stateChanged

    Parameters
    ----------

    state : WebAuthUxState
      Passed on as its number.
    """
    #  void QWebEngineWebAuthUxRequest::stateChanged(
    #      QWebEngineWebAuthUxRequest::WebAuthUxState state)
    self.uglySide.call(
        'ritual_ZN26QWebEngineWebAuthUxRequest12stateChangedENS_14WebAuthUx'
        'StateE',
        state.value,
    )

  def cancel(self) -> None:
    """
    Calls Qt's 'void QWebEngineWebAuthUxRequest::cancel()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginewebauthuxrequest.html#cancel
    """
    #  void QWebEngineWebAuthUxRequest::cancel()
    self.uglySide.call('ritual_ZN26QWebEngineWebAuthUxRequest6cancelEv')

  def retry(self) -> None:
    """
    Calls Qt's 'void QWebEngineWebAuthUxRequest::retry()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginewebauthuxrequest.html#retry
    """
    #  void QWebEngineWebAuthUxRequest::retry()
    self.uglySide.call('ritual_ZN26QWebEngineWebAuthUxRequest5retryEv')

  def d_func(self) -> Optional[QWebEngineWebAuthUxRequestPrivate]:
    """
    Calls Qt's 'QWebEngineWebAuthUxRequestPrivate
    *QWebEngineWebAuthUxRequest::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginewebauthuxrequest.html#d_func

    Returns
    -------

    Optional[QWebEngineWebAuthUxRequestPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWebEngineWebAuthUxRequestPrivate
    #      *QWebEngineWebAuthUxRequest::d_func()
    address = self.uglySide.call(
        'ritual_ZN26QWebEngineWebAuthUxRequest6d_funcEv',
    )
    from . import QWebEngineWebAuthUxRequestPrivate
    return QWebEngineWebAuthUxRequestPrivate._cuteAt(address)
