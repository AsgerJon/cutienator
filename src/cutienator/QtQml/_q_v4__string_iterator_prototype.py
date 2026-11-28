"""
QV4::StringIteratorPrototype binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4stringiterator_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QV4::StringIteratorPrototype to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
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


class StringIteratorPrototype(QV4.Object):
  """
  The cute side of Qt's QV4::StringIteratorPrototype: a plain Python object
  standing in front of one C++ QV4::StringIteratorPrototype.

  It is built on the cute 'QV4::Object', as Qt's QV4::StringIteratorPrototype
  is built on Qt's QV4::Object, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QV4::StringIteratorPrototype that has a ritual and
  that Python can call so far, 1 name in all: 'defaultPrototype'. None can be
  made from Python: one comes out of a function of another class that gives
  one back.

  What has no ritual
  ------------------

  2 of the 3 functions Qt declares: 2 leans on 'QV4.

  What to expect
  --------------

  - The C++ QV4::StringIteratorPrototype is created at the first use, not by
    'QV4::StringIteratorPrototype(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QV4::StringIteratorPrototype.
  - Each name of Qt's QV4::StringIteratorPrototype that has no cute function
    yet, 'init', 'method_next', holds a function that raises
    'NotImplementedError', and its docstring says why.
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
    *QV4::StringIteratorPrototype::defaultPrototype(QV4::ExecutionEngine
    *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-stringiteratorprototype.html#defaultPrototype

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
    #  QV4::Object *QV4::StringIteratorPrototype::defaultPrototype(QV4::
    #      ExecutionEngine *e)
    address = Rituals.call(
        'ritual_ZN3QV423StringIteratorPrototype16defaultPrototypeEPNS_15Exe'
        'cutionEngineE',
        CuteMixin._addressOf(e),
    )
    return QV4.Object._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::StringIteratorPrototype'

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
    Qt's 'void QV4::StringIteratorPrototype::init(ExecutionEngine *engine)':
    leans on 'QV4::StringIteratorObject::static_vtbl', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QV4.StringIteratorPrototype.init' has no cute function yet. Qt's "
        "'void QV4::StringIteratorPrototype::init(ExecutionEngine "
        "*engine)': leans on 'QV4::StringIteratorObject::static_vtbl', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def method_next(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::StringIteratorPrototype::method_next(const
    FunctionObject *b, const Value *thisObject, const Value *argv, int
    argc)': leans on 'QV4::StringIteratorObject::static_vtbl', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QV4.StringIteratorPrototype.method_next' has no cute function "
        "yet. Qt's 'ReturnedValue "
        "QV4::StringIteratorPrototype::method_next(const FunctionObject *b, "
        "const Value *thisObject, const Value *argv, int argc)': leans on "
        "'QV4::StringIteratorObject::static_vtbl', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")
