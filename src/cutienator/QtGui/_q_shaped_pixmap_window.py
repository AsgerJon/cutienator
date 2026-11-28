"""
QShapedPixmapWindow binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qshapedpixmapdndwindow_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QShapedPixmapWindow to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from . import QRasterWindow

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QPoint
  from . import QPaintEvent, QPixmap
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPaintEvent = WAIT['QPaintEvent']
  QPixmap = WAIT['QPixmap']
  QPoint = WAIT['QPoint']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QShapedPixmapWindow(QRasterWindow):
  """
  The cute side of Qt's QShapedPixmapWindow: a plain Python object standing
  in front of one C++ QShapedPixmapWindow.

  It is built on the cute 'QRasterWindow', as Qt's QShapedPixmapWindow is
  built on Qt's QRasterWindow, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QShapedPixmapWindow that has a ritual and that
  Python can call so far, 6 names in all: 'metaObject', 'setUseCompositing',
  'setPixmap', 'setHotspot', 'updateGeometry', 'paintEvent'. None can be made
  from Python: one comes out of a function of another class that gives one
  back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QShapedPixmapWindow::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QShapedPixmapWindow::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QShapedPixmapWindow::~QShapedPixmapWindow()': the destructor:
    Python never removes a C++ QShapedPixmapWindow.

  What has no ritual
  ------------------

  4 of the 13 functions Qt declares: 2 not a gap; 2 leans on
  'QShapedPixmapWindow.

  What to expect
  --------------

  - The C++ QShapedPixmapWindow is created at the first use, not by
    'QShapedPixmapWindow(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QShapedPixmapWindow.
  - Qt tells when it has removed the C++ QShapedPixmapWindow. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QShapedPixmapWindow that has no cute function yet,
    '__init__', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QShapedPixmapWindow'

  #  A C++ QShapedPixmapWindow Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QShapedPixmapWindow'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QShapedPixmapWindow::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qshapedpixmapwindow.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QShapedPixmapWindow::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK19QShapedPixmapWindow10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setUseCompositing(self, on: bool) -> None:
    """
    Calls Qt's 'void QShapedPixmapWindow::setUseCompositing(bool on)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qshapedpixmapwindow.html#setUseCompositing

    Parameters
    ----------

    on : bool
      Passed on as it is.
    """
    #  void QShapedPixmapWindow::setUseCompositing(bool on)
    self.uglySide.call(
        'ritual_ZN19QShapedPixmapWindow17setUseCompositingEb', on,
    )

  @overload(QPixmap)
  def setPixmap(self, pixmap: QPixmap) -> None:
    """
    Calls Qt's 'void QShapedPixmapWindow::setPixmap(const QPixmap &pixmap)'.

    Qt's own words: https://doc.qt.io/qt-6/qshapedpixmapwindow.html#setPixmap

    Parameters
    ----------

    pixmap : QPixmap
      Passed on as a value: Qt reads the C++ QPixmap, which stays Python's
      own.
    """
    #  void QShapedPixmapWindow::setPixmap(const QPixmap &pixmap)
    self.uglySide.call(
        'ritual_ZN19QShapedPixmapWindow9setPixmapERK7QPixmap',
        self._valueOf(pixmap),
    )

  @overload(QPoint)
  def setHotspot(self, hotspot: QPoint) -> None:
    """
    Calls Qt's 'void QShapedPixmapWindow::setHotspot(const QPoint &hotspot)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qshapedpixmapwindow.html#setHotspot

    Parameters
    ----------

    hotspot : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void QShapedPixmapWindow::setHotspot(const QPoint &hotspot)
    self.uglySide.call(
        'ritual_ZN19QShapedPixmapWindow10setHotspotERK6QPoint',
        self._valueOf(hotspot),
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QShapedPixmapWindow::QShapedPixmapWindow(QScreen *screen)': leans
    on 'QShapedPixmapWindow::qt_metacall(QMetaObject::Call, int, void**)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QShapedPixmapWindow.__init__' has no cute function yet. Qt's "
        "'QShapedPixmapWindow::QShapedPixmapWindow(QScreen *screen)': leans "
        "on 'QShapedPixmapWindow::qt_metacall(QMetaObject::Call, int, "
        "void**)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

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

  @overload(QPoint)
  def updateGeometry(self, pos: QPoint) -> None:
    """
    Calls Qt's 'void QShapedPixmapWindow::updateGeometry(const QPoint &pos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qshapedpixmapwindow.html#updateGeometry

    Parameters
    ----------

    pos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void QShapedPixmapWindow::updateGeometry(const QPoint &pos)
    self.uglySide.call(
        'ritual_ZN19QShapedPixmapWindow14updateGeometryERK6QPoint',
        self._valueOf(pos),
    )

  @overload(QPaintEvent)
  @overload(NoneType)
  def paintEvent(self, a0: Optional[QPaintEvent]) -> None:
    """
    Calls Qt's 'void QShapedPixmapWindow::paintEvent(QPaintEvent *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qshapedpixmapwindow.html#paintEvent

    Parameters
    ----------

    a0 : Optional[QPaintEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QShapedPixmapWindow::paintEvent(QPaintEvent *a0)
    ritual = 'ritual_ZN19QShapedPixmapWindow10paintEventEP11QPaintEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QShapedPixmapWindow10paintEventEP11QPaintEvent')
    self.uglySide.call(ritual, self._addressOf(a0))
