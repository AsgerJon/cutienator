"""
QCanvasOffscreenCanvas binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCanvasPainter/qcanvasoffscreencanvas.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, CuteFlags, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QSize
  from ..QtGui import QColor, QRhiTexture
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']


class QCanvasOffscreenCanvas(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QCanvasOffscreenCanvas: a plain Python object
  standing in front of one C++ QCanvasOffscreenCanvas.

  C++ hands a QCanvasOffscreenCanvas around as a copy, so every C++
  QCanvasOffscreenCanvas behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QCanvasOffscreenCanvas that has a ritual and that
  Python can call so far, 10 names in all: 'isNull', 'width', 'height',
  'size', 'flags', 'fillColor', 'setFillColor', 'texture', '__eq__',
  '__ne__'. It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QCanvasOffscreenCanvas::~QCanvasOffscreenCanvas()': the destructor:
    Python removes its C++ QCanvasOffscreenCanvas by it, and has no other use
    for it.
  - Qt's 'QCanvasOffscreenCanvas &QCanvasOffscreenCanvas::operator=(const
    QCanvasOffscreenCanvas &canvas)': assignment: Python binds a name and has
    no operator for it.
  - Qt's
    'QCanvasOffscreenCanvas::QCanvasOffscreenCanvas(QCanvasOffscreenCanvas
    &&other)': takes a type Python has no way to hand over yet.
  - Qt's 'QCanvasOffscreenCanvas
    &QCanvasOffscreenCanvas::operator=(QCanvasOffscreenCanvas &&other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'void QCanvasOffscreenCanvas::swap(QCanvasOffscreenCanvas &other)':
    takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  4 of the 21 functions Qt declares: 3 not a gap; 1 Qt's library has no name
  for it, and its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QCanvasOffscreenCanvas is created at the first use, not by
    'QCanvasOffscreenCanvas(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QCanvasOffscreenCanvas back gives a copy the ritual
    made for Python, in a new cute QCanvasOffscreenCanvas.
  - Each name of Qt's QCanvasOffscreenCanvas that has no cute function yet,
    'detach', 'swap', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  #  The enums Qt writes inside QCanvasOffscreenCanvas, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class Flag(CuteFlags, scoped=True):
    """
    The flags enum 'QCanvasOffscreenCanvas::Flag' of Qt, with the 2 names Qt
    gives in it. Qt names the type of its combinations
    'QCanvasOffscreenCanvas::Flags'. C++ keeps these names inside the enum,
    so the class that holds the enum does not have them.
    """

    PreserveContents = 0x1
    MipMaps = 0x2

  Flags = Flag

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCanvasOffscreenCanvas'

  #  Qt's '~QCanvasOffscreenCanvas()'. Naming it makes this a value class:
  #  Python owns every C++ QCanvasOffscreenCanvas behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN22QCanvasOffscreenCanvasD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isNull(self) -> bool:
    """
    Calls Qt's 'bool QCanvasOffscreenCanvas::isNull() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvasoffscreencanvas.html#isNull
    """
    #  bool QCanvasOffscreenCanvas::isNull() const
    return self.uglySide.call('ritual_ZNK22QCanvasOffscreenCanvas6isNullEv')

  def width(self) -> int:
    """
    Calls Qt's 'int QCanvasOffscreenCanvas::width() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvasoffscreencanvas.html#width
    """
    #  int QCanvasOffscreenCanvas::width() const
    return self.uglySide.call('ritual_ZNK22QCanvasOffscreenCanvas5widthEv')

  def height(self) -> int:
    """
    Calls Qt's 'int QCanvasOffscreenCanvas::height() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvasoffscreencanvas.html#height
    """
    #  int QCanvasOffscreenCanvas::height() const
    return self.uglySide.call('ritual_ZNK22QCanvasOffscreenCanvas6heightEv')

  def size(self) -> QSize:
    """
    Calls Qt's 'QSize QCanvasOffscreenCanvas::size() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvasoffscreencanvas.html#size

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QCanvasOffscreenCanvas::size() const
    address = self.uglySide.call('ritual_ZNK22QCanvasOffscreenCanvas4sizeEv')
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def flags(self) -> Flags:
    """
    Calls Qt's 'Flags QCanvasOffscreenCanvas::flags() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvasoffscreencanvas.html#flags

    Returns
    -------

    Flags
      The value standing for the combination Qt gave back.
    """
    #  Flags QCanvasOffscreenCanvas::flags() const
    return QCanvasOffscreenCanvas.Flags(self.uglySide.call(
        'ritual_ZNK22QCanvasOffscreenCanvas5flagsEv',
    ))

  def fillColor(self) -> QColor:
    """
    Calls Qt's 'QColor QCanvasOffscreenCanvas::fillColor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvasoffscreencanvas.html#fillColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QCanvasOffscreenCanvas::fillColor() const
    address = self.uglySide.call(
        'ritual_ZNK22QCanvasOffscreenCanvas9fillColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def texture(self) -> Optional[QRhiTexture]:
    """
    Calls Qt's 'QRhiTexture *QCanvasOffscreenCanvas::texture() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvasoffscreencanvas.html#texture

    Returns
    -------

    Optional[QRhiTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiTexture *QCanvasOffscreenCanvas::texture() const
    address = self.uglySide.call(
        'ritual_ZNK22QCanvasOffscreenCanvas7textureEv',
    )
    from ..QtGui import QRhiTexture
    return QRhiTexture._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QColor)
  def setFillColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QCanvasOffscreenCanvas::setFillColor(QColor color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvasoffscreencanvas.html#setFillColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QCanvasOffscreenCanvas::setFillColor(QColor color)
    self.uglySide.call(
        'ritual_ZN22QCanvasOffscreenCanvas12setFillColorE6QColor',
        self._valueOf(color),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, rhs: QCanvasOffscreenCanvas) -> bool:
    """
    Calls Qt's 'bool operator==(const QCanvasOffscreenCanvas &lhs, const
    QCanvasOffscreenCanvas &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvasoffscreencanvas.html#operator==

    Parameters
    ----------

    rhs : QCanvasOffscreenCanvas
      Passed on as a value: Qt reads the C++ QCanvasOffscreenCanvas, which
      stays Python's own.
    """
    #  bool operator==(const QCanvasOffscreenCanvas &lhs, const
    #      QCanvasOffscreenCanvas &rhs)
    return Rituals.call(
        'ritual_ZeqRK22QCanvasOffscreenCanvasS1_',
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
  def __ne__(self, rhs: QCanvasOffscreenCanvas) -> bool:
    """
    Calls Qt's 'bool operator!=(const QCanvasOffscreenCanvas &lhs, const
    QCanvasOffscreenCanvas &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvasoffscreencanvas.html#operator!=

    Parameters
    ----------

    rhs : QCanvasOffscreenCanvas
      Passed on as a value: Qt reads the C++ QCanvasOffscreenCanvas, which
      stays Python's own.
    """
    #  bool operator!=(const QCanvasOffscreenCanvas &lhs, const
    #      QCanvasOffscreenCanvas &rhs)
    return Rituals.call(
        'ritual_ZneRK22QCanvasOffscreenCanvasS1_',
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

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QCanvasOffscreenCanvas::QCanvasOffscreenCanvas()', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvasoffscreencanvas.html#QCanvasOffscreenCanvas
    """
    #  QCanvasOffscreenCanvas::QCanvasOffscreenCanvas()
    self._noteCreation(QCanvasOffscreenCanvas, lambda: Rituals.call(
        'ritual_ZN22QCanvasOffscreenCanvasC1Ev',
    ))

  @overload(THIS)
  def __init__(self, canvas: QCanvasOffscreenCanvas) -> None:
    """
    Notes what was given, for Qt's
    'QCanvasOffscreenCanvas::QCanvasOffscreenCanvas(const
    QCanvasOffscreenCanvas &canvas)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvasoffscreencanvas.html#QCanvasOffscreenCanvas

    Parameters
    ----------

    canvas : QCanvasOffscreenCanvas
      Passed on as a value: Qt reads the C++ QCanvasOffscreenCanvas, which
      stays Python's own.
    """
    #  QCanvasOffscreenCanvas::QCanvasOffscreenCanvas(const
    #      QCanvasOffscreenCanvas &canvas)
    self._noteCreation(QCanvasOffscreenCanvas, lambda: Rituals.call(
        'ritual_ZN22QCanvasOffscreenCanvasC1ERKS_', self._valueOf(canvas),
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
    Qt's 'void QCanvasOffscreenCanvas::detach()': Qt's library has no name
    for it, and its code in Qt's source does not compile apart from its file:
    member access into incomplete type 'QCanvasOffscreenCanvasPrivate'.
    """
    raise NotImplementedError(
        "'QCanvasOffscreenCanvas.detach' has no cute function yet. Qt's "
        "'void QCanvasOffscreenCanvas::detach()': Qt's library has no name "
        "for it, and its code in Qt's source does not compile apart from "
        "its file: member access into incomplete type "
        "'QCanvasOffscreenCanvasPrivate'.")

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QCanvasOffscreenCanvas::swap(QCanvasOffscreenCanvas &other)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QCanvasOffscreenCanvas.swap' has no cute function yet. Qt's 'void "
        "QCanvasOffscreenCanvas::swap(QCanvasOffscreenCanvas &other)': "
        "takes a type Python has no way to hand over yet.")
