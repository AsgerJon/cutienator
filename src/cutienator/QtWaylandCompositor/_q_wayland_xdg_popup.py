"""
QWaylandXdgPopup binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWaylandCompositor/qwaylandxdgshell.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QPoint, QRect, QSize
  from . import QWaylandSurfaceRole, QWaylandXdgSurface
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRect = WAIT['QRect']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QWaylandXdgPopup(QObject):
  """
  The cute side of Qt's QWaylandXdgPopup: a plain Python object standing in
  front of one C++ QWaylandXdgPopup.

  It is built on the cute 'QObject', as Qt's QWaylandXdgPopup is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QWaylandXdgPopup that has a ritual and that Python
  can call so far, 18 names in all: 'metaObject', 'tr', 'xdgSurface',
  'parentXdgSurface', 'configuredGeometry', 'anchorRect', 'anchorEdges',
  'gravityEdges', 'slideConstraints', 'flipConstraints', 'resizeConstraints',
  'offset', 'positionerSize', 'unconstrainedPosition', 'sendConfigure',
  'sendPopupDone', 'role', 'configuredGeometryChanged'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QWaylandXdgPopup::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QWaylandXdgPopup::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QWaylandXdgPopupPrivate *QWaylandXdgPopup::d_func()': gives
    'QWaylandXdgPopupPrivate', which has no cute class yet.
  - Qt's 'const QWaylandXdgPopupPrivate *QWaylandXdgPopup::d_func() const':
    gives 'QWaylandXdgPopupPrivate', which has no cute class yet.
  - Qt's 'QWaylandXdgPopup::QWaylandXdgPopup(QWaylandXdgSurface *xdgSurface,
    QWaylandXdgSurface *parentXdgSurface, QWaylandXdgPositioner *positioner,
    QWaylandResource &resource)': names 'QWaylandXdgPositioner', which has no
    cute class yet.

  What has no ritual
  ------------------

  2 of the 25 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QWaylandXdgPopup is created at the first use, not by
    'QWaylandXdgPopup(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QWaylandXdgPopup.
  - Qt tells when it has removed the C++ QWaylandXdgPopup. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QWaylandXdgPopup that has no cute function yet,
    '__init__', holds a function that raises 'NotImplementedError', and its
    docstring says why.
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
    Calls Qt's 'QString QWaylandXdgPopup::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandxdgpopup.html#tr

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
    #  QString QWaylandXdgPopup::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN16QWaylandXdgPopup2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  def role() -> Optional[QWaylandSurfaceRole]:
    """
    Calls Qt's 'QWaylandSurfaceRole *QWaylandXdgPopup::role()'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandxdgpopup.html#role

    Returns
    -------

    Optional[QWaylandSurfaceRole]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWaylandSurfaceRole *QWaylandXdgPopup::role()
    address = Rituals.call('ritual_ZN16QWaylandXdgPopup4roleEv')
    from . import QWaylandSurfaceRole
    return QWaylandSurfaceRole._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWaylandXdgPopup'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QWaylandXdgPopup::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandxdgpopup.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QWaylandXdgPopup::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK16QWaylandXdgPopup10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def xdgSurface(self) -> Optional[QWaylandXdgSurface]:
    """
    Calls Qt's 'QWaylandXdgSurface *QWaylandXdgPopup::xdgSurface() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandxdgpopup.html#xdgSurface

    Returns
    -------

    Optional[QWaylandXdgSurface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWaylandXdgSurface *QWaylandXdgPopup::xdgSurface() const
    address = self.uglySide.call(
        'ritual_ZNK16QWaylandXdgPopup10xdgSurfaceEv',
    )
    from . import QWaylandXdgSurface
    return QWaylandXdgSurface._cuteAt(address)

  def parentXdgSurface(self) -> Optional[QWaylandXdgSurface]:
    """
    Calls Qt's 'QWaylandXdgSurface *QWaylandXdgPopup::parentXdgSurface()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandxdgpopup.html#parentXdgSurface

    Returns
    -------

    Optional[QWaylandXdgSurface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWaylandXdgSurface *QWaylandXdgPopup::parentXdgSurface() const
    address = self.uglySide.call(
        'ritual_ZNK16QWaylandXdgPopup16parentXdgSurfaceEv',
    )
    from . import QWaylandXdgSurface
    return QWaylandXdgSurface._cuteAt(address)

  def configuredGeometry(self) -> QRect:
    """
    Calls Qt's 'QRect QWaylandXdgPopup::configuredGeometry() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandxdgpopup.html#configuredGeometry

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QWaylandXdgPopup::configuredGeometry() const
    address = self.uglySide.call(
        'ritual_ZNK16QWaylandXdgPopup18configuredGeometryEv',
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  def anchorRect(self) -> QRect:
    """
    Calls Qt's 'QRect QWaylandXdgPopup::anchorRect() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandxdgpopup.html#anchorRect

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QWaylandXdgPopup::anchorRect() const
    address = self.uglySide.call(
        'ritual_ZNK16QWaylandXdgPopup10anchorRectEv',
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  def anchorEdges(self) -> Qt.Edges:
    """
    Calls Qt's 'Qt::Edges QWaylandXdgPopup::anchorEdges() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandxdgpopup.html#anchorEdges

    Returns
    -------

    Qt.Edges
      The value standing for the combination Qt gave back.
    """
    #  Qt::Edges QWaylandXdgPopup::anchorEdges() const
    return Qt.Edges(self.uglySide.call(
        'ritual_ZNK16QWaylandXdgPopup11anchorEdgesEv',
    ))

  def gravityEdges(self) -> Qt.Edges:
    """
    Calls Qt's 'Qt::Edges QWaylandXdgPopup::gravityEdges() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandxdgpopup.html#gravityEdges

    Returns
    -------

    Qt.Edges
      The value standing for the combination Qt gave back.
    """
    #  Qt::Edges QWaylandXdgPopup::gravityEdges() const
    return Qt.Edges(self.uglySide.call(
        'ritual_ZNK16QWaylandXdgPopup12gravityEdgesEv',
    ))

  def slideConstraints(self) -> Qt.Orientations:
    """
    Calls Qt's 'Qt::Orientations QWaylandXdgPopup::slideConstraints() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandxdgpopup.html#slideConstraints

    Returns
    -------

    Qt.Orientations
      The value standing for the combination Qt gave back.
    """
    #  Qt::Orientations QWaylandXdgPopup::slideConstraints() const
    return Qt.Orientations(self.uglySide.call(
        'ritual_ZNK16QWaylandXdgPopup16slideConstraintsEv',
    ))

  def flipConstraints(self) -> Qt.Orientations:
    """
    Calls Qt's 'Qt::Orientations QWaylandXdgPopup::flipConstraints() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandxdgpopup.html#flipConstraints

    Returns
    -------

    Qt.Orientations
      The value standing for the combination Qt gave back.
    """
    #  Qt::Orientations QWaylandXdgPopup::flipConstraints() const
    return Qt.Orientations(self.uglySide.call(
        'ritual_ZNK16QWaylandXdgPopup15flipConstraintsEv',
    ))

  def resizeConstraints(self) -> Qt.Orientations:
    """
    Calls Qt's 'Qt::Orientations QWaylandXdgPopup::resizeConstraints()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandxdgpopup.html#resizeConstraints

    Returns
    -------

    Qt.Orientations
      The value standing for the combination Qt gave back.
    """
    #  Qt::Orientations QWaylandXdgPopup::resizeConstraints() const
    return Qt.Orientations(self.uglySide.call(
        'ritual_ZNK16QWaylandXdgPopup17resizeConstraintsEv',
    ))

  def offset(self) -> QPoint:
    """
    Calls Qt's 'QPoint QWaylandXdgPopup::offset() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandxdgpopup.html#offset

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint QWaylandXdgPopup::offset() const
    address = self.uglySide.call('ritual_ZNK16QWaylandXdgPopup6offsetEv')
    from ..QtCore import QPoint
    return QPoint._cuteOwning(address)

  def positionerSize(self) -> QSize:
    """
    Calls Qt's 'QSize QWaylandXdgPopup::positionerSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandxdgpopup.html#positionerSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QWaylandXdgPopup::positionerSize() const
    address = self.uglySide.call(
        'ritual_ZNK16QWaylandXdgPopup14positionerSizeEv',
    )
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def unconstrainedPosition(self) -> QPoint:
    """
    Calls Qt's 'QPoint QWaylandXdgPopup::unconstrainedPosition() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandxdgpopup.html#unconstrainedPosition

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint QWaylandXdgPopup::unconstrainedPosition() const
    address = self.uglySide.call(
        'ritual_ZNK16QWaylandXdgPopup21unconstrainedPositionEv',
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
    Qt's 'QWaylandXdgPopup::QWaylandXdgPopup(QWaylandXdgSurface *xdgSurface,
    QWaylandXdgSurface *parentXdgSurface, QWaylandXdgPositioner *positioner,
    QWaylandResource &resource)': names 'QWaylandXdgPositioner', which has no
    cute class yet.
    """
    raise NotImplementedError(
        "'QWaylandXdgPopup.__init__' has no cute function yet. Qt's "
        "'QWaylandXdgPopup::QWaylandXdgPopup(QWaylandXdgSurface "
        "*xdgSurface, QWaylandXdgSurface *parentXdgSurface, "
        "QWaylandXdgPositioner *positioner, QWaylandResource &resource)': "
        "names 'QWaylandXdgPositioner', which has no cute class yet.")

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

  @overload(QRect)
  def sendConfigure(self, geometry: QRect) -> int:
    """
    Calls Qt's 'uint QWaylandXdgPopup::sendConfigure(const QRect &geometry)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandxdgpopup.html#sendConfigure

    Parameters
    ----------

    geometry : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
    """
    #  uint QWaylandXdgPopup::sendConfigure(const QRect &geometry)
    return self.uglySide.call(
        'ritual_ZN16QWaylandXdgPopup13sendConfigureERK5QRect',
        self._valueOf(geometry),
    )

  def sendPopupDone(self) -> None:
    """
    Calls Qt's 'void QWaylandXdgPopup::sendPopupDone()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandxdgpopup.html#sendPopupDone
    """
    #  void QWaylandXdgPopup::sendPopupDone()
    self.uglySide.call('ritual_ZN16QWaylandXdgPopup13sendPopupDoneEv')

  def configuredGeometryChanged(self) -> None:
    """
    Calls Qt's 'void QWaylandXdgPopup::configuredGeometryChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandxdgpopup.html#configuredGeometryChanged
    """
    #  void QWaylandXdgPopup::configuredGeometryChanged()
    self.uglySide.call(
        'ritual_ZN16QWaylandXdgPopup25configuredGeometryChangedEv',
    )
