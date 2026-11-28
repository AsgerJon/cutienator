"""
QSslError binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/qsslerror.h, Qt 6.12.0. Changes made here are lost.
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

  from . import QSslCertificate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QSslCertificate = WAIT['QSslCertificate']


class QSslError(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSslError: a plain Python object standing in front of
  one C++ QSslError.

  C++ hands a QSslError around as a copy, so every C++ QSslError behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QSslError that has a ritual and that Python can call
  so far, 5 names in all: '__eq__', '__ne__', 'error', 'errorString',
  'certificate'. It can be made from Python, in 4 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QSslError::swap(QSslError &other)': takes a type Python has no
    way to hand over yet.
  - Qt's 'QSslError::~QSslError()': the destructor: Python removes its C++
    QSslError by it, and has no other use for it.
  - Qt's 'QSslError &QSslError::operator=(QSslError &&other)': assignment:
    Python binds a name and has no operator for it.
  - Qt's 'QSslError &QSslError::operator=(const QSslError &other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'QDebug operator<<(QDebug debug, SslError error)': an operator
    between other classes, written inside this one.

  What has no ritual
  ------------------

  3 of the 17 functions Qt declares: 3 not a gap.

  What to expect
  --------------

  - The C++ QSslError is created at the first use, not by 'QSslError(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSslError back gives a copy the ritual made for
    Python, in a new cute QSslError.
  - Each name of Qt's QSslError that has no cute function yet, 'swap', holds
    a function that raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QSslError, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class SslError(CuteNum):
    """
    The enum 'QSslError::SslError' of Qt, with the 38 names Qt gives in it.
    """

    NoError = Kee[int](0)
    UnableToGetIssuerCertificate = Kee[int](1)
    UnableToDecryptCertificateSignature = Kee[int](2)
    UnableToDecodeIssuerPublicKey = Kee[int](3)
    CertificateSignatureFailed = Kee[int](4)
    CertificateNotYetValid = Kee[int](5)
    CertificateExpired = Kee[int](6)
    InvalidNotBeforeField = Kee[int](7)
    InvalidNotAfterField = Kee[int](8)
    SelfSignedCertificate = Kee[int](9)
    SelfSignedCertificateInChain = Kee[int](10)
    UnableToGetLocalIssuerCertificate = Kee[int](11)
    UnableToVerifyFirstCertificate = Kee[int](12)
    CertificateRevoked = Kee[int](13)
    InvalidCaCertificate = Kee[int](14)
    PathLengthExceeded = Kee[int](15)
    InvalidPurpose = Kee[int](16)
    CertificateUntrusted = Kee[int](17)
    CertificateRejected = Kee[int](18)
    SubjectIssuerMismatch = Kee[int](19)
    AuthorityIssuerSerialNumberMismatch = Kee[int](20)
    NoPeerCertificate = Kee[int](21)
    HostNameMismatch = Kee[int](22)
    NoSslSupport = Kee[int](23)
    CertificateBlacklisted = Kee[int](24)
    CertificateStatusUnknown = Kee[int](25)
    OcspNoResponseFound = Kee[int](26)
    OcspMalformedRequest = Kee[int](27)
    OcspMalformedResponse = Kee[int](28)
    OcspInternalError = Kee[int](29)
    OcspTryLater = Kee[int](30)
    OcspSigRequred = Kee[int](31)
    OcspUnauthorized = Kee[int](32)
    OcspResponseCannotBeTrusted = Kee[int](33)
    OcspResponseCertIdUnknown = Kee[int](34)
    OcspResponseExpired = Kee[int](35)
    OcspStatusUnknown = Kee[int](36)
    UnspecifiedError = Kee[int](-1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSslError'

  #  Qt's '~QSslError()'. Naming it makes this a value class: Python owns
  #  every C++ QSslError behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN9QSslErrorD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def error(self) -> SslError:
    """
    Calls Qt's 'SslError QSslError::error() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsslerror.html#error

    Returns
    -------

    SslError
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'SslError(number)' gives.
    """
    #  SslError QSslError::error() const
    return QSslError.SslError(self.uglySide.call(
        'ritual_ZNK9QSslError5errorEv',
    ))

  def errorString(self) -> str:
    """
    Calls Qt's 'QString QSslError::errorString() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsslerror.html#errorString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSslError::errorString() const
    return self.uglySide.call('ritual_ZNK9QSslError11errorStringEv')

  def certificate(self) -> QSslCertificate:
    """
    Calls Qt's 'QSslCertificate QSslError::certificate() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsslerror.html#certificate

    Returns
    -------

    QSslCertificate
      A new cute QSslCertificate around the copy Qt gave back. Python owns
      it.
    """
    #  QSslCertificate QSslError::certificate() const
    address = self.uglySide.call('ritual_ZNK9QSslError11certificateEv')
    from . import QSslCertificate
    return QSslCertificate._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, other: QSslError) -> bool:
    """
    Calls Qt's 'bool QSslError::operator==(const QSslError &other) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsslerror.html#operator==

    Parameters
    ----------

    other : QSslError
      Passed on as a value: Qt reads the C++ QSslError, which stays Python's
      own.
    """
    #  bool QSslError::operator==(const QSslError &other) const
    return self.uglySide.call(
        'ritual_ZNK9QSslErroreqERKS_', self._valueOf(other),
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
  def __ne__(self, other: QSslError) -> bool:
    """
    Calls Qt's 'bool QSslError::operator!=(const QSslError &other) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsslerror.html#operator!=

    Parameters
    ----------

    other : QSslError
      Passed on as a value: Qt reads the C++ QSslError, which stays Python's
      own.
    """
    #  bool QSslError::operator!=(const QSslError &other) const
    return self.uglySide.call(
        'ritual_ZNK9QSslErrorneERKS_', self._valueOf(other),
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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QSslError::QSslError()', which is called
    at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qsslerror.html#QSslError
    """
    #  QSslError::QSslError()
    self._noteCreation(QSslError, lambda: Rituals.call(
        'ritual_ZN9QSslErrorC1Ev',
    ))

  @overload(SslError)
  def __init__(self, error: SslError) -> None:
    """
    Notes what was given, for Qt's 'QSslError::QSslError(SslError error)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qsslerror.html#QSslError

    Parameters
    ----------

    error : SslError
      Passed on as its number.
    """
    #  QSslError::QSslError(SslError error)
    self._noteCreation(QSslError, lambda: Rituals.call(
        'ritual_ZN9QSslErrorC1ENS_8SslErrorE', error.value,
    ))

  @overload(SslError, QSslCertificate)
  def __init__(self, error: SslError, certificate: QSslCertificate) -> None:
    """
    Notes what was given, for Qt's 'QSslError::QSslError(SslError error,
    const QSslCertificate &certificate)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qsslerror.html#QSslError

    Parameters
    ----------

    error : SslError
      Passed on as its number.

    certificate : QSslCertificate
      Passed on as a value: Qt reads the C++ QSslCertificate, which stays
      Python's own.
    """
    #  QSslError::QSslError(SslError error, const QSslCertificate
    #      &certificate)
    self._noteCreation(QSslError, lambda: Rituals.call(
        'ritual_ZN9QSslErrorC1ENS_8SslErrorERK15QSslCertificate',
        error.value, self._valueOf(certificate),
    ))

  @overload(THIS)
  def __init__(self, other: QSslError) -> None:
    """
    Notes what was given, for Qt's 'QSslError::QSslError(const QSslError
    &other)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qsslerror.html#QSslError

    Parameters
    ----------

    other : QSslError
      Passed on as a value: Qt reads the C++ QSslError, which stays Python's
      own.
    """
    #  QSslError::QSslError(const QSslError &other)
    self._noteCreation(QSslError, lambda: Rituals.call(
        'ritual_ZN9QSslErrorC1ERKS_', self._valueOf(other),
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
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QSslError::swap(QSslError &other)': takes a type Python has no
    way to hand over yet.
    """
    raise NotImplementedError(
        "'QSslError.swap' has no cute function yet. Qt's 'void "
        "QSslError::swap(QSslError &other)': takes a type Python has no way "
        "to hand over yet.")


#  Qt's 'QList<QSslError>': the list of QSslError, which 'QList[QSslError]'
#  gives. It is made here, so that there is one as soon as there can be a
#  QSslError.
QList.createKind(
    QSslError, 'value',
    make='ritual_list_make_QSslError',
    add='ritual_list_add_QSslError',
    size='ritual_list_size_QSslError',
    at='ritual_list_at_QSslError',
    drop='ritual_list_drop_QSslError',
)
