"""
QQuickMessageDialogImplPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickDialogs2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qquickmessagedialogimpl_p_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickMessageDialogImplPrivate to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QQuickMessageDialogImpl, QQuickMessageDialogImplAttached
  from ..QtQuickTemplates2 import QQuickAbstractButton
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickAbstractButton = WAIT['QQuickAbstractButton']
  QQuickMessageDialogImpl = WAIT['QQuickMessageDialogImpl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickMessageDialogImplPrivate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuickMessageDialogImplPrivate: a plain Python object
  standing in front of one C++ QQuickMessageDialogImplPrivate.

  What exists
  -----------

  Every function of Qt's QQuickMessageDialogImplPrivate that has a ritual and
  that Python can call so far, 4 names in all: 'q_func', 'get',
  'attachedOrWarn', 'handleClick'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QQuickMessageDialogImpl
    *QQuickMessageDialogImplPrivate::q_func() const': takes in Python what
    'QQuickMessageDialogImpl *QQuickMessageDialogImplPrivate::q_func()'
    takes.

  What to expect
  --------------

  - The C++ QQuickMessageDialogImplPrivate is created at the first use, not
    by 'QQuickMessageDialogImplPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickMessageDialogImplPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QQuickMessageDialogImpl)
  @overload(NoneType)
  def get(
      dialog: Optional[QQuickMessageDialogImpl],
  ) -> Optional[QQuickMessageDialogImplPrivate]:
    """
    Calls Qt's 'QQuickMessageDialogImplPrivate
    *QQuickMessageDialogImplPrivate::get(QQuickMessageDialogImpl *dialog)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmessagedialogimplprivate.html#get

    Parameters
    ----------

    dialog : Optional[QQuickMessageDialogImpl]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQuickMessageDialogImplPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickMessageDialogImplPrivate
    #      *QQuickMessageDialogImplPrivate::get(QQuickMessageDialogImpl
    #      *dialog)
    address = Rituals.call(
        'ritual_ZN30QQuickMessageDialogImplPrivate3getEP23QQuickMessageDial'
        'ogImpl',
        CuteMixin._addressOf(dialog),
    )
    return QQuickMessageDialogImplPrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickMessageDialogImplPrivate'

  #  A C++ QQuickMessageDialogImplPrivate Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickMessageDialogImplPrivate'

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
    'QQuickMessageDialogImplPrivate::QQuickMessageDialogImplPrivate()', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmessagedialogimplprivate.html
    """
    #  QQuickMessageDialogImplPrivate::QQuickMessageDialogImplPrivate()
    self._noteCreation(QQuickMessageDialogImplPrivate, lambda: Rituals.call(
        'ritual_ZN30QQuickMessageDialogImplPrivateC1Ev',
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

  def q_func(self) -> Optional[QQuickMessageDialogImpl]:
    """
    Calls Qt's 'QQuickMessageDialogImpl
    *QQuickMessageDialogImplPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmessagedialogimplprivate.html#q_func

    Returns
    -------

    Optional[QQuickMessageDialogImpl]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickMessageDialogImpl *QQuickMessageDialogImplPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN30QQuickMessageDialogImplPrivate6q_funcEv',
    )
    from . import QQuickMessageDialogImpl
    return QQuickMessageDialogImpl._cuteAt(address)

  def attachedOrWarn(self) -> Optional[QQuickMessageDialogImplAttached]:
    """
    Calls Qt's 'QQuickMessageDialogImplAttached
    *QQuickMessageDialogImplPrivate::attachedOrWarn()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmessagedialogimplprivate.html#attachedOrWarn

    Returns
    -------

    Optional[QQuickMessageDialogImplAttached]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickMessageDialogImplAttached
    #      *QQuickMessageDialogImplPrivate::attachedOrWarn()
    address = self.uglySide.call(
        'ritual_ZN30QQuickMessageDialogImplPrivate14attachedOrWarnEv',
    )
    from . import QQuickMessageDialogImplAttached
    return QQuickMessageDialogImplAttached._cuteAt(address)

  @overload(QQuickAbstractButton)
  @overload(NoneType)
  def handleClick(self, button: Optional[QQuickAbstractButton]) -> None:
    """
    Calls Qt's 'void
    QQuickMessageDialogImplPrivate::handleClick(QQuickAbstractButton
    *button)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmessagedialogimplprivate.html#handleClick

    Parameters
    ----------

    button : Optional[QQuickAbstractButton]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickMessageDialogImplPrivate::handleClick(QQuickAbstractButton
    #      *button)
    ritual = (
        'ritual_ZN30QQuickMessageDialogImplPrivate11handleClickEP20QQuickAb'
        'stractButton')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN30QQuickMessageDialogImplPrivate11handleClickEP20QQ'
          'uickAbstractButton')
    self.uglySide.call(ritual, self._addressOf(button))
