"""
QV4::Module binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4module_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QV4::Module to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class Module(QV4.Object):
  """
  The cute side of Qt's QV4::Module: a plain Python object standing in front
  of one C++ QV4::Module.

  It is built on the cute 'QV4::Object', as Qt's QV4::Module is built on Qt's
  QV4::Object, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QV4::Module that has a ritual and that Python can
  call so far, 14 names in all: '__dataTest', 'd_unchecked', 'd', 'evaluate',
  'resolveExport', 'virtualGetOwnProperty', 'virtualHasProperty',
  'virtualPreventExtensions', 'virtualDefineOwnProperty', 'virtualPut',
  'virtualDeleteProperty', 'virtualGetPrototypeOf', 'virtualSetPrototypeOf',
  'virtualIsExtensible'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QV4::VTable *QV4::Module::staticVTable()': gives
    'QV4::VTable', which has no cute class yet.
  - Qt's 'ReturnedValue QV4::Module::virtualGet(const Managed *m, PropertyKey
    id, const Value *receiver, bool *hasProperty)': takes a number to change
    where it is.
  - Qt's 'OwnPropertyKeyIterator *QV4::Module::virtualOwnPropertyKeys(const
    Object *m, Value *target)': gives 'QV4::OwnPropertyKeyIterator', which
    has no cute class yet.

  What has no ritual
  ------------------

  4 of the 21 functions Qt declares: 3 forbidden; 1 not a gap.

  What to expect
  --------------

  - The C++ QV4::Module is created at the first use, not by
    'QV4::Module(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QV4::Module.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QV4.Managed, WAIT['QV4.PropertyKey'], WAIT['QV4.Property'])
  @overload(QV4.Managed, WAIT['QV4.PropertyKey'], NoneType)
  @overload(NoneType, WAIT['QV4.PropertyKey'], WAIT['QV4.Property'])
  @overload(NoneType, WAIT['QV4.PropertyKey'], NoneType)
  def virtualGetOwnProperty(
      m: Optional[QV4.Managed],
      id: QV4.PropertyKey,
      p: Optional[QV4.Property],
  ) -> QV4.PropertyAttributes:
    """
    Calls Qt's 'PropertyAttributes QV4::Module::virtualGetOwnProperty(const
    Managed *m, PropertyKey id, Property *p)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-module.html#virtualGetOwnProperty

    Parameters
    ----------

    m : Optional[QV4.Managed]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    id : QV4.PropertyKey
      Passed on as a value: Qt reads the C++ QV4::PropertyKey, which stays
      Python's own.

    p : Optional[QV4.Property]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QV4.PropertyAttributes
      A new cute QV4::PropertyAttributes around the copy Qt gave back. Python
      owns it.
    """
    #  PropertyAttributes QV4::Module::virtualGetOwnProperty(const Managed
    #      *m, PropertyKey id, Property *p)
    address = Rituals.call(
        'ritual_ZN3QV46Module21virtualGetOwnPropertyEPKNS_7ManagedENS_11Pro'
        'pertyKeyEPNS_8PropertyE',
        CuteMixin._addressOf(m), CuteMixin._valueOf(id),
        CuteMixin._addressOf(p),
    )
    return QV4.PropertyAttributes._cuteOwning(address)

  @staticmethod
  @overload(QV4.Managed, WAIT['QV4.PropertyKey'])
  @overload(NoneType, WAIT['QV4.PropertyKey'])
  def virtualHasProperty(
      m: Optional[QV4.Managed],
      id: QV4.PropertyKey,
  ) -> bool:
    """
    Calls Qt's 'bool QV4::Module::virtualHasProperty(const Managed *m,
    PropertyKey id)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-module.html#virtualHasProperty

    Parameters
    ----------

    m : Optional[QV4.Managed]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    id : QV4.PropertyKey
      Passed on as a value: Qt reads the C++ QV4::PropertyKey, which stays
      Python's own.
    """
    #  bool QV4::Module::virtualHasProperty(const Managed *m, PropertyKey id)
    return Rituals.call(
        'ritual_ZN3QV46Module18virtualHasPropertyEPKNS_7ManagedENS_11Proper'
        'tyKeyE',
        CuteMixin._addressOf(m), CuteMixin._valueOf(id),
    )

  @staticmethod
  @overload(QV4.Managed)
  @overload(NoneType)
  def virtualPreventExtensions(a0: Optional[QV4.Managed]) -> bool:
    """
    Calls Qt's 'bool QV4::Module::virtualPreventExtensions(Managed *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-module.html#virtualPreventExtensions

    Parameters
    ----------

    a0 : Optional[QV4.Managed]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QV4::Module::virtualPreventExtensions(Managed *a0)
    return Rituals.call(
        'ritual_ZN3QV46Module24virtualPreventExtensionsEPNS_7ManagedE',
        CuteMixin._addressOf(a0),
    )

  @staticmethod
  @overload(
      QV4.Managed, WAIT['QV4.PropertyKey'], WAIT['QV4.Property'],
      WAIT['QV4.PropertyAttributes'],
  )
  @overload(
      QV4.Managed, WAIT['QV4.PropertyKey'], NoneType,
      WAIT['QV4.PropertyAttributes'],
  )
  @overload(
      NoneType, WAIT['QV4.PropertyKey'], WAIT['QV4.Property'],
      WAIT['QV4.PropertyAttributes'],
  )
  @overload(
      NoneType, WAIT['QV4.PropertyKey'], NoneType,
      WAIT['QV4.PropertyAttributes'],
  )
  def virtualDefineOwnProperty(
      a0: Optional[QV4.Managed],
      a1: QV4.PropertyKey,
      a2: Optional[QV4.Property],
      a3: QV4.PropertyAttributes,
  ) -> bool:
    """
    Calls Qt's 'bool QV4::Module::virtualDefineOwnProperty(Managed *a0,
    PropertyKey a1, const Property *a2, PropertyAttributes a3)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-module.html#virtualDefineOwnProperty

    Parameters
    ----------

    a0 : Optional[QV4.Managed]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : QV4.PropertyKey
      Passed on as a value: Qt reads the C++ QV4::PropertyKey, which stays
      Python's own.

    a2 : Optional[QV4.Property]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a3 : QV4.PropertyAttributes
      Passed on as a value: Qt reads the C++ QV4::PropertyAttributes, which
      stays Python's own.
    """
    #  bool QV4::Module::virtualDefineOwnProperty(Managed *a0, PropertyKey
    #      a1, const Property *a2, PropertyAttributes a3)
    return Rituals.call(
        'ritual_ZN3QV46Module24virtualDefineOwnPropertyEPNS_7ManagedENS_11P'
        'ropertyKeyEPKNS_8PropertyENS_18PropertyAttributesE',
        CuteMixin._addressOf(a0), CuteMixin._valueOf(a1),
        CuteMixin._addressOf(a2), CuteMixin._valueOf(a3),
    )

  @staticmethod
  @overload(QV4.Managed, WAIT['QV4.PropertyKey'], QV4.Value, QV4.Value)
  @overload(QV4.Managed, WAIT['QV4.PropertyKey'], QV4.Value, NoneType)
  @overload(NoneType, WAIT['QV4.PropertyKey'], QV4.Value, QV4.Value)
  @overload(NoneType, WAIT['QV4.PropertyKey'], QV4.Value, NoneType)
  def virtualPut(
      a0: Optional[QV4.Managed],
      a1: QV4.PropertyKey,
      a2: QV4.Value,
      a3: Optional[QV4.Value],
  ) -> bool:
    """
    Calls Qt's 'bool QV4::Module::virtualPut(Managed *a0, PropertyKey a1,
    const Value &a2, Value *a3)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-module.html#virtualPut

    Parameters
    ----------

    a0 : Optional[QV4.Managed]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : QV4.PropertyKey
      Passed on as a value: Qt reads the C++ QV4::PropertyKey, which stays
      Python's own.

    a2 : QV4.Value
      Passed on as a value: Qt reads the C++ QV4::Value, which stays Python's
      own.

    a3 : Optional[QV4.Value]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QV4::Module::virtualPut(Managed *a0, PropertyKey a1, const Value
    #      &a2, Value *a3)
    return Rituals.call(
        'ritual_ZN3QV46Module10virtualPutEPNS_7ManagedENS_11PropertyKeyERKN'
        'S_5ValueEPS4_',
        CuteMixin._addressOf(a0), CuteMixin._valueOf(a1),
        CuteMixin._valueOf(a2), CuteMixin._addressOf(a3),
    )

  @staticmethod
  @overload(QV4.Managed, WAIT['QV4.PropertyKey'])
  @overload(NoneType, WAIT['QV4.PropertyKey'])
  def virtualDeleteProperty(
      m: Optional[QV4.Managed],
      id: QV4.PropertyKey,
  ) -> bool:
    """
    Calls Qt's 'bool QV4::Module::virtualDeleteProperty(Managed *m,
    PropertyKey id)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-module.html#virtualDeleteProperty

    Parameters
    ----------

    m : Optional[QV4.Managed]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    id : QV4.PropertyKey
      Passed on as a value: Qt reads the C++ QV4::PropertyKey, which stays
      Python's own.
    """
    #  bool QV4::Module::virtualDeleteProperty(Managed *m, PropertyKey id)
    return Rituals.call(
        'ritual_ZN3QV46Module21virtualDeletePropertyEPNS_7ManagedENS_11Prop'
        'ertyKeyE',
        CuteMixin._addressOf(m), CuteMixin._valueOf(id),
    )

  @staticmethod
  @overload(QV4.Managed)
  @overload(NoneType)
  def virtualGetPrototypeOf(
      a0: Optional[QV4.Managed],
  ) -> Optional[QV4.Heap.Object]:
    """
    Calls Qt's 'Heap::Object *QV4::Module::virtualGetPrototypeOf(const
    Managed *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-module.html#virtualGetPrototypeOf

    Parameters
    ----------

    a0 : Optional[QV4.Managed]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QV4.Heap.Object]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Heap::Object *QV4::Module::virtualGetPrototypeOf(const Managed *a0)
    address = Rituals.call(
        'ritual_ZN3QV46Module21virtualGetPrototypeOfEPKNS_7ManagedE',
        CuteMixin._addressOf(a0),
    )
    return QV4.Heap.Object._cuteAt(address)

  @staticmethod
  @overload(QV4.Managed, QV4.Object)
  @overload(QV4.Managed, NoneType)
  @overload(NoneType, QV4.Object)
  @overload(NoneType, NoneType)
  def virtualSetPrototypeOf(
      a0: Optional[QV4.Managed],
      proto: Optional[QV4.Object],
  ) -> bool:
    """
    Calls Qt's 'bool QV4::Module::virtualSetPrototypeOf(Managed *a0, const
    Object *proto)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-module.html#virtualSetPrototypeOf

    Parameters
    ----------

    a0 : Optional[QV4.Managed]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    proto : Optional[QV4.Object]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QV4::Module::virtualSetPrototypeOf(Managed *a0, const Object
    #      *proto)
    return Rituals.call(
        'ritual_ZN3QV46Module21virtualSetPrototypeOfEPNS_7ManagedEPKNS_6Obj'
        'ectE',
        CuteMixin._addressOf(a0), CuteMixin._addressOf(proto),
    )

  @staticmethod
  @overload(QV4.Managed)
  @overload(NoneType)
  def virtualIsExtensible(a0: Optional[QV4.Managed]) -> bool:
    """
    Calls Qt's 'bool QV4::Module::virtualIsExtensible(const Managed *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-module.html#virtualIsExtensible

    Parameters
    ----------

    a0 : Optional[QV4.Managed]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QV4::Module::virtualIsExtensible(const Managed *a0)
    return Rituals.call(
        'ritual_ZN3QV46Module19virtualIsExtensibleEPKNS_7ManagedE',
        CuteMixin._addressOf(a0),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::Module'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def d_unchecked(self) -> Optional[QV4.Heap.Module]:
    """
    Calls Qt's 'QV4::Heap::Module *QV4::Module::d_unchecked() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-module.html#d_unchecked

    Returns
    -------

    Optional[QV4.Heap.Module]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::Heap::Module *QV4::Module::d_unchecked() const
    address = self.uglySide.call('ritual_ZNK3QV46Module11d_uncheckedEv')
    return QV4.Heap.Module._cuteAt(address)

  def d(self) -> Optional[QV4.Heap.Module]:
    """
    Calls Qt's 'QV4::Heap::Module *QV4::Module::d() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-module.html#d

    Returns
    -------

    Optional[QV4.Heap.Module]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::Heap::Module *QV4::Module::d() const
    address = self.uglySide.call('ritual_ZNK3QV46Module1dEv')
    return QV4.Heap.Module._cuteAt(address)

  @overload(WAIT['QV4.PropertyKey'])
  def resolveExport(self, key: QV4.PropertyKey) -> Optional[QV4.Value]:
    """
    Calls Qt's 'const Value *QV4::Module::resolveExport(PropertyKey key)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-module.html#resolveExport

    Parameters
    ----------

    key : QV4.PropertyKey
      Passed on as a value: Qt reads the C++ QV4::PropertyKey, which stays
      Python's own.

    Returns
    -------

    Optional[QV4.Value]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const Value *QV4::Module::resolveExport(PropertyKey key) const
    address = self.uglySide.call(
        'ritual_ZNK3QV46Module13resolveExportENS_11PropertyKeyE',
        self._valueOf(key),
    )
    return QV4.Value._cuteAt(address)

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
    Calls Qt's 'void QV4::Module::__dataTest()'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-module.html#__dataTest
    """
    #  void QV4::Module::__dataTest()
    self.uglySide.call('ritual_ZN3QV46Module10__dataTestEv')

  def evaluate(self) -> None:
    """
    Calls Qt's 'void QV4::Module::evaluate()'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-module.html#evaluate
    """
    #  void QV4::Module::evaluate()
    self.uglySide.call('ritual_ZN3QV46Module8evaluateEv')
