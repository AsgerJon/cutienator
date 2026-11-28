"""
QQuickGridScaledImage binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickscalegrid_p_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQuickGridScaledImage to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QQuickBorderImage

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QIODevice
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QIODevice = WAIT['QIODevice']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickGridScaledImage(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuickGridScaledImage: a plain Python object standing
  in front of one C++ QQuickGridScaledImage.

  C++ hands a QQuickGridScaledImage around as a copy, so every C++
  QQuickGridScaledImage behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQuickGridScaledImage that has a ritual and that
  Python can call so far, 9 names in all: 'isValid', 'gridLeft', 'gridRight',
  'gridTop', 'gridBottom', 'horizontalTileRule', 'verticalTileRule',
  'pixmapUrl', 'stringToRule'. It can be made from Python, in 3 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQuickGridScaledImage &QQuickGridScaledImage::operator=(const
    QQuickGridScaledImage &a0)': assignment: Python binds a name and has no
    operator for it.
  - Qt's 'QQuickGridScaledImage::~QQuickGridScaledImage()': the destructor:
    Python removes its C++ QQuickGridScaledImage by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QQuickGridScaledImage is created at the first use, not by
    'QQuickGridScaledImage(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQuickGridScaledImage back gives a copy the ritual
    made for Python, in a new cute QQuickGridScaledImage.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  def stringToRule(a0: str) -> QQuickBorderImage.TileMode:
    """
    Calls Qt's 'QQuickBorderImage::TileMode
    QQuickGridScaledImage::stringToRule(QStringView a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgridscaledimage.html#stringToRule

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QQuickBorderImage.TileMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QQuickBorderImage.TileMode(number)' gives.
    """
    #  QQuickBorderImage::TileMode
    #      QQuickGridScaledImage::stringToRule(QStringView a0)
    return QQuickBorderImage.TileMode(Rituals.call(
        'ritual_ZN21QQuickGridScaledImage12stringToRuleE11QStringView', a0,
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickGridScaledImage'

  #  Qt's '~QQuickGridScaledImage()'. Naming it makes this a value class:
  #  Python owns every C++ QQuickGridScaledImage behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN21QQuickGridScaledImageD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QQuickGridScaledImage::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgridscaledimage.html#isValid
    """
    #  bool QQuickGridScaledImage::isValid() const
    return self.uglySide.call('ritual_ZNK21QQuickGridScaledImage7isValidEv')

  def gridLeft(self) -> int:
    """
    Calls Qt's 'int QQuickGridScaledImage::gridLeft() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgridscaledimage.html#gridLeft
    """
    #  int QQuickGridScaledImage::gridLeft() const
    return self.uglySide.call('ritual_ZNK21QQuickGridScaledImage8gridLeftEv')

  def gridRight(self) -> int:
    """
    Calls Qt's 'int QQuickGridScaledImage::gridRight() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgridscaledimage.html#gridRight
    """
    #  int QQuickGridScaledImage::gridRight() const
    return self.uglySide.call(
        'ritual_ZNK21QQuickGridScaledImage9gridRightEv',
    )

  def gridTop(self) -> int:
    """
    Calls Qt's 'int QQuickGridScaledImage::gridTop() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgridscaledimage.html#gridTop
    """
    #  int QQuickGridScaledImage::gridTop() const
    return self.uglySide.call('ritual_ZNK21QQuickGridScaledImage7gridTopEv')

  def gridBottom(self) -> int:
    """
    Calls Qt's 'int QQuickGridScaledImage::gridBottom() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgridscaledimage.html#gridBottom
    """
    #  int QQuickGridScaledImage::gridBottom() const
    return self.uglySide.call(
        'ritual_ZNK21QQuickGridScaledImage10gridBottomEv',
    )

  def horizontalTileRule(self) -> QQuickBorderImage.TileMode:
    """
    Calls Qt's 'QQuickBorderImage::TileMode
    QQuickGridScaledImage::horizontalTileRule() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgridscaledimage.html#horizontalTileRule

    Returns
    -------

    QQuickBorderImage.TileMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QQuickBorderImage.TileMode(number)' gives.
    """
    #  QQuickBorderImage::TileMode
    #      QQuickGridScaledImage::horizontalTileRule() const
    return QQuickBorderImage.TileMode(self.uglySide.call(
        'ritual_ZNK21QQuickGridScaledImage18horizontalTileRuleEv',
    ))

  def verticalTileRule(self) -> QQuickBorderImage.TileMode:
    """
    Calls Qt's 'QQuickBorderImage::TileMode
    QQuickGridScaledImage::verticalTileRule() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgridscaledimage.html#verticalTileRule

    Returns
    -------

    QQuickBorderImage.TileMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QQuickBorderImage.TileMode(number)' gives.
    """
    #  QQuickBorderImage::TileMode QQuickGridScaledImage::verticalTileRule()
    #      const
    return QQuickBorderImage.TileMode(self.uglySide.call(
        'ritual_ZNK21QQuickGridScaledImage16verticalTileRuleEv',
    ))

  def pixmapUrl(self) -> str:
    """
    Calls Qt's 'QString QQuickGridScaledImage::pixmapUrl() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgridscaledimage.html#pixmapUrl

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickGridScaledImage::pixmapUrl() const
    return self.uglySide.call(
        'ritual_ZNK21QQuickGridScaledImage9pixmapUrlEv',
    )

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
    Notes what was given, for Qt's
    'QQuickGridScaledImage::QQuickGridScaledImage()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgridscaledimage.html#QQuickGridScaledImage
    """
    #  QQuickGridScaledImage::QQuickGridScaledImage()
    self._noteCreation(QQuickGridScaledImage, lambda: Rituals.call(
        'ritual_ZN21QQuickGridScaledImageC1Ev',
    ))

  @overload(THIS)
  def __init__(self, a0: QQuickGridScaledImage) -> None:
    """
    Notes what was given, for Qt's
    'QQuickGridScaledImage::QQuickGridScaledImage(const QQuickGridScaledImage
    &a0)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgridscaledimage.html#QQuickGridScaledImage

    Parameters
    ----------

    a0 : QQuickGridScaledImage
      Passed on as a value: Qt reads the C++ QQuickGridScaledImage, which
      stays Python's own.
    """
    #  QQuickGridScaledImage::QQuickGridScaledImage(const
    #      QQuickGridScaledImage &a0)
    self._noteCreation(QQuickGridScaledImage, lambda: Rituals.call(
        'ritual_ZN21QQuickGridScaledImageC1ERKS_', self._valueOf(a0),
    ))

  @overload(QIODevice)
  @overload(NoneType)
  def __init__(self, a0: Optional[QIODevice]) -> None:
    """
    Notes what was given, for Qt's
    'QQuickGridScaledImage::QQuickGridScaledImage(QIODevice *a0)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgridscaledimage.html#QQuickGridScaledImage

    Parameters
    ----------

    a0 : Optional[QIODevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQuickGridScaledImage::QQuickGridScaledImage(QIODevice *a0)
    self._noteCreation(QQuickGridScaledImage, lambda: Rituals.call(
        'ritual_ZN21QQuickGridScaledImageC1EP9QIODevice',
        self._addressOf(a0),
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
