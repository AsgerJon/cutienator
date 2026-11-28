"""
QQuick3DRandomInstancing binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DHelpers/6.12.0/QtQuick3DHelpers/private/randominstancing_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQuick3DRandomInstancing to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QVector3D
  from . import QQuick3DInstanceRange
  from ..QtQuick3D import QQuick3DObject
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuick3DInstanceRange = WAIT['QQuick3DInstanceRange']
  QQuick3DObject = WAIT['QQuick3DObject']
  QVector3D = WAIT['QVector3D']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuick3DRandomInstancing(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuick3DRandomInstancing: a plain Python object
  standing in front of one C++ QQuick3DRandomInstancing.

  What exists
  -----------

  Every function of Qt's QQuick3DRandomInstancing that has a ritual and that
  Python can call so far, 31 names in all: 'metaObject', 'tr',
  'instanceCount', 'randomSeed', 'position', 'scale', 'rotation', 'color',
  'customData', 'colorModel', 'gridSpacing', 'setGridSpacing',
  'setInstanceCount', 'setRandomSeed', 'setPosition', 'setScale',
  'setRotation', 'setColor', 'setCustomData', 'setColorModel',
  'instanceCountChanged', 'randomSeedChanged', 'positionChanged',
  'scaleChanged', 'rotationChanged', 'colorChanged', 'customDataChanged',
  'colorModelChanged', 'gridSpacingChanged', 'handleChange',
  'generateInstanceTable'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuick3DRandomInstancing::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QQuick3DRandomInstancing::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuick3DRandomInstancing::~QQuick3DRandomInstancing()': the
    destructor: Python never removes a C++ QQuick3DRandomInstancing.
  - Qt's 'QByteArray QQuick3DRandomInstancing::getInstanceBuffer(int
    *instanceCount)': takes a number to change where it is.

  What has no ritual
  ------------------

  2 of the 38 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuick3DRandomInstancing is created at the first use, not by
    'QQuick3DRandomInstancing(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuick3DRandomInstancing.
  - Qt tells when it has removed the C++ QQuick3DRandomInstancing. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QQuick3DRandomInstancing, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class ColorModel(CuteNum, scoped=True):
    """
    The enum 'QQuick3DRandomInstancing::ColorModel' of Qt, with the 3 names
    Qt gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    RGB = Kee[int](0)
    HSV = Kee[int](1)
    HSL = Kee[int](2)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  @overload(NoneType)
  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  @overload(str, str, int)
  @overload(str, NoneType, int)
  @overload(NoneType, str, int)
  @overload(NoneType, NoneType, int)
  def tr(s: Optional[str], c: Optional[str] = None, n: int = -1) -> str:
    """
    Calls Qt's 'QString QQuick3DRandomInstancing::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3drandominstancing.html#tr

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    c : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuick3DRandomInstancing::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN24QQuick3DRandomInstancing2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuick3DRandomInstancing'

  #  A C++ QQuick3DRandomInstancing Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuick3DRandomInstancing'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuick3DRandomInstancing::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drandominstancing.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuick3DRandomInstancing::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK24QQuick3DRandomInstancing10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def instanceCount(self) -> int:
    """
    Calls Qt's 'int QQuick3DRandomInstancing::instanceCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drandominstancing.html#instanceCount
    """
    #  int QQuick3DRandomInstancing::instanceCount() const
    return self.uglySide.call(
        'ritual_ZNK24QQuick3DRandomInstancing13instanceCountEv',
    )

  def randomSeed(self) -> int:
    """
    Calls Qt's 'int QQuick3DRandomInstancing::randomSeed() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drandominstancing.html#randomSeed
    """
    #  int QQuick3DRandomInstancing::randomSeed() const
    return self.uglySide.call(
        'ritual_ZNK24QQuick3DRandomInstancing10randomSeedEv',
    )

  def position(self) -> Optional[QQuick3DInstanceRange]:
    """
    Calls Qt's 'QQuick3DInstanceRange *QQuick3DRandomInstancing::position()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drandominstancing.html#position

    Returns
    -------

    Optional[QQuick3DInstanceRange]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DInstanceRange *QQuick3DRandomInstancing::position() const
    address = self.uglySide.call(
        'ritual_ZNK24QQuick3DRandomInstancing8positionEv',
    )
    from . import QQuick3DInstanceRange
    return QQuick3DInstanceRange._cuteAt(address)

  def scale(self) -> Optional[QQuick3DInstanceRange]:
    """
    Calls Qt's 'QQuick3DInstanceRange *QQuick3DRandomInstancing::scale()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drandominstancing.html#scale

    Returns
    -------

    Optional[QQuick3DInstanceRange]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DInstanceRange *QQuick3DRandomInstancing::scale() const
    address = self.uglySide.call(
        'ritual_ZNK24QQuick3DRandomInstancing5scaleEv',
    )
    from . import QQuick3DInstanceRange
    return QQuick3DInstanceRange._cuteAt(address)

  def rotation(self) -> Optional[QQuick3DInstanceRange]:
    """
    Calls Qt's 'QQuick3DInstanceRange *QQuick3DRandomInstancing::rotation()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drandominstancing.html#rotation

    Returns
    -------

    Optional[QQuick3DInstanceRange]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DInstanceRange *QQuick3DRandomInstancing::rotation() const
    address = self.uglySide.call(
        'ritual_ZNK24QQuick3DRandomInstancing8rotationEv',
    )
    from . import QQuick3DInstanceRange
    return QQuick3DInstanceRange._cuteAt(address)

  def color(self) -> Optional[QQuick3DInstanceRange]:
    """
    Calls Qt's 'QQuick3DInstanceRange *QQuick3DRandomInstancing::color()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drandominstancing.html#color

    Returns
    -------

    Optional[QQuick3DInstanceRange]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DInstanceRange *QQuick3DRandomInstancing::color() const
    address = self.uglySide.call(
        'ritual_ZNK24QQuick3DRandomInstancing5colorEv',
    )
    from . import QQuick3DInstanceRange
    return QQuick3DInstanceRange._cuteAt(address)

  def customData(self) -> Optional[QQuick3DInstanceRange]:
    """
    Calls Qt's 'QQuick3DInstanceRange *QQuick3DRandomInstancing::customData()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drandominstancing.html#customData

    Returns
    -------

    Optional[QQuick3DInstanceRange]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DInstanceRange *QQuick3DRandomInstancing::customData() const
    address = self.uglySide.call(
        'ritual_ZNK24QQuick3DRandomInstancing10customDataEv',
    )
    from . import QQuick3DInstanceRange
    return QQuick3DInstanceRange._cuteAt(address)

  def colorModel(self) -> ColorModel:
    """
    Calls Qt's 'ColorModel QQuick3DRandomInstancing::colorModel() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drandominstancing.html#colorModel

    Returns
    -------

    ColorModel
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'ColorModel(number)'
      gives.
    """
    #  ColorModel QQuick3DRandomInstancing::colorModel() const
    return QQuick3DRandomInstancing.ColorModel(self.uglySide.call(
        'ritual_ZNK24QQuick3DRandomInstancing10colorModelEv',
    ))

  def gridSpacing(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D QQuick3DRandomInstancing::gridSpacing() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drandominstancing.html#gridSpacing

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QQuick3DRandomInstancing::gridSpacing() const
    address = self.uglySide.call(
        'ritual_ZNK24QQuick3DRandomInstancing11gridSpacingEv',
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QVector3D)
  def setGridSpacing(self, newGridSpacing: QVector3D) -> None:
    """
    Calls Qt's 'void QQuick3DRandomInstancing::setGridSpacing(const QVector3D
    &newGridSpacing)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drandominstancing.html#setGridSpacing

    Parameters
    ----------

    newGridSpacing : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void QQuick3DRandomInstancing::setGridSpacing(const QVector3D
    #      &newGridSpacing)
    self.uglySide.call(
        'ritual_ZN24QQuick3DRandomInstancing14setGridSpacingERK9QVector3D',
        self._valueOf(newGridSpacing),
    )

  @overload(int)
  def setInstanceCount(self, instanceCount: int) -> None:
    """
    Calls Qt's 'void QQuick3DRandomInstancing::setInstanceCount(int
    instanceCount)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drandominstancing.html#setInstanceCount

    Parameters
    ----------

    instanceCount : int
      Passed on as it is.
    """
    #  void QQuick3DRandomInstancing::setInstanceCount(int instanceCount)
    self.uglySide.call(
        'ritual_ZN24QQuick3DRandomInstancing16setInstanceCountEi',
        instanceCount,
    )

  @overload(int)
  def setRandomSeed(self, randomSeed: int) -> None:
    """
    Calls Qt's 'void QQuick3DRandomInstancing::setRandomSeed(int
    randomSeed)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drandominstancing.html#setRandomSeed

    Parameters
    ----------

    randomSeed : int
      Passed on as it is.
    """
    #  void QQuick3DRandomInstancing::setRandomSeed(int randomSeed)
    self.uglySide.call(
        'ritual_ZN24QQuick3DRandomInstancing13setRandomSeedEi', randomSeed,
    )

  @overload(QQuick3DInstanceRange)
  @overload(NoneType)
  def setPosition(self, position: Optional[QQuick3DInstanceRange]) -> None:
    """
    Calls Qt's 'void
    QQuick3DRandomInstancing::setPosition(QQuick3DInstanceRange *position)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drandominstancing.html#setPosition

    Parameters
    ----------

    position : Optional[QQuick3DInstanceRange]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DRandomInstancing::setPosition(QQuick3DInstanceRange
    #      *position)
    self.uglySide.call(
        'ritual_ZN24QQuick3DRandomInstancing11setPositionEP21QQuick3DInstan'
        'ceRange',
        self._addressOf(position),
    )

  @overload(QQuick3DInstanceRange)
  @overload(NoneType)
  def setScale(self, scale: Optional[QQuick3DInstanceRange]) -> None:
    """
    Calls Qt's 'void QQuick3DRandomInstancing::setScale(QQuick3DInstanceRange
    *scale)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drandominstancing.html#setScale

    Parameters
    ----------

    scale : Optional[QQuick3DInstanceRange]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DRandomInstancing::setScale(QQuick3DInstanceRange *scale)
    self.uglySide.call(
        'ritual_ZN24QQuick3DRandomInstancing8setScaleEP21QQuick3DInstanceRa'
        'nge',
        self._addressOf(scale),
    )

  @overload(QQuick3DInstanceRange)
  @overload(NoneType)
  def setRotation(self, rotation: Optional[QQuick3DInstanceRange]) -> None:
    """
    Calls Qt's 'void
    QQuick3DRandomInstancing::setRotation(QQuick3DInstanceRange *rotation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drandominstancing.html#setRotation

    Parameters
    ----------

    rotation : Optional[QQuick3DInstanceRange]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DRandomInstancing::setRotation(QQuick3DInstanceRange
    #      *rotation)
    self.uglySide.call(
        'ritual_ZN24QQuick3DRandomInstancing11setRotationEP21QQuick3DInstan'
        'ceRange',
        self._addressOf(rotation),
    )

  @overload(QQuick3DInstanceRange)
  @overload(NoneType)
  def setColor(self, color: Optional[QQuick3DInstanceRange]) -> None:
    """
    Calls Qt's 'void QQuick3DRandomInstancing::setColor(QQuick3DInstanceRange
    *color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drandominstancing.html#setColor

    Parameters
    ----------

    color : Optional[QQuick3DInstanceRange]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DRandomInstancing::setColor(QQuick3DInstanceRange *color)
    self.uglySide.call(
        'ritual_ZN24QQuick3DRandomInstancing8setColorEP21QQuick3DInstanceRa'
        'nge',
        self._addressOf(color),
    )

  @overload(QQuick3DInstanceRange)
  @overload(NoneType)
  def setCustomData(
      self,
      customData: Optional[QQuick3DInstanceRange],
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DRandomInstancing::setCustomData(QQuick3DInstanceRange
    *customData)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drandominstancing.html#setCustomData

    Parameters
    ----------

    customData : Optional[QQuick3DInstanceRange]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DRandomInstancing::setCustomData(QQuick3DInstanceRange
    #      *customData)
    self.uglySide.call(
        'ritual_ZN24QQuick3DRandomInstancing13setCustomDataEP21QQuick3DInst'
        'anceRange',
        self._addressOf(customData),
    )

  @overload(ColorModel)
  def setColorModel(self, colorModel: ColorModel) -> None:
    """
    Calls Qt's 'void QQuick3DRandomInstancing::setColorModel(ColorModel
    colorModel)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drandominstancing.html#setColorModel

    Parameters
    ----------

    colorModel : ColorModel
      Passed on as its number.
    """
    #  void QQuick3DRandomInstancing::setColorModel(ColorModel colorModel)
    self.uglySide.call(
        'ritual_ZN24QQuick3DRandomInstancing13setColorModelENS_10ColorModel'
        'E',
        colorModel.value,
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
  @overload(QQuick3DObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QQuick3DObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QQuick3DRandomInstancing::QQuick3DRandomInstancing(QQuick3DObject
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drandominstancing.html

    Parameters
    ----------

    parent : Optional[QQuick3DObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuick3DRandomInstancing::QQuick3DRandomInstancing(QQuick3DObject
    #      *parent)
    self._noteCreation(QQuick3DRandomInstancing, lambda: Rituals.call(
        'ritual_ZN24QQuick3DRandomInstancingC1EP14QQuick3DObject',
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

  def instanceCountChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DRandomInstancing::instanceCountChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drandominstancing.html#instanceCountChanged
    """
    #  void QQuick3DRandomInstancing::instanceCountChanged()
    self.uglySide.call(
        'ritual_ZN24QQuick3DRandomInstancing20instanceCountChangedEv',
    )

  def randomSeedChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DRandomInstancing::randomSeedChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drandominstancing.html#randomSeedChanged
    """
    #  void QQuick3DRandomInstancing::randomSeedChanged()
    self.uglySide.call(
        'ritual_ZN24QQuick3DRandomInstancing17randomSeedChangedEv',
    )

  def positionChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DRandomInstancing::positionChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drandominstancing.html#positionChanged
    """
    #  void QQuick3DRandomInstancing::positionChanged()
    self.uglySide.call(
        'ritual_ZN24QQuick3DRandomInstancing15positionChangedEv',
    )

  def scaleChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DRandomInstancing::scaleChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drandominstancing.html#scaleChanged
    """
    #  void QQuick3DRandomInstancing::scaleChanged()
    self.uglySide.call('ritual_ZN24QQuick3DRandomInstancing12scaleChangedEv')

  def rotationChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DRandomInstancing::rotationChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drandominstancing.html#rotationChanged
    """
    #  void QQuick3DRandomInstancing::rotationChanged()
    self.uglySide.call(
        'ritual_ZN24QQuick3DRandomInstancing15rotationChangedEv',
    )

  def colorChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DRandomInstancing::colorChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drandominstancing.html#colorChanged
    """
    #  void QQuick3DRandomInstancing::colorChanged()
    self.uglySide.call('ritual_ZN24QQuick3DRandomInstancing12colorChangedEv')

  def customDataChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DRandomInstancing::customDataChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drandominstancing.html#customDataChanged
    """
    #  void QQuick3DRandomInstancing::customDataChanged()
    self.uglySide.call(
        'ritual_ZN24QQuick3DRandomInstancing17customDataChangedEv',
    )

  def colorModelChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DRandomInstancing::colorModelChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drandominstancing.html#colorModelChanged
    """
    #  void QQuick3DRandomInstancing::colorModelChanged()
    self.uglySide.call(
        'ritual_ZN24QQuick3DRandomInstancing17colorModelChangedEv',
    )

  def gridSpacingChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DRandomInstancing::gridSpacingChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drandominstancing.html#gridSpacingChanged
    """
    #  void QQuick3DRandomInstancing::gridSpacingChanged()
    self.uglySide.call(
        'ritual_ZN24QQuick3DRandomInstancing18gridSpacingChangedEv',
    )

  def handleChange(self) -> None:
    """
    Calls Qt's 'void QQuick3DRandomInstancing::handleChange()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drandominstancing.html#handleChange
    """
    #  void QQuick3DRandomInstancing::handleChange()
    self.uglySide.call('ritual_ZN24QQuick3DRandomInstancing12handleChangeEv')

  def generateInstanceTable(self) -> None:
    """
    Calls Qt's 'void QQuick3DRandomInstancing::generateInstanceTable()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drandominstancing.html
    """
    #  void QQuick3DRandomInstancing::generateInstanceTable()
    self.uglySide.call(
        'ritual_ZN24QQuick3DRandomInstancing21generateInstanceTableEv',
    )
