"""
QQuickTextPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquicktext_p_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QQuickTextPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from . import QQuickImplicitSizeItemPrivate, QQuickText

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QPointF, QSizeF
  from ..QtGui import QHoverEvent, QTextLayout, QTextLine
  from . import QQuickItem
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QHoverEvent = WAIT['QHoverEvent']
  QPointF = WAIT['QPointF']
  QQuickItem = WAIT['QQuickItem']
  QSizeF = WAIT['QSizeF']
  QTextLayout = WAIT['QTextLayout']
  QTextLine = WAIT['QTextLine']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickTextPrivate(QQuickImplicitSizeItemPrivate):
  """
  The cute side of Qt's QQuickTextPrivate: a plain Python object standing in
  front of one C++ QQuickTextPrivate.

  It is built on the cute 'QQuickImplicitSizeItemPrivate', as Qt's
  QQuickTextPrivate is built on Qt's QQuickImplicitSizeItemPrivate, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickTextPrivate that has a ritual and that Python
  can call so far, 37 names in all: 'q_func', 'init', 'updateBaseline',
  'updateSize', 'signalSizeChange', 'updateLayout',
  'determineHorizontalAlignment', 'setHAlign', 'mirrorChange',
  'isLineLaidOutConnected', 'lineHeightOffset', 'elidedText', 'clearFormats',
  'processHoverEvent', 'transformChanged', 'getImplicitWidth',
  'getImplicitHeight', 'availableWidth', 'availableHeight', 'padding',
  'setTopPadding', 'setLeftPadding', 'setRightPadding', 'setBottomPadding',
  'ensureDoc', 'updateDocumentText', 'isLinkActivatedConnected',
  'isLinkHoveredConnected', 'anchorAt', 'lineHeight', 'maximumLineCount',
  'renderTypeQuality', 'lineHeightMode', 'fontSizeMode', 'minimumPixelSize',
  'minimumPointSize', 'get'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QQuickText *QQuickTextPrivate::q_func() const': takes in
    Python what 'QQuickText *QQuickTextPrivate::q_func()' takes.
  - Qt's 'QQuickTextPrivate::~QQuickTextPrivate()': the destructor: Python
    never removes a C++ QQuickTextPrivate.
  - Qt's 'void QQuickTextPrivate::setLineGeometry(QTextLine &line, qreal
    lineWidth, qreal &height)': takes a type Python has no way to hand over
    yet.
  - Qt's 'void QQuickTextPrivate::positionInlineImages(const QTextLine &line,
    const QList<QTextLayout::FormatRange> &formats)': takes a type Python has
    no way to hand over yet.
  - Qt's 'void QQuickTextPrivate::elideFormats(int start, int length, int
    offset, QList<QTextLayout::FormatRange> *elidedFormats)': names
    'QList<QTextLayout::FormatRange>', which has no cute class yet.
  - Qt's 'QRectF QQuickTextPrivate::setupTextLayout(qreal *const baseline)':
    takes a type Python has no way to hand over yet.
  - Qt's 'void QQuickTextPrivate::setupCustomLineGeometry(QTextLine &line,
    qreal &height, int fullLayoutTextLength, int lineOffset)': takes a type
    Python has no way to hand over yet.
  - Qt's 'QList<LinkDesc> QQuickTextPrivate::getLinks() const': gives a type
    Python has no way to take yet.

  What has no ritual
  ------------------

  1 of the 48 functions Qt declares: 1 cannot be called and cannot be called
  through the meta-object and cannot be copied.

  What to expect
  --------------

  - The C++ QQuickTextPrivate is created at the first use, not by
    'QQuickTextPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickTextPrivate.
  - Each name of Qt's QQuickTextPrivate that has no cute function yet,
    'elideFormats', 'getLinks', 'links', 'positionInlineImages',
    'setLineGeometry', 'setupCustomLineGeometry', 'setupTextLayout', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QQuickTextPrivate, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class UpdateType(CuteNum):
    """
    The enum 'QQuickTextPrivate::UpdateType' of Qt, with the 3 names Qt gives
    in it.
    """

    UpdateNone = Kee[int](0)
    UpdatePreprocess = Kee[int](1)
    UpdatePaintNode = Kee[int](2)

  #  The classes Qt writes inside QQuickTextPrivate, each a class in here as
  #  in C++.

  class ExtraData(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QQuickTextPrivate::ExtraData: a plain Python object
    standing in front of one C++ QQuickTextPrivate::ExtraData.

    C++ hands a QQuickTextPrivate::ExtraData around as a copy, so every C++
    QQuickTextPrivate::ExtraData behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    No function of Qt's QQuickTextPrivate::ExtraData yet. It can be made from
    Python, in 1 way; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QQuickTextPrivate::ExtraData::~ExtraData()': the destructor:
      Python removes its C++ QQuickTextPrivate::ExtraData by it, and has no
      other use for it.

    What to expect
    --------------

    - The C++ QQuickTextPrivate::ExtraData is created at the first use, not
      by 'QQuickTextPrivate::ExtraData(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QQuickTextPrivate::ExtraData back gives a copy the
      ritual made for Python, in a new cute QQuickTextPrivate::ExtraData.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QQuickTextPrivate::ExtraData'

    #  Qt's '~QQuickTextPrivate::ExtraData()'. Naming it makes this a value
    #  class: Python owns every C++ QQuickTextPrivate::ExtraData behind a
    #  cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN17QQuickTextPrivate9ExtraDataD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload()
    def __init__(self) -> None:
      """
      Notes what was given, for Qt's
      'QQuickTextPrivate::ExtraData::ExtraData()', which is called at the
      first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qquicktextprivate-extradata.html#ExtraData
      """
      #  QQuickTextPrivate::ExtraData::ExtraData()
      self._noteCreation(QQuickTextPrivate.ExtraData, lambda: Rituals.call(
          'ritual_ZN17QQuickTextPrivate9ExtraDataC1Ev',
      ))

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  class LinkDesc(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QQuickTextPrivate::LinkDesc: a plain Python object
    standing in front of one C++ QQuickTextPrivate::LinkDesc.

    C++ hands a QQuickTextPrivate::LinkDesc around as a copy, so every C++
    QQuickTextPrivate::LinkDesc behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    No function of Qt's QQuickTextPrivate::LinkDesc yet. None can be made
    from Python: one comes out of a function of another class that gives one
    back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QQuickTextPrivate::LinkDesc::~LinkDesc()': the destructor: Python
      removes its C++ QQuickTextPrivate::LinkDesc by it, and has no other use
      for it.

    What to expect
    --------------

    - The C++ QQuickTextPrivate::LinkDesc is created at the first use, not by
      'QQuickTextPrivate::LinkDesc(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QQuickTextPrivate::LinkDesc back gives a copy the
      ritual made for Python, in a new cute QQuickTextPrivate::LinkDesc.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QQuickTextPrivate::LinkDesc'

    #  Qt's '~QQuickTextPrivate::LinkDesc()'. Naming it makes this a value
    #  class: Python owns every C++ QQuickTextPrivate::LinkDesc behind a cute
    #  one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN17QQuickTextPrivate8LinkDescD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QTextLayout, QPointF)
  @overload(NoneType, QPointF)
  def anchorAt(layout: Optional[QTextLayout], mousePos: QPointF) -> str:
    """
    Calls Qt's 'QString QQuickTextPrivate::anchorAt(const QTextLayout
    *layout, const QPointF &mousePos)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextprivate.html#anchorAt

    Parameters
    ----------

    layout : Optional[QTextLayout]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    mousePos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickTextPrivate::anchorAt(const QTextLayout *layout, const
    #      QPointF &mousePos)
    return Rituals.call(
        'ritual_ZN17QQuickTextPrivate8anchorAtEPK11QTextLayoutRK7QPointF',
        CuteMixin._addressOf(layout), CuteMixin._valueOf(mousePos,
        'QPointF'),
    )

  @overload(QPointF)
  def anchorAt(self, pos: QPointF) -> str:
    """
    Calls Qt's 'QString QQuickTextPrivate::anchorAt(const QPointF &pos)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextprivate.html#anchorAt

    Parameters
    ----------

    pos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickTextPrivate::anchorAt(const QPointF &pos) const
    return self.uglySide.call(
        'ritual_ZNK17QQuickTextPrivate8anchorAtERK7QPointF',
        self._valueOf(pos, 'QPointF'),
    )

  @staticmethod
  @overload(QQuickText)
  @overload(NoneType)
  def get(t: Optional[QQuickText]) -> Optional[QQuickTextPrivate]:
    """
    Calls Qt's 'QQuickTextPrivate *QQuickTextPrivate::get(QQuickText *t)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextprivate.html#get

    Parameters
    ----------

    t : Optional[QQuickText]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQuickTextPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickTextPrivate *QQuickTextPrivate::get(QQuickText *t)
    address = Rituals.call(
        'ritual_ZN17QQuickTextPrivate3getEP10QQuickText',
        CuteMixin._addressOf(t),
    )
    return QQuickTextPrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickTextPrivate'

  #  A C++ QQuickTextPrivate Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickTextPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def lineHeightOffset(self) -> int:
    """
    Calls Qt's 'int QQuickTextPrivate::lineHeightOffset() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextprivate.html#lineHeightOffset
    """
    #  int QQuickTextPrivate::lineHeightOffset() const
    return self.uglySide.call(
        'ritual_ZNK17QQuickTextPrivate16lineHeightOffsetEv',
    )

  @overload(float, QTextLine)
  def elidedText(self, lineWidth: float, line: QTextLine) -> str:
    """
    Calls Qt's 'QString QQuickTextPrivate::elidedText(qreal lineWidth, const
    QTextLine &line) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextprivate.html#elidedText

    Parameters
    ----------

    lineWidth : float
      Passed on as it is.

    line : QTextLine
      Passed on as a value: Qt reads the C++ QTextLine, which stays Python's
      own.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickTextPrivate::elidedText(qreal lineWidth, const QTextLine
    #      &line) const
    return self.uglySide.call(
        'ritual_ZNK17QQuickTextPrivate10elidedTextEdRK9QTextLine',
        lineWidth, self._valueOf(line),
    )

  def getImplicitWidth(self) -> float:
    """
    Calls Qt's 'qreal QQuickTextPrivate::getImplicitWidth() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextprivate.html#getImplicitWidth
    """
    #  qreal QQuickTextPrivate::getImplicitWidth() const
    ritual = 'ritual_ZNK17QQuickTextPrivate16getImplicitWidthEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QQuickTextPrivate16getImplicitWidthEv'
    return self.uglySide.call(ritual)

  def getImplicitHeight(self) -> float:
    """
    Calls Qt's 'qreal QQuickTextPrivate::getImplicitHeight() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextprivate.html#getImplicitHeight
    """
    #  qreal QQuickTextPrivate::getImplicitHeight() const
    ritual = 'ritual_ZNK17QQuickTextPrivate17getImplicitHeightEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QQuickTextPrivate17getImplicitHeightEv'
    return self.uglySide.call(ritual)

  def availableWidth(self) -> float:
    """
    Calls Qt's 'qreal QQuickTextPrivate::availableWidth() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextprivate.html#availableWidth
    """
    #  qreal QQuickTextPrivate::availableWidth() const
    return self.uglySide.call(
        'ritual_ZNK17QQuickTextPrivate14availableWidthEv',
    )

  def availableHeight(self) -> float:
    """
    Calls Qt's 'qreal QQuickTextPrivate::availableHeight() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextprivate.html#availableHeight
    """
    #  qreal QQuickTextPrivate::availableHeight() const
    return self.uglySide.call(
        'ritual_ZNK17QQuickTextPrivate15availableHeightEv',
    )

  def padding(self) -> float:
    """
    Calls Qt's 'qreal QQuickTextPrivate::padding() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextprivate.html#padding
    """
    #  qreal QQuickTextPrivate::padding() const
    return self.uglySide.call('ritual_ZNK17QQuickTextPrivate7paddingEv')

  def lineHeight(self) -> float:
    """
    Calls Qt's 'qreal QQuickTextPrivate::lineHeight() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextprivate.html#lineHeight
    """
    #  qreal QQuickTextPrivate::lineHeight() const
    return self.uglySide.call('ritual_ZNK17QQuickTextPrivate10lineHeightEv')

  def maximumLineCount(self) -> int:
    """
    Calls Qt's 'int QQuickTextPrivate::maximumLineCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextprivate.html#maximumLineCount
    """
    #  int QQuickTextPrivate::maximumLineCount() const
    return self.uglySide.call(
        'ritual_ZNK17QQuickTextPrivate16maximumLineCountEv',
    )

  def renderTypeQuality(self) -> int:
    """
    Calls Qt's 'int QQuickTextPrivate::renderTypeQuality() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextprivate.html#renderTypeQuality
    """
    #  int QQuickTextPrivate::renderTypeQuality() const
    return self.uglySide.call(
        'ritual_ZNK17QQuickTextPrivate17renderTypeQualityEv',
    )

  def lineHeightMode(self) -> QQuickText.LineHeightMode:
    """
    Calls Qt's 'QQuickText::LineHeightMode
    QQuickTextPrivate::lineHeightMode() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextprivate.html#lineHeightMode

    Returns
    -------

    QQuickText.LineHeightMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QQuickText.LineHeightMode(number)' gives.
    """
    #  QQuickText::LineHeightMode QQuickTextPrivate::lineHeightMode() const
    return QQuickText.LineHeightMode(self.uglySide.call(
        'ritual_ZNK17QQuickTextPrivate14lineHeightModeEv',
    ))

  def fontSizeMode(self) -> QQuickText.FontSizeMode:
    """
    Calls Qt's 'QQuickText::FontSizeMode QQuickTextPrivate::fontSizeMode()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextprivate.html#fontSizeMode

    Returns
    -------

    QQuickText.FontSizeMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QQuickText.FontSizeMode(number)' gives.
    """
    #  QQuickText::FontSizeMode QQuickTextPrivate::fontSizeMode() const
    return QQuickText.FontSizeMode(self.uglySide.call(
        'ritual_ZNK17QQuickTextPrivate12fontSizeModeEv',
    ))

  def minimumPixelSize(self) -> int:
    """
    Calls Qt's 'int QQuickTextPrivate::minimumPixelSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextprivate.html#minimumPixelSize
    """
    #  int QQuickTextPrivate::minimumPixelSize() const
    return self.uglySide.call(
        'ritual_ZNK17QQuickTextPrivate16minimumPixelSizeEv',
    )

  def minimumPointSize(self) -> int:
    """
    Calls Qt's 'int QQuickTextPrivate::minimumPointSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextprivate.html#minimumPointSize
    """
    #  int QQuickTextPrivate::minimumPointSize() const
    return self.uglySide.call(
        'ritual_ZNK17QQuickTextPrivate16minimumPointSizeEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QQuickText.HAlignment)
  @overload(QQuickText.HAlignment, bool)
  def setHAlign(
      self,
      a0: QQuickText.HAlignment,
      forceAlign: bool = False,
  ) -> bool:
    """
    Calls Qt's 'bool QQuickTextPrivate::setHAlign(QQuickText::HAlignment a0,
    bool forceAlign)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextprivate.html#setHAlign

    Parameters
    ----------

    a0 : QQuickText.HAlignment
      Passed on as its number.

    forceAlign : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  bool QQuickTextPrivate::setHAlign(QQuickText::HAlignment a0, bool
    #      forceAlign)
    return self.uglySide.call(
        'ritual_ZN17QQuickTextPrivate9setHAlignEN10QQuickText10HAlignmentEb',
        a0.value, forceAlign,
    )

  @overload(float)
  @overload(float, bool)
  def setTopPadding(self, value: float, reset: bool = False) -> None:
    """
    Calls Qt's 'void QQuickTextPrivate::setTopPadding(qreal value, bool
    reset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextprivate.html#setTopPadding

    Parameters
    ----------

    value : float
      Passed on as it is.

    reset : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QQuickTextPrivate::setTopPadding(qreal value, bool reset)
    self.uglySide.call(
        'ritual_ZN17QQuickTextPrivate13setTopPaddingEdb', value, reset,
    )

  @overload(float)
  @overload(float, bool)
  def setLeftPadding(self, value: float, reset: bool = False) -> None:
    """
    Calls Qt's 'void QQuickTextPrivate::setLeftPadding(qreal value, bool
    reset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextprivate.html#setLeftPadding

    Parameters
    ----------

    value : float
      Passed on as it is.

    reset : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QQuickTextPrivate::setLeftPadding(qreal value, bool reset)
    self.uglySide.call(
        'ritual_ZN17QQuickTextPrivate14setLeftPaddingEdb', value, reset,
    )

  @overload(float)
  @overload(float, bool)
  def setRightPadding(self, value: float, reset: bool = False) -> None:
    """
    Calls Qt's 'void QQuickTextPrivate::setRightPadding(qreal value, bool
    reset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextprivate.html#setRightPadding

    Parameters
    ----------

    value : float
      Passed on as it is.

    reset : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QQuickTextPrivate::setRightPadding(qreal value, bool reset)
    self.uglySide.call(
        'ritual_ZN17QQuickTextPrivate15setRightPaddingEdb', value, reset,
    )

  @overload(float)
  @overload(float, bool)
  def setBottomPadding(self, value: float, reset: bool = False) -> None:
    """
    Calls Qt's 'void QQuickTextPrivate::setBottomPadding(qreal value, bool
    reset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextprivate.html#setBottomPadding

    Parameters
    ----------

    value : float
      Passed on as it is.

    reset : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QQuickTextPrivate::setBottomPadding(qreal value, bool reset)
    self.uglySide.call(
        'ritual_ZN17QQuickTextPrivate16setBottomPaddingEdb', value, reset,
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
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QQuickTextPrivate::QQuickTextPrivate()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextprivate.html#QQuickTextPrivate
    """
    #  QQuickTextPrivate::QQuickTextPrivate()
    self._noteCreation(QQuickTextPrivate, lambda: Rituals.call(
        'ritual_ZN17QQuickTextPrivateC1Ev',
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

  def q_func(self) -> Optional[QQuickText]:
    """
    Calls Qt's 'QQuickText *QQuickTextPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextprivate.html#q_func

    Returns
    -------

    Optional[QQuickText]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickText *QQuickTextPrivate::q_func()
    address = self.uglySide.call('ritual_ZN17QQuickTextPrivate6q_funcEv')
    return QQuickText._cuteAt(address)

  def init(self) -> None:
    """
    Calls Qt's 'void QQuickTextPrivate::init()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextprivate.html#init
    """
    #  void QQuickTextPrivate::init()
    self.uglySide.call('ritual_ZN17QQuickTextPrivate4initEv')

  @overload(float, float)
  def updateBaseline(self, baseline: float, dy: float) -> None:
    """
    Calls Qt's 'void QQuickTextPrivate::updateBaseline(qreal baseline, qreal
    dy)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextprivate.html#updateBaseline

    Parameters
    ----------

    baseline : float
      Passed on as it is.

    dy : float
      Passed on as it is.
    """
    #  void QQuickTextPrivate::updateBaseline(qreal baseline, qreal dy)
    self.uglySide.call(
        'ritual_ZN17QQuickTextPrivate14updateBaselineEdd', baseline, dy,
    )

  def updateSize(self) -> None:
    """
    Calls Qt's 'void QQuickTextPrivate::updateSize()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextprivate.html#updateSize
    """
    #  void QQuickTextPrivate::updateSize()
    self.uglySide.call('ritual_ZN17QQuickTextPrivate10updateSizeEv')

  @overload(QSizeF)
  def signalSizeChange(self, previousSize: QSizeF) -> None:
    """
    Calls Qt's 'void QQuickTextPrivate::signalSizeChange(const QSizeF
    &previousSize)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextprivate.html#signalSizeChange

    Parameters
    ----------

    previousSize : QSizeF
      Passed on as a value: Qt reads the C++ QSizeF, which stays Python's
      own.
    """
    #  void QQuickTextPrivate::signalSizeChange(const QSizeF &previousSize)
    self.uglySide.call(
        'ritual_ZN17QQuickTextPrivate16signalSizeChangeERK6QSizeF',
        self._valueOf(previousSize),
    )

  def updateLayout(self) -> None:
    """
    Calls Qt's 'void QQuickTextPrivate::updateLayout()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextprivate.html#updateLayout
    """
    #  void QQuickTextPrivate::updateLayout()
    self.uglySide.call('ritual_ZN17QQuickTextPrivate12updateLayoutEv')

  def determineHorizontalAlignment(self) -> bool:
    """
    Calls Qt's 'bool QQuickTextPrivate::determineHorizontalAlignment()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextprivate.html
    """
    #  bool QQuickTextPrivate::determineHorizontalAlignment()
    return self.uglySide.call(
        'ritual_ZN17QQuickTextPrivate28determineHorizontalAlignmentEv',
    )

  def mirrorChange(self) -> None:
    """
    Calls Qt's 'void QQuickTextPrivate::mirrorChange()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextprivate.html#mirrorChange
    """
    #  void QQuickTextPrivate::mirrorChange()
    ritual = 'ritual_ZN17QQuickTextPrivate12mirrorChangeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQuickTextPrivate12mirrorChangeEv'
    self.uglySide.call(ritual)

  def isLineLaidOutConnected(self) -> bool:
    """
    Calls Qt's 'bool QQuickTextPrivate::isLineLaidOutConnected()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextprivate.html#isLineLaidOutConnected
    """
    #  bool QQuickTextPrivate::isLineLaidOutConnected()
    return self.uglySide.call(
        'ritual_ZN17QQuickTextPrivate22isLineLaidOutConnectedEv',
    )

  def clearFormats(self) -> None:
    """
    Calls Qt's 'void QQuickTextPrivate::clearFormats()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextprivate.html#clearFormats
    """
    #  void QQuickTextPrivate::clearFormats()
    self.uglySide.call('ritual_ZN17QQuickTextPrivate12clearFormatsEv')

  @overload(QHoverEvent)
  @overload(NoneType)
  def processHoverEvent(self, event: Optional[QHoverEvent]) -> None:
    """
    Calls Qt's 'void QQuickTextPrivate::processHoverEvent(QHoverEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextprivate.html#processHoverEvent

    Parameters
    ----------

    event : Optional[QHoverEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickTextPrivate::processHoverEvent(QHoverEvent *event)
    self.uglySide.call(
        'ritual_ZN17QQuickTextPrivate17processHoverEventEP11QHoverEvent',
        self._addressOf(event),
    )

  @overload(QQuickItem)
  @overload(NoneType)
  def transformChanged(self, transformedItem: Optional[QQuickItem]) -> bool:
    """
    Calls Qt's 'bool QQuickTextPrivate::transformChanged(QQuickItem
    *transformedItem)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextprivate.html#transformChanged

    Parameters
    ----------

    transformedItem : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickTextPrivate::transformChanged(QQuickItem *transformedItem)
    ritual = 'ritual_ZN17QQuickTextPrivate16transformChangedEP10QQuickItem'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QQuickTextPrivate16transformChangedEP10QQuickItem')
    return self.uglySide.call(ritual, self._addressOf(transformedItem))

  def ensureDoc(self) -> None:
    """
    Calls Qt's 'void QQuickTextPrivate::ensureDoc()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextprivate.html#ensureDoc
    """
    #  void QQuickTextPrivate::ensureDoc()
    self.uglySide.call('ritual_ZN17QQuickTextPrivate9ensureDocEv')

  def updateDocumentText(self) -> None:
    """
    Calls Qt's 'void QQuickTextPrivate::updateDocumentText()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextprivate.html#updateDocumentText
    """
    #  void QQuickTextPrivate::updateDocumentText()
    self.uglySide.call('ritual_ZN17QQuickTextPrivate18updateDocumentTextEv')

  def isLinkActivatedConnected(self) -> bool:
    """
    Calls Qt's 'bool QQuickTextPrivate::isLinkActivatedConnected()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextprivate.html#isLinkActivatedConnected
    """
    #  bool QQuickTextPrivate::isLinkActivatedConnected()
    return self.uglySide.call(
        'ritual_ZN17QQuickTextPrivate24isLinkActivatedConnectedEv',
    )

  def isLinkHoveredConnected(self) -> bool:
    """
    Calls Qt's 'bool QQuickTextPrivate::isLinkHoveredConnected()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextprivate.html#isLinkHoveredConnected
    """
    #  bool QQuickTextPrivate::isLinkHoveredConnected()
    return self.uglySide.call(
        'ritual_ZN17QQuickTextPrivate22isLinkHoveredConnectedEv',
    )

  @staticmethod
  def elideFormats(*__, **_) -> Never:
    """
    Qt's 'void QQuickTextPrivate::elideFormats(int start, int length, int
    offset, QList<QTextLayout::FormatRange> *elidedFormats)': names
    'QList<QTextLayout::FormatRange>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQuickTextPrivate.elideFormats' has no cute function yet. Qt's "
        "'void QQuickTextPrivate::elideFormats(int start, int length, int "
        "offset, QList<QTextLayout::FormatRange> *elidedFormats)': names "
        "'QList<QTextLayout::FormatRange>', which has no cute class yet.")

  @staticmethod
  def getLinks(*__, **_) -> Never:
    """
    Qt's 'QList<LinkDesc> QQuickTextPrivate::getLinks() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQuickTextPrivate.getLinks' has no cute function yet. Qt's "
        "'QList<LinkDesc> QQuickTextPrivate::getLinks() const': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def links(*__, **_) -> Never:
    """
    Qt's 'QStringList QQuickTextPrivate::links() const': cannot be called and
    cannot be called through the meta-object and cannot be copied: no header
    file has its code, Qt's source does not mark it or its class for use from
    outside Qt or writes it 'inline' or nowhere, and it is no signal, slot or
    invokable function giving back nothing, of a class built on QObject, and
    Qt's source has no code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QQuickTextPrivate.links' has no cute function yet. Qt's "
        "'QStringList QQuickTextPrivate::links() const': cannot be called "
        "and cannot be called through the meta-object and cannot be copied: "
        "no header file has its code, Qt's source does not mark it or its "
        "class for use from outside Qt or writes it 'inline' or nowhere, "
        "and it is no signal, slot or invokable function giving back "
        "nothing, of a class built on QObject, and Qt's source has no code "
        "for it that could be told from the rest.")

  @staticmethod
  def positionInlineImages(*__, **_) -> Never:
    """
    Qt's 'void QQuickTextPrivate::positionInlineImages(const QTextLine &line,
    const QList<QTextLayout::FormatRange> &formats)': takes a type Python has
    no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQuickTextPrivate.positionInlineImages' has no cute function yet. "
        "Qt's 'void QQuickTextPrivate::positionInlineImages(const QTextLine "
        "&line, const QList<QTextLayout::FormatRange> &formats)': takes a "
        "type Python has no way to hand over yet.")

  @staticmethod
  def setLineGeometry(*__, **_) -> Never:
    """
    Qt's 'void QQuickTextPrivate::setLineGeometry(QTextLine &line, qreal
    lineWidth, qreal &height)': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'QQuickTextPrivate.setLineGeometry' has no cute function yet. Qt's "
        "'void QQuickTextPrivate::setLineGeometry(QTextLine &line, qreal "
        "lineWidth, qreal &height)': takes a type Python has no way to hand "
        "over yet.")

  @staticmethod
  def setupCustomLineGeometry(*__, **_) -> Never:
    """
    Qt's 'void QQuickTextPrivate::setupCustomLineGeometry(QTextLine &line,
    qreal &height, int fullLayoutTextLength, int lineOffset)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQuickTextPrivate.setupCustomLineGeometry' has no cute function "
        "yet. Qt's 'void "
        "QQuickTextPrivate::setupCustomLineGeometry(QTextLine &line, qreal "
        "&height, int fullLayoutTextLength, int lineOffset)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def setupTextLayout(*__, **_) -> Never:
    """
    Qt's 'QRectF QQuickTextPrivate::setupTextLayout(qreal *const baseline)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQuickTextPrivate.setupTextLayout' has no cute function yet. Qt's "
        "'QRectF QQuickTextPrivate::setupTextLayout(qreal *const "
        "baseline)': takes a type Python has no way to hand over yet.")
