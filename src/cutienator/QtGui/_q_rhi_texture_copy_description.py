"""
QRhiTextureCopyDescription binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/rhi/qrhi.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QPoint, QSize
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPoint = WAIT['QPoint']
  QSize = WAIT['QSize']


class QRhiTextureCopyDescription(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QRhiTextureCopyDescription: a plain Python object
  standing in front of one C++ QRhiTextureCopyDescription.

  C++ hands a QRhiTextureCopyDescription around as a copy, so every C++
  QRhiTextureCopyDescription behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QRhiTextureCopyDescription that has a ritual and
  that Python can call so far, 14 names in all: 'pixelSize', 'setPixelSize',
  'sourceLayer', 'setSourceLayer', 'sourceLevel', 'setSourceLevel',
  'sourceTopLeft', 'setSourceTopLeft', 'destinationLayer',
  'setDestinationLayer', 'destinationLevel', 'setDestinationLevel',
  'destinationTopLeft', 'setDestinationTopLeft'. It can be made from Python,
  in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QRhiTextureCopyDescription::~QRhiTextureCopyDescription()': the
    destructor: Python removes its C++ QRhiTextureCopyDescription by it, and
    has no other use for it.

  What to expect
  --------------

  - The C++ QRhiTextureCopyDescription is created at the first use, not by
    'QRhiTextureCopyDescription(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QRhiTextureCopyDescription back gives a copy the
    ritual made for Python, in a new cute QRhiTextureCopyDescription.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QRhiTextureCopyDescription'

  #  Qt's '~QRhiTextureCopyDescription()'. Naming it makes this a value
  #  class: Python owns every C++ QRhiTextureCopyDescription behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN26QRhiTextureCopyDescriptionD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def pixelSize(self) -> QSize:
    """
    Calls Qt's 'QSize QRhiTextureCopyDescription::pixelSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhitexturecopydescription.html#pixelSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QRhiTextureCopyDescription::pixelSize() const
    address = self.uglySide.call(
        'ritual_ZNK26QRhiTextureCopyDescription9pixelSizeEv',
    )
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def sourceLayer(self) -> int:
    """
    Calls Qt's 'int QRhiTextureCopyDescription::sourceLayer() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhitexturecopydescription.html#sourceLayer
    """
    #  int QRhiTextureCopyDescription::sourceLayer() const
    return self.uglySide.call(
        'ritual_ZNK26QRhiTextureCopyDescription11sourceLayerEv',
    )

  def sourceLevel(self) -> int:
    """
    Calls Qt's 'int QRhiTextureCopyDescription::sourceLevel() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhitexturecopydescription.html#sourceLevel
    """
    #  int QRhiTextureCopyDescription::sourceLevel() const
    return self.uglySide.call(
        'ritual_ZNK26QRhiTextureCopyDescription11sourceLevelEv',
    )

  def sourceTopLeft(self) -> QPoint:
    """
    Calls Qt's 'QPoint QRhiTextureCopyDescription::sourceTopLeft() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhitexturecopydescription.html#sourceTopLeft

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint QRhiTextureCopyDescription::sourceTopLeft() const
    address = self.uglySide.call(
        'ritual_ZNK26QRhiTextureCopyDescription13sourceTopLeftEv',
    )
    from ..QtCore import QPoint
    return QPoint._cuteOwning(address)

  def destinationLayer(self) -> int:
    """
    Calls Qt's 'int QRhiTextureCopyDescription::destinationLayer() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhitexturecopydescription.html#destinationLayer
    """
    #  int QRhiTextureCopyDescription::destinationLayer() const
    return self.uglySide.call(
        'ritual_ZNK26QRhiTextureCopyDescription16destinationLayerEv',
    )

  def destinationLevel(self) -> int:
    """
    Calls Qt's 'int QRhiTextureCopyDescription::destinationLevel() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhitexturecopydescription.html#destinationLevel
    """
    #  int QRhiTextureCopyDescription::destinationLevel() const
    return self.uglySide.call(
        'ritual_ZNK26QRhiTextureCopyDescription16destinationLevelEv',
    )

  def destinationTopLeft(self) -> QPoint:
    """
    Calls Qt's 'QPoint QRhiTextureCopyDescription::destinationTopLeft()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhitexturecopydescription.html#destinationTopLeft

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint QRhiTextureCopyDescription::destinationTopLeft() const
    address = self.uglySide.call(
        'ritual_ZNK26QRhiTextureCopyDescription18destinationTopLeftEv',
    )
    from ..QtCore import QPoint
    return QPoint._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QSize)
  def setPixelSize(self, sz: QSize) -> None:
    """
    Calls Qt's 'void QRhiTextureCopyDescription::setPixelSize(const QSize
    &sz)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhitexturecopydescription.html#setPixelSize

    Parameters
    ----------

    sz : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void QRhiTextureCopyDescription::setPixelSize(const QSize &sz)
    self.uglySide.call(
        'ritual_ZN26QRhiTextureCopyDescription12setPixelSizeERK5QSize',
        self._valueOf(sz),
    )

  @overload(int)
  def setSourceLayer(self, layer: int) -> None:
    """
    Calls Qt's 'void QRhiTextureCopyDescription::setSourceLayer(int layer)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhitexturecopydescription.html#setSourceLayer

    Parameters
    ----------

    layer : int
      Passed on as it is.
    """
    #  void QRhiTextureCopyDescription::setSourceLayer(int layer)
    self.uglySide.call(
        'ritual_ZN26QRhiTextureCopyDescription14setSourceLayerEi', layer,
    )

  @overload(int)
  def setSourceLevel(self, level: int) -> None:
    """
    Calls Qt's 'void QRhiTextureCopyDescription::setSourceLevel(int level)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhitexturecopydescription.html#setSourceLevel

    Parameters
    ----------

    level : int
      Passed on as it is.
    """
    #  void QRhiTextureCopyDescription::setSourceLevel(int level)
    self.uglySide.call(
        'ritual_ZN26QRhiTextureCopyDescription14setSourceLevelEi', level,
    )

  @overload(QPoint)
  def setSourceTopLeft(self, p: QPoint) -> None:
    """
    Calls Qt's 'void QRhiTextureCopyDescription::setSourceTopLeft(const
    QPoint &p)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhitexturecopydescription.html#setSourceTopLeft

    Parameters
    ----------

    p : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void QRhiTextureCopyDescription::setSourceTopLeft(const QPoint &p)
    self.uglySide.call(
        'ritual_ZN26QRhiTextureCopyDescription16setSourceTopLeftERK6QPoint',
        self._valueOf(p),
    )

  @overload(int)
  def setDestinationLayer(self, layer: int) -> None:
    """
    Calls Qt's 'void QRhiTextureCopyDescription::setDestinationLayer(int
    layer)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhitexturecopydescription.html

    Parameters
    ----------

    layer : int
      Passed on as it is.
    """
    #  void QRhiTextureCopyDescription::setDestinationLayer(int layer)
    self.uglySide.call(
        'ritual_ZN26QRhiTextureCopyDescription19setDestinationLayerEi',
        layer,
    )

  @overload(int)
  def setDestinationLevel(self, level: int) -> None:
    """
    Calls Qt's 'void QRhiTextureCopyDescription::setDestinationLevel(int
    level)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhitexturecopydescription.html

    Parameters
    ----------

    level : int
      Passed on as it is.
    """
    #  void QRhiTextureCopyDescription::setDestinationLevel(int level)
    self.uglySide.call(
        'ritual_ZN26QRhiTextureCopyDescription19setDestinationLevelEi',
        level,
    )

  @overload(QPoint)
  def setDestinationTopLeft(self, p: QPoint) -> None:
    """
    Calls Qt's 'void QRhiTextureCopyDescription::setDestinationTopLeft(const
    QPoint &p)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhitexturecopydescription.html

    Parameters
    ----------

    p : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void QRhiTextureCopyDescription::setDestinationTopLeft(const QPoint
    #      &p)
    self.uglySide.call(
        'ritual_ZN26QRhiTextureCopyDescription21setDestinationTopLeftERK6QP'
        'oint',
        self._valueOf(p),
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
    Notes what was given, for Qt's
    'QRhiTextureCopyDescription::QRhiTextureCopyDescription()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhitexturecopydescription.html
    """
    #  QRhiTextureCopyDescription::QRhiTextureCopyDescription()
    self._noteCreation(QRhiTextureCopyDescription, lambda: Rituals.call(
        'ritual_ZN26QRhiTextureCopyDescriptionC1Ev',
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
