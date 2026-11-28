"""
QSGMaterial binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/qsgmaterial.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, CuteFlags, MetaCute
from ..occult import Rituals
from . import QSGRendererInterface

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QSGMaterialShader, QSGMaterialType

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSGMaterial(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSGMaterial: a plain Python object standing in front
  of one C++ QSGMaterial.

  What exists
  -----------

  Every function of Qt's QSGMaterial that has a ritual and that Python can
  call so far, 6 names in all: 'type', 'createShader', 'compare', 'flags',
  'setFlag', 'viewCount'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSGMaterial::~QSGMaterial()': the destructor: Python never removes
    a C++ QSGMaterial.

  What has no ritual
  ------------------

  2 of the 10 functions Qt declares: 2 forbidden.

  What to expect
  --------------

  - The C++ QSGMaterial is created at the first use, not by
    'QSGMaterial(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSGMaterial.
  """

  #  The enums Qt writes inside QSGMaterial, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class Flag(CuteFlags):
    """
    The flags enum 'QSGMaterial::Flag' of Qt, with the 9 names Qt gives in
    it. Qt names the type of its combinations 'QSGMaterial::Flags'.
    """

    Blending = 0x1
    RequiresDeterminant = 0x2
    RequiresFullMatrixExceptTranslate = 0x6
    RequiresFullMatrix = 0xe
    NoBatching = 0x10
    MultiView2 = 0x10000
    MultiView3 = 0x20000
    MultiView4 = 0x40000
    CustomCompileStep = 0x10

  Flags = Flag

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSGMaterial'

  #  A C++ QSGMaterial Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSGMaterial'

  #  The functions Qt calls itself that QSGMaterial is the first to declare.
  #  A class of a program built on it can write one anew, and Qt then calls
  #  that. For each name: the key C++ knows the function by, what it gives,
  #  and what it takes.
  __virtual_functions__ = {
      'type': (
          ('_ZNK11QSGMaterial4typeEv',
           ('address', 'address', 'QtQuick:QSGMaterialType'),
           ()),
      ),
      'createShader': (
          ('_ZNK11QSGMaterial12createShaderEN20QSGRendererInterface10Render'
           'ModeE',
           ('address', 'address', 'QtQuick:QSGMaterialShader'),
           (
               ('int', 'enum', 'QtQuick:QSGRendererInterface.RenderMode'),
           )),
      ),
      'compare': (
          ('_ZNK11QSGMaterial7compareEPKS_',
           ('int', 'number', ''),
           (
               ('address', 'address', 'QtQuick:QSGMaterial'),
           )),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def type(self) -> Optional[QSGMaterialType]:
    """
    Calls Qt's 'QSGMaterialType *QSGMaterial::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgmaterial.html#type

    Returns
    -------

    Optional[QSGMaterialType]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGMaterialType *QSGMaterial::type() const
    address = self.uglySide.call('ritual_ZNK11QSGMaterial4typeEv')
    from . import QSGMaterialType
    return QSGMaterialType._cuteAt(address)

  @overload(QSGRendererInterface.RenderMode)
  def createShader(
      self,
      renderMode: QSGRendererInterface.RenderMode,
  ) -> Optional[QSGMaterialShader]:
    """
    Calls Qt's 'QSGMaterialShader
    *QSGMaterial::createShader(QSGRendererInterface::RenderMode renderMode)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgmaterial.html#createShader

    Parameters
    ----------

    renderMode : QSGRendererInterface.RenderMode
      Passed on as its number.

    Returns
    -------

    Optional[QSGMaterialShader]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGMaterialShader
    #      *QSGMaterial::createShader(QSGRendererInterface::RenderMode
    #      renderMode) const
    address = self.uglySide.call(
        'ritual_ZNK11QSGMaterial12createShaderEN20QSGRendererInterface10Ren'
        'derModeE',
        renderMode.value,
    )
    from . import QSGMaterialShader
    return QSGMaterialShader._cuteAt(address)

  @overload(THIS)
  @overload(NoneType)
  def compare(self, other: Optional[QSGMaterial]) -> int:
    """
    Calls Qt's 'int QSGMaterial::compare(const QSGMaterial *other) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgmaterial.html#compare

    Parameters
    ----------

    other : Optional[QSGMaterial]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  int QSGMaterial::compare(const QSGMaterial *other) const
    ritual = 'ritual_ZNK11QSGMaterial7compareEPKS_'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QSGMaterial7compareEPKS_'
    return self.uglySide.call(ritual, self._addressOf(other))

  def flags(self) -> Flags:
    """
    Calls Qt's 'QSGMaterial::Flags QSGMaterial::flags() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgmaterial.html#flags

    Returns
    -------

    Flags
      The value standing for the combination Qt gave back.
    """
    #  QSGMaterial::Flags QSGMaterial::flags() const
    return QSGMaterial.Flags(self.uglySide.call(
        'ritual_ZNK11QSGMaterial5flagsEv',
    ))

  def viewCount(self) -> int:
    """
    Calls Qt's 'int QSGMaterial::viewCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgmaterial.html#viewCount
    """
    #  int QSGMaterial::viewCount() const
    return self.uglySide.call('ritual_ZNK11QSGMaterial9viewCountEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Flags)
  @overload(Flags, bool)
  def setFlag(self, flags: Flags, on: bool = True) -> None:
    """
    Calls Qt's 'void QSGMaterial::setFlag(Flags flags, bool on)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgmaterial.html#setFlag

    Parameters
    ----------

    flags : Flags
      Passed on as its number.

    on : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QSGMaterial::setFlag(Flags flags, bool on)
    self.uglySide.call(
        'ritual_ZN11QSGMaterial7setFlagE6QFlagsINS_4FlagEEb',
        flags.value, on,
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
    Notes what was given, for Qt's 'QSGMaterial::QSGMaterial()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qsgmaterial.html#QSGMaterial
    """
    #  QSGMaterial::QSGMaterial()
    self._noteCreation(QSGMaterial, lambda: Rituals.call(
        'ritual_ZN11QSGMaterialC1Ev',
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
