"""
QtVirtualKeyboard::DesktopInputSelectionControl binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtVirtualKeyboard/6.12.0/QtVirtualKeyboard/private/desktopinputselectioncontrol_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QtVirtualKeyboard::DesktopInputSelectionControl to be private: it
#  declares the class in a header it calls private. cutienator does not care.
#  Qt hands objects of the class out all the same, and a class we are handed
#  is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QEvent, QMetaObject, QRect, QRectF
  from ..QtGui import QImage
  from . import QVirtualKeyboardInputContext
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEvent = WAIT['QEvent']
  QRectF = WAIT['QRectF']
  QVirtualKeyboardInputContext = WAIT['QVirtualKeyboardInputContext']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class DesktopInputSelectionControl(QObject):
  """
  The cute side of Qt's QtVirtualKeyboard::DesktopInputSelectionControl: a
  plain Python object standing in front of one C++
  QtVirtualKeyboard::DesktopInputSelectionControl.

  It is built on the cute 'QObject', as Qt's
  QtVirtualKeyboard::DesktopInputSelectionControl is built on Qt's QObject,
  and has everything that class has.

  What exists
  -----------

  Every function of Qt's QtVirtualKeyboard::DesktopInputSelectionControl that
  has a ritual and that Python can call so far, 14 names in all:
  'metaObject', 'tr', 'createHandles', 'destroyHandles', 'setEnabled',
  'handleImage', 'updateAnchorHandlePosition', 'updateCursorHandlePosition',
  'updateVisibility', 'reloadGraphics', 'eventFilter', 'anchorHandleRect',
  'cursorHandleRect', 'handleRectForCursorRect'. It can be made from Python,
  in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void
    *QtVirtualKeyboard::DesktopInputSelectionControl::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int QtVirtualKeyboard::DesktopInputSelectionControl::qt_metacall(
    QMetaObject::Call a0, int a1, void **a2)': one of Qt's own inner
    workings.
  - Qt's 'QtVirtualKeyboard::DesktopInputSelectionControl::
    ~DesktopInputSelectionControl()': the destructor: Python never removes a
    C++ QtVirtualKeyboard::DesktopInputSelectionControl.

  What has no ritual
  ------------------

  2 of the 20 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QtVirtualKeyboard::DesktopInputSelectionControl is created at the
    first use, not by 'QtVirtualKeyboard::DesktopInputSelectionControl(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++
    QtVirtualKeyboard::DesktopInputSelectionControl.
  - Qt tells when it has removed the C++
    QtVirtualKeyboard::DesktopInputSelectionControl. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  @overload(NoneType)
  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  @overload(str, str, int)
  @overload(str, NoneType, int)
  @overload(NoneType, str, int)
  @overload(NoneType, NoneType, int)
  def tr(s: Optional[str], c: Optional[str] = None, n: int = -1) -> str:
    """
    Calls Qt's 'QString
    QtVirtualKeyboard::DesktopInputSelectionControl::tr(const char *s, const
    char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-desktopinputselectioncontrol.html

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    c : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QtVirtualKeyboard::DesktopInputSelectionControl::tr(const char
    #      *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN17QtVirtualKeyboard28DesktopInputSelectionControl2trEPKcS'
        '2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QtVirtualKeyboard::DesktopInputSelectionControl'

  #  A C++ QtVirtualKeyboard::DesktopInputSelectionControl Python makes is of
  #  a C++ class of ours, in which Python can take functions over. This
  #  ritual hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QtVirtualKeyboard_DesktopInputSelectionControl'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject
    *QtVirtualKeyboard::DesktopInputSelectionControl::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-desktopinputselectioncontrol.html

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject
    #      *QtVirtualKeyboard::DesktopInputSelectionControl::metaObject()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK17QtVirtualKeyboard28DesktopInputSelectionControl10metaO'
        'bjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def anchorHandleRect(self) -> QRect:
    """
    Calls Qt's 'QRect
    QtVirtualKeyboard::DesktopInputSelectionControl::anchorHandleRect()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-desktopinputselectioncontrol.html

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect
    #      QtVirtualKeyboard::DesktopInputSelectionControl::anchorHandleRect(
    #      ) const
    address = self.uglySide.call(
        'ritual_ZNK17QtVirtualKeyboard28DesktopInputSelectionControl16ancho'
        'rHandleRectEv',
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  def cursorHandleRect(self) -> QRect:
    """
    Calls Qt's 'QRect
    QtVirtualKeyboard::DesktopInputSelectionControl::cursorHandleRect()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-desktopinputselectioncontrol.html

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect
    #      QtVirtualKeyboard::DesktopInputSelectionControl::cursorHandleRect(
    #      ) const
    address = self.uglySide.call(
        'ritual_ZNK17QtVirtualKeyboard28DesktopInputSelectionControl16curso'
        'rHandleRectEv',
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  @overload(QRectF)
  def handleRectForCursorRect(self, cursorRect: QRectF) -> QRect:
    """
    Calls Qt's 'QRect
    QtVirtualKeyboard::DesktopInputSelectionControl::handleRectForCursorRect(
    const QRectF &cursorRect) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-desktopinputselectioncontrol.html

    Parameters
    ----------

    cursorRect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QtVirtualKeyboard::DesktopInputSelectionControl::
    #      handleRectForCursorRect(const QRectF &cursorRect) const
    address = self.uglySide.call(
        'ritual_ZNK17QtVirtualKeyboard28DesktopInputSelectionControl23handl'
        'eRectForCursorRectERK6QRectF',
        self._valueOf(cursorRect),
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setEnabled(self, enable: bool) -> None:
    """
    Calls Qt's 'void
    QtVirtualKeyboard::DesktopInputSelectionControl::setEnabled(bool
    enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-desktopinputselectioncontrol.html

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QtVirtualKeyboard::DesktopInputSelectionControl::setEnabled(bool
    #      enable)
    self.uglySide.call(
        'ritual_ZN17QtVirtualKeyboard28DesktopInputSelectionControl10setEna'
        'bledEb',
        enable,
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

  @overload(QObject, QVirtualKeyboardInputContext)
  @overload(QObject, NoneType)
  @overload(NoneType, QVirtualKeyboardInputContext)
  @overload(NoneType, NoneType)
  def __init__(
      self,
      parent: Optional[QObject],
      inputContext: Optional[QVirtualKeyboardInputContext],
  ) -> None:
    """
    Notes what was given, for Qt's
    'QtVirtualKeyboard::DesktopInputSelectionControl::
    DesktopInputSelectionControl(QObject *parent,
    QVirtualKeyboardInputContext *inputContext)', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-desktopinputselectioncontrol.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    inputContext : Optional[QVirtualKeyboardInputContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QtVirtualKeyboard::DesktopInputSelectionControl::
    #      DesktopInputSelectionControl(QObject *parent,
    #      QVirtualKeyboardInputContext *inputContext)
    self._noteCreation(DesktopInputSelectionControl, lambda: Rituals.call(
        'ritual_ZN17QtVirtualKeyboard28DesktopInputSelectionControlC1EP7QOb'
        'jectP28QVirtualKeyboardInputContext',
        self._addressOf(parent, 'QObject'), self._addressOf(inputContext),
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

  def createHandles(self) -> None:
    """
    Calls Qt's 'void
    QtVirtualKeyboard::DesktopInputSelectionControl::createHandles()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-desktopinputselectioncontrol.html
    """
    #  void QtVirtualKeyboard::DesktopInputSelectionControl::createHandles()
    self.uglySide.call(
        'ritual_ZN17QtVirtualKeyboard28DesktopInputSelectionControl13create'
        'HandlesEv',
    )

  def destroyHandles(self) -> None:
    """
    Calls Qt's 'void
    QtVirtualKeyboard::DesktopInputSelectionControl::destroyHandles()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-desktopinputselectioncontrol.html
    """
    #  void QtVirtualKeyboard::DesktopInputSelectionControl::destroyHandles()
    self.uglySide.call(
        'ritual_ZN17QtVirtualKeyboard28DesktopInputSelectionControl14destro'
        'yHandlesEv',
    )

  def handleImage(self) -> Optional[QImage]:
    """
    Calls Qt's 'QImage
    *QtVirtualKeyboard::DesktopInputSelectionControl::handleImage()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-desktopinputselectioncontrol.html

    Returns
    -------

    Optional[QImage]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QImage *QtVirtualKeyboard::DesktopInputSelectionControl::handleImage()
    address = self.uglySide.call(
        'ritual_ZN17QtVirtualKeyboard28DesktopInputSelectionControl11handle'
        'ImageEv',
    )
    from ..QtGui import QImage
    return QImage._cuteAt(address)

  def updateAnchorHandlePosition(self) -> None:
    """
    Calls Qt's 'void QtVirtualKeyboard::DesktopInputSelectionControl::
    updateAnchorHandlePosition()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-desktopinputselectioncontrol.html
    """
    #  void QtVirtualKeyboard::DesktopInputSelectionControl::
    #      updateAnchorHandlePosition()
    self.uglySide.call(
        'ritual_ZN17QtVirtualKeyboard28DesktopInputSelectionControl26update'
        'AnchorHandlePositionEv',
    )

  def updateCursorHandlePosition(self) -> None:
    """
    Calls Qt's 'void QtVirtualKeyboard::DesktopInputSelectionControl::
    updateCursorHandlePosition()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-desktopinputselectioncontrol.html
    """
    #  void QtVirtualKeyboard::DesktopInputSelectionControl::
    #      updateCursorHandlePosition()
    self.uglySide.call(
        'ritual_ZN17QtVirtualKeyboard28DesktopInputSelectionControl26update'
        'CursorHandlePositionEv',
    )

  def updateVisibility(self) -> None:
    """
    Calls Qt's 'void
    QtVirtualKeyboard::DesktopInputSelectionControl::updateVisibility()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-desktopinputselectioncontrol.html
    """
    #  void
    #      QtVirtualKeyboard::DesktopInputSelectionControl::updateVisibility(
    #      )
    self.uglySide.call(
        'ritual_ZN17QtVirtualKeyboard28DesktopInputSelectionControl16update'
        'VisibilityEv',
    )

  def reloadGraphics(self) -> None:
    """
    Calls Qt's 'void
    QtVirtualKeyboard::DesktopInputSelectionControl::reloadGraphics()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-desktopinputselectioncontrol.html
    """
    #  void QtVirtualKeyboard::DesktopInputSelectionControl::reloadGraphics()
    self.uglySide.call(
        'ritual_ZN17QtVirtualKeyboard28DesktopInputSelectionControl14reload'
        'GraphicsEv',
    )

  @overload(QObject, QEvent)
  @overload(QObject, NoneType)
  @overload(NoneType, QEvent)
  @overload(NoneType, NoneType)
  def eventFilter(
      self,
      object: Optional[QObject],
      event: Optional[QEvent],
  ) -> bool:
    """
    Calls Qt's 'bool
    QtVirtualKeyboard::DesktopInputSelectionControl::eventFilter(QObject
    *object, QEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-desktopinputselectioncontrol.html

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QtVirtualKeyboard::DesktopInputSelectionControl::eventFilter(
    #      QObject *object, QEvent *event)
    ritual = (
        'ritual_ZN17QtVirtualKeyboard28DesktopInputSelectionControl11eventF'
        'ilterEP7QObjectP6QEvent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QtVirtualKeyboard28DesktopInputSelectionControl11'
          'eventFilterEP7QObjectP6QEvent')
    return self.uglySide.call(
        ritual, self._addressOf(object, 'QObject'), self._addressOf(event),
    )
