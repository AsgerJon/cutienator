"""
QSSGLightmapLoader binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssglightmapio_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QSSGLightmapLoader to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QSSGLightmapLoader(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSSGLightmapLoader: a plain Python object standing in
  front of one C++ QSSGLightmapLoader.

  What exists
  -----------

  No function of Qt's QSSGLightmapLoader yet. It can be made from Python, in
  1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSSGLightmapLoader::~QSSGLightmapLoader()': the destructor: Python
    never removes a C++ QSSGLightmapLoader.
  - Qt's 'QSharedPointer<QSSGLightmapLoader> QSSGLightmapLoader::open(const
    QSharedPointer<QIODevice> &stream)': takes a type Python has no way to
    hand over yet.
  - Qt's 'QSharedPointer<QSSGLightmapLoader> QSSGLightmapLoader::open(const
    QString &path)': gives a type Python has no way to take yet.
  - Qt's 'QByteArray QSSGLightmapLoader::readF32Image(const QString &key,
    QSSGLightmapIODataTag tag) const': names the enum
    'QSSGLightmapIODataTag', whose class cannot be named here.
  - Qt's 'QByteArray QSSGLightmapLoader::readU32Image(const QString &key,
    QSSGLightmapIODataTag tag) const': names the enum
    'QSSGLightmapIODataTag', whose class cannot be named here.
  - Qt's 'QByteArray QSSGLightmapLoader::readData(const QString &key,
    QSSGLightmapIODataTag tag) const': names the enum
    'QSSGLightmapIODataTag', whose class cannot be named here.
  - Qt's 'QVariantMap QSSGLightmapLoader::readMap(const QString &key,
    QSSGLightmapIODataTag tag) const': names the enum
    'QSSGLightmapIODataTag', whose class cannot be named here.
  - Qt's 'QList<std::pair<QString, QSSGLightmapIODataTag>>
    QSSGLightmapLoader::getKeys() const': gives a type Python has no way to
    take yet.
  - Qt's 'QSSGLoadedTexture
    *QSSGLightmapLoader::createTexture(QSharedPointer<QIODevice> stream,
    const QSSGRenderTextureFormat &format, const QString &key)': takes a type
    Python has no way to hand over yet.

  What has no ritual
  ------------------

  2 of the 12 functions Qt declares: 2 forbidden.

  What to expect
  --------------

  - The C++ QSSGLightmapLoader is created at the first use, not by
    'QSSGLightmapLoader(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSSGLightmapLoader.
  - Each name of Qt's QSSGLightmapLoader that has no cute function yet,
    'createTexture', 'getKeys', 'open', 'readData', 'readF32Image',
    'readMap', 'readU32Image', holds a function that raises
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
  __qt_class__ = 'QSSGLightmapLoader'

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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QSSGLightmapLoader::QSSGLightmapLoader()', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qssglightmaploader.html#QSSGLightmapLoader
    """
    #  QSSGLightmapLoader::QSSGLightmapLoader()
    self._noteCreation(QSSGLightmapLoader, lambda: Rituals.call(
        'ritual_ZN18QSSGLightmapLoaderC1Ev',
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

  @staticmethod
  def createTexture(*__, **_) -> Never:
    """
    Qt's 'QSSGLoadedTexture
    *QSSGLightmapLoader::createTexture(QSharedPointer<QIODevice> stream,
    const QSSGRenderTextureFormat &format, const QString &key)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGLightmapLoader.createTexture' has no cute function yet. Qt's "
        "'QSSGLoadedTexture "
        "*QSSGLightmapLoader::createTexture(QSharedPointer<QIODevice> "
        "stream, const QSSGRenderTextureFormat &format, const QString "
        "&key)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def getKeys(*__, **_) -> Never:
    """
    Qt's 'QList<std::pair<QString, QSSGLightmapIODataTag>>
    QSSGLightmapLoader::getKeys() const': gives a type Python has no way to
    take yet.
    """
    raise NotImplementedError(
        "'QSSGLightmapLoader.getKeys' has no cute function yet. Qt's "
        "'QList<std::pair<QString, QSSGLightmapIODataTag>> "
        "QSSGLightmapLoader::getKeys() const': gives a type Python has no "
        "way to take yet.")

  @staticmethod
  def open(*__, **_) -> Never:
    """
    - Qt's 'QSharedPointer<QSSGLightmapLoader> QSSGLightmapLoader::open(const
      QSharedPointer<QIODevice> &stream)': takes a type Python has no way to
      hand over yet.
    - Qt's 'QSharedPointer<QSSGLightmapLoader> QSSGLightmapLoader::open(const
      QString &path)': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QSSGLightmapLoader.open' has no cute function yet. Qt's "
        "'QSharedPointer<QSSGLightmapLoader> QSSGLightmapLoader::open(const "
        "QSharedPointer<QIODevice> &stream)': takes a type Python has no "
        "way to hand over yet. Qt's 'QSharedPointer<QSSGLightmapLoader> "
        "QSSGLightmapLoader::open(const QString &path)': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def readData(*__, **_) -> Never:
    """
    Qt's 'QByteArray QSSGLightmapLoader::readData(const QString &key,
    QSSGLightmapIODataTag tag) const': names the enum
    'QSSGLightmapIODataTag', whose class cannot be named here.
    """
    raise NotImplementedError(
        "'QSSGLightmapLoader.readData' has no cute function yet. Qt's "
        "'QByteArray QSSGLightmapLoader::readData(const QString &key, "
        "QSSGLightmapIODataTag tag) const': names the enum "
        "'QSSGLightmapIODataTag', whose class cannot be named here.")

  @staticmethod
  def readF32Image(*__, **_) -> Never:
    """
    Qt's 'QByteArray QSSGLightmapLoader::readF32Image(const QString &key,
    QSSGLightmapIODataTag tag) const': names the enum
    'QSSGLightmapIODataTag', whose class cannot be named here.
    """
    raise NotImplementedError(
        "'QSSGLightmapLoader.readF32Image' has no cute function yet. Qt's "
        "'QByteArray QSSGLightmapLoader::readF32Image(const QString &key, "
        "QSSGLightmapIODataTag tag) const': names the enum "
        "'QSSGLightmapIODataTag', whose class cannot be named here.")

  @staticmethod
  def readMap(*__, **_) -> Never:
    """
    Qt's 'QVariantMap QSSGLightmapLoader::readMap(const QString &key,
    QSSGLightmapIODataTag tag) const': names the enum
    'QSSGLightmapIODataTag', whose class cannot be named here.
    """
    raise NotImplementedError(
        "'QSSGLightmapLoader.readMap' has no cute function yet. Qt's "
        "'QVariantMap QSSGLightmapLoader::readMap(const QString &key, "
        "QSSGLightmapIODataTag tag) const': names the enum "
        "'QSSGLightmapIODataTag', whose class cannot be named here.")

  @staticmethod
  def readU32Image(*__, **_) -> Never:
    """
    Qt's 'QByteArray QSSGLightmapLoader::readU32Image(const QString &key,
    QSSGLightmapIODataTag tag) const': names the enum
    'QSSGLightmapIODataTag', whose class cannot be named here.
    """
    raise NotImplementedError(
        "'QSSGLightmapLoader.readU32Image' has no cute function yet. Qt's "
        "'QByteArray QSSGLightmapLoader::readU32Image(const QString &key, "
        "QSSGLightmapIODataTag tag) const': names the enum "
        "'QSSGLightmapIODataTag', whose class cannot be named here.")
