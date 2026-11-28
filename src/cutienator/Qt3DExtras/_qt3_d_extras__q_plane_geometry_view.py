"""
Qt3DExtras::QPlaneGeometryView binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DExtras/qplanegeometryview.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore

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


class QPlaneGeometryView(Qt3DCore.QGeometryView):
  """
  The cute side of Qt's Qt3DExtras::QPlaneGeometryView: a plain Python object
  standing in front of one C++ Qt3DExtras::QPlaneGeometryView.

  It is built on the cute 'Qt3DCore::QGeometryView', as Qt's
  Qt3DExtras::QPlaneGeometryView is built on Qt's Qt3DCore::QGeometryView,
  and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DExtras::QPlaneGeometryView that has a ritual and
  that Python can call so far, 14 names in all: 'metaObject', 'tr', 'width',
  'height', 'meshResolution', 'mirrored', 'setWidth', 'setHeight',
  'setMeshResolution', 'setMirrored', 'meshResolutionChanged',
  'widthChanged', 'heightChanged', 'mirroredChanged'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DExtras::QPlaneGeometryView::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int Qt3DExtras::QPlaneGeometryView::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DExtras::QPlaneGeometryView::~QPlaneGeometryView()': the
    destructor: Python never removes a C++ Qt3DExtras::QPlaneGeometryView.

  What has no ritual
  ------------------

  10 of the 28 functions Qt declares: 10 not a gap.

  What to expect
  --------------

  - The C++ Qt3DExtras::QPlaneGeometryView is created at the first use, not
    by 'Qt3DExtras::QPlaneGeometryView(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DExtras::QPlaneGeometryView.
  - Qt tells when it has removed the C++ Qt3DExtras::QPlaneGeometryView.
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
    Calls Qt's 'QString Qt3DExtras::QPlaneGeometryView::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qplanegeometryview.html#tr

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
    #  QString Qt3DExtras::QPlaneGeometryView::tr(const char *s, const char
    #      *c, int n)
    return Rituals.call(
        'ritual_ZN10Qt3DExtras18QPlaneGeometryView2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DExtras::QPlaneGeometryView'

  #  A C++ Qt3DExtras::QPlaneGeometryView Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DExtras_QPlaneGeometryView'

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
    *Qt3DExtras::QPlaneGeometryView::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qplanegeometryview.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DExtras::QPlaneGeometryView::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DExtras18QPlaneGeometryView10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def width(self) -> float:
    """
    Calls Qt's 'float Qt3DExtras::QPlaneGeometryView::width() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qplanegeometryview.html#width
    """
    #  float Qt3DExtras::QPlaneGeometryView::width() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DExtras18QPlaneGeometryView5widthEv',
    )

  def height(self) -> float:
    """
    Calls Qt's 'float Qt3DExtras::QPlaneGeometryView::height() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qplanegeometryview.html#height
    """
    #  float Qt3DExtras::QPlaneGeometryView::height() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DExtras18QPlaneGeometryView6heightEv',
    )

  def meshResolution(self) -> QSize:
    """
    Calls Qt's 'QSize Qt3DExtras::QPlaneGeometryView::meshResolution()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qplanegeometryview.html#meshResolution

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize Qt3DExtras::QPlaneGeometryView::meshResolution() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DExtras18QPlaneGeometryView14meshResolutionEv',
    )
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def mirrored(self) -> bool:
    """
    Calls Qt's 'bool Qt3DExtras::QPlaneGeometryView::mirrored() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qplanegeometryview.html#mirrored
    """
    #  bool Qt3DExtras::QPlaneGeometryView::mirrored() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DExtras18QPlaneGeometryView8mirroredEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setWidth(self, width: float) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QPlaneGeometryView::setWidth(float width)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qplanegeometryview.html#setWidth

    Parameters
    ----------

    width : float
      Passed on as it is.
    """
    #  void Qt3DExtras::QPlaneGeometryView::setWidth(float width)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras18QPlaneGeometryView8setWidthEf', width,
    )

  @overload(float)
  def setHeight(self, height: float) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QPlaneGeometryView::setHeight(float
    height)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qplanegeometryview.html#setHeight

    Parameters
    ----------

    height : float
      Passed on as it is.
    """
    #  void Qt3DExtras::QPlaneGeometryView::setHeight(float height)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras18QPlaneGeometryView9setHeightEf', height,
    )

  @overload(QSize)
  def setMeshResolution(self, resolution: QSize) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QPlaneGeometryView::setMeshResolution(const
    QSize &resolution)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qplanegeometryview.html

    Parameters
    ----------

    resolution : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void Qt3DExtras::QPlaneGeometryView::setMeshResolution(const QSize
    #      &resolution)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras18QPlaneGeometryView17setMeshResolutionERK5QS'
        'ize',
        self._valueOf(resolution),
    )

  @overload(bool)
  def setMirrored(self, mirrored: bool) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QPlaneGeometryView::setMirrored(bool
    mirrored)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qplanegeometryview.html#setMirrored

    Parameters
    ----------

    mirrored : bool
      Passed on as it is.
    """
    #  void Qt3DExtras::QPlaneGeometryView::setMirrored(bool mirrored)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras18QPlaneGeometryView11setMirroredEb', mirrored,
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
    'Qt3DExtras::QPlaneGeometryView::QPlaneGeometryView(Qt3DCore::QNode
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qplanegeometryview.html

    Parameters
    ----------

    parent : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DExtras::QPlaneGeometryView::QPlaneGeometryView(Qt3DCore::QNode
    #      *parent)
    self._noteCreation(QPlaneGeometryView, lambda: Rituals.call(
        'ritual_ZN10Qt3DExtras18QPlaneGeometryViewC1EPN8Qt3DCore5QNodeE',
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

  @overload(QSize)
  def meshResolutionChanged(self, meshResolution: QSize) -> None:
    """
    Calls Qt's 'void
    Qt3DExtras::QPlaneGeometryView::meshResolutionChanged(const QSize
    &meshResolution)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qplanegeometryview.html

    Parameters
    ----------

    meshResolution : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void Qt3DExtras::QPlaneGeometryView::meshResolutionChanged(const QSize
    #      &meshResolution)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras18QPlaneGeometryView21meshResolutionChangedER'
        'K5QSize',
        self._valueOf(meshResolution),
    )

  @overload(float)
  def widthChanged(self, width: float) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QPlaneGeometryView::widthChanged(float
    width)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qplanegeometryview.html#widthChanged

    Parameters
    ----------

    width : float
      Passed on as it is.
    """
    #  void Qt3DExtras::QPlaneGeometryView::widthChanged(float width)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras18QPlaneGeometryView12widthChangedEf', width,
    )

  @overload(float)
  def heightChanged(self, height: float) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QPlaneGeometryView::heightChanged(float
    height)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qplanegeometryview.html#heightChanged

    Parameters
    ----------

    height : float
      Passed on as it is.
    """
    #  void Qt3DExtras::QPlaneGeometryView::heightChanged(float height)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras18QPlaneGeometryView13heightChangedEf', height,
    )

  @overload(bool)
  def mirroredChanged(self, mirrored: bool) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QPlaneGeometryView::mirroredChanged(bool
    mirrored)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qplanegeometryview.html#mirroredChanged

    Parameters
    ----------

    mirrored : bool
      Passed on as it is.
    """
    #  void Qt3DExtras::QPlaneGeometryView::mirroredChanged(bool mirrored)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras18QPlaneGeometryView15mirroredChangedEb',
        mirrored,
    )
