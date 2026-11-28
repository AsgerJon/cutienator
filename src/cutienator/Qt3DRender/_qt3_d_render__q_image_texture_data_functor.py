"""
Qt3DRender::QImageTextureDataFunctor binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/6.12.0/Qt3DRender/private/qtextureimage_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means Qt3DRender::QImageTextureDataFunctor to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from . import Qt3DRender

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QUrl


class QImageTextureDataFunctor(Qt3DRender.QTextureImageDataGenerator):
  """
  The cute side of Qt's Qt3DRender::QImageTextureDataFunctor: a plain Python
  object standing in front of one C++ Qt3DRender::QImageTextureDataFunctor.

  It is built on the cute 'Qt3DRender::QTextureImageDataGenerator', as Qt's
  Qt3DRender::QImageTextureDataFunctor is built on Qt's
  Qt3DRender::QTextureImageDataGenerator, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::QImageTextureDataFunctor that has a
  ritual and that Python can call so far, 4 names in all: 'status', 'id',
  'url', 'isMirrored'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'bool Qt3DRender::QImageTextureDataFunctor::operator==(const
    QTextureImageDataGenerator &other) const': takes a type Python has no way
    to hand over yet.

  What has no ritual
  ------------------

  2 of the 7 functions Qt declares: 2 leans on 'Qt3DRender.

  What to expect
  --------------

  - The C++ Qt3DRender::QImageTextureDataFunctor is created at the first use,
    not by 'Qt3DRender::QImageTextureDataFunctor(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::QImageTextureDataFunctor.
  - Each name of Qt's Qt3DRender::QImageTextureDataFunctor that has no cute
    function yet, '__init__', holds a function that raises
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
  __qt_class__ = 'Qt3DRender::QImageTextureDataFunctor'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def status(self) -> Qt3DRender.QTextureImage.Status:
    """
    Calls Qt's 'QTextureImage::Status
    Qt3DRender::QImageTextureDataFunctor::status() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qimagetexturedatafunctor.html#status

    Returns
    -------

    Qt3DRender.QTextureImage.Status
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt3DRender.QTextureImage.Status(number)' gives.
    """
    #  QTextureImage::Status Qt3DRender::QImageTextureDataFunctor::status()
    #      const
    return Qt3DRender.QTextureImage.Status(self.uglySide.call(
        'ritual_ZNK10Qt3DRender24QImageTextureDataFunctor6statusEv',
    ))

  def id(self) -> int:
    """
    Calls Qt's 'qintptr Qt3DRender::QImageTextureDataFunctor::id() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qimagetexturedatafunctor.html#id
    """
    #  qintptr Qt3DRender::QImageTextureDataFunctor::id() const
    ritual = 'ritual_ZNK10Qt3DRender24QImageTextureDataFunctor2idEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK10Qt3DRender24QImageTextureDataFunctor2idEv'
    return self.uglySide.call(ritual)

  def url(self) -> QUrl:
    """
    Calls Qt's 'QUrl Qt3DRender::QImageTextureDataFunctor::url() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qimagetexturedatafunctor.html#url

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl Qt3DRender::QImageTextureDataFunctor::url() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender24QImageTextureDataFunctor3urlEv',
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def isMirrored(self) -> bool:
    """
    Calls Qt's 'bool Qt3DRender::QImageTextureDataFunctor::isMirrored()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qimagetexturedatafunctor.html
    """
    #  bool Qt3DRender::QImageTextureDataFunctor::isMirrored() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender24QImageTextureDataFunctor10isMirroredEv',
    )

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
    'Qt3DRender::QImageTextureDataFunctor::QImageTextureDataFunctor(const
    QUrl &url, bool mirrored)': leans on
    'Qt3DRender::TextureLoadingHelper::loadTextureData(QIODevice*, QString
    const&, bool, bool)', which Qt's source does not mark for use from
    outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'Qt3DRender.QImageTextureDataFunctor.__init__' has no cute "
        "function yet. Qt's "
        "'Qt3DRender::QImageTextureDataFunctor::QImageTextureDataFunctor(con"
        "st QUrl &url, bool mirrored)': leans on "
        "'Qt3DRender::TextureLoadingHelper::loadTextureData(QIODevice*, "
        "QString const&, bool, bool)', which Qt's source does not mark for "
        "use from outside Qt and has no code for that could be taken.")

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
