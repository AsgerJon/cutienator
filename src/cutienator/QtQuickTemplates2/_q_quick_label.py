"""
QQuickLabel binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquicklabel_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQuickLabel to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtQuick import QQuickItem, QQuickText

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMarginsF, QMetaObject, QRectF
  from ..QtGui import QFont
  from . import QQuickLabelPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QFont = WAIT['QFont']
  QMarginsF = WAIT['QMarginsF']
  QRectF = WAIT['QRectF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickLabel(QQuickText):
  """
  The cute side of Qt's QQuickLabel: a plain Python object standing in front
  of one C++ QQuickLabel.

  It is built on the cute 'QQuickText', as Qt's QQuickLabel is built on Qt's
  QQuickText, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickLabel that has a ritual and that Python can
  call so far, 34 names in all: 'metaObject', 'tr', 'font', 'setFont',
  'background', 'setBackground', 'implicitBackgroundWidth',
  'implicitBackgroundHeight', 'topInset', 'setTopInset', 'resetTopInset',
  'leftInset', 'setLeftInset', 'resetLeftInset', 'rightInset',
  'setRightInset', 'resetRightInset', 'bottomInset', 'setBottomInset',
  'resetBottomInset', 'fontChanged', 'backgroundChanged',
  'implicitBackgroundWidthChanged', 'implicitBackgroundHeightChanged',
  'topInsetChanged', 'leftInsetChanged', 'rightInsetChanged',
  'bottomInsetChanged', 'classBegin', 'componentComplete', 'itemChange',
  'geometryChange', 'insetChange', 'd_func'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickLabel::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QQuickLabel::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickLabel::~QQuickLabel()': the destructor: Python never removes
    a C++ QQuickLabel.
  - Qt's 'const QQuickLabelPrivate *QQuickLabel::d_func() const': takes in
    Python what 'QQuickLabelPrivate *QQuickLabel::d_func()' takes.

  What has no ritual
  ------------------

  4 of the 43 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickLabel is created at the first use, not by
    'QQuickLabel(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickLabel.
  - Qt tells when it has removed the C++ QQuickLabel. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  @overload(NoneType)
  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  @overload(str, str, int)
  @overload(str, NoneType, int)
  @overload(NoneType, str, int)
  @overload(NoneType, NoneType, int)
  def tr(s: Optional[str], c: Optional[str] = None, n: int = -1) -> str:
    """
    Calls Qt's 'QString QQuickLabel::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicklabel.html#tr

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    c : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickLabel::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN11QQuickLabel2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickLabel'

  #  A C++ QQuickLabel Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickLabel'

  #  The functions Qt calls itself that QQuickLabel is the first to declare.
  #  A class of a program built on it can write one anew, and Qt then calls
  #  that. For each name: the key C++ knows the function by, what it gives,
  #  and what it takes.
  __virtual_functions__ = {
      'insetChange': (
          ('_ZN11QQuickLabel11insetChangeERK9QMarginsFS2_',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QMarginsF'),
               ('address', 'value', 'QtCore:QMarginsF'),
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

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickLabel::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicklabel.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickLabel::metaObject() const
    address = self.uglySide.call('ritual_ZNK11QQuickLabel10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def font(self) -> QFont:
    """
    Calls Qt's 'QFont QQuickLabel::font() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicklabel.html#font

    Returns
    -------

    QFont
      A new cute QFont around the copy Qt gave back. Python owns it.
    """
    #  QFont QQuickLabel::font() const
    address = self.uglySide.call('ritual_ZNK11QQuickLabel4fontEv')
    from ..QtGui import QFont
    return QFont._cuteOwning(address)

  def background(self) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickLabel::background() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicklabel.html#background

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickLabel::background() const
    address = self.uglySide.call('ritual_ZNK11QQuickLabel10backgroundEv')
    return QQuickItem._cuteAt(address)

  def implicitBackgroundWidth(self) -> float:
    """
    Calls Qt's 'qreal QQuickLabel::implicitBackgroundWidth() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabel.html#implicitBackgroundWidth
    """
    #  qreal QQuickLabel::implicitBackgroundWidth() const
    return self.uglySide.call(
        'ritual_ZNK11QQuickLabel23implicitBackgroundWidthEv',
    )

  def implicitBackgroundHeight(self) -> float:
    """
    Calls Qt's 'qreal QQuickLabel::implicitBackgroundHeight() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabel.html#implicitBackgroundHeight
    """
    #  qreal QQuickLabel::implicitBackgroundHeight() const
    return self.uglySide.call(
        'ritual_ZNK11QQuickLabel24implicitBackgroundHeightEv',
    )

  def topInset(self) -> float:
    """
    Calls Qt's 'qreal QQuickLabel::topInset() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicklabel.html#topInset
    """
    #  qreal QQuickLabel::topInset() const
    return self.uglySide.call('ritual_ZNK11QQuickLabel8topInsetEv')

  def leftInset(self) -> float:
    """
    Calls Qt's 'qreal QQuickLabel::leftInset() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicklabel.html#leftInset
    """
    #  qreal QQuickLabel::leftInset() const
    return self.uglySide.call('ritual_ZNK11QQuickLabel9leftInsetEv')

  def rightInset(self) -> float:
    """
    Calls Qt's 'qreal QQuickLabel::rightInset() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicklabel.html#rightInset
    """
    #  qreal QQuickLabel::rightInset() const
    return self.uglySide.call('ritual_ZNK11QQuickLabel10rightInsetEv')

  def bottomInset(self) -> float:
    """
    Calls Qt's 'qreal QQuickLabel::bottomInset() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicklabel.html#bottomInset
    """
    #  qreal QQuickLabel::bottomInset() const
    return self.uglySide.call('ritual_ZNK11QQuickLabel11bottomInsetEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QFont)
  def setFont(self, font: QFont) -> None:
    """
    Calls Qt's 'void QQuickLabel::setFont(const QFont &font)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicklabel.html#setFont

    Parameters
    ----------

    font : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.
    """
    #  void QQuickLabel::setFont(const QFont &font)
    self.uglySide.call(
        'ritual_ZN11QQuickLabel7setFontERK5QFont', self._valueOf(font),
    )

  @overload(QQuickItem)
  @overload(NoneType)
  def setBackground(self, background: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickLabel::setBackground(QQuickItem *background)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicklabel.html#setBackground

    Parameters
    ----------

    background : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickLabel::setBackground(QQuickItem *background)
    self.uglySide.call(
        'ritual_ZN11QQuickLabel13setBackgroundEP10QQuickItem',
        self._addressOf(background),
    )

  @overload(float)
  def setTopInset(self, inset: float) -> None:
    """
    Calls Qt's 'void QQuickLabel::setTopInset(qreal inset)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicklabel.html#setTopInset

    Parameters
    ----------

    inset : float
      Passed on as it is.
    """
    #  void QQuickLabel::setTopInset(qreal inset)
    self.uglySide.call('ritual_ZN11QQuickLabel11setTopInsetEd', inset)

  @overload(float)
  def setLeftInset(self, inset: float) -> None:
    """
    Calls Qt's 'void QQuickLabel::setLeftInset(qreal inset)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicklabel.html#setLeftInset

    Parameters
    ----------

    inset : float
      Passed on as it is.
    """
    #  void QQuickLabel::setLeftInset(qreal inset)
    self.uglySide.call('ritual_ZN11QQuickLabel12setLeftInsetEd', inset)

  @overload(float)
  def setRightInset(self, inset: float) -> None:
    """
    Calls Qt's 'void QQuickLabel::setRightInset(qreal inset)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicklabel.html#setRightInset

    Parameters
    ----------

    inset : float
      Passed on as it is.
    """
    #  void QQuickLabel::setRightInset(qreal inset)
    self.uglySide.call('ritual_ZN11QQuickLabel13setRightInsetEd', inset)

  @overload(float)
  def setBottomInset(self, inset: float) -> None:
    """
    Calls Qt's 'void QQuickLabel::setBottomInset(qreal inset)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicklabel.html#setBottomInset

    Parameters
    ----------

    inset : float
      Passed on as it is.
    """
    #  void QQuickLabel::setBottomInset(qreal inset)
    self.uglySide.call('ritual_ZN11QQuickLabel14setBottomInsetEd', inset)

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
  @overload(QQuickItem)
  @overload(NoneType)
  def __init__(self, parent: Optional[QQuickItem] = None) -> None:
    """
    Notes what was given, for Qt's 'QQuickLabel::QQuickLabel(QQuickItem
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qquicklabel.html#QQuickLabel

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickLabel::QQuickLabel(QQuickItem *parent)
    self._noteCreation(QQuickLabel, lambda: Rituals.call(
        'ritual_ZN11QQuickLabelC1EP10QQuickItem', self._addressOf(parent),
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

  def resetTopInset(self) -> None:
    """
    Calls Qt's 'void QQuickLabel::resetTopInset()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicklabel.html#resetTopInset
    """
    #  void QQuickLabel::resetTopInset()
    self.uglySide.call('ritual_ZN11QQuickLabel13resetTopInsetEv')

  def resetLeftInset(self) -> None:
    """
    Calls Qt's 'void QQuickLabel::resetLeftInset()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicklabel.html#resetLeftInset
    """
    #  void QQuickLabel::resetLeftInset()
    self.uglySide.call('ritual_ZN11QQuickLabel14resetLeftInsetEv')

  def resetRightInset(self) -> None:
    """
    Calls Qt's 'void QQuickLabel::resetRightInset()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicklabel.html#resetRightInset
    """
    #  void QQuickLabel::resetRightInset()
    self.uglySide.call('ritual_ZN11QQuickLabel15resetRightInsetEv')

  def resetBottomInset(self) -> None:
    """
    Calls Qt's 'void QQuickLabel::resetBottomInset()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicklabel.html#resetBottomInset
    """
    #  void QQuickLabel::resetBottomInset()
    self.uglySide.call('ritual_ZN11QQuickLabel16resetBottomInsetEv')

  def fontChanged(self) -> None:
    """
    Calls Qt's 'void QQuickLabel::fontChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicklabel.html#fontChanged
    """
    #  void QQuickLabel::fontChanged()
    self.uglySide.call('ritual_ZN11QQuickLabel11fontChangedEv')

  def backgroundChanged(self) -> None:
    """
    Calls Qt's 'void QQuickLabel::backgroundChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicklabel.html#backgroundChanged
    """
    #  void QQuickLabel::backgroundChanged()
    self.uglySide.call('ritual_ZN11QQuickLabel17backgroundChangedEv')

  def implicitBackgroundWidthChanged(self) -> None:
    """
    Calls Qt's 'void QQuickLabel::implicitBackgroundWidthChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabel.html#implicitBackgroundWidthChanged
    """
    #  void QQuickLabel::implicitBackgroundWidthChanged()
    self.uglySide.call(
        'ritual_ZN11QQuickLabel30implicitBackgroundWidthChangedEv',
    )

  def implicitBackgroundHeightChanged(self) -> None:
    """
    Calls Qt's 'void QQuickLabel::implicitBackgroundHeightChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabel.html#implicitBackgroundHeightChanged
    """
    #  void QQuickLabel::implicitBackgroundHeightChanged()
    self.uglySide.call(
        'ritual_ZN11QQuickLabel31implicitBackgroundHeightChangedEv',
    )

  def topInsetChanged(self) -> None:
    """
    Calls Qt's 'void QQuickLabel::topInsetChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicklabel.html#topInsetChanged
    """
    #  void QQuickLabel::topInsetChanged()
    self.uglySide.call('ritual_ZN11QQuickLabel15topInsetChangedEv')

  def leftInsetChanged(self) -> None:
    """
    Calls Qt's 'void QQuickLabel::leftInsetChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicklabel.html#leftInsetChanged
    """
    #  void QQuickLabel::leftInsetChanged()
    self.uglySide.call('ritual_ZN11QQuickLabel16leftInsetChangedEv')

  def rightInsetChanged(self) -> None:
    """
    Calls Qt's 'void QQuickLabel::rightInsetChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicklabel.html#rightInsetChanged
    """
    #  void QQuickLabel::rightInsetChanged()
    self.uglySide.call('ritual_ZN11QQuickLabel17rightInsetChangedEv')

  def bottomInsetChanged(self) -> None:
    """
    Calls Qt's 'void QQuickLabel::bottomInsetChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabel.html#bottomInsetChanged
    """
    #  void QQuickLabel::bottomInsetChanged()
    self.uglySide.call('ritual_ZN11QQuickLabel18bottomInsetChangedEv')

  def classBegin(self) -> None:
    """
    Calls Qt's 'void QQuickLabel::classBegin()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicklabel.html#classBegin
    """
    #  void QQuickLabel::classBegin()
    ritual = 'ritual_ZN11QQuickLabel10classBeginEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QQuickLabel10classBeginEv'
    self.uglySide.call(ritual)

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQuickLabel::componentComplete()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicklabel.html#componentComplete
    """
    #  void QQuickLabel::componentComplete()
    ritual = 'ritual_ZN11QQuickLabel17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QQuickLabel17componentCompleteEv'
    self.uglySide.call(ritual)

  @overload(QQuickItem.ItemChange, QQuickItem.ItemChangeData)
  def itemChange(
      self,
      change: QQuickItem.ItemChange,
      value: QQuickItem.ItemChangeData,
  ) -> None:
    """
    Calls Qt's 'void QQuickLabel::itemChange(ItemChange change, const
    ItemChangeData &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicklabel.html#itemChange

    Parameters
    ----------

    change : QQuickItem.ItemChange
      Passed on as its number.

    value : QQuickItem.ItemChangeData
      Passed on as a value: Qt reads the C++ QQuickItem::ItemChangeData,
      which stays Python's own.
    """
    #  void QQuickLabel::itemChange(ItemChange change, const ItemChangeData
    #      &value)
    ritual = (
        'ritual_ZN11QQuickLabel10itemChangeEN10QQuickItem10ItemChangeERKNS0'
        '_14ItemChangeDataE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN11QQuickLabel10itemChangeEN10QQuickItem10ItemChange'
          'ERKNS0_14ItemChangeDataE')
    self.uglySide.call(ritual, change.value, self._valueOf(value))

  @overload(QRectF, QRectF)
  def geometryChange(self, newGeometry: QRectF, oldGeometry: QRectF) -> None:
    """
    Calls Qt's 'void QQuickLabel::geometryChange(const QRectF &newGeometry,
    const QRectF &oldGeometry)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicklabel.html#geometryChange

    Parameters
    ----------

    newGeometry : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    oldGeometry : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QQuickLabel::geometryChange(const QRectF &newGeometry, const
    #      QRectF &oldGeometry)
    ritual = 'ritual_ZN11QQuickLabel14geometryChangeERK6QRectFS2_'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QQuickLabel14geometryChangeERK6QRectFS2_'
    self.uglySide.call(
        ritual, self._valueOf(newGeometry), self._valueOf(oldGeometry),
    )

  @overload(QMarginsF, QMarginsF)
  def insetChange(self, newInset: QMarginsF, oldInset: QMarginsF) -> None:
    """
    Calls Qt's 'void QQuickLabel::insetChange(const QMarginsF &newInset,
    const QMarginsF &oldInset)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicklabel.html#insetChange

    Parameters
    ----------

    newInset : QMarginsF
      Passed on as a value: Qt reads the C++ QMarginsF, which stays Python's
      own.

    oldInset : QMarginsF
      Passed on as a value: Qt reads the C++ QMarginsF, which stays Python's
      own.
    """
    #  void QQuickLabel::insetChange(const QMarginsF &newInset, const
    #      QMarginsF &oldInset)
    ritual = 'ritual_ZN11QQuickLabel11insetChangeERK9QMarginsFS2_'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QQuickLabel11insetChangeERK9QMarginsFS2_'
    self.uglySide.call(
        ritual, self._valueOf(newInset), self._valueOf(oldInset),
    )

  def d_func(self) -> Optional[QQuickLabelPrivate]:
    """
    Calls Qt's 'QQuickLabelPrivate *QQuickLabel::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicklabel.html#d_func

    Returns
    -------

    Optional[QQuickLabelPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickLabelPrivate *QQuickLabel::d_func()
    address = self.uglySide.call('ritual_ZN11QQuickLabel6d_funcEv')
    from . import QQuickLabelPrivate
    return QQuickLabelPrivate._cuteAt(address)
