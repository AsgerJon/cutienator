"""
QWaylandOutput binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWaylandCompositor/qwaylandoutput.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QList
from . import QWaylandObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QEvent, QMetaObject, QPoint, QRect, QSize
  from ..QtGui import QWindow
  from . import QWaylandCompositor, QWaylandOutputMode, QWaylandSurface
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEvent = WAIT['QEvent']
  QPoint = WAIT['QPoint']
  QRect = WAIT['QRect']
  QSize = WAIT['QSize']
  QWaylandCompositor = WAIT['QWaylandCompositor']
  QWaylandOutputMode = WAIT['QWaylandOutputMode']
  QWaylandSurface = WAIT['QWaylandSurface']
  QWindow = WAIT['QWindow']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QWaylandOutput(QWaylandObject):
  """
  The cute side of Qt's QWaylandOutput: a plain Python object standing in
  front of one C++ QWaylandOutput.

  It is built on the cute 'QWaylandObject', as Qt's QWaylandOutput is built
  on Qt's QWaylandObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QWaylandOutput that has a ritual and that Python can
  call so far, 50 names in all: 'metaObject', 'tr', 'compositor',
  'setCompositor', 'window', 'setWindow', 'manufacturer', 'setManufacturer',
  'model', 'setModel', 'position', 'setPosition', 'modes', 'addMode',
  'currentMode', 'setCurrentMode', 'geometry', 'availableGeometry',
  'setAvailableGeometry', 'physicalSize', 'setPhysicalSize', 'subpixel',
  'transform', 'scaleFactor', 'setScaleFactor', 'sizeFollowsWindow',
  'setSizeFollowsWindow', 'frameStarted', 'sendFrameCallbacks',
  'surfaceEnter', 'surfaceLeave', 'update', 'compositorChanged',
  'windowChanged', 'positionChanged', 'geometryChanged', 'modeAdded',
  'currentModeChanged', 'availableGeometryChanged', 'physicalSizeChanged',
  'scaleFactorChanged', 'subpixelChanged', 'transformChanged',
  'sizeFollowsWindowChanged', 'physicalSizeFollowsSizeChanged',
  'manufacturerChanged', 'modelChanged', 'windowDestroyed', 'event',
  'initialize'. It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QWaylandOutput::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QWaylandOutput::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QWaylandOutputPrivate *QWaylandOutput::d_func()': gives
    'QWaylandOutputPrivate', which has no cute class yet.
  - Qt's 'const QWaylandOutputPrivate *QWaylandOutput::d_func() const': gives
    'QWaylandOutputPrivate', which has no cute class yet.
  - Qt's 'void QWaylandOutput::qt_qmlMarker_uncreatable()': one of Qt's own
    inner workings.
  - Qt's 'QWaylandOutput::~QWaylandOutput()': the destructor: Python never
    removes a C++ QWaylandOutput.
  - Qt's 'QWaylandOutput *QWaylandOutput::fromResource(wl_resource
    *resource)': names 'wl_resource', which has no cute class yet.
  - Qt's 'struct ::wl_resource
    *QWaylandOutput::resourceForClient(QWaylandClient *client) const': gives
    'struct ::wl_resource', which has no cute class yet.
  - Qt's 'void QWaylandOutput::setSubpixel(const Subpixel &subpixel)': takes
    a type Python has no way to hand over yet.
  - Qt's 'void QWaylandOutput::setTransform(const Transform &transform)':
    takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  4 of the 66 functions Qt declares: 2 not a gap; 2 cannot be called and
  cannot be called through the meta-object and cannot be copied.

  What to expect
  --------------

  - The C++ QWaylandOutput is created at the first use, not by
    'QWaylandOutput(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QWaylandOutput.
  - Qt tells when it has removed the C++ QWaylandOutput. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QWaylandOutput that has no cute function yet,
    'fromResource', 'physicalSizeFollowsSize', 'resourceForClient',
    'setPhysicalSizeFollowsSize', 'setSubpixel', 'setTransform', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QWaylandOutput, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class Subpixel(CuteNum):
    """
    The enum 'QWaylandOutput::Subpixel' of Qt, with the 6 names Qt gives in
    it.
    """

    SubpixelUnknown = Kee[int](0)
    SubpixelNone = Kee[int](1)
    SubpixelHorizontalRgb = Kee[int](2)
    SubpixelHorizontalBgr = Kee[int](3)
    SubpixelVerticalRgb = Kee[int](4)
    SubpixelVerticalBgr = Kee[int](5)

  class Transform(CuteNum):
    """
    The enum 'QWaylandOutput::Transform' of Qt, with the 8 names Qt gives in
    it.
    """

    TransformNormal = Kee[int](0)
    Transform90 = Kee[int](1)
    Transform180 = Kee[int](2)
    Transform270 = Kee[int](3)
    TransformFlipped = Kee[int](4)
    TransformFlipped90 = Kee[int](5)
    TransformFlipped180 = Kee[int](6)
    TransformFlipped270 = Kee[int](7)

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
    Calls Qt's 'QString QWaylandOutput::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandoutput.html#tr

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
    #  QString QWaylandOutput::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN14QWaylandOutput2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWaylandOutput'

  #  A C++ QWaylandOutput Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QWaylandOutput'

  #  The functions Qt calls itself that QWaylandOutput is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'update': (
          ('_ZN14QWaylandOutput6updateEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'initialize': (
          ('_ZN14QWaylandOutput10initializeEv',
           ('nothing', 'nothing', ''),
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

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QWaylandOutput::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandoutput.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QWaylandOutput::metaObject() const
    address = self.uglySide.call('ritual_ZNK14QWaylandOutput10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def compositor(self) -> Optional[QWaylandCompositor]:
    """
    Calls Qt's 'QWaylandCompositor *QWaylandOutput::compositor() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandoutput.html#compositor

    Returns
    -------

    Optional[QWaylandCompositor]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWaylandCompositor *QWaylandOutput::compositor() const
    address = self.uglySide.call('ritual_ZNK14QWaylandOutput10compositorEv')
    from . import QWaylandCompositor
    return QWaylandCompositor._cuteAt(address)

  def window(self) -> Optional[QWindow]:
    """
    Calls Qt's 'QWindow *QWaylandOutput::window() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandoutput.html#window

    Returns
    -------

    Optional[QWindow]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWindow *QWaylandOutput::window() const
    address = self.uglySide.call('ritual_ZNK14QWaylandOutput6windowEv')
    from ..QtGui import QWindow
    return QWindow._cuteAt(address)

  def manufacturer(self) -> str:
    """
    Calls Qt's 'QString QWaylandOutput::manufacturer() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandoutput.html#manufacturer

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWaylandOutput::manufacturer() const
    return self.uglySide.call('ritual_ZNK14QWaylandOutput12manufacturerEv')

  def model(self) -> str:
    """
    Calls Qt's 'QString QWaylandOutput::model() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandoutput.html#model

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWaylandOutput::model() const
    return self.uglySide.call('ritual_ZNK14QWaylandOutput5modelEv')

  def position(self) -> QPoint:
    """
    Calls Qt's 'QPoint QWaylandOutput::position() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandoutput.html#position

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint QWaylandOutput::position() const
    address = self.uglySide.call('ritual_ZNK14QWaylandOutput8positionEv')
    from ..QtCore import QPoint
    return QPoint._cuteOwning(address)

  def modes(self) -> QList[QWaylandOutputMode]:
    """
    Calls Qt's 'QList<QWaylandOutputMode> QWaylandOutput::modes() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandoutput.html#modes

    Returns
    -------

    QList[QWaylandOutputMode]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QWaylandOutputMode> QWaylandOutput::modes() const
    address = self.uglySide.call('ritual_ZNK14QWaylandOutput5modesEv')
    from . import QWaylandOutputMode
    return QList[QWaylandOutputMode]._cuteOwning(address)

  def currentMode(self) -> QWaylandOutputMode:
    """
    Calls Qt's 'QWaylandOutputMode QWaylandOutput::currentMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandoutput.html#currentMode

    Returns
    -------

    QWaylandOutputMode
      A new cute QWaylandOutputMode around the copy Qt gave back. Python owns
      it.
    """
    #  QWaylandOutputMode QWaylandOutput::currentMode() const
    address = self.uglySide.call('ritual_ZNK14QWaylandOutput11currentModeEv')
    from . import QWaylandOutputMode
    return QWaylandOutputMode._cuteOwning(address)

  def geometry(self) -> QRect:
    """
    Calls Qt's 'QRect QWaylandOutput::geometry() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandoutput.html#geometry

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QWaylandOutput::geometry() const
    address = self.uglySide.call('ritual_ZNK14QWaylandOutput8geometryEv')
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  def availableGeometry(self) -> QRect:
    """
    Calls Qt's 'QRect QWaylandOutput::availableGeometry() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandoutput.html#availableGeometry

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QWaylandOutput::availableGeometry() const
    address = self.uglySide.call(
        'ritual_ZNK14QWaylandOutput17availableGeometryEv',
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  def physicalSize(self) -> QSize:
    """
    Calls Qt's 'QSize QWaylandOutput::physicalSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandoutput.html#physicalSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QWaylandOutput::physicalSize() const
    address = self.uglySide.call(
        'ritual_ZNK14QWaylandOutput12physicalSizeEv',
    )
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def subpixel(self) -> Subpixel:
    """
    Calls Qt's 'Subpixel QWaylandOutput::subpixel() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandoutput.html#subpixel

    Returns
    -------

    Subpixel
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Subpixel(number)' gives.
    """
    #  Subpixel QWaylandOutput::subpixel() const
    return QWaylandOutput.Subpixel(self.uglySide.call(
        'ritual_ZNK14QWaylandOutput8subpixelEv',
    ))

  def transform(self) -> Transform:
    """
    Calls Qt's 'Transform QWaylandOutput::transform() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandoutput.html#transform

    Returns
    -------

    Transform
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Transform(number)' gives.
    """
    #  Transform QWaylandOutput::transform() const
    return QWaylandOutput.Transform(self.uglySide.call(
        'ritual_ZNK14QWaylandOutput9transformEv',
    ))

  def scaleFactor(self) -> int:
    """
    Calls Qt's 'int QWaylandOutput::scaleFactor() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandoutput.html#scaleFactor
    """
    #  int QWaylandOutput::scaleFactor() const
    return self.uglySide.call('ritual_ZNK14QWaylandOutput11scaleFactorEv')

  def sizeFollowsWindow(self) -> bool:
    """
    Calls Qt's 'bool QWaylandOutput::sizeFollowsWindow() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandoutput.html#sizeFollowsWindow
    """
    #  bool QWaylandOutput::sizeFollowsWindow() const
    return self.uglySide.call(
        'ritual_ZNK14QWaylandOutput17sizeFollowsWindowEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QWaylandCompositor)
  @overload(NoneType)
  def setCompositor(self, compositor: Optional[QWaylandCompositor]) -> None:
    """
    Calls Qt's 'void QWaylandOutput::setCompositor(QWaylandCompositor
    *compositor)'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandoutput.html#setCompositor

    Parameters
    ----------

    compositor : Optional[QWaylandCompositor]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWaylandOutput::setCompositor(QWaylandCompositor *compositor)
    self.uglySide.call(
        'ritual_ZN14QWaylandOutput13setCompositorEP18QWaylandCompositor',
        self._addressOf(compositor),
    )

  @overload(QWindow)
  @overload(NoneType)
  def setWindow(self, window: Optional[QWindow]) -> None:
    """
    Calls Qt's 'void QWaylandOutput::setWindow(QWindow *window)'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandoutput.html#setWindow

    Parameters
    ----------

    window : Optional[QWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWaylandOutput::setWindow(QWindow *window)
    self.uglySide.call(
        'ritual_ZN14QWaylandOutput9setWindowEP7QWindow',
        self._addressOf(window),
    )

  @overload(str)
  def setManufacturer(self, manufacturer: str) -> None:
    """
    Calls Qt's 'void QWaylandOutput::setManufacturer(const QString
    &manufacturer)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandoutput.html#setManufacturer

    Parameters
    ----------

    manufacturer : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QWaylandOutput::setManufacturer(const QString &manufacturer)
    self.uglySide.call(
        'ritual_ZN14QWaylandOutput15setManufacturerERK7QString',
        manufacturer,
    )

  @overload(str)
  def setModel(self, model: str) -> None:
    """
    Calls Qt's 'void QWaylandOutput::setModel(const QString &model)'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandoutput.html#setModel

    Parameters
    ----------

    model : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QWaylandOutput::setModel(const QString &model)
    self.uglySide.call(
        'ritual_ZN14QWaylandOutput8setModelERK7QString', model,
    )

  @overload(QPoint)
  def setPosition(self, pt: QPoint) -> None:
    """
    Calls Qt's 'void QWaylandOutput::setPosition(const QPoint &pt)'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandoutput.html#setPosition

    Parameters
    ----------

    pt : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void QWaylandOutput::setPosition(const QPoint &pt)
    self.uglySide.call(
        'ritual_ZN14QWaylandOutput11setPositionERK6QPoint',
        self._valueOf(pt),
    )

  @overload(QWaylandOutputMode)
  def setCurrentMode(self, mode: QWaylandOutputMode) -> None:
    """
    Calls Qt's 'void QWaylandOutput::setCurrentMode(const QWaylandOutputMode
    &mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandoutput.html#setCurrentMode

    Parameters
    ----------

    mode : QWaylandOutputMode
      Passed on as a value: Qt reads the C++ QWaylandOutputMode, which stays
      Python's own.
    """
    #  void QWaylandOutput::setCurrentMode(const QWaylandOutputMode &mode)
    self.uglySide.call(
        'ritual_ZN14QWaylandOutput14setCurrentModeERK18QWaylandOutputMode',
        self._valueOf(mode),
    )

  @overload(QRect)
  def setAvailableGeometry(self, availableGeometry: QRect) -> None:
    """
    Calls Qt's 'void QWaylandOutput::setAvailableGeometry(const QRect
    &availableGeometry)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandoutput.html#setAvailableGeometry

    Parameters
    ----------

    availableGeometry : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
    """
    #  void QWaylandOutput::setAvailableGeometry(const QRect
    #      &availableGeometry)
    self.uglySide.call(
        'ritual_ZN14QWaylandOutput20setAvailableGeometryERK5QRect',
        self._valueOf(availableGeometry),
    )

  @overload(QSize)
  def setPhysicalSize(self, size: QSize) -> None:
    """
    Calls Qt's 'void QWaylandOutput::setPhysicalSize(const QSize &size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandoutput.html#setPhysicalSize

    Parameters
    ----------

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void QWaylandOutput::setPhysicalSize(const QSize &size)
    self.uglySide.call(
        'ritual_ZN14QWaylandOutput15setPhysicalSizeERK5QSize',
        self._valueOf(size),
    )

  @overload(int)
  def setScaleFactor(self, scale: int) -> None:
    """
    Calls Qt's 'void QWaylandOutput::setScaleFactor(int scale)'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandoutput.html#setScaleFactor

    Parameters
    ----------

    scale : int
      Passed on as it is.
    """
    #  void QWaylandOutput::setScaleFactor(int scale)
    self.uglySide.call('ritual_ZN14QWaylandOutput14setScaleFactorEi', scale)

  @overload(bool)
  def setSizeFollowsWindow(self, follow: bool) -> None:
    """
    Calls Qt's 'void QWaylandOutput::setSizeFollowsWindow(bool follow)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandoutput.html#setSizeFollowsWindow

    Parameters
    ----------

    follow : bool
      Passed on as it is.
    """
    #  void QWaylandOutput::setSizeFollowsWindow(bool follow)
    self.uglySide.call(
        'ritual_ZN14QWaylandOutput20setSizeFollowsWindowEb', follow,
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
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QWaylandOutput::QWaylandOutput()', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandoutput.html#QWaylandOutput
    """
    #  QWaylandOutput::QWaylandOutput()
    self._noteCreation(QWaylandOutput, lambda: Rituals.call(
        'ritual_ZN14QWaylandOutputC1Ev',
    ))

  @overload(QWaylandCompositor, QWindow)
  @overload(QWaylandCompositor, NoneType)
  @overload(NoneType, QWindow)
  @overload(NoneType, NoneType)
  def __init__(
      self,
      compositor: Optional[QWaylandCompositor],
      window: Optional[QWindow],
  ) -> None:
    """
    Notes what was given, for Qt's
    'QWaylandOutput::QWaylandOutput(QWaylandCompositor *compositor, QWindow
    *window)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandoutput.html#QWaylandOutput

    Parameters
    ----------

    compositor : Optional[QWaylandCompositor]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    window : Optional[QWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QWaylandOutput::QWaylandOutput(QWaylandCompositor *compositor, QWindow
    #      *window)
    self._noteCreation(QWaylandOutput, lambda: Rituals.call(
        'ritual_ZN14QWaylandOutputC1EP18QWaylandCompositorP7QWindow',
        self._addressOf(compositor), self._addressOf(window),
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

  @overload(QWaylandOutputMode)
  @overload(QWaylandOutputMode, bool)
  def addMode(
      self,
      mode: QWaylandOutputMode,
      preferred: bool = False,
  ) -> None:
    """
    Calls Qt's 'void QWaylandOutput::addMode(const QWaylandOutputMode &mode,
    bool preferred)'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandoutput.html#addMode

    Parameters
    ----------

    mode : QWaylandOutputMode
      Passed on as a value: Qt reads the C++ QWaylandOutputMode, which stays
      Python's own.

    preferred : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QWaylandOutput::addMode(const QWaylandOutputMode &mode, bool
    #      preferred)
    self.uglySide.call(
        'ritual_ZN14QWaylandOutput7addModeERK18QWaylandOutputModeb',
        self._valueOf(mode), preferred,
    )

  def frameStarted(self) -> None:
    """
    Calls Qt's 'void QWaylandOutput::frameStarted()'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandoutput.html#frameStarted
    """
    #  void QWaylandOutput::frameStarted()
    self.uglySide.call('ritual_ZN14QWaylandOutput12frameStartedEv')

  def sendFrameCallbacks(self) -> None:
    """
    Calls Qt's 'void QWaylandOutput::sendFrameCallbacks()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandoutput.html#sendFrameCallbacks
    """
    #  void QWaylandOutput::sendFrameCallbacks()
    self.uglySide.call('ritual_ZN14QWaylandOutput18sendFrameCallbacksEv')

  @overload(QWaylandSurface)
  @overload(NoneType)
  def surfaceEnter(self, surface: Optional[QWaylandSurface]) -> None:
    """
    Calls Qt's 'void QWaylandOutput::surfaceEnter(QWaylandSurface *surface)'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandoutput.html#surfaceEnter

    Parameters
    ----------

    surface : Optional[QWaylandSurface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWaylandOutput::surfaceEnter(QWaylandSurface *surface)
    self.uglySide.call(
        'ritual_ZN14QWaylandOutput12surfaceEnterEP15QWaylandSurface',
        self._addressOf(surface),
    )

  @overload(QWaylandSurface)
  @overload(NoneType)
  def surfaceLeave(self, surface: Optional[QWaylandSurface]) -> None:
    """
    Calls Qt's 'void QWaylandOutput::surfaceLeave(QWaylandSurface *surface)'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandoutput.html#surfaceLeave

    Parameters
    ----------

    surface : Optional[QWaylandSurface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWaylandOutput::surfaceLeave(QWaylandSurface *surface)
    self.uglySide.call(
        'ritual_ZN14QWaylandOutput12surfaceLeaveEP15QWaylandSurface',
        self._addressOf(surface),
    )

  def update(self) -> None:
    """
    Calls Qt's 'void QWaylandOutput::update()'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandoutput.html#update
    """
    #  void QWaylandOutput::update()
    ritual = 'ritual_ZN14QWaylandOutput6updateEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QWaylandOutput6updateEv'
    self.uglySide.call(ritual)

  def compositorChanged(self) -> None:
    """
    Calls Qt's 'void QWaylandOutput::compositorChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandoutput.html#compositorChanged
    """
    #  void QWaylandOutput::compositorChanged()
    self.uglySide.call('ritual_ZN14QWaylandOutput17compositorChangedEv')

  def windowChanged(self) -> None:
    """
    Calls Qt's 'void QWaylandOutput::windowChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandoutput.html#windowChanged
    """
    #  void QWaylandOutput::windowChanged()
    self.uglySide.call('ritual_ZN14QWaylandOutput13windowChangedEv')

  def positionChanged(self) -> None:
    """
    Calls Qt's 'void QWaylandOutput::positionChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandoutput.html#positionChanged
    """
    #  void QWaylandOutput::positionChanged()
    self.uglySide.call('ritual_ZN14QWaylandOutput15positionChangedEv')

  def geometryChanged(self) -> None:
    """
    Calls Qt's 'void QWaylandOutput::geometryChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandoutput.html#geometryChanged
    """
    #  void QWaylandOutput::geometryChanged()
    self.uglySide.call('ritual_ZN14QWaylandOutput15geometryChangedEv')

  def modeAdded(self) -> None:
    """
    Calls Qt's 'void QWaylandOutput::modeAdded()'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandoutput.html#modeAdded
    """
    #  void QWaylandOutput::modeAdded()
    self.uglySide.call('ritual_ZN14QWaylandOutput9modeAddedEv')

  def currentModeChanged(self) -> None:
    """
    Calls Qt's 'void QWaylandOutput::currentModeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandoutput.html#currentModeChanged
    """
    #  void QWaylandOutput::currentModeChanged()
    self.uglySide.call('ritual_ZN14QWaylandOutput18currentModeChangedEv')

  def availableGeometryChanged(self) -> None:
    """
    Calls Qt's 'void QWaylandOutput::availableGeometryChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandoutput.html#availableGeometryChanged
    """
    #  void QWaylandOutput::availableGeometryChanged()
    self.uglySide.call(
        'ritual_ZN14QWaylandOutput24availableGeometryChangedEv',
    )

  def physicalSizeChanged(self) -> None:
    """
    Calls Qt's 'void QWaylandOutput::physicalSizeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandoutput.html#physicalSizeChanged
    """
    #  void QWaylandOutput::physicalSizeChanged()
    self.uglySide.call('ritual_ZN14QWaylandOutput19physicalSizeChangedEv')

  def scaleFactorChanged(self) -> None:
    """
    Calls Qt's 'void QWaylandOutput::scaleFactorChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandoutput.html#scaleFactorChanged
    """
    #  void QWaylandOutput::scaleFactorChanged()
    self.uglySide.call('ritual_ZN14QWaylandOutput18scaleFactorChangedEv')

  def subpixelChanged(self) -> None:
    """
    Calls Qt's 'void QWaylandOutput::subpixelChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandoutput.html#subpixelChanged
    """
    #  void QWaylandOutput::subpixelChanged()
    self.uglySide.call('ritual_ZN14QWaylandOutput15subpixelChangedEv')

  def transformChanged(self) -> None:
    """
    Calls Qt's 'void QWaylandOutput::transformChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandoutput.html#transformChanged
    """
    #  void QWaylandOutput::transformChanged()
    self.uglySide.call('ritual_ZN14QWaylandOutput16transformChangedEv')

  def sizeFollowsWindowChanged(self) -> None:
    """
    Calls Qt's 'void QWaylandOutput::sizeFollowsWindowChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandoutput.html#sizeFollowsWindowChanged
    """
    #  void QWaylandOutput::sizeFollowsWindowChanged()
    self.uglySide.call(
        'ritual_ZN14QWaylandOutput24sizeFollowsWindowChangedEv',
    )

  def physicalSizeFollowsSizeChanged(self) -> None:
    """
    Calls Qt's 'void QWaylandOutput::physicalSizeFollowsSizeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandoutput.html#physicalSizeFollowsSizeChanged
    """
    #  void QWaylandOutput::physicalSizeFollowsSizeChanged()
    self.uglySide.call(
        'ritual_ZN14QWaylandOutput30physicalSizeFollowsSizeChangedEv',
    )

  def manufacturerChanged(self) -> None:
    """
    Calls Qt's 'void QWaylandOutput::manufacturerChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandoutput.html#manufacturerChanged
    """
    #  void QWaylandOutput::manufacturerChanged()
    self.uglySide.call('ritual_ZN14QWaylandOutput19manufacturerChangedEv')

  def modelChanged(self) -> None:
    """
    Calls Qt's 'void QWaylandOutput::modelChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandoutput.html#modelChanged
    """
    #  void QWaylandOutput::modelChanged()
    self.uglySide.call('ritual_ZN14QWaylandOutput12modelChangedEv')

  def windowDestroyed(self) -> None:
    """
    Calls Qt's 'void QWaylandOutput::windowDestroyed()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandoutput.html#windowDestroyed
    """
    #  void QWaylandOutput::windowDestroyed()
    self.uglySide.call('ritual_ZN14QWaylandOutput15windowDestroyedEv')

  @overload(QEvent)
  @overload(NoneType)
  def event(self, event: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QWaylandOutput::event(QEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandoutput.html#event

    Parameters
    ----------

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QWaylandOutput::event(QEvent *event)
    ritual = 'ritual_ZN14QWaylandOutput5eventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QWaylandOutput5eventEP6QEvent'
    return self.uglySide.call(ritual, self._addressOf(event))

  def initialize(self) -> None:
    """
    Calls Qt's 'void QWaylandOutput::initialize()'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandoutput.html#initialize
    """
    #  void QWaylandOutput::initialize()
    ritual = 'ritual_ZN14QWaylandOutput10initializeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QWaylandOutput10initializeEv'
    self.uglySide.call(ritual)

  @staticmethod
  def fromResource(*__, **_) -> Never:
    """
    Qt's 'QWaylandOutput *QWaylandOutput::fromResource(wl_resource
    *resource)': names 'wl_resource', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QWaylandOutput.fromResource' has no cute function yet. Qt's "
        "'QWaylandOutput *QWaylandOutput::fromResource(wl_resource "
        "*resource)': names 'wl_resource', which has no cute class yet.")

  @staticmethod
  def physicalSizeFollowsSize(*__, **_) -> Never:
    """
    Qt's 'bool QWaylandOutput::physicalSizeFollowsSize() const': cannot be
    called and cannot be called through the meta-object and cannot be copied:
    no header file has its code, Qt's source does not mark it or its class
    for use from outside Qt or writes it 'inline' or nowhere, and it is no
    signal, slot or invokable function giving back nothing, of a class built
    on QObject, and Qt's source has no code for it that could be told from
    the rest.
    """
    raise NotImplementedError(
        "'QWaylandOutput.physicalSizeFollowsSize' has no cute function yet. "
        "Qt's 'bool QWaylandOutput::physicalSizeFollowsSize() const': "
        "cannot be called and cannot be called through the meta-object and "
        "cannot be copied: no header file has its code, Qt's source does "
        "not mark it or its class for use from outside Qt or writes it "
        "'inline' or nowhere, and it is no signal, slot or invokable "
        "function giving back nothing, of a class built on QObject, and "
        "Qt's source has no code for it that could be told from the rest.")

  @staticmethod
  def resourceForClient(*__, **_) -> Never:
    """
    Qt's 'struct ::wl_resource
    *QWaylandOutput::resourceForClient(QWaylandClient *client) const': gives
    'struct ::wl_resource', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QWaylandOutput.resourceForClient' has no cute function yet. Qt's "
        "'struct ::wl_resource "
        "*QWaylandOutput::resourceForClient(QWaylandClient *client) const': "
        "gives 'struct ::wl_resource', which has no cute class yet.")

  @staticmethod
  def setPhysicalSizeFollowsSize(*__, **_) -> Never:
    """
    Qt's 'void QWaylandOutput::setPhysicalSizeFollowsSize(bool follow)':
    cannot be called and cannot be called through the meta-object and cannot
    be copied: no header file has its code, Qt's source does not mark it or
    its class for use from outside Qt or writes it 'inline' or nowhere, and
    it is no signal, slot or invokable function giving back nothing, of a
    class built on QObject, and Qt's source has no code for it that could be
    told from the rest.
    """
    raise NotImplementedError(
        "'QWaylandOutput.setPhysicalSizeFollowsSize' has no cute function "
        "yet. Qt's 'void QWaylandOutput::setPhysicalSizeFollowsSize(bool "
        "follow)': cannot be called and cannot be called through the "
        "meta-object and cannot be copied: no header file has its code, "
        "Qt's source does not mark it or its class for use from outside Qt "
        "or writes it 'inline' or nowhere, and it is no signal, slot or "
        "invokable function giving back nothing, of a class built on "
        "QObject, and Qt's source has no code for it that could be told "
        "from the rest.")

  @staticmethod
  def setSubpixel(*__, **_) -> Never:
    """
    Qt's 'void QWaylandOutput::setSubpixel(const Subpixel &subpixel)': takes
    a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QWaylandOutput.setSubpixel' has no cute function yet. Qt's 'void "
        "QWaylandOutput::setSubpixel(const Subpixel &subpixel)': takes a "
        "type Python has no way to hand over yet.")

  @staticmethod
  def setTransform(*__, **_) -> Never:
    """
    Qt's 'void QWaylandOutput::setTransform(const Transform &transform)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QWaylandOutput.setTransform' has no cute function yet. Qt's 'void "
        "QWaylandOutput::setTransform(const Transform &transform)': takes a "
        "type Python has no way to hand over yet.")


#  Qt's 'QList<QWaylandOutput *>': the list of QWaylandOutput, which
#  'QList[QWaylandOutput]' gives. It is made here, so that there is one as
#  soon as there can be a QWaylandOutput.
QList.createKind(
    QWaylandOutput, 'address',
    make='ritual_list_make_QWaylandOutput_ptr',
    add='ritual_list_add_QWaylandOutput_ptr',
    size='ritual_list_size_QWaylandOutput_ptr',
    at='ritual_list_at_QWaylandOutput_ptr',
    drop='ritual_list_drop_QWaylandOutput_ptr',
)
