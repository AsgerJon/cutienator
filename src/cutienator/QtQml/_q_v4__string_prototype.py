"""
QV4::StringPrototype binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4stringobject_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QV4::StringPrototype to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class StringPrototype(QV4.StringObject):
  """
  The cute side of Qt's QV4::StringPrototype: a plain Python object standing
  in front of one C++ QV4::StringPrototype.

  It is built on the cute 'QV4::StringObject', as Qt's QV4::StringPrototype
  is built on Qt's QV4::StringObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QV4::StringPrototype that has a ritual and that
  Python can call so far, 1 name in all: 'defaultPrototype'. None can be made
  from Python: one comes out of a function of another class that gives one
  back.

  What has no ritual
  ------------------

  29 of the 30 functions Qt declares: 25 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 4 leans on
  'QV4.

  What to expect
  --------------

  - The C++ QV4::StringPrototype is created at the first use, not by
    'QV4::StringPrototype(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QV4::StringPrototype.
  - Each name of Qt's QV4::StringPrototype that has no cute function yet,
    'init', 'method_charAt', 'method_charCodeAt', 'method_codePointAt',
    'method_concat', 'method_endsWith', 'method_includes', 'method_indexOf',
    'method_iterator', 'method_lastIndexOf', 'method_localeCompare',
    'method_match', 'method_normalize', 'method_padEnd', 'method_padStart',
    'method_repeat', 'method_replace', 'method_search', 'method_slice',
    'method_split', 'method_startsWith', 'method_substr', 'method_substring',
    'method_toLocaleLowerCase', 'method_toLocaleUpperCase',
    'method_toLowerCase', 'method_toString', 'method_toUpperCase',
    'method_trim', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(WAIT['QV4.ExecutionEngine'])
  @overload(NoneType)
  def defaultPrototype(
      e: Optional[QV4.ExecutionEngine],
  ) -> Optional[QV4.Object]:
    """
    Calls Qt's 'QV4::Object
    *QV4::StringPrototype::defaultPrototype(QV4::ExecutionEngine *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-stringprototype.html#defaultPrototype

    Parameters
    ----------

    e : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QV4.Object]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::Object
    #      *QV4::StringPrototype::defaultPrototype(QV4::ExecutionEngine *e)
    address = Rituals.call(
        'ritual_ZN3QV415StringPrototype16defaultPrototypeEPNS_15ExecutionEn'
        'gineE',
        CuteMixin._addressOf(e),
    )
    return QV4.Object._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::StringPrototype'

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
  def init(*__, **_) -> Never:
    """
    Qt's 'void QV4::StringPrototype::init(ExecutionEngine *engine, Object
    *ctor)': leans on 'QV4::StringObject::static_vtbl', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QV4.StringPrototype.init' has no cute function yet. Qt's 'void "
        "QV4::StringPrototype::init(ExecutionEngine *engine, Object "
        "*ctor)': leans on 'QV4::StringObject::static_vtbl', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def method_charAt(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::StringPrototype::method_charAt(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier
    'getThisString'.
    """
    raise NotImplementedError(
        "'QV4.StringPrototype.method_charAt' has no cute function yet. Qt's "
        "'ReturnedValue QV4::StringPrototype::method_charAt(const "
        "FunctionObject *a0, const Value *thisObject, const Value *argv, "
        "int argc)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'getThisString'.")

  @staticmethod
  def method_charCodeAt(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::StringPrototype::method_charCodeAt(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier
    'getThisString'.
    """
    raise NotImplementedError(
        "'QV4.StringPrototype.method_charCodeAt' has no cute function yet. "
        "Qt's 'ReturnedValue QV4::StringPrototype::method_charCodeAt(const "
        "FunctionObject *a0, const Value *thisObject, const Value *argv, "
        "int argc)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'getThisString'.")

  @staticmethod
  def method_codePointAt(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::StringPrototype::method_codePointAt(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier
    'getThisString'.
    """
    raise NotImplementedError(
        "'QV4.StringPrototype.method_codePointAt' has no cute function yet. "
        "Qt's 'ReturnedValue QV4::StringPrototype::method_codePointAt(const "
        "FunctionObject *a0, const Value *thisObject, const Value *argv, "
        "int argc)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'getThisString'.")

  @staticmethod
  def method_concat(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::StringPrototype::method_concat(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier
    'getThisString'.
    """
    raise NotImplementedError(
        "'QV4.StringPrototype.method_concat' has no cute function yet. Qt's "
        "'ReturnedValue QV4::StringPrototype::method_concat(const "
        "FunctionObject *a0, const Value *thisObject, const Value *argv, "
        "int argc)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'getThisString'.")

  @staticmethod
  def method_endsWith(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::StringPrototype::method_endsWith(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier
    'getThisString'.
    """
    raise NotImplementedError(
        "'QV4.StringPrototype.method_endsWith' has no cute function yet. "
        "Qt's 'ReturnedValue QV4::StringPrototype::method_endsWith(const "
        "FunctionObject *a0, const Value *thisObject, const Value *argv, "
        "int argc)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'getThisString'.")

  @staticmethod
  def method_includes(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::StringPrototype::method_includes(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier
    'getThisString'.
    """
    raise NotImplementedError(
        "'QV4.StringPrototype.method_includes' has no cute function yet. "
        "Qt's 'ReturnedValue QV4::StringPrototype::method_includes(const "
        "FunctionObject *a0, const Value *thisObject, const Value *argv, "
        "int argc)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'getThisString'.")

  @staticmethod
  def method_indexOf(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::StringPrototype::method_indexOf(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier
    'getThisString'.
    """
    raise NotImplementedError(
        "'QV4.StringPrototype.method_indexOf' has no cute function yet. "
        "Qt's 'ReturnedValue QV4::StringPrototype::method_indexOf(const "
        "FunctionObject *a0, const Value *thisObject, const Value *argv, "
        "int argc)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'getThisString'.")

  @staticmethod
  def method_iterator(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::StringPrototype::method_iterator(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)': leans on 'QV4::StringIteratorObject::static_vtbl', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QV4.StringPrototype.method_iterator' has no cute function yet. "
        "Qt's 'ReturnedValue QV4::StringPrototype::method_iterator(const "
        "FunctionObject *a0, const Value *thisObject, const Value *argv, "
        "int argc)': leans on 'QV4::StringIteratorObject::static_vtbl', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def method_lastIndexOf(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::StringPrototype::method_lastIndexOf(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier
    'getThisString'.
    """
    raise NotImplementedError(
        "'QV4.StringPrototype.method_lastIndexOf' has no cute function yet. "
        "Qt's 'ReturnedValue QV4::StringPrototype::method_lastIndexOf(const "
        "FunctionObject *a0, const Value *thisObject, const Value *argv, "
        "int argc)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'getThisString'.")

  @staticmethod
  def method_localeCompare(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::StringPrototype::method_localeCompare(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier
    'getThisString'.
    """
    raise NotImplementedError(
        "'QV4.StringPrototype.method_localeCompare' has no cute function "
        "yet. Qt's 'ReturnedValue "
        "QV4::StringPrototype::method_localeCompare(const FunctionObject "
        "*a0, const Value *thisObject, const Value *argv, int argc)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'getThisString'.")

  @staticmethod
  def method_match(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::StringPrototype::method_match(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)': leans on
    'QV4::RegExpCtor::virtualCallAsConstructor(QV4::FunctionObject const*,
    QV4::Value const*, int, QV4::Value const*)', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QV4.StringPrototype.method_match' has no cute function yet. Qt's "
        "'ReturnedValue QV4::StringPrototype::method_match(const "
        "FunctionObject *a0, const Value *thisObject, const Value *argv, "
        "int argc)': leans on "
        "'QV4::RegExpCtor::virtualCallAsConstructor(QV4::FunctionObject "
        "const*, QV4::Value const*, int, QV4::Value const*)', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def method_normalize(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::StringPrototype::method_normalize(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier
    'getThisString'.
    """
    raise NotImplementedError(
        "'QV4.StringPrototype.method_normalize' has no cute function yet. "
        "Qt's 'ReturnedValue QV4::StringPrototype::method_normalize(const "
        "FunctionObject *a0, const Value *thisObject, const Value *argv, "
        "int argc)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'getThisString'.")

  @staticmethod
  def method_padEnd(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::StringPrototype::method_padEnd(const
    FunctionObject *f, const Value *thisObject, const Value *argv, int
    argc)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier
    'thisAsString'.
    """
    raise NotImplementedError(
        "'QV4.StringPrototype.method_padEnd' has no cute function yet. Qt's "
        "'ReturnedValue QV4::StringPrototype::method_padEnd(const "
        "FunctionObject *f, const Value *thisObject, const Value *argv, int "
        "argc)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'thisAsString'.")

  @staticmethod
  def method_padStart(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::StringPrototype::method_padStart(const
    FunctionObject *f, const Value *thisObject, const Value *argv, int
    argc)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier
    'thisAsString'.
    """
    raise NotImplementedError(
        "'QV4.StringPrototype.method_padStart' has no cute function yet. "
        "Qt's 'ReturnedValue QV4::StringPrototype::method_padStart(const "
        "FunctionObject *f, const Value *thisObject, const Value *argv, int "
        "argc)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'thisAsString'.")

  @staticmethod
  def method_repeat(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::StringPrototype::method_repeat(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier
    'getThisString'.
    """
    raise NotImplementedError(
        "'QV4.StringPrototype.method_repeat' has no cute function yet. Qt's "
        "'ReturnedValue QV4::StringPrototype::method_repeat(const "
        "FunctionObject *a0, const Value *thisObject, const Value *argv, "
        "int argc)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'getThisString'.")

  @staticmethod
  def method_replace(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::StringPrototype::method_replace(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: incomplete type 'QV4::RegExp' named in
    nested name specifier.
    """
    raise NotImplementedError(
        "'QV4.StringPrototype.method_replace' has no cute function yet. "
        "Qt's 'ReturnedValue QV4::StringPrototype::method_replace(const "
        "FunctionObject *a0, const Value *thisObject, const Value *argv, "
        "int argc)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: incomplete type "
        "'QV4::RegExp' named in nested name specifier.")

  @staticmethod
  def method_search(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::StringPrototype::method_search(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier
    'getThisString'.
    """
    raise NotImplementedError(
        "'QV4.StringPrototype.method_search' has no cute function yet. Qt's "
        "'ReturnedValue QV4::StringPrototype::method_search(const "
        "FunctionObject *a0, const Value *thisObject, const Value *argv, "
        "int argc)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'getThisString'.")

  @staticmethod
  def method_slice(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::StringPrototype::method_slice(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier
    'thisAsString'.
    """
    raise NotImplementedError(
        "'QV4.StringPrototype.method_slice' has no cute function yet. Qt's "
        "'ReturnedValue QV4::StringPrototype::method_slice(const "
        "FunctionObject *a0, const Value *thisObject, const Value *argv, "
        "int argc)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'thisAsString'.")

  @staticmethod
  def method_split(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::StringPrototype::method_split(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier
    'getThisString'.
    """
    raise NotImplementedError(
        "'QV4.StringPrototype.method_split' has no cute function yet. Qt's "
        "'ReturnedValue QV4::StringPrototype::method_split(const "
        "FunctionObject *a0, const Value *thisObject, const Value *argv, "
        "int argc)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'getThisString'.")

  @staticmethod
  def method_startsWith(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::StringPrototype::method_startsWith(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier
    'getThisString'.
    """
    raise NotImplementedError(
        "'QV4.StringPrototype.method_startsWith' has no cute function yet. "
        "Qt's 'ReturnedValue QV4::StringPrototype::method_startsWith(const "
        "FunctionObject *a0, const Value *thisObject, const Value *argv, "
        "int argc)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'getThisString'.")

  @staticmethod
  def method_substr(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::StringPrototype::method_substr(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier
    'getThisString'.
    """
    raise NotImplementedError(
        "'QV4.StringPrototype.method_substr' has no cute function yet. Qt's "
        "'ReturnedValue QV4::StringPrototype::method_substr(const "
        "FunctionObject *a0, const Value *thisObject, const Value *argv, "
        "int argc)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'getThisString'.")

  @staticmethod
  def method_substring(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::StringPrototype::method_substring(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier
    'getThisString'.
    """
    raise NotImplementedError(
        "'QV4.StringPrototype.method_substring' has no cute function yet. "
        "Qt's 'ReturnedValue QV4::StringPrototype::method_substring(const "
        "FunctionObject *a0, const Value *thisObject, const Value *argv, "
        "int argc)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'getThisString'.")

  @staticmethod
  def method_toLocaleLowerCase(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::StringPrototype::method_toLocaleLowerCase(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier
    'getThisString'.
    """
    raise NotImplementedError(
        "'QV4.StringPrototype.method_toLocaleLowerCase' has no cute "
        "function yet. Qt's 'ReturnedValue "
        "QV4::StringPrototype::method_toLocaleLowerCase(const "
        "FunctionObject *a0, const Value *thisObject, const Value *argv, "
        "int argc)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'getThisString'.")

  @staticmethod
  def method_toLocaleUpperCase(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::StringPrototype::method_toLocaleUpperCase(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier
    'getThisString'.
    """
    raise NotImplementedError(
        "'QV4.StringPrototype.method_toLocaleUpperCase' has no cute "
        "function yet. Qt's 'ReturnedValue "
        "QV4::StringPrototype::method_toLocaleUpperCase(const "
        "FunctionObject *a0, const Value *thisObject, const Value *argv, "
        "int argc)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'getThisString'.")

  @staticmethod
  def method_toLowerCase(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::StringPrototype::method_toLowerCase(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier
    'getThisString'.
    """
    raise NotImplementedError(
        "'QV4.StringPrototype.method_toLowerCase' has no cute function yet. "
        "Qt's 'ReturnedValue QV4::StringPrototype::method_toLowerCase(const "
        "FunctionObject *a0, const Value *thisObject, const Value *argv, "
        "int argc)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'getThisString'.")

  @staticmethod
  def method_toString(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::StringPrototype::method_toString(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)': leans on 'QV4::StringObject::static_vtbl', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QV4.StringPrototype.method_toString' has no cute function yet. "
        "Qt's 'ReturnedValue QV4::StringPrototype::method_toString(const "
        "FunctionObject *a0, const Value *thisObject, const Value *argv, "
        "int argc)': leans on 'QV4::StringObject::static_vtbl', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def method_toUpperCase(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::StringPrototype::method_toUpperCase(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier
    'getThisString'.
    """
    raise NotImplementedError(
        "'QV4.StringPrototype.method_toUpperCase' has no cute function yet. "
        "Qt's 'ReturnedValue QV4::StringPrototype::method_toUpperCase(const "
        "FunctionObject *a0, const Value *thisObject, const Value *argv, "
        "int argc)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'getThisString'.")

  @staticmethod
  def method_trim(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::StringPrototype::method_trim(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier
    'getThisString'.
    """
    raise NotImplementedError(
        "'QV4.StringPrototype.method_trim' has no cute function yet. Qt's "
        "'ReturnedValue QV4::StringPrototype::method_trim(const "
        "FunctionObject *a0, const Value *thisObject, const Value *argv, "
        "int argc)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'getThisString'.")
