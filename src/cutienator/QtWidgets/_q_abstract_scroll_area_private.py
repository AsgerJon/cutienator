"""
QAbstractScrollAreaPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qabstractscrollarea_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QAbstractScrollAreaPrivate to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import Qt
from . import QFramePrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QEvent, QPoint
  from . import QAbstractScrollArea, QScrollBar
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEvent = WAIT['QEvent']
  QPoint = WAIT['QPoint']
  QScrollBar = WAIT['QScrollBar']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAbstractScrollAreaPrivate(QFramePrivate):
  """
  The cute side of Qt's QAbstractScrollAreaPrivate: a plain Python object
  standing in front of one C++ QAbstractScrollAreaPrivate.

  It is built on the cute 'QFramePrivate', as Qt's QAbstractScrollAreaPrivate
  is built on Qt's QFramePrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QAbstractScrollAreaPrivate that has a ritual and
  that Python can call so far, 10 names in all: 'q_func', 'replaceScrollBar',
  'layoutChildren', 'scrollBarPolicyChanged', 'canStartScrollingAt',
  'setScrollBarTransient', '_q_showOrHideScrollBars', 'contentsOffset',
  'viewportEvent', 'defaultSingleStep'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QAbstractScrollArea *QAbstractScrollAreaPrivate::q_func()
    const': takes in Python what 'QAbstractScrollArea
    *QAbstractScrollAreaPrivate::q_func()' takes.
  - Qt's 'QAbstractScrollAreaPrivate::~QAbstractScrollAreaPrivate()': the
    destructor: Python never removes a C++ QAbstractScrollAreaPrivate.
  - Qt's 'void QAbstractScrollAreaPrivate::layoutChildren_helper(bool
    *needHorizontalScrollbar, bool *needVerticalScrollbar)': takes a number
    to change where it is.

  What has no ritual
  ------------------

  4 of the 18 functions Qt declares: 3 leans on 'QScrollBarPrivate; 1 leans
  on 'vtable for QAbstractScrollAreaFilter', which Qt's source does not mark
  for use from outside Qt and has no code for that could be taken.

  What to expect
  --------------

  - The C++ QAbstractScrollAreaPrivate is created at the first use, not by
    'QAbstractScrollAreaPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAbstractScrollAreaPrivate.
  - Each name of Qt's QAbstractScrollAreaPrivate that has no cute function
    yet, '_q_hslide', '_q_vslide', 'flashScrollBars',
    'layoutChildren_helper', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAbstractScrollAreaPrivate'

  #  A C++ QAbstractScrollAreaPrivate Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QAbstractScrollAreaPrivate'

  #  The functions Qt calls itself that QAbstractScrollAreaPrivate is the
  #  first to declare. A class of a program built on it can write one anew,
  #  and Qt then calls that. For each name: the key C++ knows the function
  #  by, what it gives, and what it takes.
  __virtual_functions__ = {
      'scrollBarPolicyChanged': (
          ('_ZN26QAbstractScrollAreaPrivate22scrollBarPolicyChangedEN2Qt11O'
           'rientationENS0_15ScrollBarPolicyE',
           ('nothing', 'nothing', ''),
           (
               ('int', 'enum', 'QtCore:Qt.Orientation'),
               ('int', 'enum', 'QtCore:Qt.ScrollBarPolicy'),
           )),
      ),
      'canStartScrollingAt': (
          ('_ZNK26QAbstractScrollAreaPrivate19canStartScrollingAtERK6QPoint',
           ('bool', 'number', ''),
           (
               ('address', 'value', 'QtCore:QPoint'),
           )),
      ),
      'contentsOffset': (
          ('_ZNK26QAbstractScrollAreaPrivate14contentsOffsetEv',
           ('address', 'value', 'QtCore:QPoint'),
           ()),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QPoint)
  def canStartScrollingAt(self, startPos: QPoint) -> bool:
    """
    Calls Qt's 'bool QAbstractScrollAreaPrivate::canStartScrollingAt(const
    QPoint &startPos) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractscrollareaprivate.html

    Parameters
    ----------

    startPos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  bool QAbstractScrollAreaPrivate::canStartScrollingAt(const QPoint
    #      &startPos) const
    ritual = (
        'ritual_ZNK26QAbstractScrollAreaPrivate19canStartScrollingAtERK6QPo'
        'int')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK26QAbstractScrollAreaPrivate19canStartScrollingAtE'
          'RK6QPoint')
    return self.uglySide.call(ritual, self._valueOf(startPos))

  def contentsOffset(self) -> QPoint:
    """
    Calls Qt's 'QPoint QAbstractScrollAreaPrivate::contentsOffset() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractscrollareaprivate.html#contentsOffset

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint QAbstractScrollAreaPrivate::contentsOffset() const
    ritual = 'ritual_ZNK26QAbstractScrollAreaPrivate14contentsOffsetEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK26QAbstractScrollAreaPrivate14contentsOffsetEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QPoint
    return QPoint._cuteOwning(address)

  def defaultSingleStep(self) -> int:
    """
    Calls Qt's 'int QAbstractScrollAreaPrivate::defaultSingleStep() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractscrollareaprivate.html#defaultSingleStep
    """
    #  int QAbstractScrollAreaPrivate::defaultSingleStep() const
    return self.uglySide.call(
        'ritual_ZNK26QAbstractScrollAreaPrivate17defaultSingleStepEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QScrollBar, bool)
  @overload(NoneType, bool)
  def setScrollBarTransient(
      self,
      scrollBar: Optional[QScrollBar],
      transient: bool,
  ) -> None:
    """
    Calls Qt's 'void
    QAbstractScrollAreaPrivate::setScrollBarTransient(QScrollBar *scrollBar,
    bool transient)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractscrollareaprivate.html

    Parameters
    ----------

    scrollBar : Optional[QScrollBar]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    transient : bool
      Passed on as it is.
    """
    #  void QAbstractScrollAreaPrivate::setScrollBarTransient(QScrollBar
    #      *scrollBar, bool transient)
    self.uglySide.call(
        'ritual_ZN26QAbstractScrollAreaPrivate21setScrollBarTransientEP10QS'
        'crollBarb',
        self._addressOf(scrollBar), transient,
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
    'QAbstractScrollAreaPrivate::QAbstractScrollAreaPrivate()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractscrollareaprivate.html
    """
    #  QAbstractScrollAreaPrivate::QAbstractScrollAreaPrivate()
    self._noteCreation(QAbstractScrollAreaPrivate, lambda: Rituals.call(
        'ritual_ZN26QAbstractScrollAreaPrivateC1Ev',
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

  def q_func(self) -> Optional[QAbstractScrollArea]:
    """
    Calls Qt's 'QAbstractScrollArea *QAbstractScrollAreaPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractscrollareaprivate.html#q_func

    Returns
    -------

    Optional[QAbstractScrollArea]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractScrollArea *QAbstractScrollAreaPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN26QAbstractScrollAreaPrivate6q_funcEv',
    )
    from . import QAbstractScrollArea
    return QAbstractScrollArea._cuteAt(address)

  @overload(QScrollBar, Qt.Orientation)
  @overload(NoneType, Qt.Orientation)
  def replaceScrollBar(
      self,
      scrollBar: Optional[QScrollBar],
      orientation: Qt.Orientation,
  ) -> None:
    """
    Calls Qt's 'void QAbstractScrollAreaPrivate::replaceScrollBar(QScrollBar
    *scrollBar, Qt::Orientation orientation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractscrollareaprivate.html#replaceScrollBar

    Parameters
    ----------

    scrollBar : Optional[QScrollBar]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    orientation : Qt.Orientation
      Passed on as its number.
    """
    #  void QAbstractScrollAreaPrivate::replaceScrollBar(QScrollBar
    #      *scrollBar, Qt::Orientation orientation)
    self.uglySide.call(
        'ritual_ZN26QAbstractScrollAreaPrivate16replaceScrollBarEP10QScroll'
        'BarN2Qt11OrientationE',
        self._addressOf(scrollBar), orientation.value,
    )

  def layoutChildren(self) -> None:
    """
    Calls Qt's 'void QAbstractScrollAreaPrivate::layoutChildren()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractscrollareaprivate.html#layoutChildren
    """
    #  void QAbstractScrollAreaPrivate::layoutChildren()
    self.uglySide.call(
        'ritual_ZN26QAbstractScrollAreaPrivate14layoutChildrenEv',
    )

  @overload(Qt.Orientation, Qt.ScrollBarPolicy)
  def scrollBarPolicyChanged(
      self,
      a0: Qt.Orientation,
      a1: Qt.ScrollBarPolicy,
  ) -> None:
    """
    Calls Qt's 'void
    QAbstractScrollAreaPrivate::scrollBarPolicyChanged(Qt::Orientation a0,
    Qt::ScrollBarPolicy a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractscrollareaprivate.html

    Parameters
    ----------

    a0 : Qt.Orientation
      Passed on as its number.

    a1 : Qt.ScrollBarPolicy
      Passed on as its number.
    """
    #  void
    #      QAbstractScrollAreaPrivate::scrollBarPolicyChanged(Qt::Orientation
    #      a0, Qt::ScrollBarPolicy a1)
    ritual = (
        'ritual_ZN26QAbstractScrollAreaPrivate22scrollBarPolicyChangedEN2Qt'
        '11OrientationENS0_15ScrollBarPolicyE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN26QAbstractScrollAreaPrivate22scrollBarPolicyChange'
          'dEN2Qt11OrientationENS0_15ScrollBarPolicyE')
    self.uglySide.call(ritual, a0.value, a1.value)

  def _q_showOrHideScrollBars(self) -> None:
    """
    Calls Qt's 'void QAbstractScrollAreaPrivate::_q_showOrHideScrollBars()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractscrollareaprivate.html
    """
    #  void QAbstractScrollAreaPrivate::_q_showOrHideScrollBars()
    self.uglySide.call(
        'ritual_ZN26QAbstractScrollAreaPrivate23_q_showOrHideScrollBarsEv',
    )

  @overload(QEvent)
  @overload(NoneType)
  def viewportEvent(self, event: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QAbstractScrollAreaPrivate::viewportEvent(QEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractscrollareaprivate.html#viewportEvent

    Parameters
    ----------

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QAbstractScrollAreaPrivate::viewportEvent(QEvent *event)
    return self.uglySide.call(
        'ritual_ZN26QAbstractScrollAreaPrivate13viewportEventEP6QEvent',
        self._addressOf(event),
    )

  @staticmethod
  def _q_hslide(*__, **_) -> Never:
    """
    Qt's 'void QAbstractScrollAreaPrivate::_q_hslide(int a0)': leans on
    'QScrollBarPrivate::flash()', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QAbstractScrollAreaPrivate._q_hslide' has no cute function yet. "
        "Qt's 'void QAbstractScrollAreaPrivate::_q_hslide(int a0)': leans "
        "on 'QScrollBarPrivate::flash()', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def _q_vslide(*__, **_) -> Never:
    """
    Qt's 'void QAbstractScrollAreaPrivate::_q_vslide(int a0)': leans on
    'QScrollBarPrivate::flash()', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QAbstractScrollAreaPrivate._q_vslide' has no cute function yet. "
        "Qt's 'void QAbstractScrollAreaPrivate::_q_vslide(int a0)': leans "
        "on 'QScrollBarPrivate::flash()', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def flashScrollBars(*__, **_) -> Never:
    """
    Qt's 'void QAbstractScrollAreaPrivate::flashScrollBars()': leans on
    'QScrollBarPrivate::flash()', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QAbstractScrollAreaPrivate.flashScrollBars' has no cute function "
        "yet. Qt's 'void QAbstractScrollAreaPrivate::flashScrollBars()': "
        "leans on 'QScrollBarPrivate::flash()', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def layoutChildren_helper(*__, **_) -> Never:
    """
    Qt's 'void QAbstractScrollAreaPrivate::layoutChildren_helper(bool
    *needHorizontalScrollbar, bool *needVerticalScrollbar)': takes a number
    to change where it is.
    """
    raise NotImplementedError(
        "'QAbstractScrollAreaPrivate.layoutChildren_helper' has no cute "
        "function yet. Qt's 'void "
        "QAbstractScrollAreaPrivate::layoutChildren_helper(bool "
        "*needHorizontalScrollbar, bool *needVerticalScrollbar)': takes a "
        "number to change where it is.")
