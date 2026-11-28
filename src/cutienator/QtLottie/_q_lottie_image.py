"""
QLottieImage binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLottie/6.12.0/QtLottie/private/qlottieimage_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QLottieImage to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QLottieBase

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QJsonObject, QSizeF, QUrl
  from ..QtGui import QImage
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QJsonObject = WAIT['QJsonObject']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QLottieImage(QLottieBase):
  """
  The cute side of Qt's QLottieImage: a plain Python object standing in front
  of one C++ QLottieImage.

  It is built on the cute 'QLottieBase', as Qt's QLottieImage is built on
  Qt's QLottieBase, and has everything that class has.

  C++ hands a QLottieImage around as a copy, so every C++ QLottieImage behind
  a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QLottieImage that has a ritual and that Python can
  call so far, 5 names in all: 'clone', 'construct', 'url', 'size', 'image'.
  It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QLottieImage::render(QLottieRenderer &renderer) const': takes
    a type Python has no way to hand over yet.
  - Qt's 'QLottieImage::~QLottieImage()': the destructor: Python removes its
    C++ QLottieImage by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QLottieImage is created at the first use, not by
    'QLottieImage(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QLottieImage back gives a copy the ritual made for
    Python, in a new cute QLottieImage.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QLottieImage'

  #  A C++ QLottieImage Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QLottieImage'

  #  Qt's '~QLottieImage()'. Naming it makes this a value class: Python owns
  #  every C++ QLottieImage behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN12QLottieImageD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def clone(self) -> Optional[QLottieBase]:
    """
    Calls Qt's 'QLottieBase *QLottieImage::clone() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlottieimage.html#clone

    Returns
    -------

    Optional[QLottieBase]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QLottieBase *QLottieImage::clone() const
    ritual = 'ritual_ZNK12QLottieImage5cloneEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK12QLottieImage5cloneEv'
    address = self.uglySide.call(ritual)
    return QLottieBase._cuteAt(address)

  def url(self) -> QUrl:
    """
    Calls Qt's 'QUrl QLottieImage::url() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlottieimage.html#url

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QLottieImage::url() const
    address = self.uglySide.call('ritual_ZNK12QLottieImage3urlEv')
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def size(self) -> QSizeF:
    """
    Calls Qt's 'QSizeF QLottieImage::size() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlottieimage.html#size

    Returns
    -------

    QSizeF
      A new cute QSizeF around the copy Qt gave back. Python owns it.
    """
    #  QSizeF QLottieImage::size() const
    address = self.uglySide.call('ritual_ZNK12QLottieImage4sizeEv')
    from ..QtCore import QSizeF
    return QSizeF._cuteOwning(address)

  def image(self) -> QImage:
    """
    Calls Qt's 'QImage QLottieImage::image() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlottieimage.html#image

    Returns
    -------

    QImage
      A new cute QImage around the copy Qt gave back. Python owns it.
    """
    #  QImage QLottieImage::image() const
    address = self.uglySide.call('ritual_ZNK12QLottieImage5imageEv')
    from ..QtGui import QImage
    return QImage._cuteOwning(address)

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

  @overload(THIS)
  def __init__(self, other: QLottieImage) -> None:
    """
    Notes what was given, for Qt's 'QLottieImage::QLottieImage(const
    QLottieImage &other)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qlottieimage.html#QLottieImage

    Parameters
    ----------

    other : QLottieImage
      Passed on as a value: Qt reads the C++ QLottieImage, which stays
      Python's own.
    """
    #  QLottieImage::QLottieImage(const QLottieImage &other)
    self._noteCreation(QLottieImage, lambda: Rituals.call(
        'ritual_ZN12QLottieImageC1ERKS_', self._valueOf(other),
    ))

  @overload()
  @overload(QLottieBase)
  @overload(NoneType)
  def __init__(self, parent: Optional[QLottieBase] = None) -> None:
    """
    Notes what was given, for Qt's 'QLottieImage::QLottieImage(QLottieBase
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qlottieimage.html#QLottieImage

    Parameters
    ----------

    parent : Optional[QLottieBase]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QLottieImage::QLottieImage(QLottieBase *parent)
    self._noteCreation(QLottieImage, lambda: Rituals.call(
        'ritual_ZN12QLottieImageC1EP11QLottieBase', self._addressOf(parent),
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

  @overload(QJsonObject)
  def construct(self, definition: QJsonObject) -> int:
    """
    Calls Qt's 'int QLottieImage::construct(const QJsonObject &definition)'.

    Qt's own words: https://doc.qt.io/qt-6/qlottieimage.html#construct

    Parameters
    ----------

    definition : QJsonObject
      Passed on as a value: Qt reads the C++ QJsonObject, which stays
      Python's own.
    """
    #  int QLottieImage::construct(const QJsonObject &definition)
    return self.uglySide.call(
        'ritual_ZN12QLottieImage9constructERK11QJsonObject',
        self._valueOf(definition),
    )
