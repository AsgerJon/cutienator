"""
QSSGShaderLibraryManager binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendershaderlibrarymanager_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QSSGShaderLibraryManager to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QSSGShaderCache

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QByteArray
  from . import QSSGCustomShaderMetaData
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QSSGCustomShaderMetaData = WAIT['QSSGCustomShaderMetaData']


class QSSGShaderLibraryManager(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSSGShaderLibraryManager: a plain Python object
  standing in front of one C++ QSSGShaderLibraryManager.

  What exists
  -----------

  Every function of Qt's QSSGShaderLibraryManager that has a ritual and that
  Python can call so far, 6 names in all: 'getShaderCodeLibraryDirectory',
  'setShaderSource', 'loadPregeneratedShaderInfo', 'getIncludeContents',
  'getShaderSource', 'getShaderMetaData'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSSGShaderLibraryManager::~QSSGShaderLibraryManager()': the
    destructor: Python never removes a C++ QSSGShaderLibraryManager.
  - Qt's 'QQsbCollection::EntryMap
    QSSGShaderLibraryManager::getParticleShaderEntries() const': gives a type
    Python has no way to take yet.
  - Qt's 'void QSSGShaderLibraryManager::resolveIncludeFiles(QByteArray
    &theReadBuffer, const QByteArray &inMaterialInfoString)': takes a type
    Python has no way to hand over yet.
  - Qt's 'bool QSSGShaderLibraryManager::compare(const
    QSSGShaderDefaultMaterialKey &key1, const QSSGShaderDefaultMaterialKey
    &key2)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  3 of the 14 functions Qt declares: 2 forbidden; 1 cannot be called and
  cannot be called through the meta-object and cannot be copied.

  What to expect
  --------------

  - The C++ QSSGShaderLibraryManager is created at the first use, not by
    'QSSGShaderLibraryManager(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSSGShaderLibraryManager.
  - Each name of Qt's QSSGShaderLibraryManager that has no cute function yet,
    'compare', 'getParticleShaderEntries', 'resolveIncludeFiles',
    'setShaderCodeLibraryVersion', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def getShaderCodeLibraryDirectory() -> str:
    """
    Calls Qt's 'QString
    QSSGShaderLibraryManager::getShaderCodeLibraryDirectory()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshaderlibrarymanager.html

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSSGShaderLibraryManager::getShaderCodeLibraryDirectory()
    return Rituals.call(
        'ritual_ZN24QSSGShaderLibraryManager29getShaderCodeLibraryDirectory'
        'Ev',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSSGShaderLibraryManager'

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

  @overload(
      QByteArray, QSSGShaderCache.ShaderType, QByteArray,
      QSSGCustomShaderMetaData,
  )
  def setShaderSource(
      self,
      inShaderPathKey: QByteArray,
      type: QSSGShaderCache.ShaderType,
      inSource: QByteArray,
      meta: QSSGCustomShaderMetaData,
  ) -> None:
    """
    Calls Qt's 'void QSSGShaderLibraryManager::setShaderSource(const
    QByteArray &inShaderPathKey, QSSGShaderCache::ShaderType type, const
    QByteArray &inSource, const QSSGCustomShaderMetaData &meta)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshaderlibrarymanager.html#setShaderSource

    Parameters
    ----------

    inShaderPathKey : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    type : QSSGShaderCache.ShaderType
      Passed on as its number.

    inSource : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    meta : QSSGCustomShaderMetaData
      Passed on as a value: Qt reads the C++ QSSGCustomShaderMetaData, which
      stays Python's own.
    """
    #  void QSSGShaderLibraryManager::setShaderSource(const QByteArray
    #      &inShaderPathKey, QSSGShaderCache::ShaderType type, const
    #      QByteArray &inSource, const QSSGCustomShaderMetaData &meta)
    self.uglySide.call(
        'ritual_ZN24QSSGShaderLibraryManager15setShaderSourceERK10QByteArra'
        'yN15QSSGShaderCache10ShaderTypeES2_RK24QSSGCustomShaderMetaData',
        self._valueOf(inShaderPathKey), type.value, self._valueOf(inSource),
        self._valueOf(meta),
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
    'QSSGShaderLibraryManager::QSSGShaderLibraryManager()', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshaderlibrarymanager.html
    """
    #  QSSGShaderLibraryManager::QSSGShaderLibraryManager()
    self._noteCreation(QSSGShaderLibraryManager, lambda: Rituals.call(
        'ritual_ZN24QSSGShaderLibraryManagerC1Ev',
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

  def loadPregeneratedShaderInfo(self) -> None:
    """
    Calls Qt's 'void QSSGShaderLibraryManager::loadPregeneratedShaderInfo()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshaderlibrarymanager.html
    """
    #  void QSSGShaderLibraryManager::loadPregeneratedShaderInfo()
    self.uglySide.call(
        'ritual_ZN24QSSGShaderLibraryManager26loadPregeneratedShaderInfoEv',
    )

  @overload(QByteArray)
  def getIncludeContents(self, inShaderPathKey: QByteArray) -> QByteArray:
    """
    Calls Qt's 'QByteArray QSSGShaderLibraryManager::getIncludeContents(const
    QByteArray &inShaderPathKey)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshaderlibrarymanager.html#getIncludeContents

    Parameters
    ----------

    inShaderPathKey : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QSSGShaderLibraryManager::getIncludeContents(const
    #      QByteArray &inShaderPathKey)
    address = self.uglySide.call(
        'ritual_ZN24QSSGShaderLibraryManager18getIncludeContentsERK10QByteA'
        'rray',
        self._valueOf(inShaderPathKey),
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  @overload(QByteArray, QSSGShaderCache.ShaderType)
  def getShaderSource(
      self,
      inShaderPathKey: QByteArray,
      type: QSSGShaderCache.ShaderType,
  ) -> QByteArray:
    """
    Calls Qt's 'QByteArray QSSGShaderLibraryManager::getShaderSource(const
    QByteArray &inShaderPathKey, QSSGShaderCache::ShaderType type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshaderlibrarymanager.html#getShaderSource

    Parameters
    ----------

    inShaderPathKey : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    type : QSSGShaderCache.ShaderType
      Passed on as its number.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QSSGShaderLibraryManager::getShaderSource(const QByteArray
    #      &inShaderPathKey, QSSGShaderCache::ShaderType type)
    address = self.uglySide.call(
        'ritual_ZN24QSSGShaderLibraryManager15getShaderSourceERK10QByteArra'
        'yN15QSSGShaderCache10ShaderTypeE',
        self._valueOf(inShaderPathKey), type.value,
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  @overload(QByteArray, QSSGShaderCache.ShaderType)
  def getShaderMetaData(
      self,
      inShaderPathKey: QByteArray,
      type: QSSGShaderCache.ShaderType,
  ) -> QSSGCustomShaderMetaData:
    """
    Calls Qt's 'QSSGCustomShaderMetaData
    QSSGShaderLibraryManager::getShaderMetaData(const QByteArray
    &inShaderPathKey, QSSGShaderCache::ShaderType type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshaderlibrarymanager.html#getShaderMetaData

    Parameters
    ----------

    inShaderPathKey : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    type : QSSGShaderCache.ShaderType
      Passed on as its number.

    Returns
    -------

    QSSGCustomShaderMetaData
      A new cute QSSGCustomShaderMetaData around the copy Qt gave back.
      Python owns it.
    """
    #  QSSGCustomShaderMetaData
    #      QSSGShaderLibraryManager::getShaderMetaData(const QByteArray
    #      &inShaderPathKey, QSSGShaderCache::ShaderType type)
    address = self.uglySide.call(
        'ritual_ZN24QSSGShaderLibraryManager17getShaderMetaDataERK10QByteAr'
        'rayN15QSSGShaderCache10ShaderTypeE',
        self._valueOf(inShaderPathKey), type.value,
    )
    from . import QSSGCustomShaderMetaData
    return QSSGCustomShaderMetaData._cuteOwning(address)

  @staticmethod
  def compare(*__, **_) -> Never:
    """
    Qt's 'bool QSSGShaderLibraryManager::compare(const
    QSSGShaderDefaultMaterialKey &key1, const QSSGShaderDefaultMaterialKey
    &key2)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGShaderLibraryManager.compare' has no cute function yet. Qt's "
        "'bool QSSGShaderLibraryManager::compare(const "
        "QSSGShaderDefaultMaterialKey &key1, const "
        "QSSGShaderDefaultMaterialKey &key2)': takes a type Python has no "
        "way to hand over yet.")

  @staticmethod
  def getParticleShaderEntries(*__, **_) -> Never:
    """
    Qt's 'QQsbCollection::EntryMap
    QSSGShaderLibraryManager::getParticleShaderEntries() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QSSGShaderLibraryManager.getParticleShaderEntries' has no cute "
        "function yet. Qt's 'QQsbCollection::EntryMap "
        "QSSGShaderLibraryManager::getParticleShaderEntries() const': gives "
        "a type Python has no way to take yet.")

  @staticmethod
  def resolveIncludeFiles(*__, **_) -> Never:
    """
    Qt's 'void QSSGShaderLibraryManager::resolveIncludeFiles(QByteArray
    &theReadBuffer, const QByteArray &inMaterialInfoString)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGShaderLibraryManager.resolveIncludeFiles' has no cute "
        "function yet. Qt's 'void "
        "QSSGShaderLibraryManager::resolveIncludeFiles(QByteArray "
        "&theReadBuffer, const QByteArray &inMaterialInfoString)': takes a "
        "type Python has no way to hand over yet.")

  @staticmethod
  def setShaderCodeLibraryVersion(*__, **_) -> Never:
    """
    Qt's 'void QSSGShaderLibraryManager::setShaderCodeLibraryVersion(const
    QByteArray &version)': cannot be called and cannot be called through the
    meta-object and cannot be copied: no header file has its code, Qt's
    source does not mark it or its class for use from outside Qt or writes it
    'inline' or nowhere, and it is no signal, slot or invokable function
    giving back nothing, of a class built on QObject, and Qt's source has no
    code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QSSGShaderLibraryManager.setShaderCodeLibraryVersion' has no cute "
        "function yet. Qt's 'void "
        "QSSGShaderLibraryManager::setShaderCodeLibraryVersion(const "
        "QByteArray &version)': cannot be called and cannot be called "
        "through the meta-object and cannot be copied: no header file has "
        "its code, Qt's source does not mark it or its class for use from "
        "outside Qt or writes it 'inline' or nowhere, and it is no signal, "
        "slot or invokable function giving back nothing, of a class built "
        "on QObject, and Qt's source has no code for it that could be told "
        "from the rest.")
