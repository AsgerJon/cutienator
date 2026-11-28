"""
Qt3DRender::Render::ShaderBuilder binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/6.12.0/Qt3DRender/private/shaderbuilder_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means Qt3DRender::Render::ShaderBuilder to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import QStringList
from ..Qt3DCore import Qt3DCore
from . import Qt3DRender

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QUrl
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QUrl = WAIT['QUrl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class ShaderBuilder(Qt3DRender.Render.BackendNode):
  """
  The cute side of Qt's Qt3DRender::Render::ShaderBuilder: a plain Python
  object standing in front of one C++ Qt3DRender::Render::ShaderBuilder.

  It is built on the cute 'Qt3DRender::Render::BackendNode', as Qt's
  Qt3DRender::Render::ShaderBuilder is built on Qt's
  Qt3DRender::Render::BackendNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::Render::ShaderBuilder that has a ritual
  and that Python can call so far, 16 names in all: 'getPrototypesFile',
  'setPrototypesFile', 'getPrototypeNames', 'cleanup', 'shaderProgramId',
  'enabledLayers', 'graphicsApi', 'setGraphicsApi', 'shaderGraph',
  'setShaderGraph', 'shaderCode', 'isShaderCodeDirty', 'generateCode',
  'syncFromFrontEnd', 'hashKeyForShaderGraph', 'setEnabledLayers'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Qt3DRender::Render::ShaderBuilder::~ShaderBuilder()': the
    destructor: Python never removes a C++ Qt3DRender::Render::ShaderBuilder.
  - Qt's 'std::vector<ShaderBuilderUpdate>
    Qt3DRender::Render::ShaderBuilder::takePendingUpdates()': gives a type
    Python has no way to take yet.

  What to expect
  --------------

  - The C++ Qt3DRender::Render::ShaderBuilder is created at the first use,
    not by 'Qt3DRender::Render::ShaderBuilder(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::Render::ShaderBuilder.
  - Each name of Qt's Qt3DRender::Render::ShaderBuilder that has no cute
    function yet, 'takePendingUpdates', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def getPrototypesFile() -> str:
    """
    Calls Qt's 'QString
    Qt3DRender::Render::ShaderBuilder::getPrototypesFile()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-shaderbuilder.html

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString Qt3DRender::Render::ShaderBuilder::getPrototypesFile()
    return Rituals.call(
        'ritual_ZN10Qt3DRender6Render13ShaderBuilder17getPrototypesFileEv',
    )

  @staticmethod
  @overload(str)
  def setPrototypesFile(file: str) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Render::ShaderBuilder::setPrototypesFile(const QString
    &file)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-shaderbuilder.html

    Parameters
    ----------

    file : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void Qt3DRender::Render::ShaderBuilder::setPrototypesFile(const
    #      QString &file)
    Rituals.call(
        'ritual_ZN10Qt3DRender6Render13ShaderBuilder17setPrototypesFileERK7'
        'QString',
        file,
    )

  @staticmethod
  def getPrototypeNames() -> QStringList:
    """
    Calls Qt's 'QStringList
    Qt3DRender::Render::ShaderBuilder::getPrototypeNames()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-shaderbuilder.html

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList Qt3DRender::Render::ShaderBuilder::getPrototypeNames()
    address = Rituals.call(
        'ritual_ZN10Qt3DRender6Render13ShaderBuilder17getPrototypeNamesEv',
    )
    return QStringList._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::Render::ShaderBuilder'

  #  A C++ Qt3DRender::Render::ShaderBuilder Python makes is of a C++ class
  #  of ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DRender_Render_ShaderBuilder'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def shaderProgramId(self) -> Qt3DCore.QNodeId:
    """
    Calls Qt's 'Qt3DCore::QNodeId
    Qt3DRender::Render::ShaderBuilder::shaderProgramId() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-shaderbuilder.html

    Returns
    -------

    Qt3DCore.QNodeId
      A new cute Qt3DCore::QNodeId around the copy Qt gave back. Python owns
      it.
    """
    #  Qt3DCore::QNodeId Qt3DRender::Render::ShaderBuilder::shaderProgramId()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render13ShaderBuilder15shaderProgramIdEv',
    )
    return Qt3DCore.QNodeId._cuteOwning(address)

  def enabledLayers(self) -> QStringList:
    """
    Calls Qt's 'QStringList
    Qt3DRender::Render::ShaderBuilder::enabledLayers() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-shaderbuilder.html#enabledLayers

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList Qt3DRender::Render::ShaderBuilder::enabledLayers() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render13ShaderBuilder13enabledLayersEv',
    )
    return QStringList._cuteOwning(address)

  def graphicsApi(self) -> Qt3DRender.GraphicsApiFilterData:
    """
    Calls Qt's 'GraphicsApiFilterData
    Qt3DRender::Render::ShaderBuilder::graphicsApi() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-shaderbuilder.html#graphicsApi

    Returns
    -------

    Qt3DRender.GraphicsApiFilterData
      A new cute Qt3DRender::GraphicsApiFilterData around the copy Qt gave
      back. Python owns it.
    """
    #  GraphicsApiFilterData Qt3DRender::Render::ShaderBuilder::graphicsApi()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render13ShaderBuilder11graphicsApiEv',
    )
    return Qt3DRender.GraphicsApiFilterData._cuteOwning(address)

  @overload(Qt3DRender.QShaderProgram.ShaderType)
  def shaderGraph(self, type: Qt3DRender.QShaderProgram.ShaderType) -> QUrl:
    """
    Calls Qt's 'QUrl
    Qt3DRender::Render::ShaderBuilder::shaderGraph(QShaderProgram::ShaderType
    type) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-shaderbuilder.html#shaderGraph

    Parameters
    ----------

    type : Qt3DRender.QShaderProgram.ShaderType
      Passed on as its number.

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl Qt3DRender::Render::ShaderBuilder::shaderGraph(QShaderProgram::
    #      ShaderType type) const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render13ShaderBuilder11shaderGraphENS_14QSh'
        'aderProgram10ShaderTypeE',
        type.value,
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  @overload(Qt3DRender.QShaderProgram.ShaderType)
  def shaderCode(
      self,
      type: Qt3DRender.QShaderProgram.ShaderType,
  ) -> QByteArray:
    """
    Calls Qt's 'QByteArray
    Qt3DRender::Render::ShaderBuilder::shaderCode(QShaderProgram::ShaderType
    type) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-shaderbuilder.html#shaderCode

    Parameters
    ----------

    type : Qt3DRender.QShaderProgram.ShaderType
      Passed on as its number.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray
    #      Qt3DRender::Render::ShaderBuilder::shaderCode(QShaderProgram::
    #      ShaderType type) const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render13ShaderBuilder10shaderCodeENS_14QSha'
        'derProgram10ShaderTypeE',
        type.value,
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  @overload(Qt3DRender.QShaderProgram.ShaderType)
  def isShaderCodeDirty(
      self,
      type: Qt3DRender.QShaderProgram.ShaderType,
  ) -> bool:
    """
    Calls Qt's 'bool
    Qt3DRender::Render::ShaderBuilder::isShaderCodeDirty(QShaderProgram::
    ShaderType type) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-shaderbuilder.html

    Parameters
    ----------

    type : Qt3DRender.QShaderProgram.ShaderType
      Passed on as its number.
    """
    #  bool Qt3DRender::Render::ShaderBuilder::isShaderCodeDirty(
    #      QShaderProgram::ShaderType type) const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render13ShaderBuilder17isShaderCodeDirtyENS'
        '_14QShaderProgram10ShaderTypeE',
        type.value,
    )

  @overload(Qt3DRender.QShaderProgram.ShaderType)
  def hashKeyForShaderGraph(
      self,
      type: Qt3DRender.QShaderProgram.ShaderType,
  ) -> QByteArray:
    """
    Calls Qt's 'QByteArray
    Qt3DRender::Render::ShaderBuilder::hashKeyForShaderGraph(
    QShaderProgram::ShaderType type) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-shaderbuilder.html

    Parameters
    ----------

    type : Qt3DRender.QShaderProgram.ShaderType
      Passed on as its number.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray Qt3DRender::Render::ShaderBuilder::hashKeyForShaderGraph(
    #      QShaderProgram::ShaderType type) const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render13ShaderBuilder21hashKeyForShaderGrap'
        'hENS_14QShaderProgram10ShaderTypeE',
        type.value,
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(WAIT['Qt3DRender.GraphicsApiFilterData'])
  def setGraphicsApi(
      self,
      graphicsApi: Qt3DRender.GraphicsApiFilterData,
  ) -> None:
    """
    Calls Qt's 'void Qt3DRender::Render::ShaderBuilder::setGraphicsApi(const
    GraphicsApiFilterData &graphicsApi)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-shaderbuilder.html

    Parameters
    ----------

    graphicsApi : Qt3DRender.GraphicsApiFilterData
      Passed on as a value: Qt reads the C++
      Qt3DRender::GraphicsApiFilterData, which stays Python's own.
    """
    #  void Qt3DRender::Render::ShaderBuilder::setGraphicsApi(const
    #      GraphicsApiFilterData &graphicsApi)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render13ShaderBuilder14setGraphicsApiERKNS_2'
        '1GraphicsApiFilterDataE',
        self._valueOf(graphicsApi),
    )

  @overload(Qt3DRender.QShaderProgram.ShaderType, QUrl)
  def setShaderGraph(
      self,
      type: Qt3DRender.QShaderProgram.ShaderType,
      url: QUrl,
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Render::ShaderBuilder::setShaderGraph(QShaderProgram::
    ShaderType type, const QUrl &url)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-shaderbuilder.html

    Parameters
    ----------

    type : Qt3DRender.QShaderProgram.ShaderType
      Passed on as its number.

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void Qt3DRender::Render::ShaderBuilder::setShaderGraph(
    #      QShaderProgram::ShaderType type, const QUrl &url)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render13ShaderBuilder14setShaderGraphENS_14Q'
        'ShaderProgram10ShaderTypeERK4QUrl',
        type.value, self._valueOf(url),
    )

  @overload(QStringList)
  def setEnabledLayers(self, layers: QStringList) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Render::ShaderBuilder::setEnabledLayers(const QStringList
    &layers)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-shaderbuilder.html

    Parameters
    ----------

    layers : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void Qt3DRender::Render::ShaderBuilder::setEnabledLayers(const
    #      QStringList &layers)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render13ShaderBuilder16setEnabledLayersERK5Q'
        'ListI7QStringE',
        self._valueOf(layers),
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
    'Qt3DRender::Render::ShaderBuilder::ShaderBuilder()', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-shaderbuilder.html#ShaderBuilder
    """
    #  Qt3DRender::Render::ShaderBuilder::ShaderBuilder()
    self._noteCreation(ShaderBuilder, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender6Render13ShaderBuilderC1Ev',
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

  def cleanup(self) -> None:
    """
    Calls Qt's 'void Qt3DRender::Render::ShaderBuilder::cleanup()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-shaderbuilder.html#cleanup
    """
    #  void Qt3DRender::Render::ShaderBuilder::cleanup()
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render13ShaderBuilder7cleanupEv',
    )

  @overload(Qt3DRender.QShaderProgram.ShaderType)
  def generateCode(self, type: Qt3DRender.QShaderProgram.ShaderType) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Render::ShaderBuilder::generateCode(QShaderProgram::
    ShaderType type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-shaderbuilder.html#generateCode

    Parameters
    ----------

    type : Qt3DRender.QShaderProgram.ShaderType
      Passed on as its number.
    """
    #  void Qt3DRender::Render::ShaderBuilder::generateCode(QShaderProgram::
    #      ShaderType type)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render13ShaderBuilder12generateCodeENS_14QSh'
        'aderProgram10ShaderTypeE',
        type.value,
    )

  @overload(WAIT['Qt3DCore.QNode'], bool)
  @overload(NoneType, bool)
  def syncFromFrontEnd(
      self,
      frontEnd: Optional[Qt3DCore.QNode],
      firstTime: bool,
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Render::ShaderBuilder::syncFromFrontEnd(const Qt3DCore::QNode
    *frontEnd, bool firstTime)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-shaderbuilder.html

    Parameters
    ----------

    frontEnd : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    firstTime : bool
      Passed on as it is.
    """
    #  void Qt3DRender::Render::ShaderBuilder::syncFromFrontEnd(const
    #      Qt3DCore::QNode *frontEnd, bool firstTime)
    ritual = (
        'ritual_ZN10Qt3DRender6Render13ShaderBuilder16syncFromFrontEndEPKN8'
        'Qt3DCore5QNodeEb')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN10Qt3DRender6Render13ShaderBuilder16syncFromFrontEn'
          'dEPKN8Qt3DCore5QNodeEb')
    self.uglySide.call(ritual, self._addressOf(frontEnd), firstTime)

  @staticmethod
  def takePendingUpdates(*__, **_) -> Never:
    """
    Qt's 'std::vector<ShaderBuilderUpdate>
    Qt3DRender::Render::ShaderBuilder::takePendingUpdates()': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.ShaderBuilder.takePendingUpdates' has no cute "
        "function yet. Qt's 'std::vector<ShaderBuilderUpdate> "
        "Qt3DRender::Render::ShaderBuilder::takePendingUpdates()': gives a "
        "type Python has no way to take yet.")
