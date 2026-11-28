"""
QAbstract3DSeries binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDataVisualization/qabstract3dseries.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject
from . import Q3DTheme

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QColor, QLinearGradient, QQuaternion, QVector3D
  from . import QAbstract3DSeriesPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAbstract3DSeriesPrivate = WAIT['QtDataVisualization:QAbstract3DSeriesPrivate']
  QColor = WAIT['QColor']
  QLinearGradient = WAIT['QLinearGradient']
  QQuaternion = WAIT['QQuaternion']
  QVector3D = WAIT['QVector3D']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAbstract3DSeries(QObject):
  """
  The cute side of Qt's QAbstract3DSeries: a plain Python object standing in
  front of one C++ QAbstract3DSeries.

  It is built on the cute 'QObject', as Qt's QAbstract3DSeries is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QAbstract3DSeries that has a ritual and that Python
  can call so far, 51 names in all: 'metaObject', 'tr', 'type',
  'setItemLabelFormat', 'itemLabelFormat', 'setVisible', 'isVisible',
  'setMesh', 'mesh', 'setMeshSmooth', 'isMeshSmooth', 'setMeshRotation',
  'meshRotation', 'setMeshAxisAndAngle', 'setUserDefinedMesh',
  'userDefinedMesh', 'setColorStyle', 'colorStyle', 'setBaseColor',
  'baseColor', 'setBaseGradient', 'baseGradient', 'setSingleHighlightColor',
  'singleHighlightColor', 'setSingleHighlightGradient',
  'singleHighlightGradient', 'setMultiHighlightColor', 'multiHighlightColor',
  'setMultiHighlightGradient', 'multiHighlightGradient', 'setName', 'name',
  'itemLabel', 'setItemLabelVisible', 'isItemLabelVisible',
  'itemLabelFormatChanged', 'visibilityChanged', 'meshChanged',
  'meshSmoothChanged', 'meshRotationChanged', 'userDefinedMeshChanged',
  'colorStyleChanged', 'baseColorChanged', 'baseGradientChanged',
  'singleHighlightColorChanged', 'singleHighlightGradientChanged',
  'multiHighlightColorChanged', 'multiHighlightGradientChanged',
  'nameChanged', 'itemLabelChanged', 'itemLabelVisibilityChanged'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QAbstract3DSeries::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QAbstract3DSeries::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QAbstract3DSeries::~QAbstract3DSeries()': the destructor: Python
    never removes a C++ QAbstract3DSeries.

  What has no ritual
  ------------------

  4 of the 59 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QAbstract3DSeries is created at the first use, not by
    'QAbstract3DSeries(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAbstract3DSeries.
  - Qt tells when it has removed the C++ QAbstract3DSeries. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QAbstract3DSeries, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class Mesh(CuteNum):
    """
    The enum 'QAbstract3DSeries::Mesh' of Qt, with the 12 names Qt gives in
    it.
    """

    MeshUserDefined = Kee[int](0)
    MeshBar = Kee[int](1)
    MeshCube = Kee[int](2)
    MeshPyramid = Kee[int](3)
    MeshCone = Kee[int](4)
    MeshCylinder = Kee[int](5)
    MeshBevelBar = Kee[int](6)
    MeshBevelCube = Kee[int](7)
    MeshSphere = Kee[int](8)
    MeshMinimal = Kee[int](9)
    MeshArrow = Kee[int](10)
    MeshPoint = Kee[int](11)

  class SeriesType(CuteNum):
    """
    The enum 'QAbstract3DSeries::SeriesType' of Qt, with the 4 names Qt gives
    in it.
    """

    SeriesTypeNone = Kee[int](0)
    SeriesTypeBar = Kee[int](1)
    SeriesTypeScatter = Kee[int](2)
    SeriesTypeSurface = Kee[int](4)

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
    Calls Qt's 'QString QAbstract3DSeries::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstract3dseries.html#tr

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
    #  QString QAbstract3DSeries::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN17QAbstract3DSeries2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAbstract3DSeries'
  #  The part of Qt it is of, as another part has a class of its name too.
  __qt_part__ = 'QtDataVisualization'

  #  A C++ QAbstract3DSeries Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QAbstract3DSeries'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QAbstract3DSeries::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstract3dseries.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QAbstract3DSeries::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK17QAbstract3DSeries10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def type(self) -> SeriesType:
    """
    Calls Qt's 'SeriesType QAbstract3DSeries::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstract3dseries.html#type

    Returns
    -------

    SeriesType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'SeriesType(number)'
      gives.
    """
    #  SeriesType QAbstract3DSeries::type() const
    return QAbstract3DSeries.SeriesType(self.uglySide.call(
        'ritual_ZNK17QAbstract3DSeries4typeEv',
    ))

  def itemLabelFormat(self) -> str:
    """
    Calls Qt's 'QString QAbstract3DSeries::itemLabelFormat() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dseries.html#itemLabelFormat

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QAbstract3DSeries::itemLabelFormat() const
    return self.uglySide.call(
        'ritual_ZNK17QAbstract3DSeries15itemLabelFormatEv',
    )

  def isVisible(self) -> bool:
    """
    Calls Qt's 'bool QAbstract3DSeries::isVisible() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstract3dseries.html#isVisible
    """
    #  bool QAbstract3DSeries::isVisible() const
    return self.uglySide.call('ritual_ZNK17QAbstract3DSeries9isVisibleEv')

  def mesh(self) -> Mesh:
    """
    Calls Qt's 'Mesh QAbstract3DSeries::mesh() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstract3dseries.html#mesh

    Returns
    -------

    Mesh
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Mesh(number)' gives.
    """
    #  Mesh QAbstract3DSeries::mesh() const
    return QAbstract3DSeries.Mesh(self.uglySide.call(
        'ritual_ZNK17QAbstract3DSeries4meshEv',
    ))

  def isMeshSmooth(self) -> bool:
    """
    Calls Qt's 'bool QAbstract3DSeries::isMeshSmooth() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dseries.html#isMeshSmooth
    """
    #  bool QAbstract3DSeries::isMeshSmooth() const
    return self.uglySide.call(
        'ritual_ZNK17QAbstract3DSeries12isMeshSmoothEv',
    )

  def meshRotation(self) -> QQuaternion:
    """
    Calls Qt's 'QQuaternion QAbstract3DSeries::meshRotation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dseries.html#meshRotation

    Returns
    -------

    QQuaternion
      A new cute QQuaternion around the copy Qt gave back. Python owns it.
    """
    #  QQuaternion QAbstract3DSeries::meshRotation() const
    address = self.uglySide.call(
        'ritual_ZNK17QAbstract3DSeries12meshRotationEv',
    )
    from ..QtGui import QQuaternion
    return QQuaternion._cuteOwning(address)

  def userDefinedMesh(self) -> str:
    """
    Calls Qt's 'QString QAbstract3DSeries::userDefinedMesh() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dseries.html#userDefinedMesh

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QAbstract3DSeries::userDefinedMesh() const
    return self.uglySide.call(
        'ritual_ZNK17QAbstract3DSeries15userDefinedMeshEv',
    )

  def colorStyle(self) -> Q3DTheme.ColorStyle:
    """
    Calls Qt's 'Q3DTheme::ColorStyle QAbstract3DSeries::colorStyle() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstract3dseries.html#colorStyle

    Returns
    -------

    Q3DTheme.ColorStyle
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Q3DTheme.ColorStyle(number)' gives.
    """
    #  Q3DTheme::ColorStyle QAbstract3DSeries::colorStyle() const
    return Q3DTheme.ColorStyle(self.uglySide.call(
        'ritual_ZNK17QAbstract3DSeries10colorStyleEv',
    ))

  def baseColor(self) -> QColor:
    """
    Calls Qt's 'QColor QAbstract3DSeries::baseColor() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstract3dseries.html#baseColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QAbstract3DSeries::baseColor() const
    address = self.uglySide.call('ritual_ZNK17QAbstract3DSeries9baseColorEv')
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def baseGradient(self) -> QLinearGradient:
    """
    Calls Qt's 'QLinearGradient QAbstract3DSeries::baseGradient() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dseries.html#baseGradient

    Returns
    -------

    QLinearGradient
      A new cute QLinearGradient around the copy Qt gave back. Python owns
      it.
    """
    #  QLinearGradient QAbstract3DSeries::baseGradient() const
    address = self.uglySide.call(
        'ritual_ZNK17QAbstract3DSeries12baseGradientEv',
    )
    from ..QtGui import QLinearGradient
    return QLinearGradient._cuteOwning(address)

  def singleHighlightColor(self) -> QColor:
    """
    Calls Qt's 'QColor QAbstract3DSeries::singleHighlightColor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dseries.html#singleHighlightColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QAbstract3DSeries::singleHighlightColor() const
    address = self.uglySide.call(
        'ritual_ZNK17QAbstract3DSeries20singleHighlightColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def singleHighlightGradient(self) -> QLinearGradient:
    """
    Calls Qt's 'QLinearGradient QAbstract3DSeries::singleHighlightGradient()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dseries.html#singleHighlightGradient

    Returns
    -------

    QLinearGradient
      A new cute QLinearGradient around the copy Qt gave back. Python owns
      it.
    """
    #  QLinearGradient QAbstract3DSeries::singleHighlightGradient() const
    address = self.uglySide.call(
        'ritual_ZNK17QAbstract3DSeries23singleHighlightGradientEv',
    )
    from ..QtGui import QLinearGradient
    return QLinearGradient._cuteOwning(address)

  def multiHighlightColor(self) -> QColor:
    """
    Calls Qt's 'QColor QAbstract3DSeries::multiHighlightColor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dseries.html#multiHighlightColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QAbstract3DSeries::multiHighlightColor() const
    address = self.uglySide.call(
        'ritual_ZNK17QAbstract3DSeries19multiHighlightColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def multiHighlightGradient(self) -> QLinearGradient:
    """
    Calls Qt's 'QLinearGradient QAbstract3DSeries::multiHighlightGradient()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dseries.html#multiHighlightGradient

    Returns
    -------

    QLinearGradient
      A new cute QLinearGradient around the copy Qt gave back. Python owns
      it.
    """
    #  QLinearGradient QAbstract3DSeries::multiHighlightGradient() const
    address = self.uglySide.call(
        'ritual_ZNK17QAbstract3DSeries22multiHighlightGradientEv',
    )
    from ..QtGui import QLinearGradient
    return QLinearGradient._cuteOwning(address)

  def name(self) -> str:
    """
    Calls Qt's 'QString QAbstract3DSeries::name() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstract3dseries.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QAbstract3DSeries::name() const
    return self.uglySide.call('ritual_ZNK17QAbstract3DSeries4nameEv')

  def itemLabel(self) -> str:
    """
    Calls Qt's 'QString QAbstract3DSeries::itemLabel() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstract3dseries.html#itemLabel

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QAbstract3DSeries::itemLabel() const
    return self.uglySide.call('ritual_ZNK17QAbstract3DSeries9itemLabelEv')

  def isItemLabelVisible(self) -> bool:
    """
    Calls Qt's 'bool QAbstract3DSeries::isItemLabelVisible() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dseries.html#isItemLabelVisible
    """
    #  bool QAbstract3DSeries::isItemLabelVisible() const
    return self.uglySide.call(
        'ritual_ZNK17QAbstract3DSeries18isItemLabelVisibleEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setItemLabelFormat(self, format: str) -> None:
    """
    Calls Qt's 'void QAbstract3DSeries::setItemLabelFormat(const QString
    &format)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dseries.html#setItemLabelFormat

    Parameters
    ----------

    format : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QAbstract3DSeries::setItemLabelFormat(const QString &format)
    self.uglySide.call(
        'ritual_ZN17QAbstract3DSeries18setItemLabelFormatERK7QString',
        format,
    )

  @overload(bool)
  def setVisible(self, visible: bool) -> None:
    """
    Calls Qt's 'void QAbstract3DSeries::setVisible(bool visible)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstract3dseries.html#setVisible

    Parameters
    ----------

    visible : bool
      Passed on as it is.
    """
    #  void QAbstract3DSeries::setVisible(bool visible)
    self.uglySide.call('ritual_ZN17QAbstract3DSeries10setVisibleEb', visible)

  @overload(Mesh)
  def setMesh(self, mesh: Mesh) -> None:
    """
    Calls Qt's 'void QAbstract3DSeries::setMesh(Mesh mesh)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstract3dseries.html#setMesh

    Parameters
    ----------

    mesh : Mesh
      Passed on as its number.
    """
    #  void QAbstract3DSeries::setMesh(Mesh mesh)
    self.uglySide.call(
        'ritual_ZN17QAbstract3DSeries7setMeshENS_4MeshE', mesh.value,
    )

  @overload(bool)
  def setMeshSmooth(self, enable: bool) -> None:
    """
    Calls Qt's 'void QAbstract3DSeries::setMeshSmooth(bool enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dseries.html#setMeshSmooth

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QAbstract3DSeries::setMeshSmooth(bool enable)
    self.uglySide.call(
        'ritual_ZN17QAbstract3DSeries13setMeshSmoothEb', enable,
    )

  @overload(QQuaternion)
  def setMeshRotation(self, rotation: QQuaternion) -> None:
    """
    Calls Qt's 'void QAbstract3DSeries::setMeshRotation(const QQuaternion
    &rotation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dseries.html#setMeshRotation

    Parameters
    ----------

    rotation : QQuaternion
      Passed on as a value: Qt reads the C++ QQuaternion, which stays
      Python's own.
    """
    #  void QAbstract3DSeries::setMeshRotation(const QQuaternion &rotation)
    self.uglySide.call(
        'ritual_ZN17QAbstract3DSeries15setMeshRotationERK11QQuaternion',
        self._valueOf(rotation),
    )

  @overload(QVector3D, float)
  def setMeshAxisAndAngle(self, axis: QVector3D, angle: float) -> None:
    """
    Calls Qt's 'void QAbstract3DSeries::setMeshAxisAndAngle(const QVector3D
    &axis, float angle)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dseries.html#setMeshAxisAndAngle

    Parameters
    ----------

    axis : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    angle : float
      Passed on as it is.
    """
    #  void QAbstract3DSeries::setMeshAxisAndAngle(const QVector3D &axis,
    #      float angle)
    self.uglySide.call(
        'ritual_ZN17QAbstract3DSeries19setMeshAxisAndAngleERK9QVector3Df',
        self._valueOf(axis), angle,
    )

  @overload(str)
  def setUserDefinedMesh(self, fileName: str) -> None:
    """
    Calls Qt's 'void QAbstract3DSeries::setUserDefinedMesh(const QString
    &fileName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dseries.html#setUserDefinedMesh

    Parameters
    ----------

    fileName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QAbstract3DSeries::setUserDefinedMesh(const QString &fileName)
    self.uglySide.call(
        'ritual_ZN17QAbstract3DSeries18setUserDefinedMeshERK7QString',
        fileName,
    )

  @overload(Q3DTheme.ColorStyle)
  def setColorStyle(self, style: Q3DTheme.ColorStyle) -> None:
    """
    Calls Qt's 'void QAbstract3DSeries::setColorStyle(Q3DTheme::ColorStyle
    style)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dseries.html#setColorStyle

    Parameters
    ----------

    style : Q3DTheme.ColorStyle
      Passed on as its number.
    """
    #  void QAbstract3DSeries::setColorStyle(Q3DTheme::ColorStyle style)
    self.uglySide.call(
        'ritual_ZN17QAbstract3DSeries13setColorStyleEN8Q3DTheme10ColorStyle'
        'E',
        style.value,
    )

  @overload(QColor)
  def setBaseColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QAbstract3DSeries::setBaseColor(const QColor &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dseries.html#setBaseColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QAbstract3DSeries::setBaseColor(const QColor &color)
    self.uglySide.call(
        'ritual_ZN17QAbstract3DSeries12setBaseColorERK6QColor',
        self._valueOf(color),
    )

  @overload(QLinearGradient)
  def setBaseGradient(self, gradient: QLinearGradient) -> None:
    """
    Calls Qt's 'void QAbstract3DSeries::setBaseGradient(const QLinearGradient
    &gradient)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dseries.html#setBaseGradient

    Parameters
    ----------

    gradient : QLinearGradient
      Passed on as a value: Qt reads the C++ QLinearGradient, which stays
      Python's own.
    """
    #  void QAbstract3DSeries::setBaseGradient(const QLinearGradient
    #      &gradient)
    self.uglySide.call(
        'ritual_ZN17QAbstract3DSeries15setBaseGradientERK15QLinearGradient',
        self._valueOf(gradient),
    )

  @overload(QColor)
  def setSingleHighlightColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QAbstract3DSeries::setSingleHighlightColor(const QColor
    &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dseries.html#setSingleHighlightColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QAbstract3DSeries::setSingleHighlightColor(const QColor &color)
    self.uglySide.call(
        'ritual_ZN17QAbstract3DSeries23setSingleHighlightColorERK6QColor',
        self._valueOf(color),
    )

  @overload(QLinearGradient)
  def setSingleHighlightGradient(self, gradient: QLinearGradient) -> None:
    """
    Calls Qt's 'void QAbstract3DSeries::setSingleHighlightGradient(const
    QLinearGradient &gradient)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dseries.html#setSingleHighlightGradient

    Parameters
    ----------

    gradient : QLinearGradient
      Passed on as a value: Qt reads the C++ QLinearGradient, which stays
      Python's own.
    """
    #  void QAbstract3DSeries::setSingleHighlightGradient(const
    #      QLinearGradient &gradient)
    self.uglySide.call(
        'ritual_ZN17QAbstract3DSeries26setSingleHighlightGradientERK15QLine'
        'arGradient',
        self._valueOf(gradient),
    )

  @overload(QColor)
  def setMultiHighlightColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QAbstract3DSeries::setMultiHighlightColor(const QColor
    &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dseries.html#setMultiHighlightColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QAbstract3DSeries::setMultiHighlightColor(const QColor &color)
    self.uglySide.call(
        'ritual_ZN17QAbstract3DSeries22setMultiHighlightColorERK6QColor',
        self._valueOf(color),
    )

  @overload(QLinearGradient)
  def setMultiHighlightGradient(self, gradient: QLinearGradient) -> None:
    """
    Calls Qt's 'void QAbstract3DSeries::setMultiHighlightGradient(const
    QLinearGradient &gradient)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dseries.html#setMultiHighlightGradient

    Parameters
    ----------

    gradient : QLinearGradient
      Passed on as a value: Qt reads the C++ QLinearGradient, which stays
      Python's own.
    """
    #  void QAbstract3DSeries::setMultiHighlightGradient(const
    #      QLinearGradient &gradient)
    self.uglySide.call(
        'ritual_ZN17QAbstract3DSeries25setMultiHighlightGradientERK15QLinea'
        'rGradient',
        self._valueOf(gradient),
    )

  @overload(str)
  def setName(self, name: str) -> None:
    """
    Calls Qt's 'void QAbstract3DSeries::setName(const QString &name)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstract3dseries.html#setName

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QAbstract3DSeries::setName(const QString &name)
    self.uglySide.call(
        'ritual_ZN17QAbstract3DSeries7setNameERK7QString', name,
    )

  @overload(bool)
  def setItemLabelVisible(self, visible: bool) -> None:
    """
    Calls Qt's 'void QAbstract3DSeries::setItemLabelVisible(bool visible)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dseries.html#setItemLabelVisible

    Parameters
    ----------

    visible : bool
      Passed on as it is.
    """
    #  void QAbstract3DSeries::setItemLabelVisible(bool visible)
    self.uglySide.call(
        'ritual_ZN17QAbstract3DSeries19setItemLabelVisibleEb', visible,
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

  @overload(QAbstract3DSeriesPrivate)
  @overload(NoneType)
  @overload(QAbstract3DSeriesPrivate, QObject)
  @overload(QAbstract3DSeriesPrivate, NoneType)
  @overload(NoneType, QObject)
  @overload(NoneType, NoneType)
  def __init__(
      self,
      d: Optional[QAbstract3DSeriesPrivate],
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QAbstract3DSeries::QAbstract3DSeries(QAbstract3DSeriesPrivate *d,
    QObject *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dseries.html#QAbstract3DSeries

    Parameters
    ----------

    d : Optional[QAbstract3DSeriesPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QAbstract3DSeries::QAbstract3DSeries(QAbstract3DSeriesPrivate *d,
    #      QObject *parent)
    self._noteCreation(QAbstract3DSeries, lambda: Rituals.call(
        'ritual_ZN17QAbstract3DSeriesC1EP24QAbstract3DSeriesPrivateP7QObjec'
        't',
        self._addressOf(d), self._addressOf(parent, 'QObject'),
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

  @overload(str)
  def itemLabelFormatChanged(self, format: str) -> None:
    """
    Calls Qt's 'void QAbstract3DSeries::itemLabelFormatChanged(const QString
    &format)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dseries.html#itemLabelFormatChanged

    Parameters
    ----------

    format : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QAbstract3DSeries::itemLabelFormatChanged(const QString &format)
    self.uglySide.call(
        'ritual_ZN17QAbstract3DSeries22itemLabelFormatChangedERK7QString',
        format,
    )

  @overload(bool)
  def visibilityChanged(self, visible: bool) -> None:
    """
    Calls Qt's 'void QAbstract3DSeries::visibilityChanged(bool visible)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dseries.html#visibilityChanged

    Parameters
    ----------

    visible : bool
      Passed on as it is.
    """
    #  void QAbstract3DSeries::visibilityChanged(bool visible)
    self.uglySide.call(
        'ritual_ZN17QAbstract3DSeries17visibilityChangedEb', visible,
    )

  @overload(Mesh)
  def meshChanged(self, mesh: Mesh) -> None:
    """
    Calls Qt's 'void QAbstract3DSeries::meshChanged(QAbstract3DSeries::Mesh
    mesh)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstract3dseries.html#meshChanged

    Parameters
    ----------

    mesh : Mesh
      Passed on as its number.
    """
    #  void QAbstract3DSeries::meshChanged(QAbstract3DSeries::Mesh mesh)
    self.uglySide.call(
        'ritual_ZN17QAbstract3DSeries11meshChangedENS_4MeshE', mesh.value,
    )

  @overload(bool)
  def meshSmoothChanged(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QAbstract3DSeries::meshSmoothChanged(bool enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dseries.html#meshSmoothChanged

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QAbstract3DSeries::meshSmoothChanged(bool enabled)
    self.uglySide.call(
        'ritual_ZN17QAbstract3DSeries17meshSmoothChangedEb', enabled,
    )

  @overload(QQuaternion)
  def meshRotationChanged(self, rotation: QQuaternion) -> None:
    """
    Calls Qt's 'void QAbstract3DSeries::meshRotationChanged(const QQuaternion
    &rotation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dseries.html#meshRotationChanged

    Parameters
    ----------

    rotation : QQuaternion
      Passed on as a value: Qt reads the C++ QQuaternion, which stays
      Python's own.
    """
    #  void QAbstract3DSeries::meshRotationChanged(const QQuaternion
    #      &rotation)
    self.uglySide.call(
        'ritual_ZN17QAbstract3DSeries19meshRotationChangedERK11QQuaternion',
        self._valueOf(rotation),
    )

  @overload(str)
  def userDefinedMeshChanged(self, fileName: str) -> None:
    """
    Calls Qt's 'void QAbstract3DSeries::userDefinedMeshChanged(const QString
    &fileName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dseries.html#userDefinedMeshChanged

    Parameters
    ----------

    fileName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QAbstract3DSeries::userDefinedMeshChanged(const QString
    #      &fileName)
    self.uglySide.call(
        'ritual_ZN17QAbstract3DSeries22userDefinedMeshChangedERK7QString',
        fileName,
    )

  @overload(Q3DTheme.ColorStyle)
  def colorStyleChanged(self, style: Q3DTheme.ColorStyle) -> None:
    """
    Calls Qt's 'void
    QAbstract3DSeries::colorStyleChanged(Q3DTheme::ColorStyle style)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dseries.html#colorStyleChanged

    Parameters
    ----------

    style : Q3DTheme.ColorStyle
      Passed on as its number.
    """
    #  void QAbstract3DSeries::colorStyleChanged(Q3DTheme::ColorStyle style)
    self.uglySide.call(
        'ritual_ZN17QAbstract3DSeries17colorStyleChangedEN8Q3DTheme10ColorS'
        'tyleE',
        style.value,
    )

  @overload(QColor)
  def baseColorChanged(self, color: QColor) -> None:
    """
    Calls Qt's 'void QAbstract3DSeries::baseColorChanged(const QColor
    &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dseries.html#baseColorChanged

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QAbstract3DSeries::baseColorChanged(const QColor &color)
    self.uglySide.call(
        'ritual_ZN17QAbstract3DSeries16baseColorChangedERK6QColor',
        self._valueOf(color),
    )

  @overload(QLinearGradient)
  def baseGradientChanged(self, gradient: QLinearGradient) -> None:
    """
    Calls Qt's 'void QAbstract3DSeries::baseGradientChanged(const
    QLinearGradient &gradient)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dseries.html#baseGradientChanged

    Parameters
    ----------

    gradient : QLinearGradient
      Passed on as a value: Qt reads the C++ QLinearGradient, which stays
      Python's own.
    """
    #  void QAbstract3DSeries::baseGradientChanged(const QLinearGradient
    #      &gradient)
    self.uglySide.call(
        'ritual_ZN17QAbstract3DSeries19baseGradientChangedERK15QLinearGradi'
        'ent',
        self._valueOf(gradient),
    )

  @overload(QColor)
  def singleHighlightColorChanged(self, color: QColor) -> None:
    """
    Calls Qt's 'void QAbstract3DSeries::singleHighlightColorChanged(const
    QColor &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dseries.html#singleHighlightColorChanged

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QAbstract3DSeries::singleHighlightColorChanged(const QColor
    #      &color)
    self.uglySide.call(
        'ritual_ZN17QAbstract3DSeries27singleHighlightColorChangedERK6QColo'
        'r',
        self._valueOf(color),
    )

  @overload(QLinearGradient)
  def singleHighlightGradientChanged(
      self,
      gradient: QLinearGradient,
  ) -> None:
    """
    Calls Qt's 'void QAbstract3DSeries::singleHighlightGradientChanged(const
    QLinearGradient &gradient)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dseries.html

    Parameters
    ----------

    gradient : QLinearGradient
      Passed on as a value: Qt reads the C++ QLinearGradient, which stays
      Python's own.
    """
    #  void QAbstract3DSeries::singleHighlightGradientChanged(const
    #      QLinearGradient &gradient)
    self.uglySide.call(
        'ritual_ZN17QAbstract3DSeries30singleHighlightGradientChangedERK15Q'
        'LinearGradient',
        self._valueOf(gradient),
    )

  @overload(QColor)
  def multiHighlightColorChanged(self, color: QColor) -> None:
    """
    Calls Qt's 'void QAbstract3DSeries::multiHighlightColorChanged(const
    QColor &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dseries.html#multiHighlightColorChanged

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QAbstract3DSeries::multiHighlightColorChanged(const QColor
    #      &color)
    self.uglySide.call(
        'ritual_ZN17QAbstract3DSeries26multiHighlightColorChangedERK6QColor',
        self._valueOf(color),
    )

  @overload(QLinearGradient)
  def multiHighlightGradientChanged(self, gradient: QLinearGradient) -> None:
    """
    Calls Qt's 'void QAbstract3DSeries::multiHighlightGradientChanged(const
    QLinearGradient &gradient)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dseries.html

    Parameters
    ----------

    gradient : QLinearGradient
      Passed on as a value: Qt reads the C++ QLinearGradient, which stays
      Python's own.
    """
    #  void QAbstract3DSeries::multiHighlightGradientChanged(const
    #      QLinearGradient &gradient)
    self.uglySide.call(
        'ritual_ZN17QAbstract3DSeries29multiHighlightGradientChangedERK15QL'
        'inearGradient',
        self._valueOf(gradient),
    )

  @overload(str)
  def nameChanged(self, name: str) -> None:
    """
    Calls Qt's 'void QAbstract3DSeries::nameChanged(const QString &name)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstract3dseries.html#nameChanged

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QAbstract3DSeries::nameChanged(const QString &name)
    self.uglySide.call(
        'ritual_ZN17QAbstract3DSeries11nameChangedERK7QString', name,
    )

  @overload(str)
  def itemLabelChanged(self, label: str) -> None:
    """
    Calls Qt's 'void QAbstract3DSeries::itemLabelChanged(const QString
    &label)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dseries.html#itemLabelChanged

    Parameters
    ----------

    label : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QAbstract3DSeries::itemLabelChanged(const QString &label)
    self.uglySide.call(
        'ritual_ZN17QAbstract3DSeries16itemLabelChangedERK7QString', label,
    )

  @overload(bool)
  def itemLabelVisibilityChanged(self, visible: bool) -> None:
    """
    Calls Qt's 'void QAbstract3DSeries::itemLabelVisibilityChanged(bool
    visible)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dseries.html#itemLabelVisibilityChanged

    Parameters
    ----------

    visible : bool
      Passed on as it is.
    """
    #  void QAbstract3DSeries::itemLabelVisibilityChanged(bool visible)
    self.uglySide.call(
        'ritual_ZN17QAbstract3DSeries26itemLabelVisibilityChangedEb',
        visible,
    )


#  Qt's 'QList<QAbstract3DSeries *>': the list of QAbstract3DSeries, which
#  'QList[QAbstract3DSeries]' gives. It is made here, so that there is one as
#  soon as there can be a QAbstract3DSeries.
QList.createKind(
    QAbstract3DSeries, 'address',
    make='ritual_list_make_QAbstract3DSeries_ptr',
    add='ritual_list_add_QAbstract3DSeries_ptr',
    size='ritual_list_size_QAbstract3DSeries_ptr',
    at='ritual_list_at_QAbstract3DSeries_ptr',
    drop='ritual_list_drop_QAbstract3DSeries_ptr',
)
