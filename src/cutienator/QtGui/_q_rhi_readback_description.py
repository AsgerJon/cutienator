"""
QRhiReadbackDescription binding of the Qt C++
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
  from typing import Optional

  from ..QtCore import QRect
  from . import QRhiTexture
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRect = WAIT['QRect']
  QRhiTexture = WAIT['QRhiTexture']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QRhiReadbackDescription(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QRhiReadbackDescription: a plain Python object
  standing in front of one C++ QRhiReadbackDescription.

  C++ hands a QRhiReadbackDescription around as a copy, so every C++
  QRhiReadbackDescription behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QRhiReadbackDescription that has a ritual and that
  Python can call so far, 8 names in all: 'texture', 'setTexture', 'layer',
  'setLayer', 'level', 'setLevel', 'rect', 'setRect'. It can be made from
  Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QRhiReadbackDescription::~QRhiReadbackDescription()': the
    destructor: Python removes its C++ QRhiReadbackDescription by it, and has
    no other use for it.

  What to expect
  --------------

  - The C++ QRhiReadbackDescription is created at the first use, not by
    'QRhiReadbackDescription(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QRhiReadbackDescription back gives a copy the ritual
    made for Python, in a new cute QRhiReadbackDescription.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QRhiReadbackDescription'

  #  Qt's '~QRhiReadbackDescription()'. Naming it makes this a value class:
  #  Python owns every C++ QRhiReadbackDescription behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN23QRhiReadbackDescriptionD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def texture(self) -> Optional[QRhiTexture]:
    """
    Calls Qt's 'QRhiTexture *QRhiReadbackDescription::texture() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhireadbackdescription.html#texture

    Returns
    -------

    Optional[QRhiTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiTexture *QRhiReadbackDescription::texture() const
    address = self.uglySide.call(
        'ritual_ZNK23QRhiReadbackDescription7textureEv',
    )
    from . import QRhiTexture
    return QRhiTexture._cuteAt(address)

  def layer(self) -> int:
    """
    Calls Qt's 'int QRhiReadbackDescription::layer() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrhireadbackdescription.html#layer
    """
    #  int QRhiReadbackDescription::layer() const
    return self.uglySide.call('ritual_ZNK23QRhiReadbackDescription5layerEv')

  def level(self) -> int:
    """
    Calls Qt's 'int QRhiReadbackDescription::level() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrhireadbackdescription.html#level
    """
    #  int QRhiReadbackDescription::level() const
    return self.uglySide.call('ritual_ZNK23QRhiReadbackDescription5levelEv')

  def rect(self) -> QRect:
    """
    Calls Qt's 'QRect QRhiReadbackDescription::rect() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrhireadbackdescription.html#rect

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QRhiReadbackDescription::rect() const
    address = self.uglySide.call(
        'ritual_ZNK23QRhiReadbackDescription4rectEv',
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QRhiTexture)
  @overload(NoneType)
  def setTexture(self, tex: Optional[QRhiTexture]) -> None:
    """
    Calls Qt's 'void QRhiReadbackDescription::setTexture(QRhiTexture *tex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhireadbackdescription.html#setTexture

    Parameters
    ----------

    tex : Optional[QRhiTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QRhiReadbackDescription::setTexture(QRhiTexture *tex)
    self.uglySide.call(
        'ritual_ZN23QRhiReadbackDescription10setTextureEP11QRhiTexture',
        self._addressOf(tex),
    )

  @overload(int)
  def setLayer(self, layer: int) -> None:
    """
    Calls Qt's 'void QRhiReadbackDescription::setLayer(int layer)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhireadbackdescription.html#setLayer

    Parameters
    ----------

    layer : int
      Passed on as it is.
    """
    #  void QRhiReadbackDescription::setLayer(int layer)
    self.uglySide.call(
        'ritual_ZN23QRhiReadbackDescription8setLayerEi', layer,
    )

  @overload(int)
  def setLevel(self, level: int) -> None:
    """
    Calls Qt's 'void QRhiReadbackDescription::setLevel(int level)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhireadbackdescription.html#setLevel

    Parameters
    ----------

    level : int
      Passed on as it is.
    """
    #  void QRhiReadbackDescription::setLevel(int level)
    self.uglySide.call(
        'ritual_ZN23QRhiReadbackDescription8setLevelEi', level,
    )

  @overload(QRect)
  def setRect(self, rectangle: QRect) -> None:
    """
    Calls Qt's 'void QRhiReadbackDescription::setRect(const QRect
    &rectangle)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhireadbackdescription.html#setRect

    Parameters
    ----------

    rectangle : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
    """
    #  void QRhiReadbackDescription::setRect(const QRect &rectangle)
    self.uglySide.call(
        'ritual_ZN23QRhiReadbackDescription7setRectERK5QRect',
        self._valueOf(rectangle),
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
    'QRhiReadbackDescription::QRhiReadbackDescription()', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhireadbackdescription.html
    """
    #  QRhiReadbackDescription::QRhiReadbackDescription()
    self._noteCreation(QRhiReadbackDescription, lambda: Rituals.call(
        'ritual_ZN23QRhiReadbackDescriptionC1Ev',
    ))

  @overload(QRhiTexture)
  @overload(NoneType)
  def __init__(self, texture: Optional[QRhiTexture]) -> None:
    """
    Notes what was given, for Qt's
    'QRhiReadbackDescription::QRhiReadbackDescription(QRhiTexture *texture)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhireadbackdescription.html

    Parameters
    ----------

    texture : Optional[QRhiTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QRhiReadbackDescription::QRhiReadbackDescription(QRhiTexture *texture)
    self._noteCreation(QRhiReadbackDescription, lambda: Rituals.call(
        'ritual_ZN23QRhiReadbackDescriptionC1EP11QRhiTexture',
        self._addressOf(texture),
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
