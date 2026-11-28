"""
QSGCompressedTextureFactory binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qsgcompressedtexture_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QSGCompressedTextureFactory to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QQuickTextureFactory

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QSize
  from ..QtGui import QTextureFileData
  from . import QQuickWindow, QSGTexture
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickWindow = WAIT['QQuickWindow']
  QTextureFileData = WAIT['QTextureFileData']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSGCompressedTextureFactory(QQuickTextureFactory):
  """
  The cute side of Qt's QSGCompressedTextureFactory: a plain Python object
  standing in front of one C++ QSGCompressedTextureFactory.

  It is built on the cute 'QQuickTextureFactory', as Qt's
  QSGCompressedTextureFactory is built on Qt's QQuickTextureFactory, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QSGCompressedTextureFactory that has a ritual and
  that Python can call so far, 4 names in all: 'createTexture',
  'textureByteCount', 'textureSize', 'textureData'. It can be made from
  Python, in 1 way; see '__init__'.

  What to expect
  --------------

  - The C++ QSGCompressedTextureFactory is created at the first use, not by
    'QSGCompressedTextureFactory(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSGCompressedTextureFactory.
  - Qt tells when it has removed the C++ QSGCompressedTextureFactory. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSGCompressedTextureFactory'

  #  A C++ QSGCompressedTextureFactory Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSGCompressedTextureFactory'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QQuickWindow)
  @overload(NoneType)
  def createTexture(
      self,
      a0: Optional[QQuickWindow],
  ) -> Optional[QSGTexture]:
    """
    Calls Qt's 'QSGTexture
    *QSGCompressedTextureFactory::createTexture(QQuickWindow *a0) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgcompressedtexturefactory.html#createTexture

    Parameters
    ----------

    a0 : Optional[QQuickWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QSGTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGTexture *QSGCompressedTextureFactory::createTexture(QQuickWindow
    #      *a0) const
    ritual = (
        'ritual_ZNK27QSGCompressedTextureFactory13createTextureEP12QQuickWi'
        'ndow')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK27QSGCompressedTextureFactory13createTextureEP12QQ'
          'uickWindow')
    address = self.uglySide.call(ritual, self._addressOf(a0))
    from . import QSGTexture
    return QSGTexture._cuteAt(address)

  def textureByteCount(self) -> int:
    """
    Calls Qt's 'int QSGCompressedTextureFactory::textureByteCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgcompressedtexturefactory.html#textureByteCount
    """
    #  int QSGCompressedTextureFactory::textureByteCount() const
    ritual = 'ritual_ZNK27QSGCompressedTextureFactory16textureByteCountEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK27QSGCompressedTextureFactory16textureByteCountEv')
    return self.uglySide.call(ritual)

  def textureSize(self) -> QSize:
    """
    Calls Qt's 'QSize QSGCompressedTextureFactory::textureSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgcompressedtexturefactory.html#textureSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QSGCompressedTextureFactory::textureSize() const
    ritual = 'ritual_ZNK27QSGCompressedTextureFactory11textureSizeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK27QSGCompressedTextureFactory11textureSizeEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def textureData(self) -> Optional[QTextureFileData]:
    """
    Calls Qt's 'const QTextureFileData
    *QSGCompressedTextureFactory::textureData() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgcompressedtexturefactory.html#textureData

    Returns
    -------

    Optional[QTextureFileData]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QTextureFileData *QSGCompressedTextureFactory::textureData()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK27QSGCompressedTextureFactory11textureDataEv',
    )
    from ..QtGui import QTextureFileData
    return QTextureFileData._cuteAt(address)

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

  @overload(QTextureFileData)
  def __init__(self, texData: QTextureFileData) -> None:
    """
    Notes what was given, for Qt's
    'QSGCompressedTextureFactory::QSGCompressedTextureFactory(const
    QTextureFileData &texData)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgcompressedtexturefactory.html

    Parameters
    ----------

    texData : QTextureFileData
      Passed on as a value: Qt reads the C++ QTextureFileData, which stays
      Python's own.
    """
    #  QSGCompressedTextureFactory::QSGCompressedTextureFactory(const
    #      QTextureFileData &texData)
    self._noteCreation(QSGCompressedTextureFactory, lambda: Rituals.call(
        'ritual_ZN27QSGCompressedTextureFactoryC1ERK16QTextureFileData',
        self._valueOf(texData),
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
