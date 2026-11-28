"""
QQuickHorizontalHeaderViewPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickheaderview_p_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickHorizontalHeaderViewPrivate to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..occult import Rituals
from . import QQuickHeaderViewBasePrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QQuickHorizontalHeaderView


class QQuickHorizontalHeaderViewPrivate(QQuickHeaderViewBasePrivate):
  """
  The cute side of Qt's QQuickHorizontalHeaderViewPrivate: a plain Python
  object standing in front of one C++ QQuickHorizontalHeaderViewPrivate.

  It is built on the cute 'QQuickHeaderViewBasePrivate', as Qt's
  QQuickHorizontalHeaderViewPrivate is built on Qt's
  QQuickHeaderViewBasePrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickHorizontalHeaderViewPrivate that has a ritual
  and that Python can call so far, 1 name in all: 'q_func'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QQuickHorizontalHeaderView
    *QQuickHorizontalHeaderViewPrivate::q_func() const': takes in Python what
    'QQuickHorizontalHeaderView *QQuickHorizontalHeaderViewPrivate::q_func()'
    takes.
  - Qt's
    'QQuickHorizontalHeaderViewPrivate::~QQuickHorizontalHeaderViewPrivate(
    )': the destructor: Python never removes a C++
    QQuickHorizontalHeaderViewPrivate.

  What to expect
  --------------

  - The C++ QQuickHorizontalHeaderViewPrivate is created at the first use,
    not by 'QQuickHorizontalHeaderViewPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickHorizontalHeaderViewPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickHorizontalHeaderViewPrivate'

  #  A C++ QQuickHorizontalHeaderViewPrivate Python makes is of a C++ class
  #  of ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickHorizontalHeaderViewPrivate'

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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QQuickHorizontalHeaderViewPrivate::QQuickHorizontalHeaderViewPrivate()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickhorizontalheaderviewprivate.html
    """
    #  QQuickHorizontalHeaderViewPrivate::QQuickHorizontalHeaderViewPrivate()
    self._noteCreation(
        QQuickHorizontalHeaderViewPrivate, lambda: Rituals.call(
            'ritual_ZN33QQuickHorizontalHeaderViewPrivateC1Ev',
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

  def q_func(self) -> Optional[QQuickHorizontalHeaderView]:
    """
    Calls Qt's 'QQuickHorizontalHeaderView
    *QQuickHorizontalHeaderViewPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickhorizontalheaderviewprivate.html#q_func

    Returns
    -------

    Optional[QQuickHorizontalHeaderView]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickHorizontalHeaderView
    #      *QQuickHorizontalHeaderViewPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN33QQuickHorizontalHeaderViewPrivate6q_funcEv',
    )
    from . import QQuickHorizontalHeaderView
    return QQuickHorizontalHeaderView._cuteAt(address)
