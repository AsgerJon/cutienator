"""
QCanvasImage binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCanvasPainter/qcanvasimage.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QDebug, QSize
  from ..QtGui import QColor
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']
  QDebug = WAIT['QDebug']


class QCanvasImage(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QCanvasImage: a plain Python object standing in front
  of one C++ QCanvasImage.

  C++ hands a QCanvasImage around as a copy, so every C++ QCanvasImage behind
  a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QCanvasImage that has a ritual and that Python can
  call so far, 13 names in all: 'id', 'width', 'height', 'size',
  'sizeInBytes', 'devicePixelRatio', 'isNull', 'tintColor', 'setTintColor',
  '__eq__', '__ne__', 'detach', '__rlshift__'. It can be made from Python, in
  2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QCanvasImage::~QCanvasImage()': the destructor: Python removes its
    C++ QCanvasImage by it, and has no other use for it.
  - Qt's 'QCanvasImage &QCanvasImage::operator=(const QCanvasImage &image)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'QCanvasImage::QCanvasImage(QCanvasImage &&other)': takes a type
    Python has no way to hand over yet.
  - Qt's 'QCanvasImage &QCanvasImage::operator=(QCanvasImage &&other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'void QCanvasImage::swap(QCanvasImage &other)': takes a type Python
    has no way to hand over yet.
  - Qt's 'QVariant QCanvasImage::operator QVariant() const': an operator
    Python has no name for.

  What has no ritual
  ------------------

  3 of the 24 functions Qt declares: 3 not a gap.

  What to expect
  --------------

  - The C++ QCanvasImage is created at the first use, not by
    'QCanvasImage(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QCanvasImage back gives a copy the ritual made for
    Python, in a new cute QCanvasImage.
  - Each name of Qt's QCanvasImage that has no cute function yet, 'swap',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCanvasImage'

  #  Qt's '~QCanvasImage()'. Naming it makes this a value class: Python owns
  #  every C++ QCanvasImage behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN12QCanvasImageD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def id(self) -> int:
    """
    Calls Qt's 'int QCanvasImage::id() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvasimage.html#id
    """
    #  int QCanvasImage::id() const
    return self.uglySide.call('ritual_ZNK12QCanvasImage2idEv')

  def width(self) -> int:
    """
    Calls Qt's 'int QCanvasImage::width() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvasimage.html#width
    """
    #  int QCanvasImage::width() const
    return self.uglySide.call('ritual_ZNK12QCanvasImage5widthEv')

  def height(self) -> int:
    """
    Calls Qt's 'int QCanvasImage::height() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvasimage.html#height
    """
    #  int QCanvasImage::height() const
    return self.uglySide.call('ritual_ZNK12QCanvasImage6heightEv')

  def size(self) -> QSize:
    """
    Calls Qt's 'QSize QCanvasImage::size() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvasimage.html#size

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QCanvasImage::size() const
    address = self.uglySide.call('ritual_ZNK12QCanvasImage4sizeEv')
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def sizeInBytes(self) -> int:
    """
    Calls Qt's 'qsizetype QCanvasImage::sizeInBytes() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvasimage.html#sizeInBytes
    """
    #  qsizetype QCanvasImage::sizeInBytes() const
    return self.uglySide.call('ritual_ZNK12QCanvasImage11sizeInBytesEv')

  def devicePixelRatio(self) -> float:
    """
    Calls Qt's 'qreal QCanvasImage::devicePixelRatio() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvasimage.html#devicePixelRatio
    """
    #  qreal QCanvasImage::devicePixelRatio() const
    return self.uglySide.call('ritual_ZNK12QCanvasImage16devicePixelRatioEv')

  def isNull(self) -> bool:
    """
    Calls Qt's 'bool QCanvasImage::isNull() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvasimage.html#isNull
    """
    #  bool QCanvasImage::isNull() const
    return self.uglySide.call('ritual_ZNK12QCanvasImage6isNullEv')

  def tintColor(self) -> QColor:
    """
    Calls Qt's 'QColor QCanvasImage::tintColor() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvasimage.html#tintColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QCanvasImage::tintColor() const
    address = self.uglySide.call('ritual_ZNK12QCanvasImage9tintColorEv')
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QColor)
  def setTintColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QCanvasImage::setTintColor(QColor color)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvasimage.html#setTintColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QCanvasImage::setTintColor(QColor color)
    self.uglySide.call(
        'ritual_ZN12QCanvasImage12setTintColorE6QColor',
        self._valueOf(color),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, rhs: QCanvasImage) -> bool:
    """
    Calls Qt's 'bool operator==(const QCanvasImage &lhs, const QCanvasImage
    &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvasimage.html#operator==

    Parameters
    ----------

    rhs : QCanvasImage
      Passed on as a value: Qt reads the C++ QCanvasImage, which stays
      Python's own.
    """
    #  bool operator==(const QCanvasImage &lhs, const QCanvasImage &rhs)
    return Rituals.call(
        'ritual_ZeqRK12QCanvasImageS1_',
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
  def __ne__(self, rhs: QCanvasImage) -> bool:
    """
    Calls Qt's 'bool operator!=(const QCanvasImage &lhs, const QCanvasImage
    &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvasimage.html#operator!=

    Parameters
    ----------

    rhs : QCanvasImage
      Passed on as a value: Qt reads the C++ QCanvasImage, which stays
      Python's own.
    """
    #  bool operator!=(const QCanvasImage &lhs, const QCanvasImage &rhs)
    return Rituals.call(
        'ritual_ZneRK12QCanvasImageS1_',
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
    Calls Qt's 'QDebug operator<<(QDebug a0, const QCanvasImage &a1)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvasimage.html#operator<<

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
    #  QDebug operator<<(QDebug a0, const QCanvasImage &a1)
    address = Rituals.call(
        'ritual_Zls6QDebugRK12QCanvasImage',
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
    Notes what was given, for Qt's 'QCanvasImage::QCanvasImage()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qcanvasimage.html#QCanvasImage
    """
    #  QCanvasImage::QCanvasImage()
    self._noteCreation(QCanvasImage, lambda: Rituals.call(
        'ritual_ZN12QCanvasImageC1Ev',
    ))

  @overload(THIS)
  def __init__(self, image: QCanvasImage) -> None:
    """
    Notes what was given, for Qt's 'QCanvasImage::QCanvasImage(const
    QCanvasImage &image)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qcanvasimage.html#QCanvasImage

    Parameters
    ----------

    image : QCanvasImage
      Passed on as a value: Qt reads the C++ QCanvasImage, which stays
      Python's own.
    """
    #  QCanvasImage::QCanvasImage(const QCanvasImage &image)
    self._noteCreation(QCanvasImage, lambda: Rituals.call(
        'ritual_ZN12QCanvasImageC1ERKS_', self._valueOf(image),
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

  def detach(self) -> None:
    """
    Calls Qt's 'void QCanvasImage::detach()'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvasimage.html#detach
    """
    #  void QCanvasImage::detach()
    self.uglySide.call('ritual_ZN12QCanvasImage6detachEv')

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QCanvasImage::swap(QCanvasImage &other)': takes a type Python
    has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QCanvasImage.swap' has no cute function yet. Qt's 'void "
        "QCanvasImage::swap(QCanvasImage &other)': takes a type Python has "
        "no way to hand over yet.")
