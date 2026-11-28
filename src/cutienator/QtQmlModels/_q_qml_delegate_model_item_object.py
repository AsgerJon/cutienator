"""
QQmlDelegateModelItemObject binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlModels/6.12.0/QtQmlModels/private/qqmldelegatemodel_p_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQmlDelegateModelItemObject to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtQml import QV4
from . import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlDelegateModelItemObject(QV4.Object):
  """
  The cute side of Qt's QQmlDelegateModelItemObject: a plain Python object
  standing in front of one C++ QQmlDelegateModelItemObject.

  It is built on the cute 'QV4::Object', as Qt's QQmlDelegateModelItemObject
  is built on Qt's QV4::Object, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQmlDelegateModelItemObject that has a ritual and
  that Python can call so far, 4 names in all: '__dataTest', 'd_unchecked',
  'd', 'virtualDestroy'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has no ritual
  ------------------

  5 of the 9 functions Qt declares: 3 forbidden; 1 not a gap; 1 leans on
  'QQmlDelegateModelItemObject.

  What to expect
  --------------

  - The C++ QQmlDelegateModelItemObject is created at the first use, not by
    'QQmlDelegateModelItemObject(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlDelegateModelItemObject.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(WAIT['QV4.Heap.Base'])
  @overload(NoneType)
  def virtualDestroy(b: Optional[QV4.Heap.Base]) -> None:
    """
    Calls Qt's 'void
    QQmlDelegateModelItemObject::virtualDestroy(QV4::Heap::Base *b)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodelitemobject.html#virtualDestroy

    Parameters
    ----------

    b : Optional[QV4.Heap.Base]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlDelegateModelItemObject::virtualDestroy(QV4::Heap::Base *b)
    Rituals.call(
        'ritual_ZN27QQmlDelegateModelItemObject14virtualDestroyEPN3QV44Heap'
        '4BaseE',
        CuteMixin._addressOf(b),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlDelegateModelItemObject'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def d_unchecked(self) -> Optional[QV4.Heap.QQmlDelegateModelItemObject]:
    """
    Calls Qt's 'QV4::Heap::QQmlDelegateModelItemObject
    *QQmlDelegateModelItemObject::d_unchecked() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodelitemobject.html#d_unchecked

    Returns
    -------

    Optional[QV4.Heap.QQmlDelegateModelItemObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::Heap::QQmlDelegateModelItemObject
    #      *QQmlDelegateModelItemObject::d_unchecked() const
    address = self.uglySide.call(
        'ritual_ZNK27QQmlDelegateModelItemObject11d_uncheckedEv',
    )
    return QV4.Heap.QQmlDelegateModelItemObject._cuteAt(address)

  def d(self) -> Optional[QV4.Heap.QQmlDelegateModelItemObject]:
    """
    Calls Qt's 'QV4::Heap::QQmlDelegateModelItemObject
    *QQmlDelegateModelItemObject::d() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldelegatemodelitemobject.html#d

    Returns
    -------

    Optional[QV4.Heap.QQmlDelegateModelItemObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::Heap::QQmlDelegateModelItemObject
    #      *QQmlDelegateModelItemObject::d() const
    address = self.uglySide.call(
        'ritual_ZNK27QQmlDelegateModelItemObject1dEv',
    )
    return QV4.Heap.QQmlDelegateModelItemObject._cuteAt(address)

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
    Calls Qt's 'void QQmlDelegateModelItemObject::__dataTest()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodelitemobject.html#__dataTest
    """
    #  void QQmlDelegateModelItemObject::__dataTest()
    self.uglySide.call(
        'ritual_ZN27QQmlDelegateModelItemObject10__dataTestEv',
    )
