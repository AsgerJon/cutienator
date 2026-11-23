"""
QFontVariableAxis binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/qfontvariableaxis.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList
from . import QFont

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QByteArray, QDebug
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDebug = WAIT['QDebug']


class QFontVariableAxis(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QFontVariableAxis: a plain Python object standing in
  front of one C++ QFontVariableAxis.

  C++ hands a QFontVariableAxis around as a copy, so every C++
  QFontVariableAxis behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QFontVariableAxis that has a ritual and that Python
  can call so far, 12 names in all: 'tag', 'setTag', 'name', 'setName',
  'minimumValue', 'setMinimumValue', 'maximumValue', 'setMaximumValue',
  'defaultValue', 'setDefaultValue', 'tagString', '__rlshift__'. It can be
  made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QFontVariableAxis::~QFontVariableAxis()': the destructor: Python
    removes its C++ QFontVariableAxis by it, and has no other use for it.

  What has no ritual
  ------------------

  10 of the 25 functions Qt declares: 6 takes or gives a type that cannot be
  passed yet; 3 declared and nowhere to be found; 1 a template.

  What to expect
  --------------

  - The C++ QFontVariableAxis is created at the first use, not by
    'QFontVariableAxis(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QFontVariableAxis back gives a copy the ritual made
    for Python, in a new cute QFontVariableAxis.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QFontVariableAxis'

  #  Qt's '~QFontVariableAxis()'. Naming it makes this a value class: Python
  #  owns every C++ QFontVariableAxis behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN17QFontVariableAxisD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def tag(self) -> QFont.Tag:
    """
    Calls Qt's 'QFont::Tag QFontVariableAxis::tag() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontvariableaxis.html#tag

    Returns
    -------

    QFont.Tag
      A new cute QFont::Tag around the copy Qt gave back. Python owns it.
    """
    #  QFont::Tag QFontVariableAxis::tag() const
    address = self.uglySide.call('ritual_ZNK17QFontVariableAxis3tagEv')
    return QFont.Tag._cuteOwning(address)

  def name(self) -> str:
    """
    Calls Qt's 'QString QFontVariableAxis::name() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontvariableaxis.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QFontVariableAxis::name() const
    return self.uglySide.call('ritual_ZNK17QFontVariableAxis4nameEv')

  def minimumValue(self) -> float:
    """
    Calls Qt's 'qreal QFontVariableAxis::minimumValue() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfontvariableaxis.html#minimumValue
    """
    #  qreal QFontVariableAxis::minimumValue() const
    return self.uglySide.call(
        'ritual_ZNK17QFontVariableAxis12minimumValueEv',
    )

  def maximumValue(self) -> float:
    """
    Calls Qt's 'qreal QFontVariableAxis::maximumValue() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfontvariableaxis.html#maximumValue
    """
    #  qreal QFontVariableAxis::maximumValue() const
    return self.uglySide.call(
        'ritual_ZNK17QFontVariableAxis12maximumValueEv',
    )

  def defaultValue(self) -> float:
    """
    Calls Qt's 'qreal QFontVariableAxis::defaultValue() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfontvariableaxis.html#defaultValue
    """
    #  qreal QFontVariableAxis::defaultValue() const
    return self.uglySide.call(
        'ritual_ZNK17QFontVariableAxis12defaultValueEv',
    )

  def tagString(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QFontVariableAxis::tagString() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontvariableaxis.html#tagString

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QFontVariableAxis::tagString() const
    address = self.uglySide.call('ritual_ZNK17QFontVariableAxis9tagStringEv')
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QFont.Tag)
  def setTag(self, tag: QFont.Tag) -> None:
    """
    Calls Qt's 'void QFontVariableAxis::setTag(QFont::Tag tag)'.

    Qt's own words: https://doc.qt.io/qt-6/qfontvariableaxis.html#setTag

    Parameters
    ----------

    tag : QFont.Tag
      Passed on as a value: Qt reads the C++ QFont::Tag, which stays Python's
      own.
    """
    #  void QFontVariableAxis::setTag(QFont::Tag tag)
    self.uglySide.call(
        'ritual_ZN17QFontVariableAxis6setTagEN5QFont3TagE',
        self._valueOf(tag),
    )

  @overload(str)
  def setName(self, name: str) -> None:
    """
    Calls Qt's 'void QFontVariableAxis::setName(const QString &name)'.

    Qt's own words: https://doc.qt.io/qt-6/qfontvariableaxis.html#setName

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QFontVariableAxis::setName(const QString &name)
    self.uglySide.call(
        'ritual_ZN17QFontVariableAxis7setNameERK7QString', name,
    )

  @overload(float)
  def setMinimumValue(self, minimumValue: float) -> None:
    """
    Calls Qt's 'void QFontVariableAxis::setMinimumValue(qreal minimumValue)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfontvariableaxis.html#setMinimumValue

    Parameters
    ----------

    minimumValue : float
      Passed on as it is.
    """
    #  void QFontVariableAxis::setMinimumValue(qreal minimumValue)
    self.uglySide.call(
        'ritual_ZN17QFontVariableAxis15setMinimumValueEd', minimumValue,
    )

  @overload(float)
  def setMaximumValue(self, maximumValue: float) -> None:
    """
    Calls Qt's 'void QFontVariableAxis::setMaximumValue(qreal maximumValue)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfontvariableaxis.html#setMaximumValue

    Parameters
    ----------

    maximumValue : float
      Passed on as it is.
    """
    #  void QFontVariableAxis::setMaximumValue(qreal maximumValue)
    self.uglySide.call(
        'ritual_ZN17QFontVariableAxis15setMaximumValueEd', maximumValue,
    )

  @overload(float)
  def setDefaultValue(self, defaultValue: float) -> None:
    """
    Calls Qt's 'void QFontVariableAxis::setDefaultValue(qreal defaultValue)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfontvariableaxis.html#setDefaultValue

    Parameters
    ----------

    defaultValue : float
      Passed on as it is.
    """
    #  void QFontVariableAxis::setDefaultValue(qreal defaultValue)
    self.uglySide.call(
        'ritual_ZN17QFontVariableAxis15setDefaultValueEd', defaultValue,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QDebug)
  def __rlshift__(self, debug: QDebug) -> QDebug:
    """
    Calls Qt's 'QDebug operator<<(QDebug debug, const QFontVariableAxis
    &axis)'.

    Qt's own words: https://doc.qt.io/qt-6/qfontvariableaxis.html#operator<<

    Parameters
    ----------

    debug : QDebug
      Passed on as a value: Qt reads the C++ QDebug, which stays Python's
      own.

    Returns
    -------

    QDebug
      A new cute QDebug around the copy Qt gave back. Python owns it.
    """
    #  QDebug operator<<(QDebug debug, const QFontVariableAxis &axis)
    address = Rituals.call(
        'ritual_Zls6QDebugRK17QFontVariableAxis',
        CuteMixin._valueOf(debug), CuteMixin._valueOf(self),
    )
    from ..QtCore import QDebug
    return QDebug._cuteOwning(address)

  @overload.fallback
  def __rlshift__(self, *args: object) -> object:
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
    Notes what was given, for Qt's 'QFontVariableAxis::QFontVariableAxis()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qfontvariableaxis.html#QFontVariableAxis
    """
    #  QFontVariableAxis::QFontVariableAxis()
    self._noteCreation(QFontVariableAxis, lambda: Rituals.call(
        'ritual_ZN17QFontVariableAxisC1Ev',
    ))

  @overload(THIS)
  def __init__(self, axis: QFontVariableAxis) -> None:
    """
    Notes what was given, for Qt's
    'QFontVariableAxis::QFontVariableAxis(const QFontVariableAxis &axis)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qfontvariableaxis.html#QFontVariableAxis

    Parameters
    ----------

    axis : QFontVariableAxis
      Passed on as a value: Qt reads the C++ QFontVariableAxis, which stays
      Python's own.
    """
    #  QFontVariableAxis::QFontVariableAxis(const QFontVariableAxis &axis)
    self._noteCreation(QFontVariableAxis, lambda: Rituals.call(
        'ritual_ZN17QFontVariableAxisC1ERKS_', self._valueOf(axis),
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


#  Qt's 'QList<QFontVariableAxis>': the list of QFontVariableAxis, which
#  'QList[QFontVariableAxis]' gives. It is made here, so that there is one as
#  soon as there can be a QFontVariableAxis.
QList.createKind(
    QFontVariableAxis, 'value',
    make='ritual_list_make_QFontVariableAxis',
    add='ritual_list_add_QFontVariableAxis',
    size='ritual_list_size_QFontVariableAxis',
    at='ritual_list_at_QFontVariableAxis',
    drop='ritual_list_drop_QFontVariableAxis',
)
