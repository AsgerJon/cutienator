"""
QSizePolicy binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qsizepolicy.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals
from ..QtCore import Qt
from ._q_size_policy_control_type import ControlType
from ._q_size_policy_policy import Policy
from ._q_size_policy_policy_flag import PolicyFlag


class QSizePolicy(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSizePolicy: a plain Python object standing in front
  of one C++ QSizePolicy.

  C++ hands a QSizePolicy around as a copy, so every C++ QSizePolicy behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QSizePolicy that has a ritual and that Python can
  call so far, 19 names in all: 'horizontalPolicy', 'verticalPolicy',
  'controlType', 'setHorizontalPolicy', 'setVerticalPolicy',
  'setControlType', 'expandingDirections', 'setHeightForWidth',
  'hasHeightForWidth', 'setWidthForHeight', 'hasWidthForHeight',
  'horizontalStretch', 'verticalStretch', 'setHorizontalStretch',
  'setVerticalStretch', 'retainSizeWhenHidden', 'setRetainSizeWhenHidden',
  'transpose', 'transposed'. It can be made from Python, in 2 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'bool QSizePolicy::operator==(const QSizePolicy &s) const': an
    operator, which is not reflected yet.
  - Qt's 'bool QSizePolicy::operator!=(const QSizePolicy &s) const': an
    operator, which is not reflected yet.
  - Qt's 'QVariant QSizePolicy::operator QVariant() const': an operator,
    which is not reflected yet.
  - Qt's 'QSizePolicy::~QSizePolicy()': the destructor: Python removes its
    C++ QSizePolicy by it, and has no other use for it.

  What has no ritual
  ------------------

  6 of the 31 functions Qt declares: 4 private; 1 declared and nowhere to be
  found; 1 a template.

  What to expect
  --------------

  - The C++ QSizePolicy is created at the first use, not by
    'QSizePolicy(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSizePolicy back gives a copy the ritual made for
    Python, in a new cute QSizePolicy.
  """

  #  The enums Qt writes inside QSizePolicy, and the names Qt has for the
  #  combinations of its flags enums.
  ControlType = ControlType
  ControlTypes = ControlType
  Policy = Policy
  PolicyFlag = PolicyFlag

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSizePolicy'

  #  Qt's '~QSizePolicy()'. Naming it makes this a value class: Python owns
  #  every C++ QSizePolicy behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN11QSizePolicyD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def horizontalPolicy(self) -> Policy:
    """
    Calls Qt's 'Policy QSizePolicy::horizontalPolicy() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsizepolicy.html#horizontalPolicy

    Returns
    -------

    Policy
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Policy(number)' gives.
    """
    #  Policy QSizePolicy::horizontalPolicy() const
    return Policy(self.uglySide.call(
        'ritual_ZNK11QSizePolicy16horizontalPolicyEv',
    ))

  def verticalPolicy(self) -> Policy:
    """
    Calls Qt's 'Policy QSizePolicy::verticalPolicy() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsizepolicy.html#verticalPolicy

    Returns
    -------

    Policy
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Policy(number)' gives.
    """
    #  Policy QSizePolicy::verticalPolicy() const
    return Policy(self.uglySide.call(
        'ritual_ZNK11QSizePolicy14verticalPolicyEv',
    ))

  def controlType(self) -> ControlType:
    """
    Calls Qt's 'ControlType QSizePolicy::controlType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsizepolicy.html#controlType

    Returns
    -------

    ControlType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'ControlType(number)'
      gives.
    """
    #  ControlType QSizePolicy::controlType() const
    return ControlType(self.uglySide.call(
        'ritual_ZNK11QSizePolicy11controlTypeEv',
    ))

  def expandingDirections(self) -> Qt.Orientations:
    """
    Calls Qt's 'Qt::Orientations QSizePolicy::expandingDirections() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsizepolicy.html#expandingDirections

    Returns
    -------

    Qt.Orientations
      The value standing for the combination Qt gave back.
    """
    #  Qt::Orientations QSizePolicy::expandingDirections() const
    return Qt.Orientations(self.uglySide.call(
        'ritual_ZNK11QSizePolicy19expandingDirectionsEv',
    ))

  def hasHeightForWidth(self) -> bool:
    """
    Calls Qt's 'bool QSizePolicy::hasHeightForWidth() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsizepolicy.html#hasHeightForWidth
    """
    #  bool QSizePolicy::hasHeightForWidth() const
    return self.uglySide.call('ritual_ZNK11QSizePolicy17hasHeightForWidthEv')

  def hasWidthForHeight(self) -> bool:
    """
    Calls Qt's 'bool QSizePolicy::hasWidthForHeight() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsizepolicy.html#hasWidthForHeight
    """
    #  bool QSizePolicy::hasWidthForHeight() const
    return self.uglySide.call('ritual_ZNK11QSizePolicy17hasWidthForHeightEv')

  def horizontalStretch(self) -> int:
    """
    Calls Qt's 'int QSizePolicy::horizontalStretch() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsizepolicy.html#horizontalStretch
    """
    #  int QSizePolicy::horizontalStretch() const
    return self.uglySide.call('ritual_ZNK11QSizePolicy17horizontalStretchEv')

  def verticalStretch(self) -> int:
    """
    Calls Qt's 'int QSizePolicy::verticalStretch() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsizepolicy.html#verticalStretch
    """
    #  int QSizePolicy::verticalStretch() const
    return self.uglySide.call('ritual_ZNK11QSizePolicy15verticalStretchEv')

  def retainSizeWhenHidden(self) -> bool:
    """
    Calls Qt's 'bool QSizePolicy::retainSizeWhenHidden() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsizepolicy.html#retainSizeWhenHidden
    """
    #  bool QSizePolicy::retainSizeWhenHidden() const
    return self.uglySide.call(
        'ritual_ZNK11QSizePolicy20retainSizeWhenHiddenEv',
    )

  def transposed(self) -> QSizePolicy:
    """
    Calls Qt's 'QSizePolicy QSizePolicy::transposed() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsizepolicy.html#transposed

    Returns
    -------

    QSizePolicy
      A new cute QSizePolicy around the copy Qt gave back. Python owns it.
    """
    #  QSizePolicy QSizePolicy::transposed() const
    address = self.uglySide.call('ritual_ZNK11QSizePolicy10transposedEv')
    return QSizePolicy._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Policy)
  def setHorizontalPolicy(self, d: Policy) -> None:
    """
    Calls Qt's 'void QSizePolicy::setHorizontalPolicy(Policy d)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsizepolicy.html#setHorizontalPolicy

    Parameters
    ----------

    d : Policy
      Passed on as its number.
    """
    #  void QSizePolicy::setHorizontalPolicy(Policy d)
    self.uglySide.call(
        'ritual_ZN11QSizePolicy19setHorizontalPolicyENS_6PolicyE', d.value,
    )

  @overload(Policy)
  def setVerticalPolicy(self, d: Policy) -> None:
    """
    Calls Qt's 'void QSizePolicy::setVerticalPolicy(Policy d)'.

    Qt's own words: https://doc.qt.io/qt-6/qsizepolicy.html#setVerticalPolicy

    Parameters
    ----------

    d : Policy
      Passed on as its number.
    """
    #  void QSizePolicy::setVerticalPolicy(Policy d)
    self.uglySide.call(
        'ritual_ZN11QSizePolicy17setVerticalPolicyENS_6PolicyE', d.value,
    )

  @overload(ControlType)
  def setControlType(self, type: ControlType) -> None:
    """
    Calls Qt's 'void QSizePolicy::setControlType(ControlType type)'.

    Qt's own words: https://doc.qt.io/qt-6/qsizepolicy.html#setControlType

    Parameters
    ----------

    type : ControlType
      Passed on as its number.
    """
    #  void QSizePolicy::setControlType(ControlType type)
    self.uglySide.call(
        'ritual_ZN11QSizePolicy14setControlTypeENS_11ControlTypeE',
        type.value,
    )

  @overload(bool)
  def setHeightForWidth(self, b: bool) -> None:
    """
    Calls Qt's 'void QSizePolicy::setHeightForWidth(bool b)'.

    Qt's own words: https://doc.qt.io/qt-6/qsizepolicy.html#setHeightForWidth

    Parameters
    ----------

    b : bool
      Passed on as it is.
    """
    #  void QSizePolicy::setHeightForWidth(bool b)
    self.uglySide.call('ritual_ZN11QSizePolicy17setHeightForWidthEb', b)

  @overload(bool)
  def setWidthForHeight(self, b: bool) -> None:
    """
    Calls Qt's 'void QSizePolicy::setWidthForHeight(bool b)'.

    Qt's own words: https://doc.qt.io/qt-6/qsizepolicy.html#setWidthForHeight

    Parameters
    ----------

    b : bool
      Passed on as it is.
    """
    #  void QSizePolicy::setWidthForHeight(bool b)
    self.uglySide.call('ritual_ZN11QSizePolicy17setWidthForHeightEb', b)

  @overload(int)
  def setHorizontalStretch(self, stretchFactor: int) -> None:
    """
    Calls Qt's 'void QSizePolicy::setHorizontalStretch(int stretchFactor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsizepolicy.html#setHorizontalStretch

    Parameters
    ----------

    stretchFactor : int
      Passed on as it is.
    """
    #  void QSizePolicy::setHorizontalStretch(int stretchFactor)
    self.uglySide.call(
        'ritual_ZN11QSizePolicy20setHorizontalStretchEi', stretchFactor,
    )

  @overload(int)
  def setVerticalStretch(self, stretchFactor: int) -> None:
    """
    Calls Qt's 'void QSizePolicy::setVerticalStretch(int stretchFactor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsizepolicy.html#setVerticalStretch

    Parameters
    ----------

    stretchFactor : int
      Passed on as it is.
    """
    #  void QSizePolicy::setVerticalStretch(int stretchFactor)
    self.uglySide.call(
        'ritual_ZN11QSizePolicy18setVerticalStretchEi', stretchFactor,
    )

  @overload(bool)
  def setRetainSizeWhenHidden(self, retainSize: bool) -> None:
    """
    Calls Qt's 'void QSizePolicy::setRetainSizeWhenHidden(bool retainSize)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsizepolicy.html#setRetainSizeWhenHidden

    Parameters
    ----------

    retainSize : bool
      Passed on as it is.
    """
    #  void QSizePolicy::setRetainSizeWhenHidden(bool retainSize)
    self.uglySide.call(
        'ritual_ZN11QSizePolicy23setRetainSizeWhenHiddenEb', retainSize,
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
    Notes what was given, for Qt's 'QSizePolicy::QSizePolicy()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qsizepolicy.html#QSizePolicy
    """
    #  QSizePolicy::QSizePolicy()
    self._noteCreation(QSizePolicy, lambda: Rituals.call(
        'ritual_ZN11QSizePolicyC1Ev',
    ))

  @overload(Policy, Policy)
  @overload(Policy, Policy, ControlType)
  def __init__(
      self,
      horizontal: Policy,
      vertical: Policy,
      type: ControlType = ControlType.DefaultType,
  ) -> None:
    """
    Notes what was given, for Qt's 'QSizePolicy::QSizePolicy(Policy
    horizontal, Policy vertical, ControlType type)', which is called at the
    first use.

    Qt's own words: https://doc.qt.io/qt-6/qsizepolicy.html#QSizePolicy

    Parameters
    ----------

    horizontal : Policy
      Passed on as its number.

    vertical : Policy
      Passed on as its number.

    type : ControlType
      Passed on as its number. May be left out, as in Qt: it is then
      ControlType.DefaultType.
    """
    #  QSizePolicy::QSizePolicy(Policy horizontal, Policy vertical,
    #      ControlType type)
    self._noteCreation(QSizePolicy, lambda: Rituals.call(
        'ritual_ZN11QSizePolicyC1ENS_6PolicyES0_NS_11ControlTypeE',
        horizontal.value, vertical.value, type.value,
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

  def transpose(self) -> None:
    """
    Calls Qt's 'void QSizePolicy::transpose()'.

    Qt's own words: https://doc.qt.io/qt-6/qsizepolicy.html#transpose
    """
    #  void QSizePolicy::transpose()
    self.uglySide.call('ritual_ZN11QSizePolicy9transposeEv')
