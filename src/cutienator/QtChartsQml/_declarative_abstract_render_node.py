"""
DeclarativeAbstractRenderNode binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtChartsQml/6.12.0/QtChartsQml/private/declarativeabstractrendernode_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means DeclarativeAbstractRenderNode to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtCore import QList
from ..QtQuick import QSGRootNode

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QRectF, QSize
  from ..QtGui import QMouseEvent
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMouseEvent = WAIT['QMouseEvent']
  QRectF = WAIT['QRectF']
  QSize = WAIT['QSize']


class DeclarativeAbstractRenderNode(QSGRootNode):
  """
  The cute side of Qt's DeclarativeAbstractRenderNode: a plain Python object
  standing in front of one C++ DeclarativeAbstractRenderNode.

  It is built on the cute 'QSGRootNode', as Qt's
  DeclarativeAbstractRenderNode is built on Qt's QSGRootNode, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's DeclarativeAbstractRenderNode that has a ritual and
  that Python can call so far, 5 names in all: 'setTextureSize',
  'textureSize', 'setRect', 'setAntialiasing', 'addMouseEvents'. None can be
  made from Python: one comes out of a function of another class that gives
  one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void DeclarativeAbstractRenderNode::setSeriesData(bool mapDirty,
    const GLXYDataMap &dataMap)': takes a type Python has no way to hand over
    yet.
  - Qt's 'void DeclarativeAbstractRenderNode::takeMouseEventResponses(
    QList<MouseEventResponse> &responses)': takes a type Python has no way to
    hand over yet.

  What has no ritual
  ------------------

  1 of the 8 functions Qt declares: 1 the class is abstract, so C++ cannot
  make one, and the C++ class of ours does not fill in every function it
  leaves open.

  What to expect
  --------------

  - The C++ DeclarativeAbstractRenderNode is created at the first use, not by
    'DeclarativeAbstractRenderNode(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ DeclarativeAbstractRenderNode.
  - Each name of Qt's DeclarativeAbstractRenderNode that has no cute function
    yet, '__init__', 'setSeriesData', 'takeMouseEventResponses', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'DeclarativeAbstractRenderNode'

  #  A C++ DeclarativeAbstractRenderNode Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_DeclarativeAbstractRenderNode'

  #  The functions Qt calls itself that DeclarativeAbstractRenderNode is the
  #  first to declare and that cannot be handed to Python yet, each as Qt
  #  declares it. A class of a program that writes one of them anew is
  #  refused, since Qt would never call what it wrote; see
  #  'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'setSeriesData': (
          'void DeclarativeAbstractRenderNode::setSeriesData(bool, const '
          'GLXYDataMap &)',
      ),
      'addMouseEvents': (
          'void DeclarativeAbstractRenderNode::addMouseEvents(const '
          'QList<QMouseEvent *> &)',
      ),
      'takeMouseEventResponses': (
          'void '
          'DeclarativeAbstractRenderNode::takeMouseEventResponses(QList<Mou'
          'seEventResponse> &)',
      ),
  }

  #  The functions Qt calls itself that DeclarativeAbstractRenderNode is the
  #  first to declare. A class of a program built on it can write one anew,
  #  and Qt then calls that. For each name: the key C++ knows the function
  #  by, what it gives, and what it takes.
  __virtual_functions__ = {
      'setTextureSize': (
          ('_ZN29DeclarativeAbstractRenderNode14setTextureSizeERK5QSize',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QSize'),
           )),
      ),
      'textureSize': (
          ('_ZNK29DeclarativeAbstractRenderNode11textureSizeEv',
           ('address', 'value', 'QtCore:QSize'),
           ()),
      ),
      'setRect': (
          ('_ZN29DeclarativeAbstractRenderNode7setRectERK6QRectF',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QRectF'),
           )),
      ),
      'setAntialiasing': (
          ('_ZN29DeclarativeAbstractRenderNode15setAntialiasingEb',
           ('nothing', 'nothing', ''),
           (
               ('bool', 'number', ''),
           )),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def textureSize(self) -> QSize:
    """
    Calls Qt's 'QSize DeclarativeAbstractRenderNode::textureSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativeabstractrendernode.html#textureSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize DeclarativeAbstractRenderNode::textureSize() const
    address = self._callAs(
        'DeclarativeAbstractRenderNode',
        'ritual_ZNK29DeclarativeAbstractRenderNode11textureSizeEv',
    )
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QSize)
  def setTextureSize(self, textureSize: QSize) -> None:
    """
    Calls Qt's 'void DeclarativeAbstractRenderNode::setTextureSize(const
    QSize &textureSize)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativeabstractrendernode.html#setTextureSize

    Parameters
    ----------

    textureSize : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void DeclarativeAbstractRenderNode::setTextureSize(const QSize
    #      &textureSize)
    self._callAs(
        'DeclarativeAbstractRenderNode',
        'ritual_ZN29DeclarativeAbstractRenderNode14setTextureSizeERK5QSize',
        self._valueOf(textureSize),
    )

  @overload(QRectF)
  def setRect(self, rect: QRectF) -> None:
    """
    Calls Qt's 'void DeclarativeAbstractRenderNode::setRect(const QRectF
    &rect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativeabstractrendernode.html#setRect

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void DeclarativeAbstractRenderNode::setRect(const QRectF &rect)
    self._callAs(
        'DeclarativeAbstractRenderNode',
        'ritual_ZN29DeclarativeAbstractRenderNode7setRectERK6QRectF',
        self._valueOf(rect),
    )

  @overload(bool)
  def setAntialiasing(self, enable: bool) -> None:
    """
    Calls Qt's 'void DeclarativeAbstractRenderNode::setAntialiasing(bool
    enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativeabstractrendernode.html#setAntialiasing

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void DeclarativeAbstractRenderNode::setAntialiasing(bool enable)
    self._callAs(
        'DeclarativeAbstractRenderNode',
        'ritual_ZN29DeclarativeAbstractRenderNode15setAntialiasingEb',
        enable,
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
    Qt's 'DeclarativeAbstractRenderNode::DeclarativeAbstractRenderNode()':
    the class is abstract, so C++ cannot make one, and the C++ class of ours
    does not fill in every function it leaves open.
    """
    raise NotImplementedError(
        "'DeclarativeAbstractRenderNode.__init__' has no cute function yet. "
        "Qt's "
        "'DeclarativeAbstractRenderNode::DeclarativeAbstractRenderNode()': "
        "the class is abstract, so C++ cannot make one, and the C++ class "
        "of ours does not fill in every function it leaves open.")

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

  @overload(QList[QMouseEvent])
  def addMouseEvents(self, events: QList[QMouseEvent]) -> None:
    """
    Calls Qt's 'void DeclarativeAbstractRenderNode::addMouseEvents(const
    QList<QMouseEvent *> &events)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativeabstractrendernode.html#addMouseEvents

    Parameters
    ----------

    events : QList[QMouseEvent]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void DeclarativeAbstractRenderNode::addMouseEvents(const
    #      QList<QMouseEvent *> &events)
    self._callAs(
        'DeclarativeAbstractRenderNode',
        'ritual_ZN29DeclarativeAbstractRenderNode14addMouseEventsERK5QListI'
        'P11QMouseEventE',
        self._valueOf(events),
    )

  @staticmethod
  def setSeriesData(*__, **_) -> Never:
    """
    Qt's 'void DeclarativeAbstractRenderNode::setSeriesData(bool mapDirty,
    const GLXYDataMap &dataMap)': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'DeclarativeAbstractRenderNode.setSeriesData' has no cute function "
        "yet. Qt's 'void DeclarativeAbstractRenderNode::setSeriesData(bool "
        "mapDirty, const GLXYDataMap &dataMap)': takes a type Python has no "
        "way to hand over yet.")

  @staticmethod
  def takeMouseEventResponses(*__, **_) -> Never:
    """
    Qt's 'void DeclarativeAbstractRenderNode::takeMouseEventResponses(
    QList<MouseEventResponse> &responses)': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'DeclarativeAbstractRenderNode.takeMouseEventResponses' has no "
        "cute function yet. Qt's 'void "
        "DeclarativeAbstractRenderNode::takeMouseEventResponses(QList<MouseE"
        "ventResponse> &responses)': takes a type Python has no way to hand "
        "over yet.")
