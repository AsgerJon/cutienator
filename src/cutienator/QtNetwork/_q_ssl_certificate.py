"""
QSslCertificate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/qsslcertificate.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QCryptographicHash, QList, QStringList
from . import QSsl

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QDateTime, QIODevice
  from . import QSslCertificateExtension, QSslError, QSslKey
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QIODevice = WAIT['QIODevice']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSslCertificate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSslCertificate: a plain Python object standing in
  front of one C++ QSslCertificate.

  C++ hands a QSslCertificate around as a copy, so every C++ QSslCertificate
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QSslCertificate that has a ritual and that Python
  can call so far, 27 names in all: '__eq__', '__ne__', 'isNull',
  'isBlacklisted', 'isSelfSigned', 'clear', 'version', 'serialNumber',
  'digest', 'issuerInfo', 'subjectInfo', 'issuerDisplayName',
  'subjectDisplayName', 'subjectInfoAttributes', 'issuerInfoAttributes',
  'effectiveDate', 'expiryDate', 'publicKey', 'extensions', 'toPem', 'toDer',
  'toText', 'fromPath', 'fromDevice', 'fromData', 'fromFile', 'verify'. It
  can be made from Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSslCertificate::QSslCertificate(QSslCertificate &&other)': takes a
    type Python has no way to hand over yet.
  - Qt's 'QSslCertificate::~QSslCertificate()': the destructor: Python
    removes its C++ QSslCertificate by it, and has no other use for it.
  - Qt's 'QSslCertificate &QSslCertificate::operator=(QSslCertificate
    &&other)': assignment: Python binds a name and has no operator for it.
  - Qt's 'QSslCertificate &QSslCertificate::operator=(const QSslCertificate
    &other)': assignment: Python binds a name and has no operator for it.
  - Qt's 'void QSslCertificate::swap(QSslCertificate &other)': takes a type
    Python has no way to hand over yet.
  - Qt's 'QMultiMap<QSsl::AlternativeNameEntryType, QString>
    QSslCertificate::subjectAlternativeNames() const': gives a type Python
    has no way to take yet.
  - Qt's 'bool QSslCertificate::importPkcs12(QIODevice *device, QSslKey *key,
    QSslCertificate *cert, QList<QSslCertificate> *caCertificates, const
    QByteArray &passPhrase)': names 'QList<QSslCertificate>', which has no
    cute class yet.
  - Qt's 'Qt::HANDLE QSslCertificate::handle() const': gives 'void', which
    has no cute class yet.

  What to expect
  --------------

  - The C++ QSslCertificate is created at the first use, not by
    'QSslCertificate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSslCertificate back gives a copy the ritual made for
    Python, in a new cute QSslCertificate.
  - Each name of Qt's QSslCertificate that has no cute function yet,
    'handle', 'importPkcs12', 'subjectAlternativeNames', 'swap', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QSslCertificate, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class PatternSyntax(CuteNum, scoped=True):
    """
    The enum 'QSslCertificate::PatternSyntax' of Qt, with the 3 names Qt
    gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    RegularExpression = Kee[int](0)
    Wildcard = Kee[int](1)
    FixedString = Kee[int](2)

  class SubjectInfo(CuteNum):
    """
    The enum 'QSslCertificate::SubjectInfo' of Qt, with the 9 names Qt gives
    in it.
    """

    Organization = Kee[int](0)
    CommonName = Kee[int](1)
    LocalityName = Kee[int](2)
    OrganizationalUnitName = Kee[int](3)
    CountryName = Kee[int](4)
    StateOrProvinceName = Kee[int](5)
    DistinguishedNameQualifier = Kee[int](6)
    SerialNumber = Kee[int](7)
    EmailAddress = Kee[int](8)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  @overload(str, QSsl.EncodingFormat)
  @overload(str, QSsl.EncodingFormat, PatternSyntax)
  def fromPath(
      path: str,
      format: QSsl.EncodingFormat = QSsl.EncodingFormat.Pem,
      syntax: PatternSyntax = PatternSyntax.FixedString,
  ) -> QList[QSslCertificate]:
    """
    Calls Qt's 'QList<QSslCertificate> QSslCertificate::fromPath(const
    QString &path, QSsl::EncodingFormat format, PatternSyntax syntax)'.

    Qt's own words: https://doc.qt.io/qt-6/qsslcertificate.html#fromPath

    Parameters
    ----------

    path : str
      Passed on as it is: a QString is made of it for the call.

    format : QSsl.EncodingFormat
      Passed on as its number. May be left out, as in Qt: it is then
      QSsl.EncodingFormat.Pem.

    syntax : PatternSyntax
      Passed on as its number. May be left out, as in Qt: it is then
      PatternSyntax.FixedString.

    Returns
    -------

    QList[QSslCertificate]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QSslCertificate> QSslCertificate::fromPath(const QString &path,
    #      QSsl::EncodingFormat format, PatternSyntax syntax)
    address = Rituals.call(
        'ritual_ZN15QSslCertificate8fromPathERK7QStringN4QSsl14EncodingForm'
        'atENS_13PatternSyntaxE',
        path, format.value, syntax.value,
    )
    return QList[QSslCertificate]._cuteOwning(address)

  @staticmethod
  @overload(QIODevice)
  @overload(NoneType)
  @overload(QIODevice, QSsl.EncodingFormat)
  @overload(NoneType, QSsl.EncodingFormat)
  def fromDevice(
      device: Optional[QIODevice],
      format: QSsl.EncodingFormat = QSsl.EncodingFormat.Pem,
  ) -> QList[QSslCertificate]:
    """
    Calls Qt's 'QList<QSslCertificate> QSslCertificate::fromDevice(QIODevice
    *device, QSsl::EncodingFormat format)'.

    Qt's own words: https://doc.qt.io/qt-6/qsslcertificate.html#fromDevice

    Parameters
    ----------

    device : Optional[QIODevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    format : QSsl.EncodingFormat
      Passed on as its number. May be left out, as in Qt: it is then
      QSsl.EncodingFormat.Pem.

    Returns
    -------

    QList[QSslCertificate]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QSslCertificate> QSslCertificate::fromDevice(QIODevice *device,
    #      QSsl::EncodingFormat format)
    address = Rituals.call(
        'ritual_ZN15QSslCertificate10fromDeviceEP9QIODeviceN4QSsl14Encoding'
        'FormatE',
        CuteMixin._addressOf(device), format.value,
    )
    return QList[QSslCertificate]._cuteOwning(address)

  @staticmethod
  @overload(QByteArray)
  @overload(QByteArray, QSsl.EncodingFormat)
  def fromData(
      data: QByteArray,
      format: QSsl.EncodingFormat = QSsl.EncodingFormat.Pem,
  ) -> QList[QSslCertificate]:
    """
    Calls Qt's 'QList<QSslCertificate> QSslCertificate::fromData(const
    QByteArray &data, QSsl::EncodingFormat format)'.

    Qt's own words: https://doc.qt.io/qt-6/qsslcertificate.html#fromData

    Parameters
    ----------

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    format : QSsl.EncodingFormat
      Passed on as its number. May be left out, as in Qt: it is then
      QSsl.EncodingFormat.Pem.

    Returns
    -------

    QList[QSslCertificate]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QSslCertificate> QSslCertificate::fromData(const QByteArray
    #      &data, QSsl::EncodingFormat format)
    address = Rituals.call(
        'ritual_ZN15QSslCertificate8fromDataERK10QByteArrayN4QSsl14Encoding'
        'FormatE',
        CuteMixin._valueOf(data), format.value,
    )
    return QList[QSslCertificate]._cuteOwning(address)

  @staticmethod
  @overload(str)
  @overload(str, QSsl.EncodingFormat)
  def fromFile(
      filePath: str,
      format: QSsl.EncodingFormat = QSsl.EncodingFormat.Pem,
  ) -> QList[QSslCertificate]:
    """
    Calls Qt's 'QList<QSslCertificate> QSslCertificate::fromFile(const
    QString &filePath, QSsl::EncodingFormat format)'.

    Qt's own words: https://doc.qt.io/qt-6/qsslcertificate.html#fromFile

    Parameters
    ----------

    filePath : str
      Passed on as it is: a QString is made of it for the call.

    format : QSsl.EncodingFormat
      Passed on as its number. May be left out, as in Qt: it is then
      QSsl.EncodingFormat.Pem.

    Returns
    -------

    QList[QSslCertificate]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QSslCertificate> QSslCertificate::fromFile(const QString
    #      &filePath, QSsl::EncodingFormat format)
    address = Rituals.call(
        'ritual_ZN15QSslCertificate8fromFileERK7QStringN4QSsl14EncodingForm'
        'atE',
        filePath, format.value,
    )
    return QList[QSslCertificate]._cuteOwning(address)

  @staticmethod
  @overload(QList[WAIT['QSslCertificate']])
  @overload(QList[WAIT['QSslCertificate']], str)
  def verify(
      certificateChain: QList[QSslCertificate],
      hostName: str = '',
  ) -> QList[QSslError]:
    """
    Calls Qt's 'QList<QSslError> QSslCertificate::verify(const
    QList<QSslCertificate> &certificateChain, const QString &hostName)'.

    Qt's own words: https://doc.qt.io/qt-6/qsslcertificate.html#verify

    Parameters
    ----------

    certificateChain : QList[QSslCertificate]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    hostName : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    Returns
    -------

    QList[QSslError]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QSslError> QSslCertificate::verify(const QList<QSslCertificate>
    #      &certificateChain, const QString &hostName)
    address = Rituals.call(
        'ritual_ZN15QSslCertificate6verifyERK5QListIS_ERK7QString',
        CuteMixin._valueOf(certificateChain), hostName,
    )
    from . import QSslError
    return QList[QSslError]._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSslCertificate'

  #  Qt's '~QSslCertificate()'. Naming it makes this a value class: Python
  #  owns every C++ QSslCertificate behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN15QSslCertificateD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isNull(self) -> bool:
    """
    Calls Qt's 'bool QSslCertificate::isNull() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsslcertificate.html#isNull
    """
    #  bool QSslCertificate::isNull() const
    return self.uglySide.call('ritual_ZNK15QSslCertificate6isNullEv')

  def isBlacklisted(self) -> bool:
    """
    Calls Qt's 'bool QSslCertificate::isBlacklisted() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsslcertificate.html#isBlacklisted
    """
    #  bool QSslCertificate::isBlacklisted() const
    return self.uglySide.call('ritual_ZNK15QSslCertificate13isBlacklistedEv')

  def isSelfSigned(self) -> bool:
    """
    Calls Qt's 'bool QSslCertificate::isSelfSigned() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsslcertificate.html#isSelfSigned
    """
    #  bool QSslCertificate::isSelfSigned() const
    return self.uglySide.call('ritual_ZNK15QSslCertificate12isSelfSignedEv')

  def version(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QSslCertificate::version() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsslcertificate.html#version

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QSslCertificate::version() const
    address = self.uglySide.call('ritual_ZNK15QSslCertificate7versionEv')
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def serialNumber(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QSslCertificate::serialNumber() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsslcertificate.html#serialNumber

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QSslCertificate::serialNumber() const
    address = self.uglySide.call(
        'ritual_ZNK15QSslCertificate12serialNumberEv',
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  @overload()
  @overload(QCryptographicHash.Algorithm)
  def digest(
      self,
      algorithm: QCryptographicHash.Algorithm = (
          QCryptographicHash.Algorithm.Md5),
  ) -> QByteArray:
    """
    Calls Qt's 'QByteArray
    QSslCertificate::digest(QCryptographicHash::Algorithm algorithm) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsslcertificate.html#digest

    Parameters
    ----------

    algorithm : QCryptographicHash.Algorithm
      Passed on as its number. May be left out, as in Qt: it is then
      QCryptographicHash.Algorithm.Md5.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QSslCertificate::digest(QCryptographicHash::Algorithm
    #      algorithm) const
    address = self.uglySide.call(
        'ritual_ZNK15QSslCertificate6digestEN18QCryptographicHash9Algorithm'
        'E',
        algorithm.value,
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  @overload(SubjectInfo)
  def issuerInfo(self, info: SubjectInfo) -> QStringList:
    """
    Calls Qt's 'QStringList QSslCertificate::issuerInfo(SubjectInfo info)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qsslcertificate.html#issuerInfo

    Parameters
    ----------

    info : SubjectInfo
      Passed on as its number.

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QSslCertificate::issuerInfo(SubjectInfo info) const
    address = self.uglySide.call(
        'ritual_ZNK15QSslCertificate10issuerInfoENS_11SubjectInfoE',
        info.value,
    )
    return QStringList._cuteOwning(address)

  @overload(QByteArray)
  def issuerInfo(self, attribute: QByteArray) -> QStringList:
    """
    Calls Qt's 'QStringList QSslCertificate::issuerInfo(const QByteArray
    &attribute) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsslcertificate.html#issuerInfo

    Parameters
    ----------

    attribute : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QSslCertificate::issuerInfo(const QByteArray &attribute)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK15QSslCertificate10issuerInfoERK10QByteArray',
        self._valueOf(attribute),
    )
    return QStringList._cuteOwning(address)

  @overload(SubjectInfo)
  def subjectInfo(self, info: SubjectInfo) -> QStringList:
    """
    Calls Qt's 'QStringList QSslCertificate::subjectInfo(SubjectInfo info)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qsslcertificate.html#subjectInfo

    Parameters
    ----------

    info : SubjectInfo
      Passed on as its number.

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QSslCertificate::subjectInfo(SubjectInfo info) const
    address = self.uglySide.call(
        'ritual_ZNK15QSslCertificate11subjectInfoENS_11SubjectInfoE',
        info.value,
    )
    return QStringList._cuteOwning(address)

  @overload(QByteArray)
  def subjectInfo(self, attribute: QByteArray) -> QStringList:
    """
    Calls Qt's 'QStringList QSslCertificate::subjectInfo(const QByteArray
    &attribute) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsslcertificate.html#subjectInfo

    Parameters
    ----------

    attribute : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QSslCertificate::subjectInfo(const QByteArray &attribute)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK15QSslCertificate11subjectInfoERK10QByteArray',
        self._valueOf(attribute),
    )
    return QStringList._cuteOwning(address)

  def issuerDisplayName(self) -> str:
    """
    Calls Qt's 'QString QSslCertificate::issuerDisplayName() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslcertificate.html#issuerDisplayName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSslCertificate::issuerDisplayName() const
    return self.uglySide.call(
        'ritual_ZNK15QSslCertificate17issuerDisplayNameEv',
    )

  def subjectDisplayName(self) -> str:
    """
    Calls Qt's 'QString QSslCertificate::subjectDisplayName() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslcertificate.html#subjectDisplayName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSslCertificate::subjectDisplayName() const
    return self.uglySide.call(
        'ritual_ZNK15QSslCertificate18subjectDisplayNameEv',
    )

  def subjectInfoAttributes(self) -> QList[QByteArray]:
    """
    Calls Qt's 'QList<QByteArray> QSslCertificate::subjectInfoAttributes()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslcertificate.html#subjectInfoAttributes

    Returns
    -------

    QList[QByteArray]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QByteArray> QSslCertificate::subjectInfoAttributes() const
    address = self.uglySide.call(
        'ritual_ZNK15QSslCertificate21subjectInfoAttributesEv',
    )
    from ..QtCore import QByteArray
    return QList[QByteArray]._cuteOwning(address)

  def issuerInfoAttributes(self) -> QList[QByteArray]:
    """
    Calls Qt's 'QList<QByteArray> QSslCertificate::issuerInfoAttributes()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslcertificate.html#issuerInfoAttributes

    Returns
    -------

    QList[QByteArray]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QByteArray> QSslCertificate::issuerInfoAttributes() const
    address = self.uglySide.call(
        'ritual_ZNK15QSslCertificate20issuerInfoAttributesEv',
    )
    from ..QtCore import QByteArray
    return QList[QByteArray]._cuteOwning(address)

  def effectiveDate(self) -> QDateTime:
    """
    Calls Qt's 'QDateTime QSslCertificate::effectiveDate() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsslcertificate.html#effectiveDate

    Returns
    -------

    QDateTime
      A new cute QDateTime around the copy Qt gave back. Python owns it.
    """
    #  QDateTime QSslCertificate::effectiveDate() const
    address = self.uglySide.call(
        'ritual_ZNK15QSslCertificate13effectiveDateEv',
    )
    from ..QtCore import QDateTime
    return QDateTime._cuteOwning(address)

  def expiryDate(self) -> QDateTime:
    """
    Calls Qt's 'QDateTime QSslCertificate::expiryDate() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsslcertificate.html#expiryDate

    Returns
    -------

    QDateTime
      A new cute QDateTime around the copy Qt gave back. Python owns it.
    """
    #  QDateTime QSslCertificate::expiryDate() const
    address = self.uglySide.call('ritual_ZNK15QSslCertificate10expiryDateEv')
    from ..QtCore import QDateTime
    return QDateTime._cuteOwning(address)

  def publicKey(self) -> QSslKey:
    """
    Calls Qt's 'QSslKey QSslCertificate::publicKey() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsslcertificate.html#publicKey

    Returns
    -------

    QSslKey
      A new cute QSslKey around the copy Qt gave back. Python owns it.
    """
    #  QSslKey QSslCertificate::publicKey() const
    address = self.uglySide.call('ritual_ZNK15QSslCertificate9publicKeyEv')
    from . import QSslKey
    return QSslKey._cuteOwning(address)

  def extensions(self) -> QList[QSslCertificateExtension]:
    """
    Calls Qt's 'QList<QSslCertificateExtension> QSslCertificate::extensions()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qsslcertificate.html#extensions

    Returns
    -------

    QList[QSslCertificateExtension]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QSslCertificateExtension> QSslCertificate::extensions() const
    address = self.uglySide.call('ritual_ZNK15QSslCertificate10extensionsEv')
    from . import QSslCertificateExtension
    return QList[QSslCertificateExtension]._cuteOwning(address)

  def toPem(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QSslCertificate::toPem() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsslcertificate.html#toPem

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QSslCertificate::toPem() const
    address = self.uglySide.call('ritual_ZNK15QSslCertificate5toPemEv')
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def toDer(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QSslCertificate::toDer() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsslcertificate.html#toDer

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QSslCertificate::toDer() const
    address = self.uglySide.call('ritual_ZNK15QSslCertificate5toDerEv')
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def toText(self) -> str:
    """
    Calls Qt's 'QString QSslCertificate::toText() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsslcertificate.html#toText

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSslCertificate::toText() const
    return self.uglySide.call('ritual_ZNK15QSslCertificate6toTextEv')

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
  def __eq__(self, other: QSslCertificate) -> bool:
    """
    Calls Qt's 'bool QSslCertificate::operator==(const QSslCertificate
    &other) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsslcertificate.html#operator==

    Parameters
    ----------

    other : QSslCertificate
      Passed on as a value: Qt reads the C++ QSslCertificate, which stays
      Python's own.
    """
    #  bool QSslCertificate::operator==(const QSslCertificate &other) const
    return self.uglySide.call(
        'ritual_ZNK15QSslCertificateeqERKS_', self._valueOf(other),
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
  def __ne__(self, other: QSslCertificate) -> bool:
    """
    Calls Qt's 'bool QSslCertificate::operator!=(const QSslCertificate
    &other) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsslcertificate.html#operator!=

    Parameters
    ----------

    other : QSslCertificate
      Passed on as a value: Qt reads the C++ QSslCertificate, which stays
      Python's own.
    """
    #  bool QSslCertificate::operator!=(const QSslCertificate &other) const
    return self.uglySide.call(
        'ritual_ZNK15QSslCertificateneERKS_', self._valueOf(other),
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

  @overload(QIODevice)
  @overload(NoneType)
  @overload(QIODevice, QSsl.EncodingFormat)
  @overload(NoneType, QSsl.EncodingFormat)
  def __init__(
      self,
      device: Optional[QIODevice],
      format: QSsl.EncodingFormat = QSsl.EncodingFormat.Pem,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QSslCertificate::QSslCertificate(QIODevice *device, QSsl::EncodingFormat
    format)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslcertificate.html#QSslCertificate

    Parameters
    ----------

    device : Optional[QIODevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    format : QSsl.EncodingFormat
      Passed on as its number. May be left out, as in Qt: it is then
      QSsl.EncodingFormat.Pem.
    """
    #  QSslCertificate::QSslCertificate(QIODevice *device,
    #      QSsl::EncodingFormat format)
    self._noteCreation(QSslCertificate, lambda: Rituals.call(
        'ritual_ZN15QSslCertificateC1EP9QIODeviceN4QSsl14EncodingFormatE',
        self._addressOf(device), format.value,
    ))

  @overload()
  @overload(QByteArray)
  @overload(QByteArray, QSsl.EncodingFormat)
  def __init__(
      self,
      data: Optional[QByteArray] = None,
      format: QSsl.EncodingFormat = QSsl.EncodingFormat.Pem,
  ) -> None:
    """
    Notes what was given, for Qt's 'QSslCertificate::QSslCertificate(const
    QByteArray &data, QSsl::EncodingFormat format)', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslcertificate.html#QSslCertificate

    Parameters
    ----------

    data : Optional[QByteArray]
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own. May be left out, as in Qt: a new 'QByteArray()' is then passed on.

    format : QSsl.EncodingFormat
      Passed on as its number. May be left out, as in Qt: it is then
      QSsl.EncodingFormat.Pem.
    """
    #  QSslCertificate::QSslCertificate(const QByteArray &data,
    #      QSsl::EncodingFormat format)
    if data is None:
      from ..QtCore import QByteArray
      data = QByteArray()
    self._noteCreation(QSslCertificate, lambda: Rituals.call(
        'ritual_ZN15QSslCertificateC1ERK10QByteArrayN4QSsl14EncodingFormatE',
        self._valueOf(data), format.value,
    ))

  @overload(THIS)
  def __init__(self, other: QSslCertificate) -> None:
    """
    Notes what was given, for Qt's 'QSslCertificate::QSslCertificate(const
    QSslCertificate &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslcertificate.html#QSslCertificate

    Parameters
    ----------

    other : QSslCertificate
      Passed on as a value: Qt reads the C++ QSslCertificate, which stays
      Python's own.
    """
    #  QSslCertificate::QSslCertificate(const QSslCertificate &other)
    self._noteCreation(QSslCertificate, lambda: Rituals.call(
        'ritual_ZN15QSslCertificateC1ERKS_', self._valueOf(other),
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

  def clear(self) -> None:
    """
    Calls Qt's 'void QSslCertificate::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qsslcertificate.html#clear
    """
    #  void QSslCertificate::clear()
    self.uglySide.call('ritual_ZN15QSslCertificate5clearEv')

  @staticmethod
  def handle(*__, **_) -> Never:
    """
    Qt's 'Qt::HANDLE QSslCertificate::handle() const': gives 'void', which
    has no cute class yet.
    """
    raise NotImplementedError(
        "'QSslCertificate.handle' has no cute function yet. Qt's "
        "'Qt::HANDLE QSslCertificate::handle() const': gives 'void', which "
        "has no cute class yet.")

  @staticmethod
  def importPkcs12(*__, **_) -> Never:
    """
    Qt's 'bool QSslCertificate::importPkcs12(QIODevice *device, QSslKey *key,
    QSslCertificate *cert, QList<QSslCertificate> *caCertificates, const
    QByteArray &passPhrase)': names 'QList<QSslCertificate>', which has no
    cute class yet.
    """
    raise NotImplementedError(
        "'QSslCertificate.importPkcs12' has no cute function yet. Qt's "
        "'bool QSslCertificate::importPkcs12(QIODevice *device, QSslKey "
        "*key, QSslCertificate *cert, QList<QSslCertificate> "
        "*caCertificates, const QByteArray &passPhrase)': names "
        "'QList<QSslCertificate>', which has no cute class yet.")

  @staticmethod
  def subjectAlternativeNames(*__, **_) -> Never:
    """
    Qt's 'QMultiMap<QSsl::AlternativeNameEntryType, QString>
    QSslCertificate::subjectAlternativeNames() const': gives a type Python
    has no way to take yet.
    """
    raise NotImplementedError(
        "'QSslCertificate.subjectAlternativeNames' has no cute function "
        "yet. Qt's 'QMultiMap<QSsl::AlternativeNameEntryType, QString> "
        "QSslCertificate::subjectAlternativeNames() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QSslCertificate::swap(QSslCertificate &other)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSslCertificate.swap' has no cute function yet. Qt's 'void "
        "QSslCertificate::swap(QSslCertificate &other)': takes a type "
        "Python has no way to hand over yet.")


#  Qt's 'QList<QSslCertificate>': the list of QSslCertificate, which
#  'QList[QSslCertificate]' gives. It is made here, so that there is one as
#  soon as there can be a QSslCertificate.
QList.createKind(
    QSslCertificate, 'value',
    make='ritual_list_make_QSslCertificate',
    add='ritual_list_add_QSslCertificate',
    size='ritual_list_size_QSslCertificate',
    at='ritual_list_at_QSslCertificate',
    drop='ritual_list_drop_QSslCertificate',
)
