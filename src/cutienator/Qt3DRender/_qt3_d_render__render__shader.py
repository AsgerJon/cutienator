"""
Qt3DRender::Render::Shader binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/6.12.0/Qt3DRender/private/shader_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means Qt3DRender::Render::Shader to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore
from . import Qt3DRender

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class Shader(Qt3DRender.Render.BackendNode):
  """
  The cute side of Qt's Qt3DRender::Render::Shader: a plain Python object
  standing in front of one C++ Qt3DRender::Render::Shader.

  It is built on the cute 'Qt3DRender::Render::BackendNode', as Qt's
  Qt3DRender::Render::Shader is built on Qt's
  Qt3DRender::Render::BackendNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::Render::Shader that has a ritual and
  that Python can call so far, 14 names in all: 'cleanup', 'setShaderCode',
  'syncFromFrontEnd', 'log', 'status', 'setFormat', 'format', 'isDirty',
  'unsetDirty', 'requiresFrontendSync', 'unsetRequiresFrontendSync',
  'setLog', 'setStatus', 'requestCacheRebuild'. It can be made from Python,
  in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Qt3DRender::Render::Shader::~Shader()': the destructor: Python
    never removes a C++ Qt3DRender::Render::Shader.
  - Qt's 'const std::vector<QByteArray>
    &Qt3DRender::Render::Shader::shaderCode() const': gives a type Python has
    no way to take yet.
  - Qt's 'void Qt3DRender::Render::Shader::initializeFromReference(const
    Shader &other)': takes a type Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ Qt3DRender::Render::Shader is created at the first use, not by
    'Qt3DRender::Render::Shader(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::Render::Shader.
  - Each name of Qt's Qt3DRender::Render::Shader that has no cute function
    yet, 'initializeFromReference', 'shaderCode', holds a function that
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
  __qt_class__ = 'Qt3DRender::Render::Shader'

  #  A C++ Qt3DRender::Render::Shader Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DRender_Render_Shader'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def log(self) -> str:
    """
    Calls Qt's 'QString Qt3DRender::Render::Shader::log() const'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-render-shader.html#log

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString Qt3DRender::Render::Shader::log() const
    return self.uglySide.call('ritual_ZNK10Qt3DRender6Render6Shader3logEv')

  def status(self) -> Qt3DRender.QShaderProgram.Status:
    """
    Calls Qt's 'QShaderProgram::Status Qt3DRender::Render::Shader::status()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-shader.html#status

    Returns
    -------

    Qt3DRender.QShaderProgram.Status
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt3DRender.QShaderProgram.Status(number)' gives.
    """
    #  QShaderProgram::Status Qt3DRender::Render::Shader::status() const
    return Qt3DRender.QShaderProgram.Status(self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render6Shader6statusEv',
    ))

  def format(self) -> Qt3DRender.QShaderProgram.Format:
    """
    Calls Qt's 'QShaderProgram::Format Qt3DRender::Render::Shader::format()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-shader.html#format

    Returns
    -------

    Qt3DRender.QShaderProgram.Format
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt3DRender.QShaderProgram.Format(number)' gives.
    """
    #  QShaderProgram::Format Qt3DRender::Render::Shader::format() const
    return Qt3DRender.QShaderProgram.Format(self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render6Shader6formatEv',
    ))

  def isDirty(self) -> bool:
    """
    Calls Qt's 'bool Qt3DRender::Render::Shader::isDirty() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-shader.html#isDirty
    """
    #  bool Qt3DRender::Render::Shader::isDirty() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render6Shader7isDirtyEv',
    )

  def requiresFrontendSync(self) -> bool:
    """
    Calls Qt's 'bool Qt3DRender::Render::Shader::requiresFrontendSync()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-shader.html#requiresFrontendSync
    """
    #  bool Qt3DRender::Render::Shader::requiresFrontendSync() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render6Shader20requiresFrontendSyncEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Qt3DRender.QShaderProgram.ShaderType, QByteArray)
  def setShaderCode(
      self,
      type: Qt3DRender.QShaderProgram.ShaderType,
      code: QByteArray,
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Render::Shader::setShaderCode(QShaderProgram::ShaderType
    type, const QByteArray &code)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-shader.html#setShaderCode

    Parameters
    ----------

    type : Qt3DRender.QShaderProgram.ShaderType
      Passed on as its number.

    code : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void Qt3DRender::Render::Shader::setShaderCode(QShaderProgram::
    #      ShaderType type, const QByteArray &code)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render6Shader13setShaderCodeENS_14QShaderPro'
        'gram10ShaderTypeERK10QByteArray',
        type.value, self._valueOf(code),
    )

  @overload(Qt3DRender.QShaderProgram.Format)
  def setFormat(self, format: Qt3DRender.QShaderProgram.Format) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Render::Shader::setFormat(QShaderProgram::Format format)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-shader.html#setFormat

    Parameters
    ----------

    format : Qt3DRender.QShaderProgram.Format
      Passed on as its number.
    """
    #  void Qt3DRender::Render::Shader::setFormat(QShaderProgram::Format
    #      format)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render6Shader9setFormatENS_14QShaderProgram6'
        'FormatE',
        format.value,
    )

  @overload(str)
  def setLog(self, log: str) -> None:
    """
    Calls Qt's 'void Qt3DRender::Render::Shader::setLog(const QString &log)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-shader.html#setLog

    Parameters
    ----------

    log : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void Qt3DRender::Render::Shader::setLog(const QString &log)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render6Shader6setLogERK7QString', log,
    )

  @overload(Qt3DRender.QShaderProgram.Status)
  def setStatus(self, status: Qt3DRender.QShaderProgram.Status) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Render::Shader::setStatus(QShaderProgram::Status status)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-shader.html#setStatus

    Parameters
    ----------

    status : Qt3DRender.QShaderProgram.Status
      Passed on as its number.
    """
    #  void Qt3DRender::Render::Shader::setStatus(QShaderProgram::Status
    #      status)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render6Shader9setStatusENS_14QShaderProgram6'
        'StatusE',
        status.value,
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
    Notes what was given, for Qt's 'Qt3DRender::Render::Shader::Shader()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-shader.html#Shader
    """
    #  Qt3DRender::Render::Shader::Shader()
    self._noteCreation(Shader, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender6Render6ShaderC1Ev',
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
    Calls Qt's 'void Qt3DRender::Render::Shader::cleanup()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-shader.html#cleanup
    """
    #  void Qt3DRender::Render::Shader::cleanup()
    self.uglySide.call('ritual_ZN10Qt3DRender6Render6Shader7cleanupEv')

  @overload(WAIT['Qt3DCore.QNode'], bool)
  @overload(NoneType, bool)
  def syncFromFrontEnd(
      self,
      frontEnd: Optional[Qt3DCore.QNode],
      firstTime: bool,
  ) -> None:
    """
    Calls Qt's 'void Qt3DRender::Render::Shader::syncFromFrontEnd(const
    Qt3DCore::QNode *frontEnd, bool firstTime)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-shader.html#syncFromFrontEnd

    Parameters
    ----------

    frontEnd : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    firstTime : bool
      Passed on as it is.
    """
    #  void Qt3DRender::Render::Shader::syncFromFrontEnd(const
    #      Qt3DCore::QNode *frontEnd, bool firstTime)
    ritual = (
        'ritual_ZN10Qt3DRender6Render6Shader16syncFromFrontEndEPKN8Qt3DCore'
        '5QNodeEb')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN10Qt3DRender6Render6Shader16syncFromFrontEndEPKN8Qt'
          '3DCore5QNodeEb')
    self.uglySide.call(ritual, self._addressOf(frontEnd), firstTime)

  def unsetDirty(self) -> None:
    """
    Calls Qt's 'void Qt3DRender::Render::Shader::unsetDirty()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-shader.html#unsetDirty
    """
    #  void Qt3DRender::Render::Shader::unsetDirty()
    self.uglySide.call('ritual_ZN10Qt3DRender6Render6Shader10unsetDirtyEv')

  def unsetRequiresFrontendSync(self) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Render::Shader::unsetRequiresFrontendSync()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-shader.html
    """
    #  void Qt3DRender::Render::Shader::unsetRequiresFrontendSync()
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render6Shader25unsetRequiresFrontendSyncEv',
    )

  def requestCacheRebuild(self) -> None:
    """
    Calls Qt's 'void Qt3DRender::Render::Shader::requestCacheRebuild()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-shader.html#requestCacheRebuild
    """
    #  void Qt3DRender::Render::Shader::requestCacheRebuild()
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render6Shader19requestCacheRebuildEv',
    )

  @staticmethod
  def initializeFromReference(*__, **_) -> Never:
    """
    Qt's 'void Qt3DRender::Render::Shader::initializeFromReference(const
    Shader &other)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.Shader.initializeFromReference' has no cute "
        "function yet. Qt's 'void "
        "Qt3DRender::Render::Shader::initializeFromReference(const Shader "
        "&other)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def shaderCode(*__, **_) -> Never:
    """
    Qt's 'const std::vector<QByteArray>
    &Qt3DRender::Render::Shader::shaderCode() const': gives a type Python has
    no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.Shader.shaderCode' has no cute function yet. "
        "Qt's 'const std::vector<QByteArray> "
        "&Qt3DRender::Render::Shader::shaderCode() const': gives a type "
        "Python has no way to take yet.")
