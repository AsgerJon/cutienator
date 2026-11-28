"""
QSSGRenderModelData binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderdata_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QSSGRenderModelData to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QSSGRenderModelData(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSSGRenderModelData: a plain Python object standing
  in front of one C++ QSSGRenderModelData.

  What exists
  -----------

  Every function of Qt's QSSGRenderModelData that has a ritual and that
  Python can call so far, 1 name in all: 'getThreadPoolThreshold'. None can
  be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSSGRenderModelData::QSSGRenderModelData(const
    QSSGGlobalRenderNodeDataPtr &globalNodeData)': takes a type Python has no
    way to hand over yet.
  - Qt's 'ModelViewProjections
    QSSGRenderModelData::getModelViewProjection(QSSGRenderNodeHandle h)
    const': takes a type Python has no way to hand over yet.
  - Qt's 'ModelViewProjections
    QSSGRenderModelData::getModelViewProjection(const QSSGRenderModel &model)
    const': takes a type Python has no way to hand over yet.
  - Qt's 'QMatrix3x3
    QSSGRenderModelData::getNormalMatrix(QSSGRenderNodeHandle h, QMatrix3x3
    defaultValue) const': takes a type Python has no way to hand over yet.
  - Qt's 'QMatrix3x3 QSSGRenderModelData::getNormalMatrix(const
    QSSGRenderModel &model) const': takes a type Python has no way to hand
    over yet.
  - Qt's 'QSSGRenderMesh *QSSGRenderModelData::getMesh(const QSSGRenderModel
    &model) const': takes a type Python has no way to hand over yet.
  - Qt's 'MaterialList QSSGRenderModelData::getMaterials(const
    QSSGRenderModel &model) const': takes a type Python has no way to hand
    over yet.
  - Qt's 'const QSSGGlobalRenderNodeDataPtr
    &QSSGRenderModelData::globalNodeData() const': gives a type Python has no
    way to take yet.
  - Qt's 'void QSSGRenderModelData::prepareMeshData(const QSSGModelsView
    &models, QSSGRenderer *renderer)': takes a type Python has no way to hand
    over yet.
  - Qt's 'void QSSGRenderModelData::prepareMaterials(const QSSGModelsView
    &models)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  5 of the 16 functions Qt declares: 4 forbidden; 1 leans on 'vtable for
  QRunnable.

  What to expect
  --------------

  - The C++ QSSGRenderModelData is created at the first use, not by
    'QSSGRenderModelData(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSSGRenderModelData.
  - Each name of Qt's QSSGRenderModelData that has no cute function yet,
    '__init__', 'getMaterials', 'getMesh', 'getModelViewProjection',
    'getNormalMatrix', 'globalNodeData', 'prepareMaterials',
    'prepareMeshData', 'updateModelData', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def getThreadPoolThreshold() -> int:
    """
    Calls Qt's 'quint32 QSSGRenderModelData::getThreadPoolThreshold()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrendermodeldata.html#getThreadPoolThreshold
    """
    #  quint32 QSSGRenderModelData::getThreadPoolThreshold()
    return Rituals.call(
        'ritual_ZN19QSSGRenderModelData22getThreadPoolThresholdEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSSGRenderModelData'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QSSGRenderModelData::QSSGRenderModelData(const
    QSSGGlobalRenderNodeDataPtr &globalNodeData)': takes a type Python has no
    way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGRenderModelData.__init__' has no cute function yet. Qt's "
        "'QSSGRenderModelData::QSSGRenderModelData(const "
        "QSSGGlobalRenderNodeDataPtr &globalNodeData)': takes a type Python "
        "has no way to hand over yet.")

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

  @staticmethod
  def getMaterials(*__, **_) -> Never:
    """
    Qt's 'MaterialList QSSGRenderModelData::getMaterials(const
    QSSGRenderModel &model) const': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'QSSGRenderModelData.getMaterials' has no cute function yet. Qt's "
        "'MaterialList QSSGRenderModelData::getMaterials(const "
        "QSSGRenderModel &model) const': takes a type Python has no way to "
        "hand over yet.")

  @staticmethod
  def getMesh(*__, **_) -> Never:
    """
    Qt's 'QSSGRenderMesh *QSSGRenderModelData::getMesh(const QSSGRenderModel
    &model) const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGRenderModelData.getMesh' has no cute function yet. Qt's "
        "'QSSGRenderMesh *QSSGRenderModelData::getMesh(const "
        "QSSGRenderModel &model) const': takes a type Python has no way to "
        "hand over yet.")

  @staticmethod
  def getModelViewProjection(*__, **_) -> Never:
    """
    - Qt's 'ModelViewProjections
      QSSGRenderModelData::getModelViewProjection(QSSGRenderNodeHandle h)
      const': takes a type Python has no way to hand over yet.
    - Qt's 'ModelViewProjections
      QSSGRenderModelData::getModelViewProjection(const QSSGRenderModel
      &model) const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGRenderModelData.getModelViewProjection' has no cute function "
        "yet. Qt's 'ModelViewProjections "
        "QSSGRenderModelData::getModelViewProjection(QSSGRenderNodeHandle "
        "h) const': takes a type Python has no way to hand over yet. Qt's "
        "'ModelViewProjections "
        "QSSGRenderModelData::getModelViewProjection(const QSSGRenderModel "
        "&model) const': takes a type Python has no way to hand over yet.")

  @staticmethod
  def getNormalMatrix(*__, **_) -> Never:
    """
    - Qt's 'QMatrix3x3
      QSSGRenderModelData::getNormalMatrix(QSSGRenderNodeHandle h, QMatrix3x3
      defaultValue) const': takes a type Python has no way to hand over yet.
    - Qt's 'QMatrix3x3 QSSGRenderModelData::getNormalMatrix(const
      QSSGRenderModel &model) const': takes a type Python has no way to hand
      over yet.
    """
    raise NotImplementedError(
        "'QSSGRenderModelData.getNormalMatrix' has no cute function yet. "
        "Qt's 'QMatrix3x3 "
        "QSSGRenderModelData::getNormalMatrix(QSSGRenderNodeHandle h, "
        "QMatrix3x3 defaultValue) const': takes a type Python has no way to "
        "hand over yet. Qt's 'QMatrix3x3 "
        "QSSGRenderModelData::getNormalMatrix(const QSSGRenderModel &model) "
        "const': takes a type Python has no way to hand over yet.")

  @staticmethod
  def globalNodeData(*__, **_) -> Never:
    """
    Qt's 'const QSSGGlobalRenderNodeDataPtr
    &QSSGRenderModelData::globalNodeData() const': gives a type Python has no
    way to take yet.
    """
    raise NotImplementedError(
        "'QSSGRenderModelData.globalNodeData' has no cute function yet. "
        "Qt's 'const QSSGGlobalRenderNodeDataPtr "
        "&QSSGRenderModelData::globalNodeData() const': gives a type Python "
        "has no way to take yet.")

  @staticmethod
  def prepareMaterials(*__, **_) -> Never:
    """
    Qt's 'void QSSGRenderModelData::prepareMaterials(const QSSGModelsView
    &models)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGRenderModelData.prepareMaterials' has no cute function yet. "
        "Qt's 'void QSSGRenderModelData::prepareMaterials(const "
        "QSSGModelsView &models)': takes a type Python has no way to hand "
        "over yet.")

  @staticmethod
  def prepareMeshData(*__, **_) -> Never:
    """
    Qt's 'void QSSGRenderModelData::prepareMeshData(const QSSGModelsView
    &models, QSSGRenderer *renderer)': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'QSSGRenderModelData.prepareMeshData' has no cute function yet. "
        "Qt's 'void QSSGRenderModelData::prepareMeshData(const "
        "QSSGModelsView &models, QSSGRenderer *renderer)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def updateModelData(*__, **_) -> Never:
    """
    Qt's 'void QSSGRenderModelData::updateModelData(QSSGModelsView &models,
    QSSGRenderer *renderer, const QSSGRenderCameraDataList
    &renderCameraData)': leans on 'vtable for QRunnable::QGenericRunnable',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QSSGRenderModelData.updateModelData' has no cute function yet. "
        "Qt's 'void QSSGRenderModelData::updateModelData(QSSGModelsView "
        "&models, QSSGRenderer *renderer, const QSSGRenderCameraDataList "
        "&renderCameraData)': leans on 'vtable for "
        "QRunnable::QGenericRunnable', which Qt's source does not mark for "
        "use from outside Qt and has no code for that could be taken.")
