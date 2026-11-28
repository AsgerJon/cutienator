"""
QSGInternalRectangleNode binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qsgadaptationlayer_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QSGInternalRectangleNode to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from . import QSGVisitableNode

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QRectF
  from ..QtGui import QColor
  from . import QSGNodeVisitorEx
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']
  QRectF = WAIT['QRectF']
  QSGNodeVisitorEx = WAIT['QSGNodeVisitorEx']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSGInternalRectangleNode(QSGVisitableNode):
  """
  The cute side of Qt's QSGInternalRectangleNode: a plain Python object
  standing in front of one C++ QSGInternalRectangleNode.

  It is built on the cute 'QSGVisitableNode', as Qt's
  QSGInternalRectangleNode is built on Qt's QSGVisitableNode, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QSGInternalRectangleNode that has a ritual and that
  Python can call so far, 18 names in all: 'setRect', 'setColor',
  'setPenColor', 'setPenWidth', 'setGradientVertical', 'setRadius',
  'setTopLeftRadius', 'setTopRightRadius', 'setBottomLeftRadius',
  'setBottomRightRadius', 'resetTopLeftRadius', 'resetTopRightRadius',
  'resetBottomLeftRadius', 'resetBottomRightRadius', 'setAntialiasing',
  'setAligned', 'update', 'accept'. None can be made from Python: one comes
  out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSGInternalRectangleNode::~QSGInternalRectangleNode()': the
    destructor: Python never removes a C++ QSGInternalRectangleNode.
  - Qt's 'void QSGInternalRectangleNode::setGradientStops(const
    QGradientStops &stops)': takes a type Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ QSGInternalRectangleNode is created at the first use, not by
    'QSGInternalRectangleNode(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSGInternalRectangleNode.
  - Each name of Qt's QSGInternalRectangleNode that has no cute function yet,
    'setGradientStops', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSGInternalRectangleNode'

  #  A C++ QSGInternalRectangleNode Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSGInternalRectangleNode'

  #  The functions Qt calls itself that QSGInternalRectangleNode is the first
  #  to declare and that cannot be handed to Python yet, each as Qt declares
  #  it. A class of a program that writes one of them anew is refused, since
  #  Qt would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'setGradientStops': (
          'void QSGInternalRectangleNode::setGradientStops(const '
          'QGradientStops &)',
      ),
  }

  #  The functions Qt calls itself that QSGInternalRectangleNode is the first
  #  to declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'setRect': (
          ('_ZN24QSGInternalRectangleNode7setRectERK6QRectF',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QRectF'),
           )),
      ),
      'setColor': (
          ('_ZN24QSGInternalRectangleNode8setColorERK6QColor',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtGui:QColor'),
           )),
      ),
      'setPenColor': (
          ('_ZN24QSGInternalRectangleNode11setPenColorERK6QColor',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtGui:QColor'),
           )),
      ),
      'setPenWidth': (
          ('_ZN24QSGInternalRectangleNode11setPenWidthEd',
           ('nothing', 'nothing', ''),
           (
               ('double', 'number', ''),
           )),
      ),
      'setGradientVertical': (
          ('_ZN24QSGInternalRectangleNode19setGradientVerticalEb',
           ('nothing', 'nothing', ''),
           (
               ('bool', 'number', ''),
           )),
      ),
      'setRadius': (
          ('_ZN24QSGInternalRectangleNode9setRadiusEd',
           ('nothing', 'nothing', ''),
           (
               ('double', 'number', ''),
           )),
      ),
      'setTopLeftRadius': (
          ('_ZN24QSGInternalRectangleNode16setTopLeftRadiusEd',
           ('nothing', 'nothing', ''),
           (
               ('double', 'number', ''),
           )),
      ),
      'setTopRightRadius': (
          ('_ZN24QSGInternalRectangleNode17setTopRightRadiusEd',
           ('nothing', 'nothing', ''),
           (
               ('double', 'number', ''),
           )),
      ),
      'setBottomLeftRadius': (
          ('_ZN24QSGInternalRectangleNode19setBottomLeftRadiusEd',
           ('nothing', 'nothing', ''),
           (
               ('double', 'number', ''),
           )),
      ),
      'setBottomRightRadius': (
          ('_ZN24QSGInternalRectangleNode20setBottomRightRadiusEd',
           ('nothing', 'nothing', ''),
           (
               ('double', 'number', ''),
           )),
      ),
      'resetTopLeftRadius': (
          ('_ZN24QSGInternalRectangleNode18resetTopLeftRadiusEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'resetTopRightRadius': (
          ('_ZN24QSGInternalRectangleNode19resetTopRightRadiusEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'resetBottomLeftRadius': (
          ('_ZN24QSGInternalRectangleNode21resetBottomLeftRadiusEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'resetBottomRightRadius': (
          ('_ZN24QSGInternalRectangleNode22resetBottomRightRadiusEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'setAntialiasing': (
          ('_ZN24QSGInternalRectangleNode15setAntialiasingEb',
           ('nothing', 'nothing', ''),
           (
               ('bool', 'number', ''),
           )),
      ),
      'setAligned': (
          ('_ZN24QSGInternalRectangleNode10setAlignedEb',
           ('nothing', 'nothing', ''),
           (
               ('bool', 'number', ''),
           )),
      ),
      'update': (
          ('_ZN24QSGInternalRectangleNode6updateEv',
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

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QRectF)
  def setRect(self, rect: QRectF) -> None:
    """
    Calls Qt's 'void QSGInternalRectangleNode::setRect(const QRectF &rect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsginternalrectanglenode.html#setRect

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QSGInternalRectangleNode::setRect(const QRectF &rect)
    self.uglySide.call(
        'ritual_ZN24QSGInternalRectangleNode7setRectERK6QRectF',
        self._valueOf(rect),
    )

  @overload(QColor)
  def setColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QSGInternalRectangleNode::setColor(const QColor
    &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsginternalrectanglenode.html#setColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QSGInternalRectangleNode::setColor(const QColor &color)
    self.uglySide.call(
        'ritual_ZN24QSGInternalRectangleNode8setColorERK6QColor',
        self._valueOf(color),
    )

  @overload(QColor)
  def setPenColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QSGInternalRectangleNode::setPenColor(const QColor
    &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsginternalrectanglenode.html#setPenColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QSGInternalRectangleNode::setPenColor(const QColor &color)
    self.uglySide.call(
        'ritual_ZN24QSGInternalRectangleNode11setPenColorERK6QColor',
        self._valueOf(color),
    )

  @overload(float)
  def setPenWidth(self, width: float) -> None:
    """
    Calls Qt's 'void QSGInternalRectangleNode::setPenWidth(qreal width)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsginternalrectanglenode.html#setPenWidth

    Parameters
    ----------

    width : float
      Passed on as it is.
    """
    #  void QSGInternalRectangleNode::setPenWidth(qreal width)
    self.uglySide.call(
        'ritual_ZN24QSGInternalRectangleNode11setPenWidthEd', width,
    )

  @overload(bool)
  def setGradientVertical(self, vertical: bool) -> None:
    """
    Calls Qt's 'void QSGInternalRectangleNode::setGradientVertical(bool
    vertical)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsginternalrectanglenode.html#setGradientVertical

    Parameters
    ----------

    vertical : bool
      Passed on as it is.
    """
    #  void QSGInternalRectangleNode::setGradientVertical(bool vertical)
    self.uglySide.call(
        'ritual_ZN24QSGInternalRectangleNode19setGradientVerticalEb',
        vertical,
    )

  @overload(float)
  def setRadius(self, radius: float) -> None:
    """
    Calls Qt's 'void QSGInternalRectangleNode::setRadius(qreal radius)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsginternalrectanglenode.html#setRadius

    Parameters
    ----------

    radius : float
      Passed on as it is.
    """
    #  void QSGInternalRectangleNode::setRadius(qreal radius)
    self.uglySide.call(
        'ritual_ZN24QSGInternalRectangleNode9setRadiusEd', radius,
    )

  @overload(float)
  def setTopLeftRadius(self, radius: float) -> None:
    """
    Calls Qt's 'void QSGInternalRectangleNode::setTopLeftRadius(qreal
    radius)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsginternalrectanglenode.html#setTopLeftRadius

    Parameters
    ----------

    radius : float
      Passed on as it is.
    """
    #  void QSGInternalRectangleNode::setTopLeftRadius(qreal radius)
    self.uglySide.call(
        'ritual_ZN24QSGInternalRectangleNode16setTopLeftRadiusEd', radius,
    )

  @overload(float)
  def setTopRightRadius(self, radius: float) -> None:
    """
    Calls Qt's 'void QSGInternalRectangleNode::setTopRightRadius(qreal
    radius)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsginternalrectanglenode.html#setTopRightRadius

    Parameters
    ----------

    radius : float
      Passed on as it is.
    """
    #  void QSGInternalRectangleNode::setTopRightRadius(qreal radius)
    self.uglySide.call(
        'ritual_ZN24QSGInternalRectangleNode17setTopRightRadiusEd', radius,
    )

  @overload(float)
  def setBottomLeftRadius(self, radius: float) -> None:
    """
    Calls Qt's 'void QSGInternalRectangleNode::setBottomLeftRadius(qreal
    radius)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsginternalrectanglenode.html#setBottomLeftRadius

    Parameters
    ----------

    radius : float
      Passed on as it is.
    """
    #  void QSGInternalRectangleNode::setBottomLeftRadius(qreal radius)
    self.uglySide.call(
        'ritual_ZN24QSGInternalRectangleNode19setBottomLeftRadiusEd', radius,
    )

  @overload(float)
  def setBottomRightRadius(self, radius: float) -> None:
    """
    Calls Qt's 'void QSGInternalRectangleNode::setBottomRightRadius(qreal
    radius)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsginternalrectanglenode.html#setBottomRightRadius

    Parameters
    ----------

    radius : float
      Passed on as it is.
    """
    #  void QSGInternalRectangleNode::setBottomRightRadius(qreal radius)
    self.uglySide.call(
        'ritual_ZN24QSGInternalRectangleNode20setBottomRightRadiusEd',
        radius,
    )

  @overload(bool)
  def setAntialiasing(self, antialiasing: bool) -> None:
    """
    Calls Qt's 'void QSGInternalRectangleNode::setAntialiasing(bool
    antialiasing)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsginternalrectanglenode.html#setAntialiasing

    Parameters
    ----------

    antialiasing : bool
      Passed on as it is.
    """
    #  void QSGInternalRectangleNode::setAntialiasing(bool antialiasing)
    ritual = 'ritual_ZN24QSGInternalRectangleNode15setAntialiasingEb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN24QSGInternalRectangleNode15setAntialiasingEb'
    self.uglySide.call(ritual, antialiasing)

  @overload(bool)
  def setAligned(self, aligned: bool) -> None:
    """
    Calls Qt's 'void QSGInternalRectangleNode::setAligned(bool aligned)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsginternalrectanglenode.html#setAligned

    Parameters
    ----------

    aligned : bool
      Passed on as it is.
    """
    #  void QSGInternalRectangleNode::setAligned(bool aligned)
    self.uglySide.call(
        'ritual_ZN24QSGInternalRectangleNode10setAlignedEb', aligned,
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

  def resetTopLeftRadius(self) -> None:
    """
    Calls Qt's 'void QSGInternalRectangleNode::resetTopLeftRadius()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsginternalrectanglenode.html#resetTopLeftRadius
    """
    #  void QSGInternalRectangleNode::resetTopLeftRadius()
    self.uglySide.call(
        'ritual_ZN24QSGInternalRectangleNode18resetTopLeftRadiusEv',
    )

  def resetTopRightRadius(self) -> None:
    """
    Calls Qt's 'void QSGInternalRectangleNode::resetTopRightRadius()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsginternalrectanglenode.html#resetTopRightRadius
    """
    #  void QSGInternalRectangleNode::resetTopRightRadius()
    self.uglySide.call(
        'ritual_ZN24QSGInternalRectangleNode19resetTopRightRadiusEv',
    )

  def resetBottomLeftRadius(self) -> None:
    """
    Calls Qt's 'void QSGInternalRectangleNode::resetBottomLeftRadius()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsginternalrectanglenode.html
    """
    #  void QSGInternalRectangleNode::resetBottomLeftRadius()
    self.uglySide.call(
        'ritual_ZN24QSGInternalRectangleNode21resetBottomLeftRadiusEv',
    )

  def resetBottomRightRadius(self) -> None:
    """
    Calls Qt's 'void QSGInternalRectangleNode::resetBottomRightRadius()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsginternalrectanglenode.html
    """
    #  void QSGInternalRectangleNode::resetBottomRightRadius()
    self.uglySide.call(
        'ritual_ZN24QSGInternalRectangleNode22resetBottomRightRadiusEv',
    )

  def update(self) -> None:
    """
    Calls Qt's 'void QSGInternalRectangleNode::update()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsginternalrectanglenode.html#update
    """
    #  void QSGInternalRectangleNode::update()
    self.uglySide.call('ritual_ZN24QSGInternalRectangleNode6updateEv')

  @overload(QSGNodeVisitorEx)
  @overload(NoneType)
  def accept(self, visitor: Optional[QSGNodeVisitorEx]) -> None:
    """
    Calls Qt's 'void QSGInternalRectangleNode::accept(QSGNodeVisitorEx
    *visitor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsginternalrectanglenode.html#accept

    Parameters
    ----------

    visitor : Optional[QSGNodeVisitorEx]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGInternalRectangleNode::accept(QSGNodeVisitorEx *visitor)
    ritual = 'ritual_ZN24QSGInternalRectangleNode6acceptEP16QSGNodeVisitorEx'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN24QSGInternalRectangleNode6acceptEP16QSGNodeVisitor'
          'Ex')
    self.uglySide.call(ritual, self._addressOf(visitor))

  @staticmethod
  def setGradientStops(*__, **_) -> Never:
    """
    Qt's 'void QSGInternalRectangleNode::setGradientStops(const
    QGradientStops &stops)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSGInternalRectangleNode.setGradientStops' has no cute function "
        "yet. Qt's 'void QSGInternalRectangleNode::setGradientStops(const "
        "QGradientStops &stops)': takes a type Python has no way to hand "
        "over yet.")
