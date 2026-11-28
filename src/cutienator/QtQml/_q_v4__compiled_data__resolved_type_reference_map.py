"""
QV4::CompiledData::ResolvedTypeReferenceMap binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4compileddata_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QV4::CompiledData::ResolvedTypeReferenceMap to be private: it
#  declares the class in a header it calls private. cutienator does not care.
#  Qt hands objects of the class out all the same, and a class we are handed
#  is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..cute import CuteMixin, MetaCute

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class ResolvedTypeReferenceMap(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QV4::CompiledData::ResolvedTypeReferenceMap: a plain
  Python object standing in front of one C++
  QV4::CompiledData::ResolvedTypeReferenceMap.

  C++ hands a QV4::CompiledData::ResolvedTypeReferenceMap around as a copy,
  so every C++ QV4::CompiledData::ResolvedTypeReferenceMap behind a cute one
  is Python's own: it is removed, by the ritual named in '__delete_ritual__',
  when the cute object goes.

  What exists
  -----------

  No function of Qt's QV4::CompiledData::ResolvedTypeReferenceMap yet. None
  can be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'bool
    QV4::CompiledData::ResolvedTypeReferenceMap::addToHash(QCryptographicHash
    *hash, QHash<quintptr, QByteArray> *checksums) const': names
    'QHash<quintptr, QByteArray>', which has no cute class yet.
  - Qt's
    'QV4::CompiledData::ResolvedTypeReferenceMap::~ResolvedTypeReferenceMap(
    )': the destructor: Python removes its C++
    QV4::CompiledData::ResolvedTypeReferenceMap by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QV4::CompiledData::ResolvedTypeReferenceMap is created at the
    first use, not by 'QV4::CompiledData::ResolvedTypeReferenceMap(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QV4::CompiledData::ResolvedTypeReferenceMap back
    gives a copy the ritual made for Python, in a new cute
    QV4::CompiledData::ResolvedTypeReferenceMap.
  - Each name of Qt's QV4::CompiledData::ResolvedTypeReferenceMap that has no
    cute function yet, 'addToHash', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::CompiledData::ResolvedTypeReferenceMap'

  #  Qt's '~QV4::CompiledData::ResolvedTypeReferenceMap()'. Naming it makes
  #  this a value class: Python owns every C++
  #  QV4::CompiledData::ResolvedTypeReferenceMap behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = (
      'ritual_ZN3QV412CompiledData24ResolvedTypeReferenceMapD1Ev')

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
  def addToHash(*__, **_) -> Never:
    """
    Qt's 'bool
    QV4::CompiledData::ResolvedTypeReferenceMap::addToHash(QCryptographicHash
    *hash, QHash<quintptr, QByteArray> *checksums) const': names
    'QHash<quintptr, QByteArray>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QV4.CompiledData.ResolvedTypeReferenceMap.addToHash' has no cute "
        "function yet. Qt's 'bool "
        "QV4::CompiledData::ResolvedTypeReferenceMap::addToHash(QCryptograph"
        "icHash *hash, QHash<quintptr, QByteArray> *checksums) const': "
        "names 'QHash<quintptr, QByteArray>', which has no cute class yet.")
