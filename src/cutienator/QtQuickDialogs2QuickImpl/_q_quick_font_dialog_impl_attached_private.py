"""
QQuickFontDialogImplAttachedPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickDialogs2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qquickfontdialogimpl_p_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickFontDialogImplAttachedPrivate to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtCore import QObjectPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtGui import QFont
  from . import QQuickFontDialogImplAttached
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QFont = WAIT['QFont']


class QQuickFontDialogImplAttachedPrivate(QObjectPrivate):
  """
  The cute side of Qt's QQuickFontDialogImplAttachedPrivate: a plain Python
  object standing in front of one C++ QQuickFontDialogImplAttachedPrivate.

  It is built on the cute 'QObjectPrivate', as Qt's
  QQuickFontDialogImplAttachedPrivate is built on Qt's QObjectPrivate, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickFontDialogImplAttachedPrivate that has a
  ritual and that Python can call so far, 2 names in all:
  'currentFontChanged', 'q_func'. None can be made from Python: one comes out
  of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QQuickFontDialogImplAttached
    *QQuickFontDialogImplAttachedPrivate::q_func() const': takes in Python
    what 'QQuickFontDialogImplAttached
    *QQuickFontDialogImplAttachedPrivate::q_func()' takes.

  What to expect
  --------------

  - The C++ QQuickFontDialogImplAttachedPrivate is created at the first use,
    not by 'QQuickFontDialogImplAttachedPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickFontDialogImplAttachedPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickFontDialogImplAttachedPrivate'

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

  @overload(QFont)
  def currentFontChanged(self, font: QFont) -> None:
    """
    Calls Qt's 'void
    QQuickFontDialogImplAttachedPrivate::currentFontChanged(const QFont
    &font)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfontdialogimplattachedprivate.html

    Parameters
    ----------

    font : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.
    """
    #  void QQuickFontDialogImplAttachedPrivate::currentFontChanged(const
    #      QFont &font)
    self.uglySide.call(
        'ritual_ZN35QQuickFontDialogImplAttachedPrivate18currentFontChanged'
        'ERK5QFont',
        self._valueOf(font),
    )

  def q_func(self) -> Optional[QQuickFontDialogImplAttached]:
    """
    Calls Qt's 'QQuickFontDialogImplAttached
    *QQuickFontDialogImplAttachedPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfontdialogimplattachedprivate.html#q_func

    Returns
    -------

    Optional[QQuickFontDialogImplAttached]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickFontDialogImplAttached
    #      *QQuickFontDialogImplAttachedPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN35QQuickFontDialogImplAttachedPrivate6q_funcEv',
    )
    from . import QQuickFontDialogImplAttached
    return QQuickFontDialogImplAttached._cuteAt(address)
