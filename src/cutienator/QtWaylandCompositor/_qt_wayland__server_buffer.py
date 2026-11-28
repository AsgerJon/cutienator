"""
QtWayland::ServerBuffer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWaylandCompositor/6.12.0/QtWaylandCompositor/private/qwlserverbufferintegration_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QtWayland::ServerBuffer to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QSize
  from ..QtOpenGL import QOpenGLTexture
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QSize = WAIT['QSize']


class ServerBuffer(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QtWayland::ServerBuffer: a plain Python object
  standing in front of one C++ QtWayland::ServerBuffer.

  What exists
  -----------

  Every function of Qt's QtWayland::ServerBuffer that has a ritual and that
  Python can call so far, 6 names in all: 'bufferInUse', 'toOpenGlTexture',
  'releaseOpenGlTexture', 'isYInverted', 'size', 'format'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QtWayland::ServerBuffer::~ServerBuffer()': the destructor: Python
    never removes a C++ QtWayland::ServerBuffer.
  - Qt's 'struct ::wl_resource
    *QtWayland::ServerBuffer::resourceForClient(struct ::wl_client *a0)':
    names 'struct ::wl_client', which has no cute class yet.

  What to expect
  --------------

  - The C++ QtWayland::ServerBuffer is created at the first use, not by
    'QtWayland::ServerBuffer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QtWayland::ServerBuffer.
  - Each name of Qt's QtWayland::ServerBuffer that has no cute function yet,
    'resourceForClient', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  #  The enums Qt writes inside QtWayland::ServerBuffer, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class Format(CuteNum):
    """
    The enum 'QtWayland::ServerBuffer::Format' of Qt, with the 3 names Qt
    gives in it.
    """

    RGBA32 = Kee[int](0)
    A8 = Kee[int](1)
    Custom = Kee[int](2)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QtWayland::ServerBuffer'

  #  A C++ QtWayland::ServerBuffer Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QtWayland_ServerBuffer'

  #  The functions Qt calls itself that QtWayland::ServerBuffer is the first
  #  to declare and that cannot be handed to Python yet, each as Qt declares
  #  it. A class of a program that writes one of them anew is refused, since
  #  Qt would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'resourceForClient': (
          'struct ::wl_resource '
          '*QtWayland::ServerBuffer::resourceForClient(struct ::wl_client '
          '*)',
      ),
  }

  #  The functions Qt calls itself that QtWayland::ServerBuffer is the first
  #  to declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'bufferInUse': (
          ('_ZN9QtWayland12ServerBuffer11bufferInUseEv',
           ('bool', 'number', ''),
           ()),
      ),
      'toOpenGlTexture': (
          ('_ZN9QtWayland12ServerBuffer15toOpenGlTextureEv',
           ('address', 'address', 'QtOpenGL:QOpenGLTexture'),
           ()),
      ),
      'releaseOpenGlTexture': (
          ('_ZN9QtWayland12ServerBuffer20releaseOpenGlTextureEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'isYInverted': (
          ('_ZNK9QtWayland12ServerBuffer11isYInvertedEv',
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

  def isYInverted(self) -> bool:
    """
    Calls Qt's 'bool QtWayland::ServerBuffer::isYInverted() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtwayland-serverbuffer.html#isYInverted
    """
    #  bool QtWayland::ServerBuffer::isYInverted() const
    ritual = 'ritual_ZNK9QtWayland12ServerBuffer11isYInvertedEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK9QtWayland12ServerBuffer11isYInvertedEv'
    return self.uglySide.call(ritual)

  def size(self) -> QSize:
    """
    Calls Qt's 'QSize QtWayland::ServerBuffer::size() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtwayland-serverbuffer.html#size

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QtWayland::ServerBuffer::size() const
    address = self.uglySide.call('ritual_ZNK9QtWayland12ServerBuffer4sizeEv')
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def format(self) -> Format:
    """
    Calls Qt's 'Format QtWayland::ServerBuffer::format() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtwayland-serverbuffer.html#format

    Returns
    -------

    Format
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Format(number)' gives.
    """
    #  Format QtWayland::ServerBuffer::format() const
    return ServerBuffer.Format(self.uglySide.call(
        'ritual_ZNK9QtWayland12ServerBuffer6formatEv',
    ))

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

  @overload(QSize, Format)
  def __init__(self, size: QSize, format: Format) -> None:
    """
    Notes what was given, for Qt's
    'QtWayland::ServerBuffer::ServerBuffer(const QSize &size,
    ServerBuffer::Format format)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtwayland-serverbuffer.html#ServerBuffer

    Parameters
    ----------

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    format : Format
      Passed on as its number.
    """
    #  QtWayland::ServerBuffer::ServerBuffer(const QSize &size,
    #      ServerBuffer::Format format)
    self._noteCreation(ServerBuffer, lambda: Rituals.call(
        'ritual_ZN9QtWayland12ServerBufferC1ERK5QSizeNS0_6FormatE',
        self._valueOf(size), format.value,
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

  def bufferInUse(self) -> bool:
    """
    Calls Qt's 'bool QtWayland::ServerBuffer::bufferInUse()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtwayland-serverbuffer.html#bufferInUse
    """
    #  bool QtWayland::ServerBuffer::bufferInUse()
    ritual = 'ritual_ZN9QtWayland12ServerBuffer11bufferInUseEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN9QtWayland12ServerBuffer11bufferInUseEv'
    return self.uglySide.call(ritual)

  def toOpenGlTexture(self) -> Optional[QOpenGLTexture]:
    """
    Calls Qt's 'QOpenGLTexture *QtWayland::ServerBuffer::toOpenGlTexture()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtwayland-serverbuffer.html#toOpenGlTexture

    Returns
    -------

    Optional[QOpenGLTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QOpenGLTexture *QtWayland::ServerBuffer::toOpenGlTexture()
    address = self.uglySide.call(
        'ritual_ZN9QtWayland12ServerBuffer15toOpenGlTextureEv',
    )
    from ..QtOpenGL import QOpenGLTexture
    return QOpenGLTexture._cuteAt(address)

  def releaseOpenGlTexture(self) -> None:
    """
    Calls Qt's 'void QtWayland::ServerBuffer::releaseOpenGlTexture()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtwayland-serverbuffer.html#releaseOpenGlTexture
    """
    #  void QtWayland::ServerBuffer::releaseOpenGlTexture()
    ritual = 'ritual_ZN9QtWayland12ServerBuffer20releaseOpenGlTextureEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN9QtWayland12ServerBuffer20releaseOpenGlTextureEv')
    self.uglySide.call(ritual)

  @staticmethod
  def resourceForClient(*__, **_) -> Never:
    """
    Qt's 'struct ::wl_resource
    *QtWayland::ServerBuffer::resourceForClient(struct ::wl_client *a0)':
    names 'struct ::wl_client', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QtWayland.ServerBuffer.resourceForClient' has no cute function "
        "yet. Qt's 'struct ::wl_resource "
        "*QtWayland::ServerBuffer::resourceForClient(struct ::wl_client "
        "*a0)': names 'struct ::wl_client', which has no cute class yet.")
