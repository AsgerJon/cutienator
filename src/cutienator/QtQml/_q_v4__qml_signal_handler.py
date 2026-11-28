"""
QV4::QmlSignalHandler binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4qobjectwrapper_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QV4::QmlSignalHandler to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QmlSignalHandler(QV4.Object):
  """
  The cute side of Qt's QV4::QmlSignalHandler: a plain Python object standing
  in front of one C++ QV4::QmlSignalHandler.

  It is built on the cute 'QV4::Object', as Qt's QV4::QmlSignalHandler is
  built on Qt's QV4::Object, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QV4::QmlSignalHandler that has a ritual and that
  Python can call so far, 9 names in all: '__dataTest', 'd_unchecked', 'd',
  'defaultPrototype', 'virtualDestroy', 'signalIndex', 'object', 'call',
  'initProto'. None can be made from Python: one comes out of a function of
  another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QV4::VTable *QV4::QmlSignalHandler::staticVTable()': gives
    'QV4::VTable', which has no cute class yet.

  What has no ritual
  ------------------

  4 of the 14 functions Qt declares: 3 forbidden; 1 not a gap.

  What to expect
  --------------

  - The C++ QV4::QmlSignalHandler is created at the first use, not by
    'QV4::QmlSignalHandler(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QV4::QmlSignalHandler.
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
    *QV4::QmlSignalHandler::defaultPrototype(QV4::ExecutionEngine *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-qmlsignalhandler.html#defaultPrototype

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
    #  QV4::Object
    #      *QV4::QmlSignalHandler::defaultPrototype(QV4::ExecutionEngine *e)
    address = Rituals.call(
        'ritual_ZN3QV416QmlSignalHandler16defaultPrototypeEPNS_15ExecutionE'
        'ngineE',
        CuteMixin._addressOf(e),
    )
    return QV4.Object._cuteAt(address)

  @staticmethod
  @overload(WAIT['QV4.Heap.Base'])
  @overload(NoneType)
  def virtualDestroy(b: Optional[QV4.Heap.Base]) -> None:
    """
    Calls Qt's 'void QV4::QmlSignalHandler::virtualDestroy(QV4::Heap::Base
    *b)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-qmlsignalhandler.html#virtualDestroy

    Parameters
    ----------

    b : Optional[QV4.Heap.Base]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::QmlSignalHandler::virtualDestroy(QV4::Heap::Base *b)
    Rituals.call(
        'ritual_ZN3QV416QmlSignalHandler14virtualDestroyEPNS_4Heap4BaseE',
        CuteMixin._addressOf(b),
    )

  @staticmethod
  @overload(WAIT['QV4.ExecutionEngine'])
  @overload(NoneType)
  def initProto(v4: Optional[QV4.ExecutionEngine]) -> None:
    """
    Calls Qt's 'void QV4::QmlSignalHandler::initProto(ExecutionEngine *v4)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-qmlsignalhandler.html#initProto

    Parameters
    ----------

    v4 : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::QmlSignalHandler::initProto(ExecutionEngine *v4)
    Rituals.call(
        'ritual_ZN3QV416QmlSignalHandler9initProtoEPNS_15ExecutionEngineE',
        CuteMixin._addressOf(v4),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::QmlSignalHandler'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def d_unchecked(self) -> Optional[QV4.Heap.QmlSignalHandler]:
    """
    Calls Qt's 'QV4::Heap::QmlSignalHandler
    *QV4::QmlSignalHandler::d_unchecked() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-qmlsignalhandler.html#d_unchecked

    Returns
    -------

    Optional[QV4.Heap.QmlSignalHandler]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::Heap::QmlSignalHandler *QV4::QmlSignalHandler::d_unchecked()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK3QV416QmlSignalHandler11d_uncheckedEv',
    )
    return QV4.Heap.QmlSignalHandler._cuteAt(address)

  def d(self) -> Optional[QV4.Heap.QmlSignalHandler]:
    """
    Calls Qt's 'QV4::Heap::QmlSignalHandler *QV4::QmlSignalHandler::d()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-qmlsignalhandler.html#d

    Returns
    -------

    Optional[QV4.Heap.QmlSignalHandler]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::Heap::QmlSignalHandler *QV4::QmlSignalHandler::d() const
    address = self.uglySide.call('ritual_ZNK3QV416QmlSignalHandler1dEv')
    return QV4.Heap.QmlSignalHandler._cuteAt(address)

  def signalIndex(self) -> int:
    """
    Calls Qt's 'int QV4::QmlSignalHandler::signalIndex() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-qmlsignalhandler.html#signalIndex
    """
    #  int QV4::QmlSignalHandler::signalIndex() const
    return self.uglySide.call(
        'ritual_ZNK3QV416QmlSignalHandler11signalIndexEv',
    )

  def object(self) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QV4::QmlSignalHandler::object() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-qmlsignalhandler.html#object

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QV4::QmlSignalHandler::object() const
    address = self.uglySide.call('ritual_ZNK3QV416QmlSignalHandler6objectEv')
    from ..QtCore import QObject
    return QObject._cuteAt(address)

  @overload(QV4.Value, QV4.Value, int)
  @overload(QV4.Value, NoneType, int)
  @overload(NoneType, QV4.Value, int)
  @overload(NoneType, NoneType, int)
  def call(
      self,
      thisObject: Optional[QV4.Value],
      argv: Optional[QV4.Value],
      argc: int,
  ) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::QmlSignalHandler::call(const Value
    *thisObject, const Value *argv, int argc) const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-qmlsignalhandler.html#call

    Parameters
    ----------

    thisObject : Optional[QV4.Value]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    argv : Optional[QV4.Value]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    argc : int
      Passed on as it is.
    """
    #  ReturnedValue QV4::QmlSignalHandler::call(const Value *thisObject,
    #      const Value *argv, int argc) const
    return self.uglySide.call(
        'ritual_ZNK3QV416QmlSignalHandler4callEPKNS_5ValueES3_i',
        self._addressOf(thisObject), self._addressOf(argv), argc,
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

  def __dataTest(self) -> None:
    """
    Calls Qt's 'void QV4::QmlSignalHandler::__dataTest()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-qmlsignalhandler.html#__dataTest
    """
    #  void QV4::QmlSignalHandler::__dataTest()
    self.uglySide.call('ritual_ZN3QV416QmlSignalHandler10__dataTestEv')
