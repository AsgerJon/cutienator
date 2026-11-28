"""
QLayoutStyleInfo binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qgraphicslayout_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QLayoutStyleInfo to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import Qt
from . import QSizePolicy

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QStyle, QWidget
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QStyle = WAIT['QStyle']
  QWidget = WAIT['QWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QLayoutStyleInfo(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QLayoutStyleInfo: a plain Python object standing in
  front of one C++ QLayoutStyleInfo.

  C++ hands a QLayoutStyleInfo around as a copy, so every C++
  QLayoutStyleInfo behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QLayoutStyleInfo that has a ritual and that Python
  can call so far, 8 names in all: 'invalidate', 'style', 'widget', '__eq__',
  '__ne__', 'setDefaultSpacing', 'defaultSpacing', 'perItemSpacing'. It can
  be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QLayoutStyleInfo::~QLayoutStyleInfo()': the destructor: Python
    removes its C++ QLayoutStyleInfo by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QLayoutStyleInfo is created at the first use, not by
    'QLayoutStyleInfo(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QLayoutStyleInfo back gives a copy the ritual made
    for Python, in a new cute QLayoutStyleInfo.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QLayoutStyleInfo'

  #  Qt's '~QLayoutStyleInfo()'. Naming it makes this a value class: Python
  #  owns every C++ QLayoutStyleInfo behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN16QLayoutStyleInfoD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def style(self) -> Optional[QStyle]:
    """
    Calls Qt's 'QStyle *QLayoutStyleInfo::style() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlayoutstyleinfo.html#style

    Returns
    -------

    Optional[QStyle]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QStyle *QLayoutStyleInfo::style() const
    address = self.uglySide.call('ritual_ZNK16QLayoutStyleInfo5styleEv')
    from . import QStyle
    return QStyle._cuteAt(address)

  def widget(self) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget *QLayoutStyleInfo::widget() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlayoutstyleinfo.html#widget

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *QLayoutStyleInfo::widget() const
    address = self.uglySide.call('ritual_ZNK16QLayoutStyleInfo6widgetEv')
    from . import QWidget
    return QWidget._cuteAt(address)

  @overload(Qt.Orientation)
  def defaultSpacing(self, o: Qt.Orientation) -> float:
    """
    Calls Qt's 'qreal QLayoutStyleInfo::defaultSpacing(Qt::Orientation o)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlayoutstyleinfo.html#defaultSpacing

    Parameters
    ----------

    o : Qt.Orientation
      Passed on as its number.
    """
    #  qreal QLayoutStyleInfo::defaultSpacing(Qt::Orientation o) const
    return self.uglySide.call(
        'ritual_ZNK16QLayoutStyleInfo14defaultSpacingEN2Qt11OrientationE',
        o.value,
    )

  @overload(QSizePolicy.ControlType, QSizePolicy.ControlType, Qt.Orientation)
  def perItemSpacing(
      self,
      control1: QSizePolicy.ControlType,
      control2: QSizePolicy.ControlType,
      orientation: Qt.Orientation,
  ) -> float:
    """
    Calls Qt's 'qreal
    QLayoutStyleInfo::perItemSpacing(QSizePolicy::ControlType control1,
    QSizePolicy::ControlType control2, Qt::Orientation orientation) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlayoutstyleinfo.html#perItemSpacing

    Parameters
    ----------

    control1 : QSizePolicy.ControlType
      Passed on as its number.

    control2 : QSizePolicy.ControlType
      Passed on as its number.

    orientation : Qt.Orientation
      Passed on as its number.
    """
    #  qreal QLayoutStyleInfo::perItemSpacing(QSizePolicy::ControlType
    #      control1, QSizePolicy::ControlType control2, Qt::Orientation
    #      orientation) const
    return self.uglySide.call(
        'ritual_ZNK16QLayoutStyleInfo14perItemSpacingEN11QSizePolicy11Contr'
        'olTypeES1_N2Qt11OrientationE',
        control1.value, control2.value, orientation.value,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Qt.Orientation, float)
  def setDefaultSpacing(self, o: Qt.Orientation, spacing: float) -> None:
    """
    Calls Qt's 'void QLayoutStyleInfo::setDefaultSpacing(Qt::Orientation o,
    qreal spacing)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlayoutstyleinfo.html#setDefaultSpacing

    Parameters
    ----------

    o : Qt.Orientation
      Passed on as its number.

    spacing : float
      Passed on as it is.
    """
    #  void QLayoutStyleInfo::setDefaultSpacing(Qt::Orientation o, qreal
    #      spacing)
    self.uglySide.call(
        'ritual_ZN16QLayoutStyleInfo17setDefaultSpacingEN2Qt11OrientationEd',
        o.value, spacing,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, other: QLayoutStyleInfo) -> bool:
    """
    Calls Qt's 'bool QLayoutStyleInfo::operator==(const QLayoutStyleInfo
    &other) const'.

    Qt's own words: https://doc.qt.io/qt-6/qlayoutstyleinfo.html#operator==

    Parameters
    ----------

    other : QLayoutStyleInfo
      Passed on as a value: Qt reads the C++ QLayoutStyleInfo, which stays
      Python's own.
    """
    #  bool QLayoutStyleInfo::operator==(const QLayoutStyleInfo &other) const
    return self.uglySide.call(
        'ritual_ZNK16QLayoutStyleInfoeqERKS_', self._valueOf(other),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __ne__(self, other: QLayoutStyleInfo) -> bool:
    """
    Calls Qt's 'bool QLayoutStyleInfo::operator!=(const QLayoutStyleInfo
    &other) const'.

    Qt's own words: https://doc.qt.io/qt-6/qlayoutstyleinfo.html#operator!=

    Parameters
    ----------

    other : QLayoutStyleInfo
      Passed on as a value: Qt reads the C++ QLayoutStyleInfo, which stays
      Python's own.
    """
    #  bool QLayoutStyleInfo::operator!=(const QLayoutStyleInfo &other) const
    return self.uglySide.call(
        'ritual_ZNK16QLayoutStyleInfoneERKS_', self._valueOf(other),
    )

  @overload.fallback
  def __ne__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QLayoutStyleInfo::QLayoutStyleInfo()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qlayoutstyleinfo.html#QLayoutStyleInfo
    """
    #  QLayoutStyleInfo::QLayoutStyleInfo()
    self._noteCreation(QLayoutStyleInfo, lambda: Rituals.call(
        'ritual_ZN16QLayoutStyleInfoC1Ev',
    ))

  @overload(QStyle, QWidget)
  @overload(QStyle, NoneType)
  @overload(NoneType, QWidget)
  @overload(NoneType, NoneType)
  def __init__(
      self,
      style: Optional[QStyle],
      widget: Optional[QWidget],
  ) -> None:
    """
    Notes what was given, for Qt's 'QLayoutStyleInfo::QLayoutStyleInfo(QStyle
    *style, QWidget *widget)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qlayoutstyleinfo.html#QLayoutStyleInfo

    Parameters
    ----------

    style : Optional[QStyle]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QLayoutStyleInfo::QLayoutStyleInfo(QStyle *style, QWidget *widget)
    self._noteCreation(QLayoutStyleInfo, lambda: Rituals.call(
        'ritual_ZN16QLayoutStyleInfoC1EP6QStyleP7QWidget',
        self._addressOf(style), self._addressOf(widget),
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

  def invalidate(self) -> None:
    """
    Calls Qt's 'void QLayoutStyleInfo::invalidate()'.

    Qt's own words: https://doc.qt.io/qt-6/qlayoutstyleinfo.html#invalidate
    """
    #  void QLayoutStyleInfo::invalidate()
    self.uglySide.call('ritual_ZN16QLayoutStyleInfo10invalidateEv')
