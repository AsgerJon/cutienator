"""
QTabBarPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qtabbar_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QTabBarPrivate to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QAbstractAnimation, QVariantAnimation
from . import QWidgetPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QPoint, QRect, QSize, QVariant
  from ..QtGui import QIcon
  from . import QStyleOptionTab, QStyleOptionTabBarBase, QTabBar
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPoint = WAIT['QPoint']
  QSize = WAIT['QSize']
  QStyleOptionTab = WAIT['QStyleOptionTab']
  QStyleOptionTabBarBase = WAIT['QStyleOptionTabBarBase']
  QTabBar = WAIT['QTabBar']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QTabBarPrivate(QWidgetPrivate):
  """
  The cute side of Qt's QTabBarPrivate: a plain Python object standing in
  front of one C++ QTabBarPrivate.

  It is built on the cute 'QWidgetPrivate', as Qt's QTabBarPrivate is built
  on Qt's QWidgetPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QTabBarPrivate that has a ritual and that Python can
  call so far, 30 names in all: 'q_func', 'calculateFirstLastVisible',
  'selectNewCurrentIndexFrom', 'calculateNewPosition', 'slide', 'init', 'at',
  'indexAtPos', 'isAnimated', 'validIndex', 'setCurrentNextEnabledIndex',
  'scrollTabs', 'closeTab', 'moveTab', 'moveTabFinished', 'refresh',
  'layoutTabs', 'layoutWidgets', 'layoutTab', 'updateMacBorderMetrics',
  'setupMovableTab', 'autoHideTabs', 'scrollRect', 'normalizedScrollRect',
  'hoveredTabIndex', 'initBasicStyleOption', 'makeVisible', 'lastVisibleTab',
  'initStyleBaseOption', 'killSwitchTabTimer'. It can be made from Python, in
  1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QTabBar *QTabBarPrivate::q_func() const': takes in Python
    what 'QTabBar *QTabBarPrivate::q_func()' takes.
  - Qt's 'QTabBarPrivate::~QTabBarPrivate()': the destructor: Python never
    removes a C++ QTabBarPrivate.
  - Qt's 'const Tab *QTabBarPrivate::at(int index) const': takes in Python
    what 'Tab *QTabBarPrivate::at(int index)' takes.

  What has no ritual
  ------------------

  1 of the 35 functions Qt declares: 1 cannot be called and cannot be called
  through the meta-object and cannot be copied.

  What to expect
  --------------

  - The C++ QTabBarPrivate is created at the first use, not by
    'QTabBarPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QTabBarPrivate.
  - Each name of Qt's QTabBarPrivate that has no cute function yet,
    'isTabInMacUnifiedToolbarArea', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The classes Qt writes inside QTabBarPrivate, each a class in here as in
  #  C++.

  class Tab(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QTabBarPrivate::Tab: a plain Python object standing
    in front of one C++ QTabBarPrivate::Tab.

    What exists
    -----------

    Every function of Qt's QTabBarPrivate::Tab that has a ritual and that
    Python can call so far, 1 name in all: 'startAnimation'. It can be made
    from Python, in 1 way; see '__init__'.

    What has no ritual
    ------------------

    4 of the 6 functions Qt declares: 4 forbidden.

    What to expect
    --------------

    - The C++ QTabBarPrivate::Tab is created at the first use, not by
      'QTabBarPrivate::Tab(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - Python never removes the C++ QTabBarPrivate::Tab.
    """

    #  The cute classes this class names and is not built on. Each waits
    #  until it is made; see 'WAIT'. A type checker reads the imports at the
    #  top of the file instead.
    if not TYPE_CHECKING:
      QIcon = WAIT['QIcon']
      QTabBarPrivate = WAIT['QTabBarPrivate']

    #  The classes Qt writes inside QTabBarPrivate::Tab, each a class in here
    #  as in C++.

    class TabBarAnimation(QVariantAnimation):
      """
      The cute side of Qt's QTabBarPrivate::Tab::TabBarAnimation: a plain
      Python object standing in front of one C++
      QTabBarPrivate::Tab::TabBarAnimation.

      It is built on the cute 'QVariantAnimation', as Qt's
      QTabBarPrivate::Tab::TabBarAnimation is built on Qt's
      QVariantAnimation, and has everything that class has.

      What exists
      -----------

      Every function of Qt's QTabBarPrivate::Tab::TabBarAnimation that has a
      ritual and that Python can call so far, 2 names in all:
      'updateCurrentValue', 'updateState'. None can be made from Python: one
      comes out of a function of another class that gives one back.

      What has a ritual and is left out, and why
      ------------------------------------------

      - Qt's 'QTabBarPrivate::Tab::TabBarAnimation::TabBarAnimation(Tab *t,
        QTabBarPrivate *_priv)': names a class it is written two deep inside.

      What to expect
      --------------

      - The C++ QTabBarPrivate::Tab::TabBarAnimation is created at the first
        use, not by 'QTabBarPrivate::Tab::TabBarAnimation(...)'.
      - A wrong argument is refused in Python, with 'DispatchException', and
        never reaches C++.
      - None is taken wherever Qt takes an object by its address, or text as
        C has it, and is passed on as nothing. Whether Qt can do with nothing
        there is as in C++.
      - Python never removes the C++ QTabBarPrivate::Tab::TabBarAnimation.
      - Qt tells when it has removed the C++
        QTabBarPrivate::Tab::TabBarAnimation. Every call on the cute object,
        and every use of it as an argument, then raises 'RuntimeError', and
        nothing reaches C++.
      - Each name of Qt's QTabBarPrivate::Tab::TabBarAnimation that has no
        cute function yet, '__init__', holds a function that raises
        'NotImplementedError', and its docstring says why.
      """

      #  The cute classes this class names and is not built on. Each waits
      #  until it is made; see 'WAIT'. A type checker reads the imports at
      #  the top of the file instead.
      if not TYPE_CHECKING:
        QVariant = WAIT['QVariant']

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      #  Class Variables
      #  The class of Qt this class stands for.
      __qt_class__ = 'QTabBarPrivate::Tab::TabBarAnimation'

      #  Fallback Variables

      #  Private Variables

      #  Public Variables

      #  Virtual Variables

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      @staticmethod
      def __init__(*__, **_) -> Never:
        """
        Qt's 'QTabBarPrivate::Tab::TabBarAnimation::TabBarAnimation(Tab *t,
        QTabBarPrivate *_priv)': names a class it is written two deep inside.
        """
        raise NotImplementedError(
            "'QTabBarPrivate.Tab.TabBarAnimation.__init__' has no cute "
            "function yet. Qt's "
            "'QTabBarPrivate::Tab::TabBarAnimation::TabBarAnimation(Tab *t, "
            "QTabBarPrivate *_priv)': names a class it is written two deep "
            "inside.")

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      @overload(QVariant)
      def updateCurrentValue(self, current: QVariant) -> None:
        """
        Calls Qt's 'void
        QTabBarPrivate::Tab::TabBarAnimation::updateCurrentValue(const
        QVariant &current)'.

        Qt's own words:
        https://doc.qt.io/qt-6/qtabbarprivate-tab-tabbaranimation.html

        Parameters
        ----------

        current : QVariant
          Passed on as a value: Qt reads the C++ QVariant, which stays
          Python's own.
        """
        #  void
        #      QTabBarPrivate::Tab::TabBarAnimation::updateCurrentValue(const
        #      QVariant &current)
        ritual = (
            'ritual_ZN14QTabBarPrivate3Tab15TabBarAnimation18updateCurrentV'
            'alueERK8QVariant')
        if self.uglySide.isOurs():
          ritual = (
              'ritual_own_ZN14QTabBarPrivate3Tab15TabBarAnimation18updateCu'
              'rrentValueERK8QVariant')
        self.uglySide.call(ritual, self._valueOf(current))

      @overload(QAbstractAnimation.State, QAbstractAnimation.State)
      def updateState(
          self,
          newState: QAbstractAnimation.State,
          a1: QAbstractAnimation.State,
      ) -> None:
        """
        Calls Qt's 'void
        QTabBarPrivate::Tab::TabBarAnimation::updateState(State newState,
        State a1)'.

        Qt's own words:
        https://doc.qt.io/qt-6/qtabbarprivate-tab-tabbaranimation.html

        Parameters
        ----------

        newState : QAbstractAnimation.State
          Passed on as its number.

        a1 : QAbstractAnimation.State
          Passed on as its number.
        """
        #  void QTabBarPrivate::Tab::TabBarAnimation::updateState(State
        #      newState, State a1)
        ritual = (
            'ritual_ZN14QTabBarPrivate3Tab15TabBarAnimation11updateStateEN1'
            '8QAbstractAnimation5StateES3_')
        if self.uglySide.isOurs():
          ritual = (
              'ritual_own_ZN14QTabBarPrivate3Tab15TabBarAnimation11updateSt'
              'ateEN18QAbstractAnimation5StateES3_')
        self.uglySide.call(ritual, newState.value, a1.value)

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QTabBarPrivate::Tab'

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

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload(QIcon, str)
    def __init__(self, ico: QIcon, txt: str) -> None:
      """
      Notes what was given, for Qt's 'QTabBarPrivate::Tab::Tab(const QIcon
      &ico, const QString &txt)', which is called at the first use.

      Qt's own words: https://doc.qt.io/qt-6/qtabbarprivate-tab.html#Tab

      Parameters
      ----------

      ico : QIcon
        Passed on as a value: Qt reads the C++ QIcon, which stays Python's
        own.

      txt : str
        Passed on as it is: a QString is made of it for the call.
      """
      #  QTabBarPrivate::Tab::Tab(const QIcon &ico, const QString &txt)
      self._noteCreation(QTabBarPrivate.Tab, lambda: Rituals.call(
          'ritual_ZN14QTabBarPrivate3TabC1ERK5QIconRK7QString',
          self._valueOf(ico), txt,
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

    @overload(QTabBarPrivate, int)
    @overload(NoneType, int)
    def startAnimation(
        self,
        priv: Optional[QTabBarPrivate],
        duration: int,
    ) -> None:
      """
      Calls Qt's 'void QTabBarPrivate::Tab::startAnimation(QTabBarPrivate
      *priv, int duration)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qtabbarprivate-tab.html#startAnimation

      Parameters
      ----------

      priv : Optional[QTabBarPrivate]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      duration : int
        Passed on as it is.
      """
      #  void QTabBarPrivate::Tab::startAnimation(QTabBarPrivate *priv, int
      #      duration)
      self.uglySide.call(
          'ritual_ZN14QTabBarPrivate3Tab14startAnimationEPS_i',
          self._addressOf(priv), duration,
      )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QStyleOptionTabBarBase, QTabBar, QSize)
  @overload(QStyleOptionTabBarBase, NoneType, QSize)
  @overload(NoneType, QTabBar, QSize)
  @overload(NoneType, NoneType, QSize)
  def initStyleBaseOption(
      optTabBase: Optional[QStyleOptionTabBarBase],
      tabbar: Optional[QTabBar],
      size: QSize,
  ) -> None:
    """
    Calls Qt's 'void
    QTabBarPrivate::initStyleBaseOption(QStyleOptionTabBarBase *optTabBase,
    QTabBar *tabbar, QSize size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtabbarprivate.html#initStyleBaseOption

    Parameters
    ----------

    optTabBase : Optional[QStyleOptionTabBarBase]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    tabbar : Optional[QTabBar]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void QTabBarPrivate::initStyleBaseOption(QStyleOptionTabBarBase
    #      *optTabBase, QTabBar *tabbar, QSize size)
    Rituals.call(
        'ritual_ZN14QTabBarPrivate19initStyleBaseOptionEP22QStyleOptionTabB'
        'arBaseP7QTabBar5QSize',
        CuteMixin._addressOf(optTabBase), CuteMixin._addressOf(tabbar),
        CuteMixin._valueOf(size),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QTabBarPrivate'

  #  A C++ QTabBarPrivate Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QTabBarPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int, int, int)
  def calculateNewPosition(self, from_: int, to: int, index: int) -> int:
    """
    Calls Qt's 'int QTabBarPrivate::calculateNewPosition(int from, int to,
    int index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtabbarprivate.html#calculateNewPosition

    Parameters
    ----------

    from_ : int
      Passed on as it is.

    to : int
      Passed on as it is.

    index : int
      Passed on as it is.
    """
    #  int QTabBarPrivate::calculateNewPosition(int from, int to, int index)
    #      const
    return self.uglySide.call(
        'ritual_ZNK14QTabBarPrivate20calculateNewPositionEiii',
        from_, to, index,
    )

  @overload(QPoint)
  def indexAtPos(self, p: QPoint) -> int:
    """
    Calls Qt's 'int QTabBarPrivate::indexAtPos(const QPoint &p) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtabbarprivate.html#indexAtPos

    Parameters
    ----------

    p : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  int QTabBarPrivate::indexAtPos(const QPoint &p) const
    return self.uglySide.call(
        'ritual_ZNK14QTabBarPrivate10indexAtPosERK6QPoint', self._valueOf(p),
    )

  def isAnimated(self) -> bool:
    """
    Calls Qt's 'bool QTabBarPrivate::isAnimated() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtabbarprivate.html#isAnimated
    """
    #  bool QTabBarPrivate::isAnimated() const
    return self.uglySide.call('ritual_ZNK14QTabBarPrivate10isAnimatedEv')

  @overload(int)
  def validIndex(self, index: int) -> bool:
    """
    Calls Qt's 'bool QTabBarPrivate::validIndex(int index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtabbarprivate.html#validIndex

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  bool QTabBarPrivate::validIndex(int index) const
    return self.uglySide.call(
        'ritual_ZNK14QTabBarPrivate10validIndexEi', index,
    )

  @overload()
  @overload(int)
  def scrollRect(self, index: int = -1) -> QRect:
    """
    Calls Qt's 'QRect QTabBarPrivate::scrollRect(int index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtabbarprivate.html#scrollRect

    Parameters
    ----------

    index : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QTabBarPrivate::scrollRect(int index) const
    address = self.uglySide.call(
        'ritual_ZNK14QTabBarPrivate10scrollRectEi', index,
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  @overload()
  @overload(int)
  def normalizedScrollRect(self, index: int = -1) -> QRect:
    """
    Calls Qt's 'QRect QTabBarPrivate::normalizedScrollRect(int index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtabbarprivate.html#normalizedScrollRect

    Parameters
    ----------

    index : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QTabBarPrivate::normalizedScrollRect(int index) const
    address = self.uglySide.call(
        'ritual_ZNK14QTabBarPrivate20normalizedScrollRectEi', index,
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  def hoveredTabIndex(self) -> int:
    """
    Calls Qt's 'int QTabBarPrivate::hoveredTabIndex() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtabbarprivate.html#hoveredTabIndex
    """
    #  int QTabBarPrivate::hoveredTabIndex() const
    return self.uglySide.call(
        'ritual_ZNK14QTabBarPrivate15hoveredTabIndexEv',
    )

  def lastVisibleTab(self) -> Optional[Tab]:
    """
    Calls Qt's 'const Tab *QTabBarPrivate::lastVisibleTab() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtabbarprivate.html#lastVisibleTab

    Returns
    -------

    Optional[Tab]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const Tab *QTabBarPrivate::lastVisibleTab() const
    address = self.uglySide.call(
        'ritual_ZNK14QTabBarPrivate14lastVisibleTabEv',
    )
    return QTabBarPrivate.Tab._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setCurrentNextEnabledIndex(self, offset: int) -> None:
    """
    Calls Qt's 'void QTabBarPrivate::setCurrentNextEnabledIndex(int offset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtabbarprivate.html#setCurrentNextEnabledIndex

    Parameters
    ----------

    offset : int
      Passed on as it is.
    """
    #  void QTabBarPrivate::setCurrentNextEnabledIndex(int offset)
    self.uglySide.call(
        'ritual_ZN14QTabBarPrivate26setCurrentNextEnabledIndexEi', offset,
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
    Notes what was given, for Qt's 'QTabBarPrivate::QTabBarPrivate()', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qtabbarprivate.html#QTabBarPrivate
    """
    #  QTabBarPrivate::QTabBarPrivate()
    self._noteCreation(QTabBarPrivate, lambda: Rituals.call(
        'ritual_ZN14QTabBarPrivateC1Ev',
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

  def q_func(self) -> Optional[QTabBar]:
    """
    Calls Qt's 'QTabBar *QTabBarPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qtabbarprivate.html#q_func

    Returns
    -------

    Optional[QTabBar]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTabBar *QTabBarPrivate::q_func()
    address = self.uglySide.call('ritual_ZN14QTabBarPrivate6q_funcEv')
    from . import QTabBar
    return QTabBar._cuteAt(address)

  @overload(int, bool, bool)
  def calculateFirstLastVisible(
      self,
      index: int,
      visible: bool,
      remove: bool,
  ) -> None:
    """
    Calls Qt's 'void QTabBarPrivate::calculateFirstLastVisible(int index,
    bool visible, bool remove)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtabbarprivate.html#calculateFirstLastVisible

    Parameters
    ----------

    index : int
      Passed on as it is.

    visible : bool
      Passed on as it is.

    remove : bool
      Passed on as it is.
    """
    #  void QTabBarPrivate::calculateFirstLastVisible(int index, bool
    #      visible, bool remove)
    self.uglySide.call(
        'ritual_ZN14QTabBarPrivate25calculateFirstLastVisibleEibb',
        index, visible, remove,
    )

  @overload(int)
  def selectNewCurrentIndexFrom(self, currentIndex: int) -> int:
    """
    Calls Qt's 'int QTabBarPrivate::selectNewCurrentIndexFrom(int
    currentIndex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtabbarprivate.html#selectNewCurrentIndexFrom

    Parameters
    ----------

    currentIndex : int
      Passed on as it is.
    """
    #  int QTabBarPrivate::selectNewCurrentIndexFrom(int currentIndex)
    return self.uglySide.call(
        'ritual_ZN14QTabBarPrivate25selectNewCurrentIndexFromEi',
        currentIndex,
    )

  @overload(int, int)
  def slide(self, from_: int, to: int) -> None:
    """
    Calls Qt's 'void QTabBarPrivate::slide(int from, int to)'.

    Qt's own words: https://doc.qt.io/qt-6/qtabbarprivate.html#slide

    Parameters
    ----------

    from_ : int
      Passed on as it is.

    to : int
      Passed on as it is.
    """
    #  void QTabBarPrivate::slide(int from, int to)
    self.uglySide.call('ritual_ZN14QTabBarPrivate5slideEii', from_, to)

  def init(self) -> None:
    """
    Calls Qt's 'void QTabBarPrivate::init()'.

    Qt's own words: https://doc.qt.io/qt-6/qtabbarprivate.html#init
    """
    #  void QTabBarPrivate::init()
    self.uglySide.call('ritual_ZN14QTabBarPrivate4initEv')

  @overload(int)
  def at(self, index: int) -> Optional[Tab]:
    """
    Calls Qt's 'Tab *QTabBarPrivate::at(int index)'.

    Qt's own words: https://doc.qt.io/qt-6/qtabbarprivate.html#at

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    Optional[Tab]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Tab *QTabBarPrivate::at(int index)
    address = self.uglySide.call('ritual_ZN14QTabBarPrivate2atEi', index)
    return QTabBarPrivate.Tab._cuteAt(address)

  def scrollTabs(self) -> None:
    """
    Calls Qt's 'void QTabBarPrivate::scrollTabs()'.

    Qt's own words: https://doc.qt.io/qt-6/qtabbarprivate.html#scrollTabs
    """
    #  void QTabBarPrivate::scrollTabs()
    self.uglySide.call('ritual_ZN14QTabBarPrivate10scrollTabsEv')

  def closeTab(self) -> None:
    """
    Calls Qt's 'void QTabBarPrivate::closeTab()'.

    Qt's own words: https://doc.qt.io/qt-6/qtabbarprivate.html#closeTab
    """
    #  void QTabBarPrivate::closeTab()
    self.uglySide.call('ritual_ZN14QTabBarPrivate8closeTabEv')

  @overload(int, int)
  def moveTab(self, index: int, offset: int) -> None:
    """
    Calls Qt's 'void QTabBarPrivate::moveTab(int index, int offset)'.

    Qt's own words: https://doc.qt.io/qt-6/qtabbarprivate.html#moveTab

    Parameters
    ----------

    index : int
      Passed on as it is.

    offset : int
      Passed on as it is.
    """
    #  void QTabBarPrivate::moveTab(int index, int offset)
    self.uglySide.call('ritual_ZN14QTabBarPrivate7moveTabEii', index, offset)

  @overload(int)
  def moveTabFinished(self, index: int) -> None:
    """
    Calls Qt's 'void QTabBarPrivate::moveTabFinished(int index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtabbarprivate.html#moveTabFinished

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QTabBarPrivate::moveTabFinished(int index)
    self.uglySide.call('ritual_ZN14QTabBarPrivate15moveTabFinishedEi', index)

  def refresh(self) -> None:
    """
    Calls Qt's 'void QTabBarPrivate::refresh()'.

    Qt's own words: https://doc.qt.io/qt-6/qtabbarprivate.html#refresh
    """
    #  void QTabBarPrivate::refresh()
    self.uglySide.call('ritual_ZN14QTabBarPrivate7refreshEv')

  def layoutTabs(self) -> None:
    """
    Calls Qt's 'void QTabBarPrivate::layoutTabs()'.

    Qt's own words: https://doc.qt.io/qt-6/qtabbarprivate.html#layoutTabs
    """
    #  void QTabBarPrivate::layoutTabs()
    self.uglySide.call('ritual_ZN14QTabBarPrivate10layoutTabsEv')

  @overload()
  @overload(int)
  def layoutWidgets(self, start: int = 0) -> None:
    """
    Calls Qt's 'void QTabBarPrivate::layoutWidgets(int start)'.

    Qt's own words: https://doc.qt.io/qt-6/qtabbarprivate.html#layoutWidgets

    Parameters
    ----------

    start : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  void QTabBarPrivate::layoutWidgets(int start)
    self.uglySide.call('ritual_ZN14QTabBarPrivate13layoutWidgetsEi', start)

  @overload(int)
  def layoutTab(self, index: int) -> None:
    """
    Calls Qt's 'void QTabBarPrivate::layoutTab(int index)'.

    Qt's own words: https://doc.qt.io/qt-6/qtabbarprivate.html#layoutTab

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QTabBarPrivate::layoutTab(int index)
    self.uglySide.call('ritual_ZN14QTabBarPrivate9layoutTabEi', index)

  def updateMacBorderMetrics(self) -> None:
    """
    Calls Qt's 'void QTabBarPrivate::updateMacBorderMetrics()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtabbarprivate.html#updateMacBorderMetrics
    """
    #  void QTabBarPrivate::updateMacBorderMetrics()
    self.uglySide.call('ritual_ZN14QTabBarPrivate22updateMacBorderMetricsEv')

  def setupMovableTab(self) -> None:
    """
    Calls Qt's 'void QTabBarPrivate::setupMovableTab()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtabbarprivate.html#setupMovableTab
    """
    #  void QTabBarPrivate::setupMovableTab()
    self.uglySide.call('ritual_ZN14QTabBarPrivate15setupMovableTabEv')

  def autoHideTabs(self) -> None:
    """
    Calls Qt's 'void QTabBarPrivate::autoHideTabs()'.

    Qt's own words: https://doc.qt.io/qt-6/qtabbarprivate.html#autoHideTabs
    """
    #  void QTabBarPrivate::autoHideTabs()
    self.uglySide.call('ritual_ZN14QTabBarPrivate12autoHideTabsEv')

  @overload(QStyleOptionTab, int)
  @overload(NoneType, int)
  def initBasicStyleOption(
      self,
      option: Optional[QStyleOptionTab],
      tabIndex: int,
  ) -> None:
    """
    Calls Qt's 'void QTabBarPrivate::initBasicStyleOption(QStyleOptionTab
    *option, int tabIndex) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtabbarprivate.html#initBasicStyleOption

    Parameters
    ----------

    option : Optional[QStyleOptionTab]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    tabIndex : int
      Passed on as it is.
    """
    #  void QTabBarPrivate::initBasicStyleOption(QStyleOptionTab *option, int
    #      tabIndex) const
    self.uglySide.call(
        'ritual_ZNK14QTabBarPrivate20initBasicStyleOptionEP15QStyleOptionTa'
        'bi',
        self._addressOf(option), tabIndex,
    )

  @overload(int)
  def makeVisible(self, index: int) -> None:
    """
    Calls Qt's 'void QTabBarPrivate::makeVisible(int index)'.

    Qt's own words: https://doc.qt.io/qt-6/qtabbarprivate.html#makeVisible

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QTabBarPrivate::makeVisible(int index)
    self.uglySide.call('ritual_ZN14QTabBarPrivate11makeVisibleEi', index)

  def killSwitchTabTimer(self) -> None:
    """
    Calls Qt's 'void QTabBarPrivate::killSwitchTabTimer()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtabbarprivate.html#killSwitchTabTimer
    """
    #  void QTabBarPrivate::killSwitchTabTimer()
    self.uglySide.call('ritual_ZN14QTabBarPrivate18killSwitchTabTimerEv')

  @staticmethod
  def isTabInMacUnifiedToolbarArea(*__, **_) -> Never:
    """
    Qt's 'bool QTabBarPrivate::isTabInMacUnifiedToolbarArea() const': cannot
    be called and cannot be called through the meta-object and cannot be
    copied: no header file has its code, Qt's source does not mark it or its
    class for use from outside Qt or writes it 'inline' or nowhere, and it is
    no signal, slot or invokable function giving back nothing, of a class
    built on QObject, and Qt's source has no code for it that could be told
    from the rest.
    """
    raise NotImplementedError(
        "'QTabBarPrivate.isTabInMacUnifiedToolbarArea' has no cute function "
        "yet. Qt's 'bool QTabBarPrivate::isTabInMacUnifiedToolbarArea() "
        "const': cannot be called and cannot be called through the "
        "meta-object and cannot be copied: no header file has its code, "
        "Qt's source does not mark it or its class for use from outside Qt "
        "or writes it 'inline' or nowhere, and it is no signal, slot or "
        "invokable function giving back nothing, of a class built on "
        "QObject, and Qt's source has no code for it that could be told "
        "from the rest.")
