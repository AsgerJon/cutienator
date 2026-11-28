"""
QPlatformOffscreenSurface binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/qpa/qplatformoffscreensurface.h, Qt 6.12.0. Changes
#  made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QPlatformSurface

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QOffscreenSurface, QPlatformScreen, QSurfaceFormat
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QOffscreenSurface = WAIT['QOffscreenSurface']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPlatformOffscreenSurface(QPlatformSurface):
  """
  The cute side of Qt's QPlatformOffscreenSurface: a plain Python object
  standing in front of one C++ QPlatformOffscreenSurface.

  It is built on the cute 'QPlatformSurface', as Qt's
  QPlatformOffscreenSurface is built on Qt's QPlatformSurface, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QPlatformOffscreenSurface that has a ritual and that
  Python can call so far, 4 names in all: 'offscreenSurface', 'screen',
  'format', 'isValid'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QPlatformOffscreenSurfacePrivate
    *QPlatformOffscreenSurface::d_func()': gives
    'QPlatformOffscreenSurfacePrivate', which has no cute class yet.
  - Qt's 'const QPlatformOffscreenSurfacePrivate
    *QPlatformOffscreenSurface::d_func() const': gives
    'QPlatformOffscreenSurfacePrivate', which has no cute class yet.
  - Qt's 'QPlatformOffscreenSurface::~QPlatformOffscreenSurface()': the
    destructor: Python never removes a C++ QPlatformOffscreenSurface.

  What has no ritual
  ------------------

  2 of the 10 functions Qt declares: 2 forbidden.

  What to expect
  --------------

  - The C++ QPlatformOffscreenSurface is created at the first use, not by
    'QPlatformOffscreenSurface(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QPlatformOffscreenSurface.
  - Each name of Qt's QPlatformOffscreenSurface that has no cute function
    yet, 'd_func', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPlatformOffscreenSurface'

  #  A C++ QPlatformOffscreenSurface Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QPlatformOffscreenSurface'

  #  The functions Qt calls itself that QPlatformOffscreenSurface is the
  #  first to declare. A class of a program built on it can write one anew,
  #  and Qt then calls that. For each name: the key C++ knows the function
  #  by, what it gives, and what it takes.
  __virtual_functions__ = {
      'isValid': (
          ('_ZNK25QPlatformOffscreenSurface7isValidEv',
           ('bool', 'number', ''),
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

  def offscreenSurface(self) -> Optional[QOffscreenSurface]:
    """
    Calls Qt's 'QOffscreenSurface
    *QPlatformOffscreenSurface::offscreenSurface() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformoffscreensurface.html#offscreenSurface

    Returns
    -------

    Optional[QOffscreenSurface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QOffscreenSurface *QPlatformOffscreenSurface::offscreenSurface() const
    address = self.uglySide.call(
        'ritual_ZNK25QPlatformOffscreenSurface16offscreenSurfaceEv',
    )
    from . import QOffscreenSurface
    return QOffscreenSurface._cuteAt(address)

  def screen(self) -> Optional[QPlatformScreen]:
    """
    Calls Qt's 'QPlatformScreen *QPlatformOffscreenSurface::screen() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformoffscreensurface.html#screen

    Returns
    -------

    Optional[QPlatformScreen]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlatformScreen *QPlatformOffscreenSurface::screen() const
    ritual = 'ritual_ZNK25QPlatformOffscreenSurface6screenEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK25QPlatformOffscreenSurface6screenEv'
    address = self.uglySide.call(ritual)
    from . import QPlatformScreen
    return QPlatformScreen._cuteAt(address)

  def format(self) -> QSurfaceFormat:
    """
    Calls Qt's 'QSurfaceFormat QPlatformOffscreenSurface::format() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformoffscreensurface.html#format

    Returns
    -------

    QSurfaceFormat
      A new cute QSurfaceFormat around the copy Qt gave back. Python owns it.
    """
    #  QSurfaceFormat QPlatformOffscreenSurface::format() const
    ritual = 'ritual_ZNK25QPlatformOffscreenSurface6formatEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK25QPlatformOffscreenSurface6formatEv'
    address = self.uglySide.call(ritual)
    from . import QSurfaceFormat
    return QSurfaceFormat._cuteOwning(address)

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QPlatformOffscreenSurface::isValid() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformoffscreensurface.html#isValid
    """
    #  bool QPlatformOffscreenSurface::isValid() const
    ritual = 'ritual_ZNK25QPlatformOffscreenSurface7isValidEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK25QPlatformOffscreenSurface7isValidEv'
    return self.uglySide.call(ritual)

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

  @overload(QOffscreenSurface)
  @overload(NoneType)
  def __init__(self, offscreenSurface: Optional[QOffscreenSurface]) -> None:
    """
    Notes what was given, for Qt's
    'QPlatformOffscreenSurface::QPlatformOffscreenSurface(QOffscreenSurface
    *offscreenSurface)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformoffscreensurface.html

    Parameters
    ----------

    offscreenSurface : Optional[QOffscreenSurface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QPlatformOffscreenSurface::QPlatformOffscreenSurface(QOffscreenSurface
    #      *offscreenSurface)
    self._noteCreation(QPlatformOffscreenSurface, lambda: Rituals.call(
        'ritual_ZN25QPlatformOffscreenSurfaceC1EP17QOffscreenSurface',
        self._addressOf(offscreenSurface),
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
  def d_func(*__, **_) -> Never:
    """
    - Qt's 'QPlatformOffscreenSurfacePrivate
      *QPlatformOffscreenSurface::d_func()': gives
      'QPlatformOffscreenSurfacePrivate', which has no cute class yet.
    - Qt's 'const QPlatformOffscreenSurfacePrivate
      *QPlatformOffscreenSurface::d_func() const': gives
      'QPlatformOffscreenSurfacePrivate', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QPlatformOffscreenSurface.d_func' has no cute function yet. Qt's "
        "'QPlatformOffscreenSurfacePrivate "
        "*QPlatformOffscreenSurface::d_func()': gives "
        "'QPlatformOffscreenSurfacePrivate', which has no cute class yet. "
        "Qt's 'const QPlatformOffscreenSurfacePrivate "
        "*QPlatformOffscreenSurface::d_func() const': gives "
        "'QPlatformOffscreenSurfacePrivate', which has no cute class yet.")
