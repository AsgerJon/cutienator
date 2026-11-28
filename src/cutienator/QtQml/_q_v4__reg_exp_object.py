"""
QV4::RegExpObject binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4regexpobject_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QV4::RegExpObject to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from . import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QRegularExpression

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class RegExpObject(QV4.Object):
  """
  The cute side of Qt's QV4::RegExpObject: a plain Python object standing in
  front of one C++ QV4::RegExpObject.

  It is built on the cute 'QV4::Object', as Qt's QV4::RegExpObject is built
  on Qt's QV4::Object, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QV4::RegExpObject that has a ritual and that Python
  can call so far, 12 names in all: '__dataTest', 'd_unchecked', 'd',
  'defaultInternalClass', 'defaultPrototype', 'initProperties', 'lastIndex',
  'setLastIndex', 'toQRegularExpression', 'toString', 'source',
  'builtinExec'. None can be made from Python: one comes out of a function of
  another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QV4::VTable *QV4::RegExpObject::staticVTable()': gives
    'QV4::VTable', which has no cute class yet.

  What has no ritual
  ------------------

  9 of the 22 functions Qt declares: 5 a template; 3 forbidden; 1 not a gap.

  What to expect
  --------------

  - The C++ QV4::RegExpObject is created at the first use, not by
    'QV4::RegExpObject(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QV4::RegExpObject.
  - Each name of Qt's QV4::RegExpObject that has no cute function yet,
    'flags', 'global_', 'sticky', 'unicode', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QV4::RegExpObject, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class Flags(CuteNum):
    """
    The enum 'QV4::RegExpObject::Flags' of Qt, with the 5 names Qt gives in
    it.
    """

    RegExp_Global = Kee[int](1)
    RegExp_IgnoreCase = Kee[int](2)
    RegExp_Multiline = Kee[int](4)
    RegExp_Unicode = Kee[int](8)
    RegExp_Sticky = Kee[int](16)

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
    *QV4::RegExpObject::defaultInternalClass(QV4::EngineBase *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-regexpobject.html#defaultInternalClass

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
    #      *QV4::RegExpObject::defaultInternalClass(QV4::EngineBase *e)
    address = Rituals.call(
        'ritual_ZN3QV412RegExpObject20defaultInternalClassEPNS_10EngineBase'
        'E',
        CuteMixin._addressOf(e),
    )
    return QV4.Heap.InternalClass._cuteAt(address)

  @staticmethod
  @overload(WAIT['QV4.ExecutionEngine'])
  @overload(NoneType)
  def defaultPrototype(
      e: Optional[QV4.ExecutionEngine],
  ) -> Optional[QV4.Object]:
    """
    Calls Qt's 'QV4::Object
    *QV4::RegExpObject::defaultPrototype(QV4::ExecutionEngine *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-regexpobject.html#defaultPrototype

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
    #  QV4::Object *QV4::RegExpObject::defaultPrototype(QV4::ExecutionEngine
    #      *e)
    address = Rituals.call(
        'ritual_ZN3QV412RegExpObject16defaultPrototypeEPNS_15ExecutionEngin'
        'eE',
        CuteMixin._addressOf(e),
    )
    return QV4.Object._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::RegExpObject'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def d_unchecked(self) -> Optional[QV4.Heap.RegExpObject]:
    """
    Calls Qt's 'QV4::Heap::RegExpObject *QV4::RegExpObject::d_unchecked()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-regexpobject.html#d_unchecked

    Returns
    -------

    Optional[QV4.Heap.RegExpObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::Heap::RegExpObject *QV4::RegExpObject::d_unchecked() const
    address = self.uglySide.call(
        'ritual_ZNK3QV412RegExpObject11d_uncheckedEv',
    )
    return QV4.Heap.RegExpObject._cuteAt(address)

  def d(self) -> Optional[QV4.Heap.RegExpObject]:
    """
    Calls Qt's 'QV4::Heap::RegExpObject *QV4::RegExpObject::d() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-regexpobject.html#d

    Returns
    -------

    Optional[QV4.Heap.RegExpObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::Heap::RegExpObject *QV4::RegExpObject::d() const
    address = self.uglySide.call('ritual_ZNK3QV412RegExpObject1dEv')
    return QV4.Heap.RegExpObject._cuteAt(address)

  def lastIndex(self) -> int:
    """
    Calls Qt's 'int QV4::RegExpObject::lastIndex() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-regexpobject.html#lastIndex
    """
    #  int QV4::RegExpObject::lastIndex() const
    return self.uglySide.call('ritual_ZNK3QV412RegExpObject9lastIndexEv')

  def toQRegularExpression(self) -> QRegularExpression:
    """
    Calls Qt's 'QRegularExpression QV4::RegExpObject::toQRegularExpression()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-regexpobject.html#toQRegularExpression

    Returns
    -------

    QRegularExpression
      A new cute QRegularExpression around the copy Qt gave back. Python owns
      it.
    """
    #  QRegularExpression QV4::RegExpObject::toQRegularExpression() const
    address = self.uglySide.call(
        'ritual_ZNK3QV412RegExpObject20toQRegularExpressionEv',
    )
    from ..QtCore import QRegularExpression
    return QRegularExpression._cuteOwning(address)

  def toString(self) -> str:
    """
    Calls Qt's 'QString QV4::RegExpObject::toString() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-regexpobject.html#toString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QV4::RegExpObject::toString() const
    return self.uglySide.call('ritual_ZNK3QV412RegExpObject8toStringEv')

  def source(self) -> str:
    """
    Calls Qt's 'QString QV4::RegExpObject::source() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-regexpobject.html#source

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QV4::RegExpObject::source() const
    return self.uglySide.call('ritual_ZNK3QV412RegExpObject6sourceEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setLastIndex(self, index: int) -> None:
    """
    Calls Qt's 'void QV4::RegExpObject::setLastIndex(int index)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-regexpobject.html#setLastIndex

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QV4::RegExpObject::setLastIndex(int index)
    self.uglySide.call('ritual_ZN3QV412RegExpObject12setLastIndexEi', index)

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
    Calls Qt's 'void QV4::RegExpObject::__dataTest()'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-regexpobject.html#__dataTest
    """
    #  void QV4::RegExpObject::__dataTest()
    self.uglySide.call('ritual_ZN3QV412RegExpObject10__dataTestEv')

  def initProperties(self) -> None:
    """
    Calls Qt's 'void QV4::RegExpObject::initProperties()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-regexpobject.html#initProperties
    """
    #  void QV4::RegExpObject::initProperties()
    self.uglySide.call('ritual_ZN3QV412RegExpObject14initPropertiesEv')

  @overload(WAIT['QV4.ExecutionEngine'], WAIT['QV4.String'])
  @overload(WAIT['QV4.ExecutionEngine'], NoneType)
  @overload(NoneType, WAIT['QV4.String'])
  @overload(NoneType, NoneType)
  def builtinExec(
      self,
      engine: Optional[QV4.ExecutionEngine],
      s: Optional[QV4.String],
  ) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::RegExpObject::builtinExec(ExecutionEngine
    *engine, const String *s)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-regexpobject.html#builtinExec

    Parameters
    ----------

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    s : Optional[QV4.String]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  ReturnedValue QV4::RegExpObject::builtinExec(ExecutionEngine *engine,
    #      const String *s)
    return self.uglySide.call(
        'ritual_ZN3QV412RegExpObject11builtinExecEPNS_15ExecutionEngineEPKN'
        'S_6StringE',
        self._addressOf(engine), self._addressOf(s),
    )

  @staticmethod
  def flags(*__, **_) -> Never:
    """
    Qt's 'QV4::RegExpObject::flags': a template: a pattern and no single
    function.
    """
    raise NotImplementedError(
        "'QV4.RegExpObject.flags' has no cute function yet. Qt's "
        "'QV4::RegExpObject::flags': a template: a pattern and no single "
        "function.")

  @staticmethod
  def global_(*__, **_) -> Never:
    """
    Qt's 'QV4::RegExpObject::global': a template: a pattern and no single
    function.
    """
    raise NotImplementedError(
        "'QV4.RegExpObject.global_' has no cute function yet. Qt's "
        "'QV4::RegExpObject::global': a template: a pattern and no single "
        "function.")

  @staticmethod
  def sticky(*__, **_) -> Never:
    """
    Qt's 'QV4::RegExpObject::sticky': a template: a pattern and no single
    function.
    """
    raise NotImplementedError(
        "'QV4.RegExpObject.sticky' has no cute function yet. Qt's "
        "'QV4::RegExpObject::sticky': a template: a pattern and no single "
        "function.")

  @staticmethod
  def unicode(*__, **_) -> Never:
    """
    Qt's 'QV4::RegExpObject::unicode': a template: a pattern and no single
    function.
    """
    raise NotImplementedError(
        "'QV4.RegExpObject.unicode' has no cute function yet. Qt's "
        "'QV4::RegExpObject::unicode': a template: a pattern and no single "
        "function.")
