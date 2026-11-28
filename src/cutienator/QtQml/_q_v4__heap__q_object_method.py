"""
QV4::Heap::QObjectMethod binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4qobjectwrapper_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QV4::Heap::QObjectMethod to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from . import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QObject
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMetaObject = WAIT['QMetaObject']
  QObject = WAIT['QObject']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QObjectMethod(QV4.Heap.FunctionObject, QV4.Heap.QObjectMethodData):
  """
  The cute side of Qt's QV4::Heap::QObjectMethod: a plain Python object
  standing in front of one C++ QV4::Heap::QObjectMethod.

  It is built on the cute 'QV4::Heap::FunctionObject', as Qt's
  QV4::Heap::QObjectMethod is built on Qt's QV4::Heap::FunctionObject, and
  has everything that class has. It is built on the cute
  'QV4::Heap::QObjectMethodData' as well, as Qt's QV4::Heap::QObjectMethod is
  built on Qt's QV4::Heap::QObjectMethodData too, and has everything that
  class has.

  What exists
  -----------

  Every function of Qt's QV4::Heap::QObjectMethod that has a ritual and that
  Python can call so far, 10 names in all: 'markObjects', 'init', 'destroy',
  'ensureMethodsCache', 'name', 'metaObject', 'object', 'isDetached',
  'isAttachedTo', 'checkThisObject'. None can be made from Python: one comes
  out of a function of another class that gives one back.

  What to expect
  --------------

  - The C++ QV4::Heap::QObjectMethod is created at the first use, not by
    'QV4::Heap::QObjectMethod(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QV4::Heap::QObjectMethod.
  """

  #  The enums Qt writes inside QV4::Heap::QObjectMethod, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class ThisObjectMode(CuteNum):
    """
    The enum 'QV4::Heap::QObjectMethod::ThisObjectMode' of Qt, with the 3
    names Qt gives in it.
    """

    Invalid = Kee[int](0)
    Included = Kee[int](1)
    Explicit = Kee[int](2)

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
    Calls Qt's 'void QV4::Heap::QObjectMethod::markObjects(Heap::Base *b,
    MarkStack *stack)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-qobjectmethod.html#markObjects

    Parameters
    ----------

    b : Optional[QV4.Heap.Base]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    stack : Optional[QV4.MarkStack]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::Heap::QObjectMethod::markObjects(Heap::Base *b, MarkStack
    #      *stack)
    Rituals.call(
        'ritual_ZN3QV44Heap13QObjectMethod11markObjectsEPNS0_4BaseEPNS_9Mar'
        'kStackE',
        CuteMixin._addressOf(b), CuteMixin._addressOf(stack),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::Heap::QObjectMethod'

  #  Qt's QV4::Heap::QObjectMethod is built on more than one class. The part
  #  of a C++ QV4::Heap::QObjectMethod that belongs to a class after the
  #  first begins somewhere inside the object, and the ritual named for that
  #  class gives where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QV4::Heap::QObjectMethodData':
          'ritual_cast_QV4_Heap_QObjectMethod_QV4_Heap_QObjectMethodData',
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def name(self) -> str:
    """
    Calls Qt's 'QString QV4::Heap::QObjectMethod::name() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-heap-qobjectmethod.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QV4::Heap::QObjectMethod::name() const
    return self.uglySide.call('ritual_ZNK3QV44Heap13QObjectMethod4nameEv')

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QV4::Heap::QObjectMethod::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-qobjectmethod.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QV4::Heap::QObjectMethod::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK3QV44Heap13QObjectMethod10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def object(self) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QV4::Heap::QObjectMethod::object() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-heap-qobjectmethod.html#object

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QV4::Heap::QObjectMethod::object() const
    address = self.uglySide.call(
        'ritual_ZNK3QV44Heap13QObjectMethod6objectEv',
    )
    from ..QtCore import QObject
    return QObject._cuteAt(address)

  def isDetached(self) -> bool:
    """
    Calls Qt's 'bool QV4::Heap::QObjectMethod::isDetached() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-qobjectmethod.html#isDetached
    """
    #  bool QV4::Heap::QObjectMethod::isDetached() const
    return self.uglySide.call(
        'ritual_ZNK3QV44Heap13QObjectMethod10isDetachedEv',
    )

  @overload(QObject)
  @overload(NoneType)
  def isAttachedTo(self, o: Optional[QObject]) -> bool:
    """
    Calls Qt's 'bool QV4::Heap::QObjectMethod::isAttachedTo(QObject *o)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-qobjectmethod.html#isAttachedTo

    Parameters
    ----------

    o : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QV4::Heap::QObjectMethod::isAttachedTo(QObject *o) const
    return self.uglySide.call(
        'ritual_ZNK3QV44Heap13QObjectMethod12isAttachedToEP7QObject',
        self._addressOf(o, 'QObject'),
    )

  @overload(QMetaObject)
  @overload(NoneType)
  def checkThisObject(
      self,
      thisMeta: Optional[QMetaObject],
  ) -> ThisObjectMode:
    """
    Calls Qt's 'QV4::Heap::QObjectMethod::ThisObjectMode
    QV4::Heap::QObjectMethod::checkThisObject(const QMetaObject *thisMeta)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-qobjectmethod.html#checkThisObject

    Parameters
    ----------

    thisMeta : Optional[QMetaObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    ThisObjectMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'ThisObjectMode(number)'
      gives.
    """
    #  QV4::Heap::QObjectMethod::ThisObjectMode
    #      QV4::Heap::QObjectMethod::checkThisObject(const QMetaObject
    #      *thisMeta) const
    return QObjectMethod.ThisObjectMode(self.uglySide.call(
        'ritual_ZNK3QV44Heap13QObjectMethod15checkThisObjectEPK11QMetaObjec'
        't',
        self._addressOf(thisMeta, 'QMetaObject'),
    ))

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

  @overload(WAIT['QV4.ExecutionEngine'], QV4.Heap.Object, int)
  @overload(WAIT['QV4.ExecutionEngine'], NoneType, int)
  @overload(NoneType, QV4.Heap.Object, int)
  @overload(NoneType, NoneType, int)
  def init(
      self,
      engine: Optional[QV4.ExecutionEngine],
      wrapper: Optional[QV4.Heap.Object],
      index: int,
  ) -> None:
    """
    Calls Qt's 'void QV4::Heap::QObjectMethod::init(QV4::ExecutionEngine
    *engine, Object *wrapper, int index)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-heap-qobjectmethod.html#init

    Parameters
    ----------

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    wrapper : Optional[QV4.Heap.Object]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    index : int
      Passed on as it is.
    """
    #  void QV4::Heap::QObjectMethod::init(QV4::ExecutionEngine *engine,
    #      Object *wrapper, int index)
    self.uglySide.call(
        'ritual_ZN3QV44Heap13QObjectMethod4initEPNS_15ExecutionEngineEPNS0_'
        '6ObjectEi',
        self._addressOf(engine), self._addressOf(wrapper), index,
    )

  def destroy(self) -> None:
    """
    Calls Qt's 'void QV4::Heap::QObjectMethod::destroy()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-qobjectmethod.html#destroy
    """
    #  void QV4::Heap::QObjectMethod::destroy()
    self.uglySide.call('ritual_ZN3QV44Heap13QObjectMethod7destroyEv')

  @overload(QMetaObject)
  @overload(NoneType)
  def ensureMethodsCache(self, thisMeta: Optional[QMetaObject]) -> None:
    """
    Calls Qt's 'void QV4::Heap::QObjectMethod::ensureMethodsCache(const
    QMetaObject *thisMeta)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-qobjectmethod.html#ensureMethodsCache

    Parameters
    ----------

    thisMeta : Optional[QMetaObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::Heap::QObjectMethod::ensureMethodsCache(const QMetaObject
    #      *thisMeta)
    self.uglySide.call(
        'ritual_ZN3QV44Heap13QObjectMethod18ensureMethodsCacheEPK11QMetaObj'
        'ect',
        self._addressOf(thisMeta, 'QMetaObject'),
    )
