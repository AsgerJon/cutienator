"""
QV4::VariantObject binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4variantobject_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QV4::VariantObject to be private: it declares the class in a
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


class VariantObject(QV4.Object):
  """
  The cute side of Qt's QV4::VariantObject: a plain Python object standing in
  front of one C++ QV4::VariantObject.

  It is built on the cute 'QV4::Object', as Qt's QV4::VariantObject is built
  on Qt's QV4::Object, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QV4::VariantObject that has a ritual and that Python
  can call so far, 7 names in all: '__dataTest', 'd_unchecked', 'd',
  'defaultPrototype', 'addVmePropertyReference',
  'removeVmePropertyReference', 'virtualIsEqualTo'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QV4::VTable *QV4::VariantObject::staticVTable()': gives
    'QV4::VTable', which has no cute class yet.

  What has no ritual
  ------------------

  5 of the 13 functions Qt declares: 3 forbidden; 1 not a gap; 1 leans on
  'QV4.

  What to expect
  --------------

  - The C++ QV4::VariantObject is created at the first use, not by
    'QV4::VariantObject(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QV4::VariantObject.
  - Each name of Qt's QV4::VariantObject that has no cute function yet,
    'virtualDestroy', holds a function that raises 'NotImplementedError', and
    its docstring says why.
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
    *QV4::VariantObject::defaultPrototype(QV4::ExecutionEngine *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-variantobject.html#defaultPrototype

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
    #  QV4::Object *QV4::VariantObject::defaultPrototype(QV4::ExecutionEngine
    #      *e)
    address = Rituals.call(
        'ritual_ZN3QV413VariantObject16defaultPrototypeEPNS_15ExecutionEngi'
        'neE',
        CuteMixin._addressOf(e),
    )
    return QV4.Object._cuteAt(address)

  @staticmethod
  @overload(QV4.Managed, QV4.Managed)
  @overload(QV4.Managed, NoneType)
  @overload(NoneType, QV4.Managed)
  @overload(NoneType, NoneType)
  def virtualIsEqualTo(
      m: Optional[QV4.Managed],
      other: Optional[QV4.Managed],
  ) -> bool:
    """
    Calls Qt's 'bool QV4::VariantObject::virtualIsEqualTo(Managed *m, Managed
    *other)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-variantobject.html#virtualIsEqualTo

    Parameters
    ----------

    m : Optional[QV4.Managed]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    other : Optional[QV4.Managed]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QV4::VariantObject::virtualIsEqualTo(Managed *m, Managed *other)
    return Rituals.call(
        'ritual_ZN3QV413VariantObject16virtualIsEqualToEPNS_7ManagedES2_',
        CuteMixin._addressOf(m), CuteMixin._addressOf(other),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::VariantObject'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def d_unchecked(self) -> Optional[QV4.Heap.VariantObject]:
    """
    Calls Qt's 'QV4::Heap::VariantObject *QV4::VariantObject::d_unchecked()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-variantobject.html#d_unchecked

    Returns
    -------

    Optional[QV4.Heap.VariantObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::Heap::VariantObject *QV4::VariantObject::d_unchecked() const
    address = self.uglySide.call(
        'ritual_ZNK3QV413VariantObject11d_uncheckedEv',
    )
    return QV4.Heap.VariantObject._cuteAt(address)

  def d(self) -> Optional[QV4.Heap.VariantObject]:
    """
    Calls Qt's 'QV4::Heap::VariantObject *QV4::VariantObject::d() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-variantobject.html#d

    Returns
    -------

    Optional[QV4.Heap.VariantObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::Heap::VariantObject *QV4::VariantObject::d() const
    address = self.uglySide.call('ritual_ZNK3QV413VariantObject1dEv')
    return QV4.Heap.VariantObject._cuteAt(address)

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
    Calls Qt's 'void QV4::VariantObject::__dataTest()'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-variantobject.html#__dataTest
    """
    #  void QV4::VariantObject::__dataTest()
    self.uglySide.call('ritual_ZN3QV413VariantObject10__dataTestEv')

  def addVmePropertyReference(self) -> None:
    """
    Calls Qt's 'void QV4::VariantObject::addVmePropertyReference() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-variantobject.html#addVmePropertyReference
    """
    #  void QV4::VariantObject::addVmePropertyReference() const
    self.uglySide.call(
        'ritual_ZNK3QV413VariantObject23addVmePropertyReferenceEv',
    )

  def removeVmePropertyReference(self) -> None:
    """
    Calls Qt's 'void QV4::VariantObject::removeVmePropertyReference() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-variantobject.html#removeVmePropertyReference
    """
    #  void QV4::VariantObject::removeVmePropertyReference() const
    self.uglySide.call(
        'ritual_ZNK3QV413VariantObject26removeVmePropertyReferenceEv',
    )

  @staticmethod
  def virtualDestroy(*__, **_) -> Never:
    """
    Qt's 'void QV4::VariantObject::virtualDestroy(QV4::Heap::Base *b)': leans
    on 'QV4::Heap::VariantObject::isScarce() const', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QV4.VariantObject.virtualDestroy' has no cute function yet. Qt's "
        "'void QV4::VariantObject::virtualDestroy(QV4::Heap::Base *b)': "
        "leans on 'QV4::Heap::VariantObject::isScarce() const', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")
