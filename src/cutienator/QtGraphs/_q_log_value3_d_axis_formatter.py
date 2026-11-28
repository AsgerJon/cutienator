"""
QLogValue3DAxisFormatter binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGraphs/qlogvalue3daxisformatter.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtCore import QObject
from . import QValue3DAxisFormatter

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtDataVisualization import QLogValue3DAxisFormatterPrivate

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QLogValue3DAxisFormatter(QValue3DAxisFormatter):
  """
  The cute side of Qt's QLogValue3DAxisFormatter: a plain Python object
  standing in front of one C++ QLogValue3DAxisFormatter.

  It is built on the cute 'QValue3DAxisFormatter', as Qt's
  QLogValue3DAxisFormatter is built on Qt's QValue3DAxisFormatter, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QLogValue3DAxisFormatter that has a ritual and that
  Python can call so far, 16 names in all: 'metaObject', 'tr', 'd_func',
  'setBase', 'base', 'setAutoSubGrid', 'autoSubGrid', 'setEdgeLabelsVisible',
  'edgeLabelsVisible', 'baseChanged', 'autoSubGridChanged',
  'edgeLabelsVisibleChanged', 'createNewInstance', 'recalculate',
  'positionAt', 'valueAt'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QLogValue3DAxisFormatter::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QLogValue3DAxisFormatter::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'const QLogValue3DAxisFormatterPrivate
    *QLogValue3DAxisFormatter::d_func() const': takes in Python what
    'QLogValue3DAxisFormatterPrivate *QLogValue3DAxisFormatter::d_func()'
    takes.
  - Qt's 'QLogValue3DAxisFormatter::QLogValue3DAxisFormatter(
    QLogValue3DAxisFormatterPrivate &d, QObject *parent)': takes a type
    Python has no way to hand over yet.
  - Qt's 'QLogValue3DAxisFormatter::~QLogValue3DAxisFormatter()': the
    destructor: Python never removes a C++ QLogValue3DAxisFormatter.
  - Qt's 'void QLogValue3DAxisFormatter::populateCopy(QValue3DAxisFormatter
    &copy)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  4 of the 27 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QLogValue3DAxisFormatter is created at the first use, not by
    'QLogValue3DAxisFormatter(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QLogValue3DAxisFormatter.
  - Qt tells when it has removed the C++ QLogValue3DAxisFormatter. Every call
    on the cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QLogValue3DAxisFormatter::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qlogvalue3daxisformatter.html#tr

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
    #  QString QLogValue3DAxisFormatter::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN24QLogValue3DAxisFormatter2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QLogValue3DAxisFormatter'
  #  The part of Qt it is of, as another part has a class of its name too.
  __qt_part__ = 'QtGraphs'

  #  A C++ QLogValue3DAxisFormatter Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QLogValue3DAxisFormatter'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QLogValue3DAxisFormatter::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlogvalue3daxisformatter.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QLogValue3DAxisFormatter::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK24QLogValue3DAxisFormatter10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def base(self) -> float:
    """
    Calls Qt's 'qreal QLogValue3DAxisFormatter::base() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlogvalue3daxisformatter.html#base
    """
    #  qreal QLogValue3DAxisFormatter::base() const
    return self.uglySide.call('ritual_ZNK24QLogValue3DAxisFormatter4baseEv')

  def autoSubGrid(self) -> bool:
    """
    Calls Qt's 'bool QLogValue3DAxisFormatter::autoSubGrid() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlogvalue3daxisformatter.html#autoSubGrid
    """
    #  bool QLogValue3DAxisFormatter::autoSubGrid() const
    return self.uglySide.call(
        'ritual_ZNK24QLogValue3DAxisFormatter11autoSubGridEv',
    )

  def edgeLabelsVisible(self) -> bool:
    """
    Calls Qt's 'bool QLogValue3DAxisFormatter::edgeLabelsVisible() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlogvalue3daxisformatter.html#edgeLabelsVisible
    """
    #  bool QLogValue3DAxisFormatter::edgeLabelsVisible() const
    return self.uglySide.call(
        'ritual_ZNK24QLogValue3DAxisFormatter17edgeLabelsVisibleEv',
    )

  def createNewInstance(self) -> Optional[QValue3DAxisFormatter]:
    """
    Calls Qt's 'QValue3DAxisFormatter
    *QLogValue3DAxisFormatter::createNewInstance() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlogvalue3daxisformatter.html#createNewInstance

    Returns
    -------

    Optional[QValue3DAxisFormatter]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QValue3DAxisFormatter *QLogValue3DAxisFormatter::createNewInstance()
    #      const
    ritual = 'ritual_ZNK24QLogValue3DAxisFormatter17createNewInstanceEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK24QLogValue3DAxisFormatter17createNewInstanceEv')
    address = self.uglySide.call(ritual)
    return QValue3DAxisFormatter._cuteAt(address)

  @overload(float)
  def positionAt(self, value: float) -> float:
    """
    Calls Qt's 'float QLogValue3DAxisFormatter::positionAt(float value)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlogvalue3daxisformatter.html#positionAt

    Parameters
    ----------

    value : float
      Passed on as it is.
    """
    #  float QLogValue3DAxisFormatter::positionAt(float value) const
    ritual = 'ritual_ZNK24QLogValue3DAxisFormatter10positionAtEf'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK24QLogValue3DAxisFormatter10positionAtEf'
    return self.uglySide.call(ritual, value)

  @overload(float)
  def valueAt(self, position: float) -> float:
    """
    Calls Qt's 'float QLogValue3DAxisFormatter::valueAt(float position)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlogvalue3daxisformatter.html#valueAt

    Parameters
    ----------

    position : float
      Passed on as it is.
    """
    #  float QLogValue3DAxisFormatter::valueAt(float position) const
    ritual = 'ritual_ZNK24QLogValue3DAxisFormatter7valueAtEf'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK24QLogValue3DAxisFormatter7valueAtEf'
    return self.uglySide.call(ritual, position)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setBase(self, base: float) -> None:
    """
    Calls Qt's 'void QLogValue3DAxisFormatter::setBase(qreal base)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlogvalue3daxisformatter.html#setBase

    Parameters
    ----------

    base : float
      Passed on as it is.
    """
    #  void QLogValue3DAxisFormatter::setBase(qreal base)
    self.uglySide.call('ritual_ZN24QLogValue3DAxisFormatter7setBaseEd', base)

  @overload(bool)
  def setAutoSubGrid(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QLogValue3DAxisFormatter::setAutoSubGrid(bool enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlogvalue3daxisformatter.html#setAutoSubGrid

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QLogValue3DAxisFormatter::setAutoSubGrid(bool enabled)
    self.uglySide.call(
        'ritual_ZN24QLogValue3DAxisFormatter14setAutoSubGridEb', enabled,
    )

  @overload(bool)
  def setEdgeLabelsVisible(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QLogValue3DAxisFormatter::setEdgeLabelsVisible(bool
    enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlogvalue3daxisformatter.html#setEdgeLabelsVisible

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QLogValue3DAxisFormatter::setEdgeLabelsVisible(bool enabled)
    self.uglySide.call(
        'ritual_ZN24QLogValue3DAxisFormatter20setEdgeLabelsVisibleEb',
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

  @overload()
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QLogValue3DAxisFormatter::QLogValue3DAxisFormatter(QObject *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qlogvalue3daxisformatter.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QLogValue3DAxisFormatter::QLogValue3DAxisFormatter(QObject *parent)
    self._noteCreation(QLogValue3DAxisFormatter, lambda: Rituals.call(
        'ritual_ZN24QLogValue3DAxisFormatterC1EP7QObject',
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

  def d_func(self) -> Optional[QLogValue3DAxisFormatterPrivate]:
    """
    Calls Qt's 'QLogValue3DAxisFormatterPrivate
    *QLogValue3DAxisFormatter::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlogvalue3daxisformatter.html#d_func

    Returns
    -------

    Optional[QLogValue3DAxisFormatterPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QLogValue3DAxisFormatterPrivate *QLogValue3DAxisFormatter::d_func()
    address = self.uglySide.call(
        'ritual_ZN24QLogValue3DAxisFormatter6d_funcEv',
    )
    from ..QtDataVisualization import QLogValue3DAxisFormatterPrivate
    return QLogValue3DAxisFormatterPrivate._cuteAt(address)

  @overload(float)
  def baseChanged(self, base: float) -> None:
    """
    Calls Qt's 'void QLogValue3DAxisFormatter::baseChanged(qreal base)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlogvalue3daxisformatter.html#baseChanged

    Parameters
    ----------

    base : float
      Passed on as it is.
    """
    #  void QLogValue3DAxisFormatter::baseChanged(qreal base)
    self.uglySide.call(
        'ritual_ZN24QLogValue3DAxisFormatter11baseChangedEd', base,
    )

  @overload(bool)
  def autoSubGridChanged(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QLogValue3DAxisFormatter::autoSubGridChanged(bool
    enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlogvalue3daxisformatter.html#autoSubGridChanged

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QLogValue3DAxisFormatter::autoSubGridChanged(bool enabled)
    self.uglySide.call(
        'ritual_ZN24QLogValue3DAxisFormatter18autoSubGridChangedEb', enabled,
    )

  @overload(bool)
  def edgeLabelsVisibleChanged(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QLogValue3DAxisFormatter::edgeLabelsVisibleChanged(bool
    enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlogvalue3daxisformatter.html

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QLogValue3DAxisFormatter::edgeLabelsVisibleChanged(bool enabled)
    self.uglySide.call(
        'ritual_ZN24QLogValue3DAxisFormatter24edgeLabelsVisibleChangedEb',
        enabled,
    )

  def recalculate(self) -> None:
    """
    Calls Qt's 'void QLogValue3DAxisFormatter::recalculate()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlogvalue3daxisformatter.html#recalculate
    """
    #  void QLogValue3DAxisFormatter::recalculate()
    ritual = 'ritual_ZN24QLogValue3DAxisFormatter11recalculateEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN24QLogValue3DAxisFormatter11recalculateEv'
    self.uglySide.call(ritual)
