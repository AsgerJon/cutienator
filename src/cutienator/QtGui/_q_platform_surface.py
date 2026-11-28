"""
QPlatformSurface binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/qpa/qplatformsurface.h, Qt 6.12.0. Changes made here
#  are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QPlatformScreen, QSurface, QSurfaceFormat
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QSurface = WAIT['QSurface']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPlatformSurface(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QPlatformSurface: a plain Python object standing in
  front of one C++ QPlatformSurface.

  What exists
  -----------

  Every function of Qt's QPlatformSurface that has a ritual and that Python
  can call so far, 3 names in all: 'format', 'surface', 'screen'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QPlatformSurface::~QPlatformSurface()': the destructor: Python
    never removes a C++ QPlatformSurface.

  What has no ritual
  ------------------

  4 of the 9 functions Qt declares: 4 forbidden.

  What to expect
  --------------

  - The C++ QPlatformSurface is created at the first use, not by
    'QPlatformSurface(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QPlatformSurface.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPlatformSurface'

  #  A C++ QPlatformSurface Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QPlatformSurface'

  #  The functions Qt calls itself that QPlatformSurface is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'format': (
          ('_ZNK16QPlatformSurface6formatEv',
           ('address', 'value', 'QtGui:QSurfaceFormat'),
           ()),
      ),
      'screen': (
          ('_ZNK16QPlatformSurface6screenEv',
           ('address', 'address', 'QtGui:QPlatformScreen'),
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

  def format(self) -> QSurfaceFormat:
    """
    Calls Qt's 'QSurfaceFormat QPlatformSurface::format() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformsurface.html#format

    Returns
    -------

    QSurfaceFormat
      A new cute QSurfaceFormat around the copy Qt gave back. Python owns it.
    """
    #  QSurfaceFormat QPlatformSurface::format() const
    address = self.uglySide.call('ritual_ZNK16QPlatformSurface6formatEv')
    from . import QSurfaceFormat
    return QSurfaceFormat._cuteOwning(address)

  def surface(self) -> Optional[QSurface]:
    """
    Calls Qt's 'QSurface *QPlatformSurface::surface() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformsurface.html#surface

    Returns
    -------

    Optional[QSurface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSurface *QPlatformSurface::surface() const
    address = self.uglySide.call('ritual_ZNK16QPlatformSurface7surfaceEv')
    from . import QSurface
    return QSurface._cuteAt(address)

  def screen(self) -> Optional[QPlatformScreen]:
    """
    Calls Qt's 'QPlatformScreen *QPlatformSurface::screen() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformsurface.html#screen

    Returns
    -------

    Optional[QPlatformScreen]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlatformScreen *QPlatformSurface::screen() const
    address = self.uglySide.call('ritual_ZNK16QPlatformSurface6screenEv')
    from . import QPlatformScreen
    return QPlatformScreen._cuteAt(address)

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

  @overload(QSurface)
  @overload(NoneType)
  def __init__(self, surface: Optional[QSurface]) -> None:
    """
    Notes what was given, for Qt's
    'QPlatformSurface::QPlatformSurface(QSurface *surface)', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformsurface.html#QPlatformSurface

    Parameters
    ----------

    surface : Optional[QSurface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QPlatformSurface::QPlatformSurface(QSurface *surface)
    self._noteCreation(QPlatformSurface, lambda: Rituals.call(
        'ritual_ZN16QPlatformSurfaceC1EP8QSurface',
        self._addressOf(surface, 'QSurface'),
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
