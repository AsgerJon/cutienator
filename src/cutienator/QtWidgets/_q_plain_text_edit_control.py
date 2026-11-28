"""
QPlainTextEditControl binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qplaintextedit_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QPlainTextEditControl to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtCore import Qt
from . import QWidgetTextControl

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QMimeData, QPointF, QRectF, QUrl
  from ..QtCore import QVariant
  from ..QtGui import QTextBlock, QTextCursor
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMimeData = WAIT['QMimeData']
  QPointF = WAIT['QPointF']
  QTextBlock = WAIT['QTextBlock']
  QTextCursor = WAIT['QTextCursor']
  QUrl = WAIT['QUrl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPlainTextEditControl(QWidgetTextControl):
  """
  The cute side of Qt's QPlainTextEditControl: a plain Python object standing
  in front of one C++ QPlainTextEditControl.

  It is built on the cute 'QWidgetTextControl', as Qt's QPlainTextEditControl
  is built on Qt's QWidgetTextControl, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QPlainTextEditControl that has a ritual and that
  Python can call so far, 11 names in all: 'metaObject',
  'createMimeDataFromSelection', 'canInsertFromMimeData',
  'insertFromMimeData', 'hitTest', 'blockBoundingRect', 'anchorAt',
  'cursorRect', 'ensureCursorVisible', 'firstVisibleBlock', 'loadResource'.
  None can be made from Python: one comes out of a function of another class
  that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QPlainTextEditControl::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QPlainTextEditControl::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  4 of the 18 functions Qt declares: 2 not a gap; 2 leans on
  'QPlainTextEditControl.

  What to expect
  --------------

  - The C++ QPlainTextEditControl is created at the first use, not by
    'QPlainTextEditControl(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QPlainTextEditControl.
  - Qt tells when it has removed the C++ QPlainTextEditControl. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QPlainTextEditControl that has no cute function yet,
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
  __qt_class__ = 'QPlainTextEditControl'

  #  A C++ QPlainTextEditControl Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QPlainTextEditControl'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QPlainTextEditControl::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplaintexteditcontrol.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QPlainTextEditControl::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK21QPlainTextEditControl10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def createMimeDataFromSelection(self) -> Optional[QMimeData]:
    """
    Calls Qt's 'QMimeData
    *QPlainTextEditControl::createMimeDataFromSelection() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplaintexteditcontrol.html

    Returns
    -------

    Optional[QMimeData]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QMimeData *QPlainTextEditControl::createMimeDataFromSelection() const
    ritual = (
        'ritual_ZNK21QPlainTextEditControl27createMimeDataFromSelectionEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK21QPlainTextEditControl27createMimeDataFromSelecti'
          'onEv')
    address = self.uglySide.call(ritual)
    from ..QtCore import QMimeData
    return QMimeData._cuteAt(address)

  @overload(QMimeData)
  @overload(NoneType)
  def canInsertFromMimeData(self, source: Optional[QMimeData]) -> bool:
    """
    Calls Qt's 'bool QPlainTextEditControl::canInsertFromMimeData(const
    QMimeData *source) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplaintexteditcontrol.html#canInsertFromMimeData

    Parameters
    ----------

    source : Optional[QMimeData]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QPlainTextEditControl::canInsertFromMimeData(const QMimeData
    #      *source) const
    ritual = (
        'ritual_ZNK21QPlainTextEditControl21canInsertFromMimeDataEPK9QMimeD'
        'ata')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK21QPlainTextEditControl21canInsertFromMimeDataEPK9'
          'QMimeData')
    return self.uglySide.call(ritual, self._addressOf(source))

  @overload(QPointF)
  @overload(QPointF, Qt.HitTestAccuracy)
  def hitTest(
      self,
      point: QPointF,
      a1: Qt.HitTestAccuracy = Qt.HitTestAccuracy.FuzzyHit,
  ) -> int:
    """
    Calls Qt's 'int QPlainTextEditControl::hitTest(const QPointF &point,
    Qt::HitTestAccuracy a1) const'.

    Qt's own words: https://doc.qt.io/qt-6/qplaintexteditcontrol.html#hitTest

    Parameters
    ----------

    point : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    a1 : Qt.HitTestAccuracy
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.HitTestAccuracy.FuzzyHit.
    """
    #  int QPlainTextEditControl::hitTest(const QPointF &point,
    #      Qt::HitTestAccuracy a1) const
    ritual = (
        'ritual_ZNK21QPlainTextEditControl7hitTestERK7QPointFN2Qt15HitTestA'
        'ccuracyE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK21QPlainTextEditControl7hitTestERK7QPointFN2Qt15Hi'
          'tTestAccuracyE')
    return self.uglySide.call(
        ritual, self._valueOf(point, 'QPointF'), a1.value,
    )

  @overload(QTextBlock)
  def blockBoundingRect(self, block: QTextBlock) -> QRectF:
    """
    Calls Qt's 'QRectF QPlainTextEditControl::blockBoundingRect(const
    QTextBlock &block) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplaintexteditcontrol.html#blockBoundingRect

    Parameters
    ----------

    block : QTextBlock
      Passed on as a value: Qt reads the C++ QTextBlock, which stays Python's
      own.

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QPlainTextEditControl::blockBoundingRect(const QTextBlock
    #      &block) const
    ritual = (
        'ritual_ZNK21QPlainTextEditControl17blockBoundingRectERK10QTextBloc'
        'k')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK21QPlainTextEditControl17blockBoundingRectERK10QTe'
          'xtBlock')
    address = self.uglySide.call(ritual, self._valueOf(block))
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  @overload(QPointF)
  def anchorAt(self, pos: QPointF) -> str:
    """
    Calls Qt's 'QString QPlainTextEditControl::anchorAt(const QPointF &pos)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplaintexteditcontrol.html#anchorAt

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
    #  QString QPlainTextEditControl::anchorAt(const QPointF &pos) const
    ritual = 'ritual_ZNK21QPlainTextEditControl8anchorAtERK7QPointF'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK21QPlainTextEditControl8anchorAtERK7QPointF'
    return self.uglySide.call(ritual, self._valueOf(pos, 'QPointF'))

  @overload(QTextCursor)
  def cursorRect(self, cursor: QTextCursor) -> QRectF:
    """
    Calls Qt's 'QRectF QPlainTextEditControl::cursorRect(const QTextCursor
    &cursor) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplaintexteditcontrol.html#cursorRect

    Parameters
    ----------

    cursor : QTextCursor
      Passed on as a value: Qt reads the C++ QTextCursor, which stays
      Python's own.

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QPlainTextEditControl::cursorRect(const QTextCursor &cursor)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK21QPlainTextEditControl10cursorRectERK11QTextCursor',
        self._valueOf(cursor),
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  @overload()
  def cursorRect(self) -> QRectF:
    """
    Calls Qt's 'QRectF QPlainTextEditControl::cursorRect()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplaintexteditcontrol.html#cursorRect

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QPlainTextEditControl::cursorRect()
    address = self.uglySide.call(
        'ritual_ZN21QPlainTextEditControl10cursorRectEv',
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def firstVisibleBlock(self) -> QTextBlock:
    """
    Calls Qt's 'QTextBlock QPlainTextEditControl::firstVisibleBlock() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplaintexteditcontrol.html#firstVisibleBlock

    Returns
    -------

    QTextBlock
      A new cute QTextBlock around the copy Qt gave back. Python owns it.
    """
    #  QTextBlock QPlainTextEditControl::firstVisibleBlock() const
    address = self.uglySide.call(
        'ritual_ZNK21QPlainTextEditControl17firstVisibleBlockEv',
    )
    from ..QtGui import QTextBlock
    return QTextBlock._cuteOwning(address)

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
    Qt's 'QPlainTextEditControl::QPlainTextEditControl(QPlainTextEdit
    *parent)': leans on
    'QPlainTextEditControl::qt_metacall(QMetaObject::Call, int, void**)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QPlainTextEditControl.__init__' has no cute function yet. Qt's "
        "'QPlainTextEditControl::QPlainTextEditControl(QPlainTextEdit "
        "*parent)': leans on "
        "'QPlainTextEditControl::qt_metacall(QMetaObject::Call, int, "
        "void**)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

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

  @overload(QMimeData)
  @overload(NoneType)
  def insertFromMimeData(self, source: Optional[QMimeData]) -> None:
    """
    Calls Qt's 'void QPlainTextEditControl::insertFromMimeData(const
    QMimeData *source)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplaintexteditcontrol.html#insertFromMimeData

    Parameters
    ----------

    source : Optional[QMimeData]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPlainTextEditControl::insertFromMimeData(const QMimeData
    #      *source)
    ritual = (
        'ritual_ZN21QPlainTextEditControl18insertFromMimeDataEPK9QMimeData')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN21QPlainTextEditControl18insertFromMimeDataEPK9QMim'
          'eData')
    self.uglySide.call(ritual, self._addressOf(source))

  def ensureCursorVisible(self) -> None:
    """
    Calls Qt's 'void QPlainTextEditControl::ensureCursorVisible()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplaintexteditcontrol.html#ensureCursorVisible
    """
    #  void QPlainTextEditControl::ensureCursorVisible()
    ritual = 'ritual_ZN21QPlainTextEditControl19ensureCursorVisibleEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QPlainTextEditControl19ensureCursorVisibleEv'
    self.uglySide.call(ritual)

  @overload(int, QUrl)
  def loadResource(self, type: int, name: QUrl) -> QVariant:
    """
    Calls Qt's 'QVariant QPlainTextEditControl::loadResource(int type, const
    QUrl &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplaintexteditcontrol.html#loadResource

    Parameters
    ----------

    type : int
      Passed on as it is.

    name : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QPlainTextEditControl::loadResource(int type, const QUrl
    #      &name)
    ritual = 'ritual_ZN21QPlainTextEditControl12loadResourceEiRK4QUrl'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QPlainTextEditControl12loadResourceEiRK4QUrl'
    address = self.uglySide.call(ritual, type, self._valueOf(name))
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)
