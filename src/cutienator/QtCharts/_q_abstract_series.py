"""
QAbstractSeries binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCharts/qabstractseries.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from . import QAbstractAxis, QChart
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAbstractAxis = WAIT['QtCharts:QAbstractAxis']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAbstractSeries(QObject):
  """
  The cute side of Qt's QAbstractSeries: a plain Python object standing in
  front of one C++ QAbstractSeries.

  It is built on the cute 'QObject', as Qt's QAbstractSeries is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QAbstractSeries that has a ritual and that Python
  can call so far, 21 names in all: 'metaObject', 'tr', 'type', 'setName',
  'name', 'setVisible', 'isVisible', 'opacity', 'setOpacity', 'setUseOpenGL',
  'useOpenGL', 'chart', 'attachAxis', 'detachAxis', 'attachedAxes', 'show',
  'hide', 'nameChanged', 'visibleChanged', 'opacityChanged',
  'useOpenGLChanged'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QAbstractSeries::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QAbstractSeries::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QAbstractSeries::QAbstractSeries(QAbstractSeriesPrivate &d, QObject
    *parent)': takes a type Python has no way to hand over yet.
  - Qt's 'QAbstractSeries::~QAbstractSeries()': the destructor: Python never
    removes a C++ QAbstractSeries.

  What has no ritual
  ------------------

  2 of the 27 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QAbstractSeries is created at the first use, not by
    'QAbstractSeries(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAbstractSeries.
  - Qt tells when it has removed the C++ QAbstractSeries. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QAbstractSeries that has no cute function yet,
    '__init__', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  #  The enums Qt writes inside QAbstractSeries, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class SeriesType(CuteNum):
    """
    The enum 'QAbstractSeries::SeriesType' of Qt, with the 13 names Qt gives
    in it.
    """

    SeriesTypeLine = Kee[int](0)
    SeriesTypeArea = Kee[int](1)
    SeriesTypeBar = Kee[int](2)
    SeriesTypeStackedBar = Kee[int](3)
    SeriesTypePercentBar = Kee[int](4)
    SeriesTypePie = Kee[int](5)
    SeriesTypeScatter = Kee[int](6)
    SeriesTypeSpline = Kee[int](7)
    SeriesTypeHorizontalBar = Kee[int](8)
    SeriesTypeHorizontalStackedBar = Kee[int](9)
    SeriesTypeHorizontalPercentBar = Kee[int](10)
    SeriesTypeBoxPlot = Kee[int](11)
    SeriesTypeCandlestick = Kee[int](12)

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
    Calls Qt's 'QString QAbstractSeries::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractseries.html#tr

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
    #  QString QAbstractSeries::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN15QAbstractSeries2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAbstractSeries'
  #  The part of Qt it is of, as another part has a class of its name too.
  __qt_part__ = 'QtCharts'

  #  A C++ QAbstractSeries Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QAbstractSeries'

  #  The functions Qt calls itself that QAbstractSeries is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'type': (
          ('_ZNK15QAbstractSeries4typeEv',
           ('int', 'enum', 'QtCharts:QAbstractSeries.SeriesType'),
           ()),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QAbstractSeries::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractseries.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QAbstractSeries::metaObject() const
    address = self.uglySide.call('ritual_ZNK15QAbstractSeries10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def type(self) -> SeriesType:
    """
    Calls Qt's 'SeriesType QAbstractSeries::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractseries.html#type

    Returns
    -------

    SeriesType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'SeriesType(number)'
      gives.
    """
    #  SeriesType QAbstractSeries::type() const
    return QAbstractSeries.SeriesType(self.uglySide.call(
        'ritual_ZNK15QAbstractSeries4typeEv',
    ))

  def name(self) -> str:
    """
    Calls Qt's 'QString QAbstractSeries::name() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractseries.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QAbstractSeries::name() const
    return self.uglySide.call('ritual_ZNK15QAbstractSeries4nameEv')

  def isVisible(self) -> bool:
    """
    Calls Qt's 'bool QAbstractSeries::isVisible() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractseries.html#isVisible
    """
    #  bool QAbstractSeries::isVisible() const
    return self.uglySide.call('ritual_ZNK15QAbstractSeries9isVisibleEv')

  def opacity(self) -> float:
    """
    Calls Qt's 'qreal QAbstractSeries::opacity() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractseries.html#opacity
    """
    #  qreal QAbstractSeries::opacity() const
    return self.uglySide.call('ritual_ZNK15QAbstractSeries7opacityEv')

  def useOpenGL(self) -> bool:
    """
    Calls Qt's 'bool QAbstractSeries::useOpenGL() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractseries.html#useOpenGL
    """
    #  bool QAbstractSeries::useOpenGL() const
    return self.uglySide.call('ritual_ZNK15QAbstractSeries9useOpenGLEv')

  def chart(self) -> Optional[QChart]:
    """
    Calls Qt's 'QChart *QAbstractSeries::chart() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractseries.html#chart

    Returns
    -------

    Optional[QChart]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QChart *QAbstractSeries::chart() const
    address = self.uglySide.call('ritual_ZNK15QAbstractSeries5chartEv')
    from . import QChart
    return QChart._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setName(self, name: str) -> None:
    """
    Calls Qt's 'void QAbstractSeries::setName(const QString &name)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractseries.html#setName

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QAbstractSeries::setName(const QString &name)
    self.uglySide.call('ritual_ZN15QAbstractSeries7setNameERK7QString', name)

  @overload()
  @overload(bool)
  def setVisible(self, visible: bool = True) -> None:
    """
    Calls Qt's 'void QAbstractSeries::setVisible(bool visible)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractseries.html#setVisible

    Parameters
    ----------

    visible : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QAbstractSeries::setVisible(bool visible)
    self.uglySide.call('ritual_ZN15QAbstractSeries10setVisibleEb', visible)

  @overload(float)
  def setOpacity(self, opacity: float) -> None:
    """
    Calls Qt's 'void QAbstractSeries::setOpacity(qreal opacity)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractseries.html#setOpacity

    Parameters
    ----------

    opacity : float
      Passed on as it is.
    """
    #  void QAbstractSeries::setOpacity(qreal opacity)
    self.uglySide.call('ritual_ZN15QAbstractSeries10setOpacityEd', opacity)

  @overload()
  @overload(bool)
  def setUseOpenGL(self, enable: bool = True) -> None:
    """
    Calls Qt's 'void QAbstractSeries::setUseOpenGL(bool enable)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractseries.html#setUseOpenGL

    Parameters
    ----------

    enable : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QAbstractSeries::setUseOpenGL(bool enable)
    self.uglySide.call('ritual_ZN15QAbstractSeries12setUseOpenGLEb', enable)

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
    Qt's 'QAbstractSeries::QAbstractSeries(QAbstractSeriesPrivate &d, QObject
    *parent)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QAbstractSeries.__init__' has no cute function yet. Qt's "
        "'QAbstractSeries::QAbstractSeries(QAbstractSeriesPrivate &d, "
        "QObject *parent)': takes a type Python has no way to hand over yet."
    )

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

  @overload(QAbstractAxis)
  @overload(NoneType)
  def attachAxis(self, axis: Optional[QAbstractAxis]) -> bool:
    """
    Calls Qt's 'bool QAbstractSeries::attachAxis(QAbstractAxis *axis)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractseries.html#attachAxis

    Parameters
    ----------

    axis : Optional[QAbstractAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QAbstractSeries::attachAxis(QAbstractAxis *axis)
    return self.uglySide.call(
        'ritual_ZN15QAbstractSeries10attachAxisEP13QAbstractAxis',
        self._addressOf(axis),
    )

  @overload(QAbstractAxis)
  @overload(NoneType)
  def detachAxis(self, axis: Optional[QAbstractAxis]) -> bool:
    """
    Calls Qt's 'bool QAbstractSeries::detachAxis(QAbstractAxis *axis)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractseries.html#detachAxis

    Parameters
    ----------

    axis : Optional[QAbstractAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QAbstractSeries::detachAxis(QAbstractAxis *axis)
    return self.uglySide.call(
        'ritual_ZN15QAbstractSeries10detachAxisEP13QAbstractAxis',
        self._addressOf(axis),
    )

  def attachedAxes(self) -> QList[QAbstractAxis]:
    """
    Calls Qt's 'QList<QAbstractAxis *> QAbstractSeries::attachedAxes()'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractseries.html#attachedAxes

    Returns
    -------

    QList[QAbstractAxis]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QAbstractAxis *> QAbstractSeries::attachedAxes()
    address = self.uglySide.call(
        'ritual_ZN15QAbstractSeries12attachedAxesEv',
    )
    from . import QAbstractAxis
    return QList[QAbstractAxis]._cuteOwning(address)

  def show(self) -> None:
    """
    Calls Qt's 'void QAbstractSeries::show()'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractseries.html#show
    """
    #  void QAbstractSeries::show()
    self.uglySide.call('ritual_ZN15QAbstractSeries4showEv')

  def hide(self) -> None:
    """
    Calls Qt's 'void QAbstractSeries::hide()'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractseries.html#hide
    """
    #  void QAbstractSeries::hide()
    self.uglySide.call('ritual_ZN15QAbstractSeries4hideEv')

  def nameChanged(self) -> None:
    """
    Calls Qt's 'void QAbstractSeries::nameChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractseries.html#nameChanged
    """
    #  void QAbstractSeries::nameChanged()
    self.uglySide.call('ritual_ZN15QAbstractSeries11nameChangedEv')

  def visibleChanged(self) -> None:
    """
    Calls Qt's 'void QAbstractSeries::visibleChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractseries.html#visibleChanged
    """
    #  void QAbstractSeries::visibleChanged()
    self.uglySide.call('ritual_ZN15QAbstractSeries14visibleChangedEv')

  def opacityChanged(self) -> None:
    """
    Calls Qt's 'void QAbstractSeries::opacityChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractseries.html#opacityChanged
    """
    #  void QAbstractSeries::opacityChanged()
    self.uglySide.call('ritual_ZN15QAbstractSeries14opacityChangedEv')

  def useOpenGLChanged(self) -> None:
    """
    Calls Qt's 'void QAbstractSeries::useOpenGLChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractseries.html#useOpenGLChanged
    """
    #  void QAbstractSeries::useOpenGLChanged()
    self.uglySide.call('ritual_ZN15QAbstractSeries16useOpenGLChangedEv')


#  Qt's 'QList<QAbstractSeries *>': the list of QAbstractSeries, which
#  'QList[QAbstractSeries]' gives. It is made here, so that there is one as
#  soon as there can be a QAbstractSeries.
QList.createKind(
    QAbstractSeries, 'address',
    make='ritual_list_make_QAbstractSeries_ptr',
    add='ritual_list_add_QAbstractSeries_ptr',
    size='ritual_list_size_QAbstractSeries_ptr',
    at='ritual_list_at_QAbstractSeries_ptr',
    drop='ritual_list_drop_QAbstractSeries_ptr',
)
