"""
QQmlPrivate::AOTLookupValidation::Type binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/qqmlprivate.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals


class Type(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlPrivate::AOTLookupValidation::Type: a plain
  Python object standing in front of one C++
  QQmlPrivate::AOTLookupValidation::Type.

  C++ hands a QQmlPrivate::AOTLookupValidation::Type around as a copy, so
  every C++ QQmlPrivate::AOTLookupValidation::Type behind a cute one is
  Python's own: it is removed, by the ritual named in '__delete_ritual__',
  when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQmlPrivate::AOTLookupValidation::Type that has a
  ritual and that Python can call so far, 2 names in all: '__eq__', '__ne__'.
  None can be made from Python: one comes out of a function of another class
  that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQmlPrivate::AOTLookupValidation::Type::~Type()': the destructor:
    Python removes its C++ QQmlPrivate::AOTLookupValidation::Type by it, and
    has no other use for it.

  What to expect
  --------------

  - The C++ QQmlPrivate::AOTLookupValidation::Type is created at the first
    use, not by 'QQmlPrivate::AOTLookupValidation::Type(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlPrivate::AOTLookupValidation::Type back gives a
    copy the ritual made for Python, in a new cute
    QQmlPrivate::AOTLookupValidation::Type.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlPrivate::AOTLookupValidation::Type'

  #  Qt's '~QQmlPrivate::AOTLookupValidation::Type()'. Naming it makes this a
  #  value class: Python owns every C++
  #  QQmlPrivate::AOTLookupValidation::Type behind a cute one, and removes it
  #  by this ritual.
  __delete_ritual__ = 'ritual_ZN11QQmlPrivate19AOTLookupValidation4TypeD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
  def __eq__(self, rhs: Type) -> bool:
    """
    Calls Qt's 'bool operator==(const Type &lhs, const Type &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlprivate-aotlookupvalidation-type.html

    Parameters
    ----------

    rhs : Type
      Passed on as a value: Qt reads the C++
      QQmlPrivate::AOTLookupValidation::Type, which stays Python's own.
    """
    #  bool operator==(const Type &lhs, const Type &rhs)
    return Rituals.call(
        'ritual_ZN11QQmlPrivate19AOTLookupValidationeqERKNS0_4TypeES3_',
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
  def __ne__(self, rhs: Type) -> bool:
    """
    Calls Qt's 'bool operator!=(const Type &lhs, const Type &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlprivate-aotlookupvalidation-type.html

    Parameters
    ----------

    rhs : Type
      Passed on as a value: Qt reads the C++
      QQmlPrivate::AOTLookupValidation::Type, which stays Python's own.
    """
    #  bool operator!=(const Type &lhs, const Type &rhs)
    return Rituals.call(
        'ritual_ZN11QQmlPrivate19AOTLookupValidationneERKNS0_4TypeES3_',
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
