"""
QV4::QmlContext binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4qmlcontext_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QV4::QmlContext to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QmlContext(QV4.ExecutionContext):
  """
  The cute side of Qt's QV4::QmlContext: a plain Python object standing in
  front of one C++ QV4::QmlContext.

  It is built on the cute 'QV4::ExecutionContext', as Qt's QV4::QmlContext is
  built on Qt's QV4::ExecutionContext, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QV4::QmlContext that has a ritual and that Python
  can call so far, 5 names in all: '__dataTest', 'd_unchecked', 'd',
  'defaultInternalClass', 'qmlScope'. None can be made from Python: one comes
  out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QV4::VTable *QV4::QmlContext::staticVTable()': gives
    'QV4::VTable', which has no cute class yet.
  - Qt's 'Heap::QmlContext *QV4::QmlContext::create(QV4::ExecutionContext
    *parent, QQmlRefPointer<QQmlContextData> context, QObject *scopeObject)':
    takes a type Python has no way to hand over yet.
  - Qt's 'QQmlRefPointer<QQmlContextData> QV4::QmlContext::qmlContext()
    const': gives a type Python has no way to take yet.

  What has no ritual
  ------------------

  4 of the 12 functions Qt declares: 3 forbidden; 1 not a gap.

  What to expect
  --------------

  - The C++ QV4::QmlContext is created at the first use, not by
    'QV4::QmlContext(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QV4::QmlContext.
  - Each name of Qt's QV4::QmlContext that has no cute function yet,
    'create', 'qmlContext', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(WAIT['QV4.EngineBase'])
  @overload(NoneType)
  def defaultInternalClass(
      e: Optional[QV4.EngineBase],
  ) -> Optional[QV4.Heap.InternalClass]:
    """
    Calls Qt's 'Heap::InternalClass
    *QV4::QmlContext::defaultInternalClass(QV4::EngineBase *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-qmlcontext.html#defaultInternalClass

    Parameters
    ----------

    e : Optional[QV4.EngineBase]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QV4.Heap.InternalClass]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Heap::InternalClass
    #      *QV4::QmlContext::defaultInternalClass(QV4::EngineBase *e)
    address = Rituals.call(
        'ritual_ZN3QV410QmlContext20defaultInternalClassEPNS_10EngineBaseE',
        CuteMixin._addressOf(e),
    )
    return QV4.Heap.InternalClass._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::QmlContext'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def d_unchecked(self) -> Optional[QV4.Heap.QmlContext]:
    """
    Calls Qt's 'QV4::Heap::QmlContext *QV4::QmlContext::d_unchecked() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-qmlcontext.html#d_unchecked

    Returns
    -------

    Optional[QV4.Heap.QmlContext]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::Heap::QmlContext *QV4::QmlContext::d_unchecked() const
    address = self.uglySide.call('ritual_ZNK3QV410QmlContext11d_uncheckedEv')
    return QV4.Heap.QmlContext._cuteAt(address)

  def d(self) -> Optional[QV4.Heap.QmlContext]:
    """
    Calls Qt's 'QV4::Heap::QmlContext *QV4::QmlContext::d() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-qmlcontext.html#d

    Returns
    -------

    Optional[QV4.Heap.QmlContext]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::Heap::QmlContext *QV4::QmlContext::d() const
    address = self.uglySide.call('ritual_ZNK3QV410QmlContext1dEv')
    return QV4.Heap.QmlContext._cuteAt(address)

  def qmlScope(self) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QV4::QmlContext::qmlScope() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-qmlcontext.html#qmlScope

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QV4::QmlContext::qmlScope() const
    address = self.uglySide.call('ritual_ZNK3QV410QmlContext8qmlScopeEv')
    from ..QtCore import QObject
    return QObject._cuteAt(address)

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
    Calls Qt's 'void QV4::QmlContext::__dataTest()'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-qmlcontext.html#__dataTest
    """
    #  void QV4::QmlContext::__dataTest()
    self.uglySide.call('ritual_ZN3QV410QmlContext10__dataTestEv')

  @staticmethod
  def create(*__, **_) -> Never:
    """
    Qt's 'Heap::QmlContext *QV4::QmlContext::create(QV4::ExecutionContext
    *parent, QQmlRefPointer<QQmlContextData> context, QObject *scopeObject)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QV4.QmlContext.create' has no cute function yet. Qt's "
        "'Heap::QmlContext *QV4::QmlContext::create(QV4::ExecutionContext "
        "*parent, QQmlRefPointer<QQmlContextData> context, QObject "
        "*scopeObject)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def qmlContext(*__, **_) -> Never:
    """
    Qt's 'QQmlRefPointer<QQmlContextData> QV4::QmlContext::qmlContext()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QV4.QmlContext.qmlContext' has no cute function yet. Qt's "
        "'QQmlRefPointer<QQmlContextData> QV4::QmlContext::qmlContext() "
        "const': gives a type Python has no way to take yet.")
