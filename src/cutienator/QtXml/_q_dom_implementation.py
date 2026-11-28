"""
QDomImplementation binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of QtXml/qdom.h, Qt
#  6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QDomDocument, QDomDocumentType, QDomImplementationPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDomDocumentType = WAIT['QDomDocumentType']
  QDomImplementationPrivate = WAIT['QDomImplementationPrivate']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDomImplementation(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QDomImplementation: a plain Python object standing in
  front of one C++ QDomImplementation.

  C++ hands a QDomImplementation around as a copy, so every C++
  QDomImplementation behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QDomImplementation that has a ritual and that Python
  can call so far, 8 names in all: '__eq__', '__ne__', 'hasFeature',
  'createDocumentType', 'createDocument', 'invalidDataPolicy',
  'setInvalidDataPolicy', 'isNull'. It can be made from Python, in 3 ways;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QDomImplementation::~QDomImplementation()': the destructor: Python
    removes its C++ QDomImplementation by it, and has no other use for it.
  - Qt's 'QDomImplementation &QDomImplementation::operator=(const
    QDomImplementation &other)': assignment: Python binds a name and has no
    operator for it.

  What to expect
  --------------

  - The C++ QDomImplementation is created at the first use, not by
    'QDomImplementation(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QDomImplementation back gives a copy the ritual made
    for Python, in a new cute QDomImplementation.
  """

  #  The enums Qt writes inside QDomImplementation, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class InvalidDataPolicy(CuteNum):
    """
    The enum 'QDomImplementation::InvalidDataPolicy' of Qt, with the 3 names
    Qt gives in it.
    """

    AcceptInvalidChars = Kee[int](0)
    DropInvalidChars = Kee[int](1)
    ReturnNullNode = Kee[int](2)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def invalidDataPolicy() -> InvalidDataPolicy:
    """
    Calls Qt's 'InvalidDataPolicy QDomImplementation::invalidDataPolicy()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdomimplementation.html#invalidDataPolicy

    Returns
    -------

    InvalidDataPolicy
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'InvalidDataPolicy(number)' gives.
    """
    #  InvalidDataPolicy QDomImplementation::invalidDataPolicy()
    return QDomImplementation.InvalidDataPolicy(Rituals.call(
        'ritual_ZN18QDomImplementation17invalidDataPolicyEv',
    ))

  @staticmethod
  @overload(InvalidDataPolicy)
  def setInvalidDataPolicy(policy: InvalidDataPolicy) -> None:
    """
    Calls Qt's 'void
    QDomImplementation::setInvalidDataPolicy(InvalidDataPolicy policy)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdomimplementation.html#setInvalidDataPolicy

    Parameters
    ----------

    policy : InvalidDataPolicy
      Passed on as its number.
    """
    #  void QDomImplementation::setInvalidDataPolicy(InvalidDataPolicy
    #      policy)
    Rituals.call(
        'ritual_ZN18QDomImplementation20setInvalidDataPolicyENS_17InvalidDa'
        'taPolicyE',
        policy.value,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDomImplementation'

  #  Qt's '~QDomImplementation()'. Naming it makes this a value class: Python
  #  owns every C++ QDomImplementation behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN18QDomImplementationD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str, str)
  def hasFeature(self, feature: str, version: str) -> bool:
    """
    Calls Qt's 'bool QDomImplementation::hasFeature(const QString &feature,
    const QString &version) const'.

    Qt's own words: https://doc.qt.io/qt-6/qdomimplementation.html#hasFeature

    Parameters
    ----------

    feature : str
      Passed on as it is: a QString is made of it for the call.

    version : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QDomImplementation::hasFeature(const QString &feature, const
    #      QString &version) const
    return self.uglySide.call(
        'ritual_ZNK18QDomImplementation10hasFeatureERK7QStringS2_',
        feature, version,
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
  def __eq__(self, other: QDomImplementation) -> bool:
    """
    Calls Qt's 'bool QDomImplementation::operator==(const QDomImplementation
    &other) const'.

    Qt's own words: https://doc.qt.io/qt-6/qdomimplementation.html#operator==

    Parameters
    ----------

    other : QDomImplementation
      Passed on as a value: Qt reads the C++ QDomImplementation, which stays
      Python's own.
    """
    #  bool QDomImplementation::operator==(const QDomImplementation &other)
    #      const
    return self.uglySide.call(
        'ritual_ZNK18QDomImplementationeqERKS_', self._valueOf(other),
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
  def __ne__(self, other: QDomImplementation) -> bool:
    """
    Calls Qt's 'bool QDomImplementation::operator!=(const QDomImplementation
    &other) const'.

    Qt's own words: https://doc.qt.io/qt-6/qdomimplementation.html#operator!=

    Parameters
    ----------

    other : QDomImplementation
      Passed on as a value: Qt reads the C++ QDomImplementation, which stays
      Python's own.
    """
    #  bool QDomImplementation::operator!=(const QDomImplementation &other)
    #      const
    return self.uglySide.call(
        'ritual_ZNK18QDomImplementationneERKS_', self._valueOf(other),
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
    Notes what was given, for Qt's
    'QDomImplementation::QDomImplementation()', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdomimplementation.html#QDomImplementation
    """
    #  QDomImplementation::QDomImplementation()
    self._noteCreation(QDomImplementation, lambda: Rituals.call(
        'ritual_ZN18QDomImplementationC1Ev',
    ))

  @overload(THIS)
  def __init__(self, implementation: QDomImplementation) -> None:
    """
    Notes what was given, for Qt's
    'QDomImplementation::QDomImplementation(const QDomImplementation
    &implementation)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdomimplementation.html#QDomImplementation

    Parameters
    ----------

    implementation : QDomImplementation
      Passed on as a value: Qt reads the C++ QDomImplementation, which stays
      Python's own.
    """
    #  QDomImplementation::QDomImplementation(const QDomImplementation
    #      &implementation)
    self._noteCreation(QDomImplementation, lambda: Rituals.call(
        'ritual_ZN18QDomImplementationC1ERKS_',
        self._valueOf(implementation),
    ))

  @overload(QDomImplementationPrivate)
  @overload(NoneType)
  def __init__(self, a0: Optional[QDomImplementationPrivate]) -> None:
    """
    Notes what was given, for Qt's
    'QDomImplementation::QDomImplementation(QDomImplementationPrivate *a0)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdomimplementation.html#QDomImplementation

    Parameters
    ----------

    a0 : Optional[QDomImplementationPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QDomImplementation::QDomImplementation(QDomImplementationPrivate *a0)
    self._noteCreation(QDomImplementation, lambda: Rituals.call(
        'ritual_ZN18QDomImplementationC1EP25QDomImplementationPrivate',
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

  @overload(str, str, str)
  def createDocumentType(
      self,
      qName: str,
      publicId: str,
      systemId: str,
  ) -> QDomDocumentType:
    """
    Calls Qt's 'QDomDocumentType QDomImplementation::createDocumentType(const
    QString &qName, const QString &publicId, const QString &systemId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdomimplementation.html#createDocumentType

    Parameters
    ----------

    qName : str
      Passed on as it is: a QString is made of it for the call.

    publicId : str
      Passed on as it is: a QString is made of it for the call.

    systemId : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QDomDocumentType
      A new cute QDomDocumentType around the copy Qt gave back. Python owns
      it.
    """
    #  QDomDocumentType QDomImplementation::createDocumentType(const QString
    #      &qName, const QString &publicId, const QString &systemId)
    address = self.uglySide.call(
        'ritual_ZN18QDomImplementation18createDocumentTypeERK7QStringS2_S2_',
        qName, publicId, systemId,
    )
    from . import QDomDocumentType
    return QDomDocumentType._cuteOwning(address)

  @overload(str, str, QDomDocumentType)
  def createDocument(
      self,
      nsURI: str,
      qName: str,
      doctype: QDomDocumentType,
  ) -> QDomDocument:
    """
    Calls Qt's 'QDomDocument QDomImplementation::createDocument(const QString
    &nsURI, const QString &qName, const QDomDocumentType &doctype)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdomimplementation.html#createDocument

    Parameters
    ----------

    nsURI : str
      Passed on as it is: a QString is made of it for the call.

    qName : str
      Passed on as it is: a QString is made of it for the call.

    doctype : QDomDocumentType
      Passed on as a value: Qt reads the C++ QDomDocumentType, which stays
      Python's own.

    Returns
    -------

    QDomDocument
      A new cute QDomDocument around the copy Qt gave back. Python owns it.
    """
    #  QDomDocument QDomImplementation::createDocument(const QString &nsURI,
    #      const QString &qName, const QDomDocumentType &doctype)
    address = self.uglySide.call(
        'ritual_ZN18QDomImplementation14createDocumentERK7QStringS2_RK16QDo'
        'mDocumentType',
        nsURI, qName, self._valueOf(doctype),
    )
    from . import QDomDocument
    return QDomDocument._cuteOwning(address)

  def isNull(self) -> bool:
    """
    Calls Qt's 'bool QDomImplementation::isNull()'.

    Qt's own words: https://doc.qt.io/qt-6/qdomimplementation.html#isNull
    """
    #  bool QDomImplementation::isNull()
    return self.uglySide.call('ritual_ZN18QDomImplementation6isNullEv')
