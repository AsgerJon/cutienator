"""
QSSGRenderContextInterface binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/ssg/qssgrendercontextcore.h,
#  Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtGui import QRhi
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRhi = WAIT['QRhi']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSSGRenderContextInterface(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSSGRenderContextInterface: a plain Python object
  standing in front of one C++ QSSGRenderContextInterface.

  What exists
  -----------

  Every function of Qt's QSSGRenderContextInterface that has a ritual and
  that Python can call so far, 3 names in all: 'rhi', 'init',
  'releaseCachedResources'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSSGRenderContextInterface::~QSSGRenderContextInterface()': the
    destructor: Python never removes a C++ QSSGRenderContextInterface.
  - Qt's 'const std::unique_ptr<QSSGRenderer>
    &QSSGRenderContextInterface::renderer() const': gives a type Python has
    no way to take yet.
  - Qt's 'const std::unique_ptr<QSSGBufferManager>
    &QSSGRenderContextInterface::bufferManager() const': gives a type Python
    has no way to take yet.
  - Qt's 'const std::unique_ptr<QSSGRhiContext>
    &QSSGRenderContextInterface::rhiContext() const': gives a type Python has
    no way to take yet.
  - Qt's 'const std::unique_ptr<QSSGShaderCache>
    &QSSGRenderContextInterface::shaderCache() const': gives a type Python
    has no way to take yet.
  - Qt's 'const std::shared_ptr<QSSGShaderLibraryManager>
    &QSSGRenderContextInterface::shaderLibraryManager() const': gives a type
    Python has no way to take yet.
  - Qt's 'const std::unique_ptr<QSSGCustomMaterialSystem>
    &QSSGRenderContextInterface::customMaterialSystem() const': gives a type
    Python has no way to take yet.
  - Qt's 'const std::unique_ptr<QSSGProgramGenerator>
    &QSSGRenderContextInterface::shaderProgramGenerator() const': gives a
    type Python has no way to take yet.
  - Qt's 'const std::unique_ptr<QSSGDebugDrawSystem>
    &QSSGRenderContextInterface::debugDrawSystem() const': gives a type
    Python has no way to take yet.
  - Qt's 'const std::unique_ptr<QSSGPerFrameAllocator>
    &QSSGRenderContextInterface::perFrameAllocator() const': gives a type
    Python has no way to take yet.

  What has no ritual
  ------------------

  4 of the 18 functions Qt declares: 2 forbidden; 2 the compiler refuses its
  ritual as it would be written here.

  What to expect
  --------------

  - The C++ QSSGRenderContextInterface is created at the first use, not by
    'QSSGRenderContextInterface(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSSGRenderContextInterface.
  - Each name of Qt's QSSGRenderContextInterface that has no cute function
    yet, 'bufferManager', 'customMaterialSystem', 'debugDrawSystem',
    'perFrameAllocator', 'renderer', 'rhiContext', 'shaderCache',
    'shaderLibraryManager', 'shaderProgramGenerator', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSSGRenderContextInterface'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def rhi(self) -> Optional[QRhi]:
    """
    Calls Qt's 'QRhi *QSSGRenderContextInterface::rhi() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrendercontextinterface.html#rhi

    Returns
    -------

    Optional[QRhi]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhi *QSSGRenderContextInterface::rhi() const
    address = self.uglySide.call(
        'ritual_ZNK26QSSGRenderContextInterface3rhiEv',
    )
    from ..QtGui import QRhi
    return QRhi._cuteAt(address)

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

  @overload(QRhi)
  @overload(NoneType)
  def __init__(self, rhi: Optional[QRhi]) -> None:
    """
    Notes what was given, for Qt's
    'QSSGRenderContextInterface::QSSGRenderContextInterface(QRhi *rhi)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrendercontextinterface.html

    Parameters
    ----------

    rhi : Optional[QRhi]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QSSGRenderContextInterface::QSSGRenderContextInterface(QRhi *rhi)
    self._noteCreation(QSSGRenderContextInterface, lambda: Rituals.call(
        'ritual_ZN26QSSGRenderContextInterfaceC1EP4QRhi',
        self._addressOf(rhi),
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

  def init(self) -> None:
    """
    Calls Qt's 'void QSSGRenderContextInterface::init()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrendercontextinterface.html#init
    """
    #  void QSSGRenderContextInterface::init()
    self.uglySide.call('ritual_ZN26QSSGRenderContextInterface4initEv')

  def releaseCachedResources(self) -> None:
    """
    Calls Qt's 'void QSSGRenderContextInterface::releaseCachedResources()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrendercontextinterface.html
    """
    #  void QSSGRenderContextInterface::releaseCachedResources()
    self.uglySide.call(
        'ritual_ZN26QSSGRenderContextInterface22releaseCachedResourcesEv',
    )

  @staticmethod
  def bufferManager(*__, **_) -> Never:
    """
    Qt's 'const std::unique_ptr<QSSGBufferManager>
    &QSSGRenderContextInterface::bufferManager() const': gives a type Python
    has no way to take yet.
    """
    raise NotImplementedError(
        "'QSSGRenderContextInterface.bufferManager' has no cute function "
        "yet. Qt's 'const std::unique_ptr<QSSGBufferManager> "
        "&QSSGRenderContextInterface::bufferManager() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def customMaterialSystem(*__, **_) -> Never:
    """
    Qt's 'const std::unique_ptr<QSSGCustomMaterialSystem>
    &QSSGRenderContextInterface::customMaterialSystem() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QSSGRenderContextInterface.customMaterialSystem' has no cute "
        "function yet. Qt's 'const "
        "std::unique_ptr<QSSGCustomMaterialSystem> "
        "&QSSGRenderContextInterface::customMaterialSystem() const': gives "
        "a type Python has no way to take yet.")

  @staticmethod
  def debugDrawSystem(*__, **_) -> Never:
    """
    Qt's 'const std::unique_ptr<QSSGDebugDrawSystem>
    &QSSGRenderContextInterface::debugDrawSystem() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QSSGRenderContextInterface.debugDrawSystem' has no cute function "
        "yet. Qt's 'const std::unique_ptr<QSSGDebugDrawSystem> "
        "&QSSGRenderContextInterface::debugDrawSystem() const': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def perFrameAllocator(*__, **_) -> Never:
    """
    Qt's 'const std::unique_ptr<QSSGPerFrameAllocator>
    &QSSGRenderContextInterface::perFrameAllocator() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QSSGRenderContextInterface.perFrameAllocator' has no cute "
        "function yet. Qt's 'const std::unique_ptr<QSSGPerFrameAllocator> "
        "&QSSGRenderContextInterface::perFrameAllocator() const': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def renderer(*__, **_) -> Never:
    """
    Qt's 'const std::unique_ptr<QSSGRenderer>
    &QSSGRenderContextInterface::renderer() const': gives a type Python has
    no way to take yet.
    """
    raise NotImplementedError(
        "'QSSGRenderContextInterface.renderer' has no cute function yet. "
        "Qt's 'const std::unique_ptr<QSSGRenderer> "
        "&QSSGRenderContextInterface::renderer() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def rhiContext(*__, **_) -> Never:
    """
    Qt's 'const std::unique_ptr<QSSGRhiContext>
    &QSSGRenderContextInterface::rhiContext() const': gives a type Python has
    no way to take yet.
    """
    raise NotImplementedError(
        "'QSSGRenderContextInterface.rhiContext' has no cute function yet. "
        "Qt's 'const std::unique_ptr<QSSGRhiContext> "
        "&QSSGRenderContextInterface::rhiContext() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def shaderCache(*__, **_) -> Never:
    """
    Qt's 'const std::unique_ptr<QSSGShaderCache>
    &QSSGRenderContextInterface::shaderCache() const': gives a type Python
    has no way to take yet.
    """
    raise NotImplementedError(
        "'QSSGRenderContextInterface.shaderCache' has no cute function yet. "
        "Qt's 'const std::unique_ptr<QSSGShaderCache> "
        "&QSSGRenderContextInterface::shaderCache() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def shaderLibraryManager(*__, **_) -> Never:
    """
    Qt's 'const std::shared_ptr<QSSGShaderLibraryManager>
    &QSSGRenderContextInterface::shaderLibraryManager() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QSSGRenderContextInterface.shaderLibraryManager' has no cute "
        "function yet. Qt's 'const "
        "std::shared_ptr<QSSGShaderLibraryManager> "
        "&QSSGRenderContextInterface::shaderLibraryManager() const': gives "
        "a type Python has no way to take yet.")

  @staticmethod
  def shaderProgramGenerator(*__, **_) -> Never:
    """
    Qt's 'const std::unique_ptr<QSSGProgramGenerator>
    &QSSGRenderContextInterface::shaderProgramGenerator() const': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QSSGRenderContextInterface.shaderProgramGenerator' has no cute "
        "function yet. Qt's 'const std::unique_ptr<QSSGProgramGenerator> "
        "&QSSGRenderContextInterface::shaderProgramGenerator() const': "
        "gives a type Python has no way to take yet.")
