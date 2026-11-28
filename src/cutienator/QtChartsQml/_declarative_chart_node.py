"""
DeclarativeChartNode binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtChartsQml/6.12.0/QtChartsQml/private/declarativechartnode_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means DeclarativeChartNode to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtQuick import QSGRootNode

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QRectF
  from ..QtGui import QImage
  from . import DeclarativeAbstractRenderNode
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QImage = WAIT['QImage']
  QRectF = WAIT['QRectF']


class DeclarativeChartNode(QSGRootNode):
  """
  The cute side of Qt's DeclarativeChartNode: a plain Python object standing
  in front of one C++ DeclarativeChartNode.

  It is built on the cute 'QSGRootNode', as Qt's DeclarativeChartNode is
  built on Qt's QSGRootNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's DeclarativeChartNode that has a ritual and that
  Python can call so far, 3 names in all: 'createTextureFromImage',
  'renderNode', 'setRect'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'DeclarativeChartNode::~DeclarativeChartNode()': the destructor:
    Python never removes a C++ DeclarativeChartNode.

  What has no ritual
  ------------------

  1 of the 5 functions Qt declares: 1 leans on 'DeclarativeOpenGLRenderNode.

  What to expect
  --------------

  - The C++ DeclarativeChartNode is created at the first use, not by
    'DeclarativeChartNode(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ DeclarativeChartNode.
  - Each name of Qt's DeclarativeChartNode that has no cute function yet,
    '__init__', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'DeclarativeChartNode'

  #  A C++ DeclarativeChartNode Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_DeclarativeChartNode'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def renderNode(self) -> Optional[DeclarativeAbstractRenderNode]:
    """
    Calls Qt's 'DeclarativeAbstractRenderNode
    *DeclarativeChartNode::renderNode() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativechartnode.html#renderNode

    Returns
    -------

    Optional[DeclarativeAbstractRenderNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DeclarativeAbstractRenderNode *DeclarativeChartNode::renderNode()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK20DeclarativeChartNode10renderNodeEv',
    )
    from . import DeclarativeAbstractRenderNode
    return DeclarativeAbstractRenderNode._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QRectF)
  def setRect(self, rect: QRectF) -> None:
    """
    Calls Qt's 'void DeclarativeChartNode::setRect(const QRectF &rect)'.

    Qt's own words: https://doc.qt.io/qt-6/declarativechartnode.html#setRect

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void DeclarativeChartNode::setRect(const QRectF &rect)
    self.uglySide.call(
        'ritual_ZN20DeclarativeChartNode7setRectERK6QRectF',
        self._valueOf(rect),
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
    Qt's 'DeclarativeChartNode::DeclarativeChartNode(QQuickWindow *window)':
    leans on 'DeclarativeOpenGLRenderNode::staticMetaObject', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'DeclarativeChartNode.__init__' has no cute function yet. Qt's "
        "'DeclarativeChartNode::DeclarativeChartNode(QQuickWindow "
        "*window)': leans on "
        "'DeclarativeOpenGLRenderNode::staticMetaObject', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

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

  @overload(QImage)
  def createTextureFromImage(self, chartImage: QImage) -> None:
    """
    Calls Qt's 'void DeclarativeChartNode::createTextureFromImage(const
    QImage &chartImage)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativechartnode.html#createTextureFromImage

    Parameters
    ----------

    chartImage : QImage
      Passed on as a value: Qt reads the C++ QImage, which stays Python's
      own.
    """
    #  void DeclarativeChartNode::createTextureFromImage(const QImage
    #      &chartImage)
    self.uglySide.call(
        'ritual_ZN20DeclarativeChartNode22createTextureFromImageERK6QImage',
        self._valueOf(chartImage),
    )
