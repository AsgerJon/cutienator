"""
QV4::SequencePrototype binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4sequenceobject_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QV4::SequencePrototype to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from . import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaType, QVariant
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMetaType = WAIT['QMetaType']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class SequencePrototype(QV4.Object):
  """
  The cute side of Qt's QV4::SequencePrototype: a plain Python object
  standing in front of one C++ QV4::SequencePrototype.

  It is built on the cute 'QV4::Object', as Qt's QV4::SequencePrototype is
  built on Qt's QV4::Object, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QV4::SequencePrototype that has a ritual and that
  Python can call so far, 12 names in all: 'defaultPrototype', 'init',
  'method_valueOf', 'method_shift', 'method_unshift', 'method_push',
  'method_pop', 'method_getLength', 'method_setLength', 'fromVariant',
  'metaTypeForSequence', 'toVariant'. None can be made from Python: one comes
  out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'ReturnedValue
    QV4::SequencePrototype::newSequence(QV4::ExecutionEngine *engine,
    QMetaType type, QMetaSequence metaSequence, const void *data,
    Heap::Object *object, int propertyIndex, Heap::ReferenceObject::Flags
    flags)': names 'void', which has no cute class yet.
  - Qt's 'ReturnedValue QV4::SequencePrototype::fromData(QV4::ExecutionEngine
    *engine, QMetaType type, QMetaSequence metaSequence, const void *data)':
    names 'void', which has no cute class yet.
  - Qt's 'void *QV4::SequencePrototype::rawContainerPtr(const Sequence
    *sequence, QMetaType typeHint)': gives 'void', which has no cute class
    yet.
  - Qt's 'RawCopyResult QV4::SequencePrototype::setRawContainer(Sequence
    *sequence, const void *container, QMetaType typeHint)': names 'void',
    which has no cute class yet.
  - Qt's 'RawCopyResult QV4::SequencePrototype::getRawContainer(const
    Sequence *sequence, void *container, QMetaType typeHint)': names 'void',
    which has no cute class yet.

  What to expect
  --------------

  - The C++ QV4::SequencePrototype is created at the first use, not by
    'QV4::SequencePrototype(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QV4::SequencePrototype.
  - Each name of Qt's QV4::SequencePrototype that has no cute function yet,
    'fromData', 'getRawContainer', 'newSequence', 'rawContainerPtr',
    'setRawContainer', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  #  The enums Qt writes inside QV4::SequencePrototype, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class RawCopyResult(CuteNum):
    """
    The enum 'QV4::SequencePrototype::RawCopyResult' of Qt, with the 3 names
    Qt gives in it.
    """

    Copied = Kee[int](0)
    WasEqual = Kee[int](1)
    TypeMismatch = Kee[int](2)

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
    *QV4::SequencePrototype::defaultPrototype(QV4::ExecutionEngine *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-sequenceprototype.html#defaultPrototype

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
    #      *QV4::SequencePrototype::defaultPrototype(QV4::ExecutionEngine *e)
    address = Rituals.call(
        'ritual_ZN3QV417SequencePrototype16defaultPrototypeEPNS_15Execution'
        'EngineE',
        CuteMixin._addressOf(e),
    )
    return QV4.Object._cuteAt(address)

  @staticmethod
  @overload(WAIT['QV4.FunctionObject'], QV4.Value, QV4.Value, int)
  @overload(WAIT['QV4.FunctionObject'], QV4.Value, NoneType, int)
  @overload(WAIT['QV4.FunctionObject'], NoneType, QV4.Value, int)
  @overload(WAIT['QV4.FunctionObject'], NoneType, NoneType, int)
  @overload(NoneType, QV4.Value, QV4.Value, int)
  @overload(NoneType, QV4.Value, NoneType, int)
  @overload(NoneType, NoneType, QV4.Value, int)
  @overload(NoneType, NoneType, NoneType, int)
  def method_valueOf(
      a0: Optional[QV4.FunctionObject],
      thisObject: Optional[QV4.Value],
      argv: Optional[QV4.Value],
      argc: int,
  ) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::SequencePrototype::method_valueOf(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-sequenceprototype.html#method_valueOf

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
    #  ReturnedValue QV4::SequencePrototype::method_valueOf(const
    #      FunctionObject *a0, const Value *thisObject, const Value *argv,
    #      int argc)
    return Rituals.call(
        'ritual_ZN3QV417SequencePrototype14method_valueOfEPKNS_14FunctionOb'
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
  def method_shift(
      b: Optional[QV4.FunctionObject],
      thisObject: Optional[QV4.Value],
      a2: Optional[QV4.Value],
      a3: int,
  ) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::SequencePrototype::method_shift(const
    FunctionObject *b, const Value *thisObject, const Value *a2, int a3)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-sequenceprototype.html#method_shift

    Parameters
    ----------

    b : Optional[QV4.FunctionObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    thisObject : Optional[QV4.Value]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a2 : Optional[QV4.Value]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a3 : int
      Passed on as it is.
    """
    #  ReturnedValue QV4::SequencePrototype::method_shift(const
    #      FunctionObject *b, const Value *thisObject, const Value *a2, int
    #      a3)
    return Rituals.call(
        'ritual_ZN3QV417SequencePrototype12method_shiftEPKNS_14FunctionObje'
        'ctEPKNS_5ValueES6_i',
        CuteMixin._addressOf(b), CuteMixin._addressOf(thisObject),
        CuteMixin._addressOf(a2), a3,
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
  def method_unshift(
      f: Optional[QV4.FunctionObject],
      thisObject: Optional[QV4.Value],
      argv: Optional[QV4.Value],
      argc: int,
  ) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::SequencePrototype::method_unshift(const
    FunctionObject *f, const Value *thisObject, const Value *argv, int
    argc)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-sequenceprototype.html#method_unshift

    Parameters
    ----------

    f : Optional[QV4.FunctionObject]
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
    #  ReturnedValue QV4::SequencePrototype::method_unshift(const
    #      FunctionObject *f, const Value *thisObject, const Value *argv, int
    #      argc)
    return Rituals.call(
        'ritual_ZN3QV417SequencePrototype14method_unshiftEPKNS_14FunctionOb'
        'jectEPKNS_5ValueES6_i',
        CuteMixin._addressOf(f), CuteMixin._addressOf(thisObject),
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
  def method_push(
      f: Optional[QV4.FunctionObject],
      thisObject: Optional[QV4.Value],
      argv: Optional[QV4.Value],
      argc: int,
  ) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::SequencePrototype::method_push(const
    FunctionObject *f, const Value *thisObject, const Value *argv, int
    argc)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-sequenceprototype.html#method_push

    Parameters
    ----------

    f : Optional[QV4.FunctionObject]
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
    #  ReturnedValue QV4::SequencePrototype::method_push(const FunctionObject
    #      *f, const Value *thisObject, const Value *argv, int argc)
    return Rituals.call(
        'ritual_ZN3QV417SequencePrototype11method_pushEPKNS_14FunctionObjec'
        'tEPKNS_5ValueES6_i',
        CuteMixin._addressOf(f), CuteMixin._addressOf(thisObject),
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
  def method_pop(
      f: Optional[QV4.FunctionObject],
      thisObject: Optional[QV4.Value],
      argv: Optional[QV4.Value],
      argc: int,
  ) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::SequencePrototype::method_pop(const
    FunctionObject *f, const Value *thisObject, const Value *argv, int
    argc)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-sequenceprototype.html#method_pop

    Parameters
    ----------

    f : Optional[QV4.FunctionObject]
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
    #  ReturnedValue QV4::SequencePrototype::method_pop(const FunctionObject
    #      *f, const Value *thisObject, const Value *argv, int argc)
    return Rituals.call(
        'ritual_ZN3QV417SequencePrototype10method_popEPKNS_14FunctionObject'
        'EPKNS_5ValueES6_i',
        CuteMixin._addressOf(f), CuteMixin._addressOf(thisObject),
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
  def method_getLength(
      b: Optional[QV4.FunctionObject],
      thisObject: Optional[QV4.Value],
      a2: Optional[QV4.Value],
      a3: int,
  ) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::SequencePrototype::method_getLength(const
    FunctionObject *b, const Value *thisObject, const Value *a2, int a3)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-sequenceprototype.html#method_getLength

    Parameters
    ----------

    b : Optional[QV4.FunctionObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    thisObject : Optional[QV4.Value]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a2 : Optional[QV4.Value]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a3 : int
      Passed on as it is.
    """
    #  ReturnedValue QV4::SequencePrototype::method_getLength(const
    #      FunctionObject *b, const Value *thisObject, const Value *a2, int
    #      a3)
    return Rituals.call(
        'ritual_ZN3QV417SequencePrototype16method_getLengthEPKNS_14Function'
        'ObjectEPKNS_5ValueES6_i',
        CuteMixin._addressOf(b), CuteMixin._addressOf(thisObject),
        CuteMixin._addressOf(a2), a3,
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
  def method_setLength(
      f: Optional[QV4.FunctionObject],
      thisObject: Optional[QV4.Value],
      argv: Optional[QV4.Value],
      argc: int,
  ) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::SequencePrototype::method_setLength(const
    FunctionObject *f, const Value *thisObject, const Value *argv, int
    argc)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-sequenceprototype.html#method_setLength

    Parameters
    ----------

    f : Optional[QV4.FunctionObject]
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
    #  ReturnedValue QV4::SequencePrototype::method_setLength(const
    #      FunctionObject *f, const Value *thisObject, const Value *argv, int
    #      argc)
    return Rituals.call(
        'ritual_ZN3QV417SequencePrototype16method_setLengthEPKNS_14Function'
        'ObjectEPKNS_5ValueES6_i',
        CuteMixin._addressOf(f), CuteMixin._addressOf(thisObject),
        CuteMixin._addressOf(argv), argc,
    )

  @staticmethod
  @overload(WAIT['QV4.ExecutionEngine'], QVariant)
  @overload(NoneType, QVariant)
  def fromVariant(
      engine: Optional[QV4.ExecutionEngine],
      vd: QVariant,
  ) -> int:
    """
    Calls Qt's 'ReturnedValue
    QV4::SequencePrototype::fromVariant(QV4::ExecutionEngine *engine, const
    QVariant &vd)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-sequenceprototype.html#fromVariant

    Parameters
    ----------

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    vd : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  ReturnedValue QV4::SequencePrototype::fromVariant(QV4::ExecutionEngine
    #      *engine, const QVariant &vd)
    return Rituals.call(
        'ritual_ZN3QV417SequencePrototype11fromVariantEPNS_15ExecutionEngin'
        'eERK8QVariant',
        CuteMixin._addressOf(engine), CuteMixin._valueOf(vd),
    )

  @staticmethod
  @overload(WAIT['QV4.Sequence'])
  @overload(NoneType)
  def metaTypeForSequence(object: Optional[QV4.Sequence]) -> QMetaType:
    """
    Calls Qt's 'QMetaType QV4::SequencePrototype::metaTypeForSequence(const
    Sequence *object)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-sequenceprototype.html#metaTypeForSequence

    Parameters
    ----------

    object : Optional[QV4.Sequence]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QMetaType
      A new cute QMetaType around the copy Qt gave back. Python owns it.
    """
    #  QMetaType QV4::SequencePrototype::metaTypeForSequence(const Sequence
    #      *object)
    address = Rituals.call(
        'ritual_ZN3QV417SequencePrototype19metaTypeForSequenceEPKNS_8Sequen'
        'ceE',
        CuteMixin._addressOf(object),
    )
    from ..QtCore import QMetaType
    return QMetaType._cuteOwning(address)

  @staticmethod
  @overload(WAIT['QV4.Sequence'])
  @overload(NoneType)
  def toVariant(object: Optional[QV4.Sequence]) -> QVariant:
    """
    Calls Qt's 'QVariant QV4::SequencePrototype::toVariant(const Sequence
    *object)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-sequenceprototype.html#toVariant

    Parameters
    ----------

    object : Optional[QV4.Sequence]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QV4::SequencePrototype::toVariant(const Sequence *object)
    address = Rituals.call(
        'ritual_ZN3QV417SequencePrototype9toVariantEPKNS_8SequenceE',
        CuteMixin._addressOf(object),
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @staticmethod
  @overload(QV4.Value, QMetaType)
  def toVariant(array: QV4.Value, targetType: QMetaType) -> QVariant:
    """
    Calls Qt's 'QVariant QV4::SequencePrototype::toVariant(const Value
    &array, QMetaType targetType)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-sequenceprototype.html#toVariant

    Parameters
    ----------

    array : QV4.Value
      Passed on as a value: Qt reads the C++ QV4::Value, which stays Python's
      own.

    targetType : QMetaType
      Passed on as a value: Qt reads the C++ QMetaType, which stays Python's
      own.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QV4::SequencePrototype::toVariant(const Value &array,
    #      QMetaType targetType)
    address = Rituals.call(
        'ritual_ZN3QV417SequencePrototype9toVariantERKNS_5ValueE9QMetaType',
        CuteMixin._valueOf(array), CuteMixin._valueOf(targetType),
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::SequencePrototype'

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

  def init(self) -> None:
    """
    Calls Qt's 'void QV4::SequencePrototype::init()'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-sequenceprototype.html#init
    """
    #  void QV4::SequencePrototype::init()
    self.uglySide.call('ritual_ZN3QV417SequencePrototype4initEv')

  @staticmethod
  def fromData(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::SequencePrototype::fromData(QV4::ExecutionEngine
    *engine, QMetaType type, QMetaSequence metaSequence, const void *data)':
    names 'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QV4.SequencePrototype.fromData' has no cute function yet. Qt's "
        "'ReturnedValue "
        "QV4::SequencePrototype::fromData(QV4::ExecutionEngine *engine, "
        "QMetaType type, QMetaSequence metaSequence, const void *data)': "
        "names 'void', which has no cute class yet.")

  @staticmethod
  def getRawContainer(*__, **_) -> Never:
    """
    Qt's 'RawCopyResult QV4::SequencePrototype::getRawContainer(const
    Sequence *sequence, void *container, QMetaType typeHint)': names 'void',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QV4.SequencePrototype.getRawContainer' has no cute function yet. "
        "Qt's 'RawCopyResult QV4::SequencePrototype::getRawContainer(const "
        "Sequence *sequence, void *container, QMetaType typeHint)': names "
        "'void', which has no cute class yet.")

  @staticmethod
  def newSequence(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue
    QV4::SequencePrototype::newSequence(QV4::ExecutionEngine *engine,
    QMetaType type, QMetaSequence metaSequence, const void *data,
    Heap::Object *object, int propertyIndex, Heap::ReferenceObject::Flags
    flags)': names 'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QV4.SequencePrototype.newSequence' has no cute function yet. Qt's "
        "'ReturnedValue "
        "QV4::SequencePrototype::newSequence(QV4::ExecutionEngine *engine, "
        "QMetaType type, QMetaSequence metaSequence, const void *data, "
        "Heap::Object *object, int propertyIndex, "
        "Heap::ReferenceObject::Flags flags)': names 'void', which has no "
        "cute class yet.")

  @staticmethod
  def rawContainerPtr(*__, **_) -> Never:
    """
    Qt's 'void *QV4::SequencePrototype::rawContainerPtr(const Sequence
    *sequence, QMetaType typeHint)': gives 'void', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QV4.SequencePrototype.rawContainerPtr' has no cute function yet. "
        "Qt's 'void *QV4::SequencePrototype::rawContainerPtr(const Sequence "
        "*sequence, QMetaType typeHint)': gives 'void', which has no cute "
        "class yet.")

  @staticmethod
  def setRawContainer(*__, **_) -> Never:
    """
    Qt's 'RawCopyResult QV4::SequencePrototype::setRawContainer(Sequence
    *sequence, const void *container, QMetaType typeHint)': names 'void',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QV4.SequencePrototype.setRawContainer' has no cute function yet. "
        "Qt's 'RawCopyResult "
        "QV4::SequencePrototype::setRawContainer(Sequence *sequence, const "
        "void *container, QMetaType typeHint)': names 'void', which has no "
        "cute class yet.")
