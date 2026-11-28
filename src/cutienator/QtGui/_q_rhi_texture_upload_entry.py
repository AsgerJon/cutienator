"""
QRhiTextureUploadEntry binding of the Qt C++
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
  from . import QRhiTextureSubresourceUploadDescription
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRhiTextureSubresourceUploadDescription = WAIT['QRhiTextureSubresourceUploadDescription']


class QRhiTextureUploadEntry(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QRhiTextureUploadEntry: a plain Python object
  standing in front of one C++ QRhiTextureUploadEntry.

  C++ hands a QRhiTextureUploadEntry around as a copy, so every C++
  QRhiTextureUploadEntry behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QRhiTextureUploadEntry that has a ritual and that
  Python can call so far, 6 names in all: 'layer', 'setLayer', 'level',
  'setLevel', 'description', 'setDescription'. It can be made from Python, in
  2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QRhiTextureUploadEntry::~QRhiTextureUploadEntry()': the destructor:
    Python removes its C++ QRhiTextureUploadEntry by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QRhiTextureUploadEntry is created at the first use, not by
    'QRhiTextureUploadEntry(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QRhiTextureUploadEntry back gives a copy the ritual
    made for Python, in a new cute QRhiTextureUploadEntry.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QRhiTextureUploadEntry'

  #  Qt's '~QRhiTextureUploadEntry()'. Naming it makes this a value class:
  #  Python owns every C++ QRhiTextureUploadEntry behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN22QRhiTextureUploadEntryD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def layer(self) -> int:
    """
    Calls Qt's 'int QRhiTextureUploadEntry::layer() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrhitextureuploadentry.html#layer
    """
    #  int QRhiTextureUploadEntry::layer() const
    return self.uglySide.call('ritual_ZNK22QRhiTextureUploadEntry5layerEv')

  def level(self) -> int:
    """
    Calls Qt's 'int QRhiTextureUploadEntry::level() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrhitextureuploadentry.html#level
    """
    #  int QRhiTextureUploadEntry::level() const
    return self.uglySide.call('ritual_ZNK22QRhiTextureUploadEntry5levelEv')

  def description(self) -> QRhiTextureSubresourceUploadDescription:
    """
    Calls Qt's 'QRhiTextureSubresourceUploadDescription
    QRhiTextureUploadEntry::description() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhitextureuploadentry.html#description

    Returns
    -------

    QRhiTextureSubresourceUploadDescription
      A new cute QRhiTextureSubresourceUploadDescription around the copy Qt
      gave back. Python owns it.
    """
    #  QRhiTextureSubresourceUploadDescription
    #      QRhiTextureUploadEntry::description() const
    address = self.uglySide.call(
        'ritual_ZNK22QRhiTextureUploadEntry11descriptionEv',
    )
    from . import QRhiTextureSubresourceUploadDescription
    return QRhiTextureSubresourceUploadDescription._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setLayer(self, layer: int) -> None:
    """
    Calls Qt's 'void QRhiTextureUploadEntry::setLayer(int layer)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhitextureuploadentry.html#setLayer

    Parameters
    ----------

    layer : int
      Passed on as it is.
    """
    #  void QRhiTextureUploadEntry::setLayer(int layer)
    self.uglySide.call('ritual_ZN22QRhiTextureUploadEntry8setLayerEi', layer)

  @overload(int)
  def setLevel(self, level: int) -> None:
    """
    Calls Qt's 'void QRhiTextureUploadEntry::setLevel(int level)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhitextureuploadentry.html#setLevel

    Parameters
    ----------

    level : int
      Passed on as it is.
    """
    #  void QRhiTextureUploadEntry::setLevel(int level)
    self.uglySide.call('ritual_ZN22QRhiTextureUploadEntry8setLevelEi', level)

  @overload(QRhiTextureSubresourceUploadDescription)
  def setDescription(
      self,
      desc: QRhiTextureSubresourceUploadDescription,
  ) -> None:
    """
    Calls Qt's 'void QRhiTextureUploadEntry::setDescription(const
    QRhiTextureSubresourceUploadDescription &desc)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhitextureuploadentry.html#setDescription

    Parameters
    ----------

    desc : QRhiTextureSubresourceUploadDescription
      Passed on as a value: Qt reads the C++
      QRhiTextureSubresourceUploadDescription, which stays Python's own.
    """
    #  void QRhiTextureUploadEntry::setDescription(const
    #      QRhiTextureSubresourceUploadDescription &desc)
    self.uglySide.call(
        'ritual_ZN22QRhiTextureUploadEntry14setDescriptionERK39QRhiTextureS'
        'ubresourceUploadDescription',
        self._valueOf(desc),
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
    'QRhiTextureUploadEntry::QRhiTextureUploadEntry()', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhitextureuploadentry.html#QRhiTextureUploadEntry
    """
    #  QRhiTextureUploadEntry::QRhiTextureUploadEntry()
    self._noteCreation(QRhiTextureUploadEntry, lambda: Rituals.call(
        'ritual_ZN22QRhiTextureUploadEntryC1Ev',
    ))

  @overload(int, int, QRhiTextureSubresourceUploadDescription)
  def __init__(
      self,
      layer: int,
      level: int,
      desc: QRhiTextureSubresourceUploadDescription,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QRhiTextureUploadEntry::QRhiTextureUploadEntry(int layer, int level,
    const QRhiTextureSubresourceUploadDescription &desc)', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhitextureuploadentry.html#QRhiTextureUploadEntry

    Parameters
    ----------

    layer : int
      Passed on as it is.

    level : int
      Passed on as it is.

    desc : QRhiTextureSubresourceUploadDescription
      Passed on as a value: Qt reads the C++
      QRhiTextureSubresourceUploadDescription, which stays Python's own.
    """
    #  QRhiTextureUploadEntry::QRhiTextureUploadEntry(int layer, int level,
    #      const QRhiTextureSubresourceUploadDescription &desc)
    self._noteCreation(QRhiTextureUploadEntry, lambda: Rituals.call(
        'ritual_ZN22QRhiTextureUploadEntryC1EiiRK39QRhiTextureSubresourceUp'
        'loadDescription',
        layer, level, self._valueOf(desc),
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
