"""
QPlatformCursorImage binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/qpa/qplatformcursor.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import Qt

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QPoint
  from . import QImage
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QImage = WAIT['QImage']


class QPlatformCursorImage(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QPlatformCursorImage: a plain Python object standing
  in front of one C++ QPlatformCursorImage.

  C++ hands a QPlatformCursorImage around as a copy, so every C++
  QPlatformCursorImage behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QPlatformCursorImage that has a ritual and that
  Python can call so far, 4 names in all: 'image', 'hotspot', 'set',
  'createSystemCursor'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QPlatformCursorImage::QPlatformCursorImage(const uchar *data, const
    uchar *mask, int width, int height, int hotX, int hotY)': names 'uchar',
    which has no cute class yet.
  - Qt's 'void QPlatformCursorImage::set(const uchar *data, const uchar
    *mask, int width, int height, int hotX, int hotY)': names 'uchar', which
    has no cute class yet.
  - Qt's 'QPlatformCursorImage::~QPlatformCursorImage()': the destructor:
    Python removes its C++ QPlatformCursorImage by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QPlatformCursorImage is created at the first use, not by
    'QPlatformCursorImage(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QPlatformCursorImage back gives a copy the ritual
    made for Python, in a new cute QPlatformCursorImage.
  - Each name of Qt's QPlatformCursorImage that has no cute function yet,
    '__init__', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(int)
  def createSystemCursor(id: int) -> None:
    """
    Calls Qt's 'void QPlatformCursorImage::createSystemCursor(int id)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformcursorimage.html#createSystemCursor

    Parameters
    ----------

    id : int
      Passed on as it is.
    """
    #  void QPlatformCursorImage::createSystemCursor(int id)
    Rituals.call('ritual_ZN20QPlatformCursorImage18createSystemCursorEi', id)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPlatformCursorImage'

  #  Qt's '~QPlatformCursorImage()'. Naming it makes this a value class:
  #  Python owns every C++ QPlatformCursorImage behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN20QPlatformCursorImageD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def hotspot(self) -> QPoint:
    """
    Calls Qt's 'QPoint QPlatformCursorImage::hotspot() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformcursorimage.html#hotspot

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint QPlatformCursorImage::hotspot() const
    address = self.uglySide.call(
        'ritual_ZNK20QPlatformCursorImage7hotspotEv',
    )
    from ..QtCore import QPoint
    return QPoint._cuteOwning(address)

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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QPlatformCursorImage::QPlatformCursorImage(const uchar *data, const
    uchar *mask, int width, int height, int hotX, int hotY)': names 'uchar',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QPlatformCursorImage.__init__' has no cute function yet. Qt's "
        "'QPlatformCursorImage::QPlatformCursorImage(const uchar *data, "
        "const uchar *mask, int width, int height, int hotX, int hotY)': "
        "names 'uchar', which has no cute class yet.")

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

  def image(self) -> Optional[QImage]:
    """
    Calls Qt's 'QImage *QPlatformCursorImage::image()'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformcursorimage.html#image

    Returns
    -------

    Optional[QImage]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QImage *QPlatformCursorImage::image()
    address = self.uglySide.call('ritual_ZN20QPlatformCursorImage5imageEv')
    from . import QImage
    return QImage._cuteAt(address)

  @overload(QImage, int, int)
  def set(self, image: QImage, hx: int, hy: int) -> None:
    """
    Calls Qt's 'void QPlatformCursorImage::set(const QImage &image, int hx,
    int hy)'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformcursorimage.html#set

    Parameters
    ----------

    image : QImage
      Passed on as a value: Qt reads the C++ QImage, which stays Python's
      own.

    hx : int
      Passed on as it is.

    hy : int
      Passed on as it is.
    """
    #  void QPlatformCursorImage::set(const QImage &image, int hx, int hy)
    self.uglySide.call(
        'ritual_ZN20QPlatformCursorImage3setERK6QImageii',
        self._valueOf(image), hx, hy,
    )

  @overload(Qt.CursorShape)
  def set(self, a0: Qt.CursorShape) -> None:
    """
    Calls Qt's 'void QPlatformCursorImage::set(Qt::CursorShape a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformcursorimage.html#set

    Parameters
    ----------

    a0 : Qt.CursorShape
      Passed on as its number.
    """
    #  void QPlatformCursorImage::set(Qt::CursorShape a0)
    self.uglySide.call(
        'ritual_ZN20QPlatformCursorImage3setEN2Qt11CursorShapeE', a0.value,
    )
