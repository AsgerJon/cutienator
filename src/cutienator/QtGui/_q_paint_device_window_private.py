"""
QPaintDeviceWindowPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qpaintdevicewindow_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QPaintDeviceWindowPrivate to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QWindowPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QPaintDeviceWindow, QRegion
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRegion = WAIT['QRegion']


class QPaintDeviceWindowPrivate(QWindowPrivate):
  """
  The cute side of Qt's QPaintDeviceWindowPrivate: a plain Python object
  standing in front of one C++ QPaintDeviceWindowPrivate.

  It is built on the cute 'QWindowPrivate', as Qt's QPaintDeviceWindowPrivate
  is built on Qt's QWindowPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QPaintDeviceWindowPrivate that has a ritual and that
  Python can call so far, 9 names in all: 'q_func', 'handleResizeEvent',
  'beginPaint', 'endPaint', 'flush', 'paint', 'doFlush', 'handleUpdateEvent',
  'markWindowAsDirty'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QPaintDeviceWindow *QPaintDeviceWindowPrivate::q_func()
    const': takes in Python what 'QPaintDeviceWindow
    *QPaintDeviceWindowPrivate::q_func()' takes.
  - Qt's 'QPaintDeviceWindowPrivate::~QPaintDeviceWindowPrivate()': the
    destructor: Python never removes a C++ QPaintDeviceWindowPrivate.

  What to expect
  --------------

  - The C++ QPaintDeviceWindowPrivate is created at the first use, not by
    'QPaintDeviceWindowPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QPaintDeviceWindowPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPaintDeviceWindowPrivate'

  #  A C++ QPaintDeviceWindowPrivate Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QPaintDeviceWindowPrivate'

  #  The functions Qt calls itself that QPaintDeviceWindowPrivate is the
  #  first to declare. A class of a program built on it can write one anew,
  #  and Qt then calls that. For each name: the key C++ knows the function
  #  by, what it gives, and what it takes.
  __virtual_functions__ = {
      'handleResizeEvent': (
          ('_ZN25QPaintDeviceWindowPrivate17handleResizeEventEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'beginPaint': (
          ('_ZN25QPaintDeviceWindowPrivate10beginPaintERK7QRegion',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtGui:QRegion'),
           )),
      ),
      'endPaint': (
          ('_ZN25QPaintDeviceWindowPrivate8endPaintEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'flush': (
          ('_ZN25QPaintDeviceWindowPrivate5flushERK7QRegion',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtGui:QRegion'),
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
    'QPaintDeviceWindowPrivate::QPaintDeviceWindowPrivate()', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qpaintdevicewindowprivate.html
    """
    #  QPaintDeviceWindowPrivate::QPaintDeviceWindowPrivate()
    self._noteCreation(QPaintDeviceWindowPrivate, lambda: Rituals.call(
        'ritual_ZN25QPaintDeviceWindowPrivateC1Ev',
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

  def q_func(self) -> Optional[QPaintDeviceWindow]:
    """
    Calls Qt's 'QPaintDeviceWindow *QPaintDeviceWindowPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpaintdevicewindowprivate.html#q_func

    Returns
    -------

    Optional[QPaintDeviceWindow]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPaintDeviceWindow *QPaintDeviceWindowPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN25QPaintDeviceWindowPrivate6q_funcEv',
    )
    from . import QPaintDeviceWindow
    return QPaintDeviceWindow._cuteAt(address)

  def handleResizeEvent(self) -> None:
    """
    Calls Qt's 'void QPaintDeviceWindowPrivate::handleResizeEvent()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpaintdevicewindowprivate.html#handleResizeEvent
    """
    #  void QPaintDeviceWindowPrivate::handleResizeEvent()
    ritual = 'ritual_ZN25QPaintDeviceWindowPrivate17handleResizeEventEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN25QPaintDeviceWindowPrivate17handleResizeEventEv')
    self.uglySide.call(ritual)

  @overload(QRegion)
  def beginPaint(self, region: QRegion) -> None:
    """
    Calls Qt's 'void QPaintDeviceWindowPrivate::beginPaint(const QRegion
    &region)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpaintdevicewindowprivate.html#beginPaint

    Parameters
    ----------

    region : QRegion
      Passed on as a value: Qt reads the C++ QRegion, which stays Python's
      own.
    """
    #  void QPaintDeviceWindowPrivate::beginPaint(const QRegion &region)
    ritual = 'ritual_ZN25QPaintDeviceWindowPrivate10beginPaintERK7QRegion'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN25QPaintDeviceWindowPrivate10beginPaintERK7QRegion')
    self.uglySide.call(ritual, self._valueOf(region))

  def endPaint(self) -> None:
    """
    Calls Qt's 'void QPaintDeviceWindowPrivate::endPaint()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpaintdevicewindowprivate.html#endPaint
    """
    #  void QPaintDeviceWindowPrivate::endPaint()
    ritual = 'ritual_ZN25QPaintDeviceWindowPrivate8endPaintEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN25QPaintDeviceWindowPrivate8endPaintEv'
    self.uglySide.call(ritual)

  @overload(QRegion)
  def flush(self, region: QRegion) -> None:
    """
    Calls Qt's 'void QPaintDeviceWindowPrivate::flush(const QRegion
    &region)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpaintdevicewindowprivate.html#flush

    Parameters
    ----------

    region : QRegion
      Passed on as a value: Qt reads the C++ QRegion, which stays Python's
      own.
    """
    #  void QPaintDeviceWindowPrivate::flush(const QRegion &region)
    ritual = 'ritual_ZN25QPaintDeviceWindowPrivate5flushERK7QRegion'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN25QPaintDeviceWindowPrivate5flushERK7QRegion'
    self.uglySide.call(ritual, self._valueOf(region))

  @overload(QRegion)
  def paint(self, region: QRegion) -> bool:
    """
    Calls Qt's 'bool QPaintDeviceWindowPrivate::paint(const QRegion
    &region)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpaintdevicewindowprivate.html#paint

    Parameters
    ----------

    region : QRegion
      Passed on as a value: Qt reads the C++ QRegion, which stays Python's
      own.
    """
    #  bool QPaintDeviceWindowPrivate::paint(const QRegion &region)
    return self.uglySide.call(
        'ritual_ZN25QPaintDeviceWindowPrivate5paintERK7QRegion',
        self._valueOf(region),
    )

  @overload(QRegion)
  def doFlush(self, region: QRegion) -> None:
    """
    Calls Qt's 'void QPaintDeviceWindowPrivate::doFlush(const QRegion
    &region)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpaintdevicewindowprivate.html#doFlush

    Parameters
    ----------

    region : QRegion
      Passed on as a value: Qt reads the C++ QRegion, which stays Python's
      own.
    """
    #  void QPaintDeviceWindowPrivate::doFlush(const QRegion &region)
    self.uglySide.call(
        'ritual_ZN25QPaintDeviceWindowPrivate7doFlushERK7QRegion',
        self._valueOf(region),
    )

  def handleUpdateEvent(self) -> None:
    """
    Calls Qt's 'void QPaintDeviceWindowPrivate::handleUpdateEvent()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpaintdevicewindowprivate.html#handleUpdateEvent
    """
    #  void QPaintDeviceWindowPrivate::handleUpdateEvent()
    self.uglySide.call(
        'ritual_ZN25QPaintDeviceWindowPrivate17handleUpdateEventEv',
    )

  def markWindowAsDirty(self) -> None:
    """
    Calls Qt's 'void QPaintDeviceWindowPrivate::markWindowAsDirty()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpaintdevicewindowprivate.html#markWindowAsDirty
    """
    #  void QPaintDeviceWindowPrivate::markWindowAsDirty()
    self.uglySide.call(
        'ritual_ZN25QPaintDeviceWindowPrivate17markWindowAsDirtyEv',
    )
