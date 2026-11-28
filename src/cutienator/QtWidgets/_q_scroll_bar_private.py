"""
QScrollBarPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qscrollbar_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QScrollBarPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from . import QAbstractSliderPrivate, QStyle

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QPoint
  from . import QScrollBar
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPoint = WAIT['QPoint']


class QScrollBarPrivate(QAbstractSliderPrivate):
  """
  The cute side of Qt's QScrollBarPrivate: a plain Python object standing in
  front of one C++ QScrollBarPrivate.

  It is built on the cute 'QAbstractSliderPrivate', as Qt's QScrollBarPrivate
  is built on Qt's QAbstractSliderPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QScrollBarPrivate that has a ritual and that Python
  can call so far, 8 names in all: 'q_func', 'activateControl',
  'stopRepeatAction', 'pixelPosToRangeValue', 'init', 'updateHoverControl',
  'newHoverControl', 'setTransient'. None can be made from Python: one comes
  out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QScrollBar *QScrollBarPrivate::q_func() const': takes in
    Python what 'QScrollBar *QScrollBarPrivate::q_func()' takes.

  What has no ritual
  ------------------

  1 of the 10 functions Qt declares: 1 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QScrollBarPrivate is created at the first use, not by
    'QScrollBarPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QScrollBarPrivate.
  - Each name of Qt's QScrollBarPrivate that has no cute function yet,
    'flash', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QScrollBarPrivate'

  #  A C++ QScrollBarPrivate Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QScrollBarPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def pixelPosToRangeValue(self, pos: int) -> int:
    """
    Calls Qt's 'int QScrollBarPrivate::pixelPosToRangeValue(int pos) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscrollbarprivate.html#pixelPosToRangeValue

    Parameters
    ----------

    pos : int
      Passed on as it is.
    """
    #  int QScrollBarPrivate::pixelPosToRangeValue(int pos) const
    return self.uglySide.call(
        'ritual_ZNK17QScrollBarPrivate20pixelPosToRangeValueEi', pos,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setTransient(self, value: bool) -> None:
    """
    Calls Qt's 'void QScrollBarPrivate::setTransient(bool value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscrollbarprivate.html#setTransient

    Parameters
    ----------

    value : bool
      Passed on as it is.
    """
    #  void QScrollBarPrivate::setTransient(bool value)
    self.uglySide.call('ritual_ZN17QScrollBarPrivate12setTransientEb', value)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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

  def q_func(self) -> Optional[QScrollBar]:
    """
    Calls Qt's 'QScrollBar *QScrollBarPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qscrollbarprivate.html#q_func

    Returns
    -------

    Optional[QScrollBar]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QScrollBar *QScrollBarPrivate::q_func()
    address = self.uglySide.call('ritual_ZN17QScrollBarPrivate6q_funcEv')
    from . import QScrollBar
    return QScrollBar._cuteAt(address)

  @overload(int)
  @overload(int, int)
  def activateControl(self, control: int, threshold: int = 500) -> None:
    """
    Calls Qt's 'void QScrollBarPrivate::activateControl(uint control, int
    threshold)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscrollbarprivate.html#activateControl

    Parameters
    ----------

    control : int
      Passed on as it is.

    threshold : int
      Passed on as it is. May be left out, as in Qt: it is then 500.
    """
    #  void QScrollBarPrivate::activateControl(uint control, int threshold)
    self.uglySide.call(
        'ritual_ZN17QScrollBarPrivate15activateControlEji',
        control, threshold,
    )

  def stopRepeatAction(self) -> None:
    """
    Calls Qt's 'void QScrollBarPrivate::stopRepeatAction()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscrollbarprivate.html#stopRepeatAction
    """
    #  void QScrollBarPrivate::stopRepeatAction()
    self.uglySide.call('ritual_ZN17QScrollBarPrivate16stopRepeatActionEv')

  def init(self) -> None:
    """
    Calls Qt's 'void QScrollBarPrivate::init()'.

    Qt's own words: https://doc.qt.io/qt-6/qscrollbarprivate.html#init
    """
    #  void QScrollBarPrivate::init()
    self.uglySide.call('ritual_ZN17QScrollBarPrivate4initEv')

  @overload(QPoint)
  def updateHoverControl(self, pos: QPoint) -> bool:
    """
    Calls Qt's 'bool QScrollBarPrivate::updateHoverControl(const QPoint
    &pos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscrollbarprivate.html#updateHoverControl

    Parameters
    ----------

    pos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  bool QScrollBarPrivate::updateHoverControl(const QPoint &pos)
    return self.uglySide.call(
        'ritual_ZN17QScrollBarPrivate18updateHoverControlERK6QPoint',
        self._valueOf(pos),
    )

  @overload(QPoint)
  def newHoverControl(self, pos: QPoint) -> QStyle.SubControl:
    """
    Calls Qt's 'QStyle::SubControl QScrollBarPrivate::newHoverControl(const
    QPoint &pos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscrollbarprivate.html#newHoverControl

    Parameters
    ----------

    pos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    Returns
    -------

    QStyle.SubControl
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QStyle.SubControl(number)' gives.
    """
    #  QStyle::SubControl QScrollBarPrivate::newHoverControl(const QPoint
    #      &pos)
    return QStyle.SubControl(self.uglySide.call(
        'ritual_ZN17QScrollBarPrivate15newHoverControlERK6QPoint',
        self._valueOf(pos),
    ))

  @staticmethod
  def flash(*__, **_) -> Never:
    """
    Qt's 'void QScrollBarPrivate::flash()': Qt's library has no name for it,
    and its code in Qt's source does not compile apart from its file: no
    matching literal operator for call to 'operator""ns' with argument of
    type 'unsigned long long' or 'const char *', and no matching literal
    operator template.
    """
    raise NotImplementedError(
        "'QScrollBarPrivate.flash' has no cute function yet. Qt's 'void "
        "QScrollBarPrivate::flash()': Qt's library has no name for it, and "
        "its code in Qt's source does not compile apart from its file: no "
        "matching literal operator for call to 'operator\"\"ns' with "
        "argument of type 'unsigned long long' or 'const char *', and no "
        "matching literal operator template.")
