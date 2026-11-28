"""
Qt3DRender::QObjectPicker binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/qobjectpicker.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore
from . import Qt3DRender

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QObjectPicker(Qt3DCore.QComponent):
  """
  The cute side of Qt's Qt3DRender::QObjectPicker: a plain Python object
  standing in front of one C++ Qt3DRender::QObjectPicker.

  It is built on the cute 'Qt3DCore::QComponent', as Qt's
  Qt3DRender::QObjectPicker is built on Qt's Qt3DCore::QComponent, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::QObjectPicker that has a ritual and that
  Python can call so far, 22 names in all: 'metaObject', 'tr',
  'isHoverEnabled', 'isDragEnabled', 'containsMouse', 'isPressed',
  'priority', 'setHoverEnabled', 'setDragEnabled', 'setPriority', 'pressed',
  'released', 'clicked', 'moved', 'entered', 'exited', 'hoverEnabledChanged',
  'dragEnabledChanged', 'pressedChanged', 'containsMouseChanged',
  'priorityChanged', 'd_func'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DRender::QObjectPicker::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int Qt3DRender::QObjectPicker::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DRender::QObjectPicker::~QObjectPicker()': the destructor:
    Python never removes a C++ Qt3DRender::QObjectPicker.
  - Qt's 'const QObjectPickerPrivate *Qt3DRender::QObjectPicker::d_func()
    const': takes in Python what 'QObjectPickerPrivate
    *Qt3DRender::QObjectPicker::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 29 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DRender::QObjectPicker is created at the first use, not by
    'Qt3DRender::QObjectPicker(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::QObjectPicker.
  - Qt tells when it has removed the C++ Qt3DRender::QObjectPicker. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
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
    Calls Qt's 'QString Qt3DRender::QObjectPicker::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-qobjectpicker.html#tr

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
    #  QString Qt3DRender::QObjectPicker::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN10Qt3DRender13QObjectPicker2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::QObjectPicker'

  #  A C++ Qt3DRender::QObjectPicker Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DRender_QObjectPicker'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *Qt3DRender::QObjectPicker::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qobjectpicker.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DRender::QObjectPicker::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender13QObjectPicker10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def isHoverEnabled(self) -> bool:
    """
    Calls Qt's 'bool Qt3DRender::QObjectPicker::isHoverEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qobjectpicker.html#isHoverEnabled
    """
    #  bool Qt3DRender::QObjectPicker::isHoverEnabled() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender13QObjectPicker14isHoverEnabledEv',
    )

  def isDragEnabled(self) -> bool:
    """
    Calls Qt's 'bool Qt3DRender::QObjectPicker::isDragEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qobjectpicker.html#isDragEnabled
    """
    #  bool Qt3DRender::QObjectPicker::isDragEnabled() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender13QObjectPicker13isDragEnabledEv',
    )

  def containsMouse(self) -> bool:
    """
    Calls Qt's 'bool Qt3DRender::QObjectPicker::containsMouse() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qobjectpicker.html#containsMouse
    """
    #  bool Qt3DRender::QObjectPicker::containsMouse() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender13QObjectPicker13containsMouseEv',
    )

  def isPressed(self) -> bool:
    """
    Calls Qt's 'bool Qt3DRender::QObjectPicker::isPressed() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qobjectpicker.html#isPressed
    """
    #  bool Qt3DRender::QObjectPicker::isPressed() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender13QObjectPicker9isPressedEv',
    )

  def priority(self) -> int:
    """
    Calls Qt's 'int Qt3DRender::QObjectPicker::priority() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qobjectpicker.html#priority
    """
    #  int Qt3DRender::QObjectPicker::priority() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender13QObjectPicker8priorityEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setHoverEnabled(self, hoverEnabled: bool) -> None:
    """
    Calls Qt's 'void Qt3DRender::QObjectPicker::setHoverEnabled(bool
    hoverEnabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qobjectpicker.html#setHoverEnabled

    Parameters
    ----------

    hoverEnabled : bool
      Passed on as it is.
    """
    #  void Qt3DRender::QObjectPicker::setHoverEnabled(bool hoverEnabled)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender13QObjectPicker15setHoverEnabledEb',
        hoverEnabled,
    )

  @overload(bool)
  def setDragEnabled(self, dragEnabled: bool) -> None:
    """
    Calls Qt's 'void Qt3DRender::QObjectPicker::setDragEnabled(bool
    dragEnabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qobjectpicker.html#setDragEnabled

    Parameters
    ----------

    dragEnabled : bool
      Passed on as it is.
    """
    #  void Qt3DRender::QObjectPicker::setDragEnabled(bool dragEnabled)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender13QObjectPicker14setDragEnabledEb',
        dragEnabled,
    )

  @overload(int)
  def setPriority(self, priority: int) -> None:
    """
    Calls Qt's 'void Qt3DRender::QObjectPicker::setPriority(int priority)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qobjectpicker.html#setPriority

    Parameters
    ----------

    priority : int
      Passed on as it is.
    """
    #  void Qt3DRender::QObjectPicker::setPriority(int priority)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender13QObjectPicker11setPriorityEi', priority,
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

  @overload()
  @overload(Qt3DCore.QNode)
  @overload(NoneType)
  def __init__(self, parent: Optional[Qt3DCore.QNode] = None) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DRender::QObjectPicker::QObjectPicker(QNode *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qobjectpicker.html#QObjectPicker

    Parameters
    ----------

    parent : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DRender::QObjectPicker::QObjectPicker(QNode *parent)
    self._noteCreation(QObjectPicker, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender13QObjectPickerC1EPN8Qt3DCore5QNodeE',
        self._addressOf(parent),
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

  @overload(WAIT['Qt3DRender.QPickEvent'])
  @overload(NoneType)
  def pressed(self, pick: Optional[Qt3DRender.QPickEvent]) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QObjectPicker::pressed(Qt3DRender::QPickEvent *pick)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qobjectpicker.html#pressed

    Parameters
    ----------

    pick : Optional[Qt3DRender.QPickEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::QObjectPicker::pressed(Qt3DRender::QPickEvent *pick)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender13QObjectPicker7pressedEPNS_10QPickEventE',
        self._addressOf(pick),
    )

  @overload(WAIT['Qt3DRender.QPickEvent'])
  @overload(NoneType)
  def released(self, pick: Optional[Qt3DRender.QPickEvent]) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QObjectPicker::released(Qt3DRender::QPickEvent *pick)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qobjectpicker.html#released

    Parameters
    ----------

    pick : Optional[Qt3DRender.QPickEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::QObjectPicker::released(Qt3DRender::QPickEvent *pick)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender13QObjectPicker8releasedEPNS_10QPickEventE',
        self._addressOf(pick),
    )

  @overload(WAIT['Qt3DRender.QPickEvent'])
  @overload(NoneType)
  def clicked(self, pick: Optional[Qt3DRender.QPickEvent]) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QObjectPicker::clicked(Qt3DRender::QPickEvent *pick)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qobjectpicker.html#clicked

    Parameters
    ----------

    pick : Optional[Qt3DRender.QPickEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::QObjectPicker::clicked(Qt3DRender::QPickEvent *pick)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender13QObjectPicker7clickedEPNS_10QPickEventE',
        self._addressOf(pick),
    )

  @overload(WAIT['Qt3DRender.QPickEvent'])
  @overload(NoneType)
  def moved(self, pick: Optional[Qt3DRender.QPickEvent]) -> None:
    """
    Calls Qt's 'void Qt3DRender::QObjectPicker::moved(Qt3DRender::QPickEvent
    *pick)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qobjectpicker.html#moved

    Parameters
    ----------

    pick : Optional[Qt3DRender.QPickEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::QObjectPicker::moved(Qt3DRender::QPickEvent *pick)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender13QObjectPicker5movedEPNS_10QPickEventE',
        self._addressOf(pick),
    )

  def entered(self) -> None:
    """
    Calls Qt's 'void Qt3DRender::QObjectPicker::entered()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qobjectpicker.html#entered
    """
    #  void Qt3DRender::QObjectPicker::entered()
    self.uglySide.call('ritual_ZN10Qt3DRender13QObjectPicker7enteredEv')

  def exited(self) -> None:
    """
    Calls Qt's 'void Qt3DRender::QObjectPicker::exited()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qobjectpicker.html#exited
    """
    #  void Qt3DRender::QObjectPicker::exited()
    self.uglySide.call('ritual_ZN10Qt3DRender13QObjectPicker6exitedEv')

  @overload(bool)
  def hoverEnabledChanged(self, hoverEnabled: bool) -> None:
    """
    Calls Qt's 'void Qt3DRender::QObjectPicker::hoverEnabledChanged(bool
    hoverEnabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qobjectpicker.html#hoverEnabledChanged

    Parameters
    ----------

    hoverEnabled : bool
      Passed on as it is.
    """
    #  void Qt3DRender::QObjectPicker::hoverEnabledChanged(bool hoverEnabled)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender13QObjectPicker19hoverEnabledChangedEb',
        hoverEnabled,
    )

  @overload(bool)
  def dragEnabledChanged(self, dragEnabled: bool) -> None:
    """
    Calls Qt's 'void Qt3DRender::QObjectPicker::dragEnabledChanged(bool
    dragEnabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qobjectpicker.html#dragEnabledChanged

    Parameters
    ----------

    dragEnabled : bool
      Passed on as it is.
    """
    #  void Qt3DRender::QObjectPicker::dragEnabledChanged(bool dragEnabled)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender13QObjectPicker18dragEnabledChangedEb',
        dragEnabled,
    )

  @overload(bool)
  def pressedChanged(self, pressed: bool) -> None:
    """
    Calls Qt's 'void Qt3DRender::QObjectPicker::pressedChanged(bool
    pressed)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qobjectpicker.html#pressedChanged

    Parameters
    ----------

    pressed : bool
      Passed on as it is.
    """
    #  void Qt3DRender::QObjectPicker::pressedChanged(bool pressed)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender13QObjectPicker14pressedChangedEb', pressed,
    )

  @overload(bool)
  def containsMouseChanged(self, containsMouse: bool) -> None:
    """
    Calls Qt's 'void Qt3DRender::QObjectPicker::containsMouseChanged(bool
    containsMouse)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qobjectpicker.html#containsMouseChanged

    Parameters
    ----------

    containsMouse : bool
      Passed on as it is.
    """
    #  void Qt3DRender::QObjectPicker::containsMouseChanged(bool
    #      containsMouse)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender13QObjectPicker20containsMouseChangedEb',
        containsMouse,
    )

  @overload(int)
  def priorityChanged(self, priority: int) -> None:
    """
    Calls Qt's 'void Qt3DRender::QObjectPicker::priorityChanged(int
    priority)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qobjectpicker.html#priorityChanged

    Parameters
    ----------

    priority : int
      Passed on as it is.
    """
    #  void Qt3DRender::QObjectPicker::priorityChanged(int priority)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender13QObjectPicker15priorityChangedEi', priority,
    )

  def d_func(self) -> Optional[Qt3DRender.QObjectPickerPrivate]:
    """
    Calls Qt's 'QObjectPickerPrivate *Qt3DRender::QObjectPicker::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qobjectpicker.html#d_func

    Returns
    -------

    Optional[Qt3DRender.QObjectPickerPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObjectPickerPrivate *Qt3DRender::QObjectPicker::d_func()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DRender13QObjectPicker6d_funcEv',
    )
    return Qt3DRender.QObjectPickerPrivate._cuteAt(address)
