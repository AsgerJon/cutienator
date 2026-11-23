"""
QKeyCombination binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qnamespace.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals
from . import Qt, QList


class QKeyCombination(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QKeyCombination: a plain Python object standing in
  front of one C++ QKeyCombination.

  C++ hands a QKeyCombination around as a copy, so every C++ QKeyCombination
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QKeyCombination that has a ritual and that Python
  can call so far, 6 names in all: 'keyboardModifiers', 'key',
  'fromCombined', 'toCombined', '__eq__', '__ne__'. It can be made from
  Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'int QKeyCombination::operator int() const': an operator Python has
    no name for.
  - Qt's 'QKeyCombination::~QKeyCombination()': the destructor: Python
    removes its C++ QKeyCombination by it, and has no other use for it.

  What has no ritual
  ------------------

  1 of the 12 functions Qt declares: 1 forbidden.

  What to expect
  --------------

  - The C++ QKeyCombination is created at the first use, not by
    'QKeyCombination(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QKeyCombination back gives a copy the ritual made for
    Python, in a new cute QKeyCombination.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(int)
  def fromCombined(combined: int) -> QKeyCombination:
    """
    Calls Qt's 'QKeyCombination QKeyCombination::fromCombined(int combined)'.

    Qt's own words: https://doc.qt.io/qt-6/qkeycombination.html#fromCombined

    Parameters
    ----------

    combined : int
      Passed on as it is.

    Returns
    -------

    QKeyCombination
      A new cute QKeyCombination around the copy Qt gave back. Python owns
      it.
    """
    #  QKeyCombination QKeyCombination::fromCombined(int combined)
    address = Rituals.call(
        'ritual_ZN15QKeyCombination12fromCombinedEi', combined,
    )
    return QKeyCombination._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QKeyCombination'

  #  Qt's '~QKeyCombination()'. Naming it makes this a value class: Python
  #  owns every C++ QKeyCombination behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN15QKeyCombinationD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def keyboardModifiers(self) -> Qt.KeyboardModifiers:
    """
    Calls Qt's 'Qt::KeyboardModifiers QKeyCombination::keyboardModifiers()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qkeycombination.html#keyboardModifiers

    Returns
    -------

    Qt.KeyboardModifiers
      The value standing for the combination Qt gave back.
    """
    #  Qt::KeyboardModifiers QKeyCombination::keyboardModifiers() const
    return Qt.KeyboardModifiers(self.uglySide.call(
        'ritual_ZNK15QKeyCombination17keyboardModifiersEv',
    ))

  def key(self) -> Qt.Key:
    """
    Calls Qt's 'Qt::Key QKeyCombination::key() const'.

    Qt's own words: https://doc.qt.io/qt-6/qkeycombination.html#key

    Returns
    -------

    Qt.Key
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.Key(number)' gives.
    """
    #  Qt::Key QKeyCombination::key() const
    return Qt.Key(self.uglySide.call('ritual_ZNK15QKeyCombination3keyEv'))

  def toCombined(self) -> int:
    """
    Calls Qt's 'int QKeyCombination::toCombined() const'.

    Qt's own words: https://doc.qt.io/qt-6/qkeycombination.html#toCombined
    """
    #  int QKeyCombination::toCombined() const
    return self.uglySide.call('ritual_ZNK15QKeyCombination10toCombinedEv')

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
  def __eq__(self, rhs: QKeyCombination) -> bool:
    """
    Calls Qt's 'bool operator==(const QKeyCombination &lhs, const
    QKeyCombination &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qkeycombination.html#operator==

    Parameters
    ----------

    rhs : QKeyCombination
      Passed on as a value: Qt reads the C++ QKeyCombination, which stays
      Python's own.
    """
    #  bool operator==(const QKeyCombination &lhs, const QKeyCombination
    #      &rhs)
    return Rituals.call(
        'ritual_ZeqRK15QKeyCombinationS1_',
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
  def __ne__(self, rhs: QKeyCombination) -> bool:
    """
    Calls Qt's 'bool operator!=(const QKeyCombination &lhs, const
    QKeyCombination &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qkeycombination.html#operator!=

    Parameters
    ----------

    rhs : QKeyCombination
      Passed on as a value: Qt reads the C++ QKeyCombination, which stays
      Python's own.
    """
    #  bool operator!=(const QKeyCombination &lhs, const QKeyCombination
    #      &rhs)
    return Rituals.call(
        'ritual_ZneRK15QKeyCombinationS1_',
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
  @overload(Qt.Key)
  def __init__(self, key: Qt.Key = Qt.Key.Key_unknown) -> None:
    """
    Notes what was given, for Qt's 'QKeyCombination::QKeyCombination(Qt::Key
    key)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qkeycombination.html#QKeyCombination

    Parameters
    ----------

    key : Qt.Key
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.Key.Key_unknown.
    """
    #  QKeyCombination::QKeyCombination(Qt::Key key)
    self._noteCreation(QKeyCombination, lambda: Rituals.call(
        'ritual_ZN15QKeyCombinationC1EN2Qt3KeyE', key.value,
    ))

  @overload(Qt.Modifiers)
  @overload(Qt.Modifiers, Qt.Key)
  def __init__(
      self,
      modifiers: Qt.Modifiers,
      key: Qt.Key = Qt.Key.Key_unknown,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QKeyCombination::QKeyCombination(Qt::Modifiers modifiers, Qt::Key key)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qkeycombination.html#QKeyCombination

    Parameters
    ----------

    modifiers : Qt.Modifiers
      Passed on as its number.

    key : Qt.Key
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.Key.Key_unknown.
    """
    #  QKeyCombination::QKeyCombination(Qt::Modifiers modifiers, Qt::Key key)
    self._noteCreation(QKeyCombination, lambda: Rituals.call(
        'ritual_ZN15QKeyCombinationC1E6QFlagsIN2Qt8ModifierEENS1_3KeyE',
        modifiers.value, key.value,
    ))

  @overload(Qt.KeyboardModifiers)
  @overload(Qt.KeyboardModifiers, Qt.Key)
  def __init__(
      self,
      modifiers: Qt.KeyboardModifiers,
      key: Qt.Key = Qt.Key.Key_unknown,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QKeyCombination::QKeyCombination(Qt::KeyboardModifiers modifiers,
    Qt::Key key)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qkeycombination.html#QKeyCombination

    Parameters
    ----------

    modifiers : Qt.KeyboardModifiers
      Passed on as its number.

    key : Qt.Key
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.Key.Key_unknown.
    """
    #  QKeyCombination::QKeyCombination(Qt::KeyboardModifiers modifiers,
    #      Qt::Key key)
    self._noteCreation(QKeyCombination, lambda: Rituals.call(
        'ritual_ZN15QKeyCombinationC1E6QFlagsIN2Qt16KeyboardModifierEENS1_3'
        'KeyE',
        modifiers.value, key.value,
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


#  Qt's 'QList<QKeyCombination>': the list of QKeyCombination, which
#  'QList[QKeyCombination]' gives. It is made here, so that there is one as
#  soon as there can be a QKeyCombination.
QList.createKind(
    QKeyCombination, 'value',
    make='ritual_list_make_QKeyCombination',
    add='ritual_list_add_QKeyCombination',
    size='ritual_list_size_QKeyCombination',
    at='ritual_list_at_QKeyCombination',
    drop='ritual_list_drop_QKeyCombination',
)
