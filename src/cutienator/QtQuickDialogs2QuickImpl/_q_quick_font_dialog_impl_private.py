"""
QQuickFontDialogImplPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickDialogs2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qquickfontdialogimpl_p_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickFontDialogImplPrivate to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QQuickFontDialogImpl
  from ..QtQuickTemplates2 import QQuickAbstractButton
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickAbstractButton = WAIT['QQuickAbstractButton']
  QQuickFontDialogImpl = WAIT['QQuickFontDialogImpl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickFontDialogImplPrivate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuickFontDialogImplPrivate: a plain Python object
  standing in front of one C++ QQuickFontDialogImplPrivate.

  What exists
  -----------

  Every function of Qt's QQuickFontDialogImplPrivate that has a ritual and
  that Python can call so far, 4 names in all: 'q_func', 'get',
  'handleAccept', 'handleClick'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QQuickFontDialogImpl *QQuickFontDialogImplPrivate::q_func()
    const': takes in Python what 'QQuickFontDialogImpl
    *QQuickFontDialogImplPrivate::q_func()' takes.

  What has no ritual
  ------------------

  2 of the 8 functions Qt declares: 1 cannot be called and cannot be called
  through the meta-object and cannot be copied; 1 Qt's library has no name
  for it, and its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QQuickFontDialogImplPrivate is created at the first use, not by
    'QQuickFontDialogImplPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickFontDialogImplPrivate.
  - Each name of Qt's QQuickFontDialogImplPrivate that has no cute function
    yet, 'attachedOrWarn', 'updateEnabled', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QQuickFontDialogImpl)
  @overload(NoneType)
  def get(
      dialog: Optional[QQuickFontDialogImpl],
  ) -> Optional[QQuickFontDialogImplPrivate]:
    """
    Calls Qt's 'QQuickFontDialogImplPrivate
    *QQuickFontDialogImplPrivate::get(QQuickFontDialogImpl *dialog)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfontdialogimplprivate.html#get

    Parameters
    ----------

    dialog : Optional[QQuickFontDialogImpl]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQuickFontDialogImplPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickFontDialogImplPrivate
    #      *QQuickFontDialogImplPrivate::get(QQuickFontDialogImpl *dialog)
    address = Rituals.call(
        'ritual_ZN27QQuickFontDialogImplPrivate3getEP20QQuickFontDialogImpl',
        CuteMixin._addressOf(dialog),
    )
    return QQuickFontDialogImplPrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickFontDialogImplPrivate'

  #  A C++ QQuickFontDialogImplPrivate Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickFontDialogImplPrivate'

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
    'QQuickFontDialogImplPrivate::QQuickFontDialogImplPrivate()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfontdialogimplprivate.html
    """
    #  QQuickFontDialogImplPrivate::QQuickFontDialogImplPrivate()
    self._noteCreation(QQuickFontDialogImplPrivate, lambda: Rituals.call(
        'ritual_ZN27QQuickFontDialogImplPrivateC1Ev',
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

  def q_func(self) -> Optional[QQuickFontDialogImpl]:
    """
    Calls Qt's 'QQuickFontDialogImpl *QQuickFontDialogImplPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfontdialogimplprivate.html#q_func

    Returns
    -------

    Optional[QQuickFontDialogImpl]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickFontDialogImpl *QQuickFontDialogImplPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN27QQuickFontDialogImplPrivate6q_funcEv',
    )
    from . import QQuickFontDialogImpl
    return QQuickFontDialogImpl._cuteAt(address)

  def handleAccept(self) -> None:
    """
    Calls Qt's 'void QQuickFontDialogImplPrivate::handleAccept()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfontdialogimplprivate.html#handleAccept
    """
    #  void QQuickFontDialogImplPrivate::handleAccept()
    ritual = 'ritual_ZN27QQuickFontDialogImplPrivate12handleAcceptEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN27QQuickFontDialogImplPrivate12handleAcceptEv'
    self.uglySide.call(ritual)

  @overload(QQuickAbstractButton)
  @overload(NoneType)
  def handleClick(self, button: Optional[QQuickAbstractButton]) -> None:
    """
    Calls Qt's 'void
    QQuickFontDialogImplPrivate::handleClick(QQuickAbstractButton *button)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfontdialogimplprivate.html#handleClick

    Parameters
    ----------

    button : Optional[QQuickAbstractButton]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickFontDialogImplPrivate::handleClick(QQuickAbstractButton
    #      *button)
    ritual = (
        'ritual_ZN27QQuickFontDialogImplPrivate11handleClickEP20QQuickAbstr'
        'actButton')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN27QQuickFontDialogImplPrivate11handleClickEP20QQuic'
          'kAbstractButton')
    self.uglySide.call(ritual, self._addressOf(button))

  @staticmethod
  def attachedOrWarn(*__, **_) -> Never:
    """
    Qt's 'QQuickFontDialogImplAttached
    *QQuickFontDialogImplPrivate::attachedOrWarn()': Qt's library has no name
    for it, and its code in Qt's source does not compile apart from its file:
    use of undeclared identifier 'lcAttachedProperty'.
    """
    raise NotImplementedError(
        "'QQuickFontDialogImplPrivate.attachedOrWarn' has no cute function "
        "yet. Qt's 'QQuickFontDialogImplAttached "
        "*QQuickFontDialogImplPrivate::attachedOrWarn()': Qt's library has "
        "no name for it, and its code in Qt's source does not compile apart "
        "from its file: use of undeclared identifier 'lcAttachedProperty'.")

  @staticmethod
  def updateEnabled(*__, **_) -> Never:
    """
    Qt's 'void QQuickFontDialogImplPrivate::updateEnabled()': cannot be
    called and cannot be called through the meta-object and cannot be copied:
    no header file has its code, Qt's source does not mark it or its class
    for use from outside Qt or writes it 'inline' or nowhere, and it is no
    signal, slot or invokable function giving back nothing, of a class built
    on QObject, and Qt's source has no code for it that could be told from
    the rest.
    """
    raise NotImplementedError(
        "'QQuickFontDialogImplPrivate.updateEnabled' has no cute function "
        "yet. Qt's 'void QQuickFontDialogImplPrivate::updateEnabled()': "
        "cannot be called and cannot be called through the meta-object and "
        "cannot be copied: no header file has its code, Qt's source does "
        "not mark it or its class for use from outside Qt or writes it "
        "'inline' or nowhere, and it is no signal, slot or invokable "
        "function giving back nothing, of a class built on QObject, and "
        "Qt's source has no code for it that could be told from the rest.")
