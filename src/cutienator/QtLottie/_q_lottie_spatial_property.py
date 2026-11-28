"""
QLottieSpatialProperty binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLottie/6.12.0/QtLottie/private/qlottiespatialproperty_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QLottieSpatialProperty to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QJsonObject, QPointF
  from ..QtGui import QPainterPath
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QJsonObject = WAIT['QJsonObject']
  QPointF = WAIT['QPointF']


class QLottieSpatialProperty(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QLottieSpatialProperty: a plain Python object
  standing in front of one C++ QLottieSpatialProperty.

  C++ hands a QLottieSpatialProperty around as a copy, so every C++
  QLottieSpatialProperty behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QLottieSpatialProperty that has a ritual and that
  Python can call so far, 7 names in all: 'construct', 'update', 'hasCurves',
  'subPaths', 'moveTo', 'lineTo', 'cubicTo'. None can be made from Python:
  one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'EasingSegment<QPointF> QLottieSpatialProperty::parseKeyframe(const
    QJsonObject keyframe, bool fromExpression)': gives a type Python has no
    way to take yet.
  - Qt's 'EasingSegment<QPointF> QLottieSpatialProperty::parseKeyframe(const
    QJsonObject keyframe, const QJsonObject nextKeyframe, bool
    fromExpression)': gives a type Python has no way to take yet.
  - Qt's 'QLottieSpatialProperty::~QLottieSpatialProperty()': the destructor:
    Python removes its C++ QLottieSpatialProperty by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QLottieSpatialProperty is created at the first use, not by
    'QLottieSpatialProperty(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QLottieSpatialProperty back gives a copy the ritual
    made for Python, in a new cute QLottieSpatialProperty.
  - Each name of Qt's QLottieSpatialProperty that has no cute function yet,
    'parseKeyframe', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QLottieSpatialProperty'

  #  The functions Qt calls itself that QLottieSpatialProperty is the first
  #  to declare and that cannot be handed to Python yet, each as Qt declares
  #  it. A class of a program that writes one of them anew is refused, since
  #  Qt would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'parseKeyframe': (
          'EasingSegment<QPointF> '
          'QLottieSpatialProperty::parseKeyframe(const QJsonObject, bool)',
          'EasingSegment<QPointF> '
          'QLottieSpatialProperty::parseKeyframe(const QJsonObject, const '
          'QJsonObject, bool)',
      ),
  }

  #  The functions Qt calls itself that QLottieSpatialProperty is the first
  #  to declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'construct': (
          ('_ZN22QLottieSpatialProperty9constructERK11QJsonObject',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QJsonObject'),
           )),
      ),
      'update': (
          ('_ZN22QLottieSpatialProperty6updateEi',
           ('bool', 'number', ''),
           (
               ('int', 'number', ''),
           )),
      ),
  }

  #  Qt's '~QLottieSpatialProperty()'. Naming it makes this a value class:
  #  Python owns every C++ QLottieSpatialProperty behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN22QLottieSpatialPropertyD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def hasCurves(self) -> bool:
    """
    Calls Qt's 'bool QLottieSpatialProperty::hasCurves() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlottiespatialproperty.html#hasCurves
    """
    #  bool QLottieSpatialProperty::hasCurves() const
    return self.uglySide.call(
        'ritual_ZNK22QLottieSpatialProperty9hasCurvesEv',
    )

  def subPaths(self) -> QList[QPainterPath]:
    """
    Calls Qt's 'const QList<QPainterPath> &QLottieSpatialProperty::subPaths()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlottiespatialproperty.html#subPaths

    Returns
    -------

    QList[QPainterPath]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  const QList<QPainterPath> &QLottieSpatialProperty::subPaths() const
    address = self.uglySide.call(
        'ritual_ZNK22QLottieSpatialProperty8subPathsEv',
    )
    from ..QtGui import QPainterPath
    return QList[QPainterPath]._cuteOwning(address)

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

  @overload(QJsonObject)
  def construct(self, definition: QJsonObject) -> None:
    """
    Calls Qt's 'void QLottieSpatialProperty::construct(const QJsonObject
    &definition)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlottiespatialproperty.html#construct

    Parameters
    ----------

    definition : QJsonObject
      Passed on as a value: Qt reads the C++ QJsonObject, which stays
      Python's own.
    """
    #  void QLottieSpatialProperty::construct(const QJsonObject &definition)
    ritual = 'ritual_ZN22QLottieSpatialProperty9constructERK11QJsonObject'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN22QLottieSpatialProperty9constructERK11QJsonObject')
    self.uglySide.call(ritual, self._valueOf(definition))

  @overload(int)
  def update(self, frame: int) -> bool:
    """
    Calls Qt's 'bool QLottieSpatialProperty::update(int frame)'.

    Qt's own words: https://doc.qt.io/qt-6/qlottiespatialproperty.html#update

    Parameters
    ----------

    frame : int
      Passed on as it is.
    """
    #  bool QLottieSpatialProperty::update(int frame)
    ritual = 'ritual_ZN22QLottieSpatialProperty6updateEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN22QLottieSpatialProperty6updateEi'
    return self.uglySide.call(ritual, frame)

  @overload(QPointF)
  def moveTo(self, e: QPointF) -> None:
    """
    Calls Qt's 'void QLottieSpatialProperty::moveTo(const QPointF &e)'.

    Qt's own words: https://doc.qt.io/qt-6/qlottiespatialproperty.html#moveTo

    Parameters
    ----------

    e : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QLottieSpatialProperty::moveTo(const QPointF &e)
    self.uglySide.call(
        'ritual_ZN22QLottieSpatialProperty6moveToERK7QPointF',
        self._valueOf(e, 'QPointF'),
    )

  @overload(QPointF)
  def lineTo(self, e: QPointF) -> None:
    """
    Calls Qt's 'void QLottieSpatialProperty::lineTo(const QPointF &e)'.

    Qt's own words: https://doc.qt.io/qt-6/qlottiespatialproperty.html#lineTo

    Parameters
    ----------

    e : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QLottieSpatialProperty::lineTo(const QPointF &e)
    self.uglySide.call(
        'ritual_ZN22QLottieSpatialProperty6lineToERK7QPointF',
        self._valueOf(e, 'QPointF'),
    )

  @overload(QPointF, QPointF, QPointF)
  def cubicTo(self, c1: QPointF, c2: QPointF, e: QPointF) -> None:
    """
    Calls Qt's 'void QLottieSpatialProperty::cubicTo(const QPointF &c1, const
    QPointF &c2, const QPointF &e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlottiespatialproperty.html#cubicTo

    Parameters
    ----------

    c1 : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    c2 : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    e : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QLottieSpatialProperty::cubicTo(const QPointF &c1, const QPointF
    #      &c2, const QPointF &e)
    self.uglySide.call(
        'ritual_ZN22QLottieSpatialProperty7cubicToERK7QPointFS2_S2_',
        self._valueOf(c1, 'QPointF'), self._valueOf(c2, 'QPointF'),
        self._valueOf(e, 'QPointF'),
    )

  @staticmethod
  def parseKeyframe(*__, **_) -> Never:
    """
    - Qt's 'EasingSegment<QPointF>
      QLottieSpatialProperty::parseKeyframe(const QJsonObject keyframe, bool
      fromExpression)': gives a type Python has no way to take yet.
    - Qt's 'EasingSegment<QPointF>
      QLottieSpatialProperty::parseKeyframe(const QJsonObject keyframe, const
      QJsonObject nextKeyframe, bool fromExpression)': gives a type Python
      has no way to take yet.
    """
    raise NotImplementedError(
        "'QLottieSpatialProperty.parseKeyframe' has no cute function yet. "
        "Qt's 'EasingSegment<QPointF> "
        "QLottieSpatialProperty::parseKeyframe(const QJsonObject keyframe, "
        "bool fromExpression)': gives a type Python has no way to take yet. "
        "Qt's 'EasingSegment<QPointF> "
        "QLottieSpatialProperty::parseKeyframe(const QJsonObject keyframe, "
        "const QJsonObject nextKeyframe, bool fromExpression)': gives a "
        "type Python has no way to take yet.")
