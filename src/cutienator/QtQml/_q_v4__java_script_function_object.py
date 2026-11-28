"""
QV4::JavaScriptFunctionObject binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4functionobject_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QV4::JavaScriptFunctionObject to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QQmlSourceLocation

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class JavaScriptFunctionObject(QV4.FunctionObject):
  """
  The cute side of Qt's QV4::JavaScriptFunctionObject: a plain Python object
  standing in front of one C++ QV4::JavaScriptFunctionObject.

  It is built on the cute 'QV4::FunctionObject', as Qt's
  QV4::JavaScriptFunctionObject is built on Qt's QV4::FunctionObject, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QV4::JavaScriptFunctionObject that has a ritual and
  that Python can call so far, 10 names in all: '__dataTest', 'd_unchecked',
  'd', 'virtualDestroy', 'scope', 'function', 'formalParameterCount',
  'varCount', 'strictMode', 'sourceLocation'. None can be made from Python:
  one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QV4::VTable *QV4::JavaScriptFunctionObject::staticVTable()':
    gives 'QV4::VTable', which has no cute class yet.

  What has no ritual
  ------------------

  4 of the 15 functions Qt declares: 3 forbidden; 1 not a gap.

  What to expect
  --------------

  - The C++ QV4::JavaScriptFunctionObject is created at the first use, not by
    'QV4::JavaScriptFunctionObject(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QV4::JavaScriptFunctionObject.
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
    QV4::JavaScriptFunctionObject::virtualDestroy(QV4::Heap::Base *b)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-javascriptfunctionobject.html#virtualDestroy

    Parameters
    ----------

    b : Optional[QV4.Heap.Base]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::JavaScriptFunctionObject::virtualDestroy(QV4::Heap::Base *b)
    Rituals.call(
        'ritual_ZN3QV424JavaScriptFunctionObject14virtualDestroyEPNS_4Heap4'
        'BaseE',
        CuteMixin._addressOf(b),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::JavaScriptFunctionObject'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def d_unchecked(self) -> Optional[QV4.Heap.JavaScriptFunctionObject]:
    """
    Calls Qt's 'QV4::Heap::JavaScriptFunctionObject
    *QV4::JavaScriptFunctionObject::d_unchecked() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-javascriptfunctionobject.html#d_unchecked

    Returns
    -------

    Optional[QV4.Heap.JavaScriptFunctionObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::Heap::JavaScriptFunctionObject
    #      *QV4::JavaScriptFunctionObject::d_unchecked() const
    address = self.uglySide.call(
        'ritual_ZNK3QV424JavaScriptFunctionObject11d_uncheckedEv',
    )
    return QV4.Heap.JavaScriptFunctionObject._cuteAt(address)

  def d(self) -> Optional[QV4.Heap.JavaScriptFunctionObject]:
    """
    Calls Qt's 'QV4::Heap::JavaScriptFunctionObject
    *QV4::JavaScriptFunctionObject::d() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-javascriptfunctionobject.html#d

    Returns
    -------

    Optional[QV4.Heap.JavaScriptFunctionObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::Heap::JavaScriptFunctionObject
    #      *QV4::JavaScriptFunctionObject::d() const
    address = self.uglySide.call(
        'ritual_ZNK3QV424JavaScriptFunctionObject1dEv',
    )
    return QV4.Heap.JavaScriptFunctionObject._cuteAt(address)

  def scope(self) -> Optional[QV4.Heap.ExecutionContext]:
    """
    Calls Qt's 'Heap::ExecutionContext
    *QV4::JavaScriptFunctionObject::scope() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-javascriptfunctionobject.html#scope

    Returns
    -------

    Optional[QV4.Heap.ExecutionContext]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Heap::ExecutionContext *QV4::JavaScriptFunctionObject::scope() const
    address = self.uglySide.call(
        'ritual_ZNK3QV424JavaScriptFunctionObject5scopeEv',
    )
    return QV4.Heap.ExecutionContext._cuteAt(address)

  def function(self) -> Optional[QV4.Function]:
    """
    Calls Qt's 'Function *QV4::JavaScriptFunctionObject::function() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-javascriptfunctionobject.html#function

    Returns
    -------

    Optional[QV4.Function]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Function *QV4::JavaScriptFunctionObject::function() const
    address = self.uglySide.call(
        'ritual_ZNK3QV424JavaScriptFunctionObject8functionEv',
    )
    return QV4.Function._cuteAt(address)

  def formalParameterCount(self) -> int:
    """
    Calls Qt's 'unsigned int
    QV4::JavaScriptFunctionObject::formalParameterCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-javascriptfunctionobject.html
    """
    #  unsigned int QV4::JavaScriptFunctionObject::formalParameterCount()
    #      const
    return self.uglySide.call(
        'ritual_ZNK3QV424JavaScriptFunctionObject20formalParameterCountEv',
    )

  def varCount(self) -> int:
    """
    Calls Qt's 'unsigned int QV4::JavaScriptFunctionObject::varCount()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-javascriptfunctionobject.html#varCount
    """
    #  unsigned int QV4::JavaScriptFunctionObject::varCount() const
    return self.uglySide.call(
        'ritual_ZNK3QV424JavaScriptFunctionObject8varCountEv',
    )

  def strictMode(self) -> bool:
    """
    Calls Qt's 'bool QV4::JavaScriptFunctionObject::strictMode() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-javascriptfunctionobject.html#strictMode
    """
    #  bool QV4::JavaScriptFunctionObject::strictMode() const
    return self.uglySide.call(
        'ritual_ZNK3QV424JavaScriptFunctionObject10strictModeEv',
    )

  def sourceLocation(self) -> QQmlSourceLocation:
    """
    Calls Qt's 'QQmlSourceLocation
    QV4::JavaScriptFunctionObject::sourceLocation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-javascriptfunctionobject.html#sourceLocation

    Returns
    -------

    QQmlSourceLocation
      A new cute QQmlSourceLocation around the copy Qt gave back. Python owns
      it.
    """
    #  QQmlSourceLocation QV4::JavaScriptFunctionObject::sourceLocation()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK3QV424JavaScriptFunctionObject14sourceLocationEv',
    )
    from . import QQmlSourceLocation
    return QQmlSourceLocation._cuteOwning(address)

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
    Calls Qt's 'void QV4::JavaScriptFunctionObject::__dataTest()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-javascriptfunctionobject.html#__dataTest
    """
    #  void QV4::JavaScriptFunctionObject::__dataTest()
    self.uglySide.call(
        'ritual_ZN3QV424JavaScriptFunctionObject10__dataTestEv',
    )
