"""
QCanvasImagePattern binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCanvasPainter/qcanvasimagepattern.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QDebug, QPointF, QSizeF
  from ..QtGui import QColor
  from . import QCanvasImage, QCanvasImagePatternPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QCanvasImage = WAIT['QCanvasImage']
  QCanvasImagePatternPrivate = WAIT['QCanvasImagePatternPrivate']
  QColor = WAIT['QColor']
  QDebug = WAIT['QDebug']
  QPointF = WAIT['QPointF']
  QSizeF = WAIT['QSizeF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QCanvasImagePattern(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QCanvasImagePattern: a plain Python object standing
  in front of one C++ QCanvasImagePattern.

  C++ hands a QCanvasImagePattern around as a copy, so every C++
  QCanvasImagePattern behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QCanvasImagePattern that has a ritual and that
  Python can call so far, 14 names in all: 'startPosition',
  'setStartPosition', 'imageSize', 'setImageSize', 'image', 'setImage',
  'rotation', 'setRotation', 'tintColor', 'setTintColor', 'serialNumber',
  '__eq__', '__ne__', '__rlshift__'. It can be made from Python, in 6 ways;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QCanvasImagePattern &QCanvasImagePattern::operator=(const
    QCanvasImagePattern &a0)': assignment: Python binds a name and has no
    operator for it.
  - Qt's 'QCanvasImagePattern::QCanvasImagePattern(QCanvasImagePattern
    &&a0)': takes a type Python has no way to hand over yet.
  - Qt's 'QCanvasImagePattern
    &QCanvasImagePattern::operator=(QCanvasImagePattern &&other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'QCanvasImagePattern::~QCanvasImagePattern()': the destructor:
    Python removes its C++ QCanvasImagePattern by it, and has no other use
    for it.
  - Qt's 'QCanvasBrush QCanvasImagePattern::operator QCanvasBrush() const':
    an operator Python has no name for.
  - Qt's 'QVariant QCanvasImagePattern::operator QVariant() const': an
    operator Python has no name for.
  - Qt's 'void QCanvasImagePattern::swap(QCanvasImagePattern &other)': takes
    a type Python has no way to hand over yet.
  - Qt's 'QDataStream &operator<<(QDataStream &a0, const QCanvasImagePattern
    &a1)': takes a type Python has no way to hand over yet.
  - Qt's 'QDataStream &operator>>(QDataStream &a0, QCanvasImagePattern &a1)':
    an operator between other classes, written inside this one.

  What has no ritual
  ------------------

  1 of the 32 functions Qt declares: 1 leans on 'QCanvasImagePatternPrivate.

  What to expect
  --------------

  - The C++ QCanvasImagePattern is created at the first use, not by
    'QCanvasImagePattern(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QCanvasImagePattern back gives a copy the ritual made
    for Python, in a new cute QCanvasImagePattern.
  - Each name of Qt's QCanvasImagePattern that has no cute function yet,
    'detach', 'swap', holds a function that raises 'NotImplementedError', and
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
  __qt_class__ = 'QCanvasImagePattern'

  #  Qt's '~QCanvasImagePattern()'. Naming it makes this a value class:
  #  Python owns every C++ QCanvasImagePattern behind a cute one, and removes
  #  it by this ritual.
  __delete_ritual__ = 'ritual_ZN19QCanvasImagePatternD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def startPosition(self) -> QPointF:
    """
    Calls Qt's 'QPointF QCanvasImagePattern::startPosition() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvasimagepattern.html#startPosition

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QCanvasImagePattern::startPosition() const
    address = self.uglySide.call(
        'ritual_ZNK19QCanvasImagePattern13startPositionEv',
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def imageSize(self) -> QSizeF:
    """
    Calls Qt's 'QSizeF QCanvasImagePattern::imageSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvasimagepattern.html#imageSize

    Returns
    -------

    QSizeF
      A new cute QSizeF around the copy Qt gave back. Python owns it.
    """
    #  QSizeF QCanvasImagePattern::imageSize() const
    address = self.uglySide.call(
        'ritual_ZNK19QCanvasImagePattern9imageSizeEv',
    )
    from ..QtCore import QSizeF
    return QSizeF._cuteOwning(address)

  def image(self) -> QCanvasImage:
    """
    Calls Qt's 'QCanvasImage QCanvasImagePattern::image() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvasimagepattern.html#image

    Returns
    -------

    QCanvasImage
      A new cute QCanvasImage around the copy Qt gave back. Python owns it.
    """
    #  QCanvasImage QCanvasImagePattern::image() const
    address = self.uglySide.call('ritual_ZNK19QCanvasImagePattern5imageEv')
    from . import QCanvasImage
    return QCanvasImage._cuteOwning(address)

  def rotation(self) -> float:
    """
    Calls Qt's 'qreal QCanvasImagePattern::rotation() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvasimagepattern.html#rotation
    """
    #  qreal QCanvasImagePattern::rotation() const
    return self.uglySide.call('ritual_ZNK19QCanvasImagePattern8rotationEv')

  def tintColor(self) -> QColor:
    """
    Calls Qt's 'QColor QCanvasImagePattern::tintColor() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvasimagepattern.html#tintColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QCanvasImagePattern::tintColor() const
    address = self.uglySide.call(
        'ritual_ZNK19QCanvasImagePattern9tintColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def serialNumber(self) -> int:
    """
    Calls Qt's 'uint QCanvasImagePattern::serialNumber() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvasimagepattern.html#serialNumber
    """
    #  uint QCanvasImagePattern::serialNumber() const
    return self.uglySide.call(
        'ritual_ZNK19QCanvasImagePattern12serialNumberEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float, float)
  def setStartPosition(self, x: float, y: float) -> None:
    """
    Calls Qt's 'void QCanvasImagePattern::setStartPosition(qreal x, qreal
    y)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvasimagepattern.html#setStartPosition

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.
    """
    #  void QCanvasImagePattern::setStartPosition(qreal x, qreal y)
    self.uglySide.call(
        'ritual_ZN19QCanvasImagePattern16setStartPositionEdd', x, y,
    )

  @overload(QPointF)
  def setStartPosition(self, point: QPointF) -> None:
    """
    Calls Qt's 'void QCanvasImagePattern::setStartPosition(QPointF point)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvasimagepattern.html#setStartPosition

    Parameters
    ----------

    point : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QCanvasImagePattern::setStartPosition(QPointF point)
    self.uglySide.call(
        'ritual_ZN19QCanvasImagePattern16setStartPositionE7QPointF',
        self._valueOf(point, 'QPointF'),
    )

  @overload(float, float)
  def setImageSize(self, width: float, height: float) -> None:
    """
    Calls Qt's 'void QCanvasImagePattern::setImageSize(qreal width, qreal
    height)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvasimagepattern.html#setImageSize

    Parameters
    ----------

    width : float
      Passed on as it is.

    height : float
      Passed on as it is.
    """
    #  void QCanvasImagePattern::setImageSize(qreal width, qreal height)
    self.uglySide.call(
        'ritual_ZN19QCanvasImagePattern12setImageSizeEdd', width, height,
    )

  @overload(QSizeF)
  def setImageSize(self, size: QSizeF) -> None:
    """
    Calls Qt's 'void QCanvasImagePattern::setImageSize(QSizeF size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvasimagepattern.html#setImageSize

    Parameters
    ----------

    size : QSizeF
      Passed on as a value: Qt reads the C++ QSizeF, which stays Python's
      own.
    """
    #  void QCanvasImagePattern::setImageSize(QSizeF size)
    self.uglySide.call(
        'ritual_ZN19QCanvasImagePattern12setImageSizeE6QSizeF',
        self._valueOf(size),
    )

  @overload(QCanvasImage)
  def setImage(self, image: QCanvasImage) -> None:
    """
    Calls Qt's 'void QCanvasImagePattern::setImage(const QCanvasImage
    &image)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvasimagepattern.html#setImage

    Parameters
    ----------

    image : QCanvasImage
      Passed on as a value: Qt reads the C++ QCanvasImage, which stays
      Python's own.
    """
    #  void QCanvasImagePattern::setImage(const QCanvasImage &image)
    self.uglySide.call(
        'ritual_ZN19QCanvasImagePattern8setImageERK12QCanvasImage',
        self._valueOf(image),
    )

  @overload(float)
  def setRotation(self, rotation: float) -> None:
    """
    Calls Qt's 'void QCanvasImagePattern::setRotation(qreal rotation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvasimagepattern.html#setRotation

    Parameters
    ----------

    rotation : float
      Passed on as it is.
    """
    #  void QCanvasImagePattern::setRotation(qreal rotation)
    self.uglySide.call(
        'ritual_ZN19QCanvasImagePattern11setRotationEd', rotation,
    )

  @overload(QColor)
  def setTintColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QCanvasImagePattern::setTintColor(QColor color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvasimagepattern.html#setTintColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QCanvasImagePattern::setTintColor(QColor color)
    self.uglySide.call(
        'ritual_ZN19QCanvasImagePattern12setTintColorE6QColor',
        self._valueOf(color),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, rhs: QCanvasImagePattern) -> bool:
    """
    Calls Qt's 'bool operator==(const QCanvasImagePattern &lhs, const
    QCanvasImagePattern &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvasimagepattern.html#operator==

    Parameters
    ----------

    rhs : QCanvasImagePattern
      Passed on as a value: Qt reads the C++ QCanvasImagePattern, which stays
      Python's own.
    """
    #  bool operator==(const QCanvasImagePattern &lhs, const
    #      QCanvasImagePattern &rhs)
    return Rituals.call(
        'ritual_ZeqRK19QCanvasImagePatternS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __ne__(self, rhs: QCanvasImagePattern) -> bool:
    """
    Calls Qt's 'bool operator!=(const QCanvasImagePattern &lhs, const
    QCanvasImagePattern &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvasimagepattern.html#operator!=

    Parameters
    ----------

    rhs : QCanvasImagePattern
      Passed on as a value: Qt reads the C++ QCanvasImagePattern, which stays
      Python's own.
    """
    #  bool operator!=(const QCanvasImagePattern &lhs, const
    #      QCanvasImagePattern &rhs)
    return Rituals.call(
        'ritual_ZneRK19QCanvasImagePatternS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __ne__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(QDebug)
  def __rlshift__(self, a0: QDebug) -> QDebug:
    """
    Calls Qt's 'QDebug operator<<(QDebug a0, const QCanvasImagePattern &a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvasimagepattern.html#operator<<

    Parameters
    ----------

    a0 : QDebug
      Passed on as a value: Qt reads the C++ QDebug, which stays Python's
      own.

    Returns
    -------

    QDebug
      A new cute QDebug around the copy Qt gave back. Python owns it.
    """
    #  QDebug operator<<(QDebug a0, const QCanvasImagePattern &a1)
    address = Rituals.call(
        'ritual_Zls6QDebugRK19QCanvasImagePattern',
        CuteMixin._valueOf(a0), CuteMixin._valueOf(self),
    )
    from ..QtCore import QDebug
    return QDebug._cuteOwning(address)

  @overload.fallback
  def __rlshift__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QCanvasImagePattern::QCanvasImagePattern()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvasimagepattern.html#QCanvasImagePattern
    """
    #  QCanvasImagePattern::QCanvasImagePattern()
    self._noteCreation(QCanvasImagePattern, lambda: Rituals.call(
        'ritual_ZN19QCanvasImagePatternC1Ev',
    ))

  @overload(QCanvasImage)
  def __init__(self, image: QCanvasImage) -> None:
    """
    Notes what was given, for Qt's
    'QCanvasImagePattern::QCanvasImagePattern(const QCanvasImage &image)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvasimagepattern.html#QCanvasImagePattern

    Parameters
    ----------

    image : QCanvasImage
      Passed on as a value: Qt reads the C++ QCanvasImage, which stays
      Python's own.
    """
    #  QCanvasImagePattern::QCanvasImagePattern(const QCanvasImage &image)
    self._noteCreation(QCanvasImagePattern, lambda: Rituals.call(
        'ritual_ZN19QCanvasImagePatternC1ERK12QCanvasImage',
        self._valueOf(image),
    ))

  @overload(QCanvasImage, QPointF, QSizeF)
  def __init__(
      self,
      image: QCanvasImage,
      startPosition: QPointF,
      imageSize: QSizeF,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QCanvasImagePattern::QCanvasImagePattern(const QCanvasImage &image,
    QPointF startPosition, QSizeF imageSize)', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvasimagepattern.html#QCanvasImagePattern

    Parameters
    ----------

    image : QCanvasImage
      Passed on as a value: Qt reads the C++ QCanvasImage, which stays
      Python's own.

    startPosition : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    imageSize : QSizeF
      Passed on as a value: Qt reads the C++ QSizeF, which stays Python's
      own.
    """
    #  QCanvasImagePattern::QCanvasImagePattern(const QCanvasImage &image,
    #      QPointF startPosition, QSizeF imageSize)
    self._noteCreation(QCanvasImagePattern, lambda: Rituals.call(
        'ritual_ZN19QCanvasImagePatternC1ERK12QCanvasImage7QPointF6QSizeF',
        self._valueOf(image), self._valueOf(startPosition, 'QPointF'),
        self._valueOf(imageSize),
    ))

  @overload(QCanvasImage, float, float, float, float)
  def __init__(
      self,
      image: QCanvasImage,
      startX: float,
      startY: float,
      imageWidth: float,
      imageHeight: float,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QCanvasImagePattern::QCanvasImagePattern(const QCanvasImage &image,
    qreal startX, qreal startY, qreal imageWidth, qreal imageHeight)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvasimagepattern.html#QCanvasImagePattern

    Parameters
    ----------

    image : QCanvasImage
      Passed on as a value: Qt reads the C++ QCanvasImage, which stays
      Python's own.

    startX : float
      Passed on as it is.

    startY : float
      Passed on as it is.

    imageWidth : float
      Passed on as it is.

    imageHeight : float
      Passed on as it is.
    """
    #  QCanvasImagePattern::QCanvasImagePattern(const QCanvasImage &image,
    #      qreal startX, qreal startY, qreal imageWidth, qreal imageHeight)
    self._noteCreation(QCanvasImagePattern, lambda: Rituals.call(
        'ritual_ZN19QCanvasImagePatternC1ERK12QCanvasImagedddd',
        self._valueOf(image), startX, startY, imageWidth, imageHeight,
    ))

  @overload(THIS)
  def __init__(self, a0: QCanvasImagePattern) -> None:
    """
    Notes what was given, for Qt's
    'QCanvasImagePattern::QCanvasImagePattern(const QCanvasImagePattern
    &a0)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvasimagepattern.html#QCanvasImagePattern

    Parameters
    ----------

    a0 : QCanvasImagePattern
      Passed on as a value: Qt reads the C++ QCanvasImagePattern, which stays
      Python's own.
    """
    #  QCanvasImagePattern::QCanvasImagePattern(const QCanvasImagePattern
    #      &a0)
    self._noteCreation(QCanvasImagePattern, lambda: Rituals.call(
        'ritual_ZN19QCanvasImagePatternC1ERKS_', self._valueOf(a0),
    ))

  @overload(QCanvasImagePatternPrivate)
  @overload(NoneType)
  def __init__(self, p: Optional[QCanvasImagePatternPrivate]) -> None:
    """
    Notes what was given, for Qt's
    'QCanvasImagePattern::QCanvasImagePattern(QCanvasImagePatternPrivate
    *p)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvasimagepattern.html#QCanvasImagePattern

    Parameters
    ----------

    p : Optional[QCanvasImagePatternPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QCanvasImagePattern::QCanvasImagePattern(QCanvasImagePatternPrivate
    #      *p)
    self._noteCreation(QCanvasImagePattern, lambda: Rituals.call(
        'ritual_ZN19QCanvasImagePatternC1EP26QCanvasImagePatternPrivate',
        self._addressOf(p),
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

  @staticmethod
  def detach(*__, **_) -> Never:
    """
    Qt's 'void QCanvasImagePattern::detach()': leans on
    'QCanvasImagePatternPrivate::createPaint(QCanvasPainter*) const', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QCanvasImagePattern.detach' has no cute function yet. Qt's 'void "
        "QCanvasImagePattern::detach()': leans on "
        "'QCanvasImagePatternPrivate::createPaint(QCanvasPainter*) const', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QCanvasImagePattern::swap(QCanvasImagePattern &other)': takes
    a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QCanvasImagePattern.swap' has no cute function yet. Qt's 'void "
        "QCanvasImagePattern::swap(QCanvasImagePattern &other)': takes a "
        "type Python has no way to hand over yet.")
