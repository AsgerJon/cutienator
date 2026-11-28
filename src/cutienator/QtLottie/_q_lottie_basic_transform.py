"""
QLottieBasicTransform binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLottie/6.12.0/QtLottie/private/qlottiebasictransform_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QLottieBasicTransform to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QLottieBase, QLottieShape

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QLottieSpatialProperty
  from ..QtCore import QJsonObject, QPointF
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QJsonObject = WAIT['QJsonObject']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QLottieBasicTransform(QLottieShape):
  """
  The cute side of Qt's QLottieBasicTransform: a plain Python object standing
  in front of one C++ QLottieBasicTransform.

  It is built on the cute 'QLottieShape', as Qt's QLottieBasicTransform is
  built on Qt's QLottieShape, and has everything that class has.

  C++ hands a QLottieBasicTransform around as a copy, so every C++
  QLottieBasicTransform behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QLottieBasicTransform that has a ritual and that
  Python can call so far, 13 names in all: 'clone', 'parse',
  'updateProperties', 'anchorPoint', 'position', 'scale', 'rotation',
  'opacity', 'splitPosition', 'anchorPointProperty', 'positionProperty',
  'hasLinkedLayerTransform', 'setHasLinkedLayerTransform'. It can be made
  from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QLottieBasicTransform::render(QLottieRenderer &renderer)
    const': takes a type Python has no way to hand over yet.
  - Qt's 'QLottieProperty<qreal> QLottieBasicTransform::xPosProperty()
    const': gives a type Python has no way to take yet.
  - Qt's 'QLottieProperty<qreal> QLottieBasicTransform::yPosProperty()
    const': gives a type Python has no way to take yet.
  - Qt's 'QLottieProperty2D<QPointF> QLottieBasicTransform::scaleProperty()
    const': gives a type Python has no way to take yet.
  - Qt's 'QLottieProperty<qreal> QLottieBasicTransform::rotationProperty()
    const': gives a type Python has no way to take yet.
  - Qt's 'QLottieProperty<qreal> QLottieBasicTransform::opacityProperty()
    const': gives a type Python has no way to take yet.
  - Qt's 'QLottieBasicTransform::~QLottieBasicTransform()': the destructor:
    Python removes its C++ QLottieBasicTransform by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QLottieBasicTransform is created at the first use, not by
    'QLottieBasicTransform(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QLottieBasicTransform back gives a copy the ritual
    made for Python, in a new cute QLottieBasicTransform.
  - Each name of Qt's QLottieBasicTransform that has no cute function yet,
    'opacityProperty', 'rotationProperty', 'scaleProperty', 'xPosProperty',
    'yPosProperty', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QLottieBasicTransform'

  #  A C++ QLottieBasicTransform Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QLottieBasicTransform'

  #  The functions Qt calls itself that QLottieBasicTransform is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'position': (
          ('_ZNK21QLottieBasicTransform8positionEv',
           ('address', 'value', 'QtCore:QPointF'),
           ()),
      ),
  }

  #  Qt's '~QLottieBasicTransform()'. Naming it makes this a value class:
  #  Python owns every C++ QLottieBasicTransform behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN21QLottieBasicTransformD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def clone(self) -> Optional[QLottieBase]:
    """
    Calls Qt's 'QLottieBase *QLottieBasicTransform::clone() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlottiebasictransform.html#clone

    Returns
    -------

    Optional[QLottieBase]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QLottieBase *QLottieBasicTransform::clone() const
    ritual = 'ritual_ZNK21QLottieBasicTransform5cloneEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK21QLottieBasicTransform5cloneEv'
    address = self.uglySide.call(ritual)
    return QLottieBase._cuteAt(address)

  def anchorPoint(self) -> QPointF:
    """
    Calls Qt's 'QPointF QLottieBasicTransform::anchorPoint() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlottiebasictransform.html#anchorPoint

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QLottieBasicTransform::anchorPoint() const
    address = self.uglySide.call(
        'ritual_ZNK21QLottieBasicTransform11anchorPointEv',
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def position(self) -> QPointF:
    """
    Calls Qt's 'QPointF QLottieBasicTransform::position() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlottiebasictransform.html#position

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QLottieBasicTransform::position() const
    ritual = 'ritual_ZNK21QLottieBasicTransform8positionEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK21QLottieBasicTransform8positionEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def scale(self) -> QPointF:
    """
    Calls Qt's 'QPointF QLottieBasicTransform::scale() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlottiebasictransform.html#scale

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QLottieBasicTransform::scale() const
    address = self.uglySide.call('ritual_ZNK21QLottieBasicTransform5scaleEv')
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def rotation(self) -> float:
    """
    Calls Qt's 'qreal QLottieBasicTransform::rotation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlottiebasictransform.html#rotation
    """
    #  qreal QLottieBasicTransform::rotation() const
    return self.uglySide.call('ritual_ZNK21QLottieBasicTransform8rotationEv')

  def opacity(self) -> float:
    """
    Calls Qt's 'qreal QLottieBasicTransform::opacity() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlottiebasictransform.html#opacity
    """
    #  qreal QLottieBasicTransform::opacity() const
    return self.uglySide.call('ritual_ZNK21QLottieBasicTransform7opacityEv')

  def splitPosition(self) -> bool:
    """
    Calls Qt's 'bool QLottieBasicTransform::splitPosition() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlottiebasictransform.html#splitPosition
    """
    #  bool QLottieBasicTransform::splitPosition() const
    return self.uglySide.call(
        'ritual_ZNK21QLottieBasicTransform13splitPositionEv',
    )

  def anchorPointProperty(self) -> QLottieSpatialProperty:
    """
    Calls Qt's 'QLottieSpatialProperty
    QLottieBasicTransform::anchorPointProperty() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlottiebasictransform.html#anchorPointProperty

    Returns
    -------

    QLottieSpatialProperty
      A new cute QLottieSpatialProperty around the copy Qt gave back. Python
      owns it.
    """
    #  QLottieSpatialProperty QLottieBasicTransform::anchorPointProperty()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK21QLottieBasicTransform19anchorPointPropertyEv',
    )
    from . import QLottieSpatialProperty
    return QLottieSpatialProperty._cuteOwning(address)

  def positionProperty(self) -> QLottieSpatialProperty:
    """
    Calls Qt's 'QLottieSpatialProperty
    QLottieBasicTransform::positionProperty() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlottiebasictransform.html#positionProperty

    Returns
    -------

    QLottieSpatialProperty
      A new cute QLottieSpatialProperty around the copy Qt gave back. Python
      owns it.
    """
    #  QLottieSpatialProperty QLottieBasicTransform::positionProperty() const
    address = self.uglySide.call(
        'ritual_ZNK21QLottieBasicTransform16positionPropertyEv',
    )
    from . import QLottieSpatialProperty
    return QLottieSpatialProperty._cuteOwning(address)

  def hasLinkedLayerTransform(self) -> bool:
    """
    Calls Qt's 'bool QLottieBasicTransform::hasLinkedLayerTransform() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlottiebasictransform.html#hasLinkedLayerTransform
    """
    #  bool QLottieBasicTransform::hasLinkedLayerTransform() const
    return self.uglySide.call(
        'ritual_ZNK21QLottieBasicTransform23hasLinkedLayerTransformEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setHasLinkedLayerTransform(
      self,
      hasLinkedLayerTransform: bool,
  ) -> None:
    """
    Calls Qt's 'void QLottieBasicTransform::setHasLinkedLayerTransform(bool
    hasLinkedLayerTransform)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlottiebasictransform.html

    Parameters
    ----------

    hasLinkedLayerTransform : bool
      Passed on as it is.
    """
    #  void QLottieBasicTransform::setHasLinkedLayerTransform(bool
    #      hasLinkedLayerTransform)
    self.uglySide.call(
        'ritual_ZN21QLottieBasicTransform26setHasLinkedLayerTransformEb',
        hasLinkedLayerTransform,
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

  @overload(THIS)
  def __init__(self, other: QLottieBasicTransform) -> None:
    """
    Notes what was given, for Qt's
    'QLottieBasicTransform::QLottieBasicTransform(const QLottieBasicTransform
    &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qlottiebasictransform.html#QLottieBasicTransform

    Parameters
    ----------

    other : QLottieBasicTransform
      Passed on as a value: Qt reads the C++ QLottieBasicTransform, which
      stays Python's own.
    """
    #  QLottieBasicTransform::QLottieBasicTransform(const
    #      QLottieBasicTransform &other)
    self._noteCreation(QLottieBasicTransform, lambda: Rituals.call(
        'ritual_ZN21QLottieBasicTransformC1ERKS_', self._valueOf(other),
    ))

  @overload()
  @overload(QLottieBase)
  @overload(NoneType)
  def __init__(self, parent: Optional[QLottieBase] = None) -> None:
    """
    Notes what was given, for Qt's
    'QLottieBasicTransform::QLottieBasicTransform(QLottieBase *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qlottiebasictransform.html#QLottieBasicTransform

    Parameters
    ----------

    parent : Optional[QLottieBase]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QLottieBasicTransform::QLottieBasicTransform(QLottieBase *parent)
    self._noteCreation(QLottieBasicTransform, lambda: Rituals.call(
        'ritual_ZN21QLottieBasicTransformC1EP11QLottieBase',
        self._addressOf(parent),
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
    Calls Qt's 'int QLottieBasicTransform::parse(const QJsonObject
    &definition)'.

    Qt's own words: https://doc.qt.io/qt-6/qlottiebasictransform.html#parse

    Parameters
    ----------

    definition : QJsonObject
      Passed on as a value: Qt reads the C++ QJsonObject, which stays
      Python's own.
    """
    #  int QLottieBasicTransform::parse(const QJsonObject &definition)
    ritual = 'ritual_ZN21QLottieBasicTransform5parseERK11QJsonObject'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QLottieBasicTransform5parseERK11QJsonObject'
    return self.uglySide.call(ritual, self._valueOf(definition))

  @overload(int)
  def updateProperties(self, frame: int) -> None:
    """
    Calls Qt's 'void QLottieBasicTransform::updateProperties(int frame)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlottiebasictransform.html#updateProperties

    Parameters
    ----------

    frame : int
      Passed on as it is.
    """
    #  void QLottieBasicTransform::updateProperties(int frame)
    ritual = 'ritual_ZN21QLottieBasicTransform16updatePropertiesEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QLottieBasicTransform16updatePropertiesEi'
    self.uglySide.call(ritual, frame)

  @staticmethod
  def opacityProperty(*__, **_) -> Never:
    """
    Qt's 'QLottieProperty<qreal> QLottieBasicTransform::opacityProperty()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QLottieBasicTransform.opacityProperty' has no cute function yet. "
        "Qt's 'QLottieProperty<qreal> "
        "QLottieBasicTransform::opacityProperty() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def rotationProperty(*__, **_) -> Never:
    """
    Qt's 'QLottieProperty<qreal> QLottieBasicTransform::rotationProperty()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QLottieBasicTransform.rotationProperty' has no cute function yet. "
        "Qt's 'QLottieProperty<qreal> "
        "QLottieBasicTransform::rotationProperty() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def scaleProperty(*__, **_) -> Never:
    """
    Qt's 'QLottieProperty2D<QPointF> QLottieBasicTransform::scaleProperty()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QLottieBasicTransform.scaleProperty' has no cute function yet. "
        "Qt's 'QLottieProperty2D<QPointF> "
        "QLottieBasicTransform::scaleProperty() const': gives a type Python "
        "has no way to take yet.")

  @staticmethod
  def xPosProperty(*__, **_) -> Never:
    """
    Qt's 'QLottieProperty<qreal> QLottieBasicTransform::xPosProperty()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QLottieBasicTransform.xPosProperty' has no cute function yet. "
        "Qt's 'QLottieProperty<qreal> QLottieBasicTransform::xPosProperty() "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def yPosProperty(*__, **_) -> Never:
    """
    Qt's 'QLottieProperty<qreal> QLottieBasicTransform::yPosProperty()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QLottieBasicTransform.yPosProperty' has no cute function yet. "
        "Qt's 'QLottieProperty<qreal> QLottieBasicTransform::yPosProperty() "
        "const': gives a type Python has no way to take yet.")
