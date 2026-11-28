"""
QOpcUaX509CertificateSigningRequest binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtOpcUa/qopcuax509certificatesigningrequest.h, Qt 6.12.0. Changes made
#  here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QOpcUaX509DistinguishedName, QOpcUaX509Extension
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QOpcUaX509DistinguishedName = WAIT['QOpcUaX509DistinguishedName']
  QOpcUaX509Extension = WAIT['QOpcUaX509Extension']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QOpcUaX509CertificateSigningRequest(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QOpcUaX509CertificateSigningRequest: a plain Python
  object standing in front of one C++ QOpcUaX509CertificateSigningRequest.

  C++ hands a QOpcUaX509CertificateSigningRequest around as a copy, so every
  C++ QOpcUaX509CertificateSigningRequest behind a cute one is Python's own:
  it is removed, by the ritual named in '__delete_ritual__', when the cute
  object goes.

  What exists
  -----------

  Every function of Qt's QOpcUaX509CertificateSigningRequest that has a
  ritual and that Python can call so far, 7 names in all: 'setMessageDigest',
  'messageDigest', 'setEncoding', 'encoding', 'setSubject', 'subject',
  'addExtension'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QOpcUaX509CertificateSigningRequestPrivate
    *QOpcUaX509CertificateSigningRequest::d_func()': gives
    'QOpcUaX509CertificateSigningRequestPrivate', which has no cute class
    yet.
  - Qt's 'const QOpcUaX509CertificateSigningRequestPrivate
    *QOpcUaX509CertificateSigningRequest::d_func() const': gives
    'QOpcUaX509CertificateSigningRequestPrivate', which has no cute class
    yet.
  - Qt's 'QOpcUaX509CertificateSigningRequest::
    ~QOpcUaX509CertificateSigningRequest()': the destructor: Python removes
    its C++ QOpcUaX509CertificateSigningRequest by it, and has no other use
    for it.
  - Qt's 'QByteArray QOpcUaX509CertificateSigningRequest::createRequest(const
    QOpcUaKeyPair &privateKey)': takes a type Python has no way to hand over
    yet.
  - Qt's 'QByteArray
    QOpcUaX509CertificateSigningRequest::createSelfSignedCertificate(const
    QOpcUaKeyPair &privateKey, int validityInDays)': takes a type Python has
    no way to hand over yet.

  What to expect
  --------------

  - The C++ QOpcUaX509CertificateSigningRequest is created at the first use,
    not by 'QOpcUaX509CertificateSigningRequest(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QOpcUaX509CertificateSigningRequest back gives a copy
    the ritual made for Python, in a new cute
    QOpcUaX509CertificateSigningRequest.
  - Each name of Qt's QOpcUaX509CertificateSigningRequest that has no cute
    function yet, 'createRequest', 'createSelfSignedCertificate', 'd_func',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  #  The enums Qt writes inside QOpcUaX509CertificateSigningRequest, each a
  #  class in here as in C++, and the names Qt has for the combinations of
  #  its flags enums.

  class Encoding(CuteNum, scoped=True):
    """
    The enum 'QOpcUaX509CertificateSigningRequest::Encoding' of Qt, with the
    2 names Qt gives in it. C++ keeps these names inside the enum, so the
    class that holds the enum does not have them.
    """

    PEM = Kee[int](0)
    DER = Kee[int](1)

  class MessageDigest(CuteNum, scoped=True):
    """
    The enum 'QOpcUaX509CertificateSigningRequest::MessageDigest' of Qt, with
    the 1 names Qt gives in it. C++ keeps these names inside the enum, so the
    class that holds the enum does not have them.
    """

    SHA256 = Kee[int](0)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOpcUaX509CertificateSigningRequest'

  #  Qt's '~QOpcUaX509CertificateSigningRequest()'. Naming it makes this a
  #  value class: Python owns every C++ QOpcUaX509CertificateSigningRequest
  #  behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN35QOpcUaX509CertificateSigningRequestD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def messageDigest(self) -> MessageDigest:
    """
    Calls Qt's 'MessageDigest
    QOpcUaX509CertificateSigningRequest::messageDigest() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuax509certificatesigningrequest.html

    Returns
    -------

    MessageDigest
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'MessageDigest(number)'
      gives.
    """
    #  MessageDigest QOpcUaX509CertificateSigningRequest::messageDigest()
    #      const
    return QOpcUaX509CertificateSigningRequest.MessageDigest(
        self.uglySide.call(
            'ritual_ZNK35QOpcUaX509CertificateSigningRequest13messageDigest'
            'Ev',
        ))

  def encoding(self) -> Encoding:
    """
    Calls Qt's 'Encoding QOpcUaX509CertificateSigningRequest::encoding()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuax509certificatesigningrequest.html#encoding

    Returns
    -------

    Encoding
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Encoding(number)' gives.
    """
    #  Encoding QOpcUaX509CertificateSigningRequest::encoding() const
    return QOpcUaX509CertificateSigningRequest.Encoding(self.uglySide.call(
        'ritual_ZNK35QOpcUaX509CertificateSigningRequest8encodingEv',
    ))

  def subject(self) -> QOpcUaX509DistinguishedName:
    """
    Calls Qt's 'const QOpcUaX509DistinguishedName
    &QOpcUaX509CertificateSigningRequest::subject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuax509certificatesigningrequest.html#subject

    Returns
    -------

    QOpcUaX509DistinguishedName
      A new cute QOpcUaX509DistinguishedName around the copy Qt gave back.
      Python owns it.
    """
    #  const QOpcUaX509DistinguishedName
    #      &QOpcUaX509CertificateSigningRequest::subject() const
    address = self.uglySide.call(
        'ritual_ZNK35QOpcUaX509CertificateSigningRequest7subjectEv',
    )
    from . import QOpcUaX509DistinguishedName
    return QOpcUaX509DistinguishedName._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(MessageDigest)
  def setMessageDigest(self, digest: MessageDigest) -> None:
    """
    Calls Qt's 'void
    QOpcUaX509CertificateSigningRequest::setMessageDigest(MessageDigest
    digest)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuax509certificatesigningrequest.html

    Parameters
    ----------

    digest : MessageDigest
      Passed on as its number.
    """
    #  void QOpcUaX509CertificateSigningRequest::setMessageDigest(
    #      MessageDigest digest)
    self.uglySide.call(
        'ritual_ZN35QOpcUaX509CertificateSigningRequest16setMessageDigestEN'
        'S_13MessageDigestE',
        digest.value,
    )

  @overload(Encoding)
  def setEncoding(self, encoding: Encoding) -> None:
    """
    Calls Qt's 'void
    QOpcUaX509CertificateSigningRequest::setEncoding(Encoding encoding)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuax509certificatesigningrequest.html

    Parameters
    ----------

    encoding : Encoding
      Passed on as its number.
    """
    #  void QOpcUaX509CertificateSigningRequest::setEncoding(Encoding
    #      encoding)
    self.uglySide.call(
        'ritual_ZN35QOpcUaX509CertificateSigningRequest11setEncodingENS_8En'
        'codingE',
        encoding.value,
    )

  @overload(QOpcUaX509DistinguishedName)
  def setSubject(self, subject: QOpcUaX509DistinguishedName) -> None:
    """
    Calls Qt's 'void QOpcUaX509CertificateSigningRequest::setSubject(const
    QOpcUaX509DistinguishedName &subject)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuax509certificatesigningrequest.html

    Parameters
    ----------

    subject : QOpcUaX509DistinguishedName
      Passed on as a value: Qt reads the C++ QOpcUaX509DistinguishedName,
      which stays Python's own.
    """
    #  void QOpcUaX509CertificateSigningRequest::setSubject(const
    #      QOpcUaX509DistinguishedName &subject)
    self.uglySide.call(
        'ritual_ZN35QOpcUaX509CertificateSigningRequest10setSubjectERK27QOp'
        'cUaX509DistinguishedName',
        self._valueOf(subject),
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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QOpcUaX509CertificateSigningRequest::
    QOpcUaX509CertificateSigningRequest()', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuax509certificatesigningrequest.html
    """
    #  QOpcUaX509CertificateSigningRequest::
    #      QOpcUaX509CertificateSigningRequest()
    self._noteCreation(
        QOpcUaX509CertificateSigningRequest, lambda: Rituals.call(
            'ritual_ZN35QOpcUaX509CertificateSigningRequestC1Ev',
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

  @overload(QOpcUaX509Extension)
  @overload(NoneType)
  def addExtension(self, extension: Optional[QOpcUaX509Extension]) -> None:
    """
    Calls Qt's 'void
    QOpcUaX509CertificateSigningRequest::addExtension(QOpcUaX509Extension
    *extension)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuax509certificatesigningrequest.html

    Parameters
    ----------

    extension : Optional[QOpcUaX509Extension]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QOpcUaX509CertificateSigningRequest::addExtension(
    #      QOpcUaX509Extension *extension)
    self.uglySide.call(
        'ritual_ZN35QOpcUaX509CertificateSigningRequest12addExtensionEP19QO'
        'pcUaX509Extension',
        self._addressOf(extension),
    )

  @staticmethod
  def createRequest(*__, **_) -> Never:
    """
    Qt's 'QByteArray QOpcUaX509CertificateSigningRequest::createRequest(const
    QOpcUaKeyPair &privateKey)': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'QOpcUaX509CertificateSigningRequest.createRequest' has no cute "
        "function yet. Qt's 'QByteArray "
        "QOpcUaX509CertificateSigningRequest::createRequest(const "
        "QOpcUaKeyPair &privateKey)': takes a type Python has no way to "
        "hand over yet.")

  @staticmethod
  def createSelfSignedCertificate(*__, **_) -> Never:
    """
    Qt's 'QByteArray
    QOpcUaX509CertificateSigningRequest::createSelfSignedCertificate(const
    QOpcUaKeyPair &privateKey, int validityInDays)': takes a type Python has
    no way to hand over yet.
    """
    raise NotImplementedError(
        "'QOpcUaX509CertificateSigningRequest.createSelfSignedCertificate' "
        "has no cute function yet. Qt's 'QByteArray "
        "QOpcUaX509CertificateSigningRequest::createSelfSignedCertificate(co"
        "nst QOpcUaKeyPair &privateKey, int validityInDays)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def d_func(*__, **_) -> Never:
    """
    - Qt's 'QOpcUaX509CertificateSigningRequestPrivate
      *QOpcUaX509CertificateSigningRequest::d_func()': gives
      'QOpcUaX509CertificateSigningRequestPrivate', which has no cute class
      yet.
    - Qt's 'const QOpcUaX509CertificateSigningRequestPrivate
      *QOpcUaX509CertificateSigningRequest::d_func() const': gives
      'QOpcUaX509CertificateSigningRequestPrivate', which has no cute class
      yet.
    """
    raise NotImplementedError(
        "'QOpcUaX509CertificateSigningRequest.d_func' has no cute function "
        "yet. Qt's 'QOpcUaX509CertificateSigningRequestPrivate "
        "*QOpcUaX509CertificateSigningRequest::d_func()': gives "
        "'QOpcUaX509CertificateSigningRequestPrivate', which has no cute "
        "class yet. Qt's 'const QOpcUaX509CertificateSigningRequestPrivate "
        "*QOpcUaX509CertificateSigningRequest::d_func() const': gives "
        "'QOpcUaX509CertificateSigningRequestPrivate', which has no cute "
        "class yet.")
