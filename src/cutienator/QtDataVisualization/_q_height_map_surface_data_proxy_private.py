"""
QHeightMapSurfaceDataProxyPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDataVisualization/6.12.0/QtDataVisualization/private/qheightmapsurfacedataproxy_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QHeightMapSurfaceDataProxyPrivate to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from . import QSurfaceDataProxyPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from . import QHeightMapSurfaceDataProxy


class QHeightMapSurfaceDataProxyPrivate(QSurfaceDataProxyPrivate):
  """
  The cute side of Qt's QHeightMapSurfaceDataProxyPrivate: a plain Python
  object standing in front of one C++ QHeightMapSurfaceDataProxyPrivate.

  It is built on the cute 'QSurfaceDataProxyPrivate', as Qt's
  QHeightMapSurfaceDataProxyPrivate is built on Qt's
  QSurfaceDataProxyPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QHeightMapSurfaceDataProxyPrivate that has a ritual
  and that Python can call so far, 11 names in all: 'metaObject',
  'setValueRanges', 'setMinXValue', 'setMaxXValue', 'setMinZValue',
  'setMaxZValue', 'setMinYValue', 'setMaxYValue', 'setAutoScaleY', 'qptr',
  'handlePendingResolve'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QHeightMapSurfaceDataProxyPrivate::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int
    QHeightMapSurfaceDataProxyPrivate::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's
    'QHeightMapSurfaceDataProxyPrivate::~QHeightMapSurfaceDataProxyPrivate(
    )': the destructor: Python never removes a C++
    QHeightMapSurfaceDataProxyPrivate.

  What has no ritual
  ------------------

  4 of the 18 functions Qt declares: 2 not a gap; 1 Qt's library has no name
  for it, and its code in Qt's source does not compile apart from its file; 1
  leans on 'QHeightMapSurfaceDataProxyPrivate.

  What to expect
  --------------

  - The C++ QHeightMapSurfaceDataProxyPrivate is created at the first use,
    not by 'QHeightMapSurfaceDataProxyPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QHeightMapSurfaceDataProxyPrivate.
  - Qt tells when it has removed the C++ QHeightMapSurfaceDataProxyPrivate.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QHeightMapSurfaceDataProxyPrivate that has no cute
    function yet, '__init__', holds a function that raises
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
  __qt_class__ = 'QHeightMapSurfaceDataProxyPrivate'
  #  The part of Qt it is of, as another part has a class of its name too.
  __qt_part__ = 'QtDataVisualization'

  #  A C++ QHeightMapSurfaceDataProxyPrivate Python makes is of a C++ class
  #  of ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QHeightMapSurfaceDataProxyPrivate'

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
    *QHeightMapSurfaceDataProxyPrivate::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheightmapsurfacedataproxyprivate.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QHeightMapSurfaceDataProxyPrivate::metaObject()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK33QHeightMapSurfaceDataProxyPrivate10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float, float, float, float)
  def setValueRanges(
      self,
      minX: float,
      maxX: float,
      minZ: float,
      maxZ: float,
  ) -> None:
    """
    Calls Qt's 'void QHeightMapSurfaceDataProxyPrivate::setValueRanges(float
    minX, float maxX, float minZ, float maxZ)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheightmapsurfacedataproxyprivate.html

    Parameters
    ----------

    minX : float
      Passed on as it is.

    maxX : float
      Passed on as it is.

    minZ : float
      Passed on as it is.

    maxZ : float
      Passed on as it is.
    """
    #  void QHeightMapSurfaceDataProxyPrivate::setValueRanges(float minX,
    #      float maxX, float minZ, float maxZ)
    self.uglySide.call(
        'ritual_ZN33QHeightMapSurfaceDataProxyPrivate14setValueRangesEffff',
        minX, maxX, minZ, maxZ,
    )

  @overload(float)
  def setMinXValue(self, min: float) -> None:
    """
    Calls Qt's 'void QHeightMapSurfaceDataProxyPrivate::setMinXValue(float
    min)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheightmapsurfacedataproxyprivate.html

    Parameters
    ----------

    min : float
      Passed on as it is.
    """
    #  void QHeightMapSurfaceDataProxyPrivate::setMinXValue(float min)
    self.uglySide.call(
        'ritual_ZN33QHeightMapSurfaceDataProxyPrivate12setMinXValueEf', min,
    )

  @overload(float)
  def setMaxXValue(self, max: float) -> None:
    """
    Calls Qt's 'void QHeightMapSurfaceDataProxyPrivate::setMaxXValue(float
    max)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheightmapsurfacedataproxyprivate.html

    Parameters
    ----------

    max : float
      Passed on as it is.
    """
    #  void QHeightMapSurfaceDataProxyPrivate::setMaxXValue(float max)
    self.uglySide.call(
        'ritual_ZN33QHeightMapSurfaceDataProxyPrivate12setMaxXValueEf', max,
    )

  @overload(float)
  def setMinZValue(self, min: float) -> None:
    """
    Calls Qt's 'void QHeightMapSurfaceDataProxyPrivate::setMinZValue(float
    min)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheightmapsurfacedataproxyprivate.html

    Parameters
    ----------

    min : float
      Passed on as it is.
    """
    #  void QHeightMapSurfaceDataProxyPrivate::setMinZValue(float min)
    self.uglySide.call(
        'ritual_ZN33QHeightMapSurfaceDataProxyPrivate12setMinZValueEf', min,
    )

  @overload(float)
  def setMaxZValue(self, max: float) -> None:
    """
    Calls Qt's 'void QHeightMapSurfaceDataProxyPrivate::setMaxZValue(float
    max)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheightmapsurfacedataproxyprivate.html

    Parameters
    ----------

    max : float
      Passed on as it is.
    """
    #  void QHeightMapSurfaceDataProxyPrivate::setMaxZValue(float max)
    self.uglySide.call(
        'ritual_ZN33QHeightMapSurfaceDataProxyPrivate12setMaxZValueEf', max,
    )

  @overload(float)
  def setMinYValue(self, min: float) -> None:
    """
    Calls Qt's 'void QHeightMapSurfaceDataProxyPrivate::setMinYValue(float
    min)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheightmapsurfacedataproxyprivate.html

    Parameters
    ----------

    min : float
      Passed on as it is.
    """
    #  void QHeightMapSurfaceDataProxyPrivate::setMinYValue(float min)
    self.uglySide.call(
        'ritual_ZN33QHeightMapSurfaceDataProxyPrivate12setMinYValueEf', min,
    )

  @overload(float)
  def setMaxYValue(self, max: float) -> None:
    """
    Calls Qt's 'void QHeightMapSurfaceDataProxyPrivate::setMaxYValue(float
    max)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheightmapsurfacedataproxyprivate.html

    Parameters
    ----------

    max : float
      Passed on as it is.
    """
    #  void QHeightMapSurfaceDataProxyPrivate::setMaxYValue(float max)
    self.uglySide.call(
        'ritual_ZN33QHeightMapSurfaceDataProxyPrivate12setMaxYValueEf', max,
    )

  @overload(bool)
  def setAutoScaleY(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QHeightMapSurfaceDataProxyPrivate::setAutoScaleY(bool
    enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheightmapsurfacedataproxyprivate.html

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QHeightMapSurfaceDataProxyPrivate::setAutoScaleY(bool enabled)
    self.uglySide.call(
        'ritual_ZN33QHeightMapSurfaceDataProxyPrivate13setAutoScaleYEb',
        enabled,
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
    'QHeightMapSurfaceDataProxyPrivate::QHeightMapSurfaceDataProxyPrivate(
    QHeightMapSurfaceDataProxy *q)': Qt's library has no name for it, and its
    code in Qt's source does not compile apart from its file: use of
    undeclared identifier 'defaultMinValue'; did you mean
    'QFontVariableAxis::defaultValue'?.
    """
    raise NotImplementedError(
        "'QHeightMapSurfaceDataProxyPrivate.__init__' has no cute function "
        "yet. Qt's "
        "'QHeightMapSurfaceDataProxyPrivate::QHeightMapSurfaceDataProxyPriva"
        "te(QHeightMapSurfaceDataProxy *q)': Qt's library has no name for "
        "it, and its code in Qt's source does not compile apart from its "
        "file: use of undeclared identifier 'defaultMinValue'; did you mean "
        "'QFontVariableAxis::defaultValue'?.")

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

  def qptr(self) -> Optional[QHeightMapSurfaceDataProxy]:
    """
    Calls Qt's 'QHeightMapSurfaceDataProxy
    *QHeightMapSurfaceDataProxyPrivate::qptr()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheightmapsurfacedataproxyprivate.html#qptr

    Returns
    -------

    Optional[QHeightMapSurfaceDataProxy]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QHeightMapSurfaceDataProxy *QHeightMapSurfaceDataProxyPrivate::qptr()
    address = self.uglySide.call(
        'ritual_ZN33QHeightMapSurfaceDataProxyPrivate4qptrEv',
    )
    from . import QHeightMapSurfaceDataProxy
    return QHeightMapSurfaceDataProxy._cuteAt(address)

  def handlePendingResolve(self) -> None:
    """
    Calls Qt's 'void
    QHeightMapSurfaceDataProxyPrivate::handlePendingResolve()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheightmapsurfacedataproxyprivate.html
    """
    #  void QHeightMapSurfaceDataProxyPrivate::handlePendingResolve()
    self.uglySide.call(
        'ritual_ZN33QHeightMapSurfaceDataProxyPrivate20handlePendingResolve'
        'Ev',
    )
