"""
QRhiBackingStore binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qrhibackingstore_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QRhiBackingStore to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QImage, QRasterBackingStore

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QPoint
  from . import QRegion, QWindow
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPoint = WAIT['QPoint']
  QRegion = WAIT['QRegion']
  QWindow = WAIT['QWindow']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QRhiBackingStore(QRasterBackingStore):
  """
  The cute side of Qt's QRhiBackingStore: a plain Python object standing in
  front of one C++ QRhiBackingStore.

  It is built on the cute 'QRasterBackingStore', as Qt's QRhiBackingStore is
  built on Qt's QRasterBackingStore, and has everything that class has.

  C++ hands a QRhiBackingStore around as a copy, so every C++
  QRhiBackingStore behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QRhiBackingStore that has a ritual and that Python
  can call so far, 2 names in all: 'flush', 'format'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QRhiBackingStore::~QRhiBackingStore()': the destructor: Python
    removes its C++ QRhiBackingStore by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QRhiBackingStore is created at the first use, not by
    'QRhiBackingStore(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QRhiBackingStore back gives a copy the ritual made
    for Python, in a new cute QRhiBackingStore.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QRhiBackingStore'

  #  A C++ QRhiBackingStore Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QRhiBackingStore'

  #  Qt's '~QRhiBackingStore()'. Naming it makes this a value class: Python
  #  owns every C++ QRhiBackingStore behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN16QRhiBackingStoreD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def format(self) -> QImage.Format:
    """
    Calls Qt's 'QImage::Format QRhiBackingStore::format() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrhibackingstore.html#format

    Returns
    -------

    QImage.Format
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QImage.Format(number)'
      gives.
    """
    #  QImage::Format QRhiBackingStore::format() const
    ritual = 'ritual_ZNK16QRhiBackingStore6formatEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK16QRhiBackingStore6formatEv'
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
    'QRhiBackingStore::QRhiBackingStore(QWindow *window)', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhibackingstore.html#QRhiBackingStore

    Parameters
    ----------

    window : Optional[QWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QRhiBackingStore::QRhiBackingStore(QWindow *window)
    self._noteCreation(QRhiBackingStore, lambda: Rituals.call(
        'ritual_ZN16QRhiBackingStoreC1EP7QWindow', self._addressOf(window),
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

  @overload(QWindow, QRegion, QPoint)
  @overload(NoneType, QRegion, QPoint)
  def flush(
      self,
      window: Optional[QWindow],
      region: QRegion,
      offset: QPoint,
  ) -> None:
    """
    Calls Qt's 'void QRhiBackingStore::flush(QWindow *window, const QRegion
    &region, const QPoint &offset)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhibackingstore.html#flush

    Parameters
    ----------

    window : Optional[QWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    region : QRegion
      Passed on as a value: Qt reads the C++ QRegion, which stays Python's
      own.

    offset : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void QRhiBackingStore::flush(QWindow *window, const QRegion &region,
    #      const QPoint &offset)
    ritual = 'ritual_ZN16QRhiBackingStore5flushEP7QWindowRK7QRegionRK6QPoint'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QRhiBackingStore5flushEP7QWindowRK7QRegionRK6QPoi'
          'nt')
    self.uglySide.call(
        ritual,
        self._addressOf(window), self._valueOf(region),
        self._valueOf(offset),
    )
