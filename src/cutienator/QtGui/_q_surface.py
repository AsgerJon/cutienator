"""
QSurface binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/qsurface.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QSize
  from . import QPlatformSurface, QSurfaceFormat


class QSurface(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSurface: a plain Python object standing in front of
  one C++ QSurface.

  What exists
  -----------

  Every function of Qt's QSurface that has a ritual and that Python can call
  so far, 6 names in all: 'surfaceClass', 'format', 'surfaceHandle',
  'surfaceType', 'supportsOpenGL', 'size'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSurface::~QSurface()': the destructor: Python never removes a C++
    QSurface.

  What has no ritual
  ------------------

  3 of the 11 functions Qt declares: 3 not a gap.

  What to expect
  --------------

  - The C++ QSurface is created at the first use, not by 'QSurface(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSurface.
  """

  #  The enums Qt writes inside QSurface, each a class in here as in C++, and
  #  the names Qt has for the combinations of its flags enums.

  class SurfaceClass(CuteNum):
    """
    The enum 'QSurface::SurfaceClass' of Qt, with the 2 names Qt gives in it.
    """

    Window = Kee[int](0)
    Offscreen = Kee[int](1)

  class SurfaceType(CuteNum):
    """
    The enum 'QSurface::SurfaceType' of Qt, with the 7 names Qt gives in it.
    """

    RasterSurface = Kee[int](0)
    OpenGLSurface = Kee[int](1)
    RasterGLSurface = Kee[int](2)
    OpenVGSurface = Kee[int](3)
    VulkanSurface = Kee[int](4)
    MetalSurface = Kee[int](5)
    Direct3DSurface = Kee[int](6)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSurface'

  #  A C++ QSurface Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSurface'

  #  The functions Qt calls itself that QSurface is the first to declare. A
  #  class of a program built on it can write one anew, and Qt then calls
  #  that. For each name: the key C++ knows the function by, what it gives,
  #  and what it takes.
  __virtual_functions__ = {
      'format': (
          ('_ZNK8QSurface6formatEv',
           ('address', 'value', 'QtGui:QSurfaceFormat'),
           ()),
      ),
      'surfaceHandle': (
          ('_ZNK8QSurface13surfaceHandleEv',
           ('address', 'address', 'QtGui:QPlatformSurface'),
           ()),
      ),
      'surfaceType': (
          ('_ZNK8QSurface11surfaceTypeEv',
           ('int', 'enum', 'QtGui:QSurface.SurfaceType'),
           ()),
      ),
      'size': (
          ('_ZNK8QSurface4sizeEv',
           ('address', 'value', 'QtCore:QSize'),
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

  def surfaceClass(self) -> SurfaceClass:
    """
    Calls Qt's 'SurfaceClass QSurface::surfaceClass() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsurface.html#surfaceClass

    Returns
    -------

    SurfaceClass
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'SurfaceClass(number)'
      gives.
    """
    #  SurfaceClass QSurface::surfaceClass() const
    return QSurface.SurfaceClass(self._callAs(
        'QSurface', 'ritual_ZNK8QSurface12surfaceClassEv',
    ))

  def format(self) -> QSurfaceFormat:
    """
    Calls Qt's 'QSurfaceFormat QSurface::format() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsurface.html#format

    Returns
    -------

    QSurfaceFormat
      A new cute QSurfaceFormat around the copy Qt gave back. Python owns it.
    """
    #  QSurfaceFormat QSurface::format() const
    address = self._callAs('QSurface', 'ritual_ZNK8QSurface6formatEv')
    from . import QSurfaceFormat
    return QSurfaceFormat._cuteOwning(address)

  def surfaceHandle(self) -> Optional[QPlatformSurface]:
    """
    Calls Qt's 'QPlatformSurface *QSurface::surfaceHandle() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsurface.html#surfaceHandle

    Returns
    -------

    Optional[QPlatformSurface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlatformSurface *QSurface::surfaceHandle() const
    address = self._callAs(
        'QSurface', 'ritual_ZNK8QSurface13surfaceHandleEv',
    )
    from . import QPlatformSurface
    return QPlatformSurface._cuteAt(address)

  def surfaceType(self) -> SurfaceType:
    """
    Calls Qt's 'SurfaceType QSurface::surfaceType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsurface.html#surfaceType

    Returns
    -------

    SurfaceType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'SurfaceType(number)'
      gives.
    """
    #  SurfaceType QSurface::surfaceType() const
    return QSurface.SurfaceType(self._callAs(
        'QSurface', 'ritual_ZNK8QSurface11surfaceTypeEv',
    ))

  def supportsOpenGL(self) -> bool:
    """
    Calls Qt's 'bool QSurface::supportsOpenGL() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsurface.html#supportsOpenGL
    """
    #  bool QSurface::supportsOpenGL() const
    return self._callAs('QSurface', 'ritual_ZNK8QSurface14supportsOpenGLEv')

  def size(self) -> QSize:
    """
    Calls Qt's 'QSize QSurface::size() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsurface.html#size

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QSurface::size() const
    address = self._callAs('QSurface', 'ritual_ZNK8QSurface4sizeEv')
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

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

  @overload(SurfaceClass)
  def __init__(self, type: SurfaceClass) -> None:
    """
    Notes what was given, for Qt's 'QSurface::QSurface(SurfaceClass type)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qsurface.html#QSurface

    Parameters
    ----------

    type : SurfaceClass
      Passed on as its number.
    """
    #  QSurface::QSurface(SurfaceClass type)
    self._noteCreation(QSurface, lambda: Rituals.call(
        'ritual_ZN8QSurfaceC1ENS_12SurfaceClassE', type.value,
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
