"""
QQuickCanvasPixmap binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickcanvasitem_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQuickCanvasPixmap to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtGui import QImage
  from . import QQuickPixmap
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QImage = WAIT['QImage']
  QQuickPixmap = WAIT['QQuickPixmap']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickCanvasPixmap(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuickCanvasPixmap: a plain Python object standing in
  front of one C++ QQuickCanvasPixmap.

  What exists
  -----------

  Every function of Qt's QQuickCanvasPixmap that has a ritual and that Python
  can call so far, 5 names in all: 'image', 'width', 'height', 'isValid',
  'pixmap'. It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQuickCanvasPixmap::~QQuickCanvasPixmap()': the destructor: Python
    never removes a C++ QQuickCanvasPixmap.

  What to expect
  --------------

  - The C++ QQuickCanvasPixmap is created at the first use, not by
    'QQuickCanvasPixmap(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickCanvasPixmap.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickCanvasPixmap'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def width(self) -> float:
    """
    Calls Qt's 'qreal QQuickCanvasPixmap::width() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcanvaspixmap.html#width
    """
    #  qreal QQuickCanvasPixmap::width() const
    return self.uglySide.call('ritual_ZNK18QQuickCanvasPixmap5widthEv')

  def height(self) -> float:
    """
    Calls Qt's 'qreal QQuickCanvasPixmap::height() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcanvaspixmap.html#height
    """
    #  qreal QQuickCanvasPixmap::height() const
    return self.uglySide.call('ritual_ZNK18QQuickCanvasPixmap6heightEv')

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QQuickCanvasPixmap::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcanvaspixmap.html#isValid
    """
    #  bool QQuickCanvasPixmap::isValid() const
    return self.uglySide.call('ritual_ZNK18QQuickCanvasPixmap7isValidEv')

  def pixmap(self) -> Optional[QQuickPixmap]:
    """
    Calls Qt's 'QQuickPixmap *QQuickCanvasPixmap::pixmap() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcanvaspixmap.html#pixmap

    Returns
    -------

    Optional[QQuickPixmap]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickPixmap *QQuickCanvasPixmap::pixmap() const
    address = self.uglySide.call('ritual_ZNK18QQuickCanvasPixmap6pixmapEv')
    from . import QQuickPixmap
    return QQuickPixmap._cuteAt(address)

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

  @overload(QImage)
  def __init__(self, image: QImage) -> None:
    """
    Notes what was given, for Qt's
    'QQuickCanvasPixmap::QQuickCanvasPixmap(const QImage &image)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcanvaspixmap.html#QQuickCanvasPixmap

    Parameters
    ----------

    image : QImage
      Passed on as a value: Qt reads the C++ QImage, which stays Python's
      own.
    """
    #  QQuickCanvasPixmap::QQuickCanvasPixmap(const QImage &image)
    self._noteCreation(QQuickCanvasPixmap, lambda: Rituals.call(
        'ritual_ZN18QQuickCanvasPixmapC1ERK6QImage', self._valueOf(image),
    ))

  @overload(QQuickPixmap)
  @overload(NoneType)
  def __init__(self, pixmap: Optional[QQuickPixmap]) -> None:
    """
    Notes what was given, for Qt's
    'QQuickCanvasPixmap::QQuickCanvasPixmap(QQuickPixmap *pixmap)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcanvaspixmap.html#QQuickCanvasPixmap

    Parameters
    ----------

    pixmap : Optional[QQuickPixmap]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQuickCanvasPixmap::QQuickCanvasPixmap(QQuickPixmap *pixmap)
    self._noteCreation(QQuickCanvasPixmap, lambda: Rituals.call(
        'ritual_ZN18QQuickCanvasPixmapC1EP12QQuickPixmap',
        self._addressOf(pixmap),
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

  def image(self) -> QImage:
    """
    Calls Qt's 'QImage QQuickCanvasPixmap::image()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcanvaspixmap.html#image

    Returns
    -------

    QImage
      A new cute QImage around the copy Qt gave back. Python owns it.
    """
    #  QImage QQuickCanvasPixmap::image()
    address = self.uglySide.call('ritual_ZN18QQuickCanvasPixmap5imageEv')
    from ..QtGui import QImage
    return QImage._cuteOwning(address)
