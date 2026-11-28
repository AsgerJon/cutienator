"""
QV4::UrlPrototype binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4urlobject_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QV4::UrlPrototype to be private: it declares the class in a
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


class UrlPrototype(QV4.Object):
  """
  The cute side of Qt's QV4::UrlPrototype: a plain Python object standing in
  front of one C++ QV4::UrlPrototype.

  It is built on the cute 'QV4::Object', as Qt's QV4::UrlPrototype is built
  on Qt's QV4::Object, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QV4::UrlPrototype that has a ritual and that Python
  can call so far, 1 name in all: 'defaultPrototype'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has no ritual
  ------------------

  23 of the 24 functions Qt declares: 22 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 1 leans on
  'QV4.

  What to expect
  --------------

  - The C++ QV4::UrlPrototype is created at the first use, not by
    'QV4::UrlPrototype(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QV4::UrlPrototype.
  - Each name of Qt's QV4::UrlPrototype that has no cute function yet,
    'init', 'method_getHash', 'method_getHost', 'method_getHostname',
    'method_getHref', 'method_getOrigin', 'method_getPassword',
    'method_getPathname', 'method_getPort', 'method_getProtocol',
    'method_getSearch', 'method_getSearchParams', 'method_getUsername',
    'method_setHash', 'method_setHost', 'method_setHostname',
    'method_setHref', 'method_setPassword', 'method_setPathname',
    'method_setPort', 'method_setProtocol', 'method_setSearch',
    'method_setUsername', holds a function that raises 'NotImplementedError',
    and its docstring says why.
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
    *QV4::UrlPrototype::defaultPrototype(QV4::ExecutionEngine *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-urlprototype.html#defaultPrototype

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
    #  QV4::Object *QV4::UrlPrototype::defaultPrototype(QV4::ExecutionEngine
    #      *e)
    address = Rituals.call(
        'ritual_ZN3QV412UrlPrototype16defaultPrototypeEPNS_15ExecutionEngin'
        'eE',
        CuteMixin._addressOf(e),
    )
    return QV4.Object._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::UrlPrototype'

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
    Qt's 'void QV4::UrlPrototype::init(ExecutionEngine *engine, Object
    *ctor)': leans on 'QV4::UrlPrototype::method_getHash(QV4::FunctionObject
    const*, QV4::Value const*, QV4::Value const*, int)', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QV4.UrlPrototype.init' has no cute function yet. Qt's 'void "
        "QV4::UrlPrototype::init(ExecutionEngine *engine, Object *ctor)': "
        "leans on 'QV4::UrlPrototype::method_getHash(QV4::FunctionObject "
        "const*, QV4::Value const*, QV4::Value const*, int)', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def method_getHash(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::UrlPrototype::method_getHash(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier
    'checkUrlObjectType'.
    """
    raise NotImplementedError(
        "'QV4.UrlPrototype.method_getHash' has no cute function yet. Qt's "
        "'ReturnedValue QV4::UrlPrototype::method_getHash(const "
        "FunctionObject *a0, const Value *thisObject, const Value *argv, "
        "int argc)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'checkUrlObjectType'.")

  @staticmethod
  def method_getHost(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::UrlPrototype::method_getHost(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier
    'checkUrlObjectType'.
    """
    raise NotImplementedError(
        "'QV4.UrlPrototype.method_getHost' has no cute function yet. Qt's "
        "'ReturnedValue QV4::UrlPrototype::method_getHost(const "
        "FunctionObject *a0, const Value *thisObject, const Value *argv, "
        "int argc)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'checkUrlObjectType'.")

  @staticmethod
  def method_getHostname(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::UrlPrototype::method_getHostname(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier
    'checkUrlObjectType'.
    """
    raise NotImplementedError(
        "'QV4.UrlPrototype.method_getHostname' has no cute function yet. "
        "Qt's 'ReturnedValue QV4::UrlPrototype::method_getHostname(const "
        "FunctionObject *a0, const Value *thisObject, const Value *argv, "
        "int argc)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'checkUrlObjectType'.")

  @staticmethod
  def method_getHref(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::UrlPrototype::method_getHref(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier
    'checkUrlObjectType'.
    """
    raise NotImplementedError(
        "'QV4.UrlPrototype.method_getHref' has no cute function yet. Qt's "
        "'ReturnedValue QV4::UrlPrototype::method_getHref(const "
        "FunctionObject *a0, const Value *thisObject, const Value *argv, "
        "int argc)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'checkUrlObjectType'.")

  @staticmethod
  def method_getOrigin(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::UrlPrototype::method_getOrigin(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier
    'checkUrlObjectType'.
    """
    raise NotImplementedError(
        "'QV4.UrlPrototype.method_getOrigin' has no cute function yet. Qt's "
        "'ReturnedValue QV4::UrlPrototype::method_getOrigin(const "
        "FunctionObject *a0, const Value *thisObject, const Value *argv, "
        "int argc)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'checkUrlObjectType'.")

  @staticmethod
  def method_getPassword(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::UrlPrototype::method_getPassword(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier
    'checkUrlObjectType'.
    """
    raise NotImplementedError(
        "'QV4.UrlPrototype.method_getPassword' has no cute function yet. "
        "Qt's 'ReturnedValue QV4::UrlPrototype::method_getPassword(const "
        "FunctionObject *a0, const Value *thisObject, const Value *argv, "
        "int argc)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'checkUrlObjectType'.")

  @staticmethod
  def method_getPathname(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::UrlPrototype::method_getPathname(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier
    'checkUrlObjectType'.
    """
    raise NotImplementedError(
        "'QV4.UrlPrototype.method_getPathname' has no cute function yet. "
        "Qt's 'ReturnedValue QV4::UrlPrototype::method_getPathname(const "
        "FunctionObject *a0, const Value *thisObject, const Value *argv, "
        "int argc)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'checkUrlObjectType'.")

  @staticmethod
  def method_getPort(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::UrlPrototype::method_getPort(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier
    'checkUrlObjectType'.
    """
    raise NotImplementedError(
        "'QV4.UrlPrototype.method_getPort' has no cute function yet. Qt's "
        "'ReturnedValue QV4::UrlPrototype::method_getPort(const "
        "FunctionObject *a0, const Value *thisObject, const Value *argv, "
        "int argc)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'checkUrlObjectType'.")

  @staticmethod
  def method_getProtocol(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::UrlPrototype::method_getProtocol(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier
    'checkUrlObjectType'.
    """
    raise NotImplementedError(
        "'QV4.UrlPrototype.method_getProtocol' has no cute function yet. "
        "Qt's 'ReturnedValue QV4::UrlPrototype::method_getProtocol(const "
        "FunctionObject *a0, const Value *thisObject, const Value *argv, "
        "int argc)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'checkUrlObjectType'.")

  @staticmethod
  def method_getSearch(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::UrlPrototype::method_getSearch(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier
    'checkUrlObjectType'.
    """
    raise NotImplementedError(
        "'QV4.UrlPrototype.method_getSearch' has no cute function yet. Qt's "
        "'ReturnedValue QV4::UrlPrototype::method_getSearch(const "
        "FunctionObject *a0, const Value *thisObject, const Value *argv, "
        "int argc)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'checkUrlObjectType'.")

  @staticmethod
  def method_getSearchParams(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::UrlPrototype::method_getSearchParams(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier
    'checkUrlObjectType'.
    """
    raise NotImplementedError(
        "'QV4.UrlPrototype.method_getSearchParams' has no cute function "
        "yet. Qt's 'ReturnedValue "
        "QV4::UrlPrototype::method_getSearchParams(const FunctionObject "
        "*a0, const Value *thisObject, const Value *argv, int argc)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'checkUrlObjectType'.")

  @staticmethod
  def method_getUsername(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::UrlPrototype::method_getUsername(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier
    'checkUrlObjectType'.
    """
    raise NotImplementedError(
        "'QV4.UrlPrototype.method_getUsername' has no cute function yet. "
        "Qt's 'ReturnedValue QV4::UrlPrototype::method_getUsername(const "
        "FunctionObject *a0, const Value *thisObject, const Value *argv, "
        "int argc)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'checkUrlObjectType'.")

  @staticmethod
  def method_setHash(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::UrlPrototype::method_setHash(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier
    'checkUrlObjectType'.
    """
    raise NotImplementedError(
        "'QV4.UrlPrototype.method_setHash' has no cute function yet. Qt's "
        "'ReturnedValue QV4::UrlPrototype::method_setHash(const "
        "FunctionObject *a0, const Value *thisObject, const Value *argv, "
        "int argc)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'checkUrlObjectType'.")

  @staticmethod
  def method_setHost(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::UrlPrototype::method_setHost(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier
    'checkUrlObjectType'.
    """
    raise NotImplementedError(
        "'QV4.UrlPrototype.method_setHost' has no cute function yet. Qt's "
        "'ReturnedValue QV4::UrlPrototype::method_setHost(const "
        "FunctionObject *a0, const Value *thisObject, const Value *argv, "
        "int argc)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'checkUrlObjectType'.")

  @staticmethod
  def method_setHostname(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::UrlPrototype::method_setHostname(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier
    'checkUrlObjectType'.
    """
    raise NotImplementedError(
        "'QV4.UrlPrototype.method_setHostname' has no cute function yet. "
        "Qt's 'ReturnedValue QV4::UrlPrototype::method_setHostname(const "
        "FunctionObject *a0, const Value *thisObject, const Value *argv, "
        "int argc)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'checkUrlObjectType'.")

  @staticmethod
  def method_setHref(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::UrlPrototype::method_setHref(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier
    'checkUrlObjectType'.
    """
    raise NotImplementedError(
        "'QV4.UrlPrototype.method_setHref' has no cute function yet. Qt's "
        "'ReturnedValue QV4::UrlPrototype::method_setHref(const "
        "FunctionObject *a0, const Value *thisObject, const Value *argv, "
        "int argc)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'checkUrlObjectType'.")

  @staticmethod
  def method_setPassword(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::UrlPrototype::method_setPassword(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier
    'checkUrlObjectType'.
    """
    raise NotImplementedError(
        "'QV4.UrlPrototype.method_setPassword' has no cute function yet. "
        "Qt's 'ReturnedValue QV4::UrlPrototype::method_setPassword(const "
        "FunctionObject *a0, const Value *thisObject, const Value *argv, "
        "int argc)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'checkUrlObjectType'.")

  @staticmethod
  def method_setPathname(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::UrlPrototype::method_setPathname(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier
    'checkUrlObjectType'.
    """
    raise NotImplementedError(
        "'QV4.UrlPrototype.method_setPathname' has no cute function yet. "
        "Qt's 'ReturnedValue QV4::UrlPrototype::method_setPathname(const "
        "FunctionObject *a0, const Value *thisObject, const Value *argv, "
        "int argc)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'checkUrlObjectType'.")

  @staticmethod
  def method_setPort(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::UrlPrototype::method_setPort(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier
    'checkUrlObjectType'.
    """
    raise NotImplementedError(
        "'QV4.UrlPrototype.method_setPort' has no cute function yet. Qt's "
        "'ReturnedValue QV4::UrlPrototype::method_setPort(const "
        "FunctionObject *a0, const Value *thisObject, const Value *argv, "
        "int argc)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'checkUrlObjectType'.")

  @staticmethod
  def method_setProtocol(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::UrlPrototype::method_setProtocol(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier
    'checkUrlObjectType'.
    """
    raise NotImplementedError(
        "'QV4.UrlPrototype.method_setProtocol' has no cute function yet. "
        "Qt's 'ReturnedValue QV4::UrlPrototype::method_setProtocol(const "
        "FunctionObject *a0, const Value *thisObject, const Value *argv, "
        "int argc)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'checkUrlObjectType'.")

  @staticmethod
  def method_setSearch(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::UrlPrototype::method_setSearch(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier
    'checkUrlObjectType'.
    """
    raise NotImplementedError(
        "'QV4.UrlPrototype.method_setSearch' has no cute function yet. Qt's "
        "'ReturnedValue QV4::UrlPrototype::method_setSearch(const "
        "FunctionObject *a0, const Value *thisObject, const Value *argv, "
        "int argc)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'checkUrlObjectType'.")

  @staticmethod
  def method_setUsername(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::UrlPrototype::method_setUsername(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier
    'checkUrlObjectType'.
    """
    raise NotImplementedError(
        "'QV4.UrlPrototype.method_setUsername' has no cute function yet. "
        "Qt's 'ReturnedValue QV4::UrlPrototype::method_setUsername(const "
        "FunctionObject *a0, const Value *thisObject, const Value *argv, "
        "int argc)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'checkUrlObjectType'.")
