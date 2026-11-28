"""
QSvgFillStyle binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSvg/6.12.0/QtSvg/private/qsvgstyle_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QSvgFillStyle to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import Qt
from . import QSvgStyleProperty

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtGui import QBrush
  from . import QSvgPaintServer
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QBrush = WAIT['QBrush']


class QSvgFillStyle(QSvgStyleProperty):
  """
  The cute side of Qt's QSvgFillStyle: a plain Python object standing in
  front of one C++ QSvgFillStyle.

  It is built on the cute 'QSvgStyleProperty', as Qt's QSvgFillStyle is built
  on Qt's QSvgStyleProperty, and has everything that class has.

  C++ hands a QSvgFillStyle around as a copy, so every C++ QSvgFillStyle
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QSvgFillStyle that has a ritual and that Python can
  call so far, 10 names in all: 'type', 'setFillRule', 'setFillOpacity',
  'setBrush', 'qbrush', 'fillOpacity', 'fillRule', 'paintServer',
  'setPaintStyleId', 'paintStyleId'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSvgFillStyle::~QSvgFillStyle()': the destructor: Python removes
    its C++ QSvgFillStyle by it, and has no other use for it.
  - Qt's 'void QSvgFillStyle::apply(QPainter *p, const QSvgNode *node,
    QSvgExtraStates &states)': takes a type Python has no way to hand over
    yet.
  - Qt's 'void QSvgFillStyle::revert(QPainter *p, QSvgExtraStates &states)':
    takes a type Python has no way to hand over yet.
  - Qt's 'void QSvgFillStyle::setPaintServer(QSvgPaintServerSharedPtr
    paintServer)': takes a type Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ QSvgFillStyle is created at the first use, not by
    'QSvgFillStyle(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSvgFillStyle back gives a copy the ritual made for
    Python, in a new cute QSvgFillStyle.
  - Each name of Qt's QSvgFillStyle that has no cute function yet,
    'setPaintServer', holds a function that raises 'NotImplementedError', and
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
  __qt_class__ = 'QSvgFillStyle'

  #  A C++ QSvgFillStyle Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSvgFillStyle'

  #  Qt's '~QSvgFillStyle()'. Naming it makes this a value class: Python owns
  #  every C++ QSvgFillStyle behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN13QSvgFillStyleD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def type(self) -> QSvgStyleProperty.Type:
    """
    Calls Qt's 'Type QSvgFillStyle::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgfillstyle.html#type

    Returns
    -------

    QSvgStyleProperty.Type
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QSvgStyleProperty.Type(number)' gives.
    """
    #  Type QSvgFillStyle::type() const
    ritual = 'ritual_ZNK13QSvgFillStyle4typeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK13QSvgFillStyle4typeEv'
    return QSvgStyleProperty.Type(self.uglySide.call(ritual))

  def qbrush(self) -> QBrush:
    """
    Calls Qt's 'const QBrush &QSvgFillStyle::qbrush() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgfillstyle.html#qbrush

    Returns
    -------

    QBrush
      A new cute QBrush around the copy Qt gave back. Python owns it.
    """
    #  const QBrush &QSvgFillStyle::qbrush() const
    address = self.uglySide.call('ritual_ZNK13QSvgFillStyle6qbrushEv')
    from ..QtGui import QBrush
    return QBrush._cuteOwning(address)

  def fillOpacity(self) -> float:
    """
    Calls Qt's 'qreal QSvgFillStyle::fillOpacity() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgfillstyle.html#fillOpacity
    """
    #  qreal QSvgFillStyle::fillOpacity() const
    return self.uglySide.call('ritual_ZNK13QSvgFillStyle11fillOpacityEv')

  def fillRule(self) -> Qt.FillRule:
    """
    Calls Qt's 'Qt::FillRule QSvgFillStyle::fillRule() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgfillstyle.html#fillRule

    Returns
    -------

    Qt.FillRule
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.FillRule(number)'
      gives.
    """
    #  Qt::FillRule QSvgFillStyle::fillRule() const
    return Qt.FillRule(self.uglySide.call(
        'ritual_ZNK13QSvgFillStyle8fillRuleEv',
    ))

  def paintServer(self) -> Optional[QSvgPaintServer]:
    """
    Calls Qt's 'QSvgPaintServer *QSvgFillStyle::paintServer() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgfillstyle.html#paintServer

    Returns
    -------

    Optional[QSvgPaintServer]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSvgPaintServer *QSvgFillStyle::paintServer() const
    address = self.uglySide.call('ritual_ZNK13QSvgFillStyle11paintServerEv')
    from . import QSvgPaintServer
    return QSvgPaintServer._cuteAt(address)

  def paintStyleId(self) -> str:
    """
    Calls Qt's 'QString QSvgFillStyle::paintStyleId() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgfillstyle.html#paintStyleId

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSvgFillStyle::paintStyleId() const
    return self.uglySide.call('ritual_ZNK13QSvgFillStyle12paintStyleIdEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Qt.FillRule)
  def setFillRule(self, f: Qt.FillRule) -> None:
    """
    Calls Qt's 'void QSvgFillStyle::setFillRule(Qt::FillRule f)'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgfillstyle.html#setFillRule

    Parameters
    ----------

    f : Qt.FillRule
      Passed on as its number.
    """
    #  void QSvgFillStyle::setFillRule(Qt::FillRule f)
    self.uglySide.call(
        'ritual_ZN13QSvgFillStyle11setFillRuleEN2Qt8FillRuleE', f.value,
    )

  @overload(float)
  def setFillOpacity(self, opacity: float) -> None:
    """
    Calls Qt's 'void QSvgFillStyle::setFillOpacity(qreal opacity)'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgfillstyle.html#setFillOpacity

    Parameters
    ----------

    opacity : float
      Passed on as it is.
    """
    #  void QSvgFillStyle::setFillOpacity(qreal opacity)
    self.uglySide.call('ritual_ZN13QSvgFillStyle14setFillOpacityEd', opacity)

  @overload(QBrush)
  def setBrush(self, brush: QBrush) -> None:
    """
    Calls Qt's 'void QSvgFillStyle::setBrush(QBrush brush)'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgfillstyle.html#setBrush

    Parameters
    ----------

    brush : QBrush
      Passed on as a value: Qt reads the C++ QBrush, which stays Python's
      own.
    """
    #  void QSvgFillStyle::setBrush(QBrush brush)
    self.uglySide.call(
        'ritual_ZN13QSvgFillStyle8setBrushE6QBrush', self._valueOf(brush),
    )

  @overload(str)
  def setPaintStyleId(self, Id: str) -> None:
    """
    Calls Qt's 'void QSvgFillStyle::setPaintStyleId(const QString &Id)'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgfillstyle.html#setPaintStyleId

    Parameters
    ----------

    Id : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QSvgFillStyle::setPaintStyleId(const QString &Id)
    self.uglySide.call(
        'ritual_ZN13QSvgFillStyle15setPaintStyleIdERK7QString', Id,
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
    Notes what was given, for Qt's 'QSvgFillStyle::QSvgFillStyle()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qsvgfillstyle.html#QSvgFillStyle
    """
    #  QSvgFillStyle::QSvgFillStyle()
    self._noteCreation(QSvgFillStyle, lambda: Rituals.call(
        'ritual_ZN13QSvgFillStyleC1Ev',
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

  @staticmethod
  def setPaintServer(*__, **_) -> Never:
    """
    Qt's 'void QSvgFillStyle::setPaintServer(QSvgPaintServerSharedPtr
    paintServer)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSvgFillStyle.setPaintServer' has no cute function yet. Qt's "
        "'void QSvgFillStyle::setPaintServer(QSvgPaintServerSharedPtr "
        "paintServer)': takes a type Python has no way to hand over yet.")
