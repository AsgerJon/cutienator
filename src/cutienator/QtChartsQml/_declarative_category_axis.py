"""
DeclarativeCategoryAxis binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtChartsQml/6.12.0/QtChartsQml/private/declarativecategoryaxis_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means DeclarativeCategoryAxis to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteNum
from ..QtQml import QQmlParserStatus
from ..QtCharts import QCategoryAxis

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject


class DeclarativeCategoryAxis(QCategoryAxis, QQmlParserStatus):
  """
  The cute side of Qt's DeclarativeCategoryAxis: a plain Python object
  standing in front of one C++ DeclarativeCategoryAxis.

  It is built on the cute 'QCategoryAxis', as Qt's DeclarativeCategoryAxis is
  built on Qt's QCategoryAxis, and has everything that class has. It is built
  on the cute 'QQmlParserStatus' as well, as Qt's DeclarativeCategoryAxis is
  built on Qt's QQmlParserStatus too, and has everything that class has.

  What exists
  -----------

  Every function of Qt's DeclarativeCategoryAxis that has a ritual and that
  Python can call so far, 8 names in all: 'metaObject', 'classBegin',
  'componentComplete', 'labelsPosition', 'labelsPositionChanged', 'append',
  'remove', 'replace'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *DeclarativeCategoryAxis::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int DeclarativeCategoryAxis::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QQmlListProperty<QObject> DeclarativeCategoryAxis::axisChildren()':
    gives a type Python has no way to take yet.
  - Qt's 'bool DeclarativeCategoryAxis::endValueLessThan(const QPair<QString,
    qreal> &value1, const QPair<QString, qreal> &value2)': takes a type
    Python has no way to hand over yet.
  - Qt's 'void
    DeclarativeCategoryAxis::appendAxisChildren(QQmlListProperty<QObject>
    *list, QObject *element)': names 'QQmlListProperty<QObject>', which has
    no cute class yet.

  What has no ritual
  ------------------

  5 of the 18 functions Qt declares: 2 not a gap; 2 leans on
  'DeclarativeCategoryAxis; 1 leans on 'vtable for DeclarativeCategoryAxis',
  which Qt's source does not mark for use from outside Qt and has no code for
  that could be taken.

  What to expect
  --------------

  - The C++ DeclarativeCategoryAxis is created at the first use, not by
    'DeclarativeCategoryAxis(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ DeclarativeCategoryAxis.
  - Qt tells when it has removed the C++ DeclarativeCategoryAxis. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's DeclarativeCategoryAxis that has no cute function yet,
    '__init__', 'appendAxisChildren', 'axisChildren', 'endValueLessThan',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  #  The enums Qt writes inside DeclarativeCategoryAxis, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class AxisLabelsPosition(CuteNum):
    """
    The enum 'DeclarativeCategoryAxis::AxisLabelsPosition' of Qt, with the 2
    names Qt gives in it.
    """

    AxisLabelsPositionCenter = Kee[int](0)
    AxisLabelsPositionOnValue = Kee[int](1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'DeclarativeCategoryAxis'

  #  Qt's DeclarativeCategoryAxis is built on more than one class. The part
  #  of a C++ DeclarativeCategoryAxis that belongs to a class after the first
  #  begins somewhere inside the object, and the ritual named for that class
  #  gives where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QQmlParserStatus':
          'ritual_cast_DeclarativeCategoryAxis_QQmlParserStatus',
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
    Calls Qt's 'const QMetaObject *DeclarativeCategoryAxis::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativecategoryaxis.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *DeclarativeCategoryAxis::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK23DeclarativeCategoryAxis10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def labelsPosition(self) -> AxisLabelsPosition:
    """
    Calls Qt's 'AxisLabelsPosition DeclarativeCategoryAxis::labelsPosition()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativecategoryaxis.html#labelsPosition

    Returns
    -------

    AxisLabelsPosition
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'AxisLabelsPosition(number)' gives.
    """
    #  AxisLabelsPosition DeclarativeCategoryAxis::labelsPosition() const
    return DeclarativeCategoryAxis.AxisLabelsPosition(self.uglySide.call(
        'ritual_ZNK23DeclarativeCategoryAxis14labelsPositionEv',
    ))

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
    Qt's 'DeclarativeCategoryAxis::DeclarativeCategoryAxis(QObject *parent)':
    leans on 'vtable for DeclarativeCategoryAxis', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'DeclarativeCategoryAxis.__init__' has no cute function yet. Qt's "
        "'DeclarativeCategoryAxis::DeclarativeCategoryAxis(QObject "
        "*parent)': leans on 'vtable for DeclarativeCategoryAxis', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

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

  def classBegin(self) -> None:
    """
    Calls Qt's 'void DeclarativeCategoryAxis::classBegin()'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativecategoryaxis.html#classBegin
    """
    #  void DeclarativeCategoryAxis::classBegin()
    ritual = 'ritual_ZN23DeclarativeCategoryAxis10classBeginEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN23DeclarativeCategoryAxis10classBeginEv'
    self.uglySide.call(ritual)

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void DeclarativeCategoryAxis::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativecategoryaxis.html#componentComplete
    """
    #  void DeclarativeCategoryAxis::componentComplete()
    ritual = 'ritual_ZN23DeclarativeCategoryAxis17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN23DeclarativeCategoryAxis17componentCompleteEv'
    self.uglySide.call(ritual)

  @overload(AxisLabelsPosition)
  def labelsPositionChanged(self, position: AxisLabelsPosition) -> None:
    """
    Calls Qt's 'void
    DeclarativeCategoryAxis::labelsPositionChanged(AxisLabelsPosition
    position)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativecategoryaxis.html#labelsPositionChanged

    Parameters
    ----------

    position : AxisLabelsPosition
      Passed on as its number.
    """
    #  void DeclarativeCategoryAxis::labelsPositionChanged(AxisLabelsPosition
    #      position)
    self.uglySide.call(
        'ritual_ZN23DeclarativeCategoryAxis21labelsPositionChangedENS_18Axi'
        'sLabelsPositionE',
        position.value,
    )

  @overload(str, float)
  def append(self, label: str, categoryEndValue: float) -> None:
    """
    Calls Qt's 'void DeclarativeCategoryAxis::append(const QString &label,
    qreal categoryEndValue)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativecategoryaxis.html#append

    Parameters
    ----------

    label : str
      Passed on as it is: a QString is made of it for the call.

    categoryEndValue : float
      Passed on as it is.
    """
    #  void DeclarativeCategoryAxis::append(const QString &label, qreal
    #      categoryEndValue)
    self.uglySide.call(
        'ritual_ZN23DeclarativeCategoryAxis6appendERK7QStringd',
        label, categoryEndValue,
    )

  @overload(str)
  def remove(self, label: str) -> None:
    """
    Calls Qt's 'void DeclarativeCategoryAxis::remove(const QString &label)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativecategoryaxis.html#remove

    Parameters
    ----------

    label : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void DeclarativeCategoryAxis::remove(const QString &label)
    self.uglySide.call(
        'ritual_ZN23DeclarativeCategoryAxis6removeERK7QString', label,
    )

  @overload(str, str)
  def replace(self, oldLabel: str, newLabel: str) -> None:
    """
    Calls Qt's 'void DeclarativeCategoryAxis::replace(const QString
    &oldLabel, const QString &newLabel)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativecategoryaxis.html#replace

    Parameters
    ----------

    oldLabel : str
      Passed on as it is: a QString is made of it for the call.

    newLabel : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void DeclarativeCategoryAxis::replace(const QString &oldLabel, const
    #      QString &newLabel)
    self.uglySide.call(
        'ritual_ZN23DeclarativeCategoryAxis7replaceERK7QStringS2_',
        oldLabel, newLabel,
    )

  @staticmethod
  def appendAxisChildren(*__, **_) -> Never:
    """
    Qt's 'void
    DeclarativeCategoryAxis::appendAxisChildren(QQmlListProperty<QObject>
    *list, QObject *element)': names 'QQmlListProperty<QObject>', which has
    no cute class yet.
    """
    raise NotImplementedError(
        "'DeclarativeCategoryAxis.appendAxisChildren' has no cute function "
        "yet. Qt's 'void "
        "DeclarativeCategoryAxis::appendAxisChildren(QQmlListProperty<QObjec"
        "t> *list, QObject *element)': names 'QQmlListProperty<QObject>', "
        "which has no cute class yet.")

  @staticmethod
  def axisChildren(*__, **_) -> Never:
    """
    Qt's 'QQmlListProperty<QObject> DeclarativeCategoryAxis::axisChildren()':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'DeclarativeCategoryAxis.axisChildren' has no cute function yet. "
        "Qt's 'QQmlListProperty<QObject> "
        "DeclarativeCategoryAxis::axisChildren()': gives a type Python has "
        "no way to take yet.")

  @staticmethod
  def endValueLessThan(*__, **_) -> Never:
    """
    Qt's 'bool DeclarativeCategoryAxis::endValueLessThan(const QPair<QString,
    qreal> &value1, const QPair<QString, qreal> &value2)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'DeclarativeCategoryAxis.endValueLessThan' has no cute function "
        "yet. Qt's 'bool DeclarativeCategoryAxis::endValueLessThan(const "
        "QPair<QString, qreal> &value1, const QPair<QString, qreal> "
        "&value2)': takes a type Python has no way to hand over yet.")
