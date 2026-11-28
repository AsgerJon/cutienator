"""
QAbstract3DSeriesPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDataVisualization/6.12.0/QtDataVisualization/private/qabstract3dseries_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QAbstract3DSeriesPrivate to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtCore import QObject
from . import Q3DTheme, QAbstract3DSeries

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QColor, QLinearGradient, QQuaternion
  from . import Abstract3DController, QAbstractDataProxy
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  Abstract3DController = WAIT['Abstract3DController']
  QAbstractDataProxy = WAIT['QtDataVisualization:QAbstractDataProxy']
  QColor = WAIT['QColor']
  QLinearGradient = WAIT['QLinearGradient']
  QQuaternion = WAIT['QQuaternion']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAbstract3DSeriesPrivate(QObject):
  """
  The cute side of Qt's QAbstract3DSeriesPrivate: a plain Python object
  standing in front of one C++ QAbstract3DSeriesPrivate.

  It is built on the cute 'QObject', as Qt's QAbstract3DSeriesPrivate is
  built on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QAbstract3DSeriesPrivate that has a ritual and that
  Python can call so far, 24 names in all: 'metaObject', 'dataProxy',
  'setDataProxy', 'setController', 'connectControllerAndProxy',
  'createItemLabel', 'setItemLabelFormat', 'setVisible', 'setMesh',
  'setMeshSmooth', 'setMeshRotation', 'setUserDefinedMesh', 'setColorStyle',
  'setBaseColor', 'setBaseGradient', 'setSingleHighlightColor',
  'setSingleHighlightGradient', 'setMultiHighlightColor',
  'setMultiHighlightGradient', 'setName', 'itemLabel', 'markItemLabelDirty',
  'itemLabelDirty', 'setItemLabelVisible'. None can be made from Python: one
  comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QAbstract3DSeriesPrivate::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QAbstract3DSeriesPrivate::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QAbstract3DSeriesPrivate::~QAbstract3DSeriesPrivate()': the
    destructor: Python never removes a C++ QAbstract3DSeriesPrivate.
  - Qt's 'void QAbstract3DSeriesPrivate::resetToTheme(const Q3DTheme &theme,
    int seriesIndex, bool force)': takes a type Python has no way to hand
    over yet.

  What has no ritual
  ------------------

  4 of the 32 functions Qt declares: 2 not a gap; 2 leans on
  'QAbstract3DSeriesPrivate.

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
  - Qt tells when it has removed the C++ QAbstract3DSeriesPrivate. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QAbstract3DSeriesPrivate that has no cute function yet,
    '__init__', 'resetToTheme', holds a function that raises
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
  __qt_part__ = 'QtDataVisualization'

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
               ('address', 'address',
                'QtDataVisualization:QAbstractDataProxy'),
           )),
      ),
      'setController': (
          ('_ZN24QAbstract3DSeriesPrivate13setControllerEP20Abstract3DContr'
           'oller',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address',
                'QtDataVisualization:Abstract3DController'),
           )),
      ),
      'connectControllerAndProxy': (
          ('_ZN24QAbstract3DSeriesPrivate25connectControllerAndProxyEP20Abs'
           'tract3DController',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address',
                'QtDataVisualization:Abstract3DController'),
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

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QAbstract3DSeriesPrivate::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dseriesprivate.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QAbstract3DSeriesPrivate::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK24QAbstract3DSeriesPrivate10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

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

  @overload(Abstract3DController)
  @overload(NoneType)
  def setController(
      self,
      controller: Optional[Abstract3DController],
  ) -> None:
    """
    Calls Qt's 'void
    QAbstract3DSeriesPrivate::setController(Abstract3DController
    *controller)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dseriesprivate.html#setController

    Parameters
    ----------

    controller : Optional[Abstract3DController]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstract3DSeriesPrivate::setController(Abstract3DController
    #      *controller)
    ritual = (
        'ritual_ZN24QAbstract3DSeriesPrivate13setControllerEP20Abstract3DCo'
        'ntroller')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN24QAbstract3DSeriesPrivate13setControllerEP20Abstra'
          'ct3DController')
    self.uglySide.call(ritual, self._addressOf(controller))

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

  @overload(Q3DTheme.ColorStyle)
  def setColorStyle(self, style: Q3DTheme.ColorStyle) -> None:
    """
    Calls Qt's 'void
    QAbstract3DSeriesPrivate::setColorStyle(Q3DTheme::ColorStyle style)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dseriesprivate.html#setColorStyle

    Parameters
    ----------

    style : Q3DTheme.ColorStyle
      Passed on as its number.
    """
    #  void QAbstract3DSeriesPrivate::setColorStyle(Q3DTheme::ColorStyle
    #      style)
    self.uglySide.call(
        'ritual_ZN24QAbstract3DSeriesPrivate13setColorStyleEN8Q3DTheme10Col'
        'orStyleE',
        style.value,
    )

  @overload(QColor)
  def setBaseColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QAbstract3DSeriesPrivate::setBaseColor(const QColor
    &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dseriesprivate.html#setBaseColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QAbstract3DSeriesPrivate::setBaseColor(const QColor &color)
    self.uglySide.call(
        'ritual_ZN24QAbstract3DSeriesPrivate12setBaseColorERK6QColor',
        self._valueOf(color),
    )

  @overload(QLinearGradient)
  def setBaseGradient(self, gradient: QLinearGradient) -> None:
    """
    Calls Qt's 'void QAbstract3DSeriesPrivate::setBaseGradient(const
    QLinearGradient &gradient)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dseriesprivate.html#setBaseGradient

    Parameters
    ----------

    gradient : QLinearGradient
      Passed on as a value: Qt reads the C++ QLinearGradient, which stays
      Python's own.
    """
    #  void QAbstract3DSeriesPrivate::setBaseGradient(const QLinearGradient
    #      &gradient)
    self.uglySide.call(
        'ritual_ZN24QAbstract3DSeriesPrivate15setBaseGradientERK15QLinearGr'
        'adient',
        self._valueOf(gradient),
    )

  @overload(QColor)
  def setSingleHighlightColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QAbstract3DSeriesPrivate::setSingleHighlightColor(const
    QColor &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dseriesprivate.html

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QAbstract3DSeriesPrivate::setSingleHighlightColor(const QColor
    #      &color)
    self.uglySide.call(
        'ritual_ZN24QAbstract3DSeriesPrivate23setSingleHighlightColorERK6QC'
        'olor',
        self._valueOf(color),
    )

  @overload(QLinearGradient)
  def setSingleHighlightGradient(self, gradient: QLinearGradient) -> None:
    """
    Calls Qt's 'void
    QAbstract3DSeriesPrivate::setSingleHighlightGradient(const
    QLinearGradient &gradient)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dseriesprivate.html

    Parameters
    ----------

    gradient : QLinearGradient
      Passed on as a value: Qt reads the C++ QLinearGradient, which stays
      Python's own.
    """
    #  void QAbstract3DSeriesPrivate::setSingleHighlightGradient(const
    #      QLinearGradient &gradient)
    self.uglySide.call(
        'ritual_ZN24QAbstract3DSeriesPrivate26setSingleHighlightGradientERK'
        '15QLinearGradient',
        self._valueOf(gradient),
    )

  @overload(QColor)
  def setMultiHighlightColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QAbstract3DSeriesPrivate::setMultiHighlightColor(const
    QColor &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dseriesprivate.html

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QAbstract3DSeriesPrivate::setMultiHighlightColor(const QColor
    #      &color)
    self.uglySide.call(
        'ritual_ZN24QAbstract3DSeriesPrivate22setMultiHighlightColorERK6QCo'
        'lor',
        self._valueOf(color),
    )

  @overload(QLinearGradient)
  def setMultiHighlightGradient(self, gradient: QLinearGradient) -> None:
    """
    Calls Qt's 'void
    QAbstract3DSeriesPrivate::setMultiHighlightGradient(const QLinearGradient
    &gradient)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dseriesprivate.html

    Parameters
    ----------

    gradient : QLinearGradient
      Passed on as a value: Qt reads the C++ QLinearGradient, which stays
      Python's own.
    """
    #  void QAbstract3DSeriesPrivate::setMultiHighlightGradient(const
    #      QLinearGradient &gradient)
    self.uglySide.call(
        'ritual_ZN24QAbstract3DSeriesPrivate25setMultiHighlightGradientERK1'
        '5QLinearGradient',
        self._valueOf(gradient),
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
    Qt's
    'QAbstract3DSeriesPrivate::QAbstract3DSeriesPrivate(QAbstract3DSeries *q,
    QAbstract3DSeries::SeriesType type)': leans on
    'QAbstract3DSeriesPrivate::qt_metacall(QMetaObject::Call, int, void**)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QAbstract3DSeriesPrivate.__init__' has no cute function yet. Qt's "
        "'QAbstract3DSeriesPrivate::QAbstract3DSeriesPrivate(QAbstract3DSeri"
        "es *q, QAbstract3DSeries::SeriesType type)': leans on "
        "'QAbstract3DSeriesPrivate::qt_metacall(QMetaObject::Call, int, "
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

  @overload(Abstract3DController)
  @overload(NoneType)
  def connectControllerAndProxy(
      self,
      newController: Optional[Abstract3DController],
  ) -> None:
    """
    Calls Qt's 'void
    QAbstract3DSeriesPrivate::connectControllerAndProxy(Abstract3DController
    *newController)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dseriesprivate.html

    Parameters
    ----------

    newController : Optional[Abstract3DController]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstract3DSeriesPrivate::connectControllerAndProxy(
    #      Abstract3DController *newController)
    self.uglySide.call(
        'ritual_ZN24QAbstract3DSeriesPrivate25connectControllerAndProxyEP20'
        'Abstract3DController',
        self._addressOf(newController),
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

  @staticmethod
  def resetToTheme(*__, **_) -> Never:
    """
    Qt's 'void QAbstract3DSeriesPrivate::resetToTheme(const Q3DTheme &theme,
    int seriesIndex, bool force)': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'QAbstract3DSeriesPrivate.resetToTheme' has no cute function yet. "
        "Qt's 'void QAbstract3DSeriesPrivate::resetToTheme(const Q3DTheme "
        "&theme, int seriesIndex, bool force)': takes a type Python has no "
        "way to hand over yet.")
