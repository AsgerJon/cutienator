"""
QScrollerPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qscroller_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QScrollerPrivate to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QObject
from . import QScroller

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QPointF
  from . import QWidget
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPointF = WAIT['QPointF']
  QWidget = WAIT['QWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QScrollerPrivate(QObject):
  """
  The cute side of Qt's QScrollerPrivate: a plain Python object standing in
  front of one C++ QScrollerPrivate.

  It is built on the cute 'QObject', as Qt's QScrollerPrivate is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QScrollerPrivate that has a ritual and that Python
  can call so far, 13 names in all: 'metaObject', 'q_func', 'init', 'dpi',
  'setDpi', 'setDpiFromWidget', 'scrollingSegmentsEndPos',
  'scrollingSegmentsValid', 'nextSnapPos', 'frameRateSkip', 'stateName',
  'inputName', 'targetDestroyed'. None can be made from Python: one comes out
  of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QScrollerPrivate::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QScrollerPrivate::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'const QScroller *QScrollerPrivate::q_func() const': takes in Python
    what 'QScroller *QScrollerPrivate::q_func()' takes.
  - Qt's 'qreal QScrollerPrivate::nextSegmentPosition(QQueue<ScrollSegment>
    &segments, qint64 now, qreal oldPos)': takes a type Python has no way to
    hand over yet.

  What has no ritual
  ------------------

  25 of the 42 functions Qt declares: 17 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 6 leans on
  'QScrollerPrivate; 2 not a gap.

  What to expect
  --------------

  - The C++ QScrollerPrivate is created at the first use, not by
    'QScrollerPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QScrollerPrivate.
  - Qt tells when it has removed the C++ QScrollerPrivate. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QScrollerPrivate that has no cute function yet,
    '__init__', 'createScrollToSegments', 'createScrollingSegments',
    'handleDrag', 'moveWhileDragging', 'moveWhilePressed',
    'nextSegmentPosition', 'prepareScrolling', 'pressWhileInactive',
    'pressWhileScrolling', 'pushSegment', 'recalcScrollingSegments',
    'releaseWhileDragging', 'releaseWhilePressed', 'sendEvent',
    'setContentPositionHelperDragging', 'setContentPositionHelperScrolling',
    'setState', 'timerEventWhileDragging', 'timerEventWhileScrolling',
    'timerTick', 'updateVelocity', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QScrollerPrivate, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class ScrollType(CuteNum):
    """
    The enum 'QScrollerPrivate::ScrollType' of Qt, with the 3 names Qt gives
    in it.
    """

    ScrollTypeFlick = Kee[int](0)
    ScrollTypeScrollTo = Kee[int](1)
    ScrollTypeOvershoot = Kee[int](2)

  #  The classes Qt writes inside QScrollerPrivate, each a class in here as
  #  in C++.

  class ScrollSegment(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QScrollerPrivate::ScrollSegment: a plain Python
    object standing in front of one C++ QScrollerPrivate::ScrollSegment.

    C++ hands a QScrollerPrivate::ScrollSegment around as a copy, so every
    C++ QScrollerPrivate::ScrollSegment behind a cute one is Python's own: it
    is removed, by the ritual named in '__delete_ritual__', when the cute
    object goes.

    What exists
    -----------

    No function of Qt's QScrollerPrivate::ScrollSegment yet. None can be made
    from Python: one comes out of a function of another class that gives one
    back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QScrollerPrivate::ScrollSegment::~ScrollSegment()': the
      destructor: Python removes its C++ QScrollerPrivate::ScrollSegment by
      it, and has no other use for it.

    What to expect
    --------------

    - The C++ QScrollerPrivate::ScrollSegment is created at the first use,
      not by 'QScrollerPrivate::ScrollSegment(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QScrollerPrivate::ScrollSegment back gives a copy
      the ritual made for Python, in a new cute
      QScrollerPrivate::ScrollSegment.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QScrollerPrivate::ScrollSegment'

    #  Qt's '~QScrollerPrivate::ScrollSegment()'. Naming it makes this a
    #  value class: Python owns every C++ QScrollerPrivate::ScrollSegment
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN16QScrollerPrivate13ScrollSegmentD1Ev'

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

  @staticmethod
  @overload(QScroller.State)
  def stateName(state: QScroller.State) -> Optional[str]:
    """
    Calls Qt's 'const char *QScrollerPrivate::stateName(QScroller::State
    state)'.

    Qt's own words: https://doc.qt.io/qt-6/qscrollerprivate.html#stateName

    Parameters
    ----------

    state : QScroller.State
      Passed on as its number.

    Returns
    -------

    Optional[str]
      The text Qt gave back. None when Qt gave back no text.
    """
    #  const char *QScrollerPrivate::stateName(QScroller::State state)
    chars = Rituals.call(
        'ritual_ZN16QScrollerPrivate9stateNameEN9QScroller5StateE',
        state.value,
    )
    return None if chars is None else chars.decode()

  @staticmethod
  @overload(QScroller.Input)
  def inputName(input: QScroller.Input) -> Optional[str]:
    """
    Calls Qt's 'const char *QScrollerPrivate::inputName(QScroller::Input
    input)'.

    Qt's own words: https://doc.qt.io/qt-6/qscrollerprivate.html#inputName

    Parameters
    ----------

    input : QScroller.Input
      Passed on as its number.

    Returns
    -------

    Optional[str]
      The text Qt gave back. None when Qt gave back no text.
    """
    #  const char *QScrollerPrivate::inputName(QScroller::Input input)
    chars = Rituals.call(
        'ritual_ZN16QScrollerPrivate9inputNameEN9QScroller5InputE',
        input.value,
    )
    return None if chars is None else chars.decode()

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QScrollerPrivate'

  #  A C++ QScrollerPrivate Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QScrollerPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QScrollerPrivate::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qscrollerprivate.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QScrollerPrivate::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK16QScrollerPrivate10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def dpi(self) -> QPointF:
    """
    Calls Qt's 'QPointF QScrollerPrivate::dpi() const'.

    Qt's own words: https://doc.qt.io/qt-6/qscrollerprivate.html#dpi

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QScrollerPrivate::dpi() const
    address = self.uglySide.call('ritual_ZNK16QScrollerPrivate3dpiEv')
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  @overload(Qt.Orientation)
  def scrollingSegmentsEndPos(self, orientation: Qt.Orientation) -> float:
    """
    Calls Qt's 'qreal
    QScrollerPrivate::scrollingSegmentsEndPos(Qt::Orientation orientation)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscrollerprivate.html#scrollingSegmentsEndPos

    Parameters
    ----------

    orientation : Qt.Orientation
      Passed on as its number.
    """
    #  qreal QScrollerPrivate::scrollingSegmentsEndPos(Qt::Orientation
    #      orientation) const
    return self.uglySide.call(
        'ritual_ZNK16QScrollerPrivate23scrollingSegmentsEndPosEN2Qt11Orient'
        'ationE',
        orientation.value,
    )

  @overload(Qt.Orientation)
  def scrollingSegmentsValid(self, orientation: Qt.Orientation) -> bool:
    """
    Calls Qt's 'bool QScrollerPrivate::scrollingSegmentsValid(Qt::Orientation
    orientation) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscrollerprivate.html#scrollingSegmentsValid

    Parameters
    ----------

    orientation : Qt.Orientation
      Passed on as its number.
    """
    #  bool QScrollerPrivate::scrollingSegmentsValid(Qt::Orientation
    #      orientation) const
    return self.uglySide.call(
        'ritual_ZNK16QScrollerPrivate22scrollingSegmentsValidEN2Qt11Orienta'
        'tionE',
        orientation.value,
    )

  @overload(float, int, Qt.Orientation)
  def nextSnapPos(
      self,
      p: float,
      dir: int,
      orientation: Qt.Orientation,
  ) -> float:
    """
    Calls Qt's 'qreal QScrollerPrivate::nextSnapPos(qreal p, int dir,
    Qt::Orientation orientation) const'.

    Qt's own words: https://doc.qt.io/qt-6/qscrollerprivate.html#nextSnapPos

    Parameters
    ----------

    p : float
      Passed on as it is.

    dir : int
      Passed on as it is.

    orientation : Qt.Orientation
      Passed on as its number.
    """
    #  qreal QScrollerPrivate::nextSnapPos(qreal p, int dir, Qt::Orientation
    #      orientation) const
    return self.uglySide.call(
        'ritual_ZNK16QScrollerPrivate11nextSnapPosEdiN2Qt11OrientationE',
        p, dir, orientation.value,
    )

  def frameRateSkip(self) -> int:
    """
    Calls Qt's 'int QScrollerPrivate::frameRateSkip() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscrollerprivate.html#frameRateSkip
    """
    #  int QScrollerPrivate::frameRateSkip() const
    return self.uglySide.call(
        'ritual_ZNK16QScrollerPrivate13frameRateSkipEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QPointF)
  def setDpi(self, dpi: QPointF) -> None:
    """
    Calls Qt's 'void QScrollerPrivate::setDpi(const QPointF &dpi)'.

    Qt's own words: https://doc.qt.io/qt-6/qscrollerprivate.html#setDpi

    Parameters
    ----------

    dpi : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QScrollerPrivate::setDpi(const QPointF &dpi)
    self.uglySide.call(
        'ritual_ZN16QScrollerPrivate6setDpiERK7QPointF',
        self._valueOf(dpi, 'QPointF'),
    )

  @overload(QWidget)
  @overload(NoneType)
  def setDpiFromWidget(self, widget: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void QScrollerPrivate::setDpiFromWidget(QWidget *widget)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscrollerprivate.html#setDpiFromWidget

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QScrollerPrivate::setDpiFromWidget(QWidget *widget)
    self.uglySide.call(
        'ritual_ZN16QScrollerPrivate16setDpiFromWidgetEP7QWidget',
        self._addressOf(widget),
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QScrollerPrivate::QScrollerPrivate(QScroller *q, QObject *target)':
    leans on 'QScrollerPrivate::qt_metacall(QMetaObject::Call, int, void**)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QScrollerPrivate.__init__' has no cute function yet. Qt's "
        "'QScrollerPrivate::QScrollerPrivate(QScroller *q, QObject "
        "*target)': leans on "
        "'QScrollerPrivate::qt_metacall(QMetaObject::Call, int, void**)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

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

  def q_func(self) -> Optional[QScroller]:
    """
    Calls Qt's 'QScroller *QScrollerPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qscrollerprivate.html#q_func

    Returns
    -------

    Optional[QScroller]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QScroller *QScrollerPrivate::q_func()
    address = self.uglySide.call('ritual_ZN16QScrollerPrivate6q_funcEv')
    return QScroller._cuteAt(address)

  def init(self) -> None:
    """
    Calls Qt's 'void QScrollerPrivate::init()'.

    Qt's own words: https://doc.qt.io/qt-6/qscrollerprivate.html#init
    """
    #  void QScrollerPrivate::init()
    self.uglySide.call('ritual_ZN16QScrollerPrivate4initEv')

  def targetDestroyed(self) -> None:
    """
    Calls Qt's 'void QScrollerPrivate::targetDestroyed()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscrollerprivate.html#targetDestroyed
    """
    #  void QScrollerPrivate::targetDestroyed()
    self.uglySide.call('ritual_ZN16QScrollerPrivate15targetDestroyedEv')

  @staticmethod
  def createScrollToSegments(*__, **_) -> Never:
    """
    Qt's 'void QScrollerPrivate::createScrollToSegments(qreal v, qreal
    deltaTime, qreal endPos, Qt::Orientation orientation, ScrollType type)':
    Qt's library has no name for it, and its code in Qt's source does not
    compile apart from its file: unknown type name 'lcScroller'; did you mean
    'QScroller'?.
    """
    raise NotImplementedError(
        "'QScrollerPrivate.createScrollToSegments' has no cute function "
        "yet. Qt's 'void QScrollerPrivate::createScrollToSegments(qreal v, "
        "qreal deltaTime, qreal endPos, Qt::Orientation orientation, "
        "ScrollType type)': Qt's library has no name for it, and its code "
        "in Qt's source does not compile apart from its file: unknown type "
        "name 'lcScroller'; did you mean 'QScroller'?.")

  @staticmethod
  def createScrollingSegments(*__, **_) -> Never:
    """
    - Qt's 'void QScrollerPrivate::createScrollingSegments(qreal v, qreal
      startPos, qreal deltaTime, qreal deltaPos, Qt::Orientation
      orientation)': Qt's library has no name for it, and its code in Qt's
      source does not compile apart from its file: unknown type name
      'lcScroller'; did you mean 'QScroller'?.
    - Qt's 'void QScrollerPrivate::createScrollingSegments(const QPointF &v,
      const QPointF &startPos, const QPointF &ppm)': Qt's library has no name
      for it, and its code in Qt's source does not compile apart from its
      file: use of undeclared identifier 'differentialForProgress'.
    """
    raise NotImplementedError(
        "'QScrollerPrivate.createScrollingSegments' has no cute function "
        "yet. Qt's 'void QScrollerPrivate::createScrollingSegments(qreal v, "
        "qreal startPos, qreal deltaTime, qreal deltaPos, Qt::Orientation "
        "orientation)': Qt's library has no name for it, and its code in "
        "Qt's source does not compile apart from its file: unknown type "
        "name 'lcScroller'; did you mean 'QScroller'?. Qt's 'void "
        "QScrollerPrivate::createScrollingSegments(const QPointF &v, const "
        "QPointF &startPos, const QPointF &ppm)': Qt's library has no name "
        "for it, and its code in Qt's source does not compile apart from "
        "its file: use of undeclared identifier 'differentialForProgress'.")

  @staticmethod
  def handleDrag(*__, **_) -> Never:
    """
    Qt's 'void QScrollerPrivate::handleDrag(const QPointF &position, qint64
    timestamp)': Qt's library has no name for it, and its code in Qt's source
    does not compile apart from its file: unknown type name 'lcScroller'; did
    you mean 'QScroller'?.
    """
    raise NotImplementedError(
        "'QScrollerPrivate.handleDrag' has no cute function yet. Qt's 'void "
        "QScrollerPrivate::handleDrag(const QPointF &position, qint64 "
        "timestamp)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: unknown type name "
        "'lcScroller'; did you mean 'QScroller'?.")

  @staticmethod
  def moveWhileDragging(*__, **_) -> Never:
    """
    Qt's 'bool QScrollerPrivate::moveWhileDragging(const QPointF &position,
    qint64 timestamp)': leans on 'QScrollerPrivate::handleDrag(QPointF
    const&, long long)', which Qt's source does not mark for use from outside
    Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QScrollerPrivate.moveWhileDragging' has no cute function yet. "
        "Qt's 'bool QScrollerPrivate::moveWhileDragging(const QPointF "
        "&position, qint64 timestamp)': leans on "
        "'QScrollerPrivate::handleDrag(QPointF const&, long long)', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def moveWhilePressed(*__, **_) -> Never:
    """
    Qt's 'bool QScrollerPrivate::moveWhilePressed(const QPointF &position,
    qint64 timestamp)': Qt's library has no name for it, and its code in Qt's
    source does not compile apart from its file: invalid operands to binary
    expression ('QPointF' and 'QPointF').
    """
    raise NotImplementedError(
        "'QScrollerPrivate.moveWhilePressed' has no cute function yet. Qt's "
        "'bool QScrollerPrivate::moveWhilePressed(const QPointF &position, "
        "qint64 timestamp)': Qt's library has no name for it, and its code "
        "in Qt's source does not compile apart from its file: invalid "
        "operands to binary expression ('QPointF' and 'QPointF').")

  @staticmethod
  def nextSegmentPosition(*__, **_) -> Never:
    """
    Qt's 'qreal QScrollerPrivate::nextSegmentPosition(QQueue<ScrollSegment>
    &segments, qint64 now, qreal oldPos)': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QScrollerPrivate.nextSegmentPosition' has no cute function yet. "
        "Qt's 'qreal "
        "QScrollerPrivate::nextSegmentPosition(QQueue<ScrollSegment> "
        "&segments, qint64 now, qreal oldPos)': takes a type Python has no "
        "way to hand over yet.")

  @staticmethod
  def prepareScrolling(*__, **_) -> Never:
    """
    Qt's 'bool QScrollerPrivate::prepareScrolling(const QPointF &position)':
    Qt's library has no name for it, and its code in Qt's source does not
    compile apart from its file: unknown type name 'lcScroller'; did you mean
    'QScroller'?.
    """
    raise NotImplementedError(
        "'QScrollerPrivate.prepareScrolling' has no cute function yet. Qt's "
        "'bool QScrollerPrivate::prepareScrolling(const QPointF "
        "&position)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: unknown type name "
        "'lcScroller'; did you mean 'QScroller'?.")

  @staticmethod
  def pressWhileInactive(*__, **_) -> Never:
    """
    Qt's 'bool QScrollerPrivate::pressWhileInactive(const QPointF &position,
    qint64 timestamp)': leans on 'QScrollerPrivate::prepareScrolling(QPointF
    const&)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QScrollerPrivate.pressWhileInactive' has no cute function yet. "
        "Qt's 'bool QScrollerPrivate::pressWhileInactive(const QPointF "
        "&position, qint64 timestamp)': leans on "
        "'QScrollerPrivate::prepareScrolling(QPointF const&)', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def pressWhileScrolling(*__, **_) -> Never:
    """
    Qt's 'bool QScrollerPrivate::pressWhileScrolling(const QPointF &position,
    qint64 timestamp)': Qt's library has no name for it, and its code in Qt's
    source does not compile apart from its file: invalid operands to binary
    expression ('QPointF' and 'qreal' (aka 'double')).
    """
    raise NotImplementedError(
        "'QScrollerPrivate.pressWhileScrolling' has no cute function yet. "
        "Qt's 'bool QScrollerPrivate::pressWhileScrolling(const QPointF "
        "&position, qint64 timestamp)': Qt's library has no name for it, "
        "and its code in Qt's source does not compile apart from its file: "
        "invalid operands to binary expression ('QPointF' and 'qreal' (aka "
        "'double')).")

  @staticmethod
  def pushSegment(*__, **_) -> Never:
    """
    Qt's 'void QScrollerPrivate::pushSegment(ScrollType type, qreal
    deltaTime, qreal stopProgress, qreal startPos, qreal deltaPos, qreal
    stopPos, QEasingCurve::Type curve, Qt::Orientation orientation)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: unknown type name 'lcScroller'; did you mean
    'QScroller'?.
    """
    raise NotImplementedError(
        "'QScrollerPrivate.pushSegment' has no cute function yet. Qt's "
        "'void QScrollerPrivate::pushSegment(ScrollType type, qreal "
        "deltaTime, qreal stopProgress, qreal startPos, qreal deltaPos, "
        "qreal stopPos, QEasingCurve::Type curve, Qt::Orientation "
        "orientation)': Qt's library has no name for it, and its code in "
        "Qt's source does not compile apart from its file: unknown type "
        "name 'lcScroller'; did you mean 'QScroller'?.")

  @staticmethod
  def recalcScrollingSegments(*__, **_) -> Never:
    """
    Qt's 'void QScrollerPrivate::recalcScrollingSegments(bool forceRecalc)':
    leans on 'QScrollerPrivate::createScrollingSegments(QPointF const&,
    QPointF const&, QPointF const&)', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QScrollerPrivate.recalcScrollingSegments' has no cute function "
        "yet. Qt's 'void QScrollerPrivate::recalcScrollingSegments(bool "
        "forceRecalc)': leans on "
        "'QScrollerPrivate::createScrollingSegments(QPointF const&, QPointF "
        "const&, QPointF const&)', which Qt's source does not mark for use "
        "from outside Qt and has no code for that could be taken.")

  @staticmethod
  def releaseWhileDragging(*__, **_) -> Never:
    """
    Qt's 'bool QScrollerPrivate::releaseWhileDragging(const QPointF
    &position, qint64 timestamp)': Qt's library has no name for it, and its
    code in Qt's source does not compile apart from its file: invalid
    operands to binary expression ('QPointF' and 'QPointF').
    """
    raise NotImplementedError(
        "'QScrollerPrivate.releaseWhileDragging' has no cute function yet. "
        "Qt's 'bool QScrollerPrivate::releaseWhileDragging(const QPointF "
        "&position, qint64 timestamp)': Qt's library has no name for it, "
        "and its code in Qt's source does not compile apart from its file: "
        "invalid operands to binary expression ('QPointF' and 'QPointF').")

  @staticmethod
  def releaseWhilePressed(*__, **_) -> Never:
    """
    Qt's 'bool QScrollerPrivate::releaseWhilePressed(const QPointF &position,
    qint64 timestamp)': leans on
    'QScrollerPrivate::setState(QScroller::State)', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QScrollerPrivate.releaseWhilePressed' has no cute function yet. "
        "Qt's 'bool QScrollerPrivate::releaseWhilePressed(const QPointF "
        "&position, qint64 timestamp)': leans on "
        "'QScrollerPrivate::setState(QScroller::State)', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def sendEvent(*__, **_) -> Never:
    """
    Qt's 'void QScrollerPrivate::sendEvent(QObject *o, QEvent *e)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier
    'qt_sendSpontaneousEvent'.
    """
    raise NotImplementedError(
        "'QScrollerPrivate.sendEvent' has no cute function yet. Qt's 'void "
        "QScrollerPrivate::sendEvent(QObject *o, QEvent *e)': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: use of undeclared identifier "
        "'qt_sendSpontaneousEvent'.")

  @staticmethod
  def setContentPositionHelperDragging(*__, **_) -> Never:
    """
    Qt's 'void QScrollerPrivate::setContentPositionHelperDragging(const
    QPointF &deltaPos)': Qt's library has no name for it, and its code in
    Qt's source does not compile apart from its file: unknown type name
    'lcScroller'; did you mean 'QScroller'?.
    """
    raise NotImplementedError(
        "'QScrollerPrivate.setContentPositionHelperDragging' has no cute "
        "function yet. Qt's 'void "
        "QScrollerPrivate::setContentPositionHelperDragging(const QPointF "
        "&deltaPos)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: unknown type name "
        "'lcScroller'; did you mean 'QScroller'?.")

  @staticmethod
  def setContentPositionHelperScrolling(*__, **_) -> Never:
    """
    Qt's 'void QScrollerPrivate::setContentPositionHelperScrolling()': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: unknown type name 'lcScroller'; did you mean
    'QScroller'?.
    """
    raise NotImplementedError(
        "'QScrollerPrivate.setContentPositionHelperScrolling' has no cute "
        "function yet. Qt's 'void "
        "QScrollerPrivate::setContentPositionHelperScrolling()': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: unknown type name 'lcScroller'; did "
        "you mean 'QScroller'?.")

  @staticmethod
  def setState(*__, **_) -> Never:
    """
    Qt's 'void QScrollerPrivate::setState(QScroller::State s)': Qt's library
    has no name for it, and its code in Qt's source does not compile apart
    from its file: unknown type name 'lcScroller'; did you mean 'QScroller'?.
    """
    raise NotImplementedError(
        "'QScrollerPrivate.setState' has no cute function yet. Qt's 'void "
        "QScrollerPrivate::setState(QScroller::State s)': Qt's library has "
        "no name for it, and its code in Qt's source does not compile apart "
        "from its file: unknown type name 'lcScroller'; did you mean "
        "'QScroller'?.")

  @staticmethod
  def timerEventWhileDragging(*__, **_) -> Never:
    """
    Qt's 'void QScrollerPrivate::timerEventWhileDragging()': Qt's library has
    no name for it, and its code in Qt's source does not compile apart from
    its file: unknown type name 'lcScroller'; did you mean 'QScroller'?.
    """
    raise NotImplementedError(
        "'QScrollerPrivate.timerEventWhileDragging' has no cute function "
        "yet. Qt's 'void QScrollerPrivate::timerEventWhileDragging()': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: unknown type name 'lcScroller'; did "
        "you mean 'QScroller'?.")

  @staticmethod
  def timerEventWhileScrolling(*__, **_) -> Never:
    """
    Qt's 'void QScrollerPrivate::timerEventWhileScrolling()': Qt's library
    has no name for it, and its code in Qt's source does not compile apart
    from its file: unknown type name 'lcScroller'; did you mean 'QScroller'?.
    """
    raise NotImplementedError(
        "'QScrollerPrivate.timerEventWhileScrolling' has no cute function "
        "yet. Qt's 'void QScrollerPrivate::timerEventWhileScrolling()': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: unknown type name 'lcScroller'; "
        "did you mean 'QScroller'?.")

  @staticmethod
  def timerTick(*__, **_) -> Never:
    """
    Qt's 'void QScrollerPrivate::timerTick()': Qt's library has no name for
    it, and its code in Qt's source does not compile apart from its file:
    member access into incomplete type 'QScrollTimer'.
    """
    raise NotImplementedError(
        "'QScrollerPrivate.timerTick' has no cute function yet. Qt's 'void "
        "QScrollerPrivate::timerTick()': Qt's library has no name for it, "
        "and its code in Qt's source does not compile apart from its file: "
        "member access into incomplete type 'QScrollTimer'.")

  @staticmethod
  def updateVelocity(*__, **_) -> Never:
    """
    Qt's 'void QScrollerPrivate::updateVelocity(const QPointF &deltaPixelRaw,
    qint64 deltaTime)': Qt's library has no name for it, and its code in Qt's
    source does not compile apart from its file: unknown type name
    'lcScroller'; did you mean 'QScroller'?.
    """
    raise NotImplementedError(
        "'QScrollerPrivate.updateVelocity' has no cute function yet. Qt's "
        "'void QScrollerPrivate::updateVelocity(const QPointF "
        "&deltaPixelRaw, qint64 deltaTime)': Qt's library has no name for "
        "it, and its code in Qt's source does not compile apart from its "
        "file: unknown type name 'lcScroller'; did you mean 'QScroller'?.")
