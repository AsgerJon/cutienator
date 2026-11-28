"""
QRasterBackingStore binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qrasterbackingstore_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QRasterBackingStore to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QImage, QPlatformBackingStore

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QSize
  from . import QPaintDevice, QRegion, QWindow
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRegion = WAIT['QRegion']
  QSize = WAIT['QSize']
  QWindow = WAIT['QWindow']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QRasterBackingStore(QPlatformBackingStore):
  """
  The cute side of Qt's QRasterBackingStore: a plain Python object standing
  in front of one C++ QRasterBackingStore.

  It is built on the cute 'QPlatformBackingStore', as Qt's
  QRasterBackingStore is built on Qt's QPlatformBackingStore, and has
  everything that class has.

  C++ hands a QRasterBackingStore around as a copy, so every C++
  QRasterBackingStore behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QRasterBackingStore that has a ritual and that
  Python can call so far, 6 names in all: 'resize', 'scroll', 'beginPaint',
  'paintDevice', 'toImage', 'format'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QRasterBackingStore::~QRasterBackingStore()': the destructor:
    Python removes its C++ QRasterBackingStore by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QRasterBackingStore is created at the first use, not by
    'QRasterBackingStore(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QRasterBackingStore back gives a copy the ritual made
    for Python, in a new cute QRasterBackingStore.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QRasterBackingStore'

  #  A C++ QRasterBackingStore Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QRasterBackingStore'

  #  The functions Qt calls itself that QRasterBackingStore is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'format': (
          ('_ZNK19QRasterBackingStore6formatEv',
           ('int', 'enum', 'QtGui:QImage.Format'),
           ()),
      ),
  }

  #  Qt's '~QRasterBackingStore()'. Naming it makes this a value class:
  #  Python owns every C++ QRasterBackingStore behind a cute one, and removes
  #  it by this ritual.
  __delete_ritual__ = 'ritual_ZN19QRasterBackingStoreD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def toImage(self) -> QImage:
    """
    Calls Qt's 'QImage QRasterBackingStore::toImage() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrasterbackingstore.html#toImage

    Returns
    -------

    QImage
      A new cute QImage around the copy Qt gave back. Python owns it.
    """
    #  QImage QRasterBackingStore::toImage() const
    ritual = 'ritual_ZNK19QRasterBackingStore7toImageEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QRasterBackingStore7toImageEv'
    address = self.uglySide.call(ritual)
    return QImage._cuteOwning(address)

  def format(self) -> QImage.Format:
    """
    Calls Qt's 'QImage::Format QRasterBackingStore::format() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrasterbackingstore.html#format

    Returns
    -------

    QImage.Format
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QImage.Format(number)'
      gives.
    """
    #  QImage::Format QRasterBackingStore::format() const
    ritual = 'ritual_ZNK19QRasterBackingStore6formatEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QRasterBackingStore6formatEv'
    return QImage.Format(self.uglySide.call(ritual))

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

  @overload(QWindow)
  @overload(NoneType)
  def __init__(self, window: Optional[QWindow]) -> None:
    """
    Notes what was given, for Qt's
    'QRasterBackingStore::QRasterBackingStore(QWindow *window)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qrasterbackingstore.html#QRasterBackingStore

    Parameters
    ----------

    window : Optional[QWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QRasterBackingStore::QRasterBackingStore(QWindow *window)
    self._noteCreation(QRasterBackingStore, lambda: Rituals.call(
        'ritual_ZN19QRasterBackingStoreC1EP7QWindow',
        self._addressOf(window),
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

  @overload(QSize, QRegion)
  def resize(self, size: QSize, staticContents: QRegion) -> None:
    """
    Calls Qt's 'void QRasterBackingStore::resize(const QSize &size, const
    QRegion &staticContents)'.

    Qt's own words: https://doc.qt.io/qt-6/qrasterbackingstore.html#resize

    Parameters
    ----------

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    staticContents : QRegion
      Passed on as a value: Qt reads the C++ QRegion, which stays Python's
      own.
    """
    #  void QRasterBackingStore::resize(const QSize &size, const QRegion
    #      &staticContents)
    ritual = 'ritual_ZN19QRasterBackingStore6resizeERK5QSizeRK7QRegion'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QRasterBackingStore6resizeERK5QSizeRK7QRegion'
    self.uglySide.call(
        ritual, self._valueOf(size), self._valueOf(staticContents),
    )

  @overload(QRegion, int, int)
  def scroll(self, area: QRegion, dx: int, dy: int) -> bool:
    """
    Calls Qt's 'bool QRasterBackingStore::scroll(const QRegion &area, int dx,
    int dy)'.

    Qt's own words: https://doc.qt.io/qt-6/qrasterbackingstore.html#scroll

    Parameters
    ----------

    area : QRegion
      Passed on as a value: Qt reads the C++ QRegion, which stays Python's
      own.

    dx : int
      Passed on as it is.

    dy : int
      Passed on as it is.
    """
    #  bool QRasterBackingStore::scroll(const QRegion &area, int dx, int dy)
    ritual = 'ritual_ZN19QRasterBackingStore6scrollERK7QRegionii'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QRasterBackingStore6scrollERK7QRegionii'
    return self.uglySide.call(ritual, self._valueOf(area), dx, dy)

  @overload(QRegion)
  def beginPaint(self, region: QRegion) -> None:
    """
    Calls Qt's 'void QRasterBackingStore::beginPaint(const QRegion &region)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrasterbackingstore.html#beginPaint

    Parameters
    ----------

    region : QRegion
      Passed on as a value: Qt reads the C++ QRegion, which stays Python's
      own.
    """
    #  void QRasterBackingStore::beginPaint(const QRegion &region)
    ritual = 'ritual_ZN19QRasterBackingStore10beginPaintERK7QRegion'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QRasterBackingStore10beginPaintERK7QRegion'
    self.uglySide.call(ritual, self._valueOf(region))

  def paintDevice(self) -> Optional[QPaintDevice]:
    """
    Calls Qt's 'QPaintDevice *QRasterBackingStore::paintDevice()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrasterbackingstore.html#paintDevice

    Returns
    -------

    Optional[QPaintDevice]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPaintDevice *QRasterBackingStore::paintDevice()
    ritual = 'ritual_ZN19QRasterBackingStore11paintDeviceEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QRasterBackingStore11paintDeviceEv'
    address = self.uglySide.call(ritual)
    from . import QPaintDevice
    return QPaintDevice._cuteAt(address)
