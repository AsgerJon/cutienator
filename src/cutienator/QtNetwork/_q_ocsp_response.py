"""
QOcspResponse binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/qocspresponse.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from . import QSslCertificate


class QOcspResponse(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QOcspResponse: a plain Python object standing in
  front of one C++ QOcspResponse.

  C++ hands a QOcspResponse around as a copy, so every C++ QOcspResponse
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QOcspResponse that has a ritual and that Python can
  call so far, 4 names in all: 'subject', 'isEqual', '__eq__', '__ne__'. It
  can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QOcspResponse::QOcspResponse(QOcspResponse &&other)': takes a type
    Python has no way to hand over yet.
  - Qt's 'QOcspResponse::~QOcspResponse()': the destructor: Python removes
    its C++ QOcspResponse by it, and has no other use for it.
  - Qt's 'QOcspResponse &QOcspResponse::operator=(const QOcspResponse
    &other)': assignment: Python binds a name and has no operator for it.
  - Qt's 'QOcspResponse &QOcspResponse::operator=(QOcspResponse &&other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'QOcspCertificateStatus QOcspResponse::certificateStatus() const':
    gives the enum 'QOcspCertificateStatus', whose class cannot be named
    here.
  - Qt's 'QOcspRevocationReason QOcspResponse::revocationReason() const':
    gives the enum 'QOcspRevocationReason', whose class cannot be named here.
  - Qt's 'class QSslCertificate QOcspResponse::responder() const': gives a
    type Python has no way to take yet.
  - Qt's 'void QOcspResponse::swap(QOcspResponse &other)': takes a type
    Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ QOcspResponse is created at the first use, not by
    'QOcspResponse(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QOcspResponse back gives a copy the ritual made for
    Python, in a new cute QOcspResponse.
  - Each name of Qt's QOcspResponse that has no cute function yet,
    'certificateStatus', 'responder', 'revocationReason', 'swap', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOcspResponse'

  #  Qt's '~QOcspResponse()'. Naming it makes this a value class: Python owns
  #  every C++ QOcspResponse behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN13QOcspResponseD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def subject(self) -> QSslCertificate:
    """
    Calls Qt's 'QSslCertificate QOcspResponse::subject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qocspresponse.html#subject

    Returns
    -------

    QSslCertificate
      A new cute QSslCertificate around the copy Qt gave back. Python owns
      it.
    """
    #  QSslCertificate QOcspResponse::subject() const
    address = self.uglySide.call('ritual_ZNK13QOcspResponse7subjectEv')
    from . import QSslCertificate
    return QSslCertificate._cuteOwning(address)

  @overload(THIS)
  def isEqual(self, other: QOcspResponse) -> bool:
    """
    Calls Qt's 'bool QOcspResponse::isEqual(const QOcspResponse &other)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qocspresponse.html#isEqual

    Parameters
    ----------

    other : QOcspResponse
      Passed on as a value: Qt reads the C++ QOcspResponse, which stays
      Python's own.
    """
    #  bool QOcspResponse::isEqual(const QOcspResponse &other) const
    return self.uglySide.call(
        'ritual_ZNK13QOcspResponse7isEqualERKS_', self._valueOf(other),
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

  @overload(THIS)
  def __eq__(self, rhs: QOcspResponse) -> bool:
    """
    Calls Qt's 'bool operator==(const QOcspResponse &lhs, const QOcspResponse
    &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qocspresponse.html#operator==

    Parameters
    ----------

    rhs : QOcspResponse
      Passed on as a value: Qt reads the C++ QOcspResponse, which stays
      Python's own.
    """
    #  bool operator==(const QOcspResponse &lhs, const QOcspResponse &rhs)
    return Rituals.call(
        'ritual_ZeqRK13QOcspResponseS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
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
  def __ne__(self, rhs: QOcspResponse) -> bool:
    """
    Calls Qt's 'bool operator!=(const QOcspResponse &lhs, const QOcspResponse
    &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qocspresponse.html#operator!=

    Parameters
    ----------

    rhs : QOcspResponse
      Passed on as a value: Qt reads the C++ QOcspResponse, which stays
      Python's own.
    """
    #  bool operator!=(const QOcspResponse &lhs, const QOcspResponse &rhs)
    return Rituals.call(
        'ritual_ZneRK13QOcspResponseS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
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
    Notes what was given, for Qt's 'QOcspResponse::QOcspResponse()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qocspresponse.html#QOcspResponse
    """
    #  QOcspResponse::QOcspResponse()
    self._noteCreation(QOcspResponse, lambda: Rituals.call(
        'ritual_ZN13QOcspResponseC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QOcspResponse) -> None:
    """
    Notes what was given, for Qt's 'QOcspResponse::QOcspResponse(const
    QOcspResponse &other)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qocspresponse.html#QOcspResponse

    Parameters
    ----------

    other : QOcspResponse
      Passed on as a value: Qt reads the C++ QOcspResponse, which stays
      Python's own.
    """
    #  QOcspResponse::QOcspResponse(const QOcspResponse &other)
    self._noteCreation(QOcspResponse, lambda: Rituals.call(
        'ritual_ZN13QOcspResponseC1ERKS_', self._valueOf(other),
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
  def certificateStatus(*__, **_) -> Never:
    """
    Qt's 'QOcspCertificateStatus QOcspResponse::certificateStatus() const':
    gives the enum 'QOcspCertificateStatus', whose class cannot be named
    here.
    """
    raise NotImplementedError(
        "'QOcspResponse.certificateStatus' has no cute function yet. Qt's "
        "'QOcspCertificateStatus QOcspResponse::certificateStatus() const': "
        "gives the enum 'QOcspCertificateStatus', whose class cannot be "
        "named here.")

  @staticmethod
  def responder(*__, **_) -> Never:
    """
    Qt's 'class QSslCertificate QOcspResponse::responder() const': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QOcspResponse.responder' has no cute function yet. Qt's 'class "
        "QSslCertificate QOcspResponse::responder() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def revocationReason(*__, **_) -> Never:
    """
    Qt's 'QOcspRevocationReason QOcspResponse::revocationReason() const':
    gives the enum 'QOcspRevocationReason', whose class cannot be named here.
    """
    raise NotImplementedError(
        "'QOcspResponse.revocationReason' has no cute function yet. Qt's "
        "'QOcspRevocationReason QOcspResponse::revocationReason() const': "
        "gives the enum 'QOcspRevocationReason', whose class cannot be "
        "named here.")

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QOcspResponse::swap(QOcspResponse &other)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QOcspResponse.swap' has no cute function yet. Qt's 'void "
        "QOcspResponse::swap(QOcspResponse &other)': takes a type Python "
        "has no way to hand over yet.")


#  Qt's 'QList<QOcspResponse>': the list of QOcspResponse, which
#  'QList[QOcspResponse]' gives. It is made here, so that there is one as
#  soon as there can be a QOcspResponse.
QList.createKind(
    QOcspResponse, 'value',
    make='ritual_list_make_QOcspResponse',
    add='ritual_list_add_QOcspResponse',
    size='ritual_list_size_QOcspResponse',
    at='ritual_list_at_QOcspResponse',
    drop='ritual_list_drop_QOcspResponse',
)
