"""
QBar3DSeries binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDataVisualization/qbar3dseries.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject
from . import QAbstract3DSeries

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QPoint
  from ..QtGui import QColor
  from . import QBar3DSeriesPrivate, QBarDataProxy
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QBarDataProxy = WAIT['QtDataVisualization:QBarDataProxy']
  QColor = WAIT['QColor']
  QPoint = WAIT['QPoint']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QBar3DSeries(QAbstract3DSeries):
  """
  The cute side of Qt's QBar3DSeries: a plain Python object standing in front
  of one C++ QBar3DSeries.

  It is built on the cute 'QAbstract3DSeries', as Qt's QBar3DSeries is built
  on Qt's QAbstract3DSeries, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QBar3DSeries that has a ritual and that Python can
  call so far, 17 names in all: 'metaObject', 'tr', 'setDataProxy',
  'dataProxy', 'setSelectedBar', 'selectedBar', 'invalidSelectionPosition',
  'setMeshAngle', 'meshAngle', 'rowColors', 'setRowColors',
  'dataProxyChanged', 'selectedBarChanged', 'meshAngleChanged',
  'rowColorsChanged', 'dptr', 'dptrc'. It can be made from Python, in 2 ways;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QBar3DSeries::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QBar3DSeries::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QBar3DSeries::~QBar3DSeries()': the destructor: Python never
    removes a C++ QBar3DSeries.

  What has no ritual
  ------------------

  4 of the 26 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QBar3DSeries is created at the first use, not by
    'QBar3DSeries(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QBar3DSeries.
  - Qt tells when it has removed the C++ QBar3DSeries. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
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
    Calls Qt's 'QString QBar3DSeries::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qbar3dseries.html#tr

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
    #  QString QBar3DSeries::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN12QBar3DSeries2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  def invalidSelectionPosition() -> QPoint:
    """
    Calls Qt's 'QPoint QBar3DSeries::invalidSelectionPosition()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbar3dseries.html#invalidSelectionPosition

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint QBar3DSeries::invalidSelectionPosition()
    address = Rituals.call(
        'ritual_ZN12QBar3DSeries24invalidSelectionPositionEv',
    )
    from ..QtCore import QPoint
    return QPoint._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QBar3DSeries'
  #  The part of Qt it is of, as another part has a class of its name too.
  __qt_part__ = 'QtDataVisualization'

  #  A C++ QBar3DSeries Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QBar3DSeries'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QBar3DSeries::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbar3dseries.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QBar3DSeries::metaObject() const
    address = self.uglySide.call('ritual_ZNK12QBar3DSeries10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def dataProxy(self) -> Optional[QBarDataProxy]:
    """
    Calls Qt's 'QBarDataProxy *QBar3DSeries::dataProxy() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbar3dseries.html#dataProxy

    Returns
    -------

    Optional[QBarDataProxy]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QBarDataProxy *QBar3DSeries::dataProxy() const
    address = self.uglySide.call('ritual_ZNK12QBar3DSeries9dataProxyEv')
    from . import QBarDataProxy
    return QBarDataProxy._cuteAt(address)

  def selectedBar(self) -> QPoint:
    """
    Calls Qt's 'QPoint QBar3DSeries::selectedBar() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbar3dseries.html#selectedBar

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint QBar3DSeries::selectedBar() const
    address = self.uglySide.call('ritual_ZNK12QBar3DSeries11selectedBarEv')
    from ..QtCore import QPoint
    return QPoint._cuteOwning(address)

  def meshAngle(self) -> float:
    """
    Calls Qt's 'float QBar3DSeries::meshAngle() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbar3dseries.html#meshAngle
    """
    #  float QBar3DSeries::meshAngle() const
    return self.uglySide.call('ritual_ZNK12QBar3DSeries9meshAngleEv')

  def rowColors(self) -> QList[QColor]:
    """
    Calls Qt's 'QList<QColor> QBar3DSeries::rowColors() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbar3dseries.html#rowColors

    Returns
    -------

    QList[QColor]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QColor> QBar3DSeries::rowColors() const
    address = self.uglySide.call('ritual_ZNK12QBar3DSeries9rowColorsEv')
    from ..QtGui import QColor
    return QList[QColor]._cuteOwning(address)

  def dptrc(self) -> Optional[QBar3DSeriesPrivate]:
    """
    Calls Qt's 'const QBar3DSeriesPrivate *QBar3DSeries::dptrc() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbar3dseries.html#dptrc

    Returns
    -------

    Optional[QBar3DSeriesPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QBar3DSeriesPrivate *QBar3DSeries::dptrc() const
    address = self.uglySide.call('ritual_ZNK12QBar3DSeries5dptrcEv')
    from . import QBar3DSeriesPrivate
    return QBar3DSeriesPrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QBarDataProxy)
  @overload(NoneType)
  def setDataProxy(self, proxy: Optional[QBarDataProxy]) -> None:
    """
    Calls Qt's 'void QBar3DSeries::setDataProxy(QBarDataProxy *proxy)'.

    Qt's own words: https://doc.qt.io/qt-6/qbar3dseries.html#setDataProxy

    Parameters
    ----------

    proxy : Optional[QBarDataProxy]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QBar3DSeries::setDataProxy(QBarDataProxy *proxy)
    self.uglySide.call(
        'ritual_ZN12QBar3DSeries12setDataProxyEP13QBarDataProxy',
        self._addressOf(proxy),
    )

  @overload(QPoint)
  def setSelectedBar(self, position: QPoint) -> None:
    """
    Calls Qt's 'void QBar3DSeries::setSelectedBar(const QPoint &position)'.

    Qt's own words: https://doc.qt.io/qt-6/qbar3dseries.html#setSelectedBar

    Parameters
    ----------

    position : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void QBar3DSeries::setSelectedBar(const QPoint &position)
    self.uglySide.call(
        'ritual_ZN12QBar3DSeries14setSelectedBarERK6QPoint',
        self._valueOf(position),
    )

  @overload(float)
  def setMeshAngle(self, angle: float) -> None:
    """
    Calls Qt's 'void QBar3DSeries::setMeshAngle(float angle)'.

    Qt's own words: https://doc.qt.io/qt-6/qbar3dseries.html#setMeshAngle

    Parameters
    ----------

    angle : float
      Passed on as it is.
    """
    #  void QBar3DSeries::setMeshAngle(float angle)
    self.uglySide.call('ritual_ZN12QBar3DSeries12setMeshAngleEf', angle)

  @overload(QList[QColor])
  def setRowColors(self, colors: QList[QColor]) -> None:
    """
    Calls Qt's 'void QBar3DSeries::setRowColors(const QList<QColor>
    &colors)'.

    Qt's own words: https://doc.qt.io/qt-6/qbar3dseries.html#setRowColors

    Parameters
    ----------

    colors : QList[QColor]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QBar3DSeries::setRowColors(const QList<QColor> &colors)
    self.uglySide.call(
        'ritual_ZN12QBar3DSeries12setRowColorsERK5QListI6QColorE',
        self._valueOf(colors),
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

  @overload(QBarDataProxy)
  @overload(QBarDataProxy, QObject)
  @overload(QBarDataProxy, NoneType)
  @overload(NoneType, QObject)
  @overload(NoneType, NoneType)
  def __init__(
      self,
      dataProxy: Optional[QBarDataProxy],
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'QBar3DSeries::QBar3DSeries(QBarDataProxy
    *dataProxy, QObject *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qbar3dseries.html#QBar3DSeries

    Parameters
    ----------

    dataProxy : Optional[QBarDataProxy]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QBar3DSeries::QBar3DSeries(QBarDataProxy *dataProxy, QObject *parent)
    self._noteCreation(QBar3DSeries, lambda: Rituals.call(
        'ritual_ZN12QBar3DSeriesC1EP13QBarDataProxyP7QObject',
        self._addressOf(dataProxy), self._addressOf(parent, 'QObject'),
    ))

  @overload()
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's 'QBar3DSeries::QBar3DSeries(QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qbar3dseries.html#QBar3DSeries

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QBar3DSeries::QBar3DSeries(QObject *parent)
    self._noteCreation(QBar3DSeries, lambda: Rituals.call(
        'ritual_ZN12QBar3DSeriesC1EP7QObject',
        self._addressOf(parent, 'QObject'),
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

  @overload(QBarDataProxy)
  @overload(NoneType)
  def dataProxyChanged(self, proxy: Optional[QBarDataProxy]) -> None:
    """
    Calls Qt's 'void QBar3DSeries::dataProxyChanged(QBarDataProxy *proxy)'.

    Qt's own words: https://doc.qt.io/qt-6/qbar3dseries.html#dataProxyChanged

    Parameters
    ----------

    proxy : Optional[QBarDataProxy]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QBar3DSeries::dataProxyChanged(QBarDataProxy *proxy)
    self.uglySide.call(
        'ritual_ZN12QBar3DSeries16dataProxyChangedEP13QBarDataProxy',
        self._addressOf(proxy),
    )

  @overload(QPoint)
  def selectedBarChanged(self, position: QPoint) -> None:
    """
    Calls Qt's 'void QBar3DSeries::selectedBarChanged(const QPoint
    &position)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbar3dseries.html#selectedBarChanged

    Parameters
    ----------

    position : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void QBar3DSeries::selectedBarChanged(const QPoint &position)
    self.uglySide.call(
        'ritual_ZN12QBar3DSeries18selectedBarChangedERK6QPoint',
        self._valueOf(position),
    )

  @overload(float)
  def meshAngleChanged(self, angle: float) -> None:
    """
    Calls Qt's 'void QBar3DSeries::meshAngleChanged(float angle)'.

    Qt's own words: https://doc.qt.io/qt-6/qbar3dseries.html#meshAngleChanged

    Parameters
    ----------

    angle : float
      Passed on as it is.
    """
    #  void QBar3DSeries::meshAngleChanged(float angle)
    self.uglySide.call('ritual_ZN12QBar3DSeries16meshAngleChangedEf', angle)

  @overload(QList[QColor])
  def rowColorsChanged(self, rowcolors: QList[QColor]) -> None:
    """
    Calls Qt's 'void QBar3DSeries::rowColorsChanged(const QList<QColor>
    &rowcolors)'.

    Qt's own words: https://doc.qt.io/qt-6/qbar3dseries.html#rowColorsChanged

    Parameters
    ----------

    rowcolors : QList[QColor]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QBar3DSeries::rowColorsChanged(const QList<QColor> &rowcolors)
    self.uglySide.call(
        'ritual_ZN12QBar3DSeries16rowColorsChangedERK5QListI6QColorE',
        self._valueOf(rowcolors),
    )

  def dptr(self) -> Optional[QBar3DSeriesPrivate]:
    """
    Calls Qt's 'QBar3DSeriesPrivate *QBar3DSeries::dptr()'.

    Qt's own words: https://doc.qt.io/qt-6/qbar3dseries.html#dptr

    Returns
    -------

    Optional[QBar3DSeriesPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QBar3DSeriesPrivate *QBar3DSeries::dptr()
    address = self.uglySide.call('ritual_ZN12QBar3DSeries4dptrEv')
    from . import QBar3DSeriesPrivate
    return QBar3DSeriesPrivate._cuteAt(address)


#  Qt's 'QList<QBar3DSeries *>': the list of QBar3DSeries, which
#  'QList[QBar3DSeries]' gives. It is made here, so that there is one as soon
#  as there can be a QBar3DSeries.
QList.createKind(
    QBar3DSeries, 'address',
    make='ritual_list_make_QBar3DSeries_ptr',
    add='ritual_list_add_QBar3DSeries_ptr',
    size='ritual_list_size_QBar3DSeries_ptr',
    at='ritual_list_at_QBar3DSeries_ptr',
    drop='ritual_list_drop_QBar3DSeries_ptr',
)
