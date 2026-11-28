"""
QSvgImage binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSvg/6.12.0/QtSvg/private/qsvggraphics_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QSvgImage to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QSvgNode

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QRectF
  from ..QtGui import QImage
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QImage = WAIT['QImage']
  QRectF = WAIT['QRectF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSvgImage(QSvgNode):
  """
  The cute side of Qt's QSvgImage: a plain Python object standing in front of
  one C++ QSvgImage.

  It is built on the cute 'QSvgNode', as Qt's QSvgImage is built on Qt's
  QSvgNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSvgImage that has a ritual and that Python can call
  so far, 4 names in all: 'type', 'rect', 'image', 'filename'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSvgImage::~QSvgImage()': the destructor: Python never removes a
    C++ QSvgImage.
  - Qt's 'void QSvgImage::drawCommand(QPainter *p, QSvgExtraStates &states)':
    takes a type Python has no way to hand over yet.
  - Qt's 'QRectF QSvgImage::internalBounds(QPainter *p, QSvgExtraStates
    &states) const': takes a type Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ QSvgImage is created at the first use, not by 'QSvgImage(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSvgImage.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSvgImage'

  #  A C++ QSvgImage Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSvgImage'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def type(self) -> QSvgNode.Type:
    """
    Calls Qt's 'Type QSvgImage::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgimage.html#type

    Returns
    -------

    QSvgNode.Type
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QSvgNode.Type(number)'
      gives.
    """
    #  Type QSvgImage::type() const
    ritual = 'ritual_ZNK9QSvgImage4typeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK9QSvgImage4typeEv'
    return QSvgNode.Type(self.uglySide.call(ritual))

  def rect(self) -> QRectF:
    """
    Calls Qt's 'QRectF QSvgImage::rect() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgimage.html#rect

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QSvgImage::rect() const
    address = self.uglySide.call('ritual_ZNK9QSvgImage4rectEv')
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def image(self) -> QImage:
    """
    Calls Qt's 'const QImage &QSvgImage::image() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgimage.html#image

    Returns
    -------

    QImage
      A new cute QImage around the copy Qt gave back. Python owns it.
    """
    #  const QImage &QSvgImage::image() const
    address = self.uglySide.call('ritual_ZNK9QSvgImage5imageEv')
    from ..QtGui import QImage
    return QImage._cuteOwning(address)

  def filename(self) -> str:
    """
    Calls Qt's 'QString QSvgImage::filename() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgimage.html#filename

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSvgImage::filename() const
    return self.uglySide.call('ritual_ZNK9QSvgImage8filenameEv')

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

  @overload(QSvgNode, QImage, str, QRectF)
  @overload(NoneType, QImage, str, QRectF)
  def __init__(
      self,
      parent: Optional[QSvgNode],
      image: QImage,
      filename: str,
      bounds: QRectF,
  ) -> None:
    """
    Notes what was given, for Qt's 'QSvgImage::QSvgImage(QSvgNode *parent,
    const QImage &image, const QString &filename, const QRectF &bounds)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qsvgimage.html#QSvgImage

    Parameters
    ----------

    parent : Optional[QSvgNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    image : QImage
      Passed on as a value: Qt reads the C++ QImage, which stays Python's
      own.

    filename : str
      Passed on as it is: a QString is made of it for the call.

    bounds : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  QSvgImage::QSvgImage(QSvgNode *parent, const QImage &image, const
    #      QString &filename, const QRectF &bounds)
    self._noteCreation(QSvgImage, lambda: Rituals.call(
        'ritual_ZN9QSvgImageC1EP8QSvgNodeRK6QImageRK7QStringRK6QRectF',
        self._addressOf(parent), self._valueOf(image), filename,
        self._valueOf(bounds),
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
