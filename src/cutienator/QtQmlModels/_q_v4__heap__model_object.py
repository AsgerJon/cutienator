"""
QV4::Heap::ModelObject binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlModels/6.12.0/QtQmlModels/private/qqmllistmodel_p_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QV4::Heap::ModelObject to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtQml import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QObject
  from . import QQmlListModel
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QObject = WAIT['QObject']
  QQmlListModel = WAIT['QQmlListModel']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class ModelObject(QV4.Heap.QObjectWrapper):
  """
  The cute side of Qt's QV4::Heap::ModelObject: a plain Python object
  standing in front of one C++ QV4::Heap::ModelObject.

  It is built on the cute 'QV4::Heap::QObjectWrapper', as Qt's
  QV4::Heap::ModelObject is built on Qt's QV4::Heap::QObjectWrapper, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QV4::Heap::ModelObject that has a ritual and that
  Python can call so far, 3 names in all: 'init', 'destroy', 'elementIndex'.
  None can be made from Python: one comes out of a function of another class
  that gives one back.

  What to expect
  --------------

  - The C++ QV4::Heap::ModelObject is created at the first use, not by
    'QV4::Heap::ModelObject(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QV4::Heap::ModelObject.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::Heap::ModelObject'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def elementIndex(self) -> int:
    """
    Calls Qt's 'int QV4::Heap::ModelObject::elementIndex() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-modelobject.html#elementIndex
    """
    #  int QV4::Heap::ModelObject::elementIndex() const
    return self.uglySide.call(
        'ritual_ZNK3QV44Heap11ModelObject12elementIndexEv',
    )

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

  @overload(QObject, QQmlListModel)
  @overload(QObject, NoneType)
  @overload(NoneType, QQmlListModel)
  @overload(NoneType, NoneType)
  def init(
      self,
      object: Optional[QObject],
      model: Optional[QQmlListModel],
  ) -> None:
    """
    Calls Qt's 'void QV4::Heap::ModelObject::init(QObject *object,
    QQmlListModel *model)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-heap-modelobject.html#init

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    model : Optional[QQmlListModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::Heap::ModelObject::init(QObject *object, QQmlListModel
    #      *model)
    self.uglySide.call(
        'ritual_ZN3QV44Heap11ModelObject4initEP7QObjectP13QQmlListModel',
        self._addressOf(object, 'QObject'), self._addressOf(model),
    )

  def destroy(self) -> None:
    """
    Calls Qt's 'void QV4::Heap::ModelObject::destroy()'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-heap-modelobject.html#destroy
    """
    #  void QV4::Heap::ModelObject::destroy()
    self.uglySide.call('ritual_ZN3QV44Heap11ModelObject7destroyEv')
