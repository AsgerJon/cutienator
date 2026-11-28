"""
QQuickColorDialogImplPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickDialogs2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qquickcolordialogimpl_p_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickColorDialogImplPrivate to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QQuickEyeDropperEventFilter

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QPoint
  from . import QQuickColorDialogImpl, QQuickColorDialogImplAttached
  from ..QtQuickTemplates2 import QQuickAbstractButton
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPoint = WAIT['QPoint']
  QQuickAbstractButton = WAIT['QQuickAbstractButton']
  QQuickColorDialogImpl = WAIT['QQuickColorDialogImpl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickColorDialogImplPrivate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuickColorDialogImplPrivate: a plain Python object
  standing in front of one C++ QQuickColorDialogImplPrivate.

  What exists
  -----------

  Every function of Qt's QQuickColorDialogImplPrivate that has a ritual and
  that Python can call so far, 7 names in all: 'q_func', 'get',
  'attachedOrWarn', 'handleClick', 'eyeDropperEnter', 'eyeDropperLeave',
  'alphaSliderMoved'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QQuickColorDialogImpl *QQuickColorDialogImplPrivate::q_func()
    const': takes in Python what 'QQuickColorDialogImpl
    *QQuickColorDialogImplPrivate::q_func()' takes.
  - Qt's 'QQuickColorDialogImplPrivate::~QQuickColorDialogImplPrivate()': the
    destructor: Python never removes a C++ QQuickColorDialogImplPrivate.

  What has no ritual
  ------------------

  1 of the 11 functions Qt declares: 1 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QQuickColorDialogImplPrivate is created at the first use, not by
    'QQuickColorDialogImplPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickColorDialogImplPrivate.
  - Each name of Qt's QQuickColorDialogImplPrivate that has no cute function
    yet, 'eyeDropperPointerMoved', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QQuickColorDialogImpl)
  @overload(NoneType)
  def get(
      dialog: Optional[QQuickColorDialogImpl],
  ) -> Optional[QQuickColorDialogImplPrivate]:
    """
    Calls Qt's 'QQuickColorDialogImplPrivate
    *QQuickColorDialogImplPrivate::get(QQuickColorDialogImpl *dialog)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcolordialogimplprivate.html#get

    Parameters
    ----------

    dialog : Optional[QQuickColorDialogImpl]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQuickColorDialogImplPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickColorDialogImplPrivate
    #      *QQuickColorDialogImplPrivate::get(QQuickColorDialogImpl *dialog)
    address = Rituals.call(
        'ritual_ZN28QQuickColorDialogImplPrivate3getEP21QQuickColorDialogIm'
        'pl',
        CuteMixin._addressOf(dialog),
    )
    return QQuickColorDialogImplPrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickColorDialogImplPrivate'

  #  A C++ QQuickColorDialogImplPrivate Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickColorDialogImplPrivate'

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
    'QQuickColorDialogImplPrivate::QQuickColorDialogImplPrivate()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcolordialogimplprivate.html
    """
    #  QQuickColorDialogImplPrivate::QQuickColorDialogImplPrivate()
    self._noteCreation(QQuickColorDialogImplPrivate, lambda: Rituals.call(
        'ritual_ZN28QQuickColorDialogImplPrivateC1Ev',
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

  def q_func(self) -> Optional[QQuickColorDialogImpl]:
    """
    Calls Qt's 'QQuickColorDialogImpl
    *QQuickColorDialogImplPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcolordialogimplprivate.html#q_func

    Returns
    -------

    Optional[QQuickColorDialogImpl]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickColorDialogImpl *QQuickColorDialogImplPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN28QQuickColorDialogImplPrivate6q_funcEv',
    )
    from . import QQuickColorDialogImpl
    return QQuickColorDialogImpl._cuteAt(address)

  def attachedOrWarn(self) -> Optional[QQuickColorDialogImplAttached]:
    """
    Calls Qt's 'QQuickColorDialogImplAttached
    *QQuickColorDialogImplPrivate::attachedOrWarn()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcolordialogimplprivate.html#attachedOrWarn

    Returns
    -------

    Optional[QQuickColorDialogImplAttached]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickColorDialogImplAttached
    #      *QQuickColorDialogImplPrivate::attachedOrWarn()
    address = self.uglySide.call(
        'ritual_ZN28QQuickColorDialogImplPrivate14attachedOrWarnEv',
    )
    from . import QQuickColorDialogImplAttached
    return QQuickColorDialogImplAttached._cuteAt(address)

  @overload(QQuickAbstractButton)
  @overload(NoneType)
  def handleClick(self, button: Optional[QQuickAbstractButton]) -> None:
    """
    Calls Qt's 'void
    QQuickColorDialogImplPrivate::handleClick(QQuickAbstractButton *button)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcolordialogimplprivate.html#handleClick

    Parameters
    ----------

    button : Optional[QQuickAbstractButton]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickColorDialogImplPrivate::handleClick(QQuickAbstractButton
    #      *button)
    ritual = (
        'ritual_ZN28QQuickColorDialogImplPrivate11handleClickEP20QQuickAbst'
        'ractButton')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN28QQuickColorDialogImplPrivate11handleClickEP20QQui'
          'ckAbstractButton')
    self.uglySide.call(ritual, self._addressOf(button))

  def eyeDropperEnter(self) -> None:
    """
    Calls Qt's 'void QQuickColorDialogImplPrivate::eyeDropperEnter()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcolordialogimplprivate.html#eyeDropperEnter
    """
    #  void QQuickColorDialogImplPrivate::eyeDropperEnter()
    self.uglySide.call(
        'ritual_ZN28QQuickColorDialogImplPrivate15eyeDropperEnterEv',
    )

  @overload(QPoint, QQuickEyeDropperEventFilter.LeaveReason)
  def eyeDropperLeave(
      self,
      pos: QPoint,
      actionOnLeave: QQuickEyeDropperEventFilter.LeaveReason,
  ) -> None:
    """
    Calls Qt's 'void QQuickColorDialogImplPrivate::eyeDropperLeave(const
    QPoint &pos, QQuickEyeDropperEventFilter::LeaveReason actionOnLeave)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcolordialogimplprivate.html#eyeDropperLeave

    Parameters
    ----------

    pos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    actionOnLeave : QQuickEyeDropperEventFilter.LeaveReason
      Passed on as its number.
    """
    #  void QQuickColorDialogImplPrivate::eyeDropperLeave(const QPoint &pos,
    #      QQuickEyeDropperEventFilter::LeaveReason actionOnLeave)
    self.uglySide.call(
        'ritual_ZN28QQuickColorDialogImplPrivate15eyeDropperLeaveERK6QPoint'
        'N27QQuickEyeDropperEventFilter11LeaveReasonE',
        self._valueOf(pos), actionOnLeave.value,
    )

  def alphaSliderMoved(self) -> None:
    """
    Calls Qt's 'void QQuickColorDialogImplPrivate::alphaSliderMoved()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcolordialogimplprivate.html#alphaSliderMoved
    """
    #  void QQuickColorDialogImplPrivate::alphaSliderMoved()
    self.uglySide.call(
        'ritual_ZN28QQuickColorDialogImplPrivate16alphaSliderMovedEv',
    )

  @staticmethod
  def eyeDropperPointerMoved(*__, **_) -> Never:
    """
    Qt's 'void QQuickColorDialogImplPrivate::eyeDropperPointerMoved(const
    QPoint &pos)': Qt's library has no name for it, and its code in Qt's
    source does not compile apart from its file: use of undeclared identifier
    'grabScreenColor'.
    """
    raise NotImplementedError(
        "'QQuickColorDialogImplPrivate.eyeDropperPointerMoved' has no cute "
        "function yet. Qt's 'void "
        "QQuickColorDialogImplPrivate::eyeDropperPointerMoved(const QPoint "
        "&pos)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'grabScreenColor'.")
