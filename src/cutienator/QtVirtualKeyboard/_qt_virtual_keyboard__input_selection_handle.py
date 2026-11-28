"""
QtVirtualKeyboard::InputSelectionHandle binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtVirtualKeyboard/6.12.0/QtVirtualKeyboard/private/inputselectionhandle_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QtVirtualKeyboard::InputSelectionHandle to be private: it
#  declares the class in a header it calls private. cutienator does not care.
#  Qt hands objects of the class out all the same, and a class we are handed
#  is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtGui import QRasterWindow, QWindow
from . import QtVirtualKeyboard

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QEvent, QMetaObject, QSize
  from ..QtGui import QPaintEvent
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEvent = WAIT['QEvent']
  QPaintEvent = WAIT['QPaintEvent']
  QSize = WAIT['QSize']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class InputSelectionHandle(QRasterWindow):
  """
  The cute side of Qt's QtVirtualKeyboard::InputSelectionHandle: a plain
  Python object standing in front of one C++
  QtVirtualKeyboard::InputSelectionHandle.

  It is built on the cute 'QRasterWindow', as Qt's
  QtVirtualKeyboard::InputSelectionHandle is built on Qt's QRasterWindow, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's QtVirtualKeyboard::InputSelectionHandle that has a
  ritual and that Python can call so far, 5 names in all: 'metaObject', 'tr',
  'applyImage', 'paintEvent', 'event'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QtVirtualKeyboard::InputSelectionHandle::qt_metacast(const
    char *a0)': one of Qt's own inner workings.
  - Qt's 'int
    QtVirtualKeyboard::InputSelectionHandle::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  2 of the 10 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QtVirtualKeyboard::InputSelectionHandle is created at the first
    use, not by 'QtVirtualKeyboard::InputSelectionHandle(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QtVirtualKeyboard::InputSelectionHandle.
  - Qt tells when it has removed the C++
    QtVirtualKeyboard::InputSelectionHandle. Every call on the cute object,
    and every use of it as an argument, then raises 'RuntimeError', and
    nothing reaches C++.
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
    Calls Qt's 'QString QtVirtualKeyboard::InputSelectionHandle::tr(const
    char *s, const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-inputselectionhandle.html#tr

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
    #  QString QtVirtualKeyboard::InputSelectionHandle::tr(const char *s,
    #      const char *c, int n)
    return Rituals.call(
        'ritual_ZN17QtVirtualKeyboard20InputSelectionHandle2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QtVirtualKeyboard::InputSelectionHandle'

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
    *QtVirtualKeyboard::InputSelectionHandle::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-inputselectionhandle.html

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject
    #      *QtVirtualKeyboard::InputSelectionHandle::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK17QtVirtualKeyboard20InputSelectionHandle10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

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

  @overload(WAIT['QtVirtualKeyboard.DesktopInputSelectionControl'], QWindow)
  @overload(WAIT['QtVirtualKeyboard.DesktopInputSelectionControl'], NoneType)
  @overload(NoneType, QWindow)
  @overload(NoneType, NoneType)
  def __init__(
      self,
      control: Optional[QtVirtualKeyboard.DesktopInputSelectionControl],
      eventWindow: Optional[QWindow],
  ) -> None:
    """
    Notes what was given, for Qt's
    'QtVirtualKeyboard::InputSelectionHandle::InputSelectionHandle(
    DesktopInputSelectionControl *control, QWindow *eventWindow)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-inputselectionhandle.html

    Parameters
    ----------

    control : Optional[QtVirtualKeyboard.DesktopInputSelectionControl]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    eventWindow : Optional[QWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QtVirtualKeyboard::InputSelectionHandle::InputSelectionHandle(
    #      DesktopInputSelectionControl *control, QWindow *eventWindow)
    self._noteCreation(InputSelectionHandle, lambda: Rituals.call(
        'ritual_ZN17QtVirtualKeyboard20InputSelectionHandleC1EPNS_28Desktop'
        'InputSelectionControlEP7QWindow',
        self._addressOf(control), self._addressOf(eventWindow),
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

  @overload(QSize)
  def applyImage(self, windowSize: QSize) -> None:
    """
    Calls Qt's 'void
    QtVirtualKeyboard::InputSelectionHandle::applyImage(const QSize
    &windowSize)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-inputselectionhandle.html

    Parameters
    ----------

    windowSize : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void QtVirtualKeyboard::InputSelectionHandle::applyImage(const QSize
    #      &windowSize)
    self.uglySide.call(
        'ritual_ZN17QtVirtualKeyboard20InputSelectionHandle10applyImageERK5'
        'QSize',
        self._valueOf(windowSize),
    )

  @overload(QPaintEvent)
  @overload(NoneType)
  def paintEvent(self, pe: Optional[QPaintEvent]) -> None:
    """
    Calls Qt's 'void
    QtVirtualKeyboard::InputSelectionHandle::paintEvent(QPaintEvent *pe)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-inputselectionhandle.html

    Parameters
    ----------

    pe : Optional[QPaintEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QtVirtualKeyboard::InputSelectionHandle::paintEvent(QPaintEvent
    #      *pe)
    ritual = (
        'ritual_ZN17QtVirtualKeyboard20InputSelectionHandle10paintEventEP11'
        'QPaintEvent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QtVirtualKeyboard20InputSelectionHandle10paintEve'
          'ntEP11QPaintEvent')
    self.uglySide.call(ritual, self._addressOf(pe))

  @overload(QEvent)
  @overload(NoneType)
  def event(self, event: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QtVirtualKeyboard::InputSelectionHandle::event(QEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-inputselectionhandle.html#event

    Parameters
    ----------

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QtVirtualKeyboard::InputSelectionHandle::event(QEvent *event)
    ritual = (
        'ritual_ZN17QtVirtualKeyboard20InputSelectionHandle5eventEP6QEvent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QtVirtualKeyboard20InputSelectionHandle5eventEP6Q'
          'Event')
    return self.uglySide.call(ritual, self._addressOf(event))
