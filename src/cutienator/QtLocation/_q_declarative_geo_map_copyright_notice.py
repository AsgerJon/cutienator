"""
QDeclarativeGeoMapCopyrightNotice binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLocation/6.12.0/QtLocation/private/qdeclarativegeomapcopyrightsnotice_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QDeclarativeGeoMapCopyrightNotice to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtQuick import QQuickItem, QQuickPaintedItem

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QColor, QImage, QMouseEvent, QPainter
  from . import QDeclarativeGeoMap
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']
  QDeclarativeGeoMap = WAIT['QDeclarativeGeoMap']
  QImage = WAIT['QImage']
  QMouseEvent = WAIT['QMouseEvent']
  QPainter = WAIT['QPainter']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDeclarativeGeoMapCopyrightNotice(QQuickPaintedItem):
  """
  The cute side of Qt's QDeclarativeGeoMapCopyrightNotice: a plain Python
  object standing in front of one C++ QDeclarativeGeoMapCopyrightNotice.

  It is built on the cute 'QQuickPaintedItem', as Qt's
  QDeclarativeGeoMapCopyrightNotice is built on Qt's QQuickPaintedItem, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's QDeclarativeGeoMapCopyrightNotice that has a ritual
  and that Python can call so far, 24 names in all: 'metaObject', 'tr',
  'setCopyrightsZ', 'setCopyrightsVisible', 'copyrightsVisible',
  'anchorToBottomLeft', 'setMapSource', 'mapSource', 'styleSheet',
  'setStyleSheet', 'copyrightsImageChanged', 'copyrightsChanged',
  'onCopyrightsStyleSheetChanged', 'linkActivated', 'mapSourceChanged',
  'backgroundColorChanged', 'styleSheetChanged', 'copyrightsVisibleChanged',
  'paint', 'mousePressEvent', 'mouseReleaseEvent', 'rasterizeHtmlAndUpdate',
  'connectMap', 'createCopyright'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QDeclarativeGeoMapCopyrightNotice::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int
    QDeclarativeGeoMapCopyrightNotice::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's
    'QDeclarativeGeoMapCopyrightNotice::~QDeclarativeGeoMapCopyrightNotice(
    )': the destructor: Python never removes a C++
    QDeclarativeGeoMapCopyrightNotice.
  - Qt's 'QDeclarativeGeoMapCopyrightNoticePrivate
    *QDeclarativeGeoMapCopyrightNotice::d_func()': gives
    'QDeclarativeGeoMapCopyrightNoticePrivate', which has no cute class yet.
  - Qt's 'const QDeclarativeGeoMapCopyrightNoticePrivate
    *QDeclarativeGeoMapCopyrightNotice::d_func() const': gives
    'QDeclarativeGeoMapCopyrightNoticePrivate', which has no cute class yet.

  What has no ritual
  ------------------

  4 of the 34 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QDeclarativeGeoMapCopyrightNotice is created at the first use,
    not by 'QDeclarativeGeoMapCopyrightNotice(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDeclarativeGeoMapCopyrightNotice.
  - Qt tells when it has removed the C++ QDeclarativeGeoMapCopyrightNotice.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
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
    Calls Qt's 'QString QDeclarativeGeoMapCopyrightNotice::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapcopyrightnotice.html#tr

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
    #  QString QDeclarativeGeoMapCopyrightNotice::tr(const char *s, const
    #      char *c, int n)
    return Rituals.call(
        'ritual_ZN33QDeclarativeGeoMapCopyrightNotice2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDeclarativeGeoMapCopyrightNotice'

  #  A C++ QDeclarativeGeoMapCopyrightNotice Python makes is of a C++ class
  #  of ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QDeclarativeGeoMapCopyrightNotice'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject
    *QDeclarativeGeoMapCopyrightNotice::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapcopyrightnotice.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QDeclarativeGeoMapCopyrightNotice::metaObject()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK33QDeclarativeGeoMapCopyrightNotice10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def copyrightsVisible(self) -> bool:
    """
    Calls Qt's 'bool QDeclarativeGeoMapCopyrightNotice::copyrightsVisible()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapcopyrightnotice.html
    """
    #  bool QDeclarativeGeoMapCopyrightNotice::copyrightsVisible() const
    return self.uglySide.call(
        'ritual_ZNK33QDeclarativeGeoMapCopyrightNotice17copyrightsVisibleEv',
    )

  def styleSheet(self) -> str:
    """
    Calls Qt's 'QString QDeclarativeGeoMapCopyrightNotice::styleSheet()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapcopyrightnotice.html#styleSheet

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDeclarativeGeoMapCopyrightNotice::styleSheet() const
    return self.uglySide.call(
        'ritual_ZNK33QDeclarativeGeoMapCopyrightNotice10styleSheetEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setCopyrightsZ(self, copyrightsZ: float) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoMapCopyrightNotice::setCopyrightsZ(qreal
    copyrightsZ)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapcopyrightnotice.html

    Parameters
    ----------

    copyrightsZ : float
      Passed on as it is.
    """
    #  void QDeclarativeGeoMapCopyrightNotice::setCopyrightsZ(qreal
    #      copyrightsZ)
    self.uglySide.call(
        'ritual_ZN33QDeclarativeGeoMapCopyrightNotice14setCopyrightsZEd',
        copyrightsZ,
    )

  @overload(bool)
  def setCopyrightsVisible(self, visible: bool) -> None:
    """
    Calls Qt's 'void
    QDeclarativeGeoMapCopyrightNotice::setCopyrightsVisible(bool visible)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapcopyrightnotice.html

    Parameters
    ----------

    visible : bool
      Passed on as it is.
    """
    #  void QDeclarativeGeoMapCopyrightNotice::setCopyrightsVisible(bool
    #      visible)
    self.uglySide.call(
        'ritual_ZN33QDeclarativeGeoMapCopyrightNotice20setCopyrightsVisible'
        'Eb',
        visible,
    )

  @overload(QDeclarativeGeoMap)
  @overload(NoneType)
  def setMapSource(self, mapSource: Optional[QDeclarativeGeoMap]) -> None:
    """
    Calls Qt's 'void
    QDeclarativeGeoMapCopyrightNotice::setMapSource(QDeclarativeGeoMap
    *mapSource)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapcopyrightnotice.html

    Parameters
    ----------

    mapSource : Optional[QDeclarativeGeoMap]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void
    #      QDeclarativeGeoMapCopyrightNotice::setMapSource(QDeclarativeGeoMap
    #      *mapSource)
    self.uglySide.call(
        'ritual_ZN33QDeclarativeGeoMapCopyrightNotice12setMapSourceEP18QDec'
        'larativeGeoMap',
        self._addressOf(mapSource),
    )

  @overload(str)
  def setStyleSheet(self, styleSheet: str) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoMapCopyrightNotice::setStyleSheet(const
    QString &styleSheet)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapcopyrightnotice.html

    Parameters
    ----------

    styleSheet : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDeclarativeGeoMapCopyrightNotice::setStyleSheet(const QString
    #      &styleSheet)
    self.uglySide.call(
        'ritual_ZN33QDeclarativeGeoMapCopyrightNotice13setStyleSheetERK7QSt'
        'ring',
        styleSheet,
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
    'QDeclarativeGeoMapCopyrightNotice::QDeclarativeGeoMapCopyrightNotice(
    QQuickItem *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapcopyrightnotice.html

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QDeclarativeGeoMapCopyrightNotice::
    #      QDeclarativeGeoMapCopyrightNotice(QQuickItem *parent)
    self._noteCreation(
        QDeclarativeGeoMapCopyrightNotice, lambda: Rituals.call(
            'ritual_ZN33QDeclarativeGeoMapCopyrightNoticeC1EP10QQuickItem',
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

  def anchorToBottomLeft(self) -> None:
    """
    Calls Qt's 'void
    QDeclarativeGeoMapCopyrightNotice::anchorToBottomLeft()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapcopyrightnotice.html
    """
    #  void QDeclarativeGeoMapCopyrightNotice::anchorToBottomLeft()
    self.uglySide.call(
        'ritual_ZN33QDeclarativeGeoMapCopyrightNotice18anchorToBottomLeftEv',
    )

  def mapSource(self) -> Optional[QDeclarativeGeoMap]:
    """
    Calls Qt's 'QDeclarativeGeoMap
    *QDeclarativeGeoMapCopyrightNotice::mapSource()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapcopyrightnotice.html#mapSource

    Returns
    -------

    Optional[QDeclarativeGeoMap]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDeclarativeGeoMap *QDeclarativeGeoMapCopyrightNotice::mapSource()
    address = self.uglySide.call(
        'ritual_ZN33QDeclarativeGeoMapCopyrightNotice9mapSourceEv',
    )
    from . import QDeclarativeGeoMap
    return QDeclarativeGeoMap._cuteAt(address)

  @overload(QImage)
  def copyrightsImageChanged(self, copyrightsImage: QImage) -> None:
    """
    Calls Qt's 'void
    QDeclarativeGeoMapCopyrightNotice::copyrightsImageChanged(const QImage
    &copyrightsImage)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapcopyrightnotice.html

    Parameters
    ----------

    copyrightsImage : QImage
      Passed on as a value: Qt reads the C++ QImage, which stays Python's
      own.
    """
    #  void QDeclarativeGeoMapCopyrightNotice::copyrightsImageChanged(const
    #      QImage &copyrightsImage)
    self.uglySide.call(
        'ritual_ZN33QDeclarativeGeoMapCopyrightNotice22copyrightsImageChang'
        'edERK6QImage',
        self._valueOf(copyrightsImage),
    )

  @overload(str)
  def copyrightsChanged(self, copyrightsHtml: str) -> None:
    """
    Calls Qt's 'void
    QDeclarativeGeoMapCopyrightNotice::copyrightsChanged(const QString
    &copyrightsHtml)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapcopyrightnotice.html

    Parameters
    ----------

    copyrightsHtml : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDeclarativeGeoMapCopyrightNotice::copyrightsChanged(const
    #      QString &copyrightsHtml)
    self.uglySide.call(
        'ritual_ZN33QDeclarativeGeoMapCopyrightNotice17copyrightsChangedERK'
        '7QString',
        copyrightsHtml,
    )

  @overload(str)
  def onCopyrightsStyleSheetChanged(self, styleSheet: str) -> None:
    """
    Calls Qt's 'void
    QDeclarativeGeoMapCopyrightNotice::onCopyrightsStyleSheetChanged(const
    QString &styleSheet)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapcopyrightnotice.html

    Parameters
    ----------

    styleSheet : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDeclarativeGeoMapCopyrightNotice::onCopyrightsStyleSheetChanged(
    #      const QString &styleSheet)
    self.uglySide.call(
        'ritual_ZN33QDeclarativeGeoMapCopyrightNotice29onCopyrightsStyleShe'
        'etChangedERK7QString',
        styleSheet,
    )

  @overload(str)
  def linkActivated(self, link: str) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoMapCopyrightNotice::linkActivated(const
    QString &link)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapcopyrightnotice.html

    Parameters
    ----------

    link : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDeclarativeGeoMapCopyrightNotice::linkActivated(const QString
    #      &link)
    self.uglySide.call(
        'ritual_ZN33QDeclarativeGeoMapCopyrightNotice13linkActivatedERK7QSt'
        'ring',
        link,
    )

  def mapSourceChanged(self) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoMapCopyrightNotice::mapSourceChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapcopyrightnotice.html
    """
    #  void QDeclarativeGeoMapCopyrightNotice::mapSourceChanged()
    self.uglySide.call(
        'ritual_ZN33QDeclarativeGeoMapCopyrightNotice16mapSourceChangedEv',
    )

  @overload(QColor)
  def backgroundColorChanged(self, color: QColor) -> None:
    """
    Calls Qt's 'void
    QDeclarativeGeoMapCopyrightNotice::backgroundColorChanged(const QColor
    &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapcopyrightnotice.html

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QDeclarativeGeoMapCopyrightNotice::backgroundColorChanged(const
    #      QColor &color)
    self.uglySide.call(
        'ritual_ZN33QDeclarativeGeoMapCopyrightNotice22backgroundColorChang'
        'edERK6QColor',
        self._valueOf(color),
    )

  @overload(str)
  def styleSheetChanged(self, styleSheet: str) -> None:
    """
    Calls Qt's 'void
    QDeclarativeGeoMapCopyrightNotice::styleSheetChanged(const QString
    &styleSheet)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapcopyrightnotice.html

    Parameters
    ----------

    styleSheet : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDeclarativeGeoMapCopyrightNotice::styleSheetChanged(const
    #      QString &styleSheet)
    self.uglySide.call(
        'ritual_ZN33QDeclarativeGeoMapCopyrightNotice17styleSheetChangedERK'
        '7QString',
        styleSheet,
    )

  def copyrightsVisibleChanged(self) -> None:
    """
    Calls Qt's 'void
    QDeclarativeGeoMapCopyrightNotice::copyrightsVisibleChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapcopyrightnotice.html
    """
    #  void QDeclarativeGeoMapCopyrightNotice::copyrightsVisibleChanged()
    self.uglySide.call(
        'ritual_ZN33QDeclarativeGeoMapCopyrightNotice24copyrightsVisibleCha'
        'ngedEv',
    )

  @overload(QPainter)
  @overload(NoneType)
  def paint(self, painter: Optional[QPainter]) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoMapCopyrightNotice::paint(QPainter
    *painter)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapcopyrightnotice.html#paint

    Parameters
    ----------

    painter : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDeclarativeGeoMapCopyrightNotice::paint(QPainter *painter)
    ritual = 'ritual_ZN33QDeclarativeGeoMapCopyrightNotice5paintEP8QPainter'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN33QDeclarativeGeoMapCopyrightNotice5paintEP8QPainte'
          'r')
    self.uglySide.call(ritual, self._addressOf(painter))

  @overload(QMouseEvent)
  @overload(NoneType)
  def mousePressEvent(self, event: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void
    QDeclarativeGeoMapCopyrightNotice::mousePressEvent(QMouseEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapcopyrightnotice.html

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDeclarativeGeoMapCopyrightNotice::mousePressEvent(QMouseEvent
    #      *event)
    ritual = (
        'ritual_ZN33QDeclarativeGeoMapCopyrightNotice15mousePressEventEP11Q'
        'MouseEvent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN33QDeclarativeGeoMapCopyrightNotice15mousePressEven'
          'tEP11QMouseEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QMouseEvent)
  @overload(NoneType)
  def mouseReleaseEvent(self, event: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void
    QDeclarativeGeoMapCopyrightNotice::mouseReleaseEvent(QMouseEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapcopyrightnotice.html

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDeclarativeGeoMapCopyrightNotice::mouseReleaseEvent(QMouseEvent
    #      *event)
    ritual = (
        'ritual_ZN33QDeclarativeGeoMapCopyrightNotice17mouseReleaseEventEP1'
        '1QMouseEvent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN33QDeclarativeGeoMapCopyrightNotice17mouseReleaseEv'
          'entEP11QMouseEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  def rasterizeHtmlAndUpdate(self) -> None:
    """
    Calls Qt's 'void
    QDeclarativeGeoMapCopyrightNotice::rasterizeHtmlAndUpdate()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapcopyrightnotice.html
    """
    #  void QDeclarativeGeoMapCopyrightNotice::rasterizeHtmlAndUpdate()
    self.uglySide.call(
        'ritual_ZN33QDeclarativeGeoMapCopyrightNotice22rasterizeHtmlAndUpda'
        'teEv',
    )

  def connectMap(self) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoMapCopyrightNotice::connectMap()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapcopyrightnotice.html#connectMap
    """
    #  void QDeclarativeGeoMapCopyrightNotice::connectMap()
    self.uglySide.call(
        'ritual_ZN33QDeclarativeGeoMapCopyrightNotice10connectMapEv',
    )

  def createCopyright(self) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoMapCopyrightNotice::createCopyright()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapcopyrightnotice.html
    """
    #  void QDeclarativeGeoMapCopyrightNotice::createCopyright()
    self.uglySide.call(
        'ritual_ZN33QDeclarativeGeoMapCopyrightNotice15createCopyrightEv',
    )
