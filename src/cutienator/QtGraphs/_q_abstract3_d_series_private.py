"""
QAbstract3DSeriesPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGraphs/6.12.0/QtGraphs/private/qabstract3dseries_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QAbstract3DSeriesPrivate to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import QObjectPrivate
from . import QAbstract3DSeries, QGraphsTheme

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtGui import QColor, QQuaternion
  from . import QAbstractDataProxy, QQuickGraphsItem
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAbstractDataProxy = WAIT['QtGraphs:QAbstractDataProxy']
  QColor = WAIT['QColor']
  QQuaternion = WAIT['QQuaternion']
  QQuickGraphsItem = WAIT['QQuickGraphsItem']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAbstract3DSeriesPrivate(QObjectPrivate):
  """
  The cute side of Qt's QAbstract3DSeriesPrivate: a plain Python object
  standing in front of one C++ QAbstract3DSeriesPrivate.

  It is built on the cute 'QObjectPrivate', as Qt's QAbstract3DSeriesPrivate
  is built on Qt's QObjectPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QAbstract3DSeriesPrivate that has a ritual and that
  Python can call so far, 23 names in all: 'q_func', 'dataProxy',
  'setDataProxy', 'setGraph', 'connectGraphAndProxy', 'createItemLabel',
  'setItemLabelFormat', 'setVisible', 'setMesh', 'setMeshSmooth',
  'setMeshRotation', 'setUserDefinedMesh', 'setColorStyle', 'setBaseColor',
  'setSingleHighlightColor', 'setMultiHighlightColor', 'setName',
  'itemLabel', 'markItemLabelDirty', 'itemLabelDirty', 'setItemLabelVisible',
  'isUsingGradient', 'setLightingMode'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QAbstract3DSeries *QAbstract3DSeriesPrivate::q_func() const':
    takes in Python what 'QAbstract3DSeries
    *QAbstract3DSeriesPrivate::q_func()' takes.
  - Qt's 'QAbstract3DSeriesPrivate::~QAbstract3DSeriesPrivate()': the
    destructor: Python never removes a C++ QAbstract3DSeriesPrivate.
  - Qt's 'void QAbstract3DSeriesPrivate::resetToTheme(const QGraphsTheme
    &theme, qsizetype seriesIndex, bool force)': takes a type Python has no
    way to hand over yet.

  What has no ritual
  ------------------

  3 of the 30 functions Qt declares: 3 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QAbstract3DSeriesPrivate is created at the first use, not by
    'QAbstract3DSeriesPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAbstract3DSeriesPrivate.
  - Each name of Qt's QAbstract3DSeriesPrivate that has no cute function yet,
    'resetToTheme', 'setBaseGradient', 'setMultiHighlightGradient',
    'setSingleHighlightGradient', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAbstract3DSeriesPrivate'
  #  The part of Qt it is of, as another part has a class of its name too.
  __qt_part__ = 'QtGraphs'

  #  A C++ QAbstract3DSeriesPrivate Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QAbstract3DSeriesPrivate'

  #  The functions Qt calls itself that QAbstract3DSeriesPrivate is the first
  #  to declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'setDataProxy': (
          ('_ZN24QAbstract3DSeriesPrivate12setDataProxyEP18QAbstractDataPro'
           'xy',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGraphs:QAbstractDataProxy'),
           )),
      ),
      'setGraph': (
          ('_ZN24QAbstract3DSeriesPrivate8setGraphEP16QQuickGraphsItem',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGraphs:QQuickGraphsItem'),
           )),
      ),
      'connectGraphAndProxy': (
          ('_ZN24QAbstract3DSeriesPrivate20connectGraphAndProxyEP16QQuickGr'
           'aphsItem',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGraphs:QQuickGraphsItem'),
           )),
      ),
      'createItemLabel': (
          ('_ZN24QAbstract3DSeriesPrivate15createItemLabelEv',
           ('nothing', 'nothing', ''),
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

  def dataProxy(self) -> Optional[QAbstractDataProxy]:
    """
    Calls Qt's 'QAbstractDataProxy *QAbstract3DSeriesPrivate::dataProxy()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dseriesprivate.html#dataProxy

    Returns
    -------

    Optional[QAbstractDataProxy]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractDataProxy *QAbstract3DSeriesPrivate::dataProxy() const
    address = self.uglySide.call(
        'ritual_ZNK24QAbstract3DSeriesPrivate9dataProxyEv',
    )
    from . import QAbstractDataProxy
    return QAbstractDataProxy._cuteAt(address)

  def itemLabelDirty(self) -> bool:
    """
    Calls Qt's 'bool QAbstract3DSeriesPrivate::itemLabelDirty() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dseriesprivate.html#itemLabelDirty
    """
    #  bool QAbstract3DSeriesPrivate::itemLabelDirty() const
    return self.uglySide.call(
        'ritual_ZNK24QAbstract3DSeriesPrivate14itemLabelDirtyEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QAbstractDataProxy)
  @overload(NoneType)
  def setDataProxy(self, proxy: Optional[QAbstractDataProxy]) -> None:
    """
    Calls Qt's 'void
    QAbstract3DSeriesPrivate::setDataProxy(QAbstractDataProxy *proxy)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dseriesprivate.html#setDataProxy

    Parameters
    ----------

    proxy : Optional[QAbstractDataProxy]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstract3DSeriesPrivate::setDataProxy(QAbstractDataProxy *proxy)
    ritual = (
        'ritual_ZN24QAbstract3DSeriesPrivate12setDataProxyEP18QAbstractData'
        'Proxy')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN24QAbstract3DSeriesPrivate12setDataProxyEP18QAbstra'
          'ctDataProxy')
    self.uglySide.call(ritual, self._addressOf(proxy))

  @overload(QQuickGraphsItem)
  @overload(NoneType)
  def setGraph(self, graph: Optional[QQuickGraphsItem]) -> None:
    """
    Calls Qt's 'void QAbstract3DSeriesPrivate::setGraph(QQuickGraphsItem
    *graph)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dseriesprivate.html#setGraph

    Parameters
    ----------

    graph : Optional[QQuickGraphsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstract3DSeriesPrivate::setGraph(QQuickGraphsItem *graph)
    ritual = (
        'ritual_ZN24QAbstract3DSeriesPrivate8setGraphEP16QQuickGraphsItem')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN24QAbstract3DSeriesPrivate8setGraphEP16QQuickGraphs'
          'Item')
    self.uglySide.call(ritual, self._addressOf(graph))

  @overload(str)
  def setItemLabelFormat(self, format: str) -> None:
    """
    Calls Qt's 'void QAbstract3DSeriesPrivate::setItemLabelFormat(const
    QString &format)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dseriesprivate.html#setItemLabelFormat

    Parameters
    ----------

    format : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QAbstract3DSeriesPrivate::setItemLabelFormat(const QString
    #      &format)
    self.uglySide.call(
        'ritual_ZN24QAbstract3DSeriesPrivate18setItemLabelFormatERK7QString',
        format,
    )

  @overload(bool)
  def setVisible(self, visible: bool) -> None:
    """
    Calls Qt's 'void QAbstract3DSeriesPrivate::setVisible(bool visible)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dseriesprivate.html#setVisible

    Parameters
    ----------

    visible : bool
      Passed on as it is.
    """
    #  void QAbstract3DSeriesPrivate::setVisible(bool visible)
    self.uglySide.call(
        'ritual_ZN24QAbstract3DSeriesPrivate10setVisibleEb', visible,
    )

  @overload(QAbstract3DSeries.Mesh)
  def setMesh(self, mesh: QAbstract3DSeries.Mesh) -> None:
    """
    Calls Qt's 'void
    QAbstract3DSeriesPrivate::setMesh(QAbstract3DSeries::Mesh mesh)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dseriesprivate.html#setMesh

    Parameters
    ----------

    mesh : QAbstract3DSeries.Mesh
      Passed on as its number.
    """
    #  void QAbstract3DSeriesPrivate::setMesh(QAbstract3DSeries::Mesh mesh)
    self.uglySide.call(
        'ritual_ZN24QAbstract3DSeriesPrivate7setMeshEN17QAbstract3DSeries4M'
        'eshE',
        mesh.value,
    )

  @overload(bool)
  def setMeshSmooth(self, enable: bool) -> None:
    """
    Calls Qt's 'void QAbstract3DSeriesPrivate::setMeshSmooth(bool enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dseriesprivate.html#setMeshSmooth

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QAbstract3DSeriesPrivate::setMeshSmooth(bool enable)
    self.uglySide.call(
        'ritual_ZN24QAbstract3DSeriesPrivate13setMeshSmoothEb', enable,
    )

  @overload(QQuaternion)
  def setMeshRotation(self, rotation: QQuaternion) -> None:
    """
    Calls Qt's 'void QAbstract3DSeriesPrivate::setMeshRotation(const
    QQuaternion &rotation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dseriesprivate.html#setMeshRotation

    Parameters
    ----------

    rotation : QQuaternion
      Passed on as a value: Qt reads the C++ QQuaternion, which stays
      Python's own.
    """
    #  void QAbstract3DSeriesPrivate::setMeshRotation(const QQuaternion
    #      &rotation)
    self.uglySide.call(
        'ritual_ZN24QAbstract3DSeriesPrivate15setMeshRotationERK11QQuaterni'
        'on',
        self._valueOf(rotation),
    )

  @overload(str)
  def setUserDefinedMesh(self, meshFile: str) -> None:
    """
    Calls Qt's 'void QAbstract3DSeriesPrivate::setUserDefinedMesh(const
    QString &meshFile)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dseriesprivate.html#setUserDefinedMesh

    Parameters
    ----------

    meshFile : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QAbstract3DSeriesPrivate::setUserDefinedMesh(const QString
    #      &meshFile)
    self.uglySide.call(
        'ritual_ZN24QAbstract3DSeriesPrivate18setUserDefinedMeshERK7QString',
        meshFile,
    )

  @overload(QGraphsTheme.ColorStyle)
  def setColorStyle(self, style: QGraphsTheme.ColorStyle) -> None:
    """
    Calls Qt's 'void
    QAbstract3DSeriesPrivate::setColorStyle(QGraphsTheme::ColorStyle style)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dseriesprivate.html#setColorStyle

    Parameters
    ----------

    style : QGraphsTheme.ColorStyle
      Passed on as its number.
    """
    #  void QAbstract3DSeriesPrivate::setColorStyle(QGraphsTheme::ColorStyle
    #      style)
    self.uglySide.call(
        'ritual_ZN24QAbstract3DSeriesPrivate13setColorStyleEN12QGraphsTheme'
        '10ColorStyleE',
        style.value,
    )

  @overload(QColor)
  def setBaseColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QAbstract3DSeriesPrivate::setBaseColor(QColor color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dseriesprivate.html#setBaseColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QAbstract3DSeriesPrivate::setBaseColor(QColor color)
    self.uglySide.call(
        'ritual_ZN24QAbstract3DSeriesPrivate12setBaseColorE6QColor',
        self._valueOf(color),
    )

  @overload(QColor)
  def setSingleHighlightColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QAbstract3DSeriesPrivate::setSingleHighlightColor(QColor
    color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dseriesprivate.html

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QAbstract3DSeriesPrivate::setSingleHighlightColor(QColor color)
    self.uglySide.call(
        'ritual_ZN24QAbstract3DSeriesPrivate23setSingleHighlightColorE6QCol'
        'or',
        self._valueOf(color),
    )

  @overload(QColor)
  def setMultiHighlightColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QAbstract3DSeriesPrivate::setMultiHighlightColor(QColor
    color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dseriesprivate.html

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QAbstract3DSeriesPrivate::setMultiHighlightColor(QColor color)
    self.uglySide.call(
        'ritual_ZN24QAbstract3DSeriesPrivate22setMultiHighlightColorE6QColo'
        'r',
        self._valueOf(color),
    )

  @overload(str)
  def setName(self, name: str) -> None:
    """
    Calls Qt's 'void QAbstract3DSeriesPrivate::setName(const QString &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dseriesprivate.html#setName

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QAbstract3DSeriesPrivate::setName(const QString &name)
    self.uglySide.call(
        'ritual_ZN24QAbstract3DSeriesPrivate7setNameERK7QString', name,
    )

  @overload(bool)
  def setItemLabelVisible(self, visible: bool) -> None:
    """
    Calls Qt's 'void QAbstract3DSeriesPrivate::setItemLabelVisible(bool
    visible)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dseriesprivate.html#setItemLabelVisible

    Parameters
    ----------

    visible : bool
      Passed on as it is.
    """
    #  void QAbstract3DSeriesPrivate::setItemLabelVisible(bool visible)
    self.uglySide.call(
        'ritual_ZN24QAbstract3DSeriesPrivate19setItemLabelVisibleEb',
        visible,
    )

  @overload(QAbstract3DSeries.LightingMode)
  def setLightingMode(self, mode: QAbstract3DSeries.LightingMode) -> None:
    """
    Calls Qt's 'void
    QAbstract3DSeriesPrivate::setLightingMode(QAbstract3DSeries::LightingMode
    mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dseriesprivate.html#setLightingMode

    Parameters
    ----------

    mode : QAbstract3DSeries.LightingMode
      Passed on as its number.
    """
    #  void QAbstract3DSeriesPrivate::setLightingMode(QAbstract3DSeries::
    #      LightingMode mode)
    self.uglySide.call(
        'ritual_ZN24QAbstract3DSeriesPrivate15setLightingModeEN17QAbstract3'
        'DSeries12LightingModeE',
        mode.value,
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

  @overload(QAbstract3DSeries.SeriesType)
  def __init__(self, type: QAbstract3DSeries.SeriesType) -> None:
    """
    Notes what was given, for Qt's
    'QAbstract3DSeriesPrivate::QAbstract3DSeriesPrivate(QAbstract3DSeries::
    SeriesType type)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dseriesprivate.html

    Parameters
    ----------

    type : QAbstract3DSeries.SeriesType
      Passed on as its number.
    """
    #  QAbstract3DSeriesPrivate::QAbstract3DSeriesPrivate(
    #      QAbstract3DSeries::SeriesType type)
    self._noteCreation(QAbstract3DSeriesPrivate, lambda: Rituals.call(
        'ritual_ZN24QAbstract3DSeriesPrivateC1EN17QAbstract3DSeries10Series'
        'TypeE',
        type.value,
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

  def q_func(self) -> Optional[QAbstract3DSeries]:
    """
    Calls Qt's 'QAbstract3DSeries *QAbstract3DSeriesPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dseriesprivate.html#q_func

    Returns
    -------

    Optional[QAbstract3DSeries]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstract3DSeries *QAbstract3DSeriesPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN24QAbstract3DSeriesPrivate6q_funcEv',
    )
    return QAbstract3DSeries._cuteAt(address)

  @overload(QQuickGraphsItem)
  @overload(NoneType)
  def connectGraphAndProxy(
      self,
      newGraph: Optional[QQuickGraphsItem],
  ) -> None:
    """
    Calls Qt's 'void
    QAbstract3DSeriesPrivate::connectGraphAndProxy(QQuickGraphsItem
    *newGraph)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dseriesprivate.html#connectGraphAndProxy

    Parameters
    ----------

    newGraph : Optional[QQuickGraphsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstract3DSeriesPrivate::connectGraphAndProxy(QQuickGraphsItem
    #      *newGraph)
    self.uglySide.call(
        'ritual_ZN24QAbstract3DSeriesPrivate20connectGraphAndProxyEP16QQuic'
        'kGraphsItem',
        self._addressOf(newGraph),
    )

  def createItemLabel(self) -> None:
    """
    Calls Qt's 'void QAbstract3DSeriesPrivate::createItemLabel()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dseriesprivate.html#createItemLabel
    """
    #  void QAbstract3DSeriesPrivate::createItemLabel()
    self.uglySide.call(
        'ritual_ZN24QAbstract3DSeriesPrivate15createItemLabelEv',
    )

  def itemLabel(self) -> str:
    """
    Calls Qt's 'QString QAbstract3DSeriesPrivate::itemLabel()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dseriesprivate.html#itemLabel

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QAbstract3DSeriesPrivate::itemLabel()
    return self.uglySide.call(
        'ritual_ZN24QAbstract3DSeriesPrivate9itemLabelEv',
    )

  def markItemLabelDirty(self) -> None:
    """
    Calls Qt's 'void QAbstract3DSeriesPrivate::markItemLabelDirty()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dseriesprivate.html#markItemLabelDirty
    """
    #  void QAbstract3DSeriesPrivate::markItemLabelDirty()
    self.uglySide.call(
        'ritual_ZN24QAbstract3DSeriesPrivate18markItemLabelDirtyEv',
    )

  def isUsingGradient(self) -> bool:
    """
    Calls Qt's 'bool QAbstract3DSeriesPrivate::isUsingGradient()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dseriesprivate.html#isUsingGradient
    """
    #  bool QAbstract3DSeriesPrivate::isUsingGradient()
    return self.uglySide.call(
        'ritual_ZN24QAbstract3DSeriesPrivate15isUsingGradientEv',
    )

  @staticmethod
  def resetToTheme(*__, **_) -> Never:
    """
    Qt's 'void QAbstract3DSeriesPrivate::resetToTheme(const QGraphsTheme
    &theme, qsizetype seriesIndex, bool force)': takes a type Python has no
    way to hand over yet.
    """
    raise NotImplementedError(
        "'QAbstract3DSeriesPrivate.resetToTheme' has no cute function yet. "
        "Qt's 'void QAbstract3DSeriesPrivate::resetToTheme(const "
        "QGraphsTheme &theme, qsizetype seriesIndex, bool force)': takes a "
        "type Python has no way to hand over yet.")

  @staticmethod
  def setBaseGradient(*__, **_) -> Never:
    """
    Qt's 'void QAbstract3DSeriesPrivate::setBaseGradient(const
    QLinearGradient &gradient)': Qt's library has no name for it, and its
    code in Qt's source does not compile apart from its file: use of
    undeclared identifier 'Utils'.
    """
    raise NotImplementedError(
        "'QAbstract3DSeriesPrivate.setBaseGradient' has no cute function "
        "yet. Qt's 'void QAbstract3DSeriesPrivate::setBaseGradient(const "
        "QLinearGradient &gradient)': Qt's library has no name for it, and "
        "its code in Qt's source does not compile apart from its file: use "
        "of undeclared identifier 'Utils'.")

  @staticmethod
  def setMultiHighlightGradient(*__, **_) -> Never:
    """
    Qt's 'void QAbstract3DSeriesPrivate::setMultiHighlightGradient(const
    QLinearGradient &gradient)': Qt's library has no name for it, and its
    code in Qt's source does not compile apart from its file: use of
    undeclared identifier 'Utils'.
    """
    raise NotImplementedError(
        "'QAbstract3DSeriesPrivate.setMultiHighlightGradient' has no cute "
        "function yet. Qt's 'void "
        "QAbstract3DSeriesPrivate::setMultiHighlightGradient(const "
        "QLinearGradient &gradient)': Qt's library has no name for it, and "
        "its code in Qt's source does not compile apart from its file: use "
        "of undeclared identifier 'Utils'.")

  @staticmethod
  def setSingleHighlightGradient(*__, **_) -> Never:
    """
    Qt's 'void QAbstract3DSeriesPrivate::setSingleHighlightGradient(const
    QLinearGradient &gradient)': Qt's library has no name for it, and its
    code in Qt's source does not compile apart from its file: use of
    undeclared identifier 'Utils'.
    """
    raise NotImplementedError(
        "'QAbstract3DSeriesPrivate.setSingleHighlightGradient' has no cute "
        "function yet. Qt's 'void "
        "QAbstract3DSeriesPrivate::setSingleHighlightGradient(const "
        "QLinearGradient &gradient)': Qt's library has no name for it, and "
        "its code in Qt's source does not compile apart from its file: use "
        "of undeclared identifier 'Utils'.")
