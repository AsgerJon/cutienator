"""
QWhatsThis binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qwhatsthis.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QObject, QPoint
  from ..QtGui import QAction
  from . import QWidget
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QObject = WAIT['QObject']
  QPoint = WAIT['QPoint']
  QWidget = WAIT['QWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QWhatsThis(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QWhatsThis: a plain Python object standing in front
  of one C++ QWhatsThis.

  C++ hands a QWhatsThis around as a copy, so every C++ QWhatsThis behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QWhatsThis that has a ritual and that Python can
  call so far, 6 names in all: 'enterWhatsThisMode', 'inWhatsThisMode',
  'leaveWhatsThisMode', 'showText', 'hideText', 'createAction'. None can be
  made from Python: one comes out of a function of another class that gives
  one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QWhatsThis::~QWhatsThis()': the destructor: Python removes its C++
    QWhatsThis by it, and has no other use for it.

  What has no ritual
  ------------------

  1 of the 8 functions Qt declares: 1 forbidden.

  What to expect
  --------------

  - The C++ QWhatsThis is created at the first use, not by 'QWhatsThis(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QWhatsThis back gives a copy the ritual made for
    Python, in a new cute QWhatsThis.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def enterWhatsThisMode() -> None:
    """
    Calls Qt's 'void QWhatsThis::enterWhatsThisMode()'.

    Qt's own words: https://doc.qt.io/qt-6/qwhatsthis.html#enterWhatsThisMode
    """
    #  void QWhatsThis::enterWhatsThisMode()
    Rituals.call('ritual_ZN10QWhatsThis18enterWhatsThisModeEv')

  @staticmethod
  def inWhatsThisMode() -> bool:
    """
    Calls Qt's 'bool QWhatsThis::inWhatsThisMode()'.

    Qt's own words: https://doc.qt.io/qt-6/qwhatsthis.html#inWhatsThisMode
    """
    #  bool QWhatsThis::inWhatsThisMode()
    return Rituals.call('ritual_ZN10QWhatsThis15inWhatsThisModeEv')

  @staticmethod
  def leaveWhatsThisMode() -> None:
    """
    Calls Qt's 'void QWhatsThis::leaveWhatsThisMode()'.

    Qt's own words: https://doc.qt.io/qt-6/qwhatsthis.html#leaveWhatsThisMode
    """
    #  void QWhatsThis::leaveWhatsThisMode()
    Rituals.call('ritual_ZN10QWhatsThis18leaveWhatsThisModeEv')

  @staticmethod
  @overload(QPoint, str)
  @overload(QPoint, str, QWidget)
  @overload(QPoint, str, NoneType)
  def showText(pos: QPoint, text: str, w: Optional[QWidget] = None) -> None:
    """
    Calls Qt's 'void QWhatsThis::showText(const QPoint &pos, const QString
    &text, QWidget *w)'.

    Qt's own words: https://doc.qt.io/qt-6/qwhatsthis.html#showText

    Parameters
    ----------

    pos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    text : str
      Passed on as it is: a QString is made of it for the call.

    w : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  void QWhatsThis::showText(const QPoint &pos, const QString &text,
    #      QWidget *w)
    Rituals.call(
        'ritual_ZN10QWhatsThis8showTextERK6QPointRK7QStringP7QWidget',
        CuteMixin._valueOf(pos), text, CuteMixin._addressOf(w),
    )

  @staticmethod
  def hideText() -> None:
    """
    Calls Qt's 'void QWhatsThis::hideText()'.

    Qt's own words: https://doc.qt.io/qt-6/qwhatsthis.html#hideText
    """
    #  void QWhatsThis::hideText()
    Rituals.call('ritual_ZN10QWhatsThis8hideTextEv')

  @staticmethod
  @overload()
  @overload(QObject)
  @overload(NoneType)
  def createAction(parent: Optional[QObject] = None) -> Optional[QAction]:
    """
    Calls Qt's 'QAction *QWhatsThis::createAction(QObject *parent)'.

    Qt's own words: https://doc.qt.io/qt-6/qwhatsthis.html#createAction

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    Returns
    -------

    Optional[QAction]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAction *QWhatsThis::createAction(QObject *parent)
    address = Rituals.call(
        'ritual_ZN10QWhatsThis12createActionEP7QObject',
        CuteMixin._addressOf(parent, 'QObject'),
    )
    from ..QtGui import QAction
    return QAction._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWhatsThis'

  #  Qt's '~QWhatsThis()'. Naming it makes this a value class: Python owns
  #  every C++ QWhatsThis behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN10QWhatsThisD1Ev'

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
