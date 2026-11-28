"""
QV4::VariantAssociationPrototype binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4variantassociationobject_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QV4::VariantAssociationPrototype to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QHash, QMap
from . import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QVariant
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class VariantAssociationPrototype(QV4.Object):
  """
  The cute side of Qt's QV4::VariantAssociationPrototype: a plain Python
  object standing in front of one C++ QV4::VariantAssociationPrototype.

  It is built on the cute 'QV4::Object', as Qt's
  QV4::VariantAssociationPrototype is built on Qt's QV4::Object, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QV4::VariantAssociationPrototype that has a ritual
  and that Python can call so far, 3 names in all: 'defaultPrototype',
  'fromQVariantMap', 'fromQVariantHash'. None can be made from Python: one
  comes out of a function of another class that gives one back.

  What to expect
  --------------

  - The C++ QV4::VariantAssociationPrototype is created at the first use, not
    by 'QV4::VariantAssociationPrototype(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QV4::VariantAssociationPrototype.
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
    *QV4::VariantAssociationPrototype::defaultPrototype(QV4::ExecutionEngine
    *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-variantassociationprototype.html

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
    #  QV4::Object *QV4::VariantAssociationPrototype::defaultPrototype(QV4::
    #      ExecutionEngine *e)
    address = Rituals.call(
        'ritual_ZN3QV427VariantAssociationPrototype16defaultPrototypeEPNS_1'
        '5ExecutionEngineE',
        CuteMixin._addressOf(e),
    )
    return QV4.Object._cuteAt(address)

  @staticmethod
  @overload(
      WAIT['QV4.ExecutionEngine'], QMap[str, QVariant],
      WAIT['QV4.Heap.Object'], int, QV4.Heap.ReferenceObject.Flags,
  )
  @overload(
      WAIT['QV4.ExecutionEngine'], QMap[str, QVariant], NoneType, int,
      QV4.Heap.ReferenceObject.Flags,
  )
  @overload(
      NoneType, QMap[str, QVariant], WAIT['QV4.Heap.Object'], int,
      QV4.Heap.ReferenceObject.Flags,
  )
  @overload(
      NoneType, QMap[str, QVariant], NoneType, int,
      QV4.Heap.ReferenceObject.Flags,
  )
  def fromQVariantMap(
      engine: Optional[QV4.ExecutionEngine],
      variantMap: QMap[str, QVariant],
      container: Optional[QV4.Heap.Object],
      property: int,
      flags: QV4.Heap.ReferenceObject.Flags,
  ) -> int:
    """
    Calls Qt's 'ReturnedValue
    QV4::VariantAssociationPrototype::fromQVariantMap(ExecutionEngine
    *engine, const QVariantMap &variantMap, QV4::Heap::Object *container, int
    property, Heap::ReferenceObject::Flags flags)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-variantassociationprototype.html

    Parameters
    ----------

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    variantMap : QMap[str, QVariant]
      Passed on as a map of Qt: Qt reads the C++ map, which stays Python's
      own. A dict of Python is made into one first, and refused when a key or
      a value does not fit.

    container : Optional[QV4.Heap.Object]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    property : int
      Passed on as it is.

    flags : QV4.Heap.ReferenceObject.Flags
      Passed on as its number.
    """
    #  ReturnedValue
    #      QV4::VariantAssociationPrototype::fromQVariantMap(ExecutionEngine
    #      *engine, const QVariantMap &variantMap, QV4::Heap::Object
    #      *container, int property, Heap::ReferenceObject::Flags flags)
    return Rituals.call(
        'ritual_ZN3QV427VariantAssociationPrototype15fromQVariantMapEPNS_15'
        'ExecutionEngineERK4QMapI7QString8QVariantEPNS_4Heap6ObjectEi6QFlag'
        'sINS9_15ReferenceObject4FlagEE',
        CuteMixin._addressOf(engine), CuteMixin._valueOf(variantMap),
        CuteMixin._addressOf(container), property, flags.value,
    )

  @staticmethod
  @overload(
      WAIT['QV4.ExecutionEngine'], QHash[str, QVariant],
      WAIT['QV4.Heap.Object'], int, QV4.Heap.ReferenceObject.Flags,
  )
  @overload(
      WAIT['QV4.ExecutionEngine'], QHash[str, QVariant], NoneType, int,
      QV4.Heap.ReferenceObject.Flags,
  )
  @overload(
      NoneType, QHash[str, QVariant], WAIT['QV4.Heap.Object'], int,
      QV4.Heap.ReferenceObject.Flags,
  )
  @overload(
      NoneType, QHash[str, QVariant], NoneType, int,
      QV4.Heap.ReferenceObject.Flags,
  )
  def fromQVariantHash(
      engine: Optional[QV4.ExecutionEngine],
      variantHash: QHash[str, QVariant],
      container: Optional[QV4.Heap.Object],
      property: int,
      flags: QV4.Heap.ReferenceObject.Flags,
  ) -> int:
    """
    Calls Qt's 'ReturnedValue
    QV4::VariantAssociationPrototype::fromQVariantHash(ExecutionEngine
    *engine, const QVariantHash &variantHash, QV4::Heap::Object *container,
    int property, Heap::ReferenceObject::Flags flags)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-variantassociationprototype.html

    Parameters
    ----------

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    variantHash : QHash[str, QVariant]
      Passed on as a map of Qt: Qt reads the C++ map, which stays Python's
      own. A dict of Python is made into one first, and refused when a key or
      a value does not fit.

    container : Optional[QV4.Heap.Object]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    property : int
      Passed on as it is.

    flags : QV4.Heap.ReferenceObject.Flags
      Passed on as its number.
    """
    #  ReturnedValue
    #      QV4::VariantAssociationPrototype::fromQVariantHash(ExecutionEngine
    #      *engine, const QVariantHash &variantHash, QV4::Heap::Object
    #      *container, int property, Heap::ReferenceObject::Flags flags)
    return Rituals.call(
        'ritual_ZN3QV427VariantAssociationPrototype16fromQVariantHashEPNS_1'
        '5ExecutionEngineERK5QHashI7QString8QVariantEPNS_4Heap6ObjectEi6QFl'
        'agsINS9_15ReferenceObject4FlagEE',
        CuteMixin._addressOf(engine), CuteMixin._valueOf(variantHash),
        CuteMixin._addressOf(container), property, flags.value,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::VariantAssociationPrototype'

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
