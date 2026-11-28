"""
QV4::ScopedPropertyKey binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4scopedvalue_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QV4::ScopedPropertyKey to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from . import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class ScopedPropertyKey(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QV4::ScopedPropertyKey: a plain Python object
  standing in front of one C++ QV4::ScopedPropertyKey.

  C++ hands a QV4::ScopedPropertyKey around as a copy, so every C++
  QV4::ScopedPropertyKey behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QV4::ScopedPropertyKey that has a ritual and that
  Python can call so far, 2 names in all: '__eq__', '__ne__'. None can be
  made from Python: one comes out of a function of another class that gives
  one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QV4::ScopedPropertyKey::ScopedPropertyKey(const Scope &scope)':
    takes a type Python has no way to hand over yet.
  - Qt's 'QV4::ScopedPropertyKey::ScopedPropertyKey(const Scope &scope, const
    PropertyKey &v)': takes a type Python has no way to hand over yet.
  - Qt's 'ScopedPropertyKey &QV4::ScopedPropertyKey::operator=(const
    PropertyKey &other)': assignment: Python binds a name and has no operator
    for it.
  - Qt's 'PropertyKey *QV4::ScopedPropertyKey::operator->()': an operator
    Python has no name for.
  - Qt's 'PropertyKey QV4::ScopedPropertyKey::operator PropertyKey() const':
    an operator Python has no name for.
  - Qt's 'QV4::ScopedPropertyKey::~ScopedPropertyKey()': the destructor:
    Python removes its C++ QV4::ScopedPropertyKey by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QV4::ScopedPropertyKey is created at the first use, not by
    'QV4::ScopedPropertyKey(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QV4::ScopedPropertyKey back gives a copy the ritual
    made for Python, in a new cute QV4::ScopedPropertyKey.
  - Each name of Qt's QV4::ScopedPropertyKey that has no cute function yet,
    '__init__', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::ScopedPropertyKey'

  #  Qt's '~QV4::ScopedPropertyKey()'. Naming it makes this a value class:
  #  Python owns every C++ QV4::ScopedPropertyKey behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN3QV417ScopedPropertyKeyD1Ev'

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

  @overload(WAIT['QV4.PropertyKey'])
  def __eq__(self, other: QV4.PropertyKey) -> bool:
    """
    Calls Qt's 'bool QV4::ScopedPropertyKey::operator==(const PropertyKey
    &other) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-scopedpropertykey.html#operator==

    Parameters
    ----------

    other : QV4.PropertyKey
      Passed on as a value: Qt reads the C++ QV4::PropertyKey, which stays
      Python's own.
    """
    #  bool QV4::ScopedPropertyKey::operator==(const PropertyKey &other)
    #      const
    return self.uglySide.call(
        'ritual_ZNK3QV417ScopedPropertyKeyeqERKNS_11PropertyKeyE',
        self._valueOf(other),
    )

  @overload(THIS)
  def __eq__(self, other: ScopedPropertyKey) -> bool:
    """
    Calls Qt's 'bool QV4::ScopedPropertyKey::operator==(const
    ScopedPropertyKey &other) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-scopedpropertykey.html#operator==

    Parameters
    ----------

    other : ScopedPropertyKey
      Passed on as a value: Qt reads the C++ QV4::ScopedPropertyKey, which
      stays Python's own.
    """
    #  bool QV4::ScopedPropertyKey::operator==(const ScopedPropertyKey
    #      &other) const
    return self.uglySide.call(
        'ritual_ZNK3QV417ScopedPropertyKeyeqERKS0_', self._valueOf(other),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(WAIT['QV4.PropertyKey'])
  def __ne__(self, other: QV4.PropertyKey) -> bool:
    """
    Calls Qt's 'bool QV4::ScopedPropertyKey::operator!=(const PropertyKey
    &other) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-scopedpropertykey.html#operator!=

    Parameters
    ----------

    other : QV4.PropertyKey
      Passed on as a value: Qt reads the C++ QV4::PropertyKey, which stays
      Python's own.
    """
    #  bool QV4::ScopedPropertyKey::operator!=(const PropertyKey &other)
    #      const
    return self.uglySide.call(
        'ritual_ZNK3QV417ScopedPropertyKeyneERKNS_11PropertyKeyE',
        self._valueOf(other),
    )

  @overload(THIS)
  def __ne__(self, other: ScopedPropertyKey) -> bool:
    """
    Calls Qt's 'bool QV4::ScopedPropertyKey::operator!=(const
    ScopedPropertyKey &other) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-scopedpropertykey.html#operator!=

    Parameters
    ----------

    other : ScopedPropertyKey
      Passed on as a value: Qt reads the C++ QV4::ScopedPropertyKey, which
      stays Python's own.
    """
    #  bool QV4::ScopedPropertyKey::operator!=(const ScopedPropertyKey
    #      &other) const
    return self.uglySide.call(
        'ritual_ZNK3QV417ScopedPropertyKeyneERKS0_', self._valueOf(other),
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    - Qt's 'QV4::ScopedPropertyKey::ScopedPropertyKey(const Scope &scope)':
      takes a type Python has no way to hand over yet.
    - Qt's 'QV4::ScopedPropertyKey::ScopedPropertyKey(const Scope &scope,
      const PropertyKey &v)': takes a type Python has no way to hand over
      yet.
    """
    raise NotImplementedError(
        "'QV4.ScopedPropertyKey.__init__' has no cute function yet. Qt's "
        "'QV4::ScopedPropertyKey::ScopedPropertyKey(const Scope &scope)': "
        "takes a type Python has no way to hand over yet. Qt's "
        "'QV4::ScopedPropertyKey::ScopedPropertyKey(const Scope &scope, "
        "const PropertyKey &v)': takes a type Python has no way to hand "
        "over yet.")

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
