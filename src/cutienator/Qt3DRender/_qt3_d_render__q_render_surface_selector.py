"""
Qt3DRender::QRenderSurfaceSelector binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/qrendersurfaceselector.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from ..Qt3DCore import Qt3DCore
from . import Qt3DRender

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QSize
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QSize = WAIT['QSize']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QRenderSurfaceSelector(Qt3DRender.QFrameGraphNode):
  """
  The cute side of Qt's Qt3DRender::QRenderSurfaceSelector: a plain Python
  object standing in front of one C++ Qt3DRender::QRenderSurfaceSelector.

  It is built on the cute 'Qt3DRender::QFrameGraphNode', as Qt's
  Qt3DRender::QRenderSurfaceSelector is built on Qt's
  Qt3DRender::QFrameGraphNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::QRenderSurfaceSelector that has a ritual
  and that Python can call so far, 12 names in all: 'metaObject', 'tr',
  'surface', 'externalRenderTargetSize', 'surfacePixelRatio', 'setSurface',
  'setSurfacePixelRatio', 'setExternalRenderTargetSize', 'surfaceChanged',
  'externalRenderTargetSizeChanged', 'surfacePixelRatioChanged', 'd_func'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DRender::QRenderSurfaceSelector::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int
    Qt3DRender::QRenderSurfaceSelector::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DRender::QRenderSurfaceSelector::~QRenderSurfaceSelector()': the
    destructor: Python never removes a C++
    Qt3DRender::QRenderSurfaceSelector.
  - Qt's 'const QRenderSurfaceSelectorPrivate
    *Qt3DRender::QRenderSurfaceSelector::d_func() const': takes in Python
    what 'QRenderSurfaceSelectorPrivate
    *Qt3DRender::QRenderSurfaceSelector::d_func()' takes.
  - Qt's 'Qt3DRender::QRenderSurfaceSelector::QRenderSurfaceSelector(
    QRenderSurfaceSelectorPrivate &dd, Qt3DCore::QNode *parent)': takes a
    type Python has no way to hand over yet.

  What has no ritual
  ------------------

  2 of the 20 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DRender::QRenderSurfaceSelector is created at the first use,
    not by 'Qt3DRender::QRenderSurfaceSelector(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::QRenderSurfaceSelector.
  - Qt tells when it has removed the C++ Qt3DRender::QRenderSurfaceSelector.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
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
    Calls Qt's 'QString Qt3DRender::QRenderSurfaceSelector::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrendersurfaceselector.html#tr

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
    #  QString Qt3DRender::QRenderSurfaceSelector::tr(const char *s, const
    #      char *c, int n)
    return Rituals.call(
        'ritual_ZN10Qt3DRender22QRenderSurfaceSelector2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::QRenderSurfaceSelector'

  #  A C++ Qt3DRender::QRenderSurfaceSelector Python makes is of a C++ class
  #  of ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DRender_QRenderSurfaceSelector'

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
    *Qt3DRender::QRenderSurfaceSelector::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrendersurfaceselector.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DRender::QRenderSurfaceSelector::metaObject()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender22QRenderSurfaceSelector10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def surface(self) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *Qt3DRender::QRenderSurfaceSelector::surface()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrendersurfaceselector.html#surface

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *Qt3DRender::QRenderSurfaceSelector::surface() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender22QRenderSurfaceSelector7surfaceEv',
    )
    return QObject._cuteAt(address)

  def externalRenderTargetSize(self) -> QSize:
    """
    Calls Qt's 'QSize
    Qt3DRender::QRenderSurfaceSelector::externalRenderTargetSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrendersurfaceselector.html

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize Qt3DRender::QRenderSurfaceSelector::externalRenderTargetSize()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender22QRenderSurfaceSelector24externalRenderTarg'
        'etSizeEv',
    )
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def surfacePixelRatio(self) -> float:
    """
    Calls Qt's 'float Qt3DRender::QRenderSurfaceSelector::surfacePixelRatio()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrendersurfaceselector.html
    """
    #  float Qt3DRender::QRenderSurfaceSelector::surfacePixelRatio() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender22QRenderSurfaceSelector17surfacePixelRatioE'
        'v',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QObject)
  @overload(NoneType)
  def setSurface(self, surfaceObject: Optional[QObject]) -> None:
    """
    Calls Qt's 'void Qt3DRender::QRenderSurfaceSelector::setSurface(QObject
    *surfaceObject)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrendersurfaceselector.html#setSurface

    Parameters
    ----------

    surfaceObject : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::QRenderSurfaceSelector::setSurface(QObject
    #      *surfaceObject)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender22QRenderSurfaceSelector10setSurfaceEP7QObjec'
        't',
        self._addressOf(surfaceObject, 'QObject'),
    )

  @overload(float)
  def setSurfacePixelRatio(self, ratio: float) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QRenderSurfaceSelector::setSurfacePixelRatio(float ratio)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrendersurfaceselector.html

    Parameters
    ----------

    ratio : float
      Passed on as it is.
    """
    #  void Qt3DRender::QRenderSurfaceSelector::setSurfacePixelRatio(float
    #      ratio)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender22QRenderSurfaceSelector20setSurfacePixelRati'
        'oEf',
        ratio,
    )

  @overload(QSize)
  def setExternalRenderTargetSize(self, size: QSize) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QRenderSurfaceSelector::setExternalRenderTargetSize(const
    QSize &size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrendersurfaceselector.html

    Parameters
    ----------

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void Qt3DRender::QRenderSurfaceSelector::setExternalRenderTargetSize(
    #      const QSize &size)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender22QRenderSurfaceSelector27setExternalRenderTa'
        'rgetSizeERK5QSize',
        self._valueOf(size),
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
    'Qt3DRender::QRenderSurfaceSelector::QRenderSurfaceSelector(Qt3DCore::
    QNode *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrendersurfaceselector.html

    Parameters
    ----------

    parent : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DRender::QRenderSurfaceSelector::QRenderSurfaceSelector(
    #      Qt3DCore::QNode *parent)
    self._noteCreation(QRenderSurfaceSelector, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender22QRenderSurfaceSelectorC1EPN8Qt3DCore5QNodeE',
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

  @overload(QObject)
  @overload(NoneType)
  def surfaceChanged(self, surface: Optional[QObject]) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QRenderSurfaceSelector::surfaceChanged(QObject *surface)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrendersurfaceselector.html

    Parameters
    ----------

    surface : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::QRenderSurfaceSelector::surfaceChanged(QObject
    #      *surface)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender22QRenderSurfaceSelector14surfaceChangedEP7QO'
        'bject',
        self._addressOf(surface, 'QObject'),
    )

  @overload(QSize)
  def externalRenderTargetSizeChanged(self, size: QSize) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QRenderSurfaceSelector::externalRenderTargetSizeChanged(const
    QSize &size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrendersurfaceselector.html

    Parameters
    ----------

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void Qt3DRender::QRenderSurfaceSelector::
    #      externalRenderTargetSizeChanged(const QSize &size)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender22QRenderSurfaceSelector31externalRenderTarge'
        'tSizeChangedERK5QSize',
        self._valueOf(size),
    )

  @overload(float)
  def surfacePixelRatioChanged(self, ratio: float) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QRenderSurfaceSelector::surfacePixelRatioChanged(float
    ratio)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrendersurfaceselector.html

    Parameters
    ----------

    ratio : float
      Passed on as it is.
    """
    #  void
    #      Qt3DRender::QRenderSurfaceSelector::surfacePixelRatioChanged(float
    #      ratio)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender22QRenderSurfaceSelector24surfacePixelRatioCh'
        'angedEf',
        ratio,
    )

  def d_func(self) -> Optional[Qt3DRender.QRenderSurfaceSelectorPrivate]:
    """
    Calls Qt's 'QRenderSurfaceSelectorPrivate
    *Qt3DRender::QRenderSurfaceSelector::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrendersurfaceselector.html#d_func

    Returns
    -------

    Optional[Qt3DRender.QRenderSurfaceSelectorPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRenderSurfaceSelectorPrivate
    #      *Qt3DRender::QRenderSurfaceSelector::d_func()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DRender22QRenderSurfaceSelector6d_funcEv',
    )
    return Qt3DRender.QRenderSurfaceSelectorPrivate._cuteAt(address)
