"""
QScatter3DSeries binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDataVisualization/qscatter3dseries.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject
from . import QAbstract3DSeries

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from . import QScatter3DSeriesPrivate, QScatterDataProxy
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QScatter3DSeriesPrivate = WAIT['QtDataVisualization:QScatter3DSeriesPrivate']
  QScatterDataProxy = WAIT['QtDataVisualization:QScatterDataProxy']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QScatter3DSeries(QAbstract3DSeries):
  """
  The cute side of Qt's QScatter3DSeries: a plain Python object standing in
  front of one C++ QScatter3DSeries.

  It is built on the cute 'QAbstract3DSeries', as Qt's QScatter3DSeries is
  built on Qt's QAbstract3DSeries, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QScatter3DSeries that has a ritual and that Python
  can call so far, 14 names in all: 'metaObject', 'tr', 'setDataProxy',
  'dataProxy', 'setSelectedItem', 'selectedItem', 'invalidSelectionIndex',
  'setItemSize', 'itemSize', 'dataProxyChanged', 'selectedItemChanged',
  'itemSizeChanged', 'dptr', 'dptrc'. It can be made from Python, in 3 ways;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QScatter3DSeries::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QScatter3DSeries::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QScatter3DSeries::~QScatter3DSeries()': the destructor: Python
    never removes a C++ QScatter3DSeries.

  What has no ritual
  ------------------

  4 of the 24 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QScatter3DSeries is created at the first use, not by
    'QScatter3DSeries(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QScatter3DSeries.
  - Qt tells when it has removed the C++ QScatter3DSeries. Every call on the
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
    Calls Qt's 'QString QScatter3DSeries::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qscatter3dseries.html#tr

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
    #  QString QScatter3DSeries::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN16QScatter3DSeries2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  def invalidSelectionIndex() -> int:
    """
    Calls Qt's 'int QScatter3DSeries::invalidSelectionIndex()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscatter3dseries.html#invalidSelectionIndex
    """
    #  int QScatter3DSeries::invalidSelectionIndex()
    return Rituals.call(
        'ritual_ZN16QScatter3DSeries21invalidSelectionIndexEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QScatter3DSeries'
  #  The part of Qt it is of, as another part has a class of its name too.
  __qt_part__ = 'QtDataVisualization'

  #  A C++ QScatter3DSeries Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QScatter3DSeries'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QScatter3DSeries::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qscatter3dseries.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QScatter3DSeries::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK16QScatter3DSeries10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def dataProxy(self) -> Optional[QScatterDataProxy]:
    """
    Calls Qt's 'QScatterDataProxy *QScatter3DSeries::dataProxy() const'.

    Qt's own words: https://doc.qt.io/qt-6/qscatter3dseries.html#dataProxy

    Returns
    -------

    Optional[QScatterDataProxy]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QScatterDataProxy *QScatter3DSeries::dataProxy() const
    address = self.uglySide.call('ritual_ZNK16QScatter3DSeries9dataProxyEv')
    from . import QScatterDataProxy
    return QScatterDataProxy._cuteAt(address)

  def selectedItem(self) -> int:
    """
    Calls Qt's 'int QScatter3DSeries::selectedItem() const'.

    Qt's own words: https://doc.qt.io/qt-6/qscatter3dseries.html#selectedItem
    """
    #  int QScatter3DSeries::selectedItem() const
    return self.uglySide.call('ritual_ZNK16QScatter3DSeries12selectedItemEv')

  def itemSize(self) -> float:
    """
    Calls Qt's 'float QScatter3DSeries::itemSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qscatter3dseries.html#itemSize
    """
    #  float QScatter3DSeries::itemSize() const
    return self.uglySide.call('ritual_ZNK16QScatter3DSeries8itemSizeEv')

  def dptrc(self) -> Optional[QScatter3DSeriesPrivate]:
    """
    Calls Qt's 'const QScatter3DSeriesPrivate *QScatter3DSeries::dptrc()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qscatter3dseries.html#dptrc

    Returns
    -------

    Optional[QScatter3DSeriesPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QScatter3DSeriesPrivate *QScatter3DSeries::dptrc() const
    address = self.uglySide.call('ritual_ZNK16QScatter3DSeries5dptrcEv')
    from . import QScatter3DSeriesPrivate
    return QScatter3DSeriesPrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QScatterDataProxy)
  @overload(NoneType)
  def setDataProxy(self, proxy: Optional[QScatterDataProxy]) -> None:
    """
    Calls Qt's 'void QScatter3DSeries::setDataProxy(QScatterDataProxy
    *proxy)'.

    Qt's own words: https://doc.qt.io/qt-6/qscatter3dseries.html#setDataProxy

    Parameters
    ----------

    proxy : Optional[QScatterDataProxy]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QScatter3DSeries::setDataProxy(QScatterDataProxy *proxy)
    self.uglySide.call(
        'ritual_ZN16QScatter3DSeries12setDataProxyEP17QScatterDataProxy',
        self._addressOf(proxy),
    )

  @overload(int)
  def setSelectedItem(self, index: int) -> None:
    """
    Calls Qt's 'void QScatter3DSeries::setSelectedItem(int index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscatter3dseries.html#setSelectedItem

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QScatter3DSeries::setSelectedItem(int index)
    self.uglySide.call(
        'ritual_ZN16QScatter3DSeries15setSelectedItemEi', index,
    )

  @overload(float)
  def setItemSize(self, size: float) -> None:
    """
    Calls Qt's 'void QScatter3DSeries::setItemSize(float size)'.

    Qt's own words: https://doc.qt.io/qt-6/qscatter3dseries.html#setItemSize

    Parameters
    ----------

    size : float
      Passed on as it is.
    """
    #  void QScatter3DSeries::setItemSize(float size)
    self.uglySide.call('ritual_ZN16QScatter3DSeries11setItemSizeEf', size)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QScatterDataProxy)
  @overload(QScatterDataProxy, QObject)
  @overload(QScatterDataProxy, NoneType)
  @overload(NoneType, QObject)
  @overload(NoneType, NoneType)
  def __init__(
      self,
      dataProxy: Optional[QScatterDataProxy],
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QScatter3DSeries::QScatter3DSeries(QScatterDataProxy *dataProxy, QObject
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qscatter3dseries.html#QScatter3DSeries

    Parameters
    ----------

    dataProxy : Optional[QScatterDataProxy]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QScatter3DSeries::QScatter3DSeries(QScatterDataProxy *dataProxy,
    #      QObject *parent)
    self._noteCreation(QScatter3DSeries, lambda: Rituals.call(
        'ritual_ZN16QScatter3DSeriesC1EP17QScatterDataProxyP7QObject',
        self._addressOf(dataProxy), self._addressOf(parent, 'QObject'),
    ))

  @overload(QScatter3DSeriesPrivate)
  @overload(QScatter3DSeriesPrivate, QObject)
  @overload(QScatter3DSeriesPrivate, NoneType)
  def __init__(
      self,
      d: Optional[QScatter3DSeriesPrivate],
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QScatter3DSeries::QScatter3DSeries(QScatter3DSeriesPrivate *d, QObject
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qscatter3dseries.html#QScatter3DSeries

    Parameters
    ----------

    d : Optional[QScatter3DSeriesPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QScatter3DSeries::QScatter3DSeries(QScatter3DSeriesPrivate *d, QObject
    #      *parent)
    self._noteCreation(QScatter3DSeries, lambda: Rituals.call(
        'ritual_ZN16QScatter3DSeriesC1EP23QScatter3DSeriesPrivateP7QObject',
        self._addressOf(d), self._addressOf(parent, 'QObject'),
    ))

  @overload()
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QScatter3DSeries::QScatter3DSeries(QObject *parent)', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qscatter3dseries.html#QScatter3DSeries

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QScatter3DSeries::QScatter3DSeries(QObject *parent)
    self._noteCreation(QScatter3DSeries, lambda: Rituals.call(
        'ritual_ZN16QScatter3DSeriesC1EP7QObject',
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

  @overload(QScatterDataProxy)
  @overload(NoneType)
  def dataProxyChanged(self, proxy: Optional[QScatterDataProxy]) -> None:
    """
    Calls Qt's 'void QScatter3DSeries::dataProxyChanged(QScatterDataProxy
    *proxy)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscatter3dseries.html#dataProxyChanged

    Parameters
    ----------

    proxy : Optional[QScatterDataProxy]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QScatter3DSeries::dataProxyChanged(QScatterDataProxy *proxy)
    self.uglySide.call(
        'ritual_ZN16QScatter3DSeries16dataProxyChangedEP17QScatterDataProxy',
        self._addressOf(proxy),
    )

  @overload(int)
  def selectedItemChanged(self, index: int) -> None:
    """
    Calls Qt's 'void QScatter3DSeries::selectedItemChanged(int index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscatter3dseries.html#selectedItemChanged

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QScatter3DSeries::selectedItemChanged(int index)
    self.uglySide.call(
        'ritual_ZN16QScatter3DSeries19selectedItemChangedEi', index,
    )

  @overload(float)
  def itemSizeChanged(self, size: float) -> None:
    """
    Calls Qt's 'void QScatter3DSeries::itemSizeChanged(float size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscatter3dseries.html#itemSizeChanged

    Parameters
    ----------

    size : float
      Passed on as it is.
    """
    #  void QScatter3DSeries::itemSizeChanged(float size)
    self.uglySide.call(
        'ritual_ZN16QScatter3DSeries15itemSizeChangedEf', size,
    )

  def dptr(self) -> Optional[QScatter3DSeriesPrivate]:
    """
    Calls Qt's 'QScatter3DSeriesPrivate *QScatter3DSeries::dptr()'.

    Qt's own words: https://doc.qt.io/qt-6/qscatter3dseries.html#dptr

    Returns
    -------

    Optional[QScatter3DSeriesPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QScatter3DSeriesPrivate *QScatter3DSeries::dptr()
    address = self.uglySide.call('ritual_ZN16QScatter3DSeries4dptrEv')
    from . import QScatter3DSeriesPrivate
    return QScatter3DSeriesPrivate._cuteAt(address)


#  Qt's 'QList<QScatter3DSeries *>': the list of QScatter3DSeries, which
#  'QList[QScatter3DSeries]' gives. It is made here, so that there is one as
#  soon as there can be a QScatter3DSeries.
QList.createKind(
    QScatter3DSeries, 'address',
    make='ritual_list_make_QScatter3DSeries_ptr',
    add='ritual_list_add_QScatter3DSeries_ptr',
    size='ritual_list_size_QScatter3DSeries_ptr',
    at='ritual_list_at_QScatter3DSeries_ptr',
    drop='ritual_list_drop_QScatter3DSeries_ptr',
)
