"""
QV4::Heap::QQmlDelegateModelItemObject binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlModels/6.12.0/QtQmlModels/private/qqmldelegatemodel_p_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QV4::Heap::QQmlDelegateModelItemObject to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtQml import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QQmlDelegateModelItem
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQmlDelegateModelItem = WAIT['QQmlDelegateModelItem']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlDelegateModelItemObject(QV4.Heap.Object):
  """
  The cute side of Qt's QV4::Heap::QQmlDelegateModelItemObject: a plain
  Python object standing in front of one C++
  QV4::Heap::QQmlDelegateModelItemObject.

  It is built on the cute 'QV4::Heap::Object', as Qt's
  QV4::Heap::QQmlDelegateModelItemObject is built on Qt's QV4::Heap::Object,
  and has everything that class has.

  What exists
  -----------

  Every function of Qt's QV4::Heap::QQmlDelegateModelItemObject that has a
  ritual and that Python can call so far, 3 names in all: 'init', 'destroy',
  'item'. None can be made from Python: one comes out of a function of
  another class that gives one back.

  What to expect
  --------------

  - The C++ QV4::Heap::QQmlDelegateModelItemObject is created at the first
    use, not by 'QV4::Heap::QQmlDelegateModelItemObject(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QV4::Heap::QQmlDelegateModelItemObject.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::Heap::QQmlDelegateModelItemObject'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def item(self) -> Optional[QQmlDelegateModelItem]:
    """
    Calls Qt's 'QQmlDelegateModelItem
    *QV4::Heap::QQmlDelegateModelItemObject::item() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-qqmldelegatemodelitemobject.html#item

    Returns
    -------

    Optional[QQmlDelegateModelItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlDelegateModelItem *QV4::Heap::QQmlDelegateModelItemObject::item()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK3QV44Heap27QQmlDelegateModelItemObject4itemEv',
    )
    from . import QQmlDelegateModelItem
    return QQmlDelegateModelItem._cuteAt(address)

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

  @overload(QQmlDelegateModelItem)
  @overload(NoneType)
  def init(self, item: Optional[QQmlDelegateModelItem]) -> None:
    """
    Calls Qt's 'void
    QV4::Heap::QQmlDelegateModelItemObject::init(QQmlDelegateModelItem
    *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-qqmldelegatemodelitemobject.html#init

    Parameters
    ----------

    item : Optional[QQmlDelegateModelItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void
    #      QV4::Heap::QQmlDelegateModelItemObject::init(QQmlDelegateModelItem
    #      *item)
    self.uglySide.call(
        'ritual_ZN3QV44Heap27QQmlDelegateModelItemObject4initEP21QQmlDelega'
        'teModelItem',
        self._addressOf(item),
    )

  def destroy(self) -> None:
    """
    Calls Qt's 'void QV4::Heap::QQmlDelegateModelItemObject::destroy()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-qqmldelegatemodelitemobject.html#destroy
    """
    #  void QV4::Heap::QQmlDelegateModelItemObject::destroy()
    self.uglySide.call(
        'ritual_ZN3QV44Heap27QQmlDelegateModelItemObject7destroyEv',
    )
