"""
QWebEngineCertificateError binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWebEngineCore/qwebenginecertificateerror.h, Qt 6.12.0. Changes made here
#  are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute
from ..occult import Rituals
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QUrl
  from ..QtNetwork import QSslCertificate


class QWebEngineCertificateError(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QWebEngineCertificateError: a plain Python object
  standing in front of one C++ QWebEngineCertificateError.

  C++ hands a QWebEngineCertificateError around as a copy, so every C++
  QWebEngineCertificateError behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QWebEngineCertificateError that has a ritual and
  that Python can call so far, 9 names in all: 'type', 'url',
  'isOverridable', 'description', 'isMainFrame', 'defer',
  'rejectCertificate', 'acceptCertificate', 'certificateChain'. It can be
  made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QWebEngineCertificateError
    &QWebEngineCertificateError::operator=(const QWebEngineCertificateError
    &other)': assignment: Python binds a name and has no operator for it.
  - Qt's 'QWebEngineCertificateError::~QWebEngineCertificateError()': the
    destructor: Python removes its C++ QWebEngineCertificateError by it, and
    has no other use for it.
  - Qt's 'QWebEngineCertificateError::QWebEngineCertificateError(const
    QSharedPointer<QtWebEngineCore::CertificateErrorController>
    &controller)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  3 of the 17 functions Qt declares: 3 not a gap.

  What to expect
  --------------

  - The C++ QWebEngineCertificateError is created at the first use, not by
    'QWebEngineCertificateError(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QWebEngineCertificateError back gives a copy the
    ritual made for Python, in a new cute QWebEngineCertificateError.
  """

  #  The enums Qt writes inside QWebEngineCertificateError, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class Type(CuteNum):
    """
    The enum 'QWebEngineCertificateError::Type' of Qt, with the 19 names Qt
    gives in it.
    """

    Ok = Kee[int](0)
    SslPinnedKeyNotInCertificateChain = Kee[int](-150)
    CertificateCommonNameInvalid = Kee[int](-200)
    CertificateDateInvalid = Kee[int](-201)
    CertificateAuthorityInvalid = Kee[int](-202)
    CertificateContainsErrors = Kee[int](-203)
    CertificateNoRevocationMechanism = Kee[int](-204)
    CertificateUnableToCheckRevocation = Kee[int](-205)
    CertificateRevoked = Kee[int](-206)
    CertificateInvalid = Kee[int](-207)
    CertificateWeakSignatureAlgorithm = Kee[int](-208)
    CertificateNonUniqueName = Kee[int](-210)
    CertificateWeakKey = Kee[int](-211)
    CertificateNameConstraintViolation = Kee[int](-212)
    CertificateValidityTooLong = Kee[int](-213)
    CertificateTransparencyRequired = Kee[int](-214)
    CertificateSymantecLegacy = Kee[int](-215)
    CertificateKnownInterceptionBlocked = Kee[int](-217)
    SslObsoleteVersion = Kee[int](-218)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWebEngineCertificateError'

  #  Qt's '~QWebEngineCertificateError()'. Naming it makes this a value
  #  class: Python owns every C++ QWebEngineCertificateError behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN26QWebEngineCertificateErrorD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def type(self) -> Type:
    """
    Calls Qt's 'Type QWebEngineCertificateError::type() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginecertificateerror.html#type

    Returns
    -------

    Type
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Type(number)' gives.
    """
    #  Type QWebEngineCertificateError::type() const
    return QWebEngineCertificateError.Type(self.uglySide.call(
        'ritual_ZNK26QWebEngineCertificateError4typeEv',
    ))

  def url(self) -> QUrl:
    """
    Calls Qt's 'QUrl QWebEngineCertificateError::url() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginecertificateerror.html#url

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QWebEngineCertificateError::url() const
    address = self.uglySide.call(
        'ritual_ZNK26QWebEngineCertificateError3urlEv',
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def isOverridable(self) -> bool:
    """
    Calls Qt's 'bool QWebEngineCertificateError::isOverridable() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginecertificateerror.html#isOverridable
    """
    #  bool QWebEngineCertificateError::isOverridable() const
    return self.uglySide.call(
        'ritual_ZNK26QWebEngineCertificateError13isOverridableEv',
    )

  def description(self) -> str:
    """
    Calls Qt's 'QString QWebEngineCertificateError::description() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginecertificateerror.html#description

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWebEngineCertificateError::description() const
    return self.uglySide.call(
        'ritual_ZNK26QWebEngineCertificateError11descriptionEv',
    )

  def isMainFrame(self) -> bool:
    """
    Calls Qt's 'bool QWebEngineCertificateError::isMainFrame() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginecertificateerror.html#isMainFrame
    """
    #  bool QWebEngineCertificateError::isMainFrame() const
    return self.uglySide.call(
        'ritual_ZNK26QWebEngineCertificateError11isMainFrameEv',
    )

  def certificateChain(self) -> QList[QSslCertificate]:
    """
    Calls Qt's 'QList<QSslCertificate>
    QWebEngineCertificateError::certificateChain() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginecertificateerror.html#certificateChain

    Returns
    -------

    QList[QSslCertificate]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QSslCertificate> QWebEngineCertificateError::certificateChain()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK26QWebEngineCertificateError16certificateChainEv',
    )
    from ..QtNetwork import QSslCertificate
    return QList[QSslCertificate]._cuteOwning(address)

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
    'QWebEngineCertificateError::QWebEngineCertificateError()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginecertificateerror.html
    """
    #  QWebEngineCertificateError::QWebEngineCertificateError()
    self._noteCreation(QWebEngineCertificateError, lambda: Rituals.call(
        'ritual_ZN26QWebEngineCertificateErrorC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QWebEngineCertificateError) -> None:
    """
    Notes what was given, for Qt's
    'QWebEngineCertificateError::QWebEngineCertificateError(const
    QWebEngineCertificateError &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginecertificateerror.html

    Parameters
    ----------

    other : QWebEngineCertificateError
      Passed on as a value: Qt reads the C++ QWebEngineCertificateError,
      which stays Python's own.
    """
    #  QWebEngineCertificateError::QWebEngineCertificateError(const
    #      QWebEngineCertificateError &other)
    self._noteCreation(QWebEngineCertificateError, lambda: Rituals.call(
        'ritual_ZN26QWebEngineCertificateErrorC1ERKS_', self._valueOf(other),
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

  def defer(self) -> None:
    """
    Calls Qt's 'void QWebEngineCertificateError::defer()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginecertificateerror.html#defer
    """
    #  void QWebEngineCertificateError::defer()
    self.uglySide.call('ritual_ZN26QWebEngineCertificateError5deferEv')

  def rejectCertificate(self) -> None:
    """
    Calls Qt's 'void QWebEngineCertificateError::rejectCertificate()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginecertificateerror.html#rejectCertificate
    """
    #  void QWebEngineCertificateError::rejectCertificate()
    self.uglySide.call(
        'ritual_ZN26QWebEngineCertificateError17rejectCertificateEv',
    )

  def acceptCertificate(self) -> None:
    """
    Calls Qt's 'void QWebEngineCertificateError::acceptCertificate()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginecertificateerror.html#acceptCertificate
    """
    #  void QWebEngineCertificateError::acceptCertificate()
    self.uglySide.call(
        'ritual_ZN26QWebEngineCertificateError17acceptCertificateEv',
    )
