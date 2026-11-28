"""
QV4::GlobalFunctions binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4globalobject_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QV4::GlobalFunctions to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class GlobalFunctions(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QV4::GlobalFunctions: a plain Python object standing
  in front of one C++ QV4::GlobalFunctions.

  C++ hands a QV4::GlobalFunctions around as a copy, so every C++
  QV4::GlobalFunctions behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QV4::GlobalFunctions that has a ritual and that
  Python can call so far, 6 names in all: 'method_parseFloat',
  'method_isNaN', 'method_isFinite', 'method_decodeURI', 'method_escape',
  'method_unescape'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QV4::GlobalFunctions::~GlobalFunctions()': the destructor: Python
    removes its C++ QV4::GlobalFunctions by it, and has no other use for it.

  What has no ritual
  ------------------

  4 of the 11 functions Qt declares: 4 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QV4::GlobalFunctions is created at the first use, not by
    'QV4::GlobalFunctions(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QV4::GlobalFunctions back gives a copy the ritual
    made for Python, in a new cute QV4::GlobalFunctions.
  - Each name of Qt's QV4::GlobalFunctions that has no cute function yet,
    'method_decodeURIComponent', 'method_encodeURI',
    'method_encodeURIComponent', 'method_parseInt', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(
      WAIT['QV4.FunctionObject'], WAIT['QV4.Value'], WAIT['QV4.Value'], int,
  )
  @overload(WAIT['QV4.FunctionObject'], WAIT['QV4.Value'], NoneType, int)
  @overload(WAIT['QV4.FunctionObject'], NoneType, WAIT['QV4.Value'], int)
  @overload(WAIT['QV4.FunctionObject'], NoneType, NoneType, int)
  @overload(NoneType, WAIT['QV4.Value'], WAIT['QV4.Value'], int)
  @overload(NoneType, WAIT['QV4.Value'], NoneType, int)
  @overload(NoneType, NoneType, WAIT['QV4.Value'], int)
  @overload(NoneType, NoneType, NoneType, int)
  def method_parseFloat(
      a0: Optional[QV4.FunctionObject],
      thisObject: Optional[QV4.Value],
      argv: Optional[QV4.Value],
      argc: int,
  ) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::GlobalFunctions::method_parseFloat(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-globalfunctions.html#method_parseFloat

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
    #  ReturnedValue QV4::GlobalFunctions::method_parseFloat(const
    #      FunctionObject *a0, const Value *thisObject, const Value *argv,
    #      int argc)
    return Rituals.call(
        'ritual_ZN3QV415GlobalFunctions17method_parseFloatEPKNS_14FunctionO'
        'bjectEPKNS_5ValueES6_i',
        CuteMixin._addressOf(a0), CuteMixin._addressOf(thisObject),
        CuteMixin._addressOf(argv), argc,
    )

  @staticmethod
  @overload(
      WAIT['QV4.FunctionObject'], WAIT['QV4.Value'], WAIT['QV4.Value'], int,
  )
  @overload(WAIT['QV4.FunctionObject'], WAIT['QV4.Value'], NoneType, int)
  @overload(WAIT['QV4.FunctionObject'], NoneType, WAIT['QV4.Value'], int)
  @overload(WAIT['QV4.FunctionObject'], NoneType, NoneType, int)
  @overload(NoneType, WAIT['QV4.Value'], WAIT['QV4.Value'], int)
  @overload(NoneType, WAIT['QV4.Value'], NoneType, int)
  @overload(NoneType, NoneType, WAIT['QV4.Value'], int)
  @overload(NoneType, NoneType, NoneType, int)
  def method_isNaN(
      a0: Optional[QV4.FunctionObject],
      thisObject: Optional[QV4.Value],
      argv: Optional[QV4.Value],
      argc: int,
  ) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::GlobalFunctions::method_isNaN(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-globalfunctions.html#method_isNaN

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
    #  ReturnedValue QV4::GlobalFunctions::method_isNaN(const FunctionObject
    #      *a0, const Value *thisObject, const Value *argv, int argc)
    return Rituals.call(
        'ritual_ZN3QV415GlobalFunctions12method_isNaNEPKNS_14FunctionObject'
        'EPKNS_5ValueES6_i',
        CuteMixin._addressOf(a0), CuteMixin._addressOf(thisObject),
        CuteMixin._addressOf(argv), argc,
    )

  @staticmethod
  @overload(
      WAIT['QV4.FunctionObject'], WAIT['QV4.Value'], WAIT['QV4.Value'], int,
  )
  @overload(WAIT['QV4.FunctionObject'], WAIT['QV4.Value'], NoneType, int)
  @overload(WAIT['QV4.FunctionObject'], NoneType, WAIT['QV4.Value'], int)
  @overload(WAIT['QV4.FunctionObject'], NoneType, NoneType, int)
  @overload(NoneType, WAIT['QV4.Value'], WAIT['QV4.Value'], int)
  @overload(NoneType, WAIT['QV4.Value'], NoneType, int)
  @overload(NoneType, NoneType, WAIT['QV4.Value'], int)
  @overload(NoneType, NoneType, NoneType, int)
  def method_isFinite(
      a0: Optional[QV4.FunctionObject],
      thisObject: Optional[QV4.Value],
      argv: Optional[QV4.Value],
      argc: int,
  ) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::GlobalFunctions::method_isFinite(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-globalfunctions.html#method_isFinite

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
    #  ReturnedValue QV4::GlobalFunctions::method_isFinite(const
    #      FunctionObject *a0, const Value *thisObject, const Value *argv,
    #      int argc)
    return Rituals.call(
        'ritual_ZN3QV415GlobalFunctions15method_isFiniteEPKNS_14FunctionObj'
        'ectEPKNS_5ValueES6_i',
        CuteMixin._addressOf(a0), CuteMixin._addressOf(thisObject),
        CuteMixin._addressOf(argv), argc,
    )

  @staticmethod
  @overload(
      WAIT['QV4.FunctionObject'], WAIT['QV4.Value'], WAIT['QV4.Value'], int,
  )
  @overload(WAIT['QV4.FunctionObject'], WAIT['QV4.Value'], NoneType, int)
  @overload(WAIT['QV4.FunctionObject'], NoneType, WAIT['QV4.Value'], int)
  @overload(WAIT['QV4.FunctionObject'], NoneType, NoneType, int)
  @overload(NoneType, WAIT['QV4.Value'], WAIT['QV4.Value'], int)
  @overload(NoneType, WAIT['QV4.Value'], NoneType, int)
  @overload(NoneType, NoneType, WAIT['QV4.Value'], int)
  @overload(NoneType, NoneType, NoneType, int)
  def method_decodeURI(
      a0: Optional[QV4.FunctionObject],
      thisObject: Optional[QV4.Value],
      argv: Optional[QV4.Value],
      argc: int,
  ) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::GlobalFunctions::method_decodeURI(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-globalfunctions.html#method_decodeURI

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
    #  ReturnedValue QV4::GlobalFunctions::method_decodeURI(const
    #      FunctionObject *a0, const Value *thisObject, const Value *argv,
    #      int argc)
    return Rituals.call(
        'ritual_ZN3QV415GlobalFunctions16method_decodeURIEPKNS_14FunctionOb'
        'jectEPKNS_5ValueES6_i',
        CuteMixin._addressOf(a0), CuteMixin._addressOf(thisObject),
        CuteMixin._addressOf(argv), argc,
    )

  @staticmethod
  @overload(
      WAIT['QV4.FunctionObject'], WAIT['QV4.Value'], WAIT['QV4.Value'], int,
  )
  @overload(WAIT['QV4.FunctionObject'], WAIT['QV4.Value'], NoneType, int)
  @overload(WAIT['QV4.FunctionObject'], NoneType, WAIT['QV4.Value'], int)
  @overload(WAIT['QV4.FunctionObject'], NoneType, NoneType, int)
  @overload(NoneType, WAIT['QV4.Value'], WAIT['QV4.Value'], int)
  @overload(NoneType, WAIT['QV4.Value'], NoneType, int)
  @overload(NoneType, NoneType, WAIT['QV4.Value'], int)
  @overload(NoneType, NoneType, NoneType, int)
  def method_escape(
      a0: Optional[QV4.FunctionObject],
      thisObject: Optional[QV4.Value],
      argv: Optional[QV4.Value],
      argc: int,
  ) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::GlobalFunctions::method_escape(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-globalfunctions.html#method_escape

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
    #  ReturnedValue QV4::GlobalFunctions::method_escape(const FunctionObject
    #      *a0, const Value *thisObject, const Value *argv, int argc)
    return Rituals.call(
        'ritual_ZN3QV415GlobalFunctions13method_escapeEPKNS_14FunctionObjec'
        'tEPKNS_5ValueES6_i',
        CuteMixin._addressOf(a0), CuteMixin._addressOf(thisObject),
        CuteMixin._addressOf(argv), argc,
    )

  @staticmethod
  @overload(
      WAIT['QV4.FunctionObject'], WAIT['QV4.Value'], WAIT['QV4.Value'], int,
  )
  @overload(WAIT['QV4.FunctionObject'], WAIT['QV4.Value'], NoneType, int)
  @overload(WAIT['QV4.FunctionObject'], NoneType, WAIT['QV4.Value'], int)
  @overload(WAIT['QV4.FunctionObject'], NoneType, NoneType, int)
  @overload(NoneType, WAIT['QV4.Value'], WAIT['QV4.Value'], int)
  @overload(NoneType, WAIT['QV4.Value'], NoneType, int)
  @overload(NoneType, NoneType, WAIT['QV4.Value'], int)
  @overload(NoneType, NoneType, NoneType, int)
  def method_unescape(
      a0: Optional[QV4.FunctionObject],
      thisObject: Optional[QV4.Value],
      argv: Optional[QV4.Value],
      argc: int,
  ) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::GlobalFunctions::method_unescape(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-globalfunctions.html#method_unescape

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
    #  ReturnedValue QV4::GlobalFunctions::method_unescape(const
    #      FunctionObject *a0, const Value *thisObject, const Value *argv,
    #      int argc)
    return Rituals.call(
        'ritual_ZN3QV415GlobalFunctions15method_unescapeEPKNS_14FunctionObj'
        'ectEPKNS_5ValueES6_i',
        CuteMixin._addressOf(a0), CuteMixin._addressOf(thisObject),
        CuteMixin._addressOf(argv), argc,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::GlobalFunctions'

  #  Qt's '~QV4::GlobalFunctions()'. Naming it makes this a value class:
  #  Python owns every C++ QV4::GlobalFunctions behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN3QV415GlobalFunctionsD1Ev'

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
  def method_decodeURIComponent(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::GlobalFunctions::method_decodeURIComponent(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier 'decode';
    did you mean 'Encode'?.
    """
    raise NotImplementedError(
        "'QV4.GlobalFunctions.method_decodeURIComponent' has no cute "
        "function yet. Qt's 'ReturnedValue "
        "QV4::GlobalFunctions::method_decodeURIComponent(const "
        "FunctionObject *a0, const Value *thisObject, const Value *argv, "
        "int argc)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'decode'; did you mean 'Encode'?.")

  @staticmethod
  def method_encodeURI(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::GlobalFunctions::method_encodeURI(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier 'encode';
    did you mean 'Encode'?.
    """
    raise NotImplementedError(
        "'QV4.GlobalFunctions.method_encodeURI' has no cute function yet. "
        "Qt's 'ReturnedValue QV4::GlobalFunctions::method_encodeURI(const "
        "FunctionObject *a0, const Value *thisObject, const Value *argv, "
        "int argc)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'encode'; did you mean 'Encode'?.")

  @staticmethod
  def method_encodeURIComponent(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::GlobalFunctions::method_encodeURIComponent(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier 'encode';
    did you mean 'Encode'?.
    """
    raise NotImplementedError(
        "'QV4.GlobalFunctions.method_encodeURIComponent' has no cute "
        "function yet. Qt's 'ReturnedValue "
        "QV4::GlobalFunctions::method_encodeURIComponent(const "
        "FunctionObject *a0, const Value *thisObject, const Value *argv, "
        "int argc)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'encode'; did you mean 'Encode'?.")

  @staticmethod
  def method_parseInt(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::GlobalFunctions::method_parseInt(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier 'toInt'.
    """
    raise NotImplementedError(
        "'QV4.GlobalFunctions.method_parseInt' has no cute function yet. "
        "Qt's 'ReturnedValue QV4::GlobalFunctions::method_parseInt(const "
        "FunctionObject *a0, const Value *thisObject, const Value *argv, "
        "int argc)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'toInt'.")
