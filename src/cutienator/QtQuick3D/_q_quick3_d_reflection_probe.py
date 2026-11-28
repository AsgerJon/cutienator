"""
QQuick3DReflectionProbe binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3D/6.12.0/QtQuick3D/private/qquick3dreflectionprobe_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQuick3DReflectionProbe to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from . import QQuick3DNode, QQuick3DObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QColor, QVector3D
  from ..QtQuick3DRuntimeRender import QSSGRenderGraphObject
  from . import QQuick3DCubeMapTexture, QQuick3DSceneManager
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']
  QQuick3DCubeMapTexture = WAIT['QQuick3DCubeMapTexture']
  QQuick3DSceneManager = WAIT['QQuick3DSceneManager']
  QSSGRenderGraphObject = WAIT['QSSGRenderGraphObject']
  QVector3D = WAIT['QVector3D']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuick3DReflectionProbe(QQuick3DNode):
  """
  The cute side of Qt's QQuick3DReflectionProbe: a plain Python object
  standing in front of one C++ QQuick3DReflectionProbe.

  It is built on the cute 'QQuick3DNode', as Qt's QQuick3DReflectionProbe is
  built on Qt's QQuick3DNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuick3DReflectionProbe that has a ritual and that
  Python can call so far, 38 names in all: 'metaObject', 'tr', 'quality',
  'clearColor', 'refreshMode', 'timeSlicing', 'parallaxCorrection',
  'boxSize', 'debugView', 'boxOffset', 'scheduleUpdate', 'texture',
  'setQuality', 'setClearColor', 'setRefreshMode', 'setTimeSlicing',
  'setParallaxCorrection', 'setBoxSize', 'setDebugView', 'setBoxOffset',
  'setTexture', 'qualityChanged', 'clearColorChanged', 'refreshModeChanged',
  'timeSlicingChanged', 'parallaxCorrectionChanged', 'boxSizeChanged',
  'debugViewChanged', 'boxOffsetChanged', 'textureChanged',
  'updateSpatialNode', 'markAllDirty', 'itemChange',
  'mapToReflectionResolution', 'findSceneView', 'createDebugView',
  'updateDebugView', 'updateSceneManager'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuick3DReflectionProbe::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuick3DReflectionProbe::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuick3DReflectionProbe::~QQuick3DReflectionProbe()': the
    destructor: Python never removes a C++ QQuick3DReflectionProbe.

  What has no ritual
  ------------------

  2 of the 44 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuick3DReflectionProbe is created at the first use, not by
    'QQuick3DReflectionProbe(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuick3DReflectionProbe.
  - Qt tells when it has removed the C++ QQuick3DReflectionProbe. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QQuick3DReflectionProbe, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class ReflectionQuality(CuteNum, scoped=True):
    """
    The enum 'QQuick3DReflectionProbe::ReflectionQuality' of Qt, with the 5
    names Qt gives in it. C++ keeps these names inside the enum, so the class
    that holds the enum does not have them.
    """

    VeryLow = Kee[int](0)
    Low = Kee[int](1)
    Medium = Kee[int](2)
    High = Kee[int](3)
    VeryHigh = Kee[int](4)

  class ReflectionRefreshMode(CuteNum, scoped=True):
    """
    The enum 'QQuick3DReflectionProbe::ReflectionRefreshMode' of Qt, with the
    2 names Qt gives in it. C++ keeps these names inside the enum, so the
    class that holds the enum does not have them.
    """

    FirstFrame = Kee[int](0)
    EveryFrame = Kee[int](1)

  class ReflectionTimeSlicing(CuteNum, scoped=True):
    """
    The enum 'QQuick3DReflectionProbe::ReflectionTimeSlicing' of Qt, with the
    3 names Qt gives in it. C++ keeps these names inside the enum, so the
    class that holds the enum does not have them.
    """

    NULL = Kee[int](0)
    AllFacesAtOnce = Kee[int](1)
    IndividualFaces = Kee[int](2)

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
    Calls Qt's 'QString QQuick3DReflectionProbe::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dreflectionprobe.html#tr

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
    #  QString QQuick3DReflectionProbe::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN23QQuick3DReflectionProbe2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuick3DReflectionProbe'

  #  A C++ QQuick3DReflectionProbe Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuick3DReflectionProbe'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuick3DReflectionProbe::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dreflectionprobe.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuick3DReflectionProbe::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK23QQuick3DReflectionProbe10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def quality(self) -> ReflectionQuality:
    """
    Calls Qt's 'ReflectionQuality QQuick3DReflectionProbe::quality() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dreflectionprobe.html#quality

    Returns
    -------

    ReflectionQuality
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'ReflectionQuality(number)' gives.
    """
    #  ReflectionQuality QQuick3DReflectionProbe::quality() const
    return QQuick3DReflectionProbe.ReflectionQuality(self.uglySide.call(
        'ritual_ZNK23QQuick3DReflectionProbe7qualityEv',
    ))

  def clearColor(self) -> QColor:
    """
    Calls Qt's 'QColor QQuick3DReflectionProbe::clearColor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dreflectionprobe.html#clearColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuick3DReflectionProbe::clearColor() const
    address = self.uglySide.call(
        'ritual_ZNK23QQuick3DReflectionProbe10clearColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def refreshMode(self) -> ReflectionRefreshMode:
    """
    Calls Qt's 'ReflectionRefreshMode QQuick3DReflectionProbe::refreshMode()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dreflectionprobe.html#refreshMode

    Returns
    -------

    ReflectionRefreshMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'ReflectionRefreshMode(number)' gives.
    """
    #  ReflectionRefreshMode QQuick3DReflectionProbe::refreshMode() const
    return QQuick3DReflectionProbe.ReflectionRefreshMode(self.uglySide.call(
        'ritual_ZNK23QQuick3DReflectionProbe11refreshModeEv',
    ))

  def timeSlicing(self) -> ReflectionTimeSlicing:
    """
    Calls Qt's 'ReflectionTimeSlicing QQuick3DReflectionProbe::timeSlicing()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dreflectionprobe.html#timeSlicing

    Returns
    -------

    ReflectionTimeSlicing
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'ReflectionTimeSlicing(number)' gives.
    """
    #  ReflectionTimeSlicing QQuick3DReflectionProbe::timeSlicing() const
    return QQuick3DReflectionProbe.ReflectionTimeSlicing(self.uglySide.call(
        'ritual_ZNK23QQuick3DReflectionProbe11timeSlicingEv',
    ))

  def parallaxCorrection(self) -> bool:
    """
    Calls Qt's 'bool QQuick3DReflectionProbe::parallaxCorrection() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dreflectionprobe.html#parallaxCorrection
    """
    #  bool QQuick3DReflectionProbe::parallaxCorrection() const
    return self.uglySide.call(
        'ritual_ZNK23QQuick3DReflectionProbe18parallaxCorrectionEv',
    )

  def boxSize(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D QQuick3DReflectionProbe::boxSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dreflectionprobe.html#boxSize

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QQuick3DReflectionProbe::boxSize() const
    address = self.uglySide.call(
        'ritual_ZNK23QQuick3DReflectionProbe7boxSizeEv',
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def debugView(self) -> bool:
    """
    Calls Qt's 'bool QQuick3DReflectionProbe::debugView() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dreflectionprobe.html#debugView
    """
    #  bool QQuick3DReflectionProbe::debugView() const
    return self.uglySide.call(
        'ritual_ZNK23QQuick3DReflectionProbe9debugViewEv',
    )

  def boxOffset(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D QQuick3DReflectionProbe::boxOffset() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dreflectionprobe.html#boxOffset

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QQuick3DReflectionProbe::boxOffset() const
    address = self.uglySide.call(
        'ritual_ZNK23QQuick3DReflectionProbe9boxOffsetEv',
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def texture(self) -> Optional[QQuick3DCubeMapTexture]:
    """
    Calls Qt's 'QQuick3DCubeMapTexture *QQuick3DReflectionProbe::texture()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dreflectionprobe.html#texture

    Returns
    -------

    Optional[QQuick3DCubeMapTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DCubeMapTexture *QQuick3DReflectionProbe::texture() const
    address = self.uglySide.call(
        'ritual_ZNK23QQuick3DReflectionProbe7textureEv',
    )
    from . import QQuick3DCubeMapTexture
    return QQuick3DCubeMapTexture._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(ReflectionQuality)
  def setQuality(self, reflectionQuality: ReflectionQuality) -> None:
    """
    Calls Qt's 'void QQuick3DReflectionProbe::setQuality(ReflectionQuality
    reflectionQuality)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dreflectionprobe.html#setQuality

    Parameters
    ----------

    reflectionQuality : ReflectionQuality
      Passed on as its number.
    """
    #  void QQuick3DReflectionProbe::setQuality(ReflectionQuality
    #      reflectionQuality)
    self.uglySide.call(
        'ritual_ZN23QQuick3DReflectionProbe10setQualityENS_17ReflectionQual'
        'ityE',
        reflectionQuality.value,
    )

  @overload(QColor)
  def setClearColor(self, clearColor: QColor) -> None:
    """
    Calls Qt's 'void QQuick3DReflectionProbe::setClearColor(const QColor
    &clearColor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dreflectionprobe.html#setClearColor

    Parameters
    ----------

    clearColor : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QQuick3DReflectionProbe::setClearColor(const QColor &clearColor)
    self.uglySide.call(
        'ritual_ZN23QQuick3DReflectionProbe13setClearColorERK6QColor',
        self._valueOf(clearColor),
    )

  @overload(ReflectionRefreshMode)
  def setRefreshMode(self, newRefreshMode: ReflectionRefreshMode) -> None:
    """
    Calls Qt's 'void
    QQuick3DReflectionProbe::setRefreshMode(ReflectionRefreshMode
    newRefreshMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dreflectionprobe.html#setRefreshMode

    Parameters
    ----------

    newRefreshMode : ReflectionRefreshMode
      Passed on as its number.
    """
    #  void QQuick3DReflectionProbe::setRefreshMode(ReflectionRefreshMode
    #      newRefreshMode)
    self.uglySide.call(
        'ritual_ZN23QQuick3DReflectionProbe14setRefreshModeENS_21Reflection'
        'RefreshModeE',
        newRefreshMode.value,
    )

  @overload(ReflectionTimeSlicing)
  def setTimeSlicing(self, newTimeSlicing: ReflectionTimeSlicing) -> None:
    """
    Calls Qt's 'void
    QQuick3DReflectionProbe::setTimeSlicing(ReflectionTimeSlicing
    newTimeSlicing)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dreflectionprobe.html#setTimeSlicing

    Parameters
    ----------

    newTimeSlicing : ReflectionTimeSlicing
      Passed on as its number.
    """
    #  void QQuick3DReflectionProbe::setTimeSlicing(ReflectionTimeSlicing
    #      newTimeSlicing)
    self.uglySide.call(
        'ritual_ZN23QQuick3DReflectionProbe14setTimeSlicingENS_21Reflection'
        'TimeSlicingE',
        newTimeSlicing.value,
    )

  @overload(bool)
  def setParallaxCorrection(self, parallaxCorrection: bool) -> None:
    """
    Calls Qt's 'void QQuick3DReflectionProbe::setParallaxCorrection(bool
    parallaxCorrection)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dreflectionprobe.html#setParallaxCorrection

    Parameters
    ----------

    parallaxCorrection : bool
      Passed on as it is.
    """
    #  void QQuick3DReflectionProbe::setParallaxCorrection(bool
    #      parallaxCorrection)
    self.uglySide.call(
        'ritual_ZN23QQuick3DReflectionProbe21setParallaxCorrectionEb',
        parallaxCorrection,
    )

  @overload(QVector3D)
  def setBoxSize(self, newBoxSize: QVector3D) -> None:
    """
    Calls Qt's 'void QQuick3DReflectionProbe::setBoxSize(const QVector3D
    &newBoxSize)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dreflectionprobe.html#setBoxSize

    Parameters
    ----------

    newBoxSize : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void QQuick3DReflectionProbe::setBoxSize(const QVector3D &newBoxSize)
    self.uglySide.call(
        'ritual_ZN23QQuick3DReflectionProbe10setBoxSizeERK9QVector3D',
        self._valueOf(newBoxSize),
    )

  @overload(bool)
  def setDebugView(self, debugView: bool) -> None:
    """
    Calls Qt's 'void QQuick3DReflectionProbe::setDebugView(bool debugView)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dreflectionprobe.html#setDebugView

    Parameters
    ----------

    debugView : bool
      Passed on as it is.
    """
    #  void QQuick3DReflectionProbe::setDebugView(bool debugView)
    self.uglySide.call(
        'ritual_ZN23QQuick3DReflectionProbe12setDebugViewEb', debugView,
    )

  @overload(QVector3D)
  def setBoxOffset(self, boxOffset: QVector3D) -> None:
    """
    Calls Qt's 'void QQuick3DReflectionProbe::setBoxOffset(const QVector3D
    &boxOffset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dreflectionprobe.html#setBoxOffset

    Parameters
    ----------

    boxOffset : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void QQuick3DReflectionProbe::setBoxOffset(const QVector3D &boxOffset)
    self.uglySide.call(
        'ritual_ZN23QQuick3DReflectionProbe12setBoxOffsetERK9QVector3D',
        self._valueOf(boxOffset),
    )

  @overload(QQuick3DCubeMapTexture)
  @overload(NoneType)
  def setTexture(self, newTexture: Optional[QQuick3DCubeMapTexture]) -> None:
    """
    Calls Qt's 'void
    QQuick3DReflectionProbe::setTexture(QQuick3DCubeMapTexture *newTexture)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dreflectionprobe.html#setTexture

    Parameters
    ----------

    newTexture : Optional[QQuick3DCubeMapTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DReflectionProbe::setTexture(QQuick3DCubeMapTexture
    #      *newTexture)
    self.uglySide.call(
        'ritual_ZN23QQuick3DReflectionProbe10setTextureEP22QQuick3DCubeMapT'
        'exture',
        self._addressOf(newTexture),
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
  @overload(QQuick3DNode)
  @overload(NoneType)
  def __init__(self, parent: Optional[QQuick3DNode] = None) -> None:
    """
    Notes what was given, for Qt's
    'QQuick3DReflectionProbe::QQuick3DReflectionProbe(QQuick3DNode *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dreflectionprobe.html

    Parameters
    ----------

    parent : Optional[QQuick3DNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuick3DReflectionProbe::QQuick3DReflectionProbe(QQuick3DNode *parent)
    self._noteCreation(QQuick3DReflectionProbe, lambda: Rituals.call(
        'ritual_ZN23QQuick3DReflectionProbeC1EP12QQuick3DNode',
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

  def scheduleUpdate(self) -> None:
    """
    Calls Qt's 'void QQuick3DReflectionProbe::scheduleUpdate()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dreflectionprobe.html#scheduleUpdate
    """
    #  void QQuick3DReflectionProbe::scheduleUpdate()
    self.uglySide.call(
        'ritual_ZN23QQuick3DReflectionProbe14scheduleUpdateEv',
    )

  def qualityChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DReflectionProbe::qualityChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dreflectionprobe.html#qualityChanged
    """
    #  void QQuick3DReflectionProbe::qualityChanged()
    self.uglySide.call(
        'ritual_ZN23QQuick3DReflectionProbe14qualityChangedEv',
    )

  def clearColorChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DReflectionProbe::clearColorChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dreflectionprobe.html#clearColorChanged
    """
    #  void QQuick3DReflectionProbe::clearColorChanged()
    self.uglySide.call(
        'ritual_ZN23QQuick3DReflectionProbe17clearColorChangedEv',
    )

  def refreshModeChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DReflectionProbe::refreshModeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dreflectionprobe.html#refreshModeChanged
    """
    #  void QQuick3DReflectionProbe::refreshModeChanged()
    self.uglySide.call(
        'ritual_ZN23QQuick3DReflectionProbe18refreshModeChangedEv',
    )

  def timeSlicingChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DReflectionProbe::timeSlicingChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dreflectionprobe.html#timeSlicingChanged
    """
    #  void QQuick3DReflectionProbe::timeSlicingChanged()
    self.uglySide.call(
        'ritual_ZN23QQuick3DReflectionProbe18timeSlicingChangedEv',
    )

  def parallaxCorrectionChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DReflectionProbe::parallaxCorrectionChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dreflectionprobe.html
    """
    #  void QQuick3DReflectionProbe::parallaxCorrectionChanged()
    self.uglySide.call(
        'ritual_ZN23QQuick3DReflectionProbe25parallaxCorrectionChangedEv',
    )

  def boxSizeChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DReflectionProbe::boxSizeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dreflectionprobe.html#boxSizeChanged
    """
    #  void QQuick3DReflectionProbe::boxSizeChanged()
    self.uglySide.call(
        'ritual_ZN23QQuick3DReflectionProbe14boxSizeChangedEv',
    )

  def debugViewChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DReflectionProbe::debugViewChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dreflectionprobe.html#debugViewChanged
    """
    #  void QQuick3DReflectionProbe::debugViewChanged()
    self.uglySide.call(
        'ritual_ZN23QQuick3DReflectionProbe16debugViewChangedEv',
    )

  def boxOffsetChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DReflectionProbe::boxOffsetChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dreflectionprobe.html#boxOffsetChanged
    """
    #  void QQuick3DReflectionProbe::boxOffsetChanged()
    self.uglySide.call(
        'ritual_ZN23QQuick3DReflectionProbe16boxOffsetChangedEv',
    )

  def textureChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DReflectionProbe::textureChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dreflectionprobe.html#textureChanged
    """
    #  void QQuick3DReflectionProbe::textureChanged()
    self.uglySide.call(
        'ritual_ZN23QQuick3DReflectionProbe14textureChangedEv',
    )

  @overload(QSSGRenderGraphObject)
  @overload(NoneType)
  def updateSpatialNode(
      self,
      node: Optional[QSSGRenderGraphObject],
  ) -> Optional[QSSGRenderGraphObject]:
    """
    Calls Qt's 'QSSGRenderGraphObject
    *QQuick3DReflectionProbe::updateSpatialNode(QSSGRenderGraphObject
    *node)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dreflectionprobe.html#updateSpatialNode

    Parameters
    ----------

    node : Optional[QSSGRenderGraphObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QSSGRenderGraphObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSSGRenderGraphObject
    #      *QQuick3DReflectionProbe::updateSpatialNode(QSSGRenderGraphObject
    #      *node)
    ritual = (
        'ritual_ZN23QQuick3DReflectionProbe17updateSpatialNodeEP21QSSGRende'
        'rGraphObject')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN23QQuick3DReflectionProbe17updateSpatialNodeEP21QSS'
          'GRenderGraphObject')
    address = self.uglySide.call(ritual, self._addressOf(node))
    from ..QtQuick3DRuntimeRender import QSSGRenderGraphObject
    return QSSGRenderGraphObject._cuteAt(address)

  def markAllDirty(self) -> None:
    """
    Calls Qt's 'void QQuick3DReflectionProbe::markAllDirty()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dreflectionprobe.html#markAllDirty
    """
    #  void QQuick3DReflectionProbe::markAllDirty()
    ritual = 'ritual_ZN23QQuick3DReflectionProbe12markAllDirtyEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN23QQuick3DReflectionProbe12markAllDirtyEv'
    self.uglySide.call(ritual)

  @overload(QQuick3DObject.ItemChange, QQuick3DObject.ItemChangeData)
  def itemChange(
      self,
      a0: QQuick3DObject.ItemChange,
      a1: QQuick3DObject.ItemChangeData,
  ) -> None:
    """
    Calls Qt's 'void QQuick3DReflectionProbe::itemChange(ItemChange a0, const
    ItemChangeData &a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dreflectionprobe.html#itemChange

    Parameters
    ----------

    a0 : QQuick3DObject.ItemChange
      Passed on as its number.

    a1 : QQuick3DObject.ItemChangeData
      Passed on as a value: Qt reads the C++ QQuick3DObject::ItemChangeData,
      which stays Python's own.
    """
    #  void QQuick3DReflectionProbe::itemChange(ItemChange a0, const
    #      ItemChangeData &a1)
    ritual = (
        'ritual_ZN23QQuick3DReflectionProbe10itemChangeEN14QQuick3DObject10'
        'ItemChangeERKNS0_14ItemChangeDataE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN23QQuick3DReflectionProbe10itemChangeEN14QQuick3DOb'
          'ject10ItemChangeERKNS0_14ItemChangeDataE')
    self.uglySide.call(ritual, a0.value, self._valueOf(a1))

  @overload(ReflectionQuality)
  def mapToReflectionResolution(self, quality: ReflectionQuality) -> int:
    """
    Calls Qt's 'quint32
    QQuick3DReflectionProbe::mapToReflectionResolution(ReflectionQuality
    quality)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dreflectionprobe.html

    Parameters
    ----------

    quality : ReflectionQuality
      Passed on as its number.
    """
    #  quint32 QQuick3DReflectionProbe::mapToReflectionResolution(
    #      ReflectionQuality quality)
    return self.uglySide.call(
        'ritual_ZN23QQuick3DReflectionProbe25mapToReflectionResolutionENS_1'
        '7ReflectionQualityE',
        quality.value,
    )

  def findSceneView(self) -> None:
    """
    Calls Qt's 'void QQuick3DReflectionProbe::findSceneView()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dreflectionprobe.html#findSceneView
    """
    #  void QQuick3DReflectionProbe::findSceneView()
    self.uglySide.call('ritual_ZN23QQuick3DReflectionProbe13findSceneViewEv')

  def createDebugView(self) -> None:
    """
    Calls Qt's 'void QQuick3DReflectionProbe::createDebugView()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dreflectionprobe.html#createDebugView
    """
    #  void QQuick3DReflectionProbe::createDebugView()
    self.uglySide.call(
        'ritual_ZN23QQuick3DReflectionProbe15createDebugViewEv',
    )

  def updateDebugView(self) -> None:
    """
    Calls Qt's 'void QQuick3DReflectionProbe::updateDebugView()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dreflectionprobe.html#updateDebugView
    """
    #  void QQuick3DReflectionProbe::updateDebugView()
    self.uglySide.call(
        'ritual_ZN23QQuick3DReflectionProbe15updateDebugViewEv',
    )

  @overload(QQuick3DSceneManager)
  @overload(NoneType)
  def updateSceneManager(
      self,
      window: Optional[QQuick3DSceneManager],
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DReflectionProbe::updateSceneManager(QQuick3DSceneManager
    *window)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dreflectionprobe.html#updateSceneManager

    Parameters
    ----------

    window : Optional[QQuick3DSceneManager]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DReflectionProbe::updateSceneManager(QQuick3DSceneManager
    #      *window)
    self.uglySide.call(
        'ritual_ZN23QQuick3DReflectionProbe18updateSceneManagerEP20QQuick3D'
        'SceneManager',
        self._addressOf(window),
    )
