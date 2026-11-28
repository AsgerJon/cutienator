"""
QQuickIconImage binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickControls2Impl/6.12.0/QtQuickControls2Impl/private/qquickiconimage_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickIconImage to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtQuick import QQuickImage, QQuickItem

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QPointF, QRectF, QUrl
  from ..QtGui import QColor
  from . import QQuickIconImagePrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']
  QPointF = WAIT['QPointF']
  QRectF = WAIT['QRectF']
  QUrl = WAIT['QUrl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickIconImage(QQuickImage):
  """
  The cute side of Qt's QQuickIconImage: a plain Python object standing in
  front of one C++ QQuickIconImage.

  It is built on the cute 'QQuickImage', as Qt's QQuickIconImage is built on
  Qt's QQuickImage, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickIconImage that has a ritual and that Python
  can call so far, 15 names in all: 'metaObject', 'tr', 'name', 'setName',
  'color', 'setColor', 'setSource', 'snapPositionTo', 'nameChanged',
  'colorChanged', 'componentComplete', 'load', 'geometryChange',
  'pixmapChange', 'd_func'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickIconImage::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQuickIconImage::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'const QQuickIconImagePrivate *QQuickIconImage::d_func() const':
    takes in Python what 'QQuickIconImagePrivate *QQuickIconImage::d_func()'
    takes.

  What has no ritual
  ------------------

  4 of the 23 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickIconImage is created at the first use, not by
    'QQuickIconImage(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickIconImage.
  - Qt tells when it has removed the C++ QQuickIconImage. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

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
    Calls Qt's 'QString QQuickIconImage::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickiconimage.html#tr

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
    #  QString QQuickIconImage::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN15QQuickIconImage2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickIconImage'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickIconImage::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickiconimage.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickIconImage::metaObject() const
    address = self.uglySide.call('ritual_ZNK15QQuickIconImage10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def name(self) -> str:
    """
    Calls Qt's 'QString QQuickIconImage::name() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickiconimage.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickIconImage::name() const
    return self.uglySide.call('ritual_ZNK15QQuickIconImage4nameEv')

  def color(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickIconImage::color() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickiconimage.html#color

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickIconImage::color() const
    address = self.uglySide.call('ritual_ZNK15QQuickIconImage5colorEv')
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setName(self, name: str) -> None:
    """
    Calls Qt's 'void QQuickIconImage::setName(const QString &name)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickiconimage.html#setName

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickIconImage::setName(const QString &name)
    self.uglySide.call('ritual_ZN15QQuickIconImage7setNameERK7QString', name)

  @overload(QColor)
  def setColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QQuickIconImage::setColor(const QColor &color)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickiconimage.html#setColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QQuickIconImage::setColor(const QColor &color)
    self.uglySide.call(
        'ritual_ZN15QQuickIconImage8setColorERK6QColor',
        self._valueOf(color),
    )

  @overload(QUrl)
  def setSource(self, url: QUrl) -> None:
    """
    Calls Qt's 'void QQuickIconImage::setSource(const QUrl &url)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickiconimage.html#setSource

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QQuickIconImage::setSource(const QUrl &url)
    ritual = 'ritual_ZN15QQuickIconImage9setSourceERK4QUrl'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QQuickIconImage9setSourceERK4QUrl'
    self.uglySide.call(ritual, self._valueOf(url))

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
    'QQuickIconImage::QQuickIconImage(QQuickItem *parent)', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickiconimage.html#QQuickIconImage

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickIconImage::QQuickIconImage(QQuickItem *parent)
    self._noteCreation(QQuickIconImage, lambda: Rituals.call(
        'ritual_ZN15QQuickIconImageC1EP10QQuickItem',
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

  @overload(QPointF)
  def snapPositionTo(self, pos: QPointF) -> None:
    """
    Calls Qt's 'void QQuickIconImage::snapPositionTo(QPointF pos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickiconimage.html#snapPositionTo

    Parameters
    ----------

    pos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QQuickIconImage::snapPositionTo(QPointF pos)
    self.uglySide.call(
        'ritual_ZN15QQuickIconImage14snapPositionToE7QPointF',
        self._valueOf(pos, 'QPointF'),
    )

  def nameChanged(self) -> None:
    """
    Calls Qt's 'void QQuickIconImage::nameChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickiconimage.html#nameChanged
    """
    #  void QQuickIconImage::nameChanged()
    self.uglySide.call('ritual_ZN15QQuickIconImage11nameChangedEv')

  def colorChanged(self) -> None:
    """
    Calls Qt's 'void QQuickIconImage::colorChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickiconimage.html#colorChanged
    """
    #  void QQuickIconImage::colorChanged()
    self.uglySide.call('ritual_ZN15QQuickIconImage12colorChangedEv')

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQuickIconImage::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickiconimage.html#componentComplete
    """
    #  void QQuickIconImage::componentComplete()
    ritual = 'ritual_ZN15QQuickIconImage17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QQuickIconImage17componentCompleteEv'
    self.uglySide.call(ritual)

  def load(self) -> None:
    """
    Calls Qt's 'void QQuickIconImage::load()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickiconimage.html#load
    """
    #  void QQuickIconImage::load()
    ritual = 'ritual_ZN15QQuickIconImage4loadEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QQuickIconImage4loadEv'
    self.uglySide.call(ritual)

  @overload(QRectF, QRectF)
  def geometryChange(self, newGeometry: QRectF, oldGeometry: QRectF) -> None:
    """
    Calls Qt's 'void QQuickIconImage::geometryChange(const QRectF
    &newGeometry, const QRectF &oldGeometry)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickiconimage.html#geometryChange

    Parameters
    ----------

    newGeometry : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    oldGeometry : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QQuickIconImage::geometryChange(const QRectF &newGeometry, const
    #      QRectF &oldGeometry)
    ritual = 'ritual_ZN15QQuickIconImage14geometryChangeERK6QRectFS2_'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QQuickIconImage14geometryChangeERK6QRectFS2_'
    self.uglySide.call(
        ritual, self._valueOf(newGeometry), self._valueOf(oldGeometry),
    )

  def pixmapChange(self) -> None:
    """
    Calls Qt's 'void QQuickIconImage::pixmapChange()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickiconimage.html#pixmapChange
    """
    #  void QQuickIconImage::pixmapChange()
    ritual = 'ritual_ZN15QQuickIconImage12pixmapChangeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QQuickIconImage12pixmapChangeEv'
    self.uglySide.call(ritual)

  def d_func(self) -> Optional[QQuickIconImagePrivate]:
    """
    Calls Qt's 'QQuickIconImagePrivate *QQuickIconImage::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickiconimage.html#d_func

    Returns
    -------

    Optional[QQuickIconImagePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickIconImagePrivate *QQuickIconImage::d_func()
    address = self.uglySide.call('ritual_ZN15QQuickIconImage6d_funcEv')
    from . import QQuickIconImagePrivate
    return QQuickIconImagePrivate._cuteAt(address)
