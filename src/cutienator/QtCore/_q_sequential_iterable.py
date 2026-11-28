"""
QSequentialIterable binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qsequentialiterable.h, Qt 6.12.0. Changes made here are lost.
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


class QSequentialIterable(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSequentialIterable: a plain Python object standing
  in front of one C++ QSequentialIterable.

  What exists
  -----------

  Every function of Qt's QSequentialIterable that has a ritual and that
  Python can call so far, 6 names in all: 'at', 'set', 'addValue',
  'removeValue', 'valueMetaType', 'canRandomAccessIterate'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSequentialIterable::QSequentialIterable(const QMetaSequence
    &metaSequence, const QMetaType &metaType, void *iterable)': names 'void',
    which has no cute class yet.
  - Qt's 'QSequentialIterable::QSequentialIterable(const QMetaSequence
    &metaSequence, const QMetaType &metaType, const void *iterable)': names
    'void', which has no cute class yet.
  - Qt's 'QSequentialIterable::QSequentialIterable(QIterable<QMetaSequence>
    &&other)': takes a type Python has no way to hand over yet.
  - Qt's 'QSequentialIterable
    &QSequentialIterable::operator=(QIterable<QMetaSequence> &&other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'const_iterator QSequentialIterable::begin() const': gives a type
    Python has no way to take yet.
  - Qt's 'const_iterator QSequentialIterable::end() const': gives a type
    Python has no way to take yet.
  - Qt's 'const_iterator QSequentialIterable::constBegin() const': gives a
    type Python has no way to take yet.
  - Qt's 'const_iterator QSequentialIterable::constEnd() const': gives a type
    Python has no way to take yet.
  - Qt's 'iterator QSequentialIterable::mutableBegin()': gives a type Python
    has no way to take yet.
  - Qt's 'iterator QSequentialIterable::mutableEnd()': gives a type Python
    has no way to take yet.

  What has no ritual
  ------------------

  3 of the 20 functions Qt declares: 3 a template.

  What to expect
  --------------

  - The C++ QSequentialIterable is created at the first use, not by
    'QSequentialIterable(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSequentialIterable.
  - Each name of Qt's QSequentialIterable that has no cute function yet,
    'begin', 'constBegin', 'constEnd', 'end', 'mutableBegin', 'mutableEnd',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  #  The enums Qt writes inside QSequentialIterable, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class Position(CuteNum):
    """
    The enum 'QSequentialIterable::Position' of Qt, with the 3 names Qt gives
    in it.
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
  __qt_class__ = 'QSequentialIterable'

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
    Calls Qt's 'QVariant QSequentialIterable::at(qsizetype idx) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsequentialiterable.html#at

    Parameters
    ----------

    idx : int
      Passed on as it is.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QSequentialIterable::at(qsizetype idx) const
    address = self.uglySide.call('ritual_ZNK19QSequentialIterable2atEx', idx)
    from . import QVariant
    return QVariant._cuteOwning(address)

  def valueMetaType(self) -> QMetaType:
    """
    Calls Qt's 'QMetaType QSequentialIterable::valueMetaType() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsequentialiterable.html#valueMetaType

    Returns
    -------

    QMetaType
      A new cute QMetaType around the copy Qt gave back. Python owns it.
    """
    #  QMetaType QSequentialIterable::valueMetaType() const
    address = self.uglySide.call(
        'ritual_ZNK19QSequentialIterable13valueMetaTypeEv',
    )
    from . import QMetaType
    return QMetaType._cuteOwning(address)

  def canRandomAccessIterate(self) -> bool:
    """
    Calls Qt's 'bool QSequentialIterable::canRandomAccessIterate() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsequentialiterable.html#canRandomAccessIterate
    """
    #  bool QSequentialIterable::canRandomAccessIterate() const
    return self.uglySide.call(
        'ritual_ZNK19QSequentialIterable22canRandomAccessIterateEv',
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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QSequentialIterable::QSequentialIterable()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsequentialiterable.html#QSequentialIterable
    """
    #  QSequentialIterable::QSequentialIterable()
    self._noteCreation(QSequentialIterable, lambda: Rituals.call(
        'ritual_ZN19QSequentialIterableC1Ev',
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

  @overload(int, QVariant)
  def set(self, idx: int, value: QVariant) -> None:
    """
    Calls Qt's 'void QSequentialIterable::set(qsizetype idx, const QVariant
    &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qsequentialiterable.html#set

    Parameters
    ----------

    idx : int
      Passed on as it is.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QSequentialIterable::set(qsizetype idx, const QVariant &value)
    self.uglySide.call(
        'ritual_ZN19QSequentialIterable3setExRK8QVariant',
        idx, self._valueOf(value),
    )

  @overload(QVariant)
  @overload(QVariant, Position)
  def addValue(
      self,
      value: QVariant,
      position: Position = Position.Unspecified,
  ) -> None:
    """
    Calls Qt's 'void QSequentialIterable::addValue(const QVariant &value,
    Position position)'.

    Qt's own words: https://doc.qt.io/qt-6/qsequentialiterable.html#addValue

    Parameters
    ----------

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    position : Position
      Passed on as its number. May be left out, as in Qt: it is then
      Position.Unspecified.
    """
    #  void QSequentialIterable::addValue(const QVariant &value, Position
    #      position)
    self.uglySide.call(
        'ritual_ZN19QSequentialIterable8addValueERK8QVariantNS_8PositionE',
        self._valueOf(value), position.value,
    )

  @overload()
  @overload(Position)
  def removeValue(self, position: Position = Position.Unspecified) -> None:
    """
    Calls Qt's 'void QSequentialIterable::removeValue(Position position)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsequentialiterable.html#removeValue

    Parameters
    ----------

    position : Position
      Passed on as its number. May be left out, as in Qt: it is then
      Position.Unspecified.
    """
    #  void QSequentialIterable::removeValue(Position position)
    self.uglySide.call(
        'ritual_ZN19QSequentialIterable11removeValueENS_8PositionE',
        position.value,
    )

  @staticmethod
  def begin(*__, **_) -> Never:
    """
    Qt's 'const_iterator QSequentialIterable::begin() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QSequentialIterable.begin' has no cute function yet. Qt's "
        "'const_iterator QSequentialIterable::begin() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def constBegin(*__, **_) -> Never:
    """
    Qt's 'const_iterator QSequentialIterable::constBegin() const': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QSequentialIterable.constBegin' has no cute function yet. Qt's "
        "'const_iterator QSequentialIterable::constBegin() const': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def constEnd(*__, **_) -> Never:
    """
    Qt's 'const_iterator QSequentialIterable::constEnd() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QSequentialIterable.constEnd' has no cute function yet. Qt's "
        "'const_iterator QSequentialIterable::constEnd() const': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def end(*__, **_) -> Never:
    """
    Qt's 'const_iterator QSequentialIterable::end() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QSequentialIterable.end' has no cute function yet. Qt's "
        "'const_iterator QSequentialIterable::end() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def mutableBegin(*__, **_) -> Never:
    """
    Qt's 'iterator QSequentialIterable::mutableBegin()': gives a type Python
    has no way to take yet.
    """
    raise NotImplementedError(
        "'QSequentialIterable.mutableBegin' has no cute function yet. Qt's "
        "'iterator QSequentialIterable::mutableBegin()': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def mutableEnd(*__, **_) -> Never:
    """
    Qt's 'iterator QSequentialIterable::mutableEnd()': gives a type Python
    has no way to take yet.
    """
    raise NotImplementedError(
        "'QSequentialIterable.mutableEnd' has no cute function yet. Qt's "
        "'iterator QSequentialIterable::mutableEnd()': gives a type Python "
        "has no way to take yet.")
