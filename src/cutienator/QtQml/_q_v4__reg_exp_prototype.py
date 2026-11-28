"""
QV4::RegExpPrototype binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4regexpobject_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QV4::RegExpPrototype to be private: it declares the class in a
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


class RegExpPrototype(QV4.Object):
  """
  The cute side of Qt's QV4::RegExpPrototype: a plain Python object standing
  in front of one C++ QV4::RegExpPrototype.

  It is built on the cute 'QV4::Object', as Qt's QV4::RegExpPrototype is
  built on Qt's QV4::Object, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QV4::RegExpPrototype that has a ritual and that
  Python can call so far, 10 names in all: 'method_exec', 'method_get_flags',
  'method_search', 'method_get_source', 'method_test', 'method_toString',
  'method_compile', 'method_get_lastParen', 'method_get_input', 'exec'. None
  can be made from Python: one comes out of a function of another class that
  gives one back.

  What has no ritual
  ------------------

  13 of the 23 functions Qt declares: 9 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 3 leans on
  'QV4; 1 a template.

  What to expect
  --------------

  - The C++ QV4::RegExpPrototype is created at the first use, not by
    'QV4::RegExpPrototype(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QV4::RegExpPrototype.
  - Each name of Qt's QV4::RegExpPrototype that has no cute function yet,
    'execFirstMatch', 'init', 'method_get_global', 'method_get_ignoreCase',
    'method_get_lastMatch_n', 'method_get_leftContext',
    'method_get_multiline', 'method_get_rightContext', 'method_get_sticky',
    'method_get_unicode', 'method_match', 'method_replace', 'method_split',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(WAIT['QV4.FunctionObject'], QV4.Value, QV4.Value, int)
  @overload(WAIT['QV4.FunctionObject'], QV4.Value, NoneType, int)
  @overload(WAIT['QV4.FunctionObject'], NoneType, QV4.Value, int)
  @overload(WAIT['QV4.FunctionObject'], NoneType, NoneType, int)
  @overload(NoneType, QV4.Value, QV4.Value, int)
  @overload(NoneType, QV4.Value, NoneType, int)
  @overload(NoneType, NoneType, QV4.Value, int)
  @overload(NoneType, NoneType, NoneType, int)
  def method_exec(
      a0: Optional[QV4.FunctionObject],
      thisObject: Optional[QV4.Value],
      argv: Optional[QV4.Value],
      argc: int,
  ) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::RegExpPrototype::method_exec(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-regexpprototype.html#method_exec

    Parameters
    ----------

    a0 : Optional[QV4.FunctionObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    thisObject : Optional[QV4.Value]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    argv : Optional[QV4.Value]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    argc : int
      Passed on as it is.
    """
    #  ReturnedValue QV4::RegExpPrototype::method_exec(const FunctionObject
    #      *a0, const Value *thisObject, const Value *argv, int argc)
    return Rituals.call(
        'ritual_ZN3QV415RegExpPrototype11method_execEPKNS_14FunctionObjectE'
        'PKNS_5ValueES6_i',
        CuteMixin._addressOf(a0), CuteMixin._addressOf(thisObject),
        CuteMixin._addressOf(argv), argc,
    )

  @staticmethod
  @overload(WAIT['QV4.FunctionObject'], QV4.Value, QV4.Value, int)
  @overload(WAIT['QV4.FunctionObject'], QV4.Value, NoneType, int)
  @overload(WAIT['QV4.FunctionObject'], NoneType, QV4.Value, int)
  @overload(WAIT['QV4.FunctionObject'], NoneType, NoneType, int)
  @overload(NoneType, QV4.Value, QV4.Value, int)
  @overload(NoneType, QV4.Value, NoneType, int)
  @overload(NoneType, NoneType, QV4.Value, int)
  @overload(NoneType, NoneType, NoneType, int)
  def method_get_flags(
      a0: Optional[QV4.FunctionObject],
      thisObject: Optional[QV4.Value],
      argv: Optional[QV4.Value],
      argc: int,
  ) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::RegExpPrototype::method_get_flags(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-regexpprototype.html#method_get_flags

    Parameters
    ----------

    a0 : Optional[QV4.FunctionObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    thisObject : Optional[QV4.Value]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    argv : Optional[QV4.Value]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    argc : int
      Passed on as it is.
    """
    #  ReturnedValue QV4::RegExpPrototype::method_get_flags(const
    #      FunctionObject *a0, const Value *thisObject, const Value *argv,
    #      int argc)
    return Rituals.call(
        'ritual_ZN3QV415RegExpPrototype16method_get_flagsEPKNS_14FunctionOb'
        'jectEPKNS_5ValueES6_i',
        CuteMixin._addressOf(a0), CuteMixin._addressOf(thisObject),
        CuteMixin._addressOf(argv), argc,
    )

  @staticmethod
  @overload(WAIT['QV4.FunctionObject'], QV4.Value, QV4.Value, int)
  @overload(WAIT['QV4.FunctionObject'], QV4.Value, NoneType, int)
  @overload(WAIT['QV4.FunctionObject'], NoneType, QV4.Value, int)
  @overload(WAIT['QV4.FunctionObject'], NoneType, NoneType, int)
  @overload(NoneType, QV4.Value, QV4.Value, int)
  @overload(NoneType, QV4.Value, NoneType, int)
  @overload(NoneType, NoneType, QV4.Value, int)
  @overload(NoneType, NoneType, NoneType, int)
  def method_search(
      a0: Optional[QV4.FunctionObject],
      thisObject: Optional[QV4.Value],
      argv: Optional[QV4.Value],
      argc: int,
  ) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::RegExpPrototype::method_search(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-regexpprototype.html#method_search

    Parameters
    ----------

    a0 : Optional[QV4.FunctionObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    thisObject : Optional[QV4.Value]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    argv : Optional[QV4.Value]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    argc : int
      Passed on as it is.
    """
    #  ReturnedValue QV4::RegExpPrototype::method_search(const FunctionObject
    #      *a0, const Value *thisObject, const Value *argv, int argc)
    return Rituals.call(
        'ritual_ZN3QV415RegExpPrototype13method_searchEPKNS_14FunctionObjec'
        'tEPKNS_5ValueES6_i',
        CuteMixin._addressOf(a0), CuteMixin._addressOf(thisObject),
        CuteMixin._addressOf(argv), argc,
    )

  @staticmethod
  @overload(WAIT['QV4.FunctionObject'], QV4.Value, QV4.Value, int)
  @overload(WAIT['QV4.FunctionObject'], QV4.Value, NoneType, int)
  @overload(WAIT['QV4.FunctionObject'], NoneType, QV4.Value, int)
  @overload(WAIT['QV4.FunctionObject'], NoneType, NoneType, int)
  @overload(NoneType, QV4.Value, QV4.Value, int)
  @overload(NoneType, QV4.Value, NoneType, int)
  @overload(NoneType, NoneType, QV4.Value, int)
  @overload(NoneType, NoneType, NoneType, int)
  def method_get_source(
      a0: Optional[QV4.FunctionObject],
      thisObject: Optional[QV4.Value],
      argv: Optional[QV4.Value],
      argc: int,
  ) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::RegExpPrototype::method_get_source(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-regexpprototype.html#method_get_source

    Parameters
    ----------

    a0 : Optional[QV4.FunctionObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    thisObject : Optional[QV4.Value]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    argv : Optional[QV4.Value]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    argc : int
      Passed on as it is.
    """
    #  ReturnedValue QV4::RegExpPrototype::method_get_source(const
    #      FunctionObject *a0, const Value *thisObject, const Value *argv,
    #      int argc)
    return Rituals.call(
        'ritual_ZN3QV415RegExpPrototype17method_get_sourceEPKNS_14FunctionO'
        'bjectEPKNS_5ValueES6_i',
        CuteMixin._addressOf(a0), CuteMixin._addressOf(thisObject),
        CuteMixin._addressOf(argv), argc,
    )

  @staticmethod
  @overload(WAIT['QV4.FunctionObject'], QV4.Value, QV4.Value, int)
  @overload(WAIT['QV4.FunctionObject'], QV4.Value, NoneType, int)
  @overload(WAIT['QV4.FunctionObject'], NoneType, QV4.Value, int)
  @overload(WAIT['QV4.FunctionObject'], NoneType, NoneType, int)
  @overload(NoneType, QV4.Value, QV4.Value, int)
  @overload(NoneType, QV4.Value, NoneType, int)
  @overload(NoneType, NoneType, QV4.Value, int)
  @overload(NoneType, NoneType, NoneType, int)
  def method_test(
      a0: Optional[QV4.FunctionObject],
      thisObject: Optional[QV4.Value],
      argv: Optional[QV4.Value],
      argc: int,
  ) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::RegExpPrototype::method_test(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-regexpprototype.html#method_test

    Parameters
    ----------

    a0 : Optional[QV4.FunctionObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    thisObject : Optional[QV4.Value]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    argv : Optional[QV4.Value]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    argc : int
      Passed on as it is.
    """
    #  ReturnedValue QV4::RegExpPrototype::method_test(const FunctionObject
    #      *a0, const Value *thisObject, const Value *argv, int argc)
    return Rituals.call(
        'ritual_ZN3QV415RegExpPrototype11method_testEPKNS_14FunctionObjectE'
        'PKNS_5ValueES6_i',
        CuteMixin._addressOf(a0), CuteMixin._addressOf(thisObject),
        CuteMixin._addressOf(argv), argc,
    )

  @staticmethod
  @overload(WAIT['QV4.FunctionObject'], QV4.Value, QV4.Value, int)
  @overload(WAIT['QV4.FunctionObject'], QV4.Value, NoneType, int)
  @overload(WAIT['QV4.FunctionObject'], NoneType, QV4.Value, int)
  @overload(WAIT['QV4.FunctionObject'], NoneType, NoneType, int)
  @overload(NoneType, QV4.Value, QV4.Value, int)
  @overload(NoneType, QV4.Value, NoneType, int)
  @overload(NoneType, NoneType, QV4.Value, int)
  @overload(NoneType, NoneType, NoneType, int)
  def method_toString(
      a0: Optional[QV4.FunctionObject],
      thisObject: Optional[QV4.Value],
      argv: Optional[QV4.Value],
      argc: int,
  ) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::RegExpPrototype::method_toString(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-regexpprototype.html#method_toString

    Parameters
    ----------

    a0 : Optional[QV4.FunctionObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    thisObject : Optional[QV4.Value]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    argv : Optional[QV4.Value]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    argc : int
      Passed on as it is.
    """
    #  ReturnedValue QV4::RegExpPrototype::method_toString(const
    #      FunctionObject *a0, const Value *thisObject, const Value *argv,
    #      int argc)
    return Rituals.call(
        'ritual_ZN3QV415RegExpPrototype15method_toStringEPKNS_14FunctionObj'
        'ectEPKNS_5ValueES6_i',
        CuteMixin._addressOf(a0), CuteMixin._addressOf(thisObject),
        CuteMixin._addressOf(argv), argc,
    )

  @staticmethod
  @overload(WAIT['QV4.FunctionObject'], QV4.Value, QV4.Value, int)
  @overload(WAIT['QV4.FunctionObject'], QV4.Value, NoneType, int)
  @overload(WAIT['QV4.FunctionObject'], NoneType, QV4.Value, int)
  @overload(WAIT['QV4.FunctionObject'], NoneType, NoneType, int)
  @overload(NoneType, QV4.Value, QV4.Value, int)
  @overload(NoneType, QV4.Value, NoneType, int)
  @overload(NoneType, NoneType, QV4.Value, int)
  @overload(NoneType, NoneType, NoneType, int)
  def method_compile(
      a0: Optional[QV4.FunctionObject],
      thisObject: Optional[QV4.Value],
      argv: Optional[QV4.Value],
      argc: int,
  ) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::RegExpPrototype::method_compile(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-regexpprototype.html#method_compile

    Parameters
    ----------

    a0 : Optional[QV4.FunctionObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    thisObject : Optional[QV4.Value]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    argv : Optional[QV4.Value]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    argc : int
      Passed on as it is.
    """
    #  ReturnedValue QV4::RegExpPrototype::method_compile(const
    #      FunctionObject *a0, const Value *thisObject, const Value *argv,
    #      int argc)
    return Rituals.call(
        'ritual_ZN3QV415RegExpPrototype14method_compileEPKNS_14FunctionObje'
        'ctEPKNS_5ValueES6_i',
        CuteMixin._addressOf(a0), CuteMixin._addressOf(thisObject),
        CuteMixin._addressOf(argv), argc,
    )

  @staticmethod
  @overload(WAIT['QV4.FunctionObject'], QV4.Value, QV4.Value, int)
  @overload(WAIT['QV4.FunctionObject'], QV4.Value, NoneType, int)
  @overload(WAIT['QV4.FunctionObject'], NoneType, QV4.Value, int)
  @overload(WAIT['QV4.FunctionObject'], NoneType, NoneType, int)
  @overload(NoneType, QV4.Value, QV4.Value, int)
  @overload(NoneType, QV4.Value, NoneType, int)
  @overload(NoneType, NoneType, QV4.Value, int)
  @overload(NoneType, NoneType, NoneType, int)
  def method_get_lastParen(
      a0: Optional[QV4.FunctionObject],
      thisObject: Optional[QV4.Value],
      argv: Optional[QV4.Value],
      argc: int,
  ) -> int:
    """
    Calls Qt's 'ReturnedValue
    QV4::RegExpPrototype::method_get_lastParen(const FunctionObject *a0,
    const Value *thisObject, const Value *argv, int argc)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-regexpprototype.html#method_get_lastParen

    Parameters
    ----------

    a0 : Optional[QV4.FunctionObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    thisObject : Optional[QV4.Value]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    argv : Optional[QV4.Value]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    argc : int
      Passed on as it is.
    """
    #  ReturnedValue QV4::RegExpPrototype::method_get_lastParen(const
    #      FunctionObject *a0, const Value *thisObject, const Value *argv,
    #      int argc)
    return Rituals.call(
        'ritual_ZN3QV415RegExpPrototype20method_get_lastParenEPKNS_14Functi'
        'onObjectEPKNS_5ValueES6_i',
        CuteMixin._addressOf(a0), CuteMixin._addressOf(thisObject),
        CuteMixin._addressOf(argv), argc,
    )

  @staticmethod
  @overload(WAIT['QV4.FunctionObject'], QV4.Value, QV4.Value, int)
  @overload(WAIT['QV4.FunctionObject'], QV4.Value, NoneType, int)
  @overload(WAIT['QV4.FunctionObject'], NoneType, QV4.Value, int)
  @overload(WAIT['QV4.FunctionObject'], NoneType, NoneType, int)
  @overload(NoneType, QV4.Value, QV4.Value, int)
  @overload(NoneType, QV4.Value, NoneType, int)
  @overload(NoneType, NoneType, QV4.Value, int)
  @overload(NoneType, NoneType, NoneType, int)
  def method_get_input(
      a0: Optional[QV4.FunctionObject],
      thisObject: Optional[QV4.Value],
      argv: Optional[QV4.Value],
      argc: int,
  ) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::RegExpPrototype::method_get_input(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-regexpprototype.html#method_get_input

    Parameters
    ----------

    a0 : Optional[QV4.FunctionObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    thisObject : Optional[QV4.Value]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    argv : Optional[QV4.Value]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    argc : int
      Passed on as it is.
    """
    #  ReturnedValue QV4::RegExpPrototype::method_get_input(const
    #      FunctionObject *a0, const Value *thisObject, const Value *argv,
    #      int argc)
    return Rituals.call(
        'ritual_ZN3QV415RegExpPrototype16method_get_inputEPKNS_14FunctionOb'
        'jectEPKNS_5ValueES6_i',
        CuteMixin._addressOf(a0), CuteMixin._addressOf(thisObject),
        CuteMixin._addressOf(argv), argc,
    )

  @staticmethod
  @overload(WAIT['QV4.ExecutionEngine'], QV4.Object, WAIT['QV4.String'])
  @overload(WAIT['QV4.ExecutionEngine'], QV4.Object, NoneType)
  @overload(WAIT['QV4.ExecutionEngine'], NoneType, WAIT['QV4.String'])
  @overload(WAIT['QV4.ExecutionEngine'], NoneType, NoneType)
  @overload(NoneType, QV4.Object, WAIT['QV4.String'])
  @overload(NoneType, QV4.Object, NoneType)
  @overload(NoneType, NoneType, WAIT['QV4.String'])
  @overload(NoneType, NoneType, NoneType)
  def exec(
      engine: Optional[QV4.ExecutionEngine],
      o: Optional[QV4.Object],
      s: Optional[QV4.String],
  ) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::RegExpPrototype::exec(ExecutionEngine
    *engine, const Object *o, const String *s)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-regexpprototype.html#exec

    Parameters
    ----------

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    o : Optional[QV4.Object]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    s : Optional[QV4.String]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  ReturnedValue QV4::RegExpPrototype::exec(ExecutionEngine *engine,
    #      const Object *o, const String *s)
    return Rituals.call(
        'ritual_ZN3QV415RegExpPrototype4execEPNS_15ExecutionEngineEPKNS_6Ob'
        'jectEPKNS_6StringE',
        CuteMixin._addressOf(engine), CuteMixin._addressOf(o),
        CuteMixin._addressOf(s),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::RegExpPrototype'

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
  def execFirstMatch(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::RegExpPrototype::execFirstMatch(const
    FunctionObject *b, const Value *thisObject, const Value *argv, int
    argc)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: member access into incomplete type
    'QV4::Heap::RegExp'.
    """
    raise NotImplementedError(
        "'QV4.RegExpPrototype.execFirstMatch' has no cute function yet. "
        "Qt's 'ReturnedValue QV4::RegExpPrototype::execFirstMatch(const "
        "FunctionObject *b, const Value *thisObject, const Value *argv, int "
        "argc)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: member access into "
        "incomplete type 'QV4::Heap::RegExp'.")

  @staticmethod
  def init(*__, **_) -> Never:
    """
    Qt's 'void QV4::RegExpPrototype::init(ExecutionEngine *engine, Object
    *ctor)': leans on 'QV4::RegExpCtor::static_vtbl', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QV4.RegExpPrototype.init' has no cute function yet. Qt's 'void "
        "QV4::RegExpPrototype::init(ExecutionEngine *engine, Object "
        "*ctor)': leans on 'QV4::RegExpCtor::static_vtbl', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def method_get_global(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::RegExpPrototype::method_get_global(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: member access into incomplete type
    'QV4::Heap::RegExp'.
    """
    raise NotImplementedError(
        "'QV4.RegExpPrototype.method_get_global' has no cute function yet. "
        "Qt's 'ReturnedValue QV4::RegExpPrototype::method_get_global(const "
        "FunctionObject *a0, const Value *thisObject, const Value *argv, "
        "int argc)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: member access into "
        "incomplete type 'QV4::Heap::RegExp'.")

  @staticmethod
  def method_get_ignoreCase(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::RegExpPrototype::method_get_ignoreCase(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: member access into incomplete type
    'QV4::Heap::RegExp'.
    """
    raise NotImplementedError(
        "'QV4.RegExpPrototype.method_get_ignoreCase' has no cute function "
        "yet. Qt's 'ReturnedValue "
        "QV4::RegExpPrototype::method_get_ignoreCase(const FunctionObject "
        "*a0, const Value *thisObject, const Value *argv, int argc)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: member access into incomplete type "
        "'QV4::Heap::RegExp'.")

  @staticmethod
  def method_get_lastMatch_n(*__, **_) -> Never:
    """
    Qt's 'QV4::RegExpPrototype::method_get_lastMatch_n': a template: a
    pattern and no single function.
    """
    raise NotImplementedError(
        "'QV4.RegExpPrototype.method_get_lastMatch_n' has no cute function "
        "yet. Qt's 'QV4::RegExpPrototype::method_get_lastMatch_n': a "
        "template: a pattern and no single function.")

  @staticmethod
  def method_get_leftContext(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::RegExpPrototype::method_get_leftContext(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)': leans on 'QV4::RegExpCtor::static_vtbl', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QV4.RegExpPrototype.method_get_leftContext' has no cute function "
        "yet. Qt's 'ReturnedValue "
        "QV4::RegExpPrototype::method_get_leftContext(const FunctionObject "
        "*a0, const Value *thisObject, const Value *argv, int argc)': leans "
        "on 'QV4::RegExpCtor::static_vtbl', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def method_get_multiline(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::RegExpPrototype::method_get_multiline(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: member access into incomplete type
    'QV4::Heap::RegExp'.
    """
    raise NotImplementedError(
        "'QV4.RegExpPrototype.method_get_multiline' has no cute function "
        "yet. Qt's 'ReturnedValue "
        "QV4::RegExpPrototype::method_get_multiline(const FunctionObject "
        "*a0, const Value *thisObject, const Value *argv, int argc)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: member access into incomplete type "
        "'QV4::Heap::RegExp'.")

  @staticmethod
  def method_get_rightContext(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::RegExpPrototype::method_get_rightContext(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)': leans on 'QV4::RegExpCtor::static_vtbl', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QV4.RegExpPrototype.method_get_rightContext' has no cute function "
        "yet. Qt's 'ReturnedValue "
        "QV4::RegExpPrototype::method_get_rightContext(const FunctionObject "
        "*a0, const Value *thisObject, const Value *argv, int argc)': leans "
        "on 'QV4::RegExpCtor::static_vtbl', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def method_get_sticky(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::RegExpPrototype::method_get_sticky(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: member access into incomplete type
    'QV4::Heap::RegExp'.
    """
    raise NotImplementedError(
        "'QV4.RegExpPrototype.method_get_sticky' has no cute function yet. "
        "Qt's 'ReturnedValue QV4::RegExpPrototype::method_get_sticky(const "
        "FunctionObject *a0, const Value *thisObject, const Value *argv, "
        "int argc)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: member access into "
        "incomplete type 'QV4::Heap::RegExp'.")

  @staticmethod
  def method_get_unicode(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::RegExpPrototype::method_get_unicode(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: member access into incomplete type
    'QV4::Heap::RegExp'.
    """
    raise NotImplementedError(
        "'QV4.RegExpPrototype.method_get_unicode' has no cute function yet. "
        "Qt's 'ReturnedValue QV4::RegExpPrototype::method_get_unicode(const "
        "FunctionObject *a0, const Value *thisObject, const Value *argv, "
        "int argc)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: member access into "
        "incomplete type 'QV4::Heap::RegExp'.")

  @staticmethod
  def method_match(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::RegExpPrototype::method_match(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: no matching function for call to
    'advanceLastIndexOnEmptyMatch'.
    """
    raise NotImplementedError(
        "'QV4.RegExpPrototype.method_match' has no cute function yet. Qt's "
        "'ReturnedValue QV4::RegExpPrototype::method_match(const "
        "FunctionObject *a0, const Value *thisObject, const Value *argv, "
        "int argc)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: no matching function "
        "for call to 'advanceLastIndexOnEmptyMatch'.")

  @staticmethod
  def method_replace(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::RegExpPrototype::method_replace(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier
    'advanceLastIndexOnEmptyMatch'.
    """
    raise NotImplementedError(
        "'QV4.RegExpPrototype.method_replace' has no cute function yet. "
        "Qt's 'ReturnedValue QV4::RegExpPrototype::method_replace(const "
        "FunctionObject *a0, const Value *thisObject, const Value *argv, "
        "int argc)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'advanceLastIndexOnEmptyMatch'.")

  @staticmethod
  def method_split(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::RegExpPrototype::method_split(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier
    'advanceStringIndex'.
    """
    raise NotImplementedError(
        "'QV4.RegExpPrototype.method_split' has no cute function yet. Qt's "
        "'ReturnedValue QV4::RegExpPrototype::method_split(const "
        "FunctionObject *a0, const Value *thisObject, const Value *argv, "
        "int argc)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'advanceStringIndex'.")
