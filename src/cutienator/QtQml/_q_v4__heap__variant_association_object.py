"""
QV4::Heap::VariantAssociationObject binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4variantassociationobject_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QV4::Heap::VariantAssociationObject to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QHash, QMap
from . import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QVariant
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class VariantAssociationObject(QV4.Heap.ReferenceObject, QV4.Heap.VariantAssociationObjectData):
  """
  The cute side of Qt's QV4::Heap::VariantAssociationObject: a plain Python
  object standing in front of one C++ QV4::Heap::VariantAssociationObject.

  It is built on the cute 'QV4::Heap::ReferenceObject', as Qt's
  QV4::Heap::VariantAssociationObject is built on Qt's
  QV4::Heap::ReferenceObject, and has everything that class has. It is built
  on the cute 'QV4::Heap::VariantAssociationObjectData' as well, as Qt's
  QV4::Heap::VariantAssociationObject is built on Qt's
  QV4::Heap::VariantAssociationObjectData too, and has everything that class
  has.

  What exists
  -----------

  Every function of Qt's QV4::Heap::VariantAssociationObject that has a
  ritual and that Python can call so far, 3 names in all: 'markObjects',
  'init', 'setVariant'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QV4::Heap::VariantAssociationObject::storagePointer()': gives
    'void', which has no cute class yet.

  What has no ritual
  ------------------

  5 of the 10 functions Qt declares: 4 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 1 a template.

  What to expect
  --------------

  - The C++ QV4::Heap::VariantAssociationObject is created at the first use,
    not by 'QV4::Heap::VariantAssociationObject(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QV4::Heap::VariantAssociationObject.
  - Each name of Qt's QV4::Heap::VariantAssociationObject that has no cute
    function yet, 'createElementWrappers', 'detached', 'getElement',
    'storagePointer', 'toVariant', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QV4::Heap::VariantAssociationObject, each a
  #  class in here as in C++, and the names Qt has for the combinations of
  #  its flags enums.

  class AssociationType(CuteNum, scoped=True):
    """
    The enum 'QV4::Heap::VariantAssociationObject::AssociationType' of Qt,
    with the 2 names Qt gives in it. C++ keeps these names inside the enum,
    so the class that holds the enum does not have them.
    """

    VariantMap = Kee[int](0)
    VariantHash = Kee[int](1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QV4.Heap.Base, WAIT['QV4.MarkStack'])
  @overload(QV4.Heap.Base, NoneType)
  @overload(NoneType, WAIT['QV4.MarkStack'])
  @overload(NoneType, NoneType)
  def markObjects(
      b: Optional[QV4.Heap.Base],
      stack: Optional[QV4.MarkStack],
  ) -> None:
    """
    Calls Qt's 'void
    QV4::Heap::VariantAssociationObject::markObjects(Heap::Base *b, MarkStack
    *stack)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-variantassociationobject.html#markObjects

    Parameters
    ----------

    b : Optional[QV4.Heap.Base]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    stack : Optional[QV4.MarkStack]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::Heap::VariantAssociationObject::markObjects(Heap::Base *b,
    #      MarkStack *stack)
    Rituals.call(
        'ritual_ZN3QV44Heap24VariantAssociationObject11markObjectsEPNS0_4Ba'
        'seEPNS_9MarkStackE',
        CuteMixin._addressOf(b), CuteMixin._addressOf(stack),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::Heap::VariantAssociationObject'

  #  Qt's QV4::Heap::VariantAssociationObject is built on more than one
  #  class. The part of a C++ QV4::Heap::VariantAssociationObject that
  #  belongs to a class after the first begins somewhere inside the object,
  #  and the ritual named for that class gives where; see
  #  'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QV4::Heap::VariantAssociationObjectData':
          'ritual_cast_QV4_Heap_VariantAssociationObject_QV4_Heap_VariantAssociationObjectData',
  }

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

  @overload(QVariant)
  def setVariant(self, variant: QVariant) -> bool:
    """
    Calls Qt's 'bool QV4::Heap::VariantAssociationObject::setVariant(const
    QVariant &variant)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-variantassociationobject.html#setVariant

    Parameters
    ----------

    variant : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  bool QV4::Heap::VariantAssociationObject::setVariant(const QVariant
    #      &variant)
    return self.uglySide.call(
        'ritual_ZN3QV44Heap24VariantAssociationObject10setVariantERK8QVaria'
        'nt',
        self._valueOf(variant),
    )

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

  @overload(
      QMap[str, QVariant], QV4.Heap.Object, int,
      QV4.Heap.ReferenceObject.Flags,
  )
  @overload(
      QMap[str, QVariant], NoneType, int, QV4.Heap.ReferenceObject.Flags,
  )
  def init(
      self,
      variantMap: QMap[str, QVariant],
      container: Optional[QV4.Heap.Object],
      property: int,
      flags: QV4.Heap.ReferenceObject.Flags,
  ) -> None:
    """
    Calls Qt's 'void QV4::Heap::VariantAssociationObject::init(const
    QVariantMap &variantMap, QV4::Heap::Object *container, int property,
    Heap::ReferenceObject::Flags flags)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-variantassociationobject.html#init

    Parameters
    ----------

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
    #  void QV4::Heap::VariantAssociationObject::init(const QVariantMap
    #      &variantMap, QV4::Heap::Object *container, int property,
    #      Heap::ReferenceObject::Flags flags)
    self.uglySide.call(
        'ritual_ZN3QV44Heap24VariantAssociationObject4initERK4QMapI7QString'
        '8QVariantEPNS0_6ObjectEi6QFlagsINS0_15ReferenceObject4FlagEE',
        self._valueOf(variantMap), self._addressOf(container), property,
        flags.value,
    )

  @overload(
      QHash[str, QVariant], QV4.Heap.Object, int,
      QV4.Heap.ReferenceObject.Flags,
  )
  @overload(
      QHash[str, QVariant], NoneType, int, QV4.Heap.ReferenceObject.Flags,
  )
  def init(
      self,
      variantHash: QHash[str, QVariant],
      container: Optional[QV4.Heap.Object],
      property: int,
      flags: QV4.Heap.ReferenceObject.Flags,
  ) -> None:
    """
    Calls Qt's 'void QV4::Heap::VariantAssociationObject::init(const
    QVariantHash &variantHash, QV4::Heap::Object *container, int property,
    Heap::ReferenceObject::Flags flags)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-variantassociationobject.html#init

    Parameters
    ----------

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
    #  void QV4::Heap::VariantAssociationObject::init(const QVariantHash
    #      &variantHash, QV4::Heap::Object *container, int property,
    #      Heap::ReferenceObject::Flags flags)
    self.uglySide.call(
        'ritual_ZN3QV44Heap24VariantAssociationObject4initERK5QHashI7QStrin'
        'g8QVariantEPNS0_6ObjectEi6QFlagsINS0_15ReferenceObject4FlagEE',
        self._valueOf(variantHash), self._addressOf(container), property,
        flags.value,
    )

  @staticmethod
  def createElementWrappers(*__, **_) -> Never:
    """
    Qt's 'QV4::Heap::VariantAssociationObject::createElementWrappers': a
    template: a pattern and no single function.
    """
    raise NotImplementedError(
        "'QV4.Heap.VariantAssociationObject.createElementWrappers' has no "
        "cute function yet. Qt's "
        "'QV4::Heap::VariantAssociationObject::createElementWrappers': a "
        "template: a pattern and no single function.")

  @staticmethod
  def detached(*__, **_) -> Never:
    """
    Qt's 'VariantAssociationObject
    *QV4::Heap::VariantAssociationObject::detached()': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: use of undeclared identifier 'visitVariantAssociation'.
    """
    raise NotImplementedError(
        "'QV4.Heap.VariantAssociationObject.detached' has no cute function "
        "yet. Qt's 'VariantAssociationObject "
        "*QV4::Heap::VariantAssociationObject::detached()': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: use of undeclared identifier "
        "'visitVariantAssociation'.")

  @staticmethod
  def getElement(*__, **_) -> Never:
    """
    Qt's 'QV4::ReturnedValue
    QV4::Heap::VariantAssociationObject::getElement(const QString &id, bool
    *hasProperty)': Qt's library has no name for it, and its code in Qt's
    source does not compile apart from its file: use of undeclared identifier
    'visitVariantAssociation'.
    """
    raise NotImplementedError(
        "'QV4.Heap.VariantAssociationObject.getElement' has no cute "
        "function yet. Qt's 'QV4::ReturnedValue "
        "QV4::Heap::VariantAssociationObject::getElement(const QString &id, "
        "bool *hasProperty)': Qt's library has no name for it, and its code "
        "in Qt's source does not compile apart from its file: use of "
        "undeclared identifier 'visitVariantAssociation'.")

  @staticmethod
  def storagePointer(*__, **_) -> Never:
    """
    Qt's 'void *QV4::Heap::VariantAssociationObject::storagePointer()': gives
    'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QV4.Heap.VariantAssociationObject.storagePointer' has no cute "
        "function yet. Qt's 'void "
        "*QV4::Heap::VariantAssociationObject::storagePointer()': gives "
        "'void', which has no cute class yet.")

  @staticmethod
  def toVariant(*__, **_) -> Never:
    """
    Qt's 'QVariant QV4::Heap::VariantAssociationObject::toVariant()': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier
    'visitVariantAssociation'.
    """
    raise NotImplementedError(
        "'QV4.Heap.VariantAssociationObject.toVariant' has no cute function "
        "yet. Qt's 'QVariant "
        "QV4::Heap::VariantAssociationObject::toVariant()': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: use of undeclared identifier "
        "'visitVariantAssociation'.")
