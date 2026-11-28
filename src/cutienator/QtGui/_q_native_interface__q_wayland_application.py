"""
QNativeInterface::QWaylandApplication binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/qguiapplication_platform.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QWaylandApplication(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QNativeInterface::QWaylandApplication: a plain Python
  object standing in front of one C++ QNativeInterface::QWaylandApplication.

  What exists
  -----------

  Every function of Qt's QNativeInterface::QWaylandApplication that has a
  ritual and that Python can call so far, 1 name in all: 'lastInputSerial'.
  It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QNativeInterface::QWaylandApplication::~QWaylandApplication()': the
    destructor: Python never removes a C++
    QNativeInterface::QWaylandApplication.
  - Qt's 'wl_display *QNativeInterface::QWaylandApplication::display()
    const': gives 'wl_display', which has no cute class yet.
  - Qt's 'wl_compositor *QNativeInterface::QWaylandApplication::compositor()
    const': gives 'wl_compositor', which has no cute class yet.
  - Qt's 'wl_seat *QNativeInterface::QWaylandApplication::seat() const':
    gives 'wl_seat', which has no cute class yet.
  - Qt's 'wl_keyboard *QNativeInterface::QWaylandApplication::keyboard()
    const': gives 'wl_keyboard', which has no cute class yet.
  - Qt's 'wl_pointer *QNativeInterface::QWaylandApplication::pointer()
    const': gives 'wl_pointer', which has no cute class yet.
  - Qt's 'wl_touch *QNativeInterface::QWaylandApplication::touch() const':
    gives 'wl_touch', which has no cute class yet.
  - Qt's 'wl_seat *QNativeInterface::QWaylandApplication::lastInputSeat()
    const': gives 'wl_seat', which has no cute class yet.
  - Qt's 'xkb_context *QNativeInterface::QWaylandApplication::xkbContext()
    const': gives 'xkb_context', which has no cute class yet.

  What has no ritual
  ------------------

  4 of the 15 functions Qt declares: 4 forbidden.

  What to expect
  --------------

  - The C++ QNativeInterface::QWaylandApplication is created at the first
    use, not by 'QNativeInterface::QWaylandApplication(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QNativeInterface::QWaylandApplication.
  - Each name of Qt's QNativeInterface::QWaylandApplication that has no cute
    function yet, 'compositor', 'display', 'keyboard', 'lastInputSeat',
    'pointer', 'seat', 'touch', 'xkbContext', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QNativeInterface::QWaylandApplication'

  #  A C++ QNativeInterface::QWaylandApplication Python makes is of a C++
  #  class of ours, in which Python can take functions over. This ritual
  #  hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QNativeInterface_QWaylandApplication'

  #  The functions Qt calls itself that QNativeInterface::QWaylandApplication
  #  is the first to declare and that cannot be handed to Python yet, each as
  #  Qt declares it. A class of a program that writes one of them anew is
  #  refused, since Qt would never call what it wrote; see
  #  'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'display': (
          'wl_display *QNativeInterface::QWaylandApplication::display() '
          'const',
      ),
      'compositor': (
          'wl_compositor '
          '*QNativeInterface::QWaylandApplication::compositor() const',
      ),
      'seat': (
          'wl_seat *QNativeInterface::QWaylandApplication::seat() const',
      ),
      'keyboard': (
          'wl_keyboard *QNativeInterface::QWaylandApplication::keyboard() '
          'const',
      ),
      'pointer': (
          'wl_pointer *QNativeInterface::QWaylandApplication::pointer() '
          'const',
      ),
      'touch': (
          'wl_touch *QNativeInterface::QWaylandApplication::touch() const',
      ),
      'lastInputSeat': (
          'wl_seat *QNativeInterface::QWaylandApplication::lastInputSeat() '
          'const',
      ),
      'xkbContext': (
          'xkb_context '
          '*QNativeInterface::QWaylandApplication::xkbContext() const',
      ),
  }

  #  The functions Qt calls itself that QNativeInterface::QWaylandApplication
  #  is the first to declare. A class of a program built on it can write one
  #  anew, and Qt then calls that. For each name: the key C++ knows the
  #  function by, what it gives, and what it takes.
  __virtual_functions__ = {
      'lastInputSerial': (
          ('_ZNK16QNativeInterface19QWaylandApplication15lastInputSerialEv',
           ('unsigned int', 'number', ''),
           ()),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def lastInputSerial(self) -> int:
    """
    Calls Qt's 'uint QNativeInterface::QWaylandApplication::lastInputSerial()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnativeinterface-qwaylandapplication.html
    """
    #  uint QNativeInterface::QWaylandApplication::lastInputSerial() const
    return self.uglySide.call(
        'ritual_ZNK16QNativeInterface19QWaylandApplication15lastInputSerial'
        'Ev',
    )

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
    'QNativeInterface::QWaylandApplication::QWaylandApplication()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qnativeinterface-qwaylandapplication.html
    """
    #  QNativeInterface::QWaylandApplication::QWaylandApplication()
    self._noteCreation(QWaylandApplication, lambda: Rituals.call(
        'ritual_ZN16QNativeInterface19QWaylandApplicationC1Ev',
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

  @staticmethod
  def compositor(*__, **_) -> Never:
    """
    Qt's 'wl_compositor *QNativeInterface::QWaylandApplication::compositor()
    const': gives 'wl_compositor', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QNativeInterface.QWaylandApplication.compositor' has no cute "
        "function yet. Qt's 'wl_compositor "
        "*QNativeInterface::QWaylandApplication::compositor() const': gives "
        "'wl_compositor', which has no cute class yet.")

  @staticmethod
  def display(*__, **_) -> Never:
    """
    Qt's 'wl_display *QNativeInterface::QWaylandApplication::display()
    const': gives 'wl_display', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QNativeInterface.QWaylandApplication.display' has no cute "
        "function yet. Qt's 'wl_display "
        "*QNativeInterface::QWaylandApplication::display() const': gives "
        "'wl_display', which has no cute class yet.")

  @staticmethod
  def keyboard(*__, **_) -> Never:
    """
    Qt's 'wl_keyboard *QNativeInterface::QWaylandApplication::keyboard()
    const': gives 'wl_keyboard', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QNativeInterface.QWaylandApplication.keyboard' has no cute "
        "function yet. Qt's 'wl_keyboard "
        "*QNativeInterface::QWaylandApplication::keyboard() const': gives "
        "'wl_keyboard', which has no cute class yet.")

  @staticmethod
  def lastInputSeat(*__, **_) -> Never:
    """
    Qt's 'wl_seat *QNativeInterface::QWaylandApplication::lastInputSeat()
    const': gives 'wl_seat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QNativeInterface.QWaylandApplication.lastInputSeat' has no cute "
        "function yet. Qt's 'wl_seat "
        "*QNativeInterface::QWaylandApplication::lastInputSeat() const': "
        "gives 'wl_seat', which has no cute class yet.")

  @staticmethod
  def pointer(*__, **_) -> Never:
    """
    Qt's 'wl_pointer *QNativeInterface::QWaylandApplication::pointer()
    const': gives 'wl_pointer', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QNativeInterface.QWaylandApplication.pointer' has no cute "
        "function yet. Qt's 'wl_pointer "
        "*QNativeInterface::QWaylandApplication::pointer() const': gives "
        "'wl_pointer', which has no cute class yet.")

  @staticmethod
  def seat(*__, **_) -> Never:
    """
    Qt's 'wl_seat *QNativeInterface::QWaylandApplication::seat() const':
    gives 'wl_seat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QNativeInterface.QWaylandApplication.seat' has no cute function "
        "yet. Qt's 'wl_seat *QNativeInterface::QWaylandApplication::seat() "
        "const': gives 'wl_seat', which has no cute class yet.")

  @staticmethod
  def touch(*__, **_) -> Never:
    """
    Qt's 'wl_touch *QNativeInterface::QWaylandApplication::touch() const':
    gives 'wl_touch', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QNativeInterface.QWaylandApplication.touch' has no cute function "
        "yet. Qt's 'wl_touch "
        "*QNativeInterface::QWaylandApplication::touch() const': gives "
        "'wl_touch', which has no cute class yet.")

  @staticmethod
  def xkbContext(*__, **_) -> Never:
    """
    Qt's 'xkb_context *QNativeInterface::QWaylandApplication::xkbContext()
    const': gives 'xkb_context', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QNativeInterface.QWaylandApplication.xkbContext' has no cute "
        "function yet. Qt's 'xkb_context "
        "*QNativeInterface::QWaylandApplication::xkbContext() const': gives "
        "'xkb_context', which has no cute class yet.")
