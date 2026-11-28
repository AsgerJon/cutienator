"""
QSGTextNode binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/qsgtextnode.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteNum, WAIT
from . import QSGTexture, QSGTransformNode

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QPointF, QRectF
  from ..QtGui import QColor, QTextDocument, QTextLayout
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']
  QPointF = WAIT['QPointF']
  QRectF = WAIT['QRectF']
  QTextDocument = WAIT['QTextDocument']
  QTextLayout = WAIT['QTextLayout']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSGTextNode(QSGTransformNode):
  """
  The cute side of Qt's QSGTextNode: a plain Python object standing in front
  of one C++ QSGTextNode.

  It is built on the cute 'QSGTransformNode', as Qt's QSGTextNode is built on
  Qt's QSGTransformNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSGTextNode that has a ritual and that Python can
  call so far, 25 names in all: 'setColor', 'color', 'setTextStyle',
  'textStyle', 'setStyleColor', 'styleColor', 'setLinkColor', 'linkColor',
  'setSelectionColor', 'selectionColor', 'setSelectionTextColor',
  'selectionTextColor', 'setRenderType', 'renderType',
  'setRenderTypeQuality', 'renderTypeQuality', 'setFiltering', 'filtering',
  'clear', 'setViewport', 'viewport', 'addTextLayout', 'addTextDocument',
  'doAddTextLayout', 'doAddTextDocument'. None can be made from Python: one
  comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSGTextNode::~QSGTextNode()': the destructor: Python never removes
    a C++ QSGTextNode.

  What to expect
  --------------

  - The C++ QSGTextNode is created at the first use, not by
    'QSGTextNode(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSGTextNode.
  """

  #  The enums Qt writes inside QSGTextNode, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class RenderType(CuteNum):
    """
    The enum 'QSGTextNode::RenderType' of Qt, with the 3 names Qt gives in
    it.
    """

    QtRendering = Kee[int](0)
    NativeRendering = Kee[int](1)
    CurveRendering = Kee[int](2)

  class TextStyle(CuteNum):
    """
    The enum 'QSGTextNode::TextStyle' of Qt, with the 4 names Qt gives in it.
    """

    Normal = Kee[int](0)
    Outline = Kee[int](1)
    Raised = Kee[int](2)
    Sunken = Kee[int](3)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSGTextNode'

  #  A C++ QSGTextNode Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSGTextNode'

  #  The functions Qt calls itself that QSGTextNode is the first to declare.
  #  A class of a program built on it can write one anew, and Qt then calls
  #  that. For each name: the key C++ knows the function by, what it gives,
  #  and what it takes.
  __virtual_functions__ = {
      'setColor': (
          ('_ZN11QSGTextNode8setColorE6QColor',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtGui:QColor'),
           )),
      ),
      'color': (
          ('_ZNK11QSGTextNode5colorEv',
           ('address', 'value', 'QtGui:QColor'),
           ()),
      ),
      'setTextStyle': (
          ('_ZN11QSGTextNode12setTextStyleENS_9TextStyleE',
           ('nothing', 'nothing', ''),
           (
               ('int', 'enum', 'QtQuick:QSGTextNode.TextStyle'),
           )),
      ),
      'textStyle': (
          ('_ZN11QSGTextNode9textStyleEv',
           ('int', 'enum', 'QtQuick:QSGTextNode.TextStyle'),
           ()),
      ),
      'setStyleColor': (
          ('_ZN11QSGTextNode13setStyleColorE6QColor',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtGui:QColor'),
           )),
      ),
      'styleColor': (
          ('_ZNK11QSGTextNode10styleColorEv',
           ('address', 'value', 'QtGui:QColor'),
           ()),
      ),
      'setLinkColor': (
          ('_ZN11QSGTextNode12setLinkColorE6QColor',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtGui:QColor'),
           )),
      ),
      'linkColor': (
          ('_ZNK11QSGTextNode9linkColorEv',
           ('address', 'value', 'QtGui:QColor'),
           ()),
      ),
      'setSelectionColor': (
          ('_ZN11QSGTextNode17setSelectionColorE6QColor',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtGui:QColor'),
           )),
      ),
      'selectionColor': (
          ('_ZNK11QSGTextNode14selectionColorEv',
           ('address', 'value', 'QtGui:QColor'),
           ()),
      ),
      'setSelectionTextColor': (
          ('_ZN11QSGTextNode21setSelectionTextColorE6QColor',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtGui:QColor'),
           )),
      ),
      'selectionTextColor': (
          ('_ZNK11QSGTextNode18selectionTextColorEv',
           ('address', 'value', 'QtGui:QColor'),
           ()),
      ),
      'setRenderType': (
          ('_ZN11QSGTextNode13setRenderTypeENS_10RenderTypeE',
           ('nothing', 'nothing', ''),
           (
               ('int', 'enum', 'QtQuick:QSGTextNode.RenderType'),
           )),
      ),
      'renderType': (
          ('_ZNK11QSGTextNode10renderTypeEv',
           ('int', 'enum', 'QtQuick:QSGTextNode.RenderType'),
           ()),
      ),
      'setRenderTypeQuality': (
          ('_ZN11QSGTextNode20setRenderTypeQualityEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'renderTypeQuality': (
          ('_ZNK11QSGTextNode17renderTypeQualityEv',
           ('int', 'number', ''),
           ()),
      ),
      'setFiltering': (
          ('_ZN11QSGTextNode12setFilteringEN10QSGTexture9FilteringE',
           ('nothing', 'nothing', ''),
           (
               ('int', 'enum', 'QtQuick:QSGTexture.Filtering'),
           )),
      ),
      'filtering': (
          ('_ZNK11QSGTextNode9filteringEv',
           ('int', 'enum', 'QtQuick:QSGTexture.Filtering'),
           ()),
      ),
      'clear': (
          ('_ZN11QSGTextNode5clearEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'setViewport': (
          ('_ZN11QSGTextNode11setViewportERK6QRectF',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QRectF'),
           )),
      ),
      'viewport': (
          ('_ZNK11QSGTextNode8viewportEv',
           ('address', 'value', 'QtCore:QRectF'),
           ()),
      ),
      'doAddTextLayout': (
          ('_ZN11QSGTextNode15doAddTextLayoutE7QPointFP11QTextLayoutiiii',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QPointF'),
               ('address', 'address', 'QtGui:QTextLayout'),
               ('int', 'number', ''),
               ('int', 'number', ''),
               ('int', 'number', ''),
               ('int', 'number', ''),
           )),
      ),
      'doAddTextDocument': (
          ('_ZN11QSGTextNode17doAddTextDocumentE7QPointFP13QTextDocumentii',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QPointF'),
               ('address', 'address', 'QtGui:QTextDocument'),
               ('int', 'number', ''),
               ('int', 'number', ''),
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

  def color(self) -> QColor:
    """
    Calls Qt's 'QColor QSGTextNode::color() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgtextnode.html#color

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QSGTextNode::color() const
    address = self.uglySide.call('ritual_ZNK11QSGTextNode5colorEv')
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def styleColor(self) -> QColor:
    """
    Calls Qt's 'QColor QSGTextNode::styleColor() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgtextnode.html#styleColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QSGTextNode::styleColor() const
    address = self.uglySide.call('ritual_ZNK11QSGTextNode10styleColorEv')
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def linkColor(self) -> QColor:
    """
    Calls Qt's 'QColor QSGTextNode::linkColor() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgtextnode.html#linkColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QSGTextNode::linkColor() const
    address = self.uglySide.call('ritual_ZNK11QSGTextNode9linkColorEv')
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def selectionColor(self) -> QColor:
    """
    Calls Qt's 'QColor QSGTextNode::selectionColor() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgtextnode.html#selectionColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QSGTextNode::selectionColor() const
    address = self.uglySide.call('ritual_ZNK11QSGTextNode14selectionColorEv')
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def selectionTextColor(self) -> QColor:
    """
    Calls Qt's 'QColor QSGTextNode::selectionTextColor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgtextnode.html#selectionTextColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QSGTextNode::selectionTextColor() const
    address = self.uglySide.call(
        'ritual_ZNK11QSGTextNode18selectionTextColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def renderType(self) -> RenderType:
    """
    Calls Qt's 'RenderType QSGTextNode::renderType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgtextnode.html#renderType

    Returns
    -------

    RenderType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'RenderType(number)'
      gives.
    """
    #  RenderType QSGTextNode::renderType() const
    return QSGTextNode.RenderType(self.uglySide.call(
        'ritual_ZNK11QSGTextNode10renderTypeEv',
    ))

  def renderTypeQuality(self) -> int:
    """
    Calls Qt's 'int QSGTextNode::renderTypeQuality() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgtextnode.html#renderTypeQuality
    """
    #  int QSGTextNode::renderTypeQuality() const
    return self.uglySide.call('ritual_ZNK11QSGTextNode17renderTypeQualityEv')

  def filtering(self) -> QSGTexture.Filtering:
    """
    Calls Qt's 'QSGTexture::Filtering QSGTextNode::filtering() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgtextnode.html#filtering

    Returns
    -------

    QSGTexture.Filtering
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QSGTexture.Filtering(number)' gives.
    """
    #  QSGTexture::Filtering QSGTextNode::filtering() const
    return QSGTexture.Filtering(self.uglySide.call(
        'ritual_ZNK11QSGTextNode9filteringEv',
    ))

  def viewport(self) -> QRectF:
    """
    Calls Qt's 'QRectF QSGTextNode::viewport() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgtextnode.html#viewport

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QSGTextNode::viewport() const
    address = self.uglySide.call('ritual_ZNK11QSGTextNode8viewportEv')
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QColor)
  def setColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QSGTextNode::setColor(QColor color)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgtextnode.html#setColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QSGTextNode::setColor(QColor color)
    self.uglySide.call(
        'ritual_ZN11QSGTextNode8setColorE6QColor', self._valueOf(color),
    )

  @overload(TextStyle)
  def setTextStyle(self, textStyle: TextStyle) -> None:
    """
    Calls Qt's 'void QSGTextNode::setTextStyle(TextStyle textStyle)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgtextnode.html#setTextStyle

    Parameters
    ----------

    textStyle : TextStyle
      Passed on as its number.
    """
    #  void QSGTextNode::setTextStyle(TextStyle textStyle)
    self.uglySide.call(
        'ritual_ZN11QSGTextNode12setTextStyleENS_9TextStyleE',
        textStyle.value,
    )

  @overload(QColor)
  def setStyleColor(self, styleColor: QColor) -> None:
    """
    Calls Qt's 'void QSGTextNode::setStyleColor(QColor styleColor)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgtextnode.html#setStyleColor

    Parameters
    ----------

    styleColor : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QSGTextNode::setStyleColor(QColor styleColor)
    self.uglySide.call(
        'ritual_ZN11QSGTextNode13setStyleColorE6QColor',
        self._valueOf(styleColor),
    )

  @overload(QColor)
  def setLinkColor(self, linkColor: QColor) -> None:
    """
    Calls Qt's 'void QSGTextNode::setLinkColor(QColor linkColor)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgtextnode.html#setLinkColor

    Parameters
    ----------

    linkColor : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QSGTextNode::setLinkColor(QColor linkColor)
    self.uglySide.call(
        'ritual_ZN11QSGTextNode12setLinkColorE6QColor',
        self._valueOf(linkColor),
    )

  @overload(QColor)
  def setSelectionColor(self, selectionColor: QColor) -> None:
    """
    Calls Qt's 'void QSGTextNode::setSelectionColor(QColor selectionColor)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgtextnode.html#setSelectionColor

    Parameters
    ----------

    selectionColor : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QSGTextNode::setSelectionColor(QColor selectionColor)
    self.uglySide.call(
        'ritual_ZN11QSGTextNode17setSelectionColorE6QColor',
        self._valueOf(selectionColor),
    )

  @overload(QColor)
  def setSelectionTextColor(self, selectionTextColor: QColor) -> None:
    """
    Calls Qt's 'void QSGTextNode::setSelectionTextColor(QColor
    selectionTextColor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgtextnode.html#setSelectionTextColor

    Parameters
    ----------

    selectionTextColor : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QSGTextNode::setSelectionTextColor(QColor selectionTextColor)
    self.uglySide.call(
        'ritual_ZN11QSGTextNode21setSelectionTextColorE6QColor',
        self._valueOf(selectionTextColor),
    )

  @overload(RenderType)
  def setRenderType(self, renderType: RenderType) -> None:
    """
    Calls Qt's 'void QSGTextNode::setRenderType(RenderType renderType)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgtextnode.html#setRenderType

    Parameters
    ----------

    renderType : RenderType
      Passed on as its number.
    """
    #  void QSGTextNode::setRenderType(RenderType renderType)
    self.uglySide.call(
        'ritual_ZN11QSGTextNode13setRenderTypeENS_10RenderTypeE',
        renderType.value,
    )

  @overload(int)
  def setRenderTypeQuality(self, renderTypeQuality: int) -> None:
    """
    Calls Qt's 'void QSGTextNode::setRenderTypeQuality(int
    renderTypeQuality)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgtextnode.html#setRenderTypeQuality

    Parameters
    ----------

    renderTypeQuality : int
      Passed on as it is.
    """
    #  void QSGTextNode::setRenderTypeQuality(int renderTypeQuality)
    self.uglySide.call(
        'ritual_ZN11QSGTextNode20setRenderTypeQualityEi', renderTypeQuality,
    )

  @overload(QSGTexture.Filtering)
  def setFiltering(self, a0: QSGTexture.Filtering) -> None:
    """
    Calls Qt's 'void QSGTextNode::setFiltering(QSGTexture::Filtering a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgtextnode.html#setFiltering

    Parameters
    ----------

    a0 : QSGTexture.Filtering
      Passed on as its number.
    """
    #  void QSGTextNode::setFiltering(QSGTexture::Filtering a0)
    self.uglySide.call(
        'ritual_ZN11QSGTextNode12setFilteringEN10QSGTexture9FilteringE',
        a0.value,
    )

  @overload(QRectF)
  def setViewport(self, viewport: QRectF) -> None:
    """
    Calls Qt's 'void QSGTextNode::setViewport(const QRectF &viewport)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgtextnode.html#setViewport

    Parameters
    ----------

    viewport : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QSGTextNode::setViewport(const QRectF &viewport)
    self.uglySide.call(
        'ritual_ZN11QSGTextNode11setViewportERK6QRectF',
        self._valueOf(viewport),
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

  def textStyle(self) -> TextStyle:
    """
    Calls Qt's 'TextStyle QSGTextNode::textStyle()'.

    Qt's own words: https://doc.qt.io/qt-6/qsgtextnode.html#textStyle

    Returns
    -------

    TextStyle
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'TextStyle(number)' gives.
    """
    #  TextStyle QSGTextNode::textStyle()
    return QSGTextNode.TextStyle(self.uglySide.call(
        'ritual_ZN11QSGTextNode9textStyleEv',
    ))

  def clear(self) -> None:
    """
    Calls Qt's 'void QSGTextNode::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qsgtextnode.html#clear
    """
    #  void QSGTextNode::clear()
    self.uglySide.call('ritual_ZN11QSGTextNode5clearEv')

  @overload(QPointF, QTextLayout)
  @overload(QPointF, NoneType)
  @overload(QPointF, QTextLayout, int)
  @overload(QPointF, NoneType, int)
  @overload(QPointF, QTextLayout, int, int)
  @overload(QPointF, NoneType, int, int)
  @overload(QPointF, QTextLayout, int, int, int)
  @overload(QPointF, NoneType, int, int, int)
  @overload(QPointF, QTextLayout, int, int, int, int)
  @overload(QPointF, NoneType, int, int, int, int)
  def addTextLayout(
      self,
      position: QPointF,
      layout: Optional[QTextLayout],
      selectionStart: int = -1,
      selectionCount: int = -1,
      lineStart: int = 0,
      lineCount: int = -1,
  ) -> None:
    """
    Calls Qt's 'void QSGTextNode::addTextLayout(QPointF position, QTextLayout
    *layout, int selectionStart, int selectionCount, int lineStart, int
    lineCount)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgtextnode.html#addTextLayout

    Parameters
    ----------

    position : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    layout : Optional[QTextLayout]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    selectionStart : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    selectionCount : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    lineStart : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    lineCount : int
      Passed on as it is. May be left out, as in Qt: it is then -1.
    """
    #  void QSGTextNode::addTextLayout(QPointF position, QTextLayout *layout,
    #      int selectionStart, int selectionCount, int lineStart, int
    #      lineCount)
    self.uglySide.call(
        'ritual_ZN11QSGTextNode13addTextLayoutE7QPointFP11QTextLayoutiiii',
        self._valueOf(position, 'QPointF'), self._addressOf(layout),
        selectionStart, selectionCount, lineStart, lineCount,
    )

  @overload(QPointF, QTextDocument)
  @overload(QPointF, NoneType)
  @overload(QPointF, QTextDocument, int)
  @overload(QPointF, NoneType, int)
  @overload(QPointF, QTextDocument, int, int)
  @overload(QPointF, NoneType, int, int)
  def addTextDocument(
      self,
      position: QPointF,
      document: Optional[QTextDocument],
      selectionStart: int = -1,
      selectionCount: int = -1,
  ) -> None:
    """
    Calls Qt's 'void QSGTextNode::addTextDocument(QPointF position,
    QTextDocument *document, int selectionStart, int selectionCount)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgtextnode.html#addTextDocument

    Parameters
    ----------

    position : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    document : Optional[QTextDocument]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    selectionStart : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    selectionCount : int
      Passed on as it is. May be left out, as in Qt: it is then -1.
    """
    #  void QSGTextNode::addTextDocument(QPointF position, QTextDocument
    #      *document, int selectionStart, int selectionCount)
    self.uglySide.call(
        'ritual_ZN11QSGTextNode15addTextDocumentE7QPointFP13QTextDocumentii',
        self._valueOf(position, 'QPointF'), self._addressOf(document),
        selectionStart, selectionCount,
    )

  @overload(QPointF, QTextLayout, int, int, int, int)
  @overload(QPointF, NoneType, int, int, int, int)
  def doAddTextLayout(
      self,
      position: QPointF,
      layout: Optional[QTextLayout],
      selectionStart: int,
      selectionCount: int,
      lineStart: int,
      lineCount: int,
  ) -> None:
    """
    Calls Qt's 'void QSGTextNode::doAddTextLayout(QPointF position,
    QTextLayout *layout, int selectionStart, int selectionCount, int
    lineStart, int lineCount)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgtextnode.html#doAddTextLayout

    Parameters
    ----------

    position : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    layout : Optional[QTextLayout]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    selectionStart : int
      Passed on as it is.

    selectionCount : int
      Passed on as it is.

    lineStart : int
      Passed on as it is.

    lineCount : int
      Passed on as it is.
    """
    #  void QSGTextNode::doAddTextLayout(QPointF position, QTextLayout
    #      *layout, int selectionStart, int selectionCount, int lineStart,
    #      int lineCount)
    self.uglySide.call(
        'ritual_ZN11QSGTextNode15doAddTextLayoutE7QPointFP11QTextLayoutiiii',
        self._valueOf(position, 'QPointF'), self._addressOf(layout),
        selectionStart, selectionCount, lineStart, lineCount,
    )

  @overload(QPointF, QTextDocument, int, int)
  @overload(QPointF, NoneType, int, int)
  def doAddTextDocument(
      self,
      position: QPointF,
      document: Optional[QTextDocument],
      selectionStart: int,
      selectionCount: int,
  ) -> None:
    """
    Calls Qt's 'void QSGTextNode::doAddTextDocument(QPointF position,
    QTextDocument *document, int selectionStart, int selectionCount)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgtextnode.html#doAddTextDocument

    Parameters
    ----------

    position : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    document : Optional[QTextDocument]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    selectionStart : int
      Passed on as it is.

    selectionCount : int
      Passed on as it is.
    """
    #  void QSGTextNode::doAddTextDocument(QPointF position, QTextDocument
    #      *document, int selectionStart, int selectionCount)
    self.uglySide.call(
        'ritual_ZN11QSGTextNode17doAddTextDocumentE7QPointFP13QTextDocument'
        'ii',
        self._valueOf(position, 'QPointF'), self._addressOf(document),
        selectionStart, selectionCount,
    )
