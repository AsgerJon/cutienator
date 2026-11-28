"""
QWaylandSurfaceGrabber binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWaylandCompositor/qwaylandsurfacegrabber.h, Qt 6.12.0. Changes made here
#  are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QImage
  from . import QWaylandSurface
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QImage = WAIT['QImage']
  QWaylandSurface = WAIT['QWaylandSurface']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QWaylandSurfaceGrabber(QObject):
  """
  The cute side of Qt's QWaylandSurfaceGrabber: a plain Python object
  standing in front of one C++ QWaylandSurfaceGrabber.

  It is built on the cute 'QObject', as Qt's QWaylandSurfaceGrabber is built
  on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QWaylandSurfaceGrabber that has a ritual and that
  Python can call so far, 6 names in all: 'metaObject', 'tr', 'surface',
  'grab', 'success', 'failed'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QWaylandSurfaceGrabber::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QWaylandSurfaceGrabber::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QWaylandSurfaceGrabberPrivate *QWaylandSurfaceGrabber::d_func()':
    gives 'QWaylandSurfaceGrabberPrivate', which has no cute class yet.
  - Qt's 'const QWaylandSurfaceGrabberPrivate
    *QWaylandSurfaceGrabber::d_func() const': gives
    'QWaylandSurfaceGrabberPrivate', which has no cute class yet.

  What has no ritual
  ------------------

  2 of the 13 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QWaylandSurfaceGrabber is created at the first use, not by
    'QWaylandSurfaceGrabber(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QWaylandSurfaceGrabber.
  - Qt tells when it has removed the C++ QWaylandSurfaceGrabber. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QWaylandSurfaceGrabber, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class Error(CuteNum):
    """
    The enum 'QWaylandSurfaceGrabber::Error' of Qt, with the 4 names Qt gives
    in it.
    """

    InvalidSurface = Kee[int](0)
    NoBufferAttached = Kee[int](1)
    UnknownBufferType = Kee[int](2)
    RendererNotReady = Kee[int](3)

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
    Calls Qt's 'QString QWaylandSurfaceGrabber::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandsurfacegrabber.html#tr

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
    #  QString QWaylandSurfaceGrabber::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN22QWaylandSurfaceGrabber2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWaylandSurfaceGrabber'

  #  A C++ QWaylandSurfaceGrabber Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QWaylandSurfaceGrabber'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QWaylandSurfaceGrabber::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandsurfacegrabber.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QWaylandSurfaceGrabber::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK22QWaylandSurfaceGrabber10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def surface(self) -> Optional[QWaylandSurface]:
    """
    Calls Qt's 'QWaylandSurface *QWaylandSurfaceGrabber::surface() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandsurfacegrabber.html#surface

    Returns
    -------

    Optional[QWaylandSurface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWaylandSurface *QWaylandSurfaceGrabber::surface() const
    address = self.uglySide.call(
        'ritual_ZNK22QWaylandSurfaceGrabber7surfaceEv',
    )
    from . import QWaylandSurface
    return QWaylandSurface._cuteAt(address)

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

  @overload(QWaylandSurface)
  @overload(NoneType)
  @overload(QWaylandSurface, QObject)
  @overload(QWaylandSurface, NoneType)
  @overload(NoneType, QObject)
  @overload(NoneType, NoneType)
  def __init__(
      self,
      surface: Optional[QWaylandSurface],
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QWaylandSurfaceGrabber::QWaylandSurfaceGrabber(QWaylandSurface *surface,
    QObject *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandsurfacegrabber.html#QWaylandSurfaceGrabber

    Parameters
    ----------

    surface : Optional[QWaylandSurface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QWaylandSurfaceGrabber::QWaylandSurfaceGrabber(QWaylandSurface
    #      *surface, QObject *parent)
    self._noteCreation(QWaylandSurfaceGrabber, lambda: Rituals.call(
        'ritual_ZN22QWaylandSurfaceGrabberC1EP15QWaylandSurfaceP7QObject',
        self._addressOf(surface), self._addressOf(parent, 'QObject'),
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

  def grab(self) -> None:
    """
    Calls Qt's 'void QWaylandSurfaceGrabber::grab()'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandsurfacegrabber.html#grab
    """
    #  void QWaylandSurfaceGrabber::grab()
    self.uglySide.call('ritual_ZN22QWaylandSurfaceGrabber4grabEv')

  @overload(QImage)
  def success(self, image: QImage) -> None:
    """
    Calls Qt's 'void QWaylandSurfaceGrabber::success(const QImage &image)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandsurfacegrabber.html#success

    Parameters
    ----------

    image : QImage
      Passed on as a value: Qt reads the C++ QImage, which stays Python's
      own.
    """
    #  void QWaylandSurfaceGrabber::success(const QImage &image)
    self.uglySide.call(
        'ritual_ZN22QWaylandSurfaceGrabber7successERK6QImage',
        self._valueOf(image),
    )

  @overload(Error)
  def failed(self, error: Error) -> None:
    """
    Calls Qt's 'void QWaylandSurfaceGrabber::failed(Error error)'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandsurfacegrabber.html#failed

    Parameters
    ----------

    error : Error
      Passed on as its number.
    """
    #  void QWaylandSurfaceGrabber::failed(Error error)
    self.uglySide.call(
        'ritual_ZN22QWaylandSurfaceGrabber6failedENS_5ErrorE', error.value,
    )
