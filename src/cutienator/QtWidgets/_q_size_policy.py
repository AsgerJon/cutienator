"""
QSizePolicy binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qsizepolicy.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, MetaCute
from ..occult import Rituals
from ..QtCore import Qt


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
  call so far, 22 names in all: 'horizontalPolicy', 'verticalPolicy',
  'controlType', 'setHorizontalPolicy', 'setVerticalPolicy',
  'setControlType', 'expandingDirections', 'setHeightForWidth',
  'hasHeightForWidth', 'setWidthForHeight', 'hasWidthForHeight', '__eq__',
  '__ne__', 'horizontalStretch', 'verticalStretch', 'setHorizontalStretch',
  'setVerticalStretch', 'retainSizeWhenHidden', 'setRetainSizeWhenHidden',
  'transpose', 'transposed', 'toControlTypeFieldValue'. It can be made from
  Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QVariant QSizePolicy::operator QVariant() const': an operator
    Python has no name for.
  - Qt's 'QDataStream &operator<<(QDataStream &a0, const QSizePolicy &a1)':
    takes a type Python has no way to hand over yet.
  - Qt's 'QDataStream &operator>>(QDataStream &a0, QSizePolicy &a1)': an
    operator between other classes, written inside this one.
  - Qt's 'QSizePolicy::QSizePolicy(Bits b)': takes a type Python has no way
    to hand over yet.
  - Qt's 'QSizePolicy::~QSizePolicy()': the destructor: Python removes its
    C++ QSizePolicy by it, and has no other use for it.

  What has no ritual
  ------------------

  3 of the 33 functions Qt declares: 3 not a gap.

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

  #  The enums Qt writes inside QSizePolicy, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class ControlType(CuteFlags):
    """
    The flags enum 'QSizePolicy::ControlType' of Qt, with the 15 names Qt
    gives in it. Qt names the type of its combinations
    'QSizePolicy::ControlTypes'.
    """

    DefaultType = 0x1
    ButtonBox = 0x2
    CheckBox = 0x4
    ComboBox = 0x8
    Frame = 0x10
    GroupBox = 0x20
    Label = 0x40
    Line = 0x80
    LineEdit = 0x100
    PushButton = 0x200
    RadioButton = 0x400
    Slider = 0x800
    SpinBox = 0x1000
    TabWidget = 0x2000
    ToolButton = 0x4000

  ControlTypes = ControlType

  class Policy(CuteNum):
    """
    The enum 'QSizePolicy::Policy' of Qt, with the 7 names Qt gives in it.
    """

    Fixed = Kee[int](0)
    Minimum = Kee[int](1)
    Maximum = Kee[int](4)
    Preferred = Kee[int](5)
    MinimumExpanding = Kee[int](3)
    Expanding = Kee[int](7)
    Ignored = Kee[int](13)

  class PolicyFlag(CuteNum):
    """
    The enum 'QSizePolicy::PolicyFlag' of Qt, with the 4 names Qt gives in
    it.
    """

    GrowFlag = Kee[int](1)
    ExpandFlag = Kee[int](2)
    ShrinkFlag = Kee[int](4)
    IgnoreFlag = Kee[int](8)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(ControlType)
  def toControlTypeFieldValue(type: ControlType) -> int:
    """
    Calls Qt's 'quint32 QSizePolicy::toControlTypeFieldValue(ControlType
    type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsizepolicy.html#toControlTypeFieldValue

    Parameters
    ----------

    type : ControlType
      Passed on as its number.
    """
    #  quint32 QSizePolicy::toControlTypeFieldValue(ControlType type)
    return Rituals.call(
        'ritual_ZN11QSizePolicy23toControlTypeFieldValueENS_11ControlTypeE',
        type.value,
    )

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
    return QSizePolicy.Policy(self.uglySide.call(
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
    return QSizePolicy.Policy(self.uglySide.call(
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
    return QSizePolicy.ControlType(self.uglySide.call(
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

  @overload(THIS)
  def __eq__(self, s: QSizePolicy) -> bool:
    """
    Calls Qt's 'bool QSizePolicy::operator==(const QSizePolicy &s) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsizepolicy.html#operator==

    Parameters
    ----------

    s : QSizePolicy
      Passed on as a value: Qt reads the C++ QSizePolicy, which stays
      Python's own.
    """
    #  bool QSizePolicy::operator==(const QSizePolicy &s) const
    return self.uglySide.call(
        'ritual_ZNK11QSizePolicyeqERKS_', self._valueOf(s),
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
  def __ne__(self, s: QSizePolicy) -> bool:
    """
    Calls Qt's 'bool QSizePolicy::operator!=(const QSizePolicy &s) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsizepolicy.html#operator!=

    Parameters
    ----------

    s : QSizePolicy
      Passed on as a value: Qt reads the C++ QSizePolicy, which stays
      Python's own.
    """
    #  bool QSizePolicy::operator!=(const QSizePolicy &s) const
    return self.uglySide.call(
        'ritual_ZNK11QSizePolicyneERKS_', self._valueOf(s),
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

  @overload(int)
  def __init__(self, i: int) -> None:
    """
    Notes what was given, for Qt's 'QSizePolicy::QSizePolicy(int i)', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qsizepolicy.html#QSizePolicy

    Parameters
    ----------

    i : int
      Passed on as it is.
    """
    #  QSizePolicy::QSizePolicy(int i)
    self._noteCreation(QSizePolicy, lambda: Rituals.call(
        'ritual_ZN11QSizePolicyC1Ei', i,
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
