"""
QTlsPrivate::X509Certificate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/6.12.0/QtNetwork/private/qtlsbackend_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QTlsPrivate::X509Certificate to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..QtCore import QList, QStringList
from . import QSslCertificate, QTlsPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QDateTime, QVariant
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']


class X509Certificate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QTlsPrivate::X509Certificate: a plain Python object
  standing in front of one C++ QTlsPrivate::X509Certificate.

  What exists
  -----------

  Every function of Qt's QTlsPrivate::X509Certificate that has a ritual and
  that Python can call so far, 21 names in all: 'isNull', 'isSelfSigned',
  'version', 'serialNumber', 'issuerInfo', 'subjectInfo',
  'subjectInfoAttributes', 'issuerInfoAttributes', 'effectiveDate',
  'expiryDate', 'publicKey', 'numberOfExtensions', 'oidForExtension',
  'nameForExtension', 'valueForExtension', 'isExtensionCritical',
  'isExtensionSupported', 'toPem', 'toDer', 'toText', 'hash'. None can be
  made from Python: one comes out of a function of another class that gives
  one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QTlsPrivate::X509Certificate::~X509Certificate()': the destructor:
    Python never removes a C++ QTlsPrivate::X509Certificate.
  - Qt's 'bool QTlsPrivate::X509Certificate::isEqual(const X509Certificate
    &other) const': takes a type Python has no way to hand over yet.
  - Qt's 'QMultiMap<QSsl::AlternativeNameEntryType, QString>
    QTlsPrivate::X509Certificate::subjectAlternativeNames() const': gives a
    type Python has no way to take yet.
  - Qt's 'Qt::HANDLE QTlsPrivate::X509Certificate::handle() const': gives
    'void', which has no cute class yet.

  What to expect
  --------------

  - The C++ QTlsPrivate::X509Certificate is created at the first use, not by
    'QTlsPrivate::X509Certificate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QTlsPrivate::X509Certificate.
  - Each name of Qt's QTlsPrivate::X509Certificate that has no cute function
    yet, 'handle', 'isEqual', 'subjectAlternativeNames', holds a function
    that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QTlsPrivate::X509Certificate'

  #  A C++ QTlsPrivate::X509Certificate Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QTlsPrivate_X509Certificate'

  #  The functions Qt calls itself that QTlsPrivate::X509Certificate is the
  #  first to declare and that cannot be handed to Python yet, each as Qt
  #  declares it. A class of a program that writes one of them anew is
  #  refused, since Qt would never call what it wrote; see
  #  'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'isEqual': (
          'bool QTlsPrivate::X509Certificate::isEqual(const '
          'X509Certificate &) const',
      ),
      'issuerInfo': (
          'QStringList '
          'QTlsPrivate::X509Certificate::issuerInfo(QSslCertificate::Subjec'
          'tInfo) const',
          'QStringList QTlsPrivate::X509Certificate::issuerInfo(const '
          'QByteArray &) const',
      ),
      'subjectInfo': (
          'QStringList '
          'QTlsPrivate::X509Certificate::subjectInfo(QSslCertificate::Subje'
          'ctInfo) const',
          'QStringList QTlsPrivate::X509Certificate::subjectInfo(const '
          'QByteArray &) const',
      ),
      'subjectInfoAttributes': (
          'QList<QByteArray> '
          'QTlsPrivate::X509Certificate::subjectInfoAttributes() const',
      ),
      'issuerInfoAttributes': (
          'QList<QByteArray> '
          'QTlsPrivate::X509Certificate::issuerInfoAttributes() const',
      ),
      'subjectAlternativeNames': (
          'QMultiMap<QSsl::AlternativeNameEntryType, QString> '
          'QTlsPrivate::X509Certificate::subjectAlternativeNames() const',
      ),
      'handle': (
          'Qt::HANDLE QTlsPrivate::X509Certificate::handle() const',
      ),
  }

  #  The functions Qt calls itself that QTlsPrivate::X509Certificate is the
  #  first to declare. A class of a program built on it can write one anew,
  #  and Qt then calls that. For each name: the key C++ knows the function
  #  by, what it gives, and what it takes.
  __virtual_functions__ = {
      'isNull': (
          ('_ZNK11QTlsPrivate15X509Certificate6isNullEv',
           ('bool', 'number', ''),
           ()),
      ),
      'isSelfSigned': (
          ('_ZNK11QTlsPrivate15X509Certificate12isSelfSignedEv',
           ('bool', 'number', ''),
           ()),
      ),
      'version': (
          ('_ZNK11QTlsPrivate15X509Certificate7versionEv',
           ('address', 'value', 'QtCore:QByteArray'),
           ()),
      ),
      'serialNumber': (
          ('_ZNK11QTlsPrivate15X509Certificate12serialNumberEv',
           ('address', 'value', 'QtCore:QByteArray'),
           ()),
      ),
      'effectiveDate': (
          ('_ZNK11QTlsPrivate15X509Certificate13effectiveDateEv',
           ('address', 'value', 'QtCore:QDateTime'),
           ()),
      ),
      'expiryDate': (
          ('_ZNK11QTlsPrivate15X509Certificate10expiryDateEv',
           ('address', 'value', 'QtCore:QDateTime'),
           ()),
      ),
      'publicKey': (
          ('_ZNK11QTlsPrivate15X509Certificate9publicKeyEv',
           ('address', 'address', 'QtNetwork:QTlsPrivate.TlsKey'),
           ()),
      ),
      'numberOfExtensions': (
          ('_ZNK11QTlsPrivate15X509Certificate18numberOfExtensionsEv',
           ('long long', 'number', ''),
           ()),
      ),
      'oidForExtension': (
          ('_ZNK11QTlsPrivate15X509Certificate15oidForExtensionEx',
           ('address', 'text', ''),
           (
               ('long long', 'number', ''),
           )),
      ),
      'nameForExtension': (
          ('_ZNK11QTlsPrivate15X509Certificate16nameForExtensionEx',
           ('address', 'text', ''),
           (
               ('long long', 'number', ''),
           )),
      ),
      'valueForExtension': (
          ('_ZNK11QTlsPrivate15X509Certificate17valueForExtensionEx',
           ('address', 'value', 'QtCore:QVariant'),
           (
               ('long long', 'number', ''),
           )),
      ),
      'isExtensionCritical': (
          ('_ZNK11QTlsPrivate15X509Certificate19isExtensionCriticalEx',
           ('bool', 'number', ''),
           (
               ('long long', 'number', ''),
           )),
      ),
      'isExtensionSupported': (
          ('_ZNK11QTlsPrivate15X509Certificate20isExtensionSupportedEx',
           ('bool', 'number', ''),
           (
               ('long long', 'number', ''),
           )),
      ),
      'toPem': (
          ('_ZNK11QTlsPrivate15X509Certificate5toPemEv',
           ('address', 'value', 'QtCore:QByteArray'),
           ()),
      ),
      'toDer': (
          ('_ZNK11QTlsPrivate15X509Certificate5toDerEv',
           ('address', 'value', 'QtCore:QByteArray'),
           ()),
      ),
      'toText': (
          ('_ZNK11QTlsPrivate15X509Certificate6toTextEv',
           ('address', 'text', ''),
           ()),
      ),
      'hash': (
          ('_ZNK11QTlsPrivate15X509Certificate4hashEm',
           ('size_t', 'number', ''),
           (
               ('size_t', 'number', ''),
           )),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isNull(self) -> bool:
    """
    Calls Qt's 'bool QTlsPrivate::X509Certificate::isNull() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtlsprivate-x509certificate.html#isNull
    """
    #  bool QTlsPrivate::X509Certificate::isNull() const
    return self.uglySide.call(
        'ritual_ZNK11QTlsPrivate15X509Certificate6isNullEv',
    )

  def isSelfSigned(self) -> bool:
    """
    Calls Qt's 'bool QTlsPrivate::X509Certificate::isSelfSigned() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtlsprivate-x509certificate.html#isSelfSigned
    """
    #  bool QTlsPrivate::X509Certificate::isSelfSigned() const
    return self.uglySide.call(
        'ritual_ZNK11QTlsPrivate15X509Certificate12isSelfSignedEv',
    )

  def version(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QTlsPrivate::X509Certificate::version() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtlsprivate-x509certificate.html#version

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QTlsPrivate::X509Certificate::version() const
    address = self.uglySide.call(
        'ritual_ZNK11QTlsPrivate15X509Certificate7versionEv',
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def serialNumber(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QTlsPrivate::X509Certificate::serialNumber()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtlsprivate-x509certificate.html#serialNumber

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QTlsPrivate::X509Certificate::serialNumber() const
    address = self.uglySide.call(
        'ritual_ZNK11QTlsPrivate15X509Certificate12serialNumberEv',
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  @overload(QSslCertificate.SubjectInfo)
  def issuerInfo(self, subject: QSslCertificate.SubjectInfo) -> QStringList:
    """
    Calls Qt's 'QStringList
    QTlsPrivate::X509Certificate::issuerInfo(QSslCertificate::SubjectInfo
    subject) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtlsprivate-x509certificate.html#issuerInfo

    Parameters
    ----------

    subject : QSslCertificate.SubjectInfo
      Passed on as its number.

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QTlsPrivate::X509Certificate::issuerInfo(QSslCertificate::
    #      SubjectInfo subject) const
    address = self.uglySide.call(
        'ritual_ZNK11QTlsPrivate15X509Certificate10issuerInfoEN15QSslCertif'
        'icate11SubjectInfoE',
        subject.value,
    )
    return QStringList._cuteOwning(address)

  @overload(QByteArray)
  def issuerInfo(self, attribute: QByteArray) -> QStringList:
    """
    Calls Qt's 'QStringList QTlsPrivate::X509Certificate::issuerInfo(const
    QByteArray &attribute) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtlsprivate-x509certificate.html#issuerInfo

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
    #  QStringList QTlsPrivate::X509Certificate::issuerInfo(const QByteArray
    #      &attribute) const
    address = self.uglySide.call(
        'ritual_ZNK11QTlsPrivate15X509Certificate10issuerInfoERK10QByteArra'
        'y',
        self._valueOf(attribute),
    )
    return QStringList._cuteOwning(address)

  @overload(QSslCertificate.SubjectInfo)
  def subjectInfo(self, subject: QSslCertificate.SubjectInfo) -> QStringList:
    """
    Calls Qt's 'QStringList
    QTlsPrivate::X509Certificate::subjectInfo(QSslCertificate::SubjectInfo
    subject) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtlsprivate-x509certificate.html#subjectInfo

    Parameters
    ----------

    subject : QSslCertificate.SubjectInfo
      Passed on as its number.

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList
    #      QTlsPrivate::X509Certificate::subjectInfo(QSslCertificate::
    #      SubjectInfo subject) const
    address = self.uglySide.call(
        'ritual_ZNK11QTlsPrivate15X509Certificate11subjectInfoEN15QSslCerti'
        'ficate11SubjectInfoE',
        subject.value,
    )
    return QStringList._cuteOwning(address)

  @overload(QByteArray)
  def subjectInfo(self, attribute: QByteArray) -> QStringList:
    """
    Calls Qt's 'QStringList QTlsPrivate::X509Certificate::subjectInfo(const
    QByteArray &attribute) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtlsprivate-x509certificate.html#subjectInfo

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
    #  QStringList QTlsPrivate::X509Certificate::subjectInfo(const QByteArray
    #      &attribute) const
    address = self.uglySide.call(
        'ritual_ZNK11QTlsPrivate15X509Certificate11subjectInfoERK10QByteArr'
        'ay',
        self._valueOf(attribute),
    )
    return QStringList._cuteOwning(address)

  def subjectInfoAttributes(self) -> QList[QByteArray]:
    """
    Calls Qt's 'QList<QByteArray>
    QTlsPrivate::X509Certificate::subjectInfoAttributes() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtlsprivate-x509certificate.html

    Returns
    -------

    QList[QByteArray]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QByteArray>
    #      QTlsPrivate::X509Certificate::subjectInfoAttributes() const
    address = self.uglySide.call(
        'ritual_ZNK11QTlsPrivate15X509Certificate21subjectInfoAttributesEv',
    )
    from ..QtCore import QByteArray
    return QList[QByteArray]._cuteOwning(address)

  def issuerInfoAttributes(self) -> QList[QByteArray]:
    """
    Calls Qt's 'QList<QByteArray>
    QTlsPrivate::X509Certificate::issuerInfoAttributes() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtlsprivate-x509certificate.html

    Returns
    -------

    QList[QByteArray]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QByteArray> QTlsPrivate::X509Certificate::issuerInfoAttributes()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK11QTlsPrivate15X509Certificate20issuerInfoAttributesEv',
    )
    from ..QtCore import QByteArray
    return QList[QByteArray]._cuteOwning(address)

  def effectiveDate(self) -> QDateTime:
    """
    Calls Qt's 'QDateTime QTlsPrivate::X509Certificate::effectiveDate()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtlsprivate-x509certificate.html#effectiveDate

    Returns
    -------

    QDateTime
      A new cute QDateTime around the copy Qt gave back. Python owns it.
    """
    #  QDateTime QTlsPrivate::X509Certificate::effectiveDate() const
    address = self.uglySide.call(
        'ritual_ZNK11QTlsPrivate15X509Certificate13effectiveDateEv',
    )
    from ..QtCore import QDateTime
    return QDateTime._cuteOwning(address)

  def expiryDate(self) -> QDateTime:
    """
    Calls Qt's 'QDateTime QTlsPrivate::X509Certificate::expiryDate() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtlsprivate-x509certificate.html#expiryDate

    Returns
    -------

    QDateTime
      A new cute QDateTime around the copy Qt gave back. Python owns it.
    """
    #  QDateTime QTlsPrivate::X509Certificate::expiryDate() const
    address = self.uglySide.call(
        'ritual_ZNK11QTlsPrivate15X509Certificate10expiryDateEv',
    )
    from ..QtCore import QDateTime
    return QDateTime._cuteOwning(address)

  def publicKey(self) -> Optional[QTlsPrivate.TlsKey]:
    """
    Calls Qt's 'TlsKey *QTlsPrivate::X509Certificate::publicKey() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtlsprivate-x509certificate.html#publicKey

    Returns
    -------

    Optional[QTlsPrivate.TlsKey]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  TlsKey *QTlsPrivate::X509Certificate::publicKey() const
    ritual = 'ritual_ZNK11QTlsPrivate15X509Certificate9publicKeyEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QTlsPrivate15X509Certificate9publicKeyEv'
    address = self.uglySide.call(ritual)
    return QTlsPrivate.TlsKey._cuteAt(address)

  def numberOfExtensions(self) -> int:
    """
    Calls Qt's 'qsizetype QTlsPrivate::X509Certificate::numberOfExtensions()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtlsprivate-x509certificate.html
    """
    #  qsizetype QTlsPrivate::X509Certificate::numberOfExtensions() const
    return self.uglySide.call(
        'ritual_ZNK11QTlsPrivate15X509Certificate18numberOfExtensionsEv',
    )

  @overload(int)
  def oidForExtension(self, i: int) -> str:
    """
    Calls Qt's 'QString
    QTlsPrivate::X509Certificate::oidForExtension(qsizetype i) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtlsprivate-x509certificate.html#oidForExtension

    Parameters
    ----------

    i : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QTlsPrivate::X509Certificate::oidForExtension(qsizetype i)
    #      const
    return self.uglySide.call(
        'ritual_ZNK11QTlsPrivate15X509Certificate15oidForExtensionEx', i,
    )

  @overload(int)
  def nameForExtension(self, i: int) -> str:
    """
    Calls Qt's 'QString
    QTlsPrivate::X509Certificate::nameForExtension(qsizetype i) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtlsprivate-x509certificate.html#nameForExtension

    Parameters
    ----------

    i : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QTlsPrivate::X509Certificate::nameForExtension(qsizetype i)
    #      const
    return self.uglySide.call(
        'ritual_ZNK11QTlsPrivate15X509Certificate16nameForExtensionEx', i,
    )

  @overload(int)
  def valueForExtension(self, i: int) -> QVariant:
    """
    Calls Qt's 'QVariant
    QTlsPrivate::X509Certificate::valueForExtension(qsizetype i) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtlsprivate-x509certificate.html#valueForExtension

    Parameters
    ----------

    i : int
      Passed on as it is.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QTlsPrivate::X509Certificate::valueForExtension(qsizetype i)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK11QTlsPrivate15X509Certificate17valueForExtensionEx', i,
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(int)
  def isExtensionCritical(self, i: int) -> bool:
    """
    Calls Qt's 'bool
    QTlsPrivate::X509Certificate::isExtensionCritical(qsizetype i) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtlsprivate-x509certificate.html

    Parameters
    ----------

    i : int
      Passed on as it is.
    """
    #  bool QTlsPrivate::X509Certificate::isExtensionCritical(qsizetype i)
    #      const
    return self.uglySide.call(
        'ritual_ZNK11QTlsPrivate15X509Certificate19isExtensionCriticalEx', i,
    )

  @overload(int)
  def isExtensionSupported(self, i: int) -> bool:
    """
    Calls Qt's 'bool
    QTlsPrivate::X509Certificate::isExtensionSupported(qsizetype i) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtlsprivate-x509certificate.html

    Parameters
    ----------

    i : int
      Passed on as it is.
    """
    #  bool QTlsPrivate::X509Certificate::isExtensionSupported(qsizetype i)
    #      const
    return self.uglySide.call(
        'ritual_ZNK11QTlsPrivate15X509Certificate20isExtensionSupportedEx',
        i,
    )

  def toPem(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QTlsPrivate::X509Certificate::toPem() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtlsprivate-x509certificate.html#toPem

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QTlsPrivate::X509Certificate::toPem() const
    address = self.uglySide.call(
        'ritual_ZNK11QTlsPrivate15X509Certificate5toPemEv',
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def toDer(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QTlsPrivate::X509Certificate::toDer() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtlsprivate-x509certificate.html#toDer

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QTlsPrivate::X509Certificate::toDer() const
    address = self.uglySide.call(
        'ritual_ZNK11QTlsPrivate15X509Certificate5toDerEv',
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def toText(self) -> str:
    """
    Calls Qt's 'QString QTlsPrivate::X509Certificate::toText() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtlsprivate-x509certificate.html#toText

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QTlsPrivate::X509Certificate::toText() const
    return self.uglySide.call(
        'ritual_ZNK11QTlsPrivate15X509Certificate6toTextEv',
    )

  @overload(int)
  def hash(self, seed: int) -> int:
    """
    Calls Qt's 'size_t QTlsPrivate::X509Certificate::hash(size_t seed)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtlsprivate-x509certificate.html#hash

    Parameters
    ----------

    seed : int
      Passed on as it is.
    """
    #  size_t QTlsPrivate::X509Certificate::hash(size_t seed) const
    return self.uglySide.call(
        'ritual_ZNK11QTlsPrivate15X509Certificate4hashEm', seed,
    )

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
  def handle(*__, **_) -> Never:
    """
    Qt's 'Qt::HANDLE QTlsPrivate::X509Certificate::handle() const': gives
    'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QTlsPrivate.X509Certificate.handle' has no cute function yet. "
        "Qt's 'Qt::HANDLE QTlsPrivate::X509Certificate::handle() const': "
        "gives 'void', which has no cute class yet.")

  @staticmethod
  def isEqual(*__, **_) -> Never:
    """
    Qt's 'bool QTlsPrivate::X509Certificate::isEqual(const X509Certificate
    &other) const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QTlsPrivate.X509Certificate.isEqual' has no cute function yet. "
        "Qt's 'bool QTlsPrivate::X509Certificate::isEqual(const "
        "X509Certificate &other) const': takes a type Python has no way to "
        "hand over yet.")

  @staticmethod
  def subjectAlternativeNames(*__, **_) -> Never:
    """
    Qt's 'QMultiMap<QSsl::AlternativeNameEntryType, QString>
    QTlsPrivate::X509Certificate::subjectAlternativeNames() const': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QTlsPrivate.X509Certificate.subjectAlternativeNames' has no cute "
        "function yet. Qt's 'QMultiMap<QSsl::AlternativeNameEntryType, "
        "QString> QTlsPrivate::X509Certificate::subjectAlternativeNames() "
        "const': gives a type Python has no way to take yet.")
