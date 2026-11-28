"""
QSSGSceneDesc::TextureData binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DAssetUtils/6.12.0/QtQuick3DAssetUtils/private/qssgscenedesc_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QSSGSceneDesc::TextureData to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteNum, WAIT
from ..occult import Rituals
from . import QSSGSceneDesc

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QByteArray, QSize
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QSize = WAIT['QSize']


class TextureData(QSSGSceneDesc.Node):
  """
  The cute side of Qt's QSSGSceneDesc::TextureData: a plain Python object
  standing in front of one C++ QSSGSceneDesc::TextureData.

  It is built on the cute 'QSSGSceneDesc::Node', as Qt's
  QSSGSceneDesc::TextureData is built on Qt's QSSGSceneDesc::Node, and has
  everything that class has.

  C++ hands a QSSGSceneDesc::TextureData around as a copy, so every C++
  QSSGSceneDesc::TextureData behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  No function of Qt's QSSGSceneDesc::TextureData yet. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSSGSceneDesc::TextureData::~TextureData()': the destructor: Python
    removes its C++ QSSGSceneDesc::TextureData by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QSSGSceneDesc::TextureData is created at the first use, not by
    'QSSGSceneDesc::TextureData(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSSGSceneDesc::TextureData back gives a copy the
    ritual made for Python, in a new cute QSSGSceneDesc::TextureData.
  """

  #  The enums Qt writes inside QSSGSceneDesc::TextureData, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class Flags(CuteNum, scoped=True):
    """
    The enum 'QSSGSceneDesc::TextureData::Flags' of Qt, with the 1 names Qt
    gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    Compressed = Kee[int](1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSSGSceneDesc::TextureData'

  #  Qt's '~QSSGSceneDesc::TextureData()'. Naming it makes this a value
  #  class: Python owns every C++ QSSGSceneDesc::TextureData behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN13QSSGSceneDesc11TextureDataD1Ev'

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

  @overload(QByteArray, QSize, QByteArray)
  @overload(QByteArray, QSize, QByteArray, int)
  @overload(QByteArray, QSize, QByteArray, int, QByteArray)
  def __init__(
      self,
      textureData: QByteArray,
      size: QSize,
      format: QByteArray,
      flags: int = 0,
      name: Optional[QByteArray] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QSSGSceneDesc::TextureData::TextureData(const QByteArray &textureData,
    QSize size, const QByteArray &format, quint8 flags, QByteArray name)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgscenedesc-texturedata.html#TextureData

    Parameters
    ----------

    textureData : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    format : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    flags : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    name : Optional[QByteArray]
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own. May be left out, as in Qt: a new 'QByteArray()' is then passed on.
    """
    #  QSSGSceneDesc::TextureData::TextureData(const QByteArray &textureData,
    #      QSize size, const QByteArray &format, quint8 flags, QByteArray
    #      name)
    if name is None:
      from ..QtCore import QByteArray
      name = QByteArray()
    self._noteCreation(TextureData, lambda: Rituals.call(
        'ritual_ZN13QSSGSceneDesc11TextureDataC1ERK10QByteArray5QSizeS3_hS1'
        '_',
        self._valueOf(textureData), self._valueOf(size),
        self._valueOf(format), flags, self._valueOf(name),
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
