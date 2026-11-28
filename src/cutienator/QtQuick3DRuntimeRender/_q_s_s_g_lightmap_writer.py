"""
QSSGLightmapWriter binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssglightmapio_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QSSGLightmapWriter to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QSSGLightmapWriter(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSSGLightmapWriter: a plain Python object standing in
  front of one C++ QSSGLightmapWriter.

  What exists
  -----------

  Every function of Qt's QSSGLightmapWriter that has a ritual and that Python
  can call so far, 1 name in all: 'close'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSSGLightmapWriter::~QSSGLightmapWriter()': the destructor: Python
    never removes a C++ QSSGLightmapWriter.
  - Qt's 'QSharedPointer<QSSGLightmapWriter> QSSGLightmapWriter::open(const
    QSharedPointer<QIODevice> &stream)': takes a type Python has no way to
    hand over yet.
  - Qt's 'QSharedPointer<QSSGLightmapWriter> QSSGLightmapWriter::open(const
    QString &path)': gives a type Python has no way to take yet.
  - Qt's 'bool QSSGLightmapWriter::writeF32Image(const QString &key,
    QSSGLightmapIODataTag tag, const QByteArray &imageFP32)': names the enum
    'QSSGLightmapIODataTag', whose class cannot be named here.
  - Qt's 'bool QSSGLightmapWriter::writeU32Image(const QString &key,
    QSSGLightmapIODataTag tag, const QByteArray &imageU32)': names the enum
    'QSSGLightmapIODataTag', whose class cannot be named here.
  - Qt's 'bool QSSGLightmapWriter::writeData(const QString &key,
    QSSGLightmapIODataTag tag, const QByteArray &buffer)': names the enum
    'QSSGLightmapIODataTag', whose class cannot be named here.
  - Qt's 'bool QSSGLightmapWriter::writeMap(const QString &key,
    QSSGLightmapIODataTag tag, const QVariantMap &data)': names the enum
    'QSSGLightmapIODataTag', whose class cannot be named here.

  What has no ritual
  ------------------

  2 of the 11 functions Qt declares: 2 forbidden.

  What to expect
  --------------

  - The C++ QSSGLightmapWriter is created at the first use, not by
    'QSSGLightmapWriter(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSSGLightmapWriter.
  - Each name of Qt's QSSGLightmapWriter that has no cute function yet,
    'open', 'writeData', 'writeF32Image', 'writeMap', 'writeU32Image', holds
    a function that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSSGLightmapWriter'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def close(self) -> bool:
    """
    Calls Qt's 'bool QSSGLightmapWriter::close() const'.

    Qt's own words: https://doc.qt.io/qt-6/qssglightmapwriter.html#close
    """
    #  bool QSSGLightmapWriter::close() const
    return self.uglySide.call('ritual_ZNK18QSSGLightmapWriter5closeEv')

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
    'QSSGLightmapWriter::QSSGLightmapWriter()', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qssglightmapwriter.html#QSSGLightmapWriter
    """
    #  QSSGLightmapWriter::QSSGLightmapWriter()
    self._noteCreation(QSSGLightmapWriter, lambda: Rituals.call(
        'ritual_ZN18QSSGLightmapWriterC1Ev',
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
  def open(*__, **_) -> Never:
    """
    - Qt's 'QSharedPointer<QSSGLightmapWriter> QSSGLightmapWriter::open(const
      QSharedPointer<QIODevice> &stream)': takes a type Python has no way to
      hand over yet.
    - Qt's 'QSharedPointer<QSSGLightmapWriter> QSSGLightmapWriter::open(const
      QString &path)': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QSSGLightmapWriter.open' has no cute function yet. Qt's "
        "'QSharedPointer<QSSGLightmapWriter> QSSGLightmapWriter::open(const "
        "QSharedPointer<QIODevice> &stream)': takes a type Python has no "
        "way to hand over yet. Qt's 'QSharedPointer<QSSGLightmapWriter> "
        "QSSGLightmapWriter::open(const QString &path)': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def writeData(*__, **_) -> Never:
    """
    Qt's 'bool QSSGLightmapWriter::writeData(const QString &key,
    QSSGLightmapIODataTag tag, const QByteArray &buffer)': names the enum
    'QSSGLightmapIODataTag', whose class cannot be named here.
    """
    raise NotImplementedError(
        "'QSSGLightmapWriter.writeData' has no cute function yet. Qt's "
        "'bool QSSGLightmapWriter::writeData(const QString &key, "
        "QSSGLightmapIODataTag tag, const QByteArray &buffer)': names the "
        "enum 'QSSGLightmapIODataTag', whose class cannot be named here.")

  @staticmethod
  def writeF32Image(*__, **_) -> Never:
    """
    Qt's 'bool QSSGLightmapWriter::writeF32Image(const QString &key,
    QSSGLightmapIODataTag tag, const QByteArray &imageFP32)': names the enum
    'QSSGLightmapIODataTag', whose class cannot be named here.
    """
    raise NotImplementedError(
        "'QSSGLightmapWriter.writeF32Image' has no cute function yet. Qt's "
        "'bool QSSGLightmapWriter::writeF32Image(const QString &key, "
        "QSSGLightmapIODataTag tag, const QByteArray &imageFP32)': names "
        "the enum 'QSSGLightmapIODataTag', whose class cannot be named here."
    )

  @staticmethod
  def writeMap(*__, **_) -> Never:
    """
    Qt's 'bool QSSGLightmapWriter::writeMap(const QString &key,
    QSSGLightmapIODataTag tag, const QVariantMap &data)': names the enum
    'QSSGLightmapIODataTag', whose class cannot be named here.
    """
    raise NotImplementedError(
        "'QSSGLightmapWriter.writeMap' has no cute function yet. Qt's 'bool "
        "QSSGLightmapWriter::writeMap(const QString &key, "
        "QSSGLightmapIODataTag tag, const QVariantMap &data)': names the "
        "enum 'QSSGLightmapIODataTag', whose class cannot be named here.")

  @staticmethod
  def writeU32Image(*__, **_) -> Never:
    """
    Qt's 'bool QSSGLightmapWriter::writeU32Image(const QString &key,
    QSSGLightmapIODataTag tag, const QByteArray &imageU32)': names the enum
    'QSSGLightmapIODataTag', whose class cannot be named here.
    """
    raise NotImplementedError(
        "'QSSGLightmapWriter.writeU32Image' has no cute function yet. Qt's "
        "'bool QSSGLightmapWriter::writeU32Image(const QString &key, "
        "QSSGLightmapIODataTag tag, const QByteArray &imageU32)': names the "
        "enum 'QSSGLightmapIODataTag', whose class cannot be named here.")
