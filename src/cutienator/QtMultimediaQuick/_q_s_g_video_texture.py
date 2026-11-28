"""
QSGVideoTexture binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtMultimediaQuick/6.12.0/QtMultimediaQuick/private/qsgvideotexture_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QSGVideoTexture to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..occult import Rituals
from ..QtGui import QRhiTexture
from ..QtQuick import QSGTexture

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QSize

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSGVideoTexture(QSGTexture):
  """
  The cute side of Qt's QSGVideoTexture: a plain Python object standing in
  front of one C++ QSGVideoTexture.

  It is built on the cute 'QSGTexture', as Qt's QSGVideoTexture is built on
  Qt's QSGTexture, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSGVideoTexture that has a ritual and that Python
  can call so far, 6 names in all: 'comparisonKey', 'rhiTexture',
  'textureSize', 'hasAlphaChannel', 'hasMipmaps', 'setRhiTexture'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSGVideoTexturePrivate *QSGVideoTexture::d_func()': gives
    'QSGVideoTexturePrivate', which has no cute class yet.
  - Qt's 'const QSGVideoTexturePrivate *QSGVideoTexture::d_func() const':
    gives 'QSGVideoTexturePrivate', which has no cute class yet.
  - Qt's 'QSGVideoTexture::~QSGVideoTexture()': the destructor: Python never
    removes a C++ QSGVideoTexture.
  - Qt's 'void QSGVideoTexture::setData(QRhiTexture::Format f, const QSize
    &s, const uchar *data, int bytes)': names 'uchar', which has no cute
    class yet.

  What to expect
  --------------

  - The C++ QSGVideoTexture is created at the first use, not by
    'QSGVideoTexture(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSGVideoTexture.
  - Qt tells when it has removed the C++ QSGVideoTexture. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QSGVideoTexture that has no cute function yet,
    'setData', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSGVideoTexture'

  #  A C++ QSGVideoTexture Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSGVideoTexture'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def comparisonKey(self) -> int:
    """
    Calls Qt's 'qint64 QSGVideoTexture::comparisonKey() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgvideotexture.html#comparisonKey
    """
    #  qint64 QSGVideoTexture::comparisonKey() const
    ritual = 'ritual_ZNK15QSGVideoTexture13comparisonKeyEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QSGVideoTexture13comparisonKeyEv'
    return self.uglySide.call(ritual)

  def rhiTexture(self) -> Optional[QRhiTexture]:
    """
    Calls Qt's 'QRhiTexture *QSGVideoTexture::rhiTexture() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgvideotexture.html#rhiTexture

    Returns
    -------

    Optional[QRhiTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiTexture *QSGVideoTexture::rhiTexture() const
    ritual = 'ritual_ZNK15QSGVideoTexture10rhiTextureEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QSGVideoTexture10rhiTextureEv'
    address = self.uglySide.call(ritual)
    return QRhiTexture._cuteAt(address)

  def textureSize(self) -> QSize:
    """
    Calls Qt's 'QSize QSGVideoTexture::textureSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgvideotexture.html#textureSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QSGVideoTexture::textureSize() const
    ritual = 'ritual_ZNK15QSGVideoTexture11textureSizeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QSGVideoTexture11textureSizeEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def hasAlphaChannel(self) -> bool:
    """
    Calls Qt's 'bool QSGVideoTexture::hasAlphaChannel() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgvideotexture.html#hasAlphaChannel
    """
    #  bool QSGVideoTexture::hasAlphaChannel() const
    ritual = 'ritual_ZNK15QSGVideoTexture15hasAlphaChannelEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QSGVideoTexture15hasAlphaChannelEv'
    return self.uglySide.call(ritual)

  def hasMipmaps(self) -> bool:
    """
    Calls Qt's 'bool QSGVideoTexture::hasMipmaps() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgvideotexture.html#hasMipmaps
    """
    #  bool QSGVideoTexture::hasMipmaps() const
    ritual = 'ritual_ZNK15QSGVideoTexture10hasMipmapsEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QSGVideoTexture10hasMipmapsEv'
    return self.uglySide.call(ritual)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QRhiTexture)
  @overload(NoneType)
  def setRhiTexture(self, texture: Optional[QRhiTexture]) -> None:
    """
    Calls Qt's 'void QSGVideoTexture::setRhiTexture(QRhiTexture *texture)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgvideotexture.html#setRhiTexture

    Parameters
    ----------

    texture : Optional[QRhiTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGVideoTexture::setRhiTexture(QRhiTexture *texture)
    self.uglySide.call(
        'ritual_ZN15QSGVideoTexture13setRhiTextureEP11QRhiTexture',
        self._addressOf(texture),
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
    Notes what was given, for Qt's 'QSGVideoTexture::QSGVideoTexture()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgvideotexture.html#QSGVideoTexture
    """
    #  QSGVideoTexture::QSGVideoTexture()
    self._noteCreation(QSGVideoTexture, lambda: Rituals.call(
        'ritual_ZN15QSGVideoTextureC1Ev',
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
  def setData(*__, **_) -> Never:
    """
    Qt's 'void QSGVideoTexture::setData(QRhiTexture::Format f, const QSize
    &s, const uchar *data, int bytes)': names 'uchar', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QSGVideoTexture.setData' has no cute function yet. Qt's 'void "
        "QSGVideoTexture::setData(QRhiTexture::Format f, const QSize &s, "
        "const uchar *data, int bytes)': names 'uchar', which has no cute "
        "class yet.")
