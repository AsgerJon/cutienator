"""
QTextOption binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/qtextoption.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, MetaCute
from ..occult import Rituals
from ..QtCore import Qt


class QTextOption(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QTextOption: a plain Python object standing in front
  of one C++ QTextOption.

  C++ hands a QTextOption around as a copy, so every C++ QTextOption behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QTextOption that has a ritual and that Python can
  call so far, 12 names in all: 'setAlignment', 'alignment',
  'setTextDirection', 'textDirection', 'setWrapMode', 'wrapMode', 'setFlags',
  'flags', 'setTabStopDistance', 'tabStopDistance', 'setUseDesignMetrics',
  'useDesignMetrics'. It can be made from Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QTextOption::~QTextOption()': the destructor: Python removes its
    C++ QTextOption by it, and has no other use for it.

  What has no ritual
  ------------------

  5 of the 21 functions Qt declares: 5 takes or gives a type that cannot be
  passed yet.

  What to expect
  --------------

  - The C++ QTextOption is created at the first use, not by
    'QTextOption(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QTextOption back gives a copy the ritual made for
    Python, in a new cute QTextOption.
  """

  #  The enums Qt writes inside QTextOption, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class Flag(CuteFlags, number='unsigned int'):
    """
    The flags enum 'QTextOption::Flag' of Qt, with the 8 names Qt gives in
    it. Qt names the type of its combinations 'QTextOption::Flags'.
    """

    ShowTabsAndSpaces = 0x1
    ShowLineAndParagraphSeparators = 0x2
    AddSpaceForLineAndParagraphSeparators = 0x4
    SuppressColors = 0x8
    ShowDocumentTerminator = 0x10
    ShowDefaultIgnorables = 0x20
    DisableEmojiParsing = 0x40
    IncludeTrailingSpaces = 0x80000000

  Flags = Flag

  class TabType(CuteNum):
    """
    The enum 'QTextOption::TabType' of Qt, with the 4 names Qt gives in it.
    """

    LeftTab = Kee[int](0)
    RightTab = Kee[int](1)
    CenterTab = Kee[int](2)
    DelimiterTab = Kee[int](3)

  class WrapMode(CuteNum):
    """
    The enum 'QTextOption::WrapMode' of Qt, with the 5 names Qt gives in it.
    """

    NoWrap = Kee[int](0)
    WordWrap = Kee[int](1)
    ManualWrap = Kee[int](2)
    WrapAnywhere = Kee[int](3)
    WrapAtWordBoundaryOrAnywhere = Kee[int](4)

  #  The classes Qt writes inside QTextOption, each a class in here as in
  #  C++.

  class Tab(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QTextOption::Tab: a plain Python object standing in
    front of one C++ QTextOption::Tab.

    C++ hands a QTextOption::Tab around as a copy, so every C++
    QTextOption::Tab behind a cute one is Python's own: it is removed, by the
    ritual named in '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    Every function of Qt's QTextOption::Tab that has a ritual and that Python
    can call so far, 2 names in all: '__eq__', '__ne__'. It can be made from
    Python, in 1 way; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QTextOption::Tab::Tab(qreal pos, TabType tabType, QChar delim)':
      names the enum 'QTextOption::TabType', whose class cannot be named
      here.
    - Qt's 'QTextOption::Tab::~Tab()': the destructor: Python removes its C++
      QTextOption::Tab by it, and has no other use for it.

    What to expect
    --------------

    - The C++ QTextOption::Tab is created at the first use, not by
      'QTextOption::Tab(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QTextOption::Tab back gives a copy the ritual made
      for Python, in a new cute QTextOption::Tab.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QTextOption::Tab'

    #  Qt's '~QTextOption::Tab()'. Naming it makes this a value class: Python
    #  owns every C++ QTextOption::Tab behind a cute one, and removes it by
    #  this ritual.
    __delete_ritual__ = 'ritual_ZN11QTextOption3TabD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload(THIS)
    def __eq__(self, other: QTextOption.Tab) -> bool:
      """
      Calls Qt's 'bool QTextOption::Tab::operator==(const Tab &other) const'.

      Qt's own words: https://doc.qt.io/qt-6/qtextoption-tab.html#operator==

      Parameters
      ----------

      other : QTextOption.Tab
        Passed on as a value: Qt reads the C++ QTextOption::Tab, which stays
        Python's own.
      """
      #  bool QTextOption::Tab::operator==(const Tab &other) const
      return self.uglySide.call(
          'ritual_ZNK11QTextOption3TabeqERKS0_', self._valueOf(other),
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
    def __ne__(self, other: QTextOption.Tab) -> bool:
      """
      Calls Qt's 'bool QTextOption::Tab::operator!=(const Tab &other) const'.

      Qt's own words: https://doc.qt.io/qt-6/qtextoption-tab.html#operator!=

      Parameters
      ----------

      other : QTextOption.Tab
        Passed on as a value: Qt reads the C++ QTextOption::Tab, which stays
        Python's own.
      """
      #  bool QTextOption::Tab::operator!=(const Tab &other) const
      return self.uglySide.call(
          'ritual_ZNK11QTextOption3TabneERKS0_', self._valueOf(other),
      )

    @overload.fallback
    def __ne__(self, *args: object) -> object:
      """
      Tells Python that no function of this name takes what it was
      handed, with Python's own word for it. Python then asks the
      other side of the operator.
      """
      return NotImplemented

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload()
    def __init__(self) -> None:
      """
      Notes what was given, for Qt's 'QTextOption::Tab::Tab()', which is
      called at the first use.

      Qt's own words: https://doc.qt.io/qt-6/qtextoption-tab.html#Tab
      """
      #  QTextOption::Tab::Tab()
      self._noteCreation(QTextOption.Tab, lambda: Rituals.call(
          'ritual_ZN11QTextOption3TabC1Ev',
      ))

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QTextOption'

  #  Qt's '~QTextOption()'. Naming it makes this a value class: Python owns
  #  every C++ QTextOption behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN11QTextOptionD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def alignment(self) -> Qt.Alignment:
    """
    Calls Qt's 'Qt::Alignment QTextOption::alignment() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextoption.html#alignment

    Returns
    -------

    Qt.Alignment
      The value standing for the combination Qt gave back.
    """
    #  Qt::Alignment QTextOption::alignment() const
    return Qt.Alignment(self.uglySide.call(
        'ritual_ZNK11QTextOption9alignmentEv',
    ))

  def textDirection(self) -> Qt.LayoutDirection:
    """
    Calls Qt's 'Qt::LayoutDirection QTextOption::textDirection() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextoption.html#textDirection

    Returns
    -------

    Qt.LayoutDirection
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt.LayoutDirection(number)' gives.
    """
    #  Qt::LayoutDirection QTextOption::textDirection() const
    return Qt.LayoutDirection(self.uglySide.call(
        'ritual_ZNK11QTextOption13textDirectionEv',
    ))

  def wrapMode(self) -> WrapMode:
    """
    Calls Qt's 'WrapMode QTextOption::wrapMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextoption.html#wrapMode

    Returns
    -------

    WrapMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'WrapMode(number)' gives.
    """
    #  WrapMode QTextOption::wrapMode() const
    return QTextOption.WrapMode(self.uglySide.call(
        'ritual_ZNK11QTextOption8wrapModeEv',
    ))

  def flags(self) -> Flags:
    """
    Calls Qt's 'Flags QTextOption::flags() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextoption.html#flags

    Returns
    -------

    Flags
      The value standing for the combination Qt gave back.
    """
    #  Flags QTextOption::flags() const
    return QTextOption.Flags(self.uglySide.call(
        'ritual_ZNK11QTextOption5flagsEv',
    ))

  def tabStopDistance(self) -> float:
    """
    Calls Qt's 'qreal QTextOption::tabStopDistance() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextoption.html#tabStopDistance
    """
    #  qreal QTextOption::tabStopDistance() const
    return self.uglySide.call('ritual_ZNK11QTextOption15tabStopDistanceEv')

  def useDesignMetrics(self) -> bool:
    """
    Calls Qt's 'bool QTextOption::useDesignMetrics() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextoption.html#useDesignMetrics
    """
    #  bool QTextOption::useDesignMetrics() const
    return self.uglySide.call('ritual_ZNK11QTextOption16useDesignMetricsEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Qt.Alignment)
  def setAlignment(self, alignment: Qt.Alignment) -> None:
    """
    Calls Qt's 'void QTextOption::setAlignment(Qt::Alignment alignment)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextoption.html#setAlignment

    Parameters
    ----------

    alignment : Qt.Alignment
      Passed on as its number.
    """
    #  void QTextOption::setAlignment(Qt::Alignment alignment)
    self.uglySide.call(
        'ritual_ZN11QTextOption12setAlignmentE6QFlagsIN2Qt13AlignmentFlagEE',
        alignment.value,
    )

  @overload(Qt.LayoutDirection)
  def setTextDirection(self, aDirection: Qt.LayoutDirection) -> None:
    """
    Calls Qt's 'void QTextOption::setTextDirection(Qt::LayoutDirection
    aDirection)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextoption.html#setTextDirection

    Parameters
    ----------

    aDirection : Qt.LayoutDirection
      Passed on as its number.
    """
    #  void QTextOption::setTextDirection(Qt::LayoutDirection aDirection)
    self.uglySide.call(
        'ritual_ZN11QTextOption16setTextDirectionEN2Qt15LayoutDirectionE',
        aDirection.value,
    )

  @overload(WrapMode)
  def setWrapMode(self, wrap: WrapMode) -> None:
    """
    Calls Qt's 'void QTextOption::setWrapMode(WrapMode wrap)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextoption.html#setWrapMode

    Parameters
    ----------

    wrap : WrapMode
      Passed on as its number.
    """
    #  void QTextOption::setWrapMode(WrapMode wrap)
    self.uglySide.call(
        'ritual_ZN11QTextOption11setWrapModeENS_8WrapModeE', wrap.value,
    )

  @overload(Flags)
  def setFlags(self, flags: Flags) -> None:
    """
    Calls Qt's 'void QTextOption::setFlags(Flags flags)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextoption.html#setFlags

    Parameters
    ----------

    flags : Flags
      Passed on as its number.
    """
    #  void QTextOption::setFlags(Flags flags)
    self.uglySide.call(
        'ritual_ZN11QTextOption8setFlagsE6QFlagsINS_4FlagEE', flags.value,
    )

  @overload(float)
  def setTabStopDistance(self, tabStopDistance: float) -> None:
    """
    Calls Qt's 'void QTextOption::setTabStopDistance(qreal tabStopDistance)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextoption.html#setTabStopDistance

    Parameters
    ----------

    tabStopDistance : float
      Passed on as it is.
    """
    #  void QTextOption::setTabStopDistance(qreal tabStopDistance)
    self.uglySide.call(
        'ritual_ZN11QTextOption18setTabStopDistanceEd', tabStopDistance,
    )

  @overload(bool)
  def setUseDesignMetrics(self, b: bool) -> None:
    """
    Calls Qt's 'void QTextOption::setUseDesignMetrics(bool b)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextoption.html#setUseDesignMetrics

    Parameters
    ----------

    b : bool
      Passed on as it is.
    """
    #  void QTextOption::setUseDesignMetrics(bool b)
    self.uglySide.call('ritual_ZN11QTextOption19setUseDesignMetricsEb', b)

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
    Notes what was given, for Qt's 'QTextOption::QTextOption()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qtextoption.html#QTextOption
    """
    #  QTextOption::QTextOption()
    self._noteCreation(QTextOption, lambda: Rituals.call(
        'ritual_ZN11QTextOptionC1Ev',
    ))

  @overload(Qt.Alignment)
  def __init__(self, alignment: Qt.Alignment) -> None:
    """
    Notes what was given, for Qt's 'QTextOption::QTextOption(Qt::Alignment
    alignment)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qtextoption.html#QTextOption

    Parameters
    ----------

    alignment : Qt.Alignment
      Passed on as its number.
    """
    #  QTextOption::QTextOption(Qt::Alignment alignment)
    self._noteCreation(QTextOption, lambda: Rituals.call(
        'ritual_ZN11QTextOptionC1E6QFlagsIN2Qt13AlignmentFlagEE',
        alignment.value,
    ))

  @overload(THIS)
  def __init__(self, o: QTextOption) -> None:
    """
    Notes what was given, for Qt's 'QTextOption::QTextOption(const
    QTextOption &o)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qtextoption.html#QTextOption

    Parameters
    ----------

    o : QTextOption
      Passed on as a value: Qt reads the C++ QTextOption, which stays
      Python's own.
    """
    #  QTextOption::QTextOption(const QTextOption &o)
    self._noteCreation(QTextOption, lambda: Rituals.call(
        'ritual_ZN11QTextOptionC1ERKS_', self._valueOf(o),
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
