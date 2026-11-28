"""
Qt3DRender::Render::GLTFSkeletonLoader binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/6.12.0/Qt3DRender/private/gltfskeletonloader_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means Qt3DRender::Render::GLTFSkeletonLoader to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore
from . import Qt3DRender

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QByteArray, QJsonDocument, QJsonObject
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QJsonDocument = WAIT['QJsonDocument']
  QJsonObject = WAIT['QJsonObject']


class GLTFSkeletonLoader(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's Qt3DRender::Render::GLTFSkeletonLoader: a plain
  Python object standing in front of one C++
  Qt3DRender::Render::GLTFSkeletonLoader.

  C++ hands a Qt3DRender::Render::GLTFSkeletonLoader around as a copy, so
  every C++ Qt3DRender::Render::GLTFSkeletonLoader behind a cute one is
  Python's own: it is removed, by the ritual named in '__delete_ritual__',
  when the cute object goes.

  What exists
  -----------

  Every function of Qt's Qt3DRender::Render::GLTFSkeletonLoader that has a
  ritual and that Python can call so far, 10 names in all: 'createSkeleton',
  'accessorTypeFromJSON', 'accessorTypeSize', 'accessorDataSizeFromJson',
  'setBasePath', 'setJSON', 'cleanup', 'processJSONBuffer',
  'setupNodeParentLinks', 'resolveLocalData'. It can be made from Python, in
  1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'SkeletonData
    Qt3DRender::Render::GLTFSkeletonLoader::createSkeletonFromSkin(const Skin
    &skin) const': takes a type Python has no way to hand over yet.
  - Qt's 'QMatrix4x4
    Qt3DRender::Render::GLTFSkeletonLoader::inverseBindMatrix(const Skin
    &skin, int jointIndex) const': takes a type Python has no way to hand
    over yet.
  - Qt's 'RawData Qt3DRender::Render::GLTFSkeletonLoader::accessorData(int
    accessorIndex, int index) const': gives a type Python has no way to take
    yet.
  - Qt's 'Qt3DRender::Render::GLTFSkeletonLoader::~GLTFSkeletonLoader()': the
    destructor: Python removes its C++ Qt3DRender::Render::GLTFSkeletonLoader
    by it, and has no other use for it.

  What has no ritual
  ------------------

  7 of the 22 functions Qt declares: 7 leans on 'Qt3DRender.

  What to expect
  --------------

  - The C++ Qt3DRender::Render::GLTFSkeletonLoader is created at the first
    use, not by 'Qt3DRender::Render::GLTFSkeletonLoader(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a Qt3DRender::Render::GLTFSkeletonLoader back gives a
    copy the ritual made for Python, in a new cute
    Qt3DRender::Render::GLTFSkeletonLoader.
  - Each name of Qt's Qt3DRender::Render::GLTFSkeletonLoader that has no cute
    function yet, 'accessorData', 'createSkeletonFromSkin',
    'inverseBindMatrix', 'load', 'parse', 'parseGLTF2',
    'processJSONAccessor', 'processJSONBufferView', 'processJSONNode',
    'processJSONSkin', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(int)
  def accessorTypeFromJSON(
      componentType: int,
  ) -> Qt3DCore.QAttribute.VertexBaseType:
    """
    Calls Qt's 'Qt3DCore::QAttribute::VertexBaseType
    Qt3DRender::Render::GLTFSkeletonLoader::accessorTypeFromJSON(int
    componentType)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-gltfskeletonloader.html

    Parameters
    ----------

    componentType : int
      Passed on as it is.

    Returns
    -------

    Qt3DCore.QAttribute.VertexBaseType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt3DCore.QAttribute.VertexBaseType(number)' gives.
    """
    #  Qt3DCore::QAttribute::VertexBaseType
    #      Qt3DRender::Render::GLTFSkeletonLoader::accessorTypeFromJSON(int
    #      componentType)
    return Qt3DCore.QAttribute.VertexBaseType(Rituals.call(
        'ritual_ZN10Qt3DRender6Render18GLTFSkeletonLoader20accessorTypeFrom'
        'JSONEi',
        componentType,
    ))

  @staticmethod
  @overload(Qt3DCore.QAttribute.VertexBaseType)
  def accessorTypeSize(
      componentType: Qt3DCore.QAttribute.VertexBaseType,
  ) -> int:
    """
    Calls Qt's 'uint
    Qt3DRender::Render::GLTFSkeletonLoader::accessorTypeSize(Qt3DCore::
    QAttribute::VertexBaseType componentType)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-gltfskeletonloader.html

    Parameters
    ----------

    componentType : Qt3DCore.QAttribute.VertexBaseType
      Passed on as its number.
    """
    #  uint Qt3DRender::Render::GLTFSkeletonLoader::accessorTypeSize(
    #      Qt3DCore::QAttribute::VertexBaseType componentType)
    return Rituals.call(
        'ritual_ZN10Qt3DRender6Render18GLTFSkeletonLoader16accessorTypeSize'
        'EN8Qt3DCore10QAttribute14VertexBaseTypeE',
        componentType.value,
    )

  @staticmethod
  @overload(str)
  def accessorDataSizeFromJson(type: str) -> int:
    """
    Calls Qt's 'uint
    Qt3DRender::Render::GLTFSkeletonLoader::accessorDataSizeFromJson(const
    QString &type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-gltfskeletonloader.html

    Parameters
    ----------

    type : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  uint Qt3DRender::Render::GLTFSkeletonLoader::accessorDataSizeFromJson(
    #      const QString &type)
    return Rituals.call(
        'ritual_ZN10Qt3DRender6Render18GLTFSkeletonLoader24accessorDataSize'
        'FromJsonERK7QString',
        type,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::Render::GLTFSkeletonLoader'

  #  Qt's '~Qt3DRender::Render::GLTFSkeletonLoader()'. Naming it makes this a
  #  value class: Python owns every C++
  #  Qt3DRender::Render::GLTFSkeletonLoader behind a cute one, and removes it
  #  by this ritual.
  __delete_ritual__ = 'ritual_ZN10Qt3DRender6Render18GLTFSkeletonLoaderD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def resolveLocalData(self, path: str) -> QByteArray:
    """
    Calls Qt's 'QByteArray
    Qt3DRender::Render::GLTFSkeletonLoader::resolveLocalData(const QString
    &path) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-gltfskeletonloader.html

    Parameters
    ----------

    path : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray
    #      Qt3DRender::Render::GLTFSkeletonLoader::resolveLocalData(const
    #      QString &path) const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render18GLTFSkeletonLoader16resolveLocalDat'
        'aERK7QString',
        path,
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setBasePath(self, path: str) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Render::GLTFSkeletonLoader::setBasePath(const QString
    &path)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-gltfskeletonloader.html

    Parameters
    ----------

    path : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void Qt3DRender::Render::GLTFSkeletonLoader::setBasePath(const QString
    #      &path)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render18GLTFSkeletonLoader11setBasePathERK7Q'
        'String',
        path,
    )

  @overload(QJsonDocument)
  def setJSON(self, json: QJsonDocument) -> bool:
    """
    Calls Qt's 'bool Qt3DRender::Render::GLTFSkeletonLoader::setJSON(const
    QJsonDocument &json)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-gltfskeletonloader.html#setJSON

    Parameters
    ----------

    json : QJsonDocument
      Passed on as a value: Qt reads the C++ QJsonDocument, which stays
      Python's own.
    """
    #  bool Qt3DRender::Render::GLTFSkeletonLoader::setJSON(const
    #      QJsonDocument &json)
    return self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render18GLTFSkeletonLoader7setJSONERK13QJson'
        'Document',
        self._valueOf(json),
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
    'Qt3DRender::Render::GLTFSkeletonLoader::GLTFSkeletonLoader()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-gltfskeletonloader.html
    """
    #  Qt3DRender::Render::GLTFSkeletonLoader::GLTFSkeletonLoader()
    self._noteCreation(GLTFSkeletonLoader, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender6Render18GLTFSkeletonLoaderC1Ev',
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
  def createSkeleton(
      self,
      skeletonName: str,
  ) -> Qt3DRender.Render.SkeletonData:
    """
    Calls Qt's 'SkeletonData
    Qt3DRender::Render::GLTFSkeletonLoader::createSkeleton(const QString
    &skeletonName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-gltfskeletonloader.html

    Parameters
    ----------

    skeletonName : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    Qt3DRender.Render.SkeletonData
      A new cute Qt3DRender::Render::SkeletonData around the copy Qt gave
      back. Python owns it.
    """
    #  SkeletonData
    #      Qt3DRender::Render::GLTFSkeletonLoader::createSkeleton(const
    #      QString &skeletonName)
    address = self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render18GLTFSkeletonLoader14createSkeletonER'
        'K7QString',
        skeletonName,
    )
    return Qt3DRender.Render.SkeletonData._cuteOwning(address)

  def cleanup(self) -> None:
    """
    Calls Qt's 'void Qt3DRender::Render::GLTFSkeletonLoader::cleanup()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-gltfskeletonloader.html#cleanup
    """
    #  void Qt3DRender::Render::GLTFSkeletonLoader::cleanup()
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render18GLTFSkeletonLoader7cleanupEv',
    )

  @overload(QJsonObject)
  def processJSONBuffer(self, json: QJsonObject) -> bool:
    """
    Calls Qt's 'bool
    Qt3DRender::Render::GLTFSkeletonLoader::processJSONBuffer(const
    QJsonObject &json)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-gltfskeletonloader.html

    Parameters
    ----------

    json : QJsonObject
      Passed on as a value: Qt reads the C++ QJsonObject, which stays
      Python's own.
    """
    #  bool Qt3DRender::Render::GLTFSkeletonLoader::processJSONBuffer(const
    #      QJsonObject &json)
    return self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render18GLTFSkeletonLoader17processJSONBuffe'
        'rERK11QJsonObject',
        self._valueOf(json),
    )

  def setupNodeParentLinks(self) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Render::GLTFSkeletonLoader::setupNodeParentLinks()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-gltfskeletonloader.html
    """
    #  void Qt3DRender::Render::GLTFSkeletonLoader::setupNodeParentLinks()
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render18GLTFSkeletonLoader20setupNodeParentL'
        'inksEv',
    )

  @staticmethod
  def accessorData(*__, **_) -> Never:
    """
    Qt's 'RawData Qt3DRender::Render::GLTFSkeletonLoader::accessorData(int
    accessorIndex, int index) const': gives a type Python has no way to take
    yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.GLTFSkeletonLoader.accessorData' has no cute "
        "function yet. Qt's 'RawData "
        "Qt3DRender::Render::GLTFSkeletonLoader::accessorData(int "
        "accessorIndex, int index) const': gives a type Python has no way "
        "to take yet.")

  @staticmethod
  def createSkeletonFromSkin(*__, **_) -> Never:
    """
    Qt's 'SkeletonData
    Qt3DRender::Render::GLTFSkeletonLoader::createSkeletonFromSkin(const Skin
    &skin) const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.GLTFSkeletonLoader.createSkeletonFromSkin' has "
        "no cute function yet. Qt's 'SkeletonData "
        "Qt3DRender::Render::GLTFSkeletonLoader::createSkeletonFromSkin(cons"
        "t Skin &skin) const': takes a type Python has no way to hand over "
        "yet.")

  @staticmethod
  def inverseBindMatrix(*__, **_) -> Never:
    """
    Qt's 'QMatrix4x4
    Qt3DRender::Render::GLTFSkeletonLoader::inverseBindMatrix(const Skin
    &skin, int jointIndex) const': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.GLTFSkeletonLoader.inverseBindMatrix' has no "
        "cute function yet. Qt's 'QMatrix4x4 "
        "Qt3DRender::Render::GLTFSkeletonLoader::inverseBindMatrix(const "
        "Skin &skin, int jointIndex) const': takes a type Python has no way "
        "to hand over yet.")

  @staticmethod
  def load(*__, **_) -> Never:
    """
    Qt's 'bool Qt3DRender::Render::GLTFSkeletonLoader::load(QIODevice
    *ioDev)': leans on
    'Qt3DRender::Render::GLTFSkeletonLoader::BufferView::BufferView(
    QJsonObject const&)', which Qt's source does not mark for use from
    outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.GLTFSkeletonLoader.load' has no cute function "
        "yet. Qt's 'bool "
        "Qt3DRender::Render::GLTFSkeletonLoader::load(QIODevice *ioDev)': "
        "leans on "
        "'Qt3DRender::Render::GLTFSkeletonLoader::BufferView::BufferView(QJs"
        "onObject const&)', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken.")

  @staticmethod
  def parse(*__, **_) -> Never:
    """
    Qt's 'bool Qt3DRender::Render::GLTFSkeletonLoader::parse()': leans on
    'Qt3DRender::Render::GLTFSkeletonLoader::BufferView::BufferView(
    QJsonObject const&)', which Qt's source does not mark for use from
    outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.GLTFSkeletonLoader.parse' has no cute function "
        "yet. Qt's 'bool Qt3DRender::Render::GLTFSkeletonLoader::parse()': "
        "leans on "
        "'Qt3DRender::Render::GLTFSkeletonLoader::BufferView::BufferView(QJs"
        "onObject const&)', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken.")

  @staticmethod
  def parseGLTF2(*__, **_) -> Never:
    """
    Qt's 'bool Qt3DRender::Render::GLTFSkeletonLoader::parseGLTF2()': leans
    on 'Qt3DRender::Render::GLTFSkeletonLoader::BufferView::BufferView(
    QJsonObject const&)', which Qt's source does not mark for use from
    outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.GLTFSkeletonLoader.parseGLTF2' has no cute "
        "function yet. Qt's 'bool "
        "Qt3DRender::Render::GLTFSkeletonLoader::parseGLTF2()': leans on "
        "'Qt3DRender::Render::GLTFSkeletonLoader::BufferView::BufferView(QJs"
        "onObject const&)', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken.")

  @staticmethod
  def processJSONAccessor(*__, **_) -> Never:
    """
    Qt's 'bool
    Qt3DRender::Render::GLTFSkeletonLoader::processJSONAccessor(const
    QJsonObject &json)': leans on
    'Qt3DRender::Render::GLTFSkeletonLoader::AccessorData::AccessorData(
    QJsonObject const&)', which Qt's source does not mark for use from
    outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.GLTFSkeletonLoader.processJSONAccessor' has no "
        "cute function yet. Qt's 'bool "
        "Qt3DRender::Render::GLTFSkeletonLoader::processJSONAccessor(const "
        "QJsonObject &json)': leans on "
        "'Qt3DRender::Render::GLTFSkeletonLoader::AccessorData::AccessorData"
        "(QJsonObject const&)', which Qt's source does not mark for use "
        "from outside Qt and has no code for that could be taken.")

  @staticmethod
  def processJSONBufferView(*__, **_) -> Never:
    """
    Qt's 'bool
    Qt3DRender::Render::GLTFSkeletonLoader::processJSONBufferView(const
    QJsonObject &json)': leans on
    'Qt3DRender::Render::GLTFSkeletonLoader::BufferView::BufferView(
    QJsonObject const&)', which Qt's source does not mark for use from
    outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.GLTFSkeletonLoader.processJSONBufferView' has "
        "no cute function yet. Qt's 'bool "
        "Qt3DRender::Render::GLTFSkeletonLoader::processJSONBufferView(const"
        " QJsonObject &json)': leans on "
        "'Qt3DRender::Render::GLTFSkeletonLoader::BufferView::BufferView(QJs"
        "onObject const&)', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken.")

  @staticmethod
  def processJSONNode(*__, **_) -> Never:
    """
    Qt's 'bool Qt3DRender::Render::GLTFSkeletonLoader::processJSONNode(const
    QJsonObject &json)': leans on
    'Qt3DRender::Render::GLTFSkeletonLoader::Node::Node(QJsonObject const&)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.GLTFSkeletonLoader.processJSONNode' has no cute "
        "function yet. Qt's 'bool "
        "Qt3DRender::Render::GLTFSkeletonLoader::processJSONNode(const "
        "QJsonObject &json)': leans on "
        "'Qt3DRender::Render::GLTFSkeletonLoader::Node::Node(QJsonObject "
        "const&)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

  @staticmethod
  def processJSONSkin(*__, **_) -> Never:
    """
    Qt's 'bool Qt3DRender::Render::GLTFSkeletonLoader::processJSONSkin(const
    QJsonObject &json)': leans on
    'Qt3DRender::Render::GLTFSkeletonLoader::Skin::Skin(QJsonObject const&)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.GLTFSkeletonLoader.processJSONSkin' has no cute "
        "function yet. Qt's 'bool "
        "Qt3DRender::Render::GLTFSkeletonLoader::processJSONSkin(const "
        "QJsonObject &json)': leans on "
        "'Qt3DRender::Render::GLTFSkeletonLoader::Skin::Skin(QJsonObject "
        "const&)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")
