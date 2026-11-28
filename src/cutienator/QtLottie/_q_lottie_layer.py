"""
QLottieLayer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLottie/6.12.0/QtLottie/private/qlottielayer_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QLottieLayer to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from . import QLottieBase
from ..QtCore import QMap

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QLottieBasicTransform
  from ..QtCore import QJsonArray, QJsonObject, QSize
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QJsonArray = WAIT['QJsonArray']
  QJsonObject = WAIT['QJsonObject']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QLottieLayer(QLottieBase):
  """
  The cute side of Qt's QLottieLayer: a plain Python object standing in front
  of one C++ QLottieLayer.

  It is built on the cute 'QLottieBase', as Qt's QLottieLayer is built on
  Qt's QLottieBase, and has everything that class has.

  C++ hands a QLottieLayer around as a copy, so every C++ QLottieLayer behind
  a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QLottieLayer that has a ritual and that Python can
  call so far, 25 names in all: 'clone', 'construct', 'constructMaskLayer',
  'constructLayers', 'active', 'parse', 'updateProperties', 'findChild',
  'isUsingMatteLayer', 'isMatteLayer', 'matteMode', 'isAutoOrienting',
  'layerId', 'transform', 'hasLinkedLayer', 'linkedLayerId', 'layerSize',
  'startFrame', 'endFrame', 'frameOffset', 'timeStretch', 'checkedCast',
  'resolveLinkedLayer', 'linkedLayer', 'parseEffects'. It can be made from
  Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QLottieLayer::~QLottieLayer()': the destructor: Python removes its
    C++ QLottieLayer by it, and has no other use for it.
  - Qt's 'void QLottieLayer::render(QLottieRenderer &renderer) const': takes
    a type Python has no way to hand over yet.
  - Qt's 'void QLottieLayer::applyLayerTransform(QLottieRenderer &renderer)
    const': takes a type Python has no way to hand over yet.
  - Qt's 'void QLottieLayer::renderEffects(QLottieRenderer &renderer) const':
    takes a type Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ QLottieLayer is created at the first use, not by
    'QLottieLayer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QLottieLayer back gives a copy the ritual made for
    Python, in a new cute QLottieLayer.
  - Each name of Qt's QLottieLayer that has no cute function yet,
    'applyLayerTransform', 'renderEffects', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QLottieLayer, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class MatteClipMode(CuteNum):
    """
    The enum 'QLottieLayer::MatteClipMode' of Qt, with the 5 names Qt gives
    in it.
    """

    NoClip = Kee[int](0)
    Alpha = Kee[int](1)
    InvertedAlpha = Kee[int](2)
    Luminence = Kee[int](3)
    InvertedLuminence = Kee[int](4)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QJsonObject)
  def construct(definition: QJsonObject) -> Optional[QLottieLayer]:
    """
    Calls Qt's 'QLottieLayer *QLottieLayer::construct(QJsonObject
    definition)'.

    Qt's own words: https://doc.qt.io/qt-6/qlottielayer.html#construct

    Parameters
    ----------

    definition : QJsonObject
      Passed on as a value: Qt reads the C++ QJsonObject, which stays
      Python's own.

    Returns
    -------

    Optional[QLottieLayer]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QLottieLayer *QLottieLayer::construct(QJsonObject definition)
    address = Rituals.call(
        'ritual_ZN12QLottieLayer9constructE11QJsonObject',
        CuteMixin._valueOf(definition),
    )
    return QLottieLayer._cuteAt(address)

  @staticmethod
  @overload(THIS)
  @overload(NoneType)
  def constructMaskLayer(
      layer: Optional[QLottieLayer],
  ) -> Optional[QLottieLayer]:
    """
    Calls Qt's 'QLottieLayer *QLottieLayer::constructMaskLayer(QLottieLayer
    *layer)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlottielayer.html#constructMaskLayer

    Parameters
    ----------

    layer : Optional[QLottieLayer]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QLottieLayer]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QLottieLayer *QLottieLayer::constructMaskLayer(QLottieLayer *layer)
    address = Rituals.call(
        'ritual_ZN12QLottieLayer18constructMaskLayerEPS_',
        CuteMixin._addressOf(layer),
    )
    return QLottieLayer._cuteAt(address)

  @staticmethod
  @overload(QJsonArray, QLottieBase, QMap[str, QJsonObject])
  @overload(QJsonArray, NoneType, QMap[str, QJsonObject])
  def constructLayers(
      jsonLayers: QJsonArray,
      parent: Optional[QLottieBase],
      assets: QMap[str, QJsonObject],
  ) -> int:
    """
    Calls Qt's 'int QLottieLayer::constructLayers(QJsonArray jsonLayers,
    QLottieBase *parent, const QMap<QString, QJsonObject> &assets)'.

    Qt's own words: https://doc.qt.io/qt-6/qlottielayer.html#constructLayers

    Parameters
    ----------

    jsonLayers : QJsonArray
      Passed on as a value: Qt reads the C++ QJsonArray, which stays Python's
      own.

    parent : Optional[QLottieBase]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    assets : QMap[str, QJsonObject]
      Passed on as a map of Qt: Qt reads the C++ map, which stays Python's
      own. A dict of Python is made into one first, and refused when a key or
      a value does not fit.
    """
    #  int QLottieLayer::constructLayers(QJsonArray jsonLayers, QLottieBase
    #      *parent, const QMap<QString, QJsonObject> &assets)
    return Rituals.call(
        'ritual_ZN12QLottieLayer15constructLayersE10QJsonArrayP11QLottieBas'
        'eRK4QMapI7QString11QJsonObjectE',
        CuteMixin._valueOf(jsonLayers), CuteMixin._addressOf(parent),
        CuteMixin._valueOf(assets),
    )

  @staticmethod
  @overload(QLottieBase)
  @overload(NoneType)
  def checkedCast(node: Optional[QLottieBase]) -> Optional[QLottieLayer]:
    """
    Calls Qt's 'const QLottieLayer *QLottieLayer::checkedCast(const
    QLottieBase *node)'.

    Qt's own words: https://doc.qt.io/qt-6/qlottielayer.html#checkedCast

    Parameters
    ----------

    node : Optional[QLottieBase]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QLottieLayer]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QLottieLayer *QLottieLayer::checkedCast(const QLottieBase *node)
    address = Rituals.call(
        'ritual_ZN12QLottieLayer11checkedCastEPK11QLottieBase',
        CuteMixin._addressOf(node),
    )
    return QLottieLayer._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QLottieLayer'

  #  A C++ QLottieLayer Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QLottieLayer'

  #  The functions Qt calls itself that QLottieLayer is the first to declare.
  #  A class of a program built on it can write one anew, and Qt then calls
  #  that. For each name: the key C++ knows the function by, what it gives,
  #  and what it takes.
  __virtual_functions__ = {
      'resolveLinkedLayer': (
          ('_ZN12QLottieLayer18resolveLinkedLayerEv',
           ('address', 'address', 'QtLottie:QLottieLayer'),
           ()),
      ),
      'linkedLayer': (
          ('_ZNK12QLottieLayer11linkedLayerEv',
           ('address', 'address', 'QtLottie:QLottieLayer'),
           ()),
      ),
  }

  #  Qt's '~QLottieLayer()'. Naming it makes this a value class: Python owns
  #  every C++ QLottieLayer behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN12QLottieLayerD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def clone(self) -> Optional[QLottieBase]:
    """
    Calls Qt's 'QLottieBase *QLottieLayer::clone() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlottielayer.html#clone

    Returns
    -------

    Optional[QLottieBase]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QLottieBase *QLottieLayer::clone() const
    ritual = 'ritual_ZNK12QLottieLayer5cloneEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK12QLottieLayer5cloneEv'
    address = self.uglySide.call(ritual)
    return QLottieBase._cuteAt(address)

  @overload(int)
  def active(self, frame: int) -> bool:
    """
    Calls Qt's 'bool QLottieLayer::active(int frame) const'.

    Qt's own words: https://doc.qt.io/qt-6/qlottielayer.html#active

    Parameters
    ----------

    frame : int
      Passed on as it is.
    """
    #  bool QLottieLayer::active(int frame) const
    ritual = 'ritual_ZNK12QLottieLayer6activeEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK12QLottieLayer6activeEi'
    return self.uglySide.call(ritual, frame)

  def isUsingMatteLayer(self) -> bool:
    """
    Calls Qt's 'bool QLottieLayer::isUsingMatteLayer() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlottielayer.html#isUsingMatteLayer
    """
    #  bool QLottieLayer::isUsingMatteLayer() const
    return self.uglySide.call(
        'ritual_ZNK12QLottieLayer17isUsingMatteLayerEv',
    )

  def isMatteLayer(self) -> bool:
    """
    Calls Qt's 'bool QLottieLayer::isMatteLayer() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlottielayer.html#isMatteLayer
    """
    #  bool QLottieLayer::isMatteLayer() const
    return self.uglySide.call('ritual_ZNK12QLottieLayer12isMatteLayerEv')

  def matteMode(self) -> MatteClipMode:
    """
    Calls Qt's 'MatteClipMode QLottieLayer::matteMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlottielayer.html#matteMode

    Returns
    -------

    MatteClipMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'MatteClipMode(number)'
      gives.
    """
    #  MatteClipMode QLottieLayer::matteMode() const
    return QLottieLayer.MatteClipMode(self.uglySide.call(
        'ritual_ZNK12QLottieLayer9matteModeEv',
    ))

  def isAutoOrienting(self) -> bool:
    """
    Calls Qt's 'bool QLottieLayer::isAutoOrienting() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlottielayer.html#isAutoOrienting
    """
    #  bool QLottieLayer::isAutoOrienting() const
    return self.uglySide.call('ritual_ZNK12QLottieLayer15isAutoOrientingEv')

  def layerId(self) -> int:
    """
    Calls Qt's 'int QLottieLayer::layerId() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlottielayer.html#layerId
    """
    #  int QLottieLayer::layerId() const
    return self.uglySide.call('ritual_ZNK12QLottieLayer7layerIdEv')

  def transform(self) -> Optional[QLottieBasicTransform]:
    """
    Calls Qt's 'QLottieBasicTransform *QLottieLayer::transform() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlottielayer.html#transform

    Returns
    -------

    Optional[QLottieBasicTransform]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QLottieBasicTransform *QLottieLayer::transform() const
    address = self.uglySide.call('ritual_ZNK12QLottieLayer9transformEv')
    from . import QLottieBasicTransform
    return QLottieBasicTransform._cuteAt(address)

  def hasLinkedLayer(self) -> bool:
    """
    Calls Qt's 'bool QLottieLayer::hasLinkedLayer() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlottielayer.html#hasLinkedLayer
    """
    #  bool QLottieLayer::hasLinkedLayer() const
    return self.uglySide.call('ritual_ZNK12QLottieLayer14hasLinkedLayerEv')

  def linkedLayerId(self) -> int:
    """
    Calls Qt's 'int QLottieLayer::linkedLayerId() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlottielayer.html#linkedLayerId
    """
    #  int QLottieLayer::linkedLayerId() const
    return self.uglySide.call('ritual_ZNK12QLottieLayer13linkedLayerIdEv')

  def layerSize(self) -> QSize:
    """
    Calls Qt's 'QSize QLottieLayer::layerSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlottielayer.html#layerSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QLottieLayer::layerSize() const
    ritual = 'ritual_ZNK12QLottieLayer9layerSizeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK12QLottieLayer9layerSizeEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def startFrame(self) -> int:
    """
    Calls Qt's 'int QLottieLayer::startFrame() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlottielayer.html#startFrame
    """
    #  int QLottieLayer::startFrame() const
    return self.uglySide.call('ritual_ZNK12QLottieLayer10startFrameEv')

  def endFrame(self) -> int:
    """
    Calls Qt's 'int QLottieLayer::endFrame() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlottielayer.html#endFrame
    """
    #  int QLottieLayer::endFrame() const
    return self.uglySide.call('ritual_ZNK12QLottieLayer8endFrameEv')

  def frameOffset(self) -> float:
    """
    Calls Qt's 'qreal QLottieLayer::frameOffset() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlottielayer.html#frameOffset
    """
    #  qreal QLottieLayer::frameOffset() const
    return self.uglySide.call('ritual_ZNK12QLottieLayer11frameOffsetEv')

  def timeStretch(self) -> float:
    """
    Calls Qt's 'qreal QLottieLayer::timeStretch() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlottielayer.html#timeStretch
    """
    #  qreal QLottieLayer::timeStretch() const
    return self.uglySide.call('ritual_ZNK12QLottieLayer11timeStretchEv')

  def linkedLayer(self) -> Optional[QLottieLayer]:
    """
    Calls Qt's 'QLottieLayer *QLottieLayer::linkedLayer() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlottielayer.html#linkedLayer

    Returns
    -------

    Optional[QLottieLayer]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QLottieLayer *QLottieLayer::linkedLayer() const
    ritual = 'ritual_ZNK12QLottieLayer11linkedLayerEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK12QLottieLayer11linkedLayerEv'
    address = self.uglySide.call(ritual)
    return QLottieLayer._cuteAt(address)

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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QLottieLayer::QLottieLayer()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qlottielayer.html#QLottieLayer
    """
    #  QLottieLayer::QLottieLayer()
    self._noteCreation(QLottieLayer, lambda: Rituals.call(
        'ritual_ZN12QLottieLayerC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QLottieLayer) -> None:
    """
    Notes what was given, for Qt's 'QLottieLayer::QLottieLayer(const
    QLottieLayer &other)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qlottielayer.html#QLottieLayer

    Parameters
    ----------

    other : QLottieLayer
      Passed on as a value: Qt reads the C++ QLottieLayer, which stays
      Python's own.
    """
    #  QLottieLayer::QLottieLayer(const QLottieLayer &other)
    self._noteCreation(QLottieLayer, lambda: Rituals.call(
        'ritual_ZN12QLottieLayerC1ERKS_', self._valueOf(other),
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
  def parse(self, definition: QJsonObject) -> int:
    """
    Calls Qt's 'int QLottieLayer::parse(const QJsonObject &definition)'.

    Qt's own words: https://doc.qt.io/qt-6/qlottielayer.html#parse

    Parameters
    ----------

    definition : QJsonObject
      Passed on as a value: Qt reads the C++ QJsonObject, which stays
      Python's own.
    """
    #  int QLottieLayer::parse(const QJsonObject &definition)
    ritual = 'ritual_ZN12QLottieLayer5parseERK11QJsonObject'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QLottieLayer5parseERK11QJsonObject'
    return self.uglySide.call(ritual, self._valueOf(definition))

  @overload(int)
  def updateProperties(self, frame: int) -> None:
    """
    Calls Qt's 'void QLottieLayer::updateProperties(int frame)'.

    Qt's own words: https://doc.qt.io/qt-6/qlottielayer.html#updateProperties

    Parameters
    ----------

    frame : int
      Passed on as it is.
    """
    #  void QLottieLayer::updateProperties(int frame)
    ritual = 'ritual_ZN12QLottieLayer16updatePropertiesEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QLottieLayer16updatePropertiesEi'
    self.uglySide.call(ritual, frame)

  @overload(str)
  def findChild(self, childName: str) -> Optional[QLottieBase]:
    """
    Calls Qt's 'QLottieBase *QLottieLayer::findChild(const QString
    &childName)'.

    Qt's own words: https://doc.qt.io/qt-6/qlottielayer.html#findChild

    Parameters
    ----------

    childName : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    Optional[QLottieBase]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QLottieBase *QLottieLayer::findChild(const QString &childName)
    ritual = 'ritual_ZN12QLottieLayer9findChildERK7QString'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QLottieLayer9findChildERK7QString'
    address = self.uglySide.call(ritual, childName)
    return QLottieBase._cuteAt(address)

  def resolveLinkedLayer(self) -> Optional[QLottieLayer]:
    """
    Calls Qt's 'QLottieLayer *QLottieLayer::resolveLinkedLayer()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlottielayer.html#resolveLinkedLayer

    Returns
    -------

    Optional[QLottieLayer]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QLottieLayer *QLottieLayer::resolveLinkedLayer()
    ritual = 'ritual_ZN12QLottieLayer18resolveLinkedLayerEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QLottieLayer18resolveLinkedLayerEv'
    address = self.uglySide.call(ritual)
    return QLottieLayer._cuteAt(address)

  @overload(QJsonArray)
  @overload(QJsonArray, QLottieBase)
  @overload(QJsonArray, NoneType)
  def parseEffects(
      self,
      definition: QJsonArray,
      effectRoot: Optional[QLottieBase] = None,
  ) -> None:
    """
    Calls Qt's 'void QLottieLayer::parseEffects(const QJsonArray &definition,
    QLottieBase *effectRoot)'.

    Qt's own words: https://doc.qt.io/qt-6/qlottielayer.html#parseEffects

    Parameters
    ----------

    definition : QJsonArray
      Passed on as a value: Qt reads the C++ QJsonArray, which stays Python's
      own.

    effectRoot : Optional[QLottieBase]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  void QLottieLayer::parseEffects(const QJsonArray &definition,
    #      QLottieBase *effectRoot)
    self.uglySide.call(
        'ritual_ZN12QLottieLayer12parseEffectsERK10QJsonArrayP11QLottieBase',
        self._valueOf(definition), self._addressOf(effectRoot),
    )

  @staticmethod
  def applyLayerTransform(*__, **_) -> Never:
    """
    Qt's 'void QLottieLayer::applyLayerTransform(QLottieRenderer &renderer)
    const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QLottieLayer.applyLayerTransform' has no cute function yet. Qt's "
        "'void QLottieLayer::applyLayerTransform(QLottieRenderer &renderer) "
        "const': takes a type Python has no way to hand over yet.")

  @staticmethod
  def renderEffects(*__, **_) -> Never:
    """
    Qt's 'void QLottieLayer::renderEffects(QLottieRenderer &renderer) const':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QLottieLayer.renderEffects' has no cute function yet. Qt's 'void "
        "QLottieLayer::renderEffects(QLottieRenderer &renderer) const': "
        "takes a type Python has no way to hand over yet.")
