"""
QtMetaContainerPrivate::Sequence binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qmetasequence.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from . import QMetaType, QVariant
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QVariant = WAIT['QVariant']


class Sequence(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QtMetaContainerPrivate::Sequence: a plain Python
  object standing in front of one C++ QtMetaContainerPrivate::Sequence.

  C++ hands a QtMetaContainerPrivate::Sequence around as a copy, so every C++
  QtMetaContainerPrivate::Sequence behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QtMetaContainerPrivate::Sequence that has a ritual
  and that Python can call so far, 9 names in all: 'at', 'setAt', 'append',
  'prepend', 'removeLast', 'removeFirst', 'addValue', 'removeValue',
  'valueMetaType'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QtMetaContainerPrivate::Sequence::Sequence(const QMetaSequence
    &metaSequence, QMetaType metaType, void *iterable)': names 'void', which
    has no cute class yet.
  - Qt's 'QtMetaContainerPrivate::Sequence::Sequence(const QMetaSequence
    &metaSequence, QMetaType metaType, const void *iterable)': names 'void',
    which has no cute class yet.
  - Qt's 'QtMetaContainerPrivate::Sequence::Sequence(QIterable<QMetaSequence>
    &&other)': takes a type Python has no way to hand over yet.
  - Qt's 'Sequence
    &QtMetaContainerPrivate::Sequence::operator=(QIterable<QMetaSequence>
    &&other)': assignment: Python binds a name and has no operator for it.
  - Qt's 'ConstIterator QtMetaContainerPrivate::Sequence::begin() const':
    gives a type Python has no way to take yet.
  - Qt's 'ConstIterator QtMetaContainerPrivate::Sequence::end() const': gives
    a type Python has no way to take yet.
  - Qt's 'ConstIterator QtMetaContainerPrivate::Sequence::constBegin()
    const': gives a type Python has no way to take yet.
  - Qt's 'ConstIterator QtMetaContainerPrivate::Sequence::constEnd() const':
    gives a type Python has no way to take yet.
  - Qt's 'Iterator QtMetaContainerPrivate::Sequence::mutableBegin()': gives a
    type Python has no way to take yet.
  - Qt's 'Iterator QtMetaContainerPrivate::Sequence::mutableEnd()': gives a
    type Python has no way to take yet.
  - Qt's 'QtMetaContainerPrivate::Sequence::~Sequence()': the destructor:
    Python removes its C++ QtMetaContainerPrivate::Sequence by it, and has no
    other use for it.

  What has no ritual
  ------------------

  4 of the 25 functions Qt declares: 3 a template; 1 forbidden.

  What to expect
  --------------

  - The C++ QtMetaContainerPrivate::Sequence is created at the first use, not
    by 'QtMetaContainerPrivate::Sequence(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QtMetaContainerPrivate::Sequence back gives a copy
    the ritual made for Python, in a new cute
    QtMetaContainerPrivate::Sequence.
  - Each name of Qt's QtMetaContainerPrivate::Sequence that has no cute
    function yet, 'begin', 'constBegin', 'constEnd', 'end', 'mutableBegin',
    'mutableEnd', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  #  The enums Qt writes inside QtMetaContainerPrivate::Sequence, each a
  #  class in here as in C++, and the names Qt has for the combinations of
  #  its flags enums.

  class Position(CuteNum):
    """
    The enum 'QtMetaContainerPrivate::Sequence::Position' of Qt, with the 3
    names Qt gives in it.
    """

    Unspecified = Kee[int](0)
    AtBegin = Kee[int](1)
    AtEnd = Kee[int](2)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QtMetaContainerPrivate::Sequence'

  #  Qt's '~QtMetaContainerPrivate::Sequence()'. Naming it makes this a value
  #  class: Python owns every C++ QtMetaContainerPrivate::Sequence behind a
  #  cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN22QtMetaContainerPrivate8SequenceD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def at(self, idx: int) -> QVariant:
    """
    Calls Qt's 'QVariant QtMetaContainerPrivate::Sequence::at(qsizetype idx)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtmetacontainerprivate-sequence.html#at

    Parameters
    ----------

    idx : int
      Passed on as it is.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QtMetaContainerPrivate::Sequence::at(qsizetype idx) const
    address = self.uglySide.call(
        'ritual_ZNK22QtMetaContainerPrivate8Sequence2atEx', idx,
    )
    from . import QVariant
    return QVariant._cuteOwning(address)

  def valueMetaType(self) -> QMetaType:
    """
    Calls Qt's 'QMetaType QtMetaContainerPrivate::Sequence::valueMetaType()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtmetacontainerprivate-sequence.html#valueMetaType

    Returns
    -------

    QMetaType
      A new cute QMetaType around the copy Qt gave back. Python owns it.
    """
    #  QMetaType QtMetaContainerPrivate::Sequence::valueMetaType() const
    address = self.uglySide.call(
        'ritual_ZNK22QtMetaContainerPrivate8Sequence13valueMetaTypeEv',
    )
    from . import QMetaType
    return QMetaType._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int, QVariant)
  def setAt(self, idx: int, value: QVariant) -> None:
    """
    Calls Qt's 'void QtMetaContainerPrivate::Sequence::setAt(qsizetype idx,
    const QVariant &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtmetacontainerprivate-sequence.html#setAt

    Parameters
    ----------

    idx : int
      Passed on as it is.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QtMetaContainerPrivate::Sequence::setAt(qsizetype idx, const
    #      QVariant &value)
    self.uglySide.call(
        'ritual_ZN22QtMetaContainerPrivate8Sequence5setAtExRK8QVariant',
        idx, self._valueOf(value),
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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QtMetaContainerPrivate::Sequence::Sequence()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtmetacontainerprivate-sequence.html#Sequence
    """
    #  QtMetaContainerPrivate::Sequence::Sequence()
    self._noteCreation(Sequence, lambda: Rituals.call(
        'ritual_ZN22QtMetaContainerPrivate8SequenceC1Ev',
    ))

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

  @overload(QVariant)
  def append(self, value: QVariant) -> None:
    """
    Calls Qt's 'void QtMetaContainerPrivate::Sequence::append(const QVariant
    &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtmetacontainerprivate-sequence.html#append

    Parameters
    ----------

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QtMetaContainerPrivate::Sequence::append(const QVariant &value)
    self.uglySide.call(
        'ritual_ZN22QtMetaContainerPrivate8Sequence6appendERK8QVariant',
        self._valueOf(value),
    )

  @overload(QVariant)
  def prepend(self, value: QVariant) -> None:
    """
    Calls Qt's 'void QtMetaContainerPrivate::Sequence::prepend(const QVariant
    &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtmetacontainerprivate-sequence.html#prepend

    Parameters
    ----------

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QtMetaContainerPrivate::Sequence::prepend(const QVariant &value)
    self.uglySide.call(
        'ritual_ZN22QtMetaContainerPrivate8Sequence7prependERK8QVariant',
        self._valueOf(value),
    )

  def removeLast(self) -> None:
    """
    Calls Qt's 'void QtMetaContainerPrivate::Sequence::removeLast()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtmetacontainerprivate-sequence.html#removeLast
    """
    #  void QtMetaContainerPrivate::Sequence::removeLast()
    self.uglySide.call(
        'ritual_ZN22QtMetaContainerPrivate8Sequence10removeLastEv',
    )

  def removeFirst(self) -> None:
    """
    Calls Qt's 'void QtMetaContainerPrivate::Sequence::removeFirst()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtmetacontainerprivate-sequence.html#removeFirst
    """
    #  void QtMetaContainerPrivate::Sequence::removeFirst()
    self.uglySide.call(
        'ritual_ZN22QtMetaContainerPrivate8Sequence11removeFirstEv',
    )

  @overload(QVariant)
  @overload(QVariant, Position)
  def addValue(
      self,
      value: QVariant,
      position: Position = Position.Unspecified,
  ) -> None:
    """
    Calls Qt's 'void QtMetaContainerPrivate::Sequence::addValue(const
    QVariant &value, Position position)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtmetacontainerprivate-sequence.html#addValue

    Parameters
    ----------

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    position : Position
      Passed on as its number. May be left out, as in Qt: it is then
      Position.Unspecified.
    """
    #  void QtMetaContainerPrivate::Sequence::addValue(const QVariant &value,
    #      Position position)
    self.uglySide.call(
        'ritual_ZN22QtMetaContainerPrivate8Sequence8addValueERK8QVariantNS0'
        '_8PositionE',
        self._valueOf(value), position.value,
    )

  @overload()
  @overload(Position)
  def removeValue(self, position: Position = Position.Unspecified) -> None:
    """
    Calls Qt's 'void QtMetaContainerPrivate::Sequence::removeValue(Position
    position)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtmetacontainerprivate-sequence.html#removeValue

    Parameters
    ----------

    position : Position
      Passed on as its number. May be left out, as in Qt: it is then
      Position.Unspecified.
    """
    #  void QtMetaContainerPrivate::Sequence::removeValue(Position position)
    self.uglySide.call(
        'ritual_ZN22QtMetaContainerPrivate8Sequence11removeValueENS0_8Posit'
        'ionE',
        position.value,
    )

  @staticmethod
  def begin(*__, **_) -> Never:
    """
    Qt's 'ConstIterator QtMetaContainerPrivate::Sequence::begin() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QtMetaContainerPrivate.Sequence.begin' has no cute function yet. "
        "Qt's 'ConstIterator QtMetaContainerPrivate::Sequence::begin() "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def constBegin(*__, **_) -> Never:
    """
    Qt's 'ConstIterator QtMetaContainerPrivate::Sequence::constBegin()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QtMetaContainerPrivate.Sequence.constBegin' has no cute function "
        "yet. Qt's 'ConstIterator "
        "QtMetaContainerPrivate::Sequence::constBegin() const': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def constEnd(*__, **_) -> Never:
    """
    Qt's 'ConstIterator QtMetaContainerPrivate::Sequence::constEnd() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QtMetaContainerPrivate.Sequence.constEnd' has no cute function "
        "yet. Qt's 'ConstIterator "
        "QtMetaContainerPrivate::Sequence::constEnd() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def end(*__, **_) -> Never:
    """
    Qt's 'ConstIterator QtMetaContainerPrivate::Sequence::end() const': gives
    a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QtMetaContainerPrivate.Sequence.end' has no cute function yet. "
        "Qt's 'ConstIterator QtMetaContainerPrivate::Sequence::end() "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def mutableBegin(*__, **_) -> Never:
    """
    Qt's 'Iterator QtMetaContainerPrivate::Sequence::mutableBegin()': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QtMetaContainerPrivate.Sequence.mutableBegin' has no cute "
        "function yet. Qt's 'Iterator "
        "QtMetaContainerPrivate::Sequence::mutableBegin()': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def mutableEnd(*__, **_) -> Never:
    """
    Qt's 'Iterator QtMetaContainerPrivate::Sequence::mutableEnd()': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QtMetaContainerPrivate.Sequence.mutableEnd' has no cute function "
        "yet. Qt's 'Iterator "
        "QtMetaContainerPrivate::Sequence::mutableEnd()': gives a type "
        "Python has no way to take yet.")
