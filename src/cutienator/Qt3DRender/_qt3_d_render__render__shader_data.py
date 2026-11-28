"""
Qt3DRender::Render::ShaderData binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/6.12.0/Qt3DRender/private/shaderdata_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means Qt3DRender::Render::ShaderData to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore
from . import Qt3DRender

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QVariant
  from ..QtGui import QMatrix4x4
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMatrix4x4 = WAIT['QMatrix4x4']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class ShaderData(Qt3DRender.Render.BackendNode):
  """
  The cute side of Qt's Qt3DRender::Render::ShaderData: a plain Python object
  standing in front of one C++ Qt3DRender::Render::ShaderData.

  It is built on the cute 'Qt3DRender::Render::BackendNode', as Qt's
  Qt3DRender::Render::ShaderData is built on Qt's
  Qt3DRender::Render::BackendNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::Render::ShaderData that has a ritual and
  that Python can call so far, 7 names in all: 'updateWorldTransform',
  'getTransformedProperty', 'propertyTransformType', 'setManagers',
  'syncFromFrontEnd', 'generatePropertyValuesForBlockIfNeeded',
  'lookupResource'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Qt3DRender::Render::ShaderData::~ShaderData()': the destructor:
    Python never removes a C++ Qt3DRender::Render::ShaderData.
  - Qt's 'const QHash<QString, PropertyValue>
    &Qt3DRender::Render::ShaderData::properties() const': gives a type Python
    has no way to take yet.
  - Qt's 'const PropertyValuesForBlock
    &Qt3DRender::Render::ShaderData::propertyValuesForBlock(int blockNameId)
    const': gives a type Python has no way to take yet.

  What to expect
  --------------

  - The C++ Qt3DRender::Render::ShaderData is created at the first use, not
    by 'Qt3DRender::Render::ShaderData(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::Render::ShaderData.
  - Each name of Qt's Qt3DRender::Render::ShaderData that has no cute
    function yet, 'properties', 'propertyValuesForBlock', holds a function
    that raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside Qt3DRender::Render::ShaderData, each a class
  #  in here as in C++, and the names Qt has for the combinations of its
  #  flags enums.

  class TransformType(CuteNum):
    """
    The enum 'Qt3DRender::Render::ShaderData::TransformType' of Qt, with the
    4 names Qt gives in it.
    """

    NoTransform = Kee[int](-1)
    ModelToEye = Kee[int](0)
    ModelToWorld = Kee[int](1)
    ModelToWorldDirection = Kee[int](2)

  #  The classes Qt writes inside Qt3DRender::Render::ShaderData, each a
  #  class in here as in C++.

  class PropertyValue(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's Qt3DRender::Render::ShaderData::PropertyValue: a
    plain Python object standing in front of one C++
    Qt3DRender::Render::ShaderData::PropertyValue.

    C++ hands a Qt3DRender::Render::ShaderData::PropertyValue around as a
    copy, so every C++ Qt3DRender::Render::ShaderData::PropertyValue behind a
    cute one is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's Qt3DRender::Render::ShaderData::PropertyValue yet.
    None can be made from Python: one comes out of a function of another
    class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'Qt3DRender::Render::ShaderData::PropertyValue::~PropertyValue()':
      the destructor: Python removes its C++
      Qt3DRender::Render::ShaderData::PropertyValue by it, and has no other
      use for it.

    What to expect
    --------------

    - The C++ Qt3DRender::Render::ShaderData::PropertyValue is created at the
      first use, not by 'Qt3DRender::Render::ShaderData::PropertyValue(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a Qt3DRender::Render::ShaderData::PropertyValue back
      gives a copy the ritual made for Python, in a new cute
      Qt3DRender::Render::ShaderData::PropertyValue.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'Qt3DRender::Render::ShaderData::PropertyValue'

    #  Qt's '~Qt3DRender::Render::ShaderData::PropertyValue()'. Naming it
    #  makes this a value class: Python owns every C++
    #  Qt3DRender::Render::ShaderData::PropertyValue behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN10Qt3DRender6Render10ShaderData13PropertyValueD1Ev')

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(WAIT['Qt3DRender.Render.NodeManagers'], WAIT['Qt3DCore.QNodeId'])
  @overload(NoneType, WAIT['Qt3DCore.QNodeId'])
  def lookupResource(
      managers: Optional[Qt3DRender.Render.NodeManagers],
      id: Qt3DCore.QNodeId,
  ) -> Optional[ShaderData]:
    """
    Calls Qt's 'ShaderData
    *Qt3DRender::Render::ShaderData::lookupResource(NodeManagers *managers,
    Qt3DCore::QNodeId id)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-shaderdata.html#lookupResource

    Parameters
    ----------

    managers : Optional[Qt3DRender.Render.NodeManagers]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    id : Qt3DCore.QNodeId
      Passed on as a value: Qt reads the C++ Qt3DCore::QNodeId, which stays
      Python's own.

    Returns
    -------

    Optional[ShaderData]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  ShaderData
    #      *Qt3DRender::Render::ShaderData::lookupResource(NodeManagers
    #      *managers, Qt3DCore::QNodeId id)
    address = Rituals.call(
        'ritual_ZN10Qt3DRender6Render10ShaderData14lookupResourceEPNS0_12No'
        'deManagersEN8Qt3DCore7QNodeIdE',
        CuteMixin._addressOf(managers), CuteMixin._valueOf(id),
    )
    return ShaderData._cuteAt(address)

  @overload(WAIT['Qt3DCore.QNodeId'])
  def lookupResource(self, id: Qt3DCore.QNodeId) -> Optional[ShaderData]:
    """
    Calls Qt's 'ShaderData
    *Qt3DRender::Render::ShaderData::lookupResource(Qt3DCore::QNodeId id)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-shaderdata.html#lookupResource

    Parameters
    ----------

    id : Qt3DCore.QNodeId
      Passed on as a value: Qt reads the C++ Qt3DCore::QNodeId, which stays
      Python's own.

    Returns
    -------

    Optional[ShaderData]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  ShaderData
    #      *Qt3DRender::Render::ShaderData::lookupResource(Qt3DCore::QNodeId
    #      id)
    address = self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render10ShaderData14lookupResourceEN8Qt3DCor'
        'e7QNodeIdE',
        self._valueOf(id),
    )
    return ShaderData._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::Render::ShaderData'

  #  A C++ Qt3DRender::Render::ShaderData Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DRender_Render_ShaderData'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(PropertyValue, QMatrix4x4)
  @overload(NoneType, QMatrix4x4)
  def getTransformedProperty(
      self,
      v: Optional[PropertyValue],
      viewMatrix: QMatrix4x4,
  ) -> QVariant:
    """
    Calls Qt's 'QVariant
    Qt3DRender::Render::ShaderData::getTransformedProperty(const
    PropertyValue *v, const Matrix4x4 &viewMatrix) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-shaderdata.html

    Parameters
    ----------

    v : Optional[PropertyValue]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    viewMatrix : QMatrix4x4
      Passed on as a value: Qt reads the C++ QMatrix4x4, which stays Python's
      own.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant Qt3DRender::Render::ShaderData::getTransformedProperty(const
    #      PropertyValue *v, const Matrix4x4 &viewMatrix) const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render10ShaderData22getTransformedPropertyE'
        'PKNS1_13PropertyValueERK10QMatrix4x4',
        self._addressOf(v), self._valueOf(viewMatrix),
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(str)
  def propertyTransformType(self, name: str) -> TransformType:
    """
    Calls Qt's 'TransformType
    Qt3DRender::Render::ShaderData::propertyTransformType(const QString
    &name) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-shaderdata.html

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    TransformType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'TransformType(number)'
      gives.
    """
    #  TransformType
    #      Qt3DRender::Render::ShaderData::propertyTransformType(const
    #      QString &name) const
    return ShaderData.TransformType(self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render10ShaderData21propertyTransformTypeER'
        'K7QString',
        name,
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(WAIT['Qt3DRender.Render.NodeManagers'])
  @overload(NoneType)
  def setManagers(
      self,
      managers: Optional[Qt3DRender.Render.NodeManagers],
  ) -> None:
    """
    Calls Qt's 'void Qt3DRender::Render::ShaderData::setManagers(NodeManagers
    *managers)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-shaderdata.html#setManagers

    Parameters
    ----------

    managers : Optional[Qt3DRender.Render.NodeManagers]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::Render::ShaderData::setManagers(NodeManagers
    #      *managers)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render10ShaderData11setManagersEPNS0_12NodeM'
        'anagersE',
        self._addressOf(managers),
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
    Notes what was given, for Qt's
    'Qt3DRender::Render::ShaderData::ShaderData()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-shaderdata.html#ShaderData
    """
    #  Qt3DRender::Render::ShaderData::ShaderData()
    self._noteCreation(ShaderData, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender6Render10ShaderDataC1Ev',
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

  @overload(QMatrix4x4)
  def updateWorldTransform(self, worldMatrix: QMatrix4x4) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Render::ShaderData::updateWorldTransform(const Matrix4x4
    &worldMatrix)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-shaderdata.html

    Parameters
    ----------

    worldMatrix : QMatrix4x4
      Passed on as a value: Qt reads the C++ QMatrix4x4, which stays Python's
      own.
    """
    #  void Qt3DRender::Render::ShaderData::updateWorldTransform(const
    #      Matrix4x4 &worldMatrix)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render10ShaderData20updateWorldTransformERK1'
        '0QMatrix4x4',
        self._valueOf(worldMatrix),
    )

  @overload(WAIT['Qt3DCore.QNode'], bool)
  @overload(NoneType, bool)
  def syncFromFrontEnd(
      self,
      frontEnd: Optional[Qt3DCore.QNode],
      firstTime: bool,
  ) -> None:
    """
    Calls Qt's 'void Qt3DRender::Render::ShaderData::syncFromFrontEnd(const
    Qt3DCore::QNode *frontEnd, bool firstTime)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-shaderdata.html#syncFromFrontEnd

    Parameters
    ----------

    frontEnd : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    firstTime : bool
      Passed on as it is.
    """
    #  void Qt3DRender::Render::ShaderData::syncFromFrontEnd(const
    #      Qt3DCore::QNode *frontEnd, bool firstTime)
    ritual = (
        'ritual_ZN10Qt3DRender6Render10ShaderData16syncFromFrontEndEPKN8Qt3'
        'DCore5QNodeEb')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN10Qt3DRender6Render10ShaderData16syncFromFrontEndEP'
          'KN8Qt3DCore5QNodeEb')
    self.uglySide.call(ritual, self._addressOf(frontEnd), firstTime)

  @overload(str)
  def generatePropertyValuesForBlockIfNeeded(self, blockName: str) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Render::ShaderData::generatePropertyValuesForBlockIfNeeded(
    const QString &blockName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-shaderdata.html

    Parameters
    ----------

    blockName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void Qt3DRender::Render::ShaderData::
    #      generatePropertyValuesForBlockIfNeeded(const QString &blockName)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render10ShaderData38generatePropertyValuesFo'
        'rBlockIfNeededERK7QString',
        blockName,
    )

  @staticmethod
  def properties(*__, **_) -> Never:
    """
    Qt's 'const QHash<QString, PropertyValue>
    &Qt3DRender::Render::ShaderData::properties() const': gives a type Python
    has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.ShaderData.properties' has no cute function "
        "yet. Qt's 'const QHash<QString, PropertyValue> "
        "&Qt3DRender::Render::ShaderData::properties() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def propertyValuesForBlock(*__, **_) -> Never:
    """
    Qt's 'const PropertyValuesForBlock
    &Qt3DRender::Render::ShaderData::propertyValuesForBlock(int blockNameId)
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.ShaderData.propertyValuesForBlock' has no cute "
        "function yet. Qt's 'const PropertyValuesForBlock "
        "&Qt3DRender::Render::ShaderData::propertyValuesForBlock(int "
        "blockNameId) const': gives a type Python has no way to take yet.")
