"""
QSvgAbstractAnimation binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSvg/6.12.0/QtSvg/private/qsvgabstractanimation_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QSvgAbstractAnimation to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QSvgAbstractAnimatedProperty, QSvgEasingInterface
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QSvgAbstractAnimatedProperty = WAIT['QSvgAbstractAnimatedProperty']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSvgAbstractAnimation(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSvgAbstractAnimation: a plain Python object standing
  in front of one C++ QSvgAbstractAnimation.

  What exists
  -----------

  Every function of Qt's QSvgAbstractAnimation that has a ritual and that
  Python can call so far, 12 names in all: 'animationType',
  'evaluateAnimation', 'setRunningTime', 'start', 'duration',
  'setIterationCount', 'iterationCount', 'easing', 'appendProperty',
  'properties', 'finished', 'isActive'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSvgAbstractAnimation::~QSvgAbstractAnimation()': the destructor:
    Python never removes a C++ QSvgAbstractAnimation.

  What has no ritual
  ------------------

  5 of the 19 functions Qt declares: 4 forbidden; 1 the compiler refuses its
  ritual as it would be written here.

  What to expect
  --------------

  - The C++ QSvgAbstractAnimation is created at the first use, not by
    'QSvgAbstractAnimation(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSvgAbstractAnimation.
  - Each name of Qt's QSvgAbstractAnimation that has no cute function yet,
    'setEasing', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  #  The enums Qt writes inside QSvgAbstractAnimation, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class AnimationType(CuteNum):
    """
    The enum 'QSvgAbstractAnimation::AnimationType' of Qt, with the 2 names
    Qt gives in it.
    """

    CSS = Kee[int](0)
    SMIL = Kee[int](1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSvgAbstractAnimation'

  #  A C++ QSvgAbstractAnimation Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSvgAbstractAnimation'

  #  The functions Qt calls itself that QSvgAbstractAnimation is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'animationType': (
          ('_ZNK21QSvgAbstractAnimation13animationTypeEv',
           ('int', 'enum', 'QtSvg:QSvgAbstractAnimation.AnimationType'),
           ()),
      ),
      'appendProperty': (
          ('_ZN21QSvgAbstractAnimation14appendPropertyEP28QSvgAbstractAnima'
           'tedProperty',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtSvg:QSvgAbstractAnimatedProperty'),
           )),
      ),
      'isActive': (
          ('_ZNK21QSvgAbstractAnimation8isActiveEv',
           ('bool', 'number', ''),
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

  def animationType(self) -> AnimationType:
    """
    Calls Qt's 'AnimationType QSvgAbstractAnimation::animationType() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvgabstractanimation.html#animationType

    Returns
    -------

    AnimationType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'AnimationType(number)'
      gives.
    """
    #  AnimationType QSvgAbstractAnimation::animationType() const
    return QSvgAbstractAnimation.AnimationType(self._callAs(
        'QSvgAbstractAnimation',
        'ritual_ZNK21QSvgAbstractAnimation13animationTypeEv',
    ))

  def start(self) -> int:
    """
    Calls Qt's 'int QSvgAbstractAnimation::start() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgabstractanimation.html#start
    """
    #  int QSvgAbstractAnimation::start() const
    return self._callAs(
        'QSvgAbstractAnimation', 'ritual_ZNK21QSvgAbstractAnimation5startEv',
    )

  def duration(self) -> int:
    """
    Calls Qt's 'int QSvgAbstractAnimation::duration() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvgabstractanimation.html#duration
    """
    #  int QSvgAbstractAnimation::duration() const
    return self._callAs(
        'QSvgAbstractAnimation',
        'ritual_ZNK21QSvgAbstractAnimation8durationEv',
    )

  def iterationCount(self) -> int:
    """
    Calls Qt's 'int QSvgAbstractAnimation::iterationCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvgabstractanimation.html#iterationCount
    """
    #  int QSvgAbstractAnimation::iterationCount() const
    return self._callAs(
        'QSvgAbstractAnimation',
        'ritual_ZNK21QSvgAbstractAnimation14iterationCountEv',
    )

  def easing(self) -> Optional[QSvgEasingInterface]:
    """
    Calls Qt's 'QSvgEasingInterface *QSvgAbstractAnimation::easing() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgabstractanimation.html#easing

    Returns
    -------

    Optional[QSvgEasingInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSvgEasingInterface *QSvgAbstractAnimation::easing() const
    address = self._callAs(
        'QSvgAbstractAnimation',
        'ritual_ZNK21QSvgAbstractAnimation6easingEv',
    )
    from . import QSvgEasingInterface
    return QSvgEasingInterface._cuteAt(address)

  def properties(self) -> QList[QSvgAbstractAnimatedProperty]:
    """
    Calls Qt's 'QList<QSvgAbstractAnimatedProperty *>
    QSvgAbstractAnimation::properties() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvgabstractanimation.html#properties

    Returns
    -------

    QList[QSvgAbstractAnimatedProperty]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QSvgAbstractAnimatedProperty *>
    #      QSvgAbstractAnimation::properties() const
    address = self._callAs(
        'QSvgAbstractAnimation',
        'ritual_ZNK21QSvgAbstractAnimation10propertiesEv',
    )
    from . import QSvgAbstractAnimatedProperty
    return QList[QSvgAbstractAnimatedProperty]._cuteOwning(address)

  def finished(self) -> bool:
    """
    Calls Qt's 'bool QSvgAbstractAnimation::finished() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvgabstractanimation.html#finished
    """
    #  bool QSvgAbstractAnimation::finished() const
    return self._callAs(
        'QSvgAbstractAnimation',
        'ritual_ZNK21QSvgAbstractAnimation8finishedEv',
    )

  def isActive(self) -> bool:
    """
    Calls Qt's 'bool QSvgAbstractAnimation::isActive() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvgabstractanimation.html#isActive
    """
    #  bool QSvgAbstractAnimation::isActive() const
    ritual = 'ritual_ZNK21QSvgAbstractAnimation8isActiveEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK21QSvgAbstractAnimation8isActiveEv'
    return self._callAs('QSvgAbstractAnimation', ritual)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int, int)
  def setRunningTime(self, startMs: int, durationMs: int) -> None:
    """
    Calls Qt's 'void QSvgAbstractAnimation::setRunningTime(int startMs, int
    durationMs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvgabstractanimation.html#setRunningTime

    Parameters
    ----------

    startMs : int
      Passed on as it is.

    durationMs : int
      Passed on as it is.
    """
    #  void QSvgAbstractAnimation::setRunningTime(int startMs, int
    #      durationMs)
    self._callAs(
        'QSvgAbstractAnimation',
        'ritual_ZN21QSvgAbstractAnimation14setRunningTimeEii',
        startMs, durationMs,
    )

  @overload(int)
  def setIterationCount(self, count: int) -> None:
    """
    Calls Qt's 'void QSvgAbstractAnimation::setIterationCount(int count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvgabstractanimation.html#setIterationCount

    Parameters
    ----------

    count : int
      Passed on as it is.
    """
    #  void QSvgAbstractAnimation::setIterationCount(int count)
    self._callAs(
        'QSvgAbstractAnimation',
        'ritual_ZN21QSvgAbstractAnimation17setIterationCountEi',
        count,
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
    'QSvgAbstractAnimation::QSvgAbstractAnimation()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvgabstractanimation.html#QSvgAbstractAnimation
    """
    #  QSvgAbstractAnimation::QSvgAbstractAnimation()
    self._noteCreation(QSvgAbstractAnimation, lambda: Rituals.call(
        'ritual_ZN21QSvgAbstractAnimationC1Ev',
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

  @overload(float)
  def evaluateAnimation(self, elapsedTime: float) -> None:
    """
    Calls Qt's 'void QSvgAbstractAnimation::evaluateAnimation(qreal
    elapsedTime)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvgabstractanimation.html#evaluateAnimation

    Parameters
    ----------

    elapsedTime : float
      Passed on as it is.
    """
    #  void QSvgAbstractAnimation::evaluateAnimation(qreal elapsedTime)
    self._callAs(
        'QSvgAbstractAnimation',
        'ritual_ZN21QSvgAbstractAnimation17evaluateAnimationEd',
        elapsedTime,
    )

  @overload(QSvgAbstractAnimatedProperty)
  @overload(NoneType)
  def appendProperty(
      self,
      property: Optional[QSvgAbstractAnimatedProperty],
  ) -> None:
    """
    Calls Qt's 'void
    QSvgAbstractAnimation::appendProperty(QSvgAbstractAnimatedProperty
    *property)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvgabstractanimation.html#appendProperty

    Parameters
    ----------

    property : Optional[QSvgAbstractAnimatedProperty]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void
    #      QSvgAbstractAnimation::appendProperty(QSvgAbstractAnimatedProperty
    #      *property)
    ritual = (
        'ritual_ZN21QSvgAbstractAnimation14appendPropertyEP28QSvgAbstractAn'
        'imatedProperty')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN21QSvgAbstractAnimation14appendPropertyEP28QSvgAbst'
          'ractAnimatedProperty')
    self._callAs('QSvgAbstractAnimation', ritual, self._addressOf(property))

  @staticmethod
  def setEasing(*__, **_) -> Never:
    """
    Qt's 'void QSvgAbstractAnimation::setEasing(QSvgEasingInterfacePtr
    easing)': the compiler refuses its ritual as it would be written here:
    call to deleted constructor of 'QSvgEasingInterfacePtr' (aka
    'std::unique_ptr<QSvgEasingInterface>').
    """
    raise NotImplementedError(
        "'QSvgAbstractAnimation.setEasing' has no cute function yet. Qt's "
        "'void QSvgAbstractAnimation::setEasing(QSvgEasingInterfacePtr "
        "easing)': the compiler refuses its ritual as it would be written "
        "here: call to deleted constructor of 'QSvgEasingInterfacePtr' (aka "
        "'std::unique_ptr<QSvgEasingInterface>').")


#  Qt's 'QList<QSvgAbstractAnimation *>': the list of QSvgAbstractAnimation,
#  which 'QList[QSvgAbstractAnimation]' gives. It is made here, so that there
#  is one as soon as there can be a QSvgAbstractAnimation.
QList.createKind(
    QSvgAbstractAnimation, 'address',
    make='ritual_list_make_QSvgAbstractAnimation_ptr',
    add='ritual_list_add_QSvgAbstractAnimation_ptr',
    size='ritual_list_size_QSvgAbstractAnimation_ptr',
    at='ritual_list_at_QSvgAbstractAnimation_ptr',
    drop='ritual_list_drop_QSvgAbstractAnimation_ptr',
)
