"""
QMetaSequence binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qmetacontainer.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..occult import Rituals
from . import QMetaContainer

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from . import QMetaType


class QMetaSequence(QMetaContainer):
  """
  The cute side of Qt's QMetaSequence: a plain Python object standing in
  front of one C++ QMetaSequence.

  It is built on the cute 'QMetaContainer', as Qt's QMetaSequence is built on
  Qt's QMetaContainer, and has everything that class has.

  C++ hands a QMetaSequence around as a copy, so every C++ QMetaSequence
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QMetaSequence that has a ritual and that Python can
  call so far, 18 names in all: 'valueMetaType', 'isSortable',
  'canAddValueAtBegin', 'canAddValueAtEnd', 'canRemoveValueAtBegin',
  'canRemoveValueAtEnd', 'canGetValueAtIndex', 'canSetValueAtIndex',
  'canAddValue', 'canRemoveValue', 'canGetValueAtIterator',
  'canSetValueAtIterator', 'canInsertValueAtIterator',
  'canEraseValueAtIterator', 'canEraseRangeAtIterator',
  'canGetValueAtConstIterator', '__eq__', '__ne__'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QMetaSequence::~QMetaSequence()': the destructor: Python removes
    its C++ QMetaSequence by it, and has no other use for it.

  What has no ritual
  ------------------

  18 of the 38 functions Qt declares: 17 takes or gives a type that cannot be
  passed yet; 1 a template.

  What to expect
  --------------

  - The C++ QMetaSequence is created at the first use, not by
    'QMetaSequence(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QMetaSequence back gives a copy the ritual made for
    Python, in a new cute QMetaSequence.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QMetaSequence'

  #  Qt's '~QMetaSequence()'. Naming it makes this a value class: Python owns
  #  every C++ QMetaSequence behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN13QMetaSequenceD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def valueMetaType(self) -> QMetaType:
    """
    Calls Qt's 'QMetaType QMetaSequence::valueMetaType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetasequence.html#valueMetaType

    Returns
    -------

    QMetaType
      A new cute QMetaType around the copy Qt gave back. Python owns it.
    """
    #  QMetaType QMetaSequence::valueMetaType() const
    address = self.uglySide.call(
        'ritual_ZNK13QMetaSequence13valueMetaTypeEv',
    )
    from . import QMetaType
    return QMetaType._cuteOwning(address)

  def isSortable(self) -> bool:
    """
    Calls Qt's 'bool QMetaSequence::isSortable() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetasequence.html#isSortable
    """
    #  bool QMetaSequence::isSortable() const
    return self.uglySide.call('ritual_ZNK13QMetaSequence10isSortableEv')

  def canAddValueAtBegin(self) -> bool:
    """
    Calls Qt's 'bool QMetaSequence::canAddValueAtBegin() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetasequence.html#canAddValueAtBegin
    """
    #  bool QMetaSequence::canAddValueAtBegin() const
    return self.uglySide.call(
        'ritual_ZNK13QMetaSequence18canAddValueAtBeginEv',
    )

  def canAddValueAtEnd(self) -> bool:
    """
    Calls Qt's 'bool QMetaSequence::canAddValueAtEnd() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetasequence.html#canAddValueAtEnd
    """
    #  bool QMetaSequence::canAddValueAtEnd() const
    return self.uglySide.call(
        'ritual_ZNK13QMetaSequence16canAddValueAtEndEv',
    )

  def canRemoveValueAtBegin(self) -> bool:
    """
    Calls Qt's 'bool QMetaSequence::canRemoveValueAtBegin() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetasequence.html#canRemoveValueAtBegin
    """
    #  bool QMetaSequence::canRemoveValueAtBegin() const
    return self.uglySide.call(
        'ritual_ZNK13QMetaSequence21canRemoveValueAtBeginEv',
    )

  def canRemoveValueAtEnd(self) -> bool:
    """
    Calls Qt's 'bool QMetaSequence::canRemoveValueAtEnd() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetasequence.html#canRemoveValueAtEnd
    """
    #  bool QMetaSequence::canRemoveValueAtEnd() const
    return self.uglySide.call(
        'ritual_ZNK13QMetaSequence19canRemoveValueAtEndEv',
    )

  def canGetValueAtIndex(self) -> bool:
    """
    Calls Qt's 'bool QMetaSequence::canGetValueAtIndex() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetasequence.html#canGetValueAtIndex
    """
    #  bool QMetaSequence::canGetValueAtIndex() const
    return self.uglySide.call(
        'ritual_ZNK13QMetaSequence18canGetValueAtIndexEv',
    )

  def canSetValueAtIndex(self) -> bool:
    """
    Calls Qt's 'bool QMetaSequence::canSetValueAtIndex() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetasequence.html#canSetValueAtIndex
    """
    #  bool QMetaSequence::canSetValueAtIndex() const
    return self.uglySide.call(
        'ritual_ZNK13QMetaSequence18canSetValueAtIndexEv',
    )

  def canAddValue(self) -> bool:
    """
    Calls Qt's 'bool QMetaSequence::canAddValue() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetasequence.html#canAddValue
    """
    #  bool QMetaSequence::canAddValue() const
    return self.uglySide.call('ritual_ZNK13QMetaSequence11canAddValueEv')

  def canRemoveValue(self) -> bool:
    """
    Calls Qt's 'bool QMetaSequence::canRemoveValue() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetasequence.html#canRemoveValue
    """
    #  bool QMetaSequence::canRemoveValue() const
    return self.uglySide.call('ritual_ZNK13QMetaSequence14canRemoveValueEv')

  def canGetValueAtIterator(self) -> bool:
    """
    Calls Qt's 'bool QMetaSequence::canGetValueAtIterator() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetasequence.html#canGetValueAtIterator
    """
    #  bool QMetaSequence::canGetValueAtIterator() const
    return self.uglySide.call(
        'ritual_ZNK13QMetaSequence21canGetValueAtIteratorEv',
    )

  def canSetValueAtIterator(self) -> bool:
    """
    Calls Qt's 'bool QMetaSequence::canSetValueAtIterator() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetasequence.html#canSetValueAtIterator
    """
    #  bool QMetaSequence::canSetValueAtIterator() const
    return self.uglySide.call(
        'ritual_ZNK13QMetaSequence21canSetValueAtIteratorEv',
    )

  def canInsertValueAtIterator(self) -> bool:
    """
    Calls Qt's 'bool QMetaSequence::canInsertValueAtIterator() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetasequence.html#canInsertValueAtIterator
    """
    #  bool QMetaSequence::canInsertValueAtIterator() const
    return self.uglySide.call(
        'ritual_ZNK13QMetaSequence24canInsertValueAtIteratorEv',
    )

  def canEraseValueAtIterator(self) -> bool:
    """
    Calls Qt's 'bool QMetaSequence::canEraseValueAtIterator() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetasequence.html#canEraseValueAtIterator
    """
    #  bool QMetaSequence::canEraseValueAtIterator() const
    return self.uglySide.call(
        'ritual_ZNK13QMetaSequence23canEraseValueAtIteratorEv',
    )

  def canEraseRangeAtIterator(self) -> bool:
    """
    Calls Qt's 'bool QMetaSequence::canEraseRangeAtIterator() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetasequence.html#canEraseRangeAtIterator
    """
    #  bool QMetaSequence::canEraseRangeAtIterator() const
    return self.uglySide.call(
        'ritual_ZNK13QMetaSequence23canEraseRangeAtIteratorEv',
    )

  def canGetValueAtConstIterator(self) -> bool:
    """
    Calls Qt's 'bool QMetaSequence::canGetValueAtConstIterator() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetasequence.html#canGetValueAtConstIterator
    """
    #  bool QMetaSequence::canGetValueAtConstIterator() const
    return self.uglySide.call(
        'ritual_ZNK13QMetaSequence26canGetValueAtConstIteratorEv',
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

  @overload(THIS)
  def __eq__(self, rhs: QMetaSequence) -> bool:
    """
    Calls Qt's 'bool operator==(const QMetaSequence &lhs, const QMetaSequence
    &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qmetasequence.html#operator==

    Parameters
    ----------

    rhs : QMetaSequence
      Passed on as a value: Qt reads the C++ QMetaSequence, which stays
      Python's own.
    """
    #  bool operator==(const QMetaSequence &lhs, const QMetaSequence &rhs)
    return Rituals.call(
        'ritual_ZeqRK13QMetaSequenceS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __ne__(self, rhs: QMetaSequence) -> bool:
    """
    Calls Qt's 'bool operator!=(const QMetaSequence &lhs, const QMetaSequence
    &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qmetasequence.html#operator!=

    Parameters
    ----------

    rhs : QMetaSequence
      Passed on as a value: Qt reads the C++ QMetaSequence, which stays
      Python's own.
    """
    #  bool operator!=(const QMetaSequence &lhs, const QMetaSequence &rhs)
    return Rituals.call(
        'ritual_ZneRK13QMetaSequenceS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __ne__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QMetaSequence::QMetaSequence()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qmetasequence.html#QMetaSequence
    """
    #  QMetaSequence::QMetaSequence()
    self._noteCreation(QMetaSequence, lambda: Rituals.call(
        'ritual_ZN13QMetaSequenceC1Ev',
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
