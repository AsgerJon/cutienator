"""
QSGBatchRenderer::ShaderManager binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qsgbatchrenderer_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QSGBatchRenderer::ShaderManager to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject


class ShaderManager(QObject):
  """
  The cute side of Qt's QSGBatchRenderer::ShaderManager: a plain Python
  object standing in front of one C++ QSGBatchRenderer::ShaderManager.

  It is built on the cute 'QObject', as Qt's QSGBatchRenderer::ShaderManager
  is built on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSGBatchRenderer::ShaderManager that has a ritual
  and that Python can call so far, 3 names in all: 'metaObject',
  'clearCachedRendererData', 'invalidated'. None can be made from Python: one
  comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QSGBatchRenderer::ShaderManager::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int QSGBatchRenderer::ShaderManager::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QSGBatchRenderer::ShaderManager::~ShaderManager()': the destructor:
    Python never removes a C++ QSGBatchRenderer::ShaderManager.

  What has no ritual
  ------------------

  6 of the 12 functions Qt declares: 2 not a gap; 2 Qt's library has no name
  for it, and its code in Qt's source does not compile apart from its file; 2
  leans on 'QSGBatchRenderer.

  What to expect
  --------------

  - The C++ QSGBatchRenderer::ShaderManager is created at the first use, not
    by 'QSGBatchRenderer::ShaderManager(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSGBatchRenderer::ShaderManager.
  - Qt tells when it has removed the C++ QSGBatchRenderer::ShaderManager.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QSGBatchRenderer::ShaderManager that has no cute
    function yet, '__init__', 'prepareMaterial', 'prepareMaterialNoRewrite',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSGBatchRenderer::ShaderManager'

  #  A C++ QSGBatchRenderer::ShaderManager Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSGBatchRenderer_ShaderManager'

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
    *QSGBatchRenderer::ShaderManager::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgbatchrenderer-shadermanager.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QSGBatchRenderer::ShaderManager::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK16QSGBatchRenderer13ShaderManager10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

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
    Qt's
    'QSGBatchRenderer::ShaderManager::ShaderManager(QSGDefaultRenderContext
    *ctx)': leans on
    'QSGBatchRenderer::ShaderManager::qt_metacall(QMetaObject::Call, int,
    void**)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QSGBatchRenderer.ShaderManager.__init__' has no cute function "
        "yet. Qt's "
        "'QSGBatchRenderer::ShaderManager::ShaderManager(QSGDefaultRenderCon"
        "text *ctx)': leans on "
        "'QSGBatchRenderer::ShaderManager::qt_metacall(QMetaObject::Call, "
        "int, void**)', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken.")

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

  def clearCachedRendererData(self) -> None:
    """
    Calls Qt's 'void
    QSGBatchRenderer::ShaderManager::clearCachedRendererData()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgbatchrenderer-shadermanager.html
    """
    #  void QSGBatchRenderer::ShaderManager::clearCachedRendererData()
    self.uglySide.call(
        'ritual_ZN16QSGBatchRenderer13ShaderManager23clearCachedRendererDat'
        'aEv',
    )

  def invalidated(self) -> None:
    """
    Calls Qt's 'void QSGBatchRenderer::ShaderManager::invalidated()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgbatchrenderer-shadermanager.html#invalidated
    """
    #  void QSGBatchRenderer::ShaderManager::invalidated()
    self.uglySide.call(
        'ritual_ZN16QSGBatchRenderer13ShaderManager11invalidatedEv',
    )

  @staticmethod
  def prepareMaterial(*__, **_) -> Never:
    """
    Qt's 'Shader
    *QSGBatchRenderer::ShaderManager::prepareMaterial(QSGMaterial *material,
    const QSGGeometry *geometry, QSGRendererInterface::RenderMode renderMode,
    int multiViewCount)': Qt's library has no name for it, and its code in
    Qt's source does not compile apart from its file: use of undeclared
    identifier 'calculateVertexInputLayout'.
    """
    raise NotImplementedError(
        "'QSGBatchRenderer.ShaderManager.prepareMaterial' has no cute "
        "function yet. Qt's 'Shader "
        "*QSGBatchRenderer::ShaderManager::prepareMaterial(QSGMaterial "
        "*material, const QSGGeometry *geometry, "
        "QSGRendererInterface::RenderMode renderMode, int multiViewCount)': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: use of undeclared identifier "
        "'calculateVertexInputLayout'.")

  @staticmethod
  def prepareMaterialNoRewrite(*__, **_) -> Never:
    """
    Qt's 'Shader
    *QSGBatchRenderer::ShaderManager::prepareMaterialNoRewrite(QSGMaterial
    *material, const QSGGeometry *geometry, QSGRendererInterface::RenderMode
    renderMode, int multiViewCount)': Qt's library has no name for it, and
    its code in Qt's source does not compile apart from its file: use of
    undeclared identifier 'qsg_setMultiViewFlagsOnMaterial'.
    """
    raise NotImplementedError(
        "'QSGBatchRenderer.ShaderManager.prepareMaterialNoRewrite' has no "
        "cute function yet. Qt's 'Shader "
        "*QSGBatchRenderer::ShaderManager::prepareMaterialNoRewrite(QSGMater"
        "ial *material, const QSGGeometry *geometry, "
        "QSGRendererInterface::RenderMode renderMode, int multiViewCount)': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: use of undeclared identifier "
        "'qsg_setMultiViewFlagsOnMaterial'.")
