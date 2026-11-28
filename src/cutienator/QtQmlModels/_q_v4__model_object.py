"""
QV4::ModelObject binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlModels/6.12.0/QtQmlModels/private/qqmllistmodel_p_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QV4::ModelObject to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtQml import QV4
from . import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class ModelObject(QV4.QObjectWrapper):
  """
  The cute side of Qt's QV4::ModelObject: a plain Python object standing in
  front of one C++ QV4::ModelObject.

  It is built on the cute 'QV4::QObjectWrapper', as Qt's QV4::ModelObject is
  built on Qt's QV4::QObjectWrapper, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QV4::ModelObject that has a ritual and that Python
  can call so far, 5 names in all: '__dataTest', 'd_unchecked', 'd',
  'virtualDestroy', 'virtualResolveLookupGetter'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'OwnPropertyKeyIterator
    *QV4::ModelObject::virtualOwnPropertyKeys(const Object *m, Value
    *target)': gives 'QV4::OwnPropertyKeyIterator', which has no cute class
    yet.

  What has no ritual
  ------------------

  8 of the 14 functions Qt declares: 3 forbidden; 2 leans on 'ListLayout; 1
  not a gap; 1 cannot be called and cannot be called through the meta-object
  and cannot be copied; 1 leans on 'QV4.

  What to expect
  --------------

  - The C++ QV4::ModelObject is created at the first use, not by
    'QV4::ModelObject(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QV4::ModelObject.
  - Each name of Qt's QV4::ModelObject that has no cute function yet,
    'lookupGetter', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(WAIT['QV4.Heap.Base'])
  @overload(NoneType)
  def virtualDestroy(b: Optional[QV4.Heap.Base]) -> None:
    """
    Calls Qt's 'void QV4::ModelObject::virtualDestroy(QV4::Heap::Base *b)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-modelobject.html#virtualDestroy

    Parameters
    ----------

    b : Optional[QV4.Heap.Base]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::ModelObject::virtualDestroy(QV4::Heap::Base *b)
    Rituals.call(
        'ritual_ZN3QV411ModelObject14virtualDestroyEPNS_4Heap4BaseE',
        CuteMixin._addressOf(b),
    )

  @staticmethod
  @overload(QV4.Object, WAIT['QV4.ExecutionEngine'], WAIT['QV4.Lookup'])
  @overload(QV4.Object, WAIT['QV4.ExecutionEngine'], NoneType)
  @overload(QV4.Object, NoneType, WAIT['QV4.Lookup'])
  @overload(QV4.Object, NoneType, NoneType)
  @overload(NoneType, WAIT['QV4.ExecutionEngine'], WAIT['QV4.Lookup'])
  @overload(NoneType, WAIT['QV4.ExecutionEngine'], NoneType)
  @overload(NoneType, NoneType, WAIT['QV4.Lookup'])
  @overload(NoneType, NoneType, NoneType)
  def virtualResolveLookupGetter(
      object: Optional[QV4.Object],
      engine: Optional[QV4.ExecutionEngine],
      lookup: Optional[QV4.Lookup],
  ) -> int:
    """
    Calls Qt's 'ReturnedValue
    QV4::ModelObject::virtualResolveLookupGetter(const Object *object,
    ExecutionEngine *engine, Lookup *lookup)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-modelobject.html#virtualResolveLookupGetter

    Parameters
    ----------

    object : Optional[QV4.Object]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    lookup : Optional[QV4.Lookup]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  ReturnedValue QV4::ModelObject::virtualResolveLookupGetter(const
    #      Object *object, ExecutionEngine *engine, Lookup *lookup)
    return Rituals.call(
        'ritual_ZN3QV411ModelObject26virtualResolveLookupGetterEPKNS_6Objec'
        'tEPNS_15ExecutionEngineEPNS_6LookupE',
        CuteMixin._addressOf(object), CuteMixin._addressOf(engine),
        CuteMixin._addressOf(lookup),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::ModelObject'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def d_unchecked(self) -> Optional[QV4.Heap.ModelObject]:
    """
    Calls Qt's 'QV4::Heap::ModelObject *QV4::ModelObject::d_unchecked()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-modelobject.html#d_unchecked

    Returns
    -------

    Optional[QV4.Heap.ModelObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::Heap::ModelObject *QV4::ModelObject::d_unchecked() const
    address = self.uglySide.call(
        'ritual_ZNK3QV411ModelObject11d_uncheckedEv',
    )
    return QV4.Heap.ModelObject._cuteAt(address)

  def d(self) -> Optional[QV4.Heap.ModelObject]:
    """
    Calls Qt's 'QV4::Heap::ModelObject *QV4::ModelObject::d() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-modelobject.html#d

    Returns
    -------

    Optional[QV4.Heap.ModelObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::Heap::ModelObject *QV4::ModelObject::d() const
    address = self.uglySide.call('ritual_ZNK3QV411ModelObject1dEv')
    return QV4.Heap.ModelObject._cuteAt(address)

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
    Calls Qt's 'void QV4::ModelObject::__dataTest()'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-modelobject.html#__dataTest
    """
    #  void QV4::ModelObject::__dataTest()
    self.uglySide.call('ritual_ZN3QV411ModelObject10__dataTestEv')

  @staticmethod
  def lookupGetter(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::ModelObject::lookupGetter(Lookup *l,
    ExecutionEngine *engine, const Value &object)': cannot be called and
    cannot be called through the meta-object and cannot be copied: no header
    file has its code, Qt's source does not mark it or its class for use from
    outside Qt or writes it 'inline' or nowhere, and it is no signal, slot or
    invokable function giving back nothing, of a class built on QObject, and
    Qt's source has no code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QV4.ModelObject.lookupGetter' has no cute function yet. Qt's "
        "'ReturnedValue QV4::ModelObject::lookupGetter(Lookup *l, "
        "ExecutionEngine *engine, const Value &object)': cannot be called "
        "and cannot be called through the meta-object and cannot be copied: "
        "no header file has its code, Qt's source does not mark it or its "
        "class for use from outside Qt or writes it 'inline' or nowhere, "
        "and it is no signal, slot or invokable function giving back "
        "nothing, of a class built on QObject, and Qt's source has no code "
        "for it that could be told from the rest.")
