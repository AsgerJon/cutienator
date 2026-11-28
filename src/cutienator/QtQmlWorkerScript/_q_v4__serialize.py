"""
QV4::Serialize binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlWorkerScript/6.12.0/QtQmlWorkerScript/private/qv4serialize_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QV4::Serialize to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..cute import CuteMixin, MetaCute

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class Serialize(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QV4::Serialize: a plain Python object standing in
  front of one C++ QV4::Serialize.

  C++ hands a QV4::Serialize around as a copy, so every C++ QV4::Serialize
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  No function of Qt's QV4::Serialize yet. None can be made from Python: one
  comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QV4::Serialize::~Serialize()': the destructor: Python removes its
    C++ QV4::Serialize by it, and has no other use for it.

  What has no ritual
  ------------------

  4 of the 5 functions Qt declares: 2 leans on 'QV4; 1 takes or gives a type
  that cannot be passed yet; 1 Qt's library has no name for it, and its code
  in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QV4::Serialize is created at the first use, not by
    'QV4::Serialize(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QV4::Serialize back gives a copy the ritual made for
    Python, in a new cute QV4::Serialize.
  - Each name of Qt's QV4::Serialize that has no cute function yet,
    'deserialize', 'serialize', holds a function that raises
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
  __qt_class__ = 'QV4::Serialize'

  #  Qt's '~QV4::Serialize()'. Naming it makes this a value class: Python
  #  owns every C++ QV4::Serialize behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN3QV49SerializeD1Ev'

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
  def deserialize(*__, **_) -> Never:
    """
    - Qt's 'ReturnedValue QV4::Serialize::deserialize(const char *&a0,
      ExecutionEngine *a1)': takes or gives a type that cannot be passed yet:
      const char *&.
    - Qt's 'ReturnedValue QV4::Serialize::deserialize(const QByteArray &a0,
      ExecutionEngine *a1)': leans on 'QV4::Serialize::deserialize(char
      const*&, QV4::ExecutionEngine*)', which Qt's source does not mark for
      use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QV4.Serialize.deserialize' has no cute function yet. Qt's "
        "'ReturnedValue QV4::Serialize::deserialize(const char *&a0, "
        "ExecutionEngine *a1)': takes or gives a type that cannot be passed "
        "yet: const char *&. Qt's 'ReturnedValue "
        "QV4::Serialize::deserialize(const QByteArray &a0, ExecutionEngine "
        "*a1)': leans on 'QV4::Serialize::deserialize(char const*&, "
        "QV4::ExecutionEngine*)', which Qt's source does not mark for use "
        "from outside Qt and has no code for that could be taken.")

  @staticmethod
  def serialize(*__, **_) -> Never:
    """
    - Qt's 'void QV4::Serialize::serialize(QByteArray &a0, const Value &a1,
      ExecutionEngine *a2)': Qt's library has no name for it, and its code in
      Qt's source does not compile apart from its file: use of undeclared
      identifier 'WorkerUndefined'.
    - Qt's 'QByteArray QV4::Serialize::serialize(const Value &a0,
      ExecutionEngine *a1)': leans on 'QV4::Serialize::serialize(QByteArray&,
      QV4::Value const&, QV4::ExecutionEngine*)', which Qt's source does not
      mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QV4.Serialize.serialize' has no cute function yet. Qt's 'void "
        "QV4::Serialize::serialize(QByteArray &a0, const Value &a1, "
        "ExecutionEngine *a2)': Qt's library has no name for it, and its "
        "code in Qt's source does not compile apart from its file: use of "
        "undeclared identifier 'WorkerUndefined'. Qt's 'QByteArray "
        "QV4::Serialize::serialize(const Value &a0, ExecutionEngine *a1)': "
        "leans on 'QV4::Serialize::serialize(QByteArray&, QV4::Value "
        "const&, QV4::ExecutionEngine*)', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")
