"""
QUndoStackPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qundostack_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QUndoStackPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QObjectPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QAction, QUndoStack
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAction = WAIT['QAction']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QUndoStackPrivate(QObjectPrivate):
  """
  The cute side of Qt's QUndoStackPrivate: a plain Python object standing in
  front of one C++ QUndoStackPrivate.

  It is built on the cute 'QObjectPrivate', as Qt's QUndoStackPrivate is
  built on Qt's QObjectPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QUndoStackPrivate that has a ritual and that Python
  can call so far, 4 names in all: 'q_func', 'setIndex', 'checkUndoLimit',
  'setPrefixedText'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QUndoStack *QUndoStackPrivate::q_func() const': takes in
    Python what 'QUndoStack *QUndoStackPrivate::q_func()' takes.

  What to expect
  --------------

  - The C++ QUndoStackPrivate is created at the first use, not by
    'QUndoStackPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QUndoStackPrivate.
  """

  #  The classes Qt writes inside QUndoStackPrivate, each a class in here as
  #  in C++.

  class ActionState(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QUndoStackPrivate::ActionState: a plain Python
    object standing in front of one C++ QUndoStackPrivate::ActionState.

    C++ hands a QUndoStackPrivate::ActionState around as a copy, so every C++
    QUndoStackPrivate::ActionState behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    Every function of Qt's QUndoStackPrivate::ActionState that has a ritual
    and that Python can call so far, 2 names in all: '__eq__', '__ne__'. None
    can be made from Python: one comes out of a function of another class
    that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QUndoStackPrivate::ActionState::~ActionState()': the destructor:
      Python removes its C++ QUndoStackPrivate::ActionState by it, and has no
      other use for it.

    What to expect
    --------------

    - The C++ QUndoStackPrivate::ActionState is created at the first use, not
      by 'QUndoStackPrivate::ActionState(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QUndoStackPrivate::ActionState back gives a copy
      the ritual made for Python, in a new cute
      QUndoStackPrivate::ActionState.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QUndoStackPrivate::ActionState'

    #  Qt's '~QUndoStackPrivate::ActionState()'. Naming it makes this a value
    #  class: Python owns every C++ QUndoStackPrivate::ActionState behind a
    #  cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN17QUndoStackPrivate11ActionStateD1Ev'

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
    def __eq__(self, rhs: QUndoStackPrivate.ActionState) -> bool:
      """
      Calls Qt's 'bool operator==(const ActionState &lhs, const ActionState
      &rhs)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qundostackprivate-actionstate.html#operator==

      Parameters
      ----------

      rhs : QUndoStackPrivate.ActionState
        Passed on as a value: Qt reads the C++
        QUndoStackPrivate::ActionState, which stays Python's own.
      """
      #  bool operator==(const ActionState &lhs, const ActionState &rhs)
      return Rituals.call(
          'ritual_ZeqRKN17QUndoStackPrivate11ActionStateES2_',
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
    def __ne__(self, rhs: QUndoStackPrivate.ActionState) -> bool:
      """
      Calls Qt's 'bool operator!=(const ActionState &lhs, const ActionState
      &rhs)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qundostackprivate-actionstate.html#operator!=

      Parameters
      ----------

      rhs : QUndoStackPrivate.ActionState
        Passed on as a value: Qt reads the C++
        QUndoStackPrivate::ActionState, which stays Python's own.
      """
      #  bool operator!=(const ActionState &lhs, const ActionState &rhs)
      return Rituals.call(
          'ritual_ZneRKN17QUndoStackPrivate11ActionStateES2_',
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
  @overload(QAction, str, str, str)
  @overload(NoneType, str, str, str)
  def setPrefixedText(
      action: Optional[QAction],
      prefix: str,
      defaultText: str,
      text: str,
  ) -> None:
    """
    Calls Qt's 'void QUndoStackPrivate::setPrefixedText(QAction *action,
    const QString &prefix, const QString &defaultText, const QString &text)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qundostackprivate.html#setPrefixedText

    Parameters
    ----------

    action : Optional[QAction]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    prefix : str
      Passed on as it is: a QString is made of it for the call.

    defaultText : str
      Passed on as it is: a QString is made of it for the call.

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QUndoStackPrivate::setPrefixedText(QAction *action, const QString
    #      &prefix, const QString &defaultText, const QString &text)
    Rituals.call(
        'ritual_ZN17QUndoStackPrivate15setPrefixedTextEP7QActionRK7QStringS'
        '4_S4_',
        CuteMixin._addressOf(action), prefix, defaultText, text,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QUndoStackPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int, bool)
  def setIndex(self, idx: int, clean: bool) -> None:
    """
    Calls Qt's 'void QUndoStackPrivate::setIndex(int idx, bool clean)'.

    Qt's own words: https://doc.qt.io/qt-6/qundostackprivate.html#setIndex

    Parameters
    ----------

    idx : int
      Passed on as it is.

    clean : bool
      Passed on as it is.
    """
    #  void QUndoStackPrivate::setIndex(int idx, bool clean)
    self.uglySide.call(
        'ritual_ZN17QUndoStackPrivate8setIndexEib', idx, clean,
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
    Notes what was given, for Qt's 'QUndoStackPrivate::QUndoStackPrivate()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qundostackprivate.html#QUndoStackPrivate
    """
    #  QUndoStackPrivate::QUndoStackPrivate()
    self._noteCreation(QUndoStackPrivate, lambda: Rituals.call(
        'ritual_ZN17QUndoStackPrivateC1Ev',
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

  def q_func(self) -> Optional[QUndoStack]:
    """
    Calls Qt's 'QUndoStack *QUndoStackPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qundostackprivate.html#q_func

    Returns
    -------

    Optional[QUndoStack]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QUndoStack *QUndoStackPrivate::q_func()
    address = self.uglySide.call('ritual_ZN17QUndoStackPrivate6q_funcEv')
    from . import QUndoStack
    return QUndoStack._cuteAt(address)

  def checkUndoLimit(self) -> bool:
    """
    Calls Qt's 'bool QUndoStackPrivate::checkUndoLimit()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qundostackprivate.html#checkUndoLimit
    """
    #  bool QUndoStackPrivate::checkUndoLimit()
    return self.uglySide.call(
        'ritual_ZN17QUndoStackPrivate14checkUndoLimitEv',
    )
