"""
QDnsTlsAssociationRecord binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/qdnslookup.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute
from ..occult import Rituals
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QByteArray


class QDnsTlsAssociationRecord(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QDnsTlsAssociationRecord: a plain Python object
  standing in front of one C++ QDnsTlsAssociationRecord.

  C++ hands a QDnsTlsAssociationRecord around as a copy, so every C++
  QDnsTlsAssociationRecord behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QDnsTlsAssociationRecord that has a ritual and that
  Python can call so far, 6 names in all: 'name', 'timeToLive', 'usage',
  'selector', 'matchType', 'value'. It can be made from Python, in 2 ways;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QDnsTlsAssociationRecord::QDnsTlsAssociationRecord(
    QDnsTlsAssociationRecord &&other)': takes a type Python has no way to
    hand over yet.
  - Qt's 'QDnsTlsAssociationRecord
    &QDnsTlsAssociationRecord::operator=(QDnsTlsAssociationRecord &&other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'QDnsTlsAssociationRecord &QDnsTlsAssociationRecord::operator=(const
    QDnsTlsAssociationRecord &other)': assignment: Python binds a name and
    has no operator for it.
  - Qt's 'QDnsTlsAssociationRecord::~QDnsTlsAssociationRecord()': the
    destructor: Python removes its C++ QDnsTlsAssociationRecord by it, and
    has no other use for it.
  - Qt's 'void QDnsTlsAssociationRecord::swap(QDnsTlsAssociationRecord
    &other)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  3 of the 16 functions Qt declares: 3 not a gap.

  What to expect
  --------------

  - The C++ QDnsTlsAssociationRecord is created at the first use, not by
    'QDnsTlsAssociationRecord(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QDnsTlsAssociationRecord back gives a copy the ritual
    made for Python, in a new cute QDnsTlsAssociationRecord.
  - Each name of Qt's QDnsTlsAssociationRecord that has no cute function yet,
    'swap', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  #  The enums Qt writes inside QDnsTlsAssociationRecord, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class CertificateUsage(CuteNum, scoped=True):
    """
    The enum 'QDnsTlsAssociationRecord::CertificateUsage' of Qt, with the 10
    names Qt gives in it. C++ keeps these names inside the enum, so the class
    that holds the enum does not have them.
    """

    CertificateAuthorityConstrait = Kee[int](0)
    ServiceCertificateConstraint = Kee[int](1)
    TrustAnchorAssertion = Kee[int](2)
    DomainIssuedCertificate = Kee[int](3)
    PrivateUse = Kee[int](255)
    PKIX_TA = Kee[int](0)
    PKIX_EE = Kee[int](1)
    DANE_TA = Kee[int](2)
    DANE_EE = Kee[int](3)
    PrivCert = Kee[int](255)

  class MatchingType(CuteNum, scoped=True):
    """
    The enum 'QDnsTlsAssociationRecord::MatchingType' of Qt, with the 5 names
    Qt gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    Exact = Kee[int](0)
    Sha256 = Kee[int](1)
    Sha512 = Kee[int](2)
    PrivateUse = Kee[int](255)
    PrivMatch = Kee[int](255)

  class Selector(CuteNum, scoped=True):
    """
    The enum 'QDnsTlsAssociationRecord::Selector' of Qt, with the 6 names Qt
    gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    FullCertificate = Kee[int](0)
    SubjectPublicKeyInfo = Kee[int](1)
    PrivateUse = Kee[int](255)
    Cert = Kee[int](0)
    SPKI = Kee[int](1)
    PrivSel = Kee[int](255)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDnsTlsAssociationRecord'

  #  Qt's '~QDnsTlsAssociationRecord()'. Naming it makes this a value class:
  #  Python owns every C++ QDnsTlsAssociationRecord behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN24QDnsTlsAssociationRecordD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def name(self) -> str:
    """
    Calls Qt's 'QString QDnsTlsAssociationRecord::name() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdnstlsassociationrecord.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDnsTlsAssociationRecord::name() const
    return self.uglySide.call('ritual_ZNK24QDnsTlsAssociationRecord4nameEv')

  def timeToLive(self) -> int:
    """
    Calls Qt's 'quint32 QDnsTlsAssociationRecord::timeToLive() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdnstlsassociationrecord.html#timeToLive
    """
    #  quint32 QDnsTlsAssociationRecord::timeToLive() const
    return self.uglySide.call(
        'ritual_ZNK24QDnsTlsAssociationRecord10timeToLiveEv',
    )

  def usage(self) -> CertificateUsage:
    """
    Calls Qt's 'CertificateUsage QDnsTlsAssociationRecord::usage() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdnstlsassociationrecord.html#usage

    Returns
    -------

    CertificateUsage
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'CertificateUsage(number)'
      gives.
    """
    #  CertificateUsage QDnsTlsAssociationRecord::usage() const
    return QDnsTlsAssociationRecord.CertificateUsage(self.uglySide.call(
        'ritual_ZNK24QDnsTlsAssociationRecord5usageEv',
    ))

  def selector(self) -> Selector:
    """
    Calls Qt's 'Selector QDnsTlsAssociationRecord::selector() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdnstlsassociationrecord.html#selector

    Returns
    -------

    Selector
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Selector(number)' gives.
    """
    #  Selector QDnsTlsAssociationRecord::selector() const
    return QDnsTlsAssociationRecord.Selector(self.uglySide.call(
        'ritual_ZNK24QDnsTlsAssociationRecord8selectorEv',
    ))

  def matchType(self) -> MatchingType:
    """
    Calls Qt's 'MatchingType QDnsTlsAssociationRecord::matchType() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdnstlsassociationrecord.html#matchType

    Returns
    -------

    MatchingType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'MatchingType(number)'
      gives.
    """
    #  MatchingType QDnsTlsAssociationRecord::matchType() const
    return QDnsTlsAssociationRecord.MatchingType(self.uglySide.call(
        'ritual_ZNK24QDnsTlsAssociationRecord9matchTypeEv',
    ))

  def value(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QDnsTlsAssociationRecord::value() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdnstlsassociationrecord.html#value

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QDnsTlsAssociationRecord::value() const
    address = self.uglySide.call(
        'ritual_ZNK24QDnsTlsAssociationRecord5valueEv',
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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QDnsTlsAssociationRecord::QDnsTlsAssociationRecord()', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdnstlsassociationrecord.html
    """
    #  QDnsTlsAssociationRecord::QDnsTlsAssociationRecord()
    self._noteCreation(QDnsTlsAssociationRecord, lambda: Rituals.call(
        'ritual_ZN24QDnsTlsAssociationRecordC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QDnsTlsAssociationRecord) -> None:
    """
    Notes what was given, for Qt's
    'QDnsTlsAssociationRecord::QDnsTlsAssociationRecord(const
    QDnsTlsAssociationRecord &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdnstlsassociationrecord.html

    Parameters
    ----------

    other : QDnsTlsAssociationRecord
      Passed on as a value: Qt reads the C++ QDnsTlsAssociationRecord, which
      stays Python's own.
    """
    #  QDnsTlsAssociationRecord::QDnsTlsAssociationRecord(const
    #      QDnsTlsAssociationRecord &other)
    self._noteCreation(QDnsTlsAssociationRecord, lambda: Rituals.call(
        'ritual_ZN24QDnsTlsAssociationRecordC1ERKS_', self._valueOf(other),
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
    Qt's 'void QDnsTlsAssociationRecord::swap(QDnsTlsAssociationRecord
    &other)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QDnsTlsAssociationRecord.swap' has no cute function yet. Qt's "
        "'void QDnsTlsAssociationRecord::swap(QDnsTlsAssociationRecord "
        "&other)': takes a type Python has no way to hand over yet.")


#  Qt's 'QList<QDnsTlsAssociationRecord>': the list of
#  QDnsTlsAssociationRecord, which 'QList[QDnsTlsAssociationRecord]' gives.
#  It is made here, so that there is one as soon as there can be a
#  QDnsTlsAssociationRecord.
QList.createKind(
    QDnsTlsAssociationRecord, 'value',
    make='ritual_list_make_QDnsTlsAssociationRecord',
    add='ritual_list_add_QDnsTlsAssociationRecord',
    size='ritual_list_size_QDnsTlsAssociationRecord',
    at='ritual_list_at_QDnsTlsAssociationRecord',
    drop='ritual_list_drop_QDnsTlsAssociationRecord',
)
