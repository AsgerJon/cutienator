"""
QWaylandBufferMaterial binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWaylandCompositor/6.12.0/QtWaylandCompositor/private/qwaylandquickitem_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QWaylandBufferMaterial to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..QtQuick import QSGRendererInterface

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtQuick import QSGMaterialShader, QSGMaterialType


class QWaylandBufferMaterial(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QWaylandBufferMaterial: a plain Python object
  standing in front of one C++ QWaylandBufferMaterial.

  What exists
  -----------

  Every function of Qt's QWaylandBufferMaterial that has a ritual and that
  Python can call so far, 4 names in all: 'type', 'createShader',
  'setTextureParameters', 'ensureTextures'. None can be made from Python: one
  comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QWaylandBufferMaterial::~QWaylandBufferMaterial()': the destructor:
    Python never removes a C++ QWaylandBufferMaterial.

  What has no ritual
  ------------------

  5 of the 10 functions Qt declares: 4 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 1 cannot be
  called and cannot be called through the meta-object and cannot be copied.

  What to expect
  --------------

  - The C++ QWaylandBufferMaterial is created at the first use, not by
    'QWaylandBufferMaterial(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QWaylandBufferMaterial.
  - Each name of Qt's QWaylandBufferMaterial that has no cute function yet,
    '__init__', 'bind', 'setBufferRef', 'setTextureForPlane',
    'updateScenegraphTextures', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWaylandBufferMaterial'

  #  A C++ QWaylandBufferMaterial Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QWaylandBufferMaterial'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def type(self) -> Optional[QSGMaterialType]:
    """
    Calls Qt's 'QSGMaterialType *QWaylandBufferMaterial::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandbuffermaterial.html#type

    Returns
    -------

    Optional[QSGMaterialType]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGMaterialType *QWaylandBufferMaterial::type() const
    address = self.uglySide.call('ritual_ZNK22QWaylandBufferMaterial4typeEv')
    from ..QtQuick import QSGMaterialType
    return QSGMaterialType._cuteAt(address)

  @overload(QSGRendererInterface.RenderMode)
  def createShader(
      self,
      renderMode: QSGRendererInterface.RenderMode,
  ) -> Optional[QSGMaterialShader]:
    """
    Calls Qt's 'QSGMaterialShader
    *QWaylandBufferMaterial::createShader(QSGRendererInterface::RenderMode
    renderMode) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandbuffermaterial.html#createShader

    Parameters
    ----------

    renderMode : QSGRendererInterface.RenderMode
      Passed on as its number.

    Returns
    -------

    Optional[QSGMaterialShader]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGMaterialShader
    #      *QWaylandBufferMaterial::createShader(QSGRendererInterface::
    #      RenderMode renderMode) const
    address = self.uglySide.call(
        'ritual_ZNK22QWaylandBufferMaterial12createShaderEN20QSGRendererInt'
        'erface10RenderModeE',
        renderMode.value,
    )
    from ..QtQuick import QSGMaterialShader
    return QSGMaterialShader._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setTextureParameters(self, target: int) -> None:
    """
    Calls Qt's 'void QWaylandBufferMaterial::setTextureParameters(GLenum
    target)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandbuffermaterial.html#setTextureParameters

    Parameters
    ----------

    target : int
      Passed on as it is.
    """
    #  void QWaylandBufferMaterial::setTextureParameters(GLenum target)
    self.uglySide.call(
        'ritual_ZN22QWaylandBufferMaterial20setTextureParametersEj', target,
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QWaylandBufferMaterial::QWaylandBufferMaterial(QWaylandBufferRef::
    BufferFormatEgl format)': Qt's library has no name for it, and its code
    in Qt's source does not compile apart from its file: use of undeclared
    identifier 'bufferTypes'.
    """
    raise NotImplementedError(
        "'QWaylandBufferMaterial.__init__' has no cute function yet. Qt's "
        "'QWaylandBufferMaterial::QWaylandBufferMaterial(QWaylandBufferRef::"
        "BufferFormatEgl format)': Qt's library has no name for it, and its "
        "code in Qt's source does not compile apart from its file: use of "
        "undeclared identifier 'bufferTypes'.")

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

  @overload(int)
  def ensureTextures(self, count: int) -> None:
    """
    Calls Qt's 'void QWaylandBufferMaterial::ensureTextures(int count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandbuffermaterial.html#ensureTextures

    Parameters
    ----------

    count : int
      Passed on as it is.
    """
    #  void QWaylandBufferMaterial::ensureTextures(int count)
    self.uglySide.call(
        'ritual_ZN22QWaylandBufferMaterial14ensureTexturesEi', count,
    )

  @staticmethod
  def bind(*__, **_) -> Never:
    """
    Qt's 'void QWaylandBufferMaterial::bind()': Qt's library has no name for
    it, and its code in Qt's source does not compile apart from its file: use
    of undeclared identifier 'bufferTypes'.
    """
    raise NotImplementedError(
        "'QWaylandBufferMaterial.bind' has no cute function yet. Qt's 'void "
        "QWaylandBufferMaterial::bind()': Qt's library has no name for it, "
        "and its code in Qt's source does not compile apart from its file: "
        "use of undeclared identifier 'bufferTypes'.")

  @staticmethod
  def setBufferRef(*__, **_) -> Never:
    """
    Qt's 'void QWaylandBufferMaterial::setBufferRef(QWaylandQuickItem
    *surfaceItem, const QWaylandBufferRef &ref)': Qt's library has no name
    for it, and its code in Qt's source does not compile apart from its file:
    use of undeclared identifier 'bufferTypes'.
    """
    raise NotImplementedError(
        "'QWaylandBufferMaterial.setBufferRef' has no cute function yet. "
        "Qt's 'void QWaylandBufferMaterial::setBufferRef(QWaylandQuickItem "
        "*surfaceItem, const QWaylandBufferRef &ref)': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: use of undeclared identifier 'bufferTypes'.")

  @staticmethod
  def setTextureForPlane(*__, **_) -> Never:
    """
    Qt's 'void QWaylandBufferMaterial::setTextureForPlane(int plane,
    QOpenGLTexture *texture, QSGTexture *scenegraphTexture)': Qt's library
    has no name for it, and its code in Qt's source does not compile apart
    from its file: use of undeclared identifier 'bufferTypes'.
    """
    raise NotImplementedError(
        "'QWaylandBufferMaterial.setTextureForPlane' has no cute function "
        "yet. Qt's 'void QWaylandBufferMaterial::setTextureForPlane(int "
        "plane, QOpenGLTexture *texture, QSGTexture *scenegraphTexture)': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: use of undeclared identifier "
        "'bufferTypes'.")

  @staticmethod
  def updateScenegraphTextures(*__, **_) -> Never:
    """
    Qt's 'void QWaylandBufferMaterial::updateScenegraphTextures(QRhi *rhi)':
    cannot be called and cannot be called through the meta-object and cannot
    be copied: no header file has its code, Qt's source does not mark it or
    its class for use from outside Qt or writes it 'inline' or nowhere, and
    it is no signal, slot or invokable function giving back nothing, of a
    class built on QObject, and Qt's source has no code for it that could be
    told from the rest.
    """
    raise NotImplementedError(
        "'QWaylandBufferMaterial.updateScenegraphTextures' has no cute "
        "function yet. Qt's 'void "
        "QWaylandBufferMaterial::updateScenegraphTextures(QRhi *rhi)': "
        "cannot be called and cannot be called through the meta-object and "
        "cannot be copied: no header file has its code, Qt's source does "
        "not mark it or its class for use from outside Qt or writes it "
        "'inline' or nowhere, and it is no signal, slot or invokable "
        "function giving back nothing, of a class built on QObject, and "
        "Qt's source has no code for it that could be told from the rest.")
