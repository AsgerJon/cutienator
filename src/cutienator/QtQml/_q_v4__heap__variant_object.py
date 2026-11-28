"""
QV4::Heap::VariantObject binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4variantobject_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QV4::Heap::VariantObject to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from . import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QVariant


class VariantObject(QV4.Heap.Object):
  """
  The cute side of Qt's QV4::Heap::VariantObject: a plain Python object
  standing in front of one C++ QV4::Heap::VariantObject.

  It is built on the cute 'QV4::Heap::Object', as Qt's
  QV4::Heap::VariantObject is built on Qt's QV4::Heap::Object, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QV4::Heap::VariantObject that has a ritual and that
  Python can call so far, 4 names in all: 'init', 'data',
  'addVmePropertyReference', 'removeVmePropertyReference'. None can be made
  from Python: one comes out of a function of another class that gives one
  back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QVariant &QV4::Heap::VariantObject::data()': gives a type Python
    has no way to take yet.

  What has no ritual
  ------------------

  3 of the 8 functions Qt declares: 2 leans on 'QV4; 1 cannot be called and
  cannot be called through the meta-object and cannot be copied.

  What to expect
  --------------

  - The C++ QV4::Heap::VariantObject is created at the first use, not by
    'QV4::Heap::VariantObject(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QV4::Heap::VariantObject.
  - Each name of Qt's QV4::Heap::VariantObject that has no cute function yet,
    'isScarce', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::Heap::VariantObject'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def data(self) -> QVariant:
    """
    Calls Qt's 'const QVariant &QV4::Heap::VariantObject::data() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-heap-variantobject.html#data

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  const QVariant &QV4::Heap::VariantObject::data() const
    address = self.uglySide.call('ritual_ZNK3QV44Heap13VariantObject4dataEv')
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

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
    Calls Qt's 'void QV4::Heap::VariantObject::init()'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-heap-variantobject.html#init
    """
    #  void QV4::Heap::VariantObject::init()
    self.uglySide.call('ritual_ZN3QV44Heap13VariantObject4initEv')

  def addVmePropertyReference(self) -> None:
    """
    Calls Qt's 'void QV4::Heap::VariantObject::addVmePropertyReference()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-variantobject.html
    """
    #  void QV4::Heap::VariantObject::addVmePropertyReference()
    self.uglySide.call(
        'ritual_ZN3QV44Heap13VariantObject23addVmePropertyReferenceEv',
    )

  def removeVmePropertyReference(self) -> None:
    """
    Calls Qt's 'void QV4::Heap::VariantObject::removeVmePropertyReference()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-variantobject.html
    """
    #  void QV4::Heap::VariantObject::removeVmePropertyReference()
    self.uglySide.call(
        'ritual_ZN3QV44Heap13VariantObject26removeVmePropertyReferenceEv',
    )

  @staticmethod
  def isScarce(*__, **_) -> Never:
    """
    Qt's 'bool QV4::Heap::VariantObject::isScarce() const': cannot be called
    and cannot be called through the meta-object and cannot be copied: no
    header file has its code, Qt's source does not mark it or its class for
    use from outside Qt or writes it 'inline' or nowhere, and it is no
    signal, slot or invokable function giving back nothing, of a class built
    on QObject, and Qt's source has no code for it that could be told from
    the rest.
    """
    raise NotImplementedError(
        "'QV4.Heap.VariantObject.isScarce' has no cute function yet. Qt's "
        "'bool QV4::Heap::VariantObject::isScarce() const': cannot be "
        "called and cannot be called through the meta-object and cannot be "
        "copied: no header file has its code, Qt's source does not mark it "
        "or its class for use from outside Qt or writes it 'inline' or "
        "nowhere, and it is no signal, slot or invokable function giving "
        "back nothing, of a class built on QObject, and Qt's source has no "
        "code for it that could be told from the rest.")
