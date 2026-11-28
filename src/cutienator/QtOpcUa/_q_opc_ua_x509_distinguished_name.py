"""
QOpcUaX509DistinguishedName binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtOpcUa/qopcuax509distinguishedname.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute
from ..occult import Rituals


class QOpcUaX509DistinguishedName(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QOpcUaX509DistinguishedName: a plain Python object
  standing in front of one C++ QOpcUaX509DistinguishedName.

  C++ hands a QOpcUaX509DistinguishedName around as a copy, so every C++
  QOpcUaX509DistinguishedName behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QOpcUaX509DistinguishedName that has a ritual and
  that Python can call so far, 4 names in all: '__eq__', 'setEntry', 'entry',
  'typeToOid'. It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QOpcUaX509DistinguishedName
    &QOpcUaX509DistinguishedName::operator=(const QOpcUaX509DistinguishedName
    &a0)': assignment: Python binds a name and has no operator for it.
  - Qt's 'QOpcUaX509DistinguishedName::~QOpcUaX509DistinguishedName()': the
    destructor: Python removes its C++ QOpcUaX509DistinguishedName by it, and
    has no other use for it.

  What to expect
  --------------

  - The C++ QOpcUaX509DistinguishedName is created at the first use, not by
    'QOpcUaX509DistinguishedName(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QOpcUaX509DistinguishedName back gives a copy the
    ritual made for Python, in a new cute QOpcUaX509DistinguishedName.
  """

  #  The enums Qt writes inside QOpcUaX509DistinguishedName, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class Type(CuteNum, scoped=True):
    """
    The enum 'QOpcUaX509DistinguishedName::Type' of Qt, with the 5 names Qt
    gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    CommonName = Kee[int](0)
    CountryName = Kee[int](1)
    LocalityName = Kee[int](2)
    StateOrProvinceName = Kee[int](3)
    OrganizationName = Kee[int](4)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(Type)
  def typeToOid(type: Type) -> str:
    """
    Calls Qt's 'QString QOpcUaX509DistinguishedName::typeToOid(Type type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuax509distinguishedname.html#typeToOid

    Parameters
    ----------

    type : Type
      Passed on as its number.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QOpcUaX509DistinguishedName::typeToOid(Type type)
    return Rituals.call(
        'ritual_ZN27QOpcUaX509DistinguishedName9typeToOidENS_4TypeE',
        type.value,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOpcUaX509DistinguishedName'

  #  Qt's '~QOpcUaX509DistinguishedName()'. Naming it makes this a value
  #  class: Python owns every C++ QOpcUaX509DistinguishedName behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN27QOpcUaX509DistinguishedNameD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Type)
  def entry(self, type: Type) -> str:
    """
    Calls Qt's 'QString QOpcUaX509DistinguishedName::entry(Type type) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuax509distinguishedname.html#entry

    Parameters
    ----------

    type : Type
      Passed on as its number.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QOpcUaX509DistinguishedName::entry(Type type) const
    return self.uglySide.call(
        'ritual_ZNK27QOpcUaX509DistinguishedName5entryENS_4TypeE',
        type.value,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Type, str)
  def setEntry(self, type: Type, value: str) -> None:
    """
    Calls Qt's 'void QOpcUaX509DistinguishedName::setEntry(Type type, const
    QString &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuax509distinguishedname.html#setEntry

    Parameters
    ----------

    type : Type
      Passed on as its number.

    value : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QOpcUaX509DistinguishedName::setEntry(Type type, const QString
    #      &value)
    self.uglySide.call(
        'ritual_ZN27QOpcUaX509DistinguishedName8setEntryENS_4TypeERK7QStrin'
        'g',
        type.value, value,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, rhs: QOpcUaX509DistinguishedName) -> bool:
    """
    Calls Qt's 'bool QOpcUaX509DistinguishedName::operator==(const
    QOpcUaX509DistinguishedName &rhs) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuax509distinguishedname.html#operator==

    Parameters
    ----------

    rhs : QOpcUaX509DistinguishedName
      Passed on as a value: Qt reads the C++ QOpcUaX509DistinguishedName,
      which stays Python's own.
    """
    #  bool QOpcUaX509DistinguishedName::operator==(const
    #      QOpcUaX509DistinguishedName &rhs) const
    return self.uglySide.call(
        'ritual_ZNK27QOpcUaX509DistinguishedNameeqERKS_', self._valueOf(rhs),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
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
    'QOpcUaX509DistinguishedName::QOpcUaX509DistinguishedName()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuax509distinguishedname.html
    """
    #  QOpcUaX509DistinguishedName::QOpcUaX509DistinguishedName()
    self._noteCreation(QOpcUaX509DistinguishedName, lambda: Rituals.call(
        'ritual_ZN27QOpcUaX509DistinguishedNameC1Ev',
    ))

  @overload(THIS)
  def __init__(self, a0: QOpcUaX509DistinguishedName) -> None:
    """
    Notes what was given, for Qt's
    'QOpcUaX509DistinguishedName::QOpcUaX509DistinguishedName(const
    QOpcUaX509DistinguishedName &a0)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuax509distinguishedname.html

    Parameters
    ----------

    a0 : QOpcUaX509DistinguishedName
      Passed on as a value: Qt reads the C++ QOpcUaX509DistinguishedName,
      which stays Python's own.
    """
    #  QOpcUaX509DistinguishedName::QOpcUaX509DistinguishedName(const
    #      QOpcUaX509DistinguishedName &a0)
    self._noteCreation(QOpcUaX509DistinguishedName, lambda: Rituals.call(
        'ritual_ZN27QOpcUaX509DistinguishedNameC1ERKS_', self._valueOf(a0),
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
