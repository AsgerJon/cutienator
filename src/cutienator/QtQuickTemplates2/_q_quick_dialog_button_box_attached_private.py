"""
QQuickDialogButtonBoxAttachedPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickdialogbuttonbox_p_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickDialogButtonBoxAttachedPrivate to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObjectPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QQuickDialogButtonBox, QQuickDialogButtonBoxAttached
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickDialogButtonBox = WAIT['QQuickDialogButtonBox']
  QQuickDialogButtonBoxAttached = WAIT['QQuickDialogButtonBoxAttached']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickDialogButtonBoxAttachedPrivate(QObjectPrivate):
  """
  The cute side of Qt's QQuickDialogButtonBoxAttachedPrivate: a plain Python
  object standing in front of one C++ QQuickDialogButtonBoxAttachedPrivate.

  It is built on the cute 'QObjectPrivate', as Qt's
  QQuickDialogButtonBoxAttachedPrivate is built on Qt's QObjectPrivate, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickDialogButtonBoxAttachedPrivate that has a
  ritual and that Python can call so far, 3 names in all: 'q_func', 'get',
  'setButtonBox'. None can be made from Python: one comes out of a function
  of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QQuickDialogButtonBoxAttached
    *QQuickDialogButtonBoxAttachedPrivate::q_func() const': takes in Python
    what 'QQuickDialogButtonBoxAttached
    *QQuickDialogButtonBoxAttachedPrivate::q_func()' takes.

  What to expect
  --------------

  - The C++ QQuickDialogButtonBoxAttachedPrivate is created at the first use,
    not by 'QQuickDialogButtonBoxAttachedPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickDialogButtonBoxAttachedPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QQuickDialogButtonBoxAttached)
  @overload(NoneType)
  def get(
      q: Optional[QQuickDialogButtonBoxAttached],
  ) -> Optional[QQuickDialogButtonBoxAttachedPrivate]:
    """
    Calls Qt's 'QQuickDialogButtonBoxAttachedPrivate
    *QQuickDialogButtonBoxAttachedPrivate::get(QQuickDialogButtonBoxAttached
    *q)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdialogbuttonboxattachedprivate.html#get

    Parameters
    ----------

    q : Optional[QQuickDialogButtonBoxAttached]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQuickDialogButtonBoxAttachedPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickDialogButtonBoxAttachedPrivate
    #      *QQuickDialogButtonBoxAttachedPrivate::get(
    #      QQuickDialogButtonBoxAttached *q)
    address = Rituals.call(
        'ritual_ZN36QQuickDialogButtonBoxAttachedPrivate3getEP29QQuickDialo'
        'gButtonBoxAttached',
        CuteMixin._addressOf(q),
    )
    return QQuickDialogButtonBoxAttachedPrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickDialogButtonBoxAttachedPrivate'

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

  @overload(QQuickDialogButtonBox)
  @overload(NoneType)
  def setButtonBox(self, box: Optional[QQuickDialogButtonBox]) -> None:
    """
    Calls Qt's 'void
    QQuickDialogButtonBoxAttachedPrivate::setButtonBox(QQuickDialogButtonBox
    *box)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdialogbuttonboxattachedprivate.html

    Parameters
    ----------

    box : Optional[QQuickDialogButtonBox]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickDialogButtonBoxAttachedPrivate::setButtonBox(
    #      QQuickDialogButtonBox *box)
    self.uglySide.call(
        'ritual_ZN36QQuickDialogButtonBoxAttachedPrivate12setButtonBoxEP21Q'
        'QuickDialogButtonBox',
        self._addressOf(box),
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

  def q_func(self) -> Optional[QQuickDialogButtonBoxAttached]:
    """
    Calls Qt's 'QQuickDialogButtonBoxAttached
    *QQuickDialogButtonBoxAttachedPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdialogbuttonboxattachedprivate.html#q_func

    Returns
    -------

    Optional[QQuickDialogButtonBoxAttached]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickDialogButtonBoxAttached
    #      *QQuickDialogButtonBoxAttachedPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN36QQuickDialogButtonBoxAttachedPrivate6q_funcEv',
    )
    from . import QQuickDialogButtonBoxAttached
    return QQuickDialogButtonBoxAttached._cuteAt(address)
