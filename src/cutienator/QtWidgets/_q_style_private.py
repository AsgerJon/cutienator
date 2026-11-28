"""
QStylePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qstyle_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QStylePrivate to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObjectPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QStyle
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QStyle = WAIT['QStyle']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QStylePrivate(QObjectPrivate):
  """
  The cute side of Qt's QStylePrivate: a plain Python object standing in
  front of one C++ QStylePrivate.

  It is built on the cute 'QObjectPrivate', as Qt's QStylePrivate is built on
  Qt's QObjectPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QStylePrivate that has a ritual and that Python can
  call so far, 3 names in all: 'q_func', 'get', 'useFullScreenForPopup'. None
  can be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QStyle *QStylePrivate::q_func() const': takes in Python what
    'QStyle *QStylePrivate::q_func()' takes.
  - Qt's 'const QStylePrivate *QStylePrivate::get(const QStyle *s)': takes in
    Python what 'QStylePrivate *QStylePrivate::get(QStyle *s)' takes.

  What to expect
  --------------

  - The C++ QStylePrivate is created at the first use, not by
    'QStylePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QStylePrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QStyle)
  @overload(NoneType)
  def get(s: Optional[QStyle]) -> Optional[QStylePrivate]:
    """
    Calls Qt's 'QStylePrivate *QStylePrivate::get(QStyle *s)'.

    Qt's own words: https://doc.qt.io/qt-6/qstyleprivate.html#get

    Parameters
    ----------

    s : Optional[QStyle]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QStylePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QStylePrivate *QStylePrivate::get(QStyle *s)
    address = Rituals.call(
        'ritual_ZN13QStylePrivate3getEP6QStyle', CuteMixin._addressOf(s),
    )
    return QStylePrivate._cuteAt(address)

  @staticmethod
  def useFullScreenForPopup() -> bool:
    """
    Calls Qt's 'bool QStylePrivate::useFullScreenForPopup()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstyleprivate.html#useFullScreenForPopup
    """
    #  bool QStylePrivate::useFullScreenForPopup()
    return Rituals.call('ritual_ZN13QStylePrivate21useFullScreenForPopupEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QStylePrivate'

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

  def q_func(self) -> Optional[QStyle]:
    """
    Calls Qt's 'QStyle *QStylePrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qstyleprivate.html#q_func

    Returns
    -------

    Optional[QStyle]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QStyle *QStylePrivate::q_func()
    address = self.uglySide.call('ritual_ZN13QStylePrivate6q_funcEv')
    from . import QStyle
    return QStyle._cuteAt(address)
