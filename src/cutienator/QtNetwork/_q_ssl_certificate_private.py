"""
QSslCertificatePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/6.12.0/QtNetwork/private/qsslcertificate_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QSslCertificatePrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals
from ..QtCore import QList
from . import QSslCertificate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QByteArray
  from . import QSslCertificateExtension


class QSslCertificatePrivate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSslCertificatePrivate: a plain Python object
  standing in front of one C++ QSslCertificatePrivate.

  What exists
  -----------

  Every function of Qt's QSslCertificatePrivate that has a ritual and that
  Python can call so far, 3 names in all: 'extensions', 'isBlacklisted',
  'subjectInfoToString'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSslCertificatePrivate::~QSslCertificatePrivate()': the destructor:
    Python never removes a C++ QSslCertificatePrivate.

  What has no ritual
  ------------------

  1 of the 5 functions Qt declares: 1 leans on 'lcSsl()', which Qt's source
  does not mark for use from outside Qt and has no code for that could be
  taken.

  What to expect
  --------------

  - The C++ QSslCertificatePrivate is created at the first use, not by
    'QSslCertificatePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSslCertificatePrivate.
  - Each name of Qt's QSslCertificatePrivate that has no cute function yet,
    '__init__', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QSslCertificate)
  def isBlacklisted(certificate: QSslCertificate) -> bool:
    """
    Calls Qt's 'bool QSslCertificatePrivate::isBlacklisted(const
    QSslCertificate &certificate)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslcertificateprivate.html#isBlacklisted

    Parameters
    ----------

    certificate : QSslCertificate
      Passed on as a value: Qt reads the C++ QSslCertificate, which stays
      Python's own.
    """
    #  bool QSslCertificatePrivate::isBlacklisted(const QSslCertificate
    #      &certificate)
    return Rituals.call(
        'ritual_ZN22QSslCertificatePrivate13isBlacklistedERK15QSslCertifica'
        'te',
        CuteMixin._valueOf(certificate),
    )

  @staticmethod
  @overload(QSslCertificate.SubjectInfo)
  def subjectInfoToString(info: QSslCertificate.SubjectInfo) -> QByteArray:
    """
    Calls Qt's 'QByteArray
    QSslCertificatePrivate::subjectInfoToString(QSslCertificate::SubjectInfo
    info)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslcertificateprivate.html#subjectInfoToString

    Parameters
    ----------

    info : QSslCertificate.SubjectInfo
      Passed on as its number.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray
    #      QSslCertificatePrivate::subjectInfoToString(QSslCertificate::
    #      SubjectInfo info)
    address = Rituals.call(
        'ritual_ZN22QSslCertificatePrivate19subjectInfoToStringEN15QSslCert'
        'ificate11SubjectInfoE',
        info.value,
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSslCertificatePrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def extensions(self) -> QList[QSslCertificateExtension]:
    """
    Calls Qt's 'QList<QSslCertificateExtension>
    QSslCertificatePrivate::extensions() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslcertificateprivate.html#extensions

    Returns
    -------

    QList[QSslCertificateExtension]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QSslCertificateExtension> QSslCertificatePrivate::extensions()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK22QSslCertificatePrivate10extensionsEv',
    )
    from . import QSslCertificateExtension
    return QList[QSslCertificateExtension]._cuteOwning(address)

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
    Qt's 'QSslCertificatePrivate::QSslCertificatePrivate()': leans on
    'lcSsl()', which Qt's source does not mark for use from outside Qt and
    has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QSslCertificatePrivate.__init__' has no cute function yet. Qt's "
        "'QSslCertificatePrivate::QSslCertificatePrivate()': leans on "
        "'lcSsl()', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

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
