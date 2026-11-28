"""
QQuickDialogPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickdialog_p_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQuickDialogPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtGui import QPlatformDialogHelper
from . import QQuickPopupPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QQuickAbstractButton, QQuickDialog
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickAbstractButton = WAIT['QQuickAbstractButton']
  QQuickDialog = WAIT['QQuickDialog']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickDialogPrivate(QQuickPopupPrivate):
  """
  The cute side of Qt's QQuickDialogPrivate: a plain Python object standing
  in front of one C++ QQuickDialogPrivate.

  It is built on the cute 'QQuickPopupPrivate', as Qt's QQuickDialogPrivate
  is built on Qt's QQuickPopupPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickDialogPrivate that has a ritual and that
  Python can call so far, 6 names in all: 'q_func', 'get', 'buttonRole',
  'handleAccept', 'handleReject', 'handleClick'. It can be made from Python,
  in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QQuickDialog *QQuickDialogPrivate::q_func() const': takes in
    Python what 'QQuickDialog *QQuickDialogPrivate::q_func()' takes.

  What to expect
  --------------

  - The C++ QQuickDialogPrivate is created at the first use, not by
    'QQuickDialogPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickDialogPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QQuickDialog)
  @overload(NoneType)
  def get(dialog: Optional[QQuickDialog]) -> Optional[QQuickDialogPrivate]:
    """
    Calls Qt's 'QQuickDialogPrivate *QQuickDialogPrivate::get(QQuickDialog
    *dialog)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdialogprivate.html#get

    Parameters
    ----------

    dialog : Optional[QQuickDialog]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQuickDialogPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickDialogPrivate *QQuickDialogPrivate::get(QQuickDialog *dialog)
    address = Rituals.call(
        'ritual_ZN19QQuickDialogPrivate3getEP12QQuickDialog',
        CuteMixin._addressOf(dialog),
    )
    return QQuickDialogPrivate._cuteAt(address)

  @staticmethod
  @overload(QQuickAbstractButton)
  @overload(NoneType)
  def buttonRole(
      button: Optional[QQuickAbstractButton],
  ) -> QPlatformDialogHelper.ButtonRole:
    """
    Calls Qt's 'QPlatformDialogHelper::ButtonRole
    QQuickDialogPrivate::buttonRole(QQuickAbstractButton *button)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdialogprivate.html#buttonRole

    Parameters
    ----------

    button : Optional[QQuickAbstractButton]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QPlatformDialogHelper.ButtonRole
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QPlatformDialogHelper.ButtonRole(number)' gives.
    """
    #  QPlatformDialogHelper::ButtonRole
    #      QQuickDialogPrivate::buttonRole(QQuickAbstractButton *button)
    return QPlatformDialogHelper.ButtonRole(Rituals.call(
        'ritual_ZN19QQuickDialogPrivate10buttonRoleEP20QQuickAbstractButton',
        CuteMixin._addressOf(button),
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickDialogPrivate'

  #  A C++ QQuickDialogPrivate Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickDialogPrivate'

  #  The functions Qt calls itself that QQuickDialogPrivate is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'handleAccept': (
          ('_ZN19QQuickDialogPrivate12handleAcceptEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'handleReject': (
          ('_ZN19QQuickDialogPrivate12handleRejectEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'handleClick': (
          ('_ZN19QQuickDialogPrivate11handleClickEP20QQuickAbstractButton',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address',
                'QtQuickTemplates2:QQuickAbstractButton'),
           )),
      ),
  }

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
    'QQuickDialogPrivate::QQuickDialogPrivate()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdialogprivate.html#QQuickDialogPrivate
    """
    #  QQuickDialogPrivate::QQuickDialogPrivate()
    self._noteCreation(QQuickDialogPrivate, lambda: Rituals.call(
        'ritual_ZN19QQuickDialogPrivateC1Ev',
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

  def q_func(self) -> Optional[QQuickDialog]:
    """
    Calls Qt's 'QQuickDialog *QQuickDialogPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdialogprivate.html#q_func

    Returns
    -------

    Optional[QQuickDialog]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickDialog *QQuickDialogPrivate::q_func()
    address = self.uglySide.call('ritual_ZN19QQuickDialogPrivate6q_funcEv')
    from . import QQuickDialog
    return QQuickDialog._cuteAt(address)

  def handleAccept(self) -> None:
    """
    Calls Qt's 'void QQuickDialogPrivate::handleAccept()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdialogprivate.html#handleAccept
    """
    #  void QQuickDialogPrivate::handleAccept()
    ritual = 'ritual_ZN19QQuickDialogPrivate12handleAcceptEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQuickDialogPrivate12handleAcceptEv'
    self.uglySide.call(ritual)

  def handleReject(self) -> None:
    """
    Calls Qt's 'void QQuickDialogPrivate::handleReject()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdialogprivate.html#handleReject
    """
    #  void QQuickDialogPrivate::handleReject()
    ritual = 'ritual_ZN19QQuickDialogPrivate12handleRejectEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQuickDialogPrivate12handleRejectEv'
    self.uglySide.call(ritual)

  @overload(QQuickAbstractButton)
  @overload(NoneType)
  def handleClick(self, button: Optional[QQuickAbstractButton]) -> None:
    """
    Calls Qt's 'void QQuickDialogPrivate::handleClick(QQuickAbstractButton
    *button)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdialogprivate.html#handleClick

    Parameters
    ----------

    button : Optional[QQuickAbstractButton]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickDialogPrivate::handleClick(QQuickAbstractButton *button)
    ritual = (
        'ritual_ZN19QQuickDialogPrivate11handleClickEP20QQuickAbstractButto'
        'n')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQuickDialogPrivate11handleClickEP20QQuickAbstrac'
          'tButton')
    self.uglySide.call(ritual, self._addressOf(button))
