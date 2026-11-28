"""
QSGRhiGuiThreadShaderEffectManager binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qsgrhishadereffectnode_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QSGRhiGuiThreadShaderEffectManager to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from . import QSGGuiThreadShaderEffectManager

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QUrl
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QUrl = WAIT['QUrl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSGRhiGuiThreadShaderEffectManager(QSGGuiThreadShaderEffectManager):
  """
  The cute side of Qt's QSGRhiGuiThreadShaderEffectManager: a plain Python
  object standing in front of one C++ QSGRhiGuiThreadShaderEffectManager.

  It is built on the cute 'QSGGuiThreadShaderEffectManager', as Qt's
  QSGRhiGuiThreadShaderEffectManager is built on Qt's
  QSGGuiThreadShaderEffectManager, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSGRhiGuiThreadShaderEffectManager that has a ritual
  and that Python can call so far, 5 names in all:
  'hasSeparateSamplerAndTextureObjects', 'log', 'status',
  'prepareShaderCode', 'reflect'. None can be made from Python: one comes out
  of a function of another class that gives one back.

  What to expect
  --------------

  - The C++ QSGRhiGuiThreadShaderEffectManager is created at the first use,
    not by 'QSGRhiGuiThreadShaderEffectManager(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSGRhiGuiThreadShaderEffectManager.
  - Qt tells when it has removed the C++ QSGRhiGuiThreadShaderEffectManager.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSGRhiGuiThreadShaderEffectManager'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def hasSeparateSamplerAndTextureObjects(self) -> bool:
    """
    Calls Qt's 'bool
    QSGRhiGuiThreadShaderEffectManager::hasSeparateSamplerAndTextureObjects()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgrhiguithreadshadereffectmanager.html
    """
    #  bool QSGRhiGuiThreadShaderEffectManager::
    #      hasSeparateSamplerAndTextureObjects() const
    ritual = (
        'ritual_ZNK34QSGRhiGuiThreadShaderEffectManager35hasSeparateSampler'
        'AndTextureObjectsEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK34QSGRhiGuiThreadShaderEffectManager35hasSeparateS'
          'amplerAndTextureObjectsEv')
    return self.uglySide.call(ritual)

  def log(self) -> str:
    """
    Calls Qt's 'QString QSGRhiGuiThreadShaderEffectManager::log() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgrhiguithreadshadereffectmanager.html#log

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSGRhiGuiThreadShaderEffectManager::log() const
    ritual = 'ritual_ZNK34QSGRhiGuiThreadShaderEffectManager3logEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK34QSGRhiGuiThreadShaderEffectManager3logEv'
    return self.uglySide.call(ritual)

  def status(self) -> QSGGuiThreadShaderEffectManager.Status:
    """
    Calls Qt's 'Status QSGRhiGuiThreadShaderEffectManager::status() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgrhiguithreadshadereffectmanager.html#status

    Returns
    -------

    QSGGuiThreadShaderEffectManager.Status
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QSGGuiThreadShaderEffectManager.Status(number)' gives.
    """
    #  Status QSGRhiGuiThreadShaderEffectManager::status() const
    ritual = 'ritual_ZNK34QSGRhiGuiThreadShaderEffectManager6statusEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK34QSGRhiGuiThreadShaderEffectManager6statusEv'
    return QSGGuiThreadShaderEffectManager.Status(self.uglySide.call(ritual))

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

  @overload(
      QSGGuiThreadShaderEffectManager.ShaderInfo.Type, QUrl,
      QSGGuiThreadShaderEffectManager.ShaderInfo,
  )
  @overload(QSGGuiThreadShaderEffectManager.ShaderInfo.Type, QUrl, NoneType)
  def prepareShaderCode(
      self,
      typeHint: QSGGuiThreadShaderEffectManager.ShaderInfo.Type,
      src: QUrl,
      result: Optional[QSGGuiThreadShaderEffectManager.ShaderInfo],
  ) -> None:
    """
    Calls Qt's 'void
    QSGRhiGuiThreadShaderEffectManager::prepareShaderCode(ShaderInfo::Type
    typeHint, const QUrl &src, ShaderInfo *result)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgrhiguithreadshadereffectmanager.html

    Parameters
    ----------

    typeHint : QSGGuiThreadShaderEffectManager.ShaderInfo.Type
      Passed on as its number.

    src : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    result : Optional[QSGGuiThreadShaderEffectManager.ShaderInfo]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGRhiGuiThreadShaderEffectManager::prepareShaderCode(
    #      ShaderInfo::Type typeHint, const QUrl &src, ShaderInfo *result)
    ritual = (
        'ritual_ZN34QSGRhiGuiThreadShaderEffectManager17prepareShaderCodeEN'
        '31QSGGuiThreadShaderEffectManager10ShaderInfo4TypeERK4QUrlPS1_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN34QSGRhiGuiThreadShaderEffectManager17prepareShader'
          'CodeEN31QSGGuiThreadShaderEffectManager10ShaderInfo4TypeERK4QUrl'
          'PS1_')
    self.uglySide.call(
        ritual, typeHint.value, self._valueOf(src), self._addressOf(result),
    )

  @overload(QSGGuiThreadShaderEffectManager.ShaderInfo)
  @overload(NoneType)
  def reflect(
      self,
      result: Optional[QSGGuiThreadShaderEffectManager.ShaderInfo],
  ) -> bool:
    """
    Calls Qt's 'bool QSGRhiGuiThreadShaderEffectManager::reflect(ShaderInfo
    *result)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgrhiguithreadshadereffectmanager.html#reflect

    Parameters
    ----------

    result : Optional[QSGGuiThreadShaderEffectManager.ShaderInfo]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QSGRhiGuiThreadShaderEffectManager::reflect(ShaderInfo *result)
    return self.uglySide.call(
        'ritual_ZN34QSGRhiGuiThreadShaderEffectManager7reflectEPN31QSGGuiTh'
        'readShaderEffectManager10ShaderInfoE',
        self._addressOf(result),
    )
