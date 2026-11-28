"""
QV4::GlobalExtensions binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmlbuiltinfunctions_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QV4::GlobalExtensions to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QJSEngine, QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class GlobalExtensions(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QV4::GlobalExtensions: a plain Python object standing
  in front of one C++ QV4::GlobalExtensions.

  C++ hands a QV4::GlobalExtensions around as a copy, so every C++
  QV4::GlobalExtensions behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QV4::GlobalExtensions that has a ritual and that
  Python can call so far, 10 names in all: 'init',
  'currentTranslationContext', 'method_qsTranslate',
  'method_qsTranslateNoOp', 'method_qsTr', 'method_qsTrNoOp',
  'method_qsTrId', 'method_qsTrIdNoOp', 'method_gc', 'method_string_arg'.
  None can be made from Python: one comes out of a function of another class
  that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QV4::GlobalExtensions::~GlobalExtensions()': the destructor: Python
    removes its C++ QV4::GlobalExtensions by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QV4::GlobalExtensions is created at the first use, not by
    'QV4::GlobalExtensions(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QV4::GlobalExtensions back gives a copy the ritual
    made for Python, in a new cute QV4::GlobalExtensions.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(WAIT['QV4.Object'], QJSEngine.Extensions)
  @overload(NoneType, QJSEngine.Extensions)
  def init(
      globalObject: Optional[QV4.Object],
      extensions: QJSEngine.Extensions,
  ) -> None:
    """
    Calls Qt's 'void QV4::GlobalExtensions::init(Object *globalObject,
    QJSEngine::Extensions extensions)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-globalextensions.html#init

    Parameters
    ----------

    globalObject : Optional[QV4.Object]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    extensions : QJSEngine.Extensions
      Passed on as its number.
    """
    #  void QV4::GlobalExtensions::init(Object *globalObject,
    #      QJSEngine::Extensions extensions)
    Rituals.call(
        'ritual_ZN3QV416GlobalExtensions4initEPNS_6ObjectE6QFlagsIN9QJSEngi'
        'ne9ExtensionEE',
        CuteMixin._addressOf(globalObject), extensions.value,
    )

  @staticmethod
  @overload(WAIT['QV4.ExecutionEngine'])
  @overload(NoneType)
  def currentTranslationContext(
      engine: Optional[QV4.ExecutionEngine],
  ) -> str:
    """
    Calls Qt's 'QString
    QV4::GlobalExtensions::currentTranslationContext(ExecutionEngine
    *engine)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-globalextensions.html

    Parameters
    ----------

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString
    #      QV4::GlobalExtensions::currentTranslationContext(ExecutionEngine
    #      *engine)
    return Rituals.call(
        'ritual_ZN3QV416GlobalExtensions25currentTranslationContextEPNS_15E'
        'xecutionEngineE',
        CuteMixin._addressOf(engine),
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
  def method_qsTranslate(
      b: Optional[QV4.FunctionObject],
      thisObject: Optional[QV4.Value],
      argv: Optional[QV4.Value],
      argc: int,
  ) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::GlobalExtensions::method_qsTranslate(const
    FunctionObject *b, const Value *thisObject, const Value *argv, int
    argc)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-globalextensions.html#method_qsTranslate

    Parameters
    ----------

    b : Optional[QV4.FunctionObject]
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
    #  ReturnedValue QV4::GlobalExtensions::method_qsTranslate(const
    #      FunctionObject *b, const Value *thisObject, const Value *argv, int
    #      argc)
    return Rituals.call(
        'ritual_ZN3QV416GlobalExtensions18method_qsTranslateEPKNS_14Functio'
        'nObjectEPKNS_5ValueES6_i',
        CuteMixin._addressOf(b), CuteMixin._addressOf(thisObject),
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
  def method_qsTranslateNoOp(
      b: Optional[QV4.FunctionObject],
      thisObject: Optional[QV4.Value],
      argv: Optional[QV4.Value],
      argc: int,
  ) -> int:
    """
    Calls Qt's 'ReturnedValue
    QV4::GlobalExtensions::method_qsTranslateNoOp(const FunctionObject *b,
    const Value *thisObject, const Value *argv, int argc)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-globalextensions.html#method_qsTranslateNoOp

    Parameters
    ----------

    b : Optional[QV4.FunctionObject]
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
    #  ReturnedValue QV4::GlobalExtensions::method_qsTranslateNoOp(const
    #      FunctionObject *b, const Value *thisObject, const Value *argv, int
    #      argc)
    return Rituals.call(
        'ritual_ZN3QV416GlobalExtensions22method_qsTranslateNoOpEPKNS_14Fun'
        'ctionObjectEPKNS_5ValueES6_i',
        CuteMixin._addressOf(b), CuteMixin._addressOf(thisObject),
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
  def method_qsTr(
      b: Optional[QV4.FunctionObject],
      thisObject: Optional[QV4.Value],
      argv: Optional[QV4.Value],
      argc: int,
  ) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::GlobalExtensions::method_qsTr(const
    FunctionObject *b, const Value *thisObject, const Value *argv, int
    argc)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-globalextensions.html#method_qsTr

    Parameters
    ----------

    b : Optional[QV4.FunctionObject]
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
    #  ReturnedValue QV4::GlobalExtensions::method_qsTr(const FunctionObject
    #      *b, const Value *thisObject, const Value *argv, int argc)
    return Rituals.call(
        'ritual_ZN3QV416GlobalExtensions11method_qsTrEPKNS_14FunctionObject'
        'EPKNS_5ValueES6_i',
        CuteMixin._addressOf(b), CuteMixin._addressOf(thisObject),
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
  def method_qsTrNoOp(
      b: Optional[QV4.FunctionObject],
      thisObject: Optional[QV4.Value],
      argv: Optional[QV4.Value],
      argc: int,
  ) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::GlobalExtensions::method_qsTrNoOp(const
    FunctionObject *b, const Value *thisObject, const Value *argv, int
    argc)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-globalextensions.html#method_qsTrNoOp

    Parameters
    ----------

    b : Optional[QV4.FunctionObject]
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
    #  ReturnedValue QV4::GlobalExtensions::method_qsTrNoOp(const
    #      FunctionObject *b, const Value *thisObject, const Value *argv, int
    #      argc)
    return Rituals.call(
        'ritual_ZN3QV416GlobalExtensions15method_qsTrNoOpEPKNS_14FunctionOb'
        'jectEPKNS_5ValueES6_i',
        CuteMixin._addressOf(b), CuteMixin._addressOf(thisObject),
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
  def method_qsTrId(
      b: Optional[QV4.FunctionObject],
      thisObject: Optional[QV4.Value],
      argv: Optional[QV4.Value],
      argc: int,
  ) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::GlobalExtensions::method_qsTrId(const
    FunctionObject *b, const Value *thisObject, const Value *argv, int
    argc)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-globalextensions.html#method_qsTrId

    Parameters
    ----------

    b : Optional[QV4.FunctionObject]
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
    #  ReturnedValue QV4::GlobalExtensions::method_qsTrId(const
    #      FunctionObject *b, const Value *thisObject, const Value *argv, int
    #      argc)
    return Rituals.call(
        'ritual_ZN3QV416GlobalExtensions13method_qsTrIdEPKNS_14FunctionObje'
        'ctEPKNS_5ValueES6_i',
        CuteMixin._addressOf(b), CuteMixin._addressOf(thisObject),
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
  def method_qsTrIdNoOp(
      b: Optional[QV4.FunctionObject],
      thisObject: Optional[QV4.Value],
      argv: Optional[QV4.Value],
      argc: int,
  ) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::GlobalExtensions::method_qsTrIdNoOp(const
    FunctionObject *b, const Value *thisObject, const Value *argv, int
    argc)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-globalextensions.html#method_qsTrIdNoOp

    Parameters
    ----------

    b : Optional[QV4.FunctionObject]
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
    #  ReturnedValue QV4::GlobalExtensions::method_qsTrIdNoOp(const
    #      FunctionObject *b, const Value *thisObject, const Value *argv, int
    #      argc)
    return Rituals.call(
        'ritual_ZN3QV416GlobalExtensions17method_qsTrIdNoOpEPKNS_14Function'
        'ObjectEPKNS_5ValueES6_i',
        CuteMixin._addressOf(b), CuteMixin._addressOf(thisObject),
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
  def method_gc(
      b: Optional[QV4.FunctionObject],
      thisObject: Optional[QV4.Value],
      argv: Optional[QV4.Value],
      argc: int,
  ) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::GlobalExtensions::method_gc(const
    FunctionObject *b, const Value *thisObject, const Value *argv, int
    argc)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-globalextensions.html#method_gc

    Parameters
    ----------

    b : Optional[QV4.FunctionObject]
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
    #  ReturnedValue QV4::GlobalExtensions::method_gc(const FunctionObject
    #      *b, const Value *thisObject, const Value *argv, int argc)
    return Rituals.call(
        'ritual_ZN3QV416GlobalExtensions9method_gcEPKNS_14FunctionObjectEPK'
        'NS_5ValueES6_i',
        CuteMixin._addressOf(b), CuteMixin._addressOf(thisObject),
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
  def method_string_arg(
      b: Optional[QV4.FunctionObject],
      thisObject: Optional[QV4.Value],
      argv: Optional[QV4.Value],
      argc: int,
  ) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::GlobalExtensions::method_string_arg(const
    FunctionObject *b, const Value *thisObject, const Value *argv, int
    argc)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-globalextensions.html#method_string_arg

    Parameters
    ----------

    b : Optional[QV4.FunctionObject]
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
    #  ReturnedValue QV4::GlobalExtensions::method_string_arg(const
    #      FunctionObject *b, const Value *thisObject, const Value *argv, int
    #      argc)
    return Rituals.call(
        'ritual_ZN3QV416GlobalExtensions17method_string_argEPKNS_14Function'
        'ObjectEPKNS_5ValueES6_i',
        CuteMixin._addressOf(b), CuteMixin._addressOf(thisObject),
        CuteMixin._addressOf(argv), argc,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::GlobalExtensions'

  #  Qt's '~QV4::GlobalExtensions()'. Naming it makes this a value class:
  #  Python owns every C++ QV4::GlobalExtensions behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN3QV416GlobalExtensionsD1Ev'

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
