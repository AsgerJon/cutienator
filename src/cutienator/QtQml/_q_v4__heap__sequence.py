"""
QV4::Heap::Sequence binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4sequenceobject_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QV4::Heap::Sequence to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from . import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaSequence, QMetaType, QVariant
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMetaSequence = WAIT['QMetaSequence']
  QMetaType = WAIT['QMetaType']
  QVariant = WAIT['QVariant']


class Sequence(QV4.Heap.ReferenceObject):
  """
  The cute side of Qt's QV4::Heap::Sequence: a plain Python object standing
  in front of one C++ QV4::Heap::Sequence.

  It is built on the cute 'QV4::Heap::ReferenceObject', as Qt's
  QV4::Heap::Sequence is built on Qt's QV4::Heap::ReferenceObject, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QV4::Heap::Sequence that has a ritual and that
  Python can call so far, 12 names in all: 'detached', 'destroy',
  'isStoredInline', 'isReadOnly', 'setVariant', 'toVariant', 'listType',
  'valueMetaType', 'metaSequence', 'initTypes', 'loadReference',
  'storeReference'. None can be made from Python: one comes out of a function
  of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QV4::Heap::Sequence::init(QMetaType listType, QMetaSequence
    metaSequence, const void *container)': names 'void', which has no cute
    class yet.
  - Qt's 'void QV4::Heap::Sequence::init(QMetaType listType, QMetaSequence
    metaSequence, const void *container, Object *object, int propertyIndex,
    Heap::ReferenceObject::Flags flags)': names 'void', which has no cute
    class yet.
  - Qt's 'void *QV4::Heap::Sequence::storagePointer()': gives 'void', which
    has no cute class yet.
  - Qt's 'const void *QV4::Heap::Sequence::storagePointer() const': gives
    'void', which has no cute class yet.
  - Qt's 'void QV4::Heap::Sequence::createInlineStorage(const void
    *container)': names 'void', which has no cute class yet.

  What has no ritual
  ------------------

  1 of the 18 functions Qt declares: 1 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QV4::Heap::Sequence is created at the first use, not by
    'QV4::Heap::Sequence(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QV4::Heap::Sequence.
  - Each name of Qt's QV4::Heap::Sequence that has no cute function yet,
    'createElementWrappers', 'createInlineStorage', 'storagePointer', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::Heap::Sequence'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isStoredInline(self) -> bool:
    """
    Calls Qt's 'bool QV4::Heap::Sequence::isStoredInline() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-sequence.html#isStoredInline
    """
    #  bool QV4::Heap::Sequence::isStoredInline() const
    return self.uglySide.call(
        'ritual_ZNK3QV44Heap8Sequence14isStoredInlineEv',
    )

  def isReadOnly(self) -> bool:
    """
    Calls Qt's 'bool QV4::Heap::Sequence::isReadOnly() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-heap-sequence.html#isReadOnly
    """
    #  bool QV4::Heap::Sequence::isReadOnly() const
    return self.uglySide.call('ritual_ZNK3QV44Heap8Sequence10isReadOnlyEv')

  def toVariant(self) -> QVariant:
    """
    Calls Qt's 'QVariant QV4::Heap::Sequence::toVariant() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-heap-sequence.html#toVariant

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QV4::Heap::Sequence::toVariant() const
    address = self.uglySide.call('ritual_ZNK3QV44Heap8Sequence9toVariantEv')
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def listType(self) -> QMetaType:
    """
    Calls Qt's 'QMetaType QV4::Heap::Sequence::listType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-heap-sequence.html#listType

    Returns
    -------

    QMetaType
      A new cute QMetaType around the copy Qt gave back. Python owns it.
    """
    #  QMetaType QV4::Heap::Sequence::listType() const
    address = self.uglySide.call('ritual_ZNK3QV44Heap8Sequence8listTypeEv')
    from ..QtCore import QMetaType
    return QMetaType._cuteOwning(address)

  def valueMetaType(self) -> QMetaType:
    """
    Calls Qt's 'QMetaType QV4::Heap::Sequence::valueMetaType() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-sequence.html#valueMetaType

    Returns
    -------

    QMetaType
      A new cute QMetaType around the copy Qt gave back. Python owns it.
    """
    #  QMetaType QV4::Heap::Sequence::valueMetaType() const
    address = self.uglySide.call(
        'ritual_ZNK3QV44Heap8Sequence13valueMetaTypeEv',
    )
    from ..QtCore import QMetaType
    return QMetaType._cuteOwning(address)

  def metaSequence(self) -> QMetaSequence:
    """
    Calls Qt's 'QMetaSequence QV4::Heap::Sequence::metaSequence() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-sequence.html#metaSequence

    Returns
    -------

    QMetaSequence
      A new cute QMetaSequence around the copy Qt gave back. Python owns it.
    """
    #  QMetaSequence QV4::Heap::Sequence::metaSequence() const
    address = self.uglySide.call(
        'ritual_ZNK3QV44Heap8Sequence12metaSequenceEv',
    )
    from ..QtCore import QMetaSequence
    return QMetaSequence._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QVariant)
  def setVariant(self, variant: QVariant) -> bool:
    """
    Calls Qt's 'bool QV4::Heap::Sequence::setVariant(const QVariant
    &variant)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-heap-sequence.html#setVariant

    Parameters
    ----------

    variant : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  bool QV4::Heap::Sequence::setVariant(const QVariant &variant)
    return self.uglySide.call(
        'ritual_ZN3QV44Heap8Sequence10setVariantERK8QVariant',
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

  def detached(self) -> Optional[Sequence]:
    """
    Calls Qt's 'Sequence *QV4::Heap::Sequence::detached()'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-heap-sequence.html#detached

    Returns
    -------

    Optional[Sequence]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Sequence *QV4::Heap::Sequence::detached()
    address = self.uglySide.call('ritual_ZN3QV44Heap8Sequence8detachedEv')
    return Sequence._cuteAt(address)

  def destroy(self) -> None:
    """
    Calls Qt's 'void QV4::Heap::Sequence::destroy()'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-heap-sequence.html#destroy
    """
    #  void QV4::Heap::Sequence::destroy()
    self.uglySide.call('ritual_ZN3QV44Heap8Sequence7destroyEv')

  @overload(QMetaType, QMetaSequence)
  def initTypes(
      self,
      listType: QMetaType,
      metaSequence: QMetaSequence,
  ) -> None:
    """
    Calls Qt's 'void QV4::Heap::Sequence::initTypes(QMetaType listType,
    QMetaSequence metaSequence)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-heap-sequence.html#initTypes

    Parameters
    ----------

    listType : QMetaType
      Passed on as a value: Qt reads the C++ QMetaType, which stays Python's
      own.

    metaSequence : QMetaSequence
      Passed on as a value: Qt reads the C++ QMetaSequence, which stays
      Python's own.
    """
    #  void QV4::Heap::Sequence::initTypes(QMetaType listType, QMetaSequence
    #      metaSequence)
    self.uglySide.call(
        'ritual_ZN3QV44Heap8Sequence9initTypesE9QMetaType13QMetaSequence',
        self._valueOf(listType), self._valueOf(metaSequence),
    )

  def loadReference(self) -> bool:
    """
    Calls Qt's 'bool QV4::Heap::Sequence::loadReference()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-sequence.html#loadReference
    """
    #  bool QV4::Heap::Sequence::loadReference()
    return self.uglySide.call('ritual_ZN3QV44Heap8Sequence13loadReferenceEv')

  def storeReference(self) -> bool:
    """
    Calls Qt's 'bool QV4::Heap::Sequence::storeReference()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-sequence.html#storeReference
    """
    #  bool QV4::Heap::Sequence::storeReference()
    return self.uglySide.call(
        'ritual_ZN3QV44Heap8Sequence14storeReferenceEv',
    )

  @staticmethod
  def createElementWrappers(*__, **_) -> Never:
    """
    Qt's 'void QV4::Heap::Sequence::createElementWrappers(const void
    *container)': Qt's library has no name for it, and its code in Qt's
    source does not compile apart from its file: use of undeclared identifier
    'generateWarning'.
    """
    raise NotImplementedError(
        "'QV4.Heap.Sequence.createElementWrappers' has no cute function "
        "yet. Qt's 'void QV4::Heap::Sequence::createElementWrappers(const "
        "void *container)': Qt's library has no name for it, and its code "
        "in Qt's source does not compile apart from its file: use of "
        "undeclared identifier 'generateWarning'.")

  @staticmethod
  def createInlineStorage(*__, **_) -> Never:
    """
    Qt's 'void QV4::Heap::Sequence::createInlineStorage(const void
    *container)': names 'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QV4.Heap.Sequence.createInlineStorage' has no cute function yet. "
        "Qt's 'void QV4::Heap::Sequence::createInlineStorage(const void "
        "*container)': names 'void', which has no cute class yet.")

  @staticmethod
  def storagePointer(*__, **_) -> Never:
    """
    - Qt's 'void *QV4::Heap::Sequence::storagePointer()': gives 'void', which
      has no cute class yet.
    - Qt's 'const void *QV4::Heap::Sequence::storagePointer() const': gives
      'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QV4.Heap.Sequence.storagePointer' has no cute function yet. Qt's "
        "'void *QV4::Heap::Sequence::storagePointer()': gives 'void', which "
        "has no cute class yet. Qt's 'const void "
        "*QV4::Heap::Sequence::storagePointer() const': gives 'void', which "
        "has no cute class yet.")
