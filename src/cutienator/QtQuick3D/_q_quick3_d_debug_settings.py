"""
QQuick3DDebugSettings binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3D/6.12.0/QtQuick3D/private/qquick3ddebugsettings_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQuick3DDebugSettings to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuick3DDebugSettings(QObject):
  """
  The cute side of Qt's QQuick3DDebugSettings: a plain Python object standing
  in front of one C++ QQuick3DDebugSettings.

  It is built on the cute 'QObject', as Qt's QQuick3DDebugSettings is built
  on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuick3DDebugSettings that has a ritual and that
  Python can call so far, 34 names in all: 'metaObject', 'tr',
  'materialOverride', 'setMaterialOverride', 'wireframeEnabled',
  'setWireframeEnabled', 'drawDirectionalLightShadowBoxes',
  'setDrawDirectionalLightShadowBoxes', 'drawPointLightShadowBoxes',
  'setDrawPointLightShadowBoxes', 'drawShadowCastingBounds',
  'setDrawShadowCastingBounds', 'drawShadowReceivingBounds',
  'setDrawShadowReceivingBounds', 'drawCascades', 'setDrawCascades',
  'drawSceneCascadeIntersection', 'setDrawSceneCascadeIntersection',
  'disableShadowCameraUpdate', 'setDisableShadowCameraUpdate',
  'drawCulledObjects', 'setDrawCulledObjects', 'materialOverrideChanged',
  'wireframeEnabledChanged', 'drawDirectionalLightShadowBoxesChanged',
  'drawPointLightShadowBoxesChanged', 'drawShadowCastingBoundsChanged',
  'drawShadowReceivingBoundsChanged', 'drawCascadesChanged',
  'drawSceneCascadeIntersectionChanged', 'disableShadowCameraUpdateChanged',
  'drawCulledObjectsChanged', 'changed', 'update'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuick3DDebugSettings::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuick3DDebugSettings::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  2 of the 39 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuick3DDebugSettings is created at the first use, not by
    'QQuick3DDebugSettings(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuick3DDebugSettings.
  - Qt tells when it has removed the C++ QQuick3DDebugSettings. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QQuick3DDebugSettings, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class QQuick3DMaterialOverrides(CuteNum):
    """
    The enum 'QQuick3DDebugSettings::QQuick3DMaterialOverrides' of Qt, with
    the 13 names Qt gives in it.
    """

    NULL = Kee[int](0)
    BaseColor = Kee[int](1)
    Roughness = Kee[int](2)
    Metalness = Kee[int](3)
    Diffuse = Kee[int](4)
    Specular = Kee[int](5)
    ShadowOcclusion = Kee[int](6)
    Emission = Kee[int](7)
    AmbientOcclusion = Kee[int](8)
    Normals = Kee[int](9)
    Tangents = Kee[int](10)
    Binormals = Kee[int](11)
    F0 = Kee[int](12)

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
    Calls Qt's 'QString QQuick3DDebugSettings::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3ddebugsettings.html#tr

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
    #  QString QQuick3DDebugSettings::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN21QQuick3DDebugSettings2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuick3DDebugSettings'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuick3DDebugSettings::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddebugsettings.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuick3DDebugSettings::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK21QQuick3DDebugSettings10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def materialOverride(self) -> QQuick3DMaterialOverrides:
    """
    Calls Qt's 'QQuick3DMaterialOverrides
    QQuick3DDebugSettings::materialOverride() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddebugsettings.html#materialOverride

    Returns
    -------

    QQuick3DMaterialOverrides
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QQuick3DMaterialOverrides(number)' gives.
    """
    #  QQuick3DMaterialOverrides QQuick3DDebugSettings::materialOverride()
    #      const
    return QQuick3DDebugSettings.QQuick3DMaterialOverrides(
        self.uglySide.call(
            'ritual_ZNK21QQuick3DDebugSettings16materialOverrideEv',
        ))

  def wireframeEnabled(self) -> bool:
    """
    Calls Qt's 'bool QQuick3DDebugSettings::wireframeEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddebugsettings.html#wireframeEnabled
    """
    #  bool QQuick3DDebugSettings::wireframeEnabled() const
    return self.uglySide.call(
        'ritual_ZNK21QQuick3DDebugSettings16wireframeEnabledEv',
    )

  def drawDirectionalLightShadowBoxes(self) -> bool:
    """
    Calls Qt's 'bool QQuick3DDebugSettings::drawDirectionalLightShadowBoxes()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddebugsettings.html
    """
    #  bool QQuick3DDebugSettings::drawDirectionalLightShadowBoxes() const
    return self.uglySide.call(
        'ritual_ZNK21QQuick3DDebugSettings31drawDirectionalLightShadowBoxes'
        'Ev',
    )

  def drawPointLightShadowBoxes(self) -> bool:
    """
    Calls Qt's 'bool QQuick3DDebugSettings::drawPointLightShadowBoxes()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddebugsettings.html
    """
    #  bool QQuick3DDebugSettings::drawPointLightShadowBoxes() const
    return self.uglySide.call(
        'ritual_ZNK21QQuick3DDebugSettings25drawPointLightShadowBoxesEv',
    )

  def drawShadowCastingBounds(self) -> bool:
    """
    Calls Qt's 'bool QQuick3DDebugSettings::drawShadowCastingBounds() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddebugsettings.html#drawShadowCastingBounds
    """
    #  bool QQuick3DDebugSettings::drawShadowCastingBounds() const
    return self.uglySide.call(
        'ritual_ZNK21QQuick3DDebugSettings23drawShadowCastingBoundsEv',
    )

  def drawShadowReceivingBounds(self) -> bool:
    """
    Calls Qt's 'bool QQuick3DDebugSettings::drawShadowReceivingBounds()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddebugsettings.html
    """
    #  bool QQuick3DDebugSettings::drawShadowReceivingBounds() const
    return self.uglySide.call(
        'ritual_ZNK21QQuick3DDebugSettings25drawShadowReceivingBoundsEv',
    )

  def drawCascades(self) -> bool:
    """
    Calls Qt's 'bool QQuick3DDebugSettings::drawCascades() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddebugsettings.html#drawCascades
    """
    #  bool QQuick3DDebugSettings::drawCascades() const
    return self.uglySide.call(
        'ritual_ZNK21QQuick3DDebugSettings12drawCascadesEv',
    )

  def drawSceneCascadeIntersection(self) -> bool:
    """
    Calls Qt's 'bool QQuick3DDebugSettings::drawSceneCascadeIntersection()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddebugsettings.html
    """
    #  bool QQuick3DDebugSettings::drawSceneCascadeIntersection() const
    return self.uglySide.call(
        'ritual_ZNK21QQuick3DDebugSettings28drawSceneCascadeIntersectionEv',
    )

  def disableShadowCameraUpdate(self) -> bool:
    """
    Calls Qt's 'bool QQuick3DDebugSettings::disableShadowCameraUpdate()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddebugsettings.html
    """
    #  bool QQuick3DDebugSettings::disableShadowCameraUpdate() const
    return self.uglySide.call(
        'ritual_ZNK21QQuick3DDebugSettings25disableShadowCameraUpdateEv',
    )

  def drawCulledObjects(self) -> bool:
    """
    Calls Qt's 'bool QQuick3DDebugSettings::drawCulledObjects() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddebugsettings.html#drawCulledObjects
    """
    #  bool QQuick3DDebugSettings::drawCulledObjects() const
    return self.uglySide.call(
        'ritual_ZNK21QQuick3DDebugSettings17drawCulledObjectsEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QQuick3DMaterialOverrides)
  def setMaterialOverride(
      self,
      newMaterialOverride: QQuick3DMaterialOverrides,
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DDebugSettings::setMaterialOverride(QQuick3DMaterialOverrides
    newMaterialOverride)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddebugsettings.html#setMaterialOverride

    Parameters
    ----------

    newMaterialOverride : QQuick3DMaterialOverrides
      Passed on as its number.
    """
    #  void QQuick3DDebugSettings::setMaterialOverride(
    #      QQuick3DMaterialOverrides newMaterialOverride)
    self.uglySide.call(
        'ritual_ZN21QQuick3DDebugSettings19setMaterialOverrideENS_25QQuick3'
        'DMaterialOverridesE',
        newMaterialOverride.value,
    )

  @overload(bool)
  def setWireframeEnabled(self, newWireframeEnabled: bool) -> None:
    """
    Calls Qt's 'void QQuick3DDebugSettings::setWireframeEnabled(bool
    newWireframeEnabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddebugsettings.html#setWireframeEnabled

    Parameters
    ----------

    newWireframeEnabled : bool
      Passed on as it is.
    """
    #  void QQuick3DDebugSettings::setWireframeEnabled(bool
    #      newWireframeEnabled)
    self.uglySide.call(
        'ritual_ZN21QQuick3DDebugSettings19setWireframeEnabledEb',
        newWireframeEnabled,
    )

  @overload(bool)
  def setDrawDirectionalLightShadowBoxes(
      self,
      newDrawDirectionalLightShadowBoxes: bool,
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DDebugSettings::setDrawDirectionalLightShadowBoxes(bool
    newDrawDirectionalLightShadowBoxes)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddebugsettings.html

    Parameters
    ----------

    newDrawDirectionalLightShadowBoxes : bool
      Passed on as it is.
    """
    #  void QQuick3DDebugSettings::setDrawDirectionalLightShadowBoxes(bool
    #      newDrawDirectionalLightShadowBoxes)
    self.uglySide.call(
        'ritual_ZN21QQuick3DDebugSettings34setDrawDirectionalLightShadowBox'
        'esEb',
        newDrawDirectionalLightShadowBoxes,
    )

  @overload(bool)
  def setDrawPointLightShadowBoxes(
      self,
      newDrawPointLightShadowBoxes: bool,
  ) -> None:
    """
    Calls Qt's 'void QQuick3DDebugSettings::setDrawPointLightShadowBoxes(bool
    newDrawPointLightShadowBoxes)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddebugsettings.html

    Parameters
    ----------

    newDrawPointLightShadowBoxes : bool
      Passed on as it is.
    """
    #  void QQuick3DDebugSettings::setDrawPointLightShadowBoxes(bool
    #      newDrawPointLightShadowBoxes)
    self.uglySide.call(
        'ritual_ZN21QQuick3DDebugSettings28setDrawPointLightShadowBoxesEb',
        newDrawPointLightShadowBoxes,
    )

  @overload(bool)
  def setDrawShadowCastingBounds(
      self,
      newDrawShadowCastingBounds: bool,
  ) -> None:
    """
    Calls Qt's 'void QQuick3DDebugSettings::setDrawShadowCastingBounds(bool
    newDrawShadowCastingBounds)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddebugsettings.html

    Parameters
    ----------

    newDrawShadowCastingBounds : bool
      Passed on as it is.
    """
    #  void QQuick3DDebugSettings::setDrawShadowCastingBounds(bool
    #      newDrawShadowCastingBounds)
    self.uglySide.call(
        'ritual_ZN21QQuick3DDebugSettings26setDrawShadowCastingBoundsEb',
        newDrawShadowCastingBounds,
    )

  @overload(bool)
  def setDrawShadowReceivingBounds(
      self,
      newDrawShadowReceivingBounds: bool,
  ) -> None:
    """
    Calls Qt's 'void QQuick3DDebugSettings::setDrawShadowReceivingBounds(bool
    newDrawShadowReceivingBounds)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddebugsettings.html

    Parameters
    ----------

    newDrawShadowReceivingBounds : bool
      Passed on as it is.
    """
    #  void QQuick3DDebugSettings::setDrawShadowReceivingBounds(bool
    #      newDrawShadowReceivingBounds)
    self.uglySide.call(
        'ritual_ZN21QQuick3DDebugSettings28setDrawShadowReceivingBoundsEb',
        newDrawShadowReceivingBounds,
    )

  @overload(bool)
  def setDrawCascades(self, newDrawCascades: bool) -> None:
    """
    Calls Qt's 'void QQuick3DDebugSettings::setDrawCascades(bool
    newDrawCascades)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddebugsettings.html#setDrawCascades

    Parameters
    ----------

    newDrawCascades : bool
      Passed on as it is.
    """
    #  void QQuick3DDebugSettings::setDrawCascades(bool newDrawCascades)
    self.uglySide.call(
        'ritual_ZN21QQuick3DDebugSettings15setDrawCascadesEb',
        newDrawCascades,
    )

  @overload(bool)
  def setDrawSceneCascadeIntersection(
      self,
      newDrawSceneCascadeIntersection: bool,
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DDebugSettings::setDrawSceneCascadeIntersection(bool
    newDrawSceneCascadeIntersection)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddebugsettings.html

    Parameters
    ----------

    newDrawSceneCascadeIntersection : bool
      Passed on as it is.
    """
    #  void QQuick3DDebugSettings::setDrawSceneCascadeIntersection(bool
    #      newDrawSceneCascadeIntersection)
    self.uglySide.call(
        'ritual_ZN21QQuick3DDebugSettings31setDrawSceneCascadeIntersectionE'
        'b',
        newDrawSceneCascadeIntersection,
    )

  @overload(bool)
  def setDisableShadowCameraUpdate(
      self,
      newDisableShadowCameraUpdate: bool,
  ) -> None:
    """
    Calls Qt's 'void QQuick3DDebugSettings::setDisableShadowCameraUpdate(bool
    newDisableShadowCameraUpdate)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddebugsettings.html

    Parameters
    ----------

    newDisableShadowCameraUpdate : bool
      Passed on as it is.
    """
    #  void QQuick3DDebugSettings::setDisableShadowCameraUpdate(bool
    #      newDisableShadowCameraUpdate)
    self.uglySide.call(
        'ritual_ZN21QQuick3DDebugSettings28setDisableShadowCameraUpdateEb',
        newDisableShadowCameraUpdate,
    )

  @overload(bool)
  def setDrawCulledObjects(self, newDrawCulledObjects: bool) -> None:
    """
    Calls Qt's 'void QQuick3DDebugSettings::setDrawCulledObjects(bool
    newDrawCulledObjects)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddebugsettings.html#setDrawCulledObjects

    Parameters
    ----------

    newDrawCulledObjects : bool
      Passed on as it is.
    """
    #  void QQuick3DDebugSettings::setDrawCulledObjects(bool
    #      newDrawCulledObjects)
    self.uglySide.call(
        'ritual_ZN21QQuick3DDebugSettings20setDrawCulledObjectsEb',
        newDrawCulledObjects,
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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QQuick3DDebugSettings::QQuick3DDebugSettings(QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddebugsettings.html#QQuick3DDebugSettings

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuick3DDebugSettings::QQuick3DDebugSettings(QObject *parent)
    self._noteCreation(QQuick3DDebugSettings, lambda: Rituals.call(
        'ritual_ZN21QQuick3DDebugSettingsC1EP7QObject',
        self._addressOf(parent, 'QObject'),
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

  def materialOverrideChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DDebugSettings::materialOverrideChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddebugsettings.html#materialOverrideChanged
    """
    #  void QQuick3DDebugSettings::materialOverrideChanged()
    self.uglySide.call(
        'ritual_ZN21QQuick3DDebugSettings23materialOverrideChangedEv',
    )

  def wireframeEnabledChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DDebugSettings::wireframeEnabledChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddebugsettings.html#wireframeEnabledChanged
    """
    #  void QQuick3DDebugSettings::wireframeEnabledChanged()
    self.uglySide.call(
        'ritual_ZN21QQuick3DDebugSettings23wireframeEnabledChangedEv',
    )

  def drawDirectionalLightShadowBoxesChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuick3DDebugSettings::drawDirectionalLightShadowBoxesChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddebugsettings.html
    """
    #  void QQuick3DDebugSettings::drawDirectionalLightShadowBoxesChanged()
    self.uglySide.call(
        'ritual_ZN21QQuick3DDebugSettings38drawDirectionalLightShadowBoxesC'
        'hangedEv',
    )

  def drawPointLightShadowBoxesChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuick3DDebugSettings::drawPointLightShadowBoxesChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddebugsettings.html
    """
    #  void QQuick3DDebugSettings::drawPointLightShadowBoxesChanged()
    self.uglySide.call(
        'ritual_ZN21QQuick3DDebugSettings32drawPointLightShadowBoxesChanged'
        'Ev',
    )

  def drawShadowCastingBoundsChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuick3DDebugSettings::drawShadowCastingBoundsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddebugsettings.html
    """
    #  void QQuick3DDebugSettings::drawShadowCastingBoundsChanged()
    self.uglySide.call(
        'ritual_ZN21QQuick3DDebugSettings30drawShadowCastingBoundsChangedEv',
    )

  def drawShadowReceivingBoundsChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuick3DDebugSettings::drawShadowReceivingBoundsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddebugsettings.html
    """
    #  void QQuick3DDebugSettings::drawShadowReceivingBoundsChanged()
    self.uglySide.call(
        'ritual_ZN21QQuick3DDebugSettings32drawShadowReceivingBoundsChanged'
        'Ev',
    )

  def drawCascadesChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DDebugSettings::drawCascadesChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddebugsettings.html#drawCascadesChanged
    """
    #  void QQuick3DDebugSettings::drawCascadesChanged()
    self.uglySide.call(
        'ritual_ZN21QQuick3DDebugSettings19drawCascadesChangedEv',
    )

  def drawSceneCascadeIntersectionChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuick3DDebugSettings::drawSceneCascadeIntersectionChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddebugsettings.html
    """
    #  void QQuick3DDebugSettings::drawSceneCascadeIntersectionChanged()
    self.uglySide.call(
        'ritual_ZN21QQuick3DDebugSettings35drawSceneCascadeIntersectionChan'
        'gedEv',
    )

  def disableShadowCameraUpdateChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuick3DDebugSettings::disableShadowCameraUpdateChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddebugsettings.html
    """
    #  void QQuick3DDebugSettings::disableShadowCameraUpdateChanged()
    self.uglySide.call(
        'ritual_ZN21QQuick3DDebugSettings32disableShadowCameraUpdateChanged'
        'Ev',
    )

  def drawCulledObjectsChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DDebugSettings::drawCulledObjectsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddebugsettings.html
    """
    #  void QQuick3DDebugSettings::drawCulledObjectsChanged()
    self.uglySide.call(
        'ritual_ZN21QQuick3DDebugSettings24drawCulledObjectsChangedEv',
    )

  def changed(self) -> None:
    """
    Calls Qt's 'void QQuick3DDebugSettings::changed()'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3ddebugsettings.html#changed
    """
    #  void QQuick3DDebugSettings::changed()
    self.uglySide.call('ritual_ZN21QQuick3DDebugSettings7changedEv')

  def update(self) -> None:
    """
    Calls Qt's 'void QQuick3DDebugSettings::update()'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3ddebugsettings.html#update
    """
    #  void QQuick3DDebugSettings::update()
    self.uglySide.call('ritual_ZN21QQuick3DDebugSettings6updateEv')
