"""
QQuickBorderImage binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickborderimage_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQuickBorderImage to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from . import QQuickImageBase, QQuickItem

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QUrl
  from . import QQuickBorderImagePrivate, QQuickGridScaledImage
  from . import QQuickScaleGrid, QSGNode
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickGridScaledImage = WAIT['QQuickGridScaledImage']
  QSGNode = WAIT['QSGNode']
  QUrl = WAIT['QUrl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickBorderImage(QQuickImageBase):
  """
  The cute side of Qt's QQuickBorderImage: a plain Python object standing in
  front of one C++ QQuickBorderImage.

  It is built on the cute 'QQuickImageBase', as Qt's QQuickBorderImage is
  built on Qt's QQuickImageBase, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickBorderImage that has a ritual and that Python
  can call so far, 19 names in all: 'metaObject', 'tr', 'border',
  'horizontalTileMode', 'setHorizontalTileMode', 'verticalTileMode',
  'setVerticalTileMode', 'setSource', 'horizontalTileModeChanged',
  'verticalTileModeChanged', 'sourceSizeChanged', 'load', 'pixmapChange',
  'updatePaintNode', 'setGridScaledImage', 'doUpdate', 'requestFinished',
  'sciRequestFinished', 'd_func'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickBorderImage::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQuickBorderImage::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickBorderImage::~QQuickBorderImage()': the destructor: Python
    never removes a C++ QQuickBorderImage.
  - Qt's 'const QQuickBorderImagePrivate *QQuickBorderImage::d_func() const':
    takes in Python what 'QQuickBorderImagePrivate
    *QQuickBorderImage::d_func()' takes.

  What has no ritual
  ------------------

  4 of the 28 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickBorderImage is created at the first use, not by
    'QQuickBorderImage(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickBorderImage.
  - Qt tells when it has removed the C++ QQuickBorderImage. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QQuickBorderImage, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class TileMode(CuteNum):
    """
    The enum 'QQuickBorderImage::TileMode' of Qt, with the 3 names Qt gives
    in it.
    """

    Stretch = Kee[int](0)
    Repeat = Kee[int](1)
    Round = Kee[int](2)

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
    Calls Qt's 'QString QQuickBorderImage::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickborderimage.html#tr

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
    #  QString QQuickBorderImage::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN17QQuickBorderImage2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickBorderImage'

  #  A C++ QQuickBorderImage Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickBorderImage'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickBorderImage::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickborderimage.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickBorderImage::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK17QQuickBorderImage10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def horizontalTileMode(self) -> TileMode:
    """
    Calls Qt's 'TileMode QQuickBorderImage::horizontalTileMode() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickborderimage.html#horizontalTileMode

    Returns
    -------

    TileMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'TileMode(number)' gives.
    """
    #  TileMode QQuickBorderImage::horizontalTileMode() const
    return QQuickBorderImage.TileMode(self.uglySide.call(
        'ritual_ZNK17QQuickBorderImage18horizontalTileModeEv',
    ))

  def verticalTileMode(self) -> TileMode:
    """
    Calls Qt's 'TileMode QQuickBorderImage::verticalTileMode() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickborderimage.html#verticalTileMode

    Returns
    -------

    TileMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'TileMode(number)' gives.
    """
    #  TileMode QQuickBorderImage::verticalTileMode() const
    return QQuickBorderImage.TileMode(self.uglySide.call(
        'ritual_ZNK17QQuickBorderImage16verticalTileModeEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(TileMode)
  def setHorizontalTileMode(self, a0: TileMode) -> None:
    """
    Calls Qt's 'void QQuickBorderImage::setHorizontalTileMode(TileMode a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickborderimage.html#setHorizontalTileMode

    Parameters
    ----------

    a0 : TileMode
      Passed on as its number.
    """
    #  void QQuickBorderImage::setHorizontalTileMode(TileMode a0)
    self.uglySide.call(
        'ritual_ZN17QQuickBorderImage21setHorizontalTileModeENS_8TileModeE',
        a0.value,
    )

  @overload(TileMode)
  def setVerticalTileMode(self, a0: TileMode) -> None:
    """
    Calls Qt's 'void QQuickBorderImage::setVerticalTileMode(TileMode a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickborderimage.html#setVerticalTileMode

    Parameters
    ----------

    a0 : TileMode
      Passed on as its number.
    """
    #  void QQuickBorderImage::setVerticalTileMode(TileMode a0)
    self.uglySide.call(
        'ritual_ZN17QQuickBorderImage19setVerticalTileModeENS_8TileModeE',
        a0.value,
    )

  @overload(QUrl)
  def setSource(self, url: QUrl) -> None:
    """
    Calls Qt's 'void QQuickBorderImage::setSource(const QUrl &url)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickborderimage.html#setSource

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QQuickBorderImage::setSource(const QUrl &url)
    ritual = 'ritual_ZN17QQuickBorderImage9setSourceERK4QUrl'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQuickBorderImage9setSourceERK4QUrl'
    self.uglySide.call(ritual, self._valueOf(url))

  @overload(QQuickGridScaledImage)
  def setGridScaledImage(self, sci: QQuickGridScaledImage) -> None:
    """
    Calls Qt's 'void QQuickBorderImage::setGridScaledImage(const
    QQuickGridScaledImage &sci)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickborderimage.html#setGridScaledImage

    Parameters
    ----------

    sci : QQuickGridScaledImage
      Passed on as a value: Qt reads the C++ QQuickGridScaledImage, which
      stays Python's own.
    """
    #  void QQuickBorderImage::setGridScaledImage(const QQuickGridScaledImage
    #      &sci)
    self.uglySide.call(
        'ritual_ZN17QQuickBorderImage18setGridScaledImageERK21QQuickGridSca'
        'ledImage',
        self._valueOf(sci),
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
  @overload(QQuickItem)
  @overload(NoneType)
  def __init__(self, parent: Optional[QQuickItem] = None) -> None:
    """
    Notes what was given, for Qt's
    'QQuickBorderImage::QQuickBorderImage(QQuickItem *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickborderimage.html#QQuickBorderImage

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickBorderImage::QQuickBorderImage(QQuickItem *parent)
    self._noteCreation(QQuickBorderImage, lambda: Rituals.call(
        'ritual_ZN17QQuickBorderImageC1EP10QQuickItem',
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

  def border(self) -> Optional[QQuickScaleGrid]:
    """
    Calls Qt's 'QQuickScaleGrid *QQuickBorderImage::border()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickborderimage.html#border

    Returns
    -------

    Optional[QQuickScaleGrid]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickScaleGrid *QQuickBorderImage::border()
    address = self.uglySide.call('ritual_ZN17QQuickBorderImage6borderEv')
    from . import QQuickScaleGrid
    return QQuickScaleGrid._cuteAt(address)

  def horizontalTileModeChanged(self) -> None:
    """
    Calls Qt's 'void QQuickBorderImage::horizontalTileModeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickborderimage.html#horizontalTileModeChanged
    """
    #  void QQuickBorderImage::horizontalTileModeChanged()
    self.uglySide.call(
        'ritual_ZN17QQuickBorderImage25horizontalTileModeChangedEv',
    )

  def verticalTileModeChanged(self) -> None:
    """
    Calls Qt's 'void QQuickBorderImage::verticalTileModeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickborderimage.html#verticalTileModeChanged
    """
    #  void QQuickBorderImage::verticalTileModeChanged()
    self.uglySide.call(
        'ritual_ZN17QQuickBorderImage23verticalTileModeChangedEv',
    )

  def sourceSizeChanged(self) -> None:
    """
    Calls Qt's 'void QQuickBorderImage::sourceSizeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickborderimage.html#sourceSizeChanged
    """
    #  void QQuickBorderImage::sourceSizeChanged()
    self.uglySide.call('ritual_ZN17QQuickBorderImage17sourceSizeChangedEv')

  def load(self) -> None:
    """
    Calls Qt's 'void QQuickBorderImage::load()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickborderimage.html#load
    """
    #  void QQuickBorderImage::load()
    ritual = 'ritual_ZN17QQuickBorderImage4loadEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQuickBorderImage4loadEv'
    self.uglySide.call(ritual)

  def pixmapChange(self) -> None:
    """
    Calls Qt's 'void QQuickBorderImage::pixmapChange()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickborderimage.html#pixmapChange
    """
    #  void QQuickBorderImage::pixmapChange()
    ritual = 'ritual_ZN17QQuickBorderImage12pixmapChangeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQuickBorderImage12pixmapChangeEv'
    self.uglySide.call(ritual)

  @overload(QSGNode, QQuickItem.UpdatePaintNodeData)
  @overload(QSGNode, NoneType)
  @overload(NoneType, QQuickItem.UpdatePaintNodeData)
  @overload(NoneType, NoneType)
  def updatePaintNode(
      self,
      a0: Optional[QSGNode],
      a1: Optional[QQuickItem.UpdatePaintNodeData],
  ) -> Optional[QSGNode]:
    """
    Calls Qt's 'QSGNode *QQuickBorderImage::updatePaintNode(QSGNode *a0,
    UpdatePaintNodeData *a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickborderimage.html#updatePaintNode

    Parameters
    ----------

    a0 : Optional[QSGNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : Optional[QQuickItem.UpdatePaintNodeData]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QSGNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGNode *QQuickBorderImage::updatePaintNode(QSGNode *a0,
    #      UpdatePaintNodeData *a1)
    ritual = (
        'ritual_ZN17QQuickBorderImage15updatePaintNodeEP7QSGNodePN10QQuickI'
        'tem19UpdatePaintNodeDataE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QQuickBorderImage15updatePaintNodeEP7QSGNodePN10Q'
          'QuickItem19UpdatePaintNodeDataE')
    address = self.uglySide.call(
        ritual, self._addressOf(a0, 'QSGNode'), self._addressOf(a1),
    )
    from . import QSGNode
    return QSGNode._cuteAt(address)

  def doUpdate(self) -> None:
    """
    Calls Qt's 'void QQuickBorderImage::doUpdate()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickborderimage.html#doUpdate
    """
    #  void QQuickBorderImage::doUpdate()
    self.uglySide.call('ritual_ZN17QQuickBorderImage8doUpdateEv')

  def requestFinished(self) -> None:
    """
    Calls Qt's 'void QQuickBorderImage::requestFinished()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickborderimage.html#requestFinished
    """
    #  void QQuickBorderImage::requestFinished()
    ritual = 'ritual_ZN17QQuickBorderImage15requestFinishedEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQuickBorderImage15requestFinishedEv'
    self.uglySide.call(ritual)

  def sciRequestFinished(self) -> None:
    """
    Calls Qt's 'void QQuickBorderImage::sciRequestFinished()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickborderimage.html#sciRequestFinished
    """
    #  void QQuickBorderImage::sciRequestFinished()
    self.uglySide.call('ritual_ZN17QQuickBorderImage18sciRequestFinishedEv')

  def d_func(self) -> Optional[QQuickBorderImagePrivate]:
    """
    Calls Qt's 'QQuickBorderImagePrivate *QQuickBorderImage::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickborderimage.html#d_func

    Returns
    -------

    Optional[QQuickBorderImagePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickBorderImagePrivate *QQuickBorderImage::d_func()
    address = self.uglySide.call('ritual_ZN17QQuickBorderImage6d_funcEv')
    from . import QQuickBorderImagePrivate
    return QQuickBorderImagePrivate._cuteAt(address)
