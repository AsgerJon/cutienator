"""
QQuickFolderDialogImplPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickDialogs2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qquickfolderdialogimpl_p_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickFolderDialogImplPrivate to be private: it declares the
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

  from . import QQuickFolderDialogImpl, QQuickFolderDialogImplAttached
  from ..QtQuickTemplates2 import QQuickAbstractButton
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickAbstractButton = WAIT['QQuickAbstractButton']
  QQuickFolderDialogImpl = WAIT['QQuickFolderDialogImpl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickFolderDialogImplPrivate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuickFolderDialogImplPrivate: a plain Python object
  standing in front of one C++ QQuickFolderDialogImplPrivate.

  What exists
  -----------

  Every function of Qt's QQuickFolderDialogImplPrivate that has a ritual and
  that Python can call so far, 7 names in all: 'q_func', 'get',
  'attachedOrWarn', 'updateEnabled', 'updateSelectedFolder', 'handleAccept',
  'handleClick'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QQuickFolderDialogImpl
    *QQuickFolderDialogImplPrivate::q_func() const': takes in Python what
    'QQuickFolderDialogImpl *QQuickFolderDialogImplPrivate::q_func()' takes.

  What to expect
  --------------

  - The C++ QQuickFolderDialogImplPrivate is created at the first use, not by
    'QQuickFolderDialogImplPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickFolderDialogImplPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QQuickFolderDialogImpl)
  @overload(NoneType)
  def get(
      dialog: Optional[QQuickFolderDialogImpl],
  ) -> Optional[QQuickFolderDialogImplPrivate]:
    """
    Calls Qt's 'QQuickFolderDialogImplPrivate
    *QQuickFolderDialogImplPrivate::get(QQuickFolderDialogImpl *dialog)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderdialogimplprivate.html#get

    Parameters
    ----------

    dialog : Optional[QQuickFolderDialogImpl]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQuickFolderDialogImplPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickFolderDialogImplPrivate
    #      *QQuickFolderDialogImplPrivate::get(QQuickFolderDialogImpl
    #      *dialog)
    address = Rituals.call(
        'ritual_ZN29QQuickFolderDialogImplPrivate3getEP22QQuickFolderDialog'
        'Impl',
        CuteMixin._addressOf(dialog),
    )
    return QQuickFolderDialogImplPrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickFolderDialogImplPrivate'

  #  A C++ QQuickFolderDialogImplPrivate Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickFolderDialogImplPrivate'

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
    'QQuickFolderDialogImplPrivate::QQuickFolderDialogImplPrivate()', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderdialogimplprivate.html
    """
    #  QQuickFolderDialogImplPrivate::QQuickFolderDialogImplPrivate()
    self._noteCreation(QQuickFolderDialogImplPrivate, lambda: Rituals.call(
        'ritual_ZN29QQuickFolderDialogImplPrivateC1Ev',
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

  def q_func(self) -> Optional[QQuickFolderDialogImpl]:
    """
    Calls Qt's 'QQuickFolderDialogImpl
    *QQuickFolderDialogImplPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderdialogimplprivate.html#q_func

    Returns
    -------

    Optional[QQuickFolderDialogImpl]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickFolderDialogImpl *QQuickFolderDialogImplPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN29QQuickFolderDialogImplPrivate6q_funcEv',
    )
    from . import QQuickFolderDialogImpl
    return QQuickFolderDialogImpl._cuteAt(address)

  def attachedOrWarn(self) -> Optional[QQuickFolderDialogImplAttached]:
    """
    Calls Qt's 'QQuickFolderDialogImplAttached
    *QQuickFolderDialogImplPrivate::attachedOrWarn()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderdialogimplprivate.html#attachedOrWarn

    Returns
    -------

    Optional[QQuickFolderDialogImplAttached]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickFolderDialogImplAttached
    #      *QQuickFolderDialogImplPrivate::attachedOrWarn()
    address = self.uglySide.call(
        'ritual_ZN29QQuickFolderDialogImplPrivate14attachedOrWarnEv',
    )
    from . import QQuickFolderDialogImplAttached
    return QQuickFolderDialogImplAttached._cuteAt(address)

  def updateEnabled(self) -> None:
    """
    Calls Qt's 'void QQuickFolderDialogImplPrivate::updateEnabled()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderdialogimplprivate.html#updateEnabled
    """
    #  void QQuickFolderDialogImplPrivate::updateEnabled()
    self.uglySide.call(
        'ritual_ZN29QQuickFolderDialogImplPrivate13updateEnabledEv',
    )

  @overload(str)
  def updateSelectedFolder(self, oldFolderPath: str) -> None:
    """
    Calls Qt's 'void
    QQuickFolderDialogImplPrivate::updateSelectedFolder(const QString
    &oldFolderPath)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderdialogimplprivate.html

    Parameters
    ----------

    oldFolderPath : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickFolderDialogImplPrivate::updateSelectedFolder(const QString
    #      &oldFolderPath)
    self.uglySide.call(
        'ritual_ZN29QQuickFolderDialogImplPrivate20updateSelectedFolderERK7'
        'QString',
        oldFolderPath,
    )

  def handleAccept(self) -> None:
    """
    Calls Qt's 'void QQuickFolderDialogImplPrivate::handleAccept()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderdialogimplprivate.html#handleAccept
    """
    #  void QQuickFolderDialogImplPrivate::handleAccept()
    ritual = 'ritual_ZN29QQuickFolderDialogImplPrivate12handleAcceptEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN29QQuickFolderDialogImplPrivate12handleAcceptEv'
    self.uglySide.call(ritual)

  @overload(QQuickAbstractButton)
  @overload(NoneType)
  def handleClick(self, button: Optional[QQuickAbstractButton]) -> None:
    """
    Calls Qt's 'void
    QQuickFolderDialogImplPrivate::handleClick(QQuickAbstractButton
    *button)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderdialogimplprivate.html#handleClick

    Parameters
    ----------

    button : Optional[QQuickAbstractButton]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickFolderDialogImplPrivate::handleClick(QQuickAbstractButton
    #      *button)
    ritual = (
        'ritual_ZN29QQuickFolderDialogImplPrivate11handleClickEP20QQuickAbs'
        'tractButton')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN29QQuickFolderDialogImplPrivate11handleClickEP20QQu'
          'ickAbstractButton')
    self.uglySide.call(ritual, self._addressOf(button))
