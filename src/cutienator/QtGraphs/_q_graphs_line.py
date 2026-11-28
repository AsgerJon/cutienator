"""
QGraphsLine binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGraphs/qgraphstheme.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QVariant
  from ..QtGui import QColor
  from ..QtQml import QJSValue
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']
  QJSValue = WAIT['QJSValue']


class QGraphsLine(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QGraphsLine: a plain Python object standing in front
  of one C++ QGraphsLine.

  C++ hands a QGraphsLine around as a copy, so every C++ QGraphsLine behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QGraphsLine that has a ritual and that Python can
  call so far, 14 names in all: 'create', 'mainColor', 'setMainColor',
  'subColor', 'setSubColor', 'mainWidth', 'setMainWidth', 'subWidth',
  'setSubWidth', 'labelTextColor', 'setLabelTextColor', 'detach', '__eq__',
  '__ne__'. It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QGraphsLine::QGraphsLine(QGraphsLine &&other)': takes a type Python
    has no way to hand over yet.
  - Qt's 'QGraphsLine::~QGraphsLine()': the destructor: Python removes its
    C++ QGraphsLine by it, and has no other use for it.
  - Qt's 'QGraphsLine &QGraphsLine::operator=(const QGraphsLine &other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'void QGraphsLine::swap(QGraphsLine &other)': takes a type Python
    has no way to hand over yet.
  - Qt's 'QGraphsLine &QGraphsLine::operator=(QGraphsLine &&other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'QVariant QGraphsLine::operator QVariant() const': an operator
    Python has no name for.

  What has no ritual
  ------------------

  3 of the 25 functions Qt declares: 3 not a gap.

  What to expect
  --------------

  - The C++ QGraphsLine is created at the first use, not by
    'QGraphsLine(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QGraphsLine back gives a copy the ritual made for
    Python, in a new cute QGraphsLine.
  - Each name of Qt's QGraphsLine that has no cute function yet, 'swap',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QJSValue)
  def create(params: QJSValue) -> QVariant:
    """
    Calls Qt's 'QVariant QGraphsLine::create(const QJSValue &params)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphsline.html#create

    Parameters
    ----------

    params : QJSValue
      Passed on as a value: Qt reads the C++ QJSValue, which stays Python's
      own.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QGraphsLine::create(const QJSValue &params)
    address = Rituals.call(
        'ritual_ZN11QGraphsLine6createERK8QJSValue',
        CuteMixin._valueOf(params),
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGraphsLine'

  #  Qt's '~QGraphsLine()'. Naming it makes this a value class: Python owns
  #  every C++ QGraphsLine behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN11QGraphsLineD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def mainColor(self) -> QColor:
    """
    Calls Qt's 'QColor QGraphsLine::mainColor() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphsline.html#mainColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QGraphsLine::mainColor() const
    address = self.uglySide.call('ritual_ZNK11QGraphsLine9mainColorEv')
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def subColor(self) -> QColor:
    """
    Calls Qt's 'QColor QGraphsLine::subColor() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphsline.html#subColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QGraphsLine::subColor() const
    address = self.uglySide.call('ritual_ZNK11QGraphsLine8subColorEv')
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def mainWidth(self) -> float:
    """
    Calls Qt's 'qreal QGraphsLine::mainWidth() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphsline.html#mainWidth
    """
    #  qreal QGraphsLine::mainWidth() const
    return self.uglySide.call('ritual_ZNK11QGraphsLine9mainWidthEv')

  def subWidth(self) -> float:
    """
    Calls Qt's 'qreal QGraphsLine::subWidth() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphsline.html#subWidth
    """
    #  qreal QGraphsLine::subWidth() const
    return self.uglySide.call('ritual_ZNK11QGraphsLine8subWidthEv')

  def labelTextColor(self) -> QColor:
    """
    Calls Qt's 'QColor QGraphsLine::labelTextColor() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphsline.html#labelTextColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QGraphsLine::labelTextColor() const
    address = self.uglySide.call('ritual_ZNK11QGraphsLine14labelTextColorEv')
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QColor)
  def setMainColor(self, newColor: QColor) -> None:
    """
    Calls Qt's 'void QGraphsLine::setMainColor(QColor newColor)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphsline.html#setMainColor

    Parameters
    ----------

    newColor : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QGraphsLine::setMainColor(QColor newColor)
    self.uglySide.call(
        'ritual_ZN11QGraphsLine12setMainColorE6QColor',
        self._valueOf(newColor),
    )

  @overload(QColor)
  def setSubColor(self, newColor: QColor) -> None:
    """
    Calls Qt's 'void QGraphsLine::setSubColor(QColor newColor)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphsline.html#setSubColor

    Parameters
    ----------

    newColor : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QGraphsLine::setSubColor(QColor newColor)
    self.uglySide.call(
        'ritual_ZN11QGraphsLine11setSubColorE6QColor',
        self._valueOf(newColor),
    )

  @overload(float)
  def setMainWidth(self, newWidth: float) -> None:
    """
    Calls Qt's 'void QGraphsLine::setMainWidth(qreal newWidth)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphsline.html#setMainWidth

    Parameters
    ----------

    newWidth : float
      Passed on as it is.
    """
    #  void QGraphsLine::setMainWidth(qreal newWidth)
    self.uglySide.call('ritual_ZN11QGraphsLine12setMainWidthEd', newWidth)

  @overload(float)
  def setSubWidth(self, newWidth: float) -> None:
    """
    Calls Qt's 'void QGraphsLine::setSubWidth(qreal newWidth)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphsline.html#setSubWidth

    Parameters
    ----------

    newWidth : float
      Passed on as it is.
    """
    #  void QGraphsLine::setSubWidth(qreal newWidth)
    self.uglySide.call('ritual_ZN11QGraphsLine11setSubWidthEd', newWidth)

  @overload(QColor)
  def setLabelTextColor(self, newColor: QColor) -> None:
    """
    Calls Qt's 'void QGraphsLine::setLabelTextColor(QColor newColor)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphsline.html#setLabelTextColor

    Parameters
    ----------

    newColor : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QGraphsLine::setLabelTextColor(QColor newColor)
    self.uglySide.call(
        'ritual_ZN11QGraphsLine17setLabelTextColorE6QColor',
        self._valueOf(newColor),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, rhs: QGraphsLine) -> bool:
    """
    Calls Qt's 'bool operator==(const QGraphsLine &lhs, const QGraphsLine
    &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphsline.html#operator==

    Parameters
    ----------

    rhs : QGraphsLine
      Passed on as a value: Qt reads the C++ QGraphsLine, which stays
      Python's own.
    """
    #  bool operator==(const QGraphsLine &lhs, const QGraphsLine &rhs)
    return Rituals.call(
        'ritual_ZeqRK11QGraphsLineS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
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
  def __ne__(self, rhs: QGraphsLine) -> bool:
    """
    Calls Qt's 'bool operator!=(const QGraphsLine &lhs, const QGraphsLine
    &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphsline.html#operator!=

    Parameters
    ----------

    rhs : QGraphsLine
      Passed on as a value: Qt reads the C++ QGraphsLine, which stays
      Python's own.
    """
    #  bool operator!=(const QGraphsLine &lhs, const QGraphsLine &rhs)
    return Rituals.call(
        'ritual_ZneRK11QGraphsLineS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
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
    Notes what was given, for Qt's 'QGraphsLine::QGraphsLine()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qgraphsline.html#QGraphsLine
    """
    #  QGraphsLine::QGraphsLine()
    self._noteCreation(QGraphsLine, lambda: Rituals.call(
        'ritual_ZN11QGraphsLineC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QGraphsLine) -> None:
    """
    Notes what was given, for Qt's 'QGraphsLine::QGraphsLine(const
    QGraphsLine &other)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qgraphsline.html#QGraphsLine

    Parameters
    ----------

    other : QGraphsLine
      Passed on as a value: Qt reads the C++ QGraphsLine, which stays
      Python's own.
    """
    #  QGraphsLine::QGraphsLine(const QGraphsLine &other)
    self._noteCreation(QGraphsLine, lambda: Rituals.call(
        'ritual_ZN11QGraphsLineC1ERKS_', self._valueOf(other),
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

  def detach(self) -> None:
    """
    Calls Qt's 'void QGraphsLine::detach()'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphsline.html#detach
    """
    #  void QGraphsLine::detach()
    self.uglySide.call('ritual_ZN11QGraphsLine6detachEv')

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QGraphsLine::swap(QGraphsLine &other)': takes a type Python
    has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QGraphsLine.swap' has no cute function yet. Qt's 'void "
        "QGraphsLine::swap(QGraphsLine &other)': takes a type Python has no "
        "way to hand over yet.")
