"""
QV4::QMetaObjectWrapper binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4qmetaobjectwrapper_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QV4::QMetaObjectWrapper to be private: it declares the class in a
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

  from ..QtCore import QMetaObject
  from . import QQmlPropertyData
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMetaObject = WAIT['QMetaObject']
  QQmlPropertyData = WAIT['QQmlPropertyData']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QMetaObjectWrapper(QV4.FunctionObject):
  """
  The cute side of Qt's QV4::QMetaObjectWrapper: a plain Python object
  standing in front of one C++ QV4::QMetaObjectWrapper.

  It is built on the cute 'QV4::FunctionObject', as Qt's
  QV4::QMetaObjectWrapper is built on Qt's QV4::FunctionObject, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QV4::QMetaObjectWrapper that has a ritual and that
  Python can call so far, 10 names in all: '__dataTest', 'd_unchecked', 'd',
  'virtualDestroy', 'create', 'metaObject', 'virtualCallAsConstructor',
  'virtualIsEqualTo', 'init', 'constructInternal'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QV4::VTable *QV4::QMetaObjectWrapper::staticVTable()': gives
    'QV4::VTable', which has no cute class yet.

  What has no ritual
  ------------------

  5 of the 16 functions Qt declares: 3 forbidden; 1 not a gap; 1 a template.

  What to expect
  --------------

  - The C++ QV4::QMetaObjectWrapper is created at the first use, not by
    'QV4::QMetaObjectWrapper(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QV4::QMetaObjectWrapper.
  - Each name of Qt's QV4::QMetaObjectWrapper that has no cute function yet,
    'construct', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(WAIT['QV4.Heap.Base'])
  @overload(NoneType)
  def virtualDestroy(b: Optional[QV4.Heap.Base]) -> None:
    """
    Calls Qt's 'void QV4::QMetaObjectWrapper::virtualDestroy(QV4::Heap::Base
    *b)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-qmetaobjectwrapper.html#virtualDestroy

    Parameters
    ----------

    b : Optional[QV4.Heap.Base]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::QMetaObjectWrapper::virtualDestroy(QV4::Heap::Base *b)
    Rituals.call(
        'ritual_ZN3QV418QMetaObjectWrapper14virtualDestroyEPNS_4Heap4BaseE',
        CuteMixin._addressOf(b),
    )

  @staticmethod
  @overload(WAIT['QV4.ExecutionEngine'], QMetaObject)
  @overload(WAIT['QV4.ExecutionEngine'], NoneType)
  @overload(NoneType, QMetaObject)
  @overload(NoneType, NoneType)
  def create(
      engine: Optional[QV4.ExecutionEngine],
      metaObject: Optional[QMetaObject],
  ) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::QMetaObjectWrapper::create(ExecutionEngine
    *engine, const QMetaObject *metaObject)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-qmetaobjectwrapper.html#create

    Parameters
    ----------

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    metaObject : Optional[QMetaObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  ReturnedValue QV4::QMetaObjectWrapper::create(ExecutionEngine *engine,
    #      const QMetaObject *metaObject)
    return Rituals.call(
        'ritual_ZN3QV418QMetaObjectWrapper6createEPNS_15ExecutionEngineEPK1'
        '1QMetaObject',
        CuteMixin._addressOf(engine), CuteMixin._addressOf(metaObject,
        'QMetaObject'),
    )

  @staticmethod
  @overload(QV4.FunctionObject, QV4.Value, int, QV4.Value)
  @overload(QV4.FunctionObject, QV4.Value, int, NoneType)
  @overload(QV4.FunctionObject, NoneType, int, QV4.Value)
  @overload(QV4.FunctionObject, NoneType, int, NoneType)
  @overload(NoneType, QV4.Value, int, QV4.Value)
  @overload(NoneType, QV4.Value, int, NoneType)
  @overload(NoneType, NoneType, int, QV4.Value)
  @overload(NoneType, NoneType, int, NoneType)
  def virtualCallAsConstructor(
      a0: Optional[QV4.FunctionObject],
      argv: Optional[QV4.Value],
      argc: int,
      a3: Optional[QV4.Value],
  ) -> int:
    """
    Calls Qt's 'ReturnedValue
    QV4::QMetaObjectWrapper::virtualCallAsConstructor(const FunctionObject
    *a0, const Value *argv, int argc, const Value *a3)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-qmetaobjectwrapper.html

    Parameters
    ----------

    a0 : Optional[QV4.FunctionObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    argv : Optional[QV4.Value]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    argc : int
      Passed on as it is.

    a3 : Optional[QV4.Value]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  ReturnedValue QV4::QMetaObjectWrapper::virtualCallAsConstructor(const
    #      FunctionObject *a0, const Value *argv, int argc, const Value *a3)
    return Rituals.call(
        'ritual_ZN3QV418QMetaObjectWrapper24virtualCallAsConstructorEPKNS_1'
        '4FunctionObjectEPKNS_5ValueEiS6_',
        CuteMixin._addressOf(a0), CuteMixin._addressOf(argv), argc,
        CuteMixin._addressOf(a3),
    )

  @staticmethod
  @overload(QV4.Managed, QV4.Managed)
  @overload(QV4.Managed, NoneType)
  @overload(NoneType, QV4.Managed)
  @overload(NoneType, NoneType)
  def virtualIsEqualTo(
      a: Optional[QV4.Managed],
      b: Optional[QV4.Managed],
  ) -> bool:
    """
    Calls Qt's 'bool QV4::QMetaObjectWrapper::virtualIsEqualTo(Managed *a,
    Managed *b)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-qmetaobjectwrapper.html#virtualIsEqualTo

    Parameters
    ----------

    a : Optional[QV4.Managed]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    b : Optional[QV4.Managed]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QV4::QMetaObjectWrapper::virtualIsEqualTo(Managed *a, Managed *b)
    return Rituals.call(
        'ritual_ZN3QV418QMetaObjectWrapper16virtualIsEqualToEPNS_7ManagedES'
        '2_',
        CuteMixin._addressOf(a), CuteMixin._addressOf(b),
    )

  @staticmethod
  @overload(
      QMetaObject, QQmlPropertyData, WAIT['QV4.Heap.FunctionObject'],
      QV4.Value, int,
  )
  @overload(
      QMetaObject, QQmlPropertyData, WAIT['QV4.Heap.FunctionObject'],
      NoneType, int,
  )
  @overload(QMetaObject, QQmlPropertyData, NoneType, QV4.Value, int)
  @overload(QMetaObject, QQmlPropertyData, NoneType, NoneType, int)
  @overload(
      QMetaObject, NoneType, WAIT['QV4.Heap.FunctionObject'], QV4.Value, int,
  )
  @overload(
      QMetaObject, NoneType, WAIT['QV4.Heap.FunctionObject'], NoneType, int,
  )
  @overload(QMetaObject, NoneType, NoneType, QV4.Value, int)
  @overload(QMetaObject, NoneType, NoneType, NoneType, int)
  @overload(
      NoneType, QQmlPropertyData, WAIT['QV4.Heap.FunctionObject'], QV4.Value,
      int,
  )
  @overload(
      NoneType, QQmlPropertyData, WAIT['QV4.Heap.FunctionObject'], NoneType,
      int,
  )
  @overload(NoneType, QQmlPropertyData, NoneType, QV4.Value, int)
  @overload(NoneType, QQmlPropertyData, NoneType, NoneType, int)
  @overload(
      NoneType, NoneType, WAIT['QV4.Heap.FunctionObject'], QV4.Value, int,
  )
  @overload(
      NoneType, NoneType, WAIT['QV4.Heap.FunctionObject'], NoneType, int,
  )
  @overload(NoneType, NoneType, NoneType, QV4.Value, int)
  @overload(NoneType, NoneType, NoneType, NoneType, int)
  def constructInternal(
      mo: Optional[QMetaObject],
      constructors: Optional[QQmlPropertyData],
      d: Optional[QV4.Heap.FunctionObject],
      argv: Optional[QV4.Value],
      argc: int,
  ) -> int:
    """
    Calls Qt's 'ReturnedValue
    QV4::QMetaObjectWrapper::constructInternal(const QMetaObject *mo, const
    QQmlPropertyData *constructors, Heap::FunctionObject *d, const Value
    *argv, int argc)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-qmetaobjectwrapper.html#constructInternal

    Parameters
    ----------

    mo : Optional[QMetaObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    constructors : Optional[QQmlPropertyData]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    d : Optional[QV4.Heap.FunctionObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    argv : Optional[QV4.Value]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    argc : int
      Passed on as it is.
    """
    #  ReturnedValue QV4::QMetaObjectWrapper::constructInternal(const
    #      QMetaObject *mo, const QQmlPropertyData *constructors,
    #      Heap::FunctionObject *d, const Value *argv, int argc)
    return Rituals.call(
        'ritual_ZN3QV418QMetaObjectWrapper17constructInternalEPK11QMetaObje'
        'ctPK16QQmlPropertyDataPNS_4Heap14FunctionObjectEPKNS_5ValueEi',
        CuteMixin._addressOf(mo, 'QMetaObject'),
        CuteMixin._addressOf(constructors), CuteMixin._addressOf(d),
        CuteMixin._addressOf(argv), argc,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::QMetaObjectWrapper'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def d_unchecked(self) -> Optional[QV4.Heap.QMetaObjectWrapper]:
    """
    Calls Qt's 'QV4::Heap::QMetaObjectWrapper
    *QV4::QMetaObjectWrapper::d_unchecked() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-qmetaobjectwrapper.html#d_unchecked

    Returns
    -------

    Optional[QV4.Heap.QMetaObjectWrapper]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::Heap::QMetaObjectWrapper *QV4::QMetaObjectWrapper::d_unchecked()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK3QV418QMetaObjectWrapper11d_uncheckedEv',
    )
    return QV4.Heap.QMetaObjectWrapper._cuteAt(address)

  def d(self) -> Optional[QV4.Heap.QMetaObjectWrapper]:
    """
    Calls Qt's 'QV4::Heap::QMetaObjectWrapper *QV4::QMetaObjectWrapper::d()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-qmetaobjectwrapper.html#d

    Returns
    -------

    Optional[QV4.Heap.QMetaObjectWrapper]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::Heap::QMetaObjectWrapper *QV4::QMetaObjectWrapper::d() const
    address = self.uglySide.call('ritual_ZNK3QV418QMetaObjectWrapper1dEv')
    return QV4.Heap.QMetaObjectWrapper._cuteAt(address)

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QV4::QMetaObjectWrapper::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-qmetaobjectwrapper.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QV4::QMetaObjectWrapper::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK3QV418QMetaObjectWrapper10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

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

  def __dataTest(self) -> None:
    """
    Calls Qt's 'void QV4::QMetaObjectWrapper::__dataTest()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-qmetaobjectwrapper.html#__dataTest
    """
    #  void QV4::QMetaObjectWrapper::__dataTest()
    self.uglySide.call('ritual_ZN3QV418QMetaObjectWrapper10__dataTestEv')

  @overload(WAIT['QV4.ExecutionEngine'])
  @overload(NoneType)
  def init(self, engine: Optional[QV4.ExecutionEngine]) -> None:
    """
    Calls Qt's 'void QV4::QMetaObjectWrapper::init(ExecutionEngine *engine)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-qmetaobjectwrapper.html#init

    Parameters
    ----------

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::QMetaObjectWrapper::init(ExecutionEngine *engine)
    self.uglySide.call(
        'ritual_ZN3QV418QMetaObjectWrapper4initEPNS_15ExecutionEngineE',
        self._addressOf(engine),
    )

  @staticmethod
  def construct(*__, **_) -> Never:
    """
    Qt's 'QV4::QMetaObjectWrapper::construct': a template: a pattern and no
    single function.
    """
    raise NotImplementedError(
        "'QV4.QMetaObjectWrapper.construct' has no cute function yet. Qt's "
        "'QV4::QMetaObjectWrapper::construct': a template: a pattern and no "
        "single function.")
