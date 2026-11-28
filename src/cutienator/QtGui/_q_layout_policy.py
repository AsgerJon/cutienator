"""
QLayoutPolicy binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qlayoutpolicy_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QLayoutPolicy to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, CuteFlags, MetaCute
from ..occult import Rituals
from ..QtCore import Qt


class QLayoutPolicy(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QLayoutPolicy: a plain Python object standing in
  front of one C++ QLayoutPolicy.

  C++ hands a QLayoutPolicy around as a copy, so every C++ QLayoutPolicy
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QLayoutPolicy that has a ritual and that Python can
  call so far, 18 names in all: 'horizontalPolicy', 'verticalPolicy',
  'controlType', 'setHorizontalPolicy', 'setVerticalPolicy',
  'setControlType', 'expandingDirections', 'setHeightForWidth',
  'hasHeightForWidth', 'setWidthForHeight', 'hasWidthForHeight', '__eq__',
  '__ne__', 'horizontalStretch', 'verticalStretch', 'setHorizontalStretch',
  'setVerticalStretch', 'transpose'. It can be made from Python, in 3 ways;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QLayoutPolicy::~QLayoutPolicy()': the destructor: Python removes
    its C++ QLayoutPolicy by it, and has no other use for it.

  What has no ritual
  ------------------

  5 of the 27 functions Qt declares: 3 not a gap; 2 cannot be called and
  cannot be called through the meta-object and cannot be copied.

  What to expect
  --------------

  - The C++ QLayoutPolicy is created at the first use, not by
    'QLayoutPolicy(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QLayoutPolicy back gives a copy the ritual made for
    Python, in a new cute QLayoutPolicy.
  """

  #  The enums Qt writes inside QLayoutPolicy, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class ControlType(CuteFlags):
    """
    The flags enum 'QLayoutPolicy::ControlType' of Qt, with the 15 names Qt
    gives in it. Qt names the type of its combinations
    'QLayoutPolicy::ControlTypes'.
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

  class PolicyFlag(CuteFlags):
    """
    The flags enum 'QLayoutPolicy::PolicyFlag' of Qt, with the 4 names Qt
    gives in it. Qt names the type of its combinations
    'QLayoutPolicy::Policy'.
    """

    GrowFlag = 0x1
    ExpandFlag = 0x2
    ShrinkFlag = 0x4
    IgnoreFlag = 0x8

  Policy = PolicyFlag

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QLayoutPolicy'

  #  Qt's '~QLayoutPolicy()'. Naming it makes this a value class: Python owns
  #  every C++ QLayoutPolicy behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN13QLayoutPolicyD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def horizontalPolicy(self) -> Policy:
    """
    Calls Qt's 'Policy QLayoutPolicy::horizontalPolicy() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlayoutpolicy.html#horizontalPolicy

    Returns
    -------

    Policy
      The value standing for the combination Qt gave back.
    """
    #  Policy QLayoutPolicy::horizontalPolicy() const
    return QLayoutPolicy.Policy(self.uglySide.call(
        'ritual_ZNK13QLayoutPolicy16horizontalPolicyEv',
    ))

  def verticalPolicy(self) -> Policy:
    """
    Calls Qt's 'Policy QLayoutPolicy::verticalPolicy() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlayoutpolicy.html#verticalPolicy

    Returns
    -------

    Policy
      The value standing for the combination Qt gave back.
    """
    #  Policy QLayoutPolicy::verticalPolicy() const
    return QLayoutPolicy.Policy(self.uglySide.call(
        'ritual_ZNK13QLayoutPolicy14verticalPolicyEv',
    ))

  def controlType(self) -> ControlType:
    """
    Calls Qt's 'ControlType QLayoutPolicy::controlType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlayoutpolicy.html#controlType

    Returns
    -------

    ControlType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'ControlType(number)'
      gives.
    """
    #  ControlType QLayoutPolicy::controlType() const
    return QLayoutPolicy.ControlType(self.uglySide.call(
        'ritual_ZNK13QLayoutPolicy11controlTypeEv',
    ))

  def expandingDirections(self) -> Qt.Orientations:
    """
    Calls Qt's 'Qt::Orientations QLayoutPolicy::expandingDirections() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlayoutpolicy.html#expandingDirections

    Returns
    -------

    Qt.Orientations
      The value standing for the combination Qt gave back.
    """
    #  Qt::Orientations QLayoutPolicy::expandingDirections() const
    return Qt.Orientations(self.uglySide.call(
        'ritual_ZNK13QLayoutPolicy19expandingDirectionsEv',
    ))

  def hasHeightForWidth(self) -> bool:
    """
    Calls Qt's 'bool QLayoutPolicy::hasHeightForWidth() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlayoutpolicy.html#hasHeightForWidth
    """
    #  bool QLayoutPolicy::hasHeightForWidth() const
    return self.uglySide.call(
        'ritual_ZNK13QLayoutPolicy17hasHeightForWidthEv',
    )

  def hasWidthForHeight(self) -> bool:
    """
    Calls Qt's 'bool QLayoutPolicy::hasWidthForHeight() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlayoutpolicy.html#hasWidthForHeight
    """
    #  bool QLayoutPolicy::hasWidthForHeight() const
    return self.uglySide.call(
        'ritual_ZNK13QLayoutPolicy17hasWidthForHeightEv',
    )

  def horizontalStretch(self) -> int:
    """
    Calls Qt's 'int QLayoutPolicy::horizontalStretch() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlayoutpolicy.html#horizontalStretch
    """
    #  int QLayoutPolicy::horizontalStretch() const
    return self.uglySide.call(
        'ritual_ZNK13QLayoutPolicy17horizontalStretchEv',
    )

  def verticalStretch(self) -> int:
    """
    Calls Qt's 'int QLayoutPolicy::verticalStretch() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlayoutpolicy.html#verticalStretch
    """
    #  int QLayoutPolicy::verticalStretch() const
    return self.uglySide.call('ritual_ZNK13QLayoutPolicy15verticalStretchEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Policy)
  def setHorizontalPolicy(self, d: Policy) -> None:
    """
    Calls Qt's 'void QLayoutPolicy::setHorizontalPolicy(Policy d)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlayoutpolicy.html#setHorizontalPolicy

    Parameters
    ----------

    d : Policy
      Passed on as its number.
    """
    #  void QLayoutPolicy::setHorizontalPolicy(Policy d)
    self.uglySide.call(
        'ritual_ZN13QLayoutPolicy19setHorizontalPolicyE6QFlagsINS_10PolicyF'
        'lagEE',
        d.value,
    )

  @overload(Policy)
  def setVerticalPolicy(self, d: Policy) -> None:
    """
    Calls Qt's 'void QLayoutPolicy::setVerticalPolicy(Policy d)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlayoutpolicy.html#setVerticalPolicy

    Parameters
    ----------

    d : Policy
      Passed on as its number.
    """
    #  void QLayoutPolicy::setVerticalPolicy(Policy d)
    self.uglySide.call(
        'ritual_ZN13QLayoutPolicy17setVerticalPolicyE6QFlagsINS_10PolicyFla'
        'gEE',
        d.value,
    )

  @overload(ControlType)
  def setControlType(self, type: ControlType) -> None:
    """
    Calls Qt's 'void QLayoutPolicy::setControlType(ControlType type)'.

    Qt's own words: https://doc.qt.io/qt-6/qlayoutpolicy.html#setControlType

    Parameters
    ----------

    type : ControlType
      Passed on as its number.
    """
    #  void QLayoutPolicy::setControlType(ControlType type)
    self.uglySide.call(
        'ritual_ZN13QLayoutPolicy14setControlTypeENS_11ControlTypeE',
        type.value,
    )

  @overload(bool)
  def setHeightForWidth(self, b: bool) -> None:
    """
    Calls Qt's 'void QLayoutPolicy::setHeightForWidth(bool b)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlayoutpolicy.html#setHeightForWidth

    Parameters
    ----------

    b : bool
      Passed on as it is.
    """
    #  void QLayoutPolicy::setHeightForWidth(bool b)
    self.uglySide.call('ritual_ZN13QLayoutPolicy17setHeightForWidthEb', b)

  @overload(bool)
  def setWidthForHeight(self, b: bool) -> None:
    """
    Calls Qt's 'void QLayoutPolicy::setWidthForHeight(bool b)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlayoutpolicy.html#setWidthForHeight

    Parameters
    ----------

    b : bool
      Passed on as it is.
    """
    #  void QLayoutPolicy::setWidthForHeight(bool b)
    self.uglySide.call('ritual_ZN13QLayoutPolicy17setWidthForHeightEb', b)

  @overload(int)
  def setHorizontalStretch(self, stretchFactor: int) -> None:
    """
    Calls Qt's 'void QLayoutPolicy::setHorizontalStretch(int stretchFactor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlayoutpolicy.html#setHorizontalStretch

    Parameters
    ----------

    stretchFactor : int
      Passed on as it is.
    """
    #  void QLayoutPolicy::setHorizontalStretch(int stretchFactor)
    self.uglySide.call(
        'ritual_ZN13QLayoutPolicy20setHorizontalStretchEi', stretchFactor,
    )

  @overload(int)
  def setVerticalStretch(self, stretchFactor: int) -> None:
    """
    Calls Qt's 'void QLayoutPolicy::setVerticalStretch(int stretchFactor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlayoutpolicy.html#setVerticalStretch

    Parameters
    ----------

    stretchFactor : int
      Passed on as it is.
    """
    #  void QLayoutPolicy::setVerticalStretch(int stretchFactor)
    self.uglySide.call(
        'ritual_ZN13QLayoutPolicy18setVerticalStretchEi', stretchFactor,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, s: QLayoutPolicy) -> bool:
    """
    Calls Qt's 'bool QLayoutPolicy::operator==(const QLayoutPolicy &s)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qlayoutpolicy.html#operator==

    Parameters
    ----------

    s : QLayoutPolicy
      Passed on as a value: Qt reads the C++ QLayoutPolicy, which stays
      Python's own.
    """
    #  bool QLayoutPolicy::operator==(const QLayoutPolicy &s) const
    return self.uglySide.call(
        'ritual_ZNK13QLayoutPolicyeqERKS_', self._valueOf(s),
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
  def __ne__(self, s: QLayoutPolicy) -> bool:
    """
    Calls Qt's 'bool QLayoutPolicy::operator!=(const QLayoutPolicy &s)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qlayoutpolicy.html#operator!=

    Parameters
    ----------

    s : QLayoutPolicy
      Passed on as a value: Qt reads the C++ QLayoutPolicy, which stays
      Python's own.
    """
    #  bool QLayoutPolicy::operator!=(const QLayoutPolicy &s) const
    return self.uglySide.call(
        'ritual_ZNK13QLayoutPolicyneERKS_', self._valueOf(s),
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
    Notes what was given, for Qt's 'QLayoutPolicy::QLayoutPolicy()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qlayoutpolicy.html#QLayoutPolicy
    """
    #  QLayoutPolicy::QLayoutPolicy()
    self._noteCreation(QLayoutPolicy, lambda: Rituals.call(
        'ritual_ZN13QLayoutPolicyC1Ev',
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
    Notes what was given, for Qt's 'QLayoutPolicy::QLayoutPolicy(Policy
    horizontal, Policy vertical, ControlType type)', which is called at the
    first use.

    Qt's own words: https://doc.qt.io/qt-6/qlayoutpolicy.html#QLayoutPolicy

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
    #  QLayoutPolicy::QLayoutPolicy(Policy horizontal, Policy vertical,
    #      ControlType type)
    self._noteCreation(QLayoutPolicy, lambda: Rituals.call(
        'ritual_ZN13QLayoutPolicyC1E6QFlagsINS_10PolicyFlagEES2_NS_11Contro'
        'lTypeE',
        horizontal.value, vertical.value, type.value,
    ))

  @overload(int)
  def __init__(self, i: int) -> None:
    """
    Notes what was given, for Qt's 'QLayoutPolicy::QLayoutPolicy(int i)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qlayoutpolicy.html#QLayoutPolicy

    Parameters
    ----------

    i : int
      Passed on as it is.
    """
    #  QLayoutPolicy::QLayoutPolicy(int i)
    self._noteCreation(QLayoutPolicy, lambda: Rituals.call(
        'ritual_ZN13QLayoutPolicyC1Ei', i,
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
    Calls Qt's 'void QLayoutPolicy::transpose()'.

    Qt's own words: https://doc.qt.io/qt-6/qlayoutpolicy.html#transpose
    """
    #  void QLayoutPolicy::transpose()
    self.uglySide.call('ritual_ZN13QLayoutPolicy9transposeEv')
