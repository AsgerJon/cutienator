"""
QKeySequenceEditPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qkeysequenceedit_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QKeySequenceEditPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..QtCore import Qt
from . import QWidgetPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QKeySequenceEdit


class QKeySequenceEditPrivate(QWidgetPrivate):
  """
  The cute side of Qt's QKeySequenceEditPrivate: a plain Python object
  standing in front of one C++ QKeySequenceEditPrivate.

  It is built on the cute 'QWidgetPrivate', as Qt's QKeySequenceEditPrivate
  is built on Qt's QWidgetPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QKeySequenceEditPrivate that has a ritual and that
  Python can call so far, 6 names in all: 'q_func', 'init',
  'translateModifiers', 'resetState', 'finishEditing', 'rebuildKeySequence'.
  None can be made from Python: one comes out of a function of another class
  that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QKeySequenceEdit *QKeySequenceEditPrivate::q_func() const':
    takes in Python what 'QKeySequenceEdit
    *QKeySequenceEditPrivate::q_func()' takes.

  What to expect
  --------------

  - The C++ QKeySequenceEditPrivate is created at the first use, not by
    'QKeySequenceEditPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QKeySequenceEditPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QKeySequenceEditPrivate'

  #  A C++ QKeySequenceEditPrivate Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QKeySequenceEditPrivate'

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

  def q_func(self) -> Optional[QKeySequenceEdit]:
    """
    Calls Qt's 'QKeySequenceEdit *QKeySequenceEditPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qkeysequenceeditprivate.html#q_func

    Returns
    -------

    Optional[QKeySequenceEdit]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QKeySequenceEdit *QKeySequenceEditPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN23QKeySequenceEditPrivate6q_funcEv',
    )
    from . import QKeySequenceEdit
    return QKeySequenceEdit._cuteAt(address)

  def init(self) -> None:
    """
    Calls Qt's 'void QKeySequenceEditPrivate::init()'.

    Qt's own words: https://doc.qt.io/qt-6/qkeysequenceeditprivate.html#init
    """
    #  void QKeySequenceEditPrivate::init()
    self.uglySide.call('ritual_ZN23QKeySequenceEditPrivate4initEv')

  @overload(Qt.KeyboardModifiers, str)
  def translateModifiers(
      self,
      state: Qt.KeyboardModifiers,
      text: str,
  ) -> int:
    """
    Calls Qt's 'int
    QKeySequenceEditPrivate::translateModifiers(Qt::KeyboardModifiers state,
    const QString &text)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qkeysequenceeditprivate.html#translateModifiers

    Parameters
    ----------

    state : Qt.KeyboardModifiers
      Passed on as its number.

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  int QKeySequenceEditPrivate::translateModifiers(Qt::KeyboardModifiers
    #      state, const QString &text)
    return self.uglySide.call(
        'ritual_ZN23QKeySequenceEditPrivate18translateModifiersE6QFlagsIN2Q'
        't16KeyboardModifierEERK7QString',
        state.value, text,
    )

  def resetState(self) -> None:
    """
    Calls Qt's 'void QKeySequenceEditPrivate::resetState()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qkeysequenceeditprivate.html#resetState
    """
    #  void QKeySequenceEditPrivate::resetState()
    self.uglySide.call('ritual_ZN23QKeySequenceEditPrivate10resetStateEv')

  def finishEditing(self) -> None:
    """
    Calls Qt's 'void QKeySequenceEditPrivate::finishEditing()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qkeysequenceeditprivate.html#finishEditing
    """
    #  void QKeySequenceEditPrivate::finishEditing()
    self.uglySide.call('ritual_ZN23QKeySequenceEditPrivate13finishEditingEv')

  def rebuildKeySequence(self) -> None:
    """
    Calls Qt's 'void QKeySequenceEditPrivate::rebuildKeySequence()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qkeysequenceeditprivate.html#rebuildKeySequence
    """
    #  void QKeySequenceEditPrivate::rebuildKeySequence()
    self.uglySide.call(
        'ritual_ZN23QKeySequenceEditPrivate18rebuildKeySequenceEv',
    )
