"""
QRadioButton binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qradiobutton.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QAbstractButton, QWidget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QEvent, QMetaObject, QPoint, QSize
  from ..QtGui import QMouseEvent, QPaintEvent
  from . import QStyleOptionButton
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEvent = WAIT['QEvent']
  QMouseEvent = WAIT['QMouseEvent']
  QPaintEvent = WAIT['QPaintEvent']
  QPoint = WAIT['QPoint']
  QStyleOptionButton = WAIT['QStyleOptionButton']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QRadioButton(QAbstractButton):
  """
  The cute side of Qt's QRadioButton: a plain Python object standing in front
  of one C++ QRadioButton.

  It is built on the cute 'QAbstractButton', as Qt's QRadioButton is built on
  Qt's QAbstractButton, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QRadioButton that has a ritual and that Python can
  call so far, 9 names in all: 'metaObject', 'tr', 'sizeHint',
  'minimumSizeHint', 'event', 'hitButton', 'paintEvent', 'mouseMoveEvent',
  'initStyleOption'. It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QRadioButton::~QRadioButton()': the destructor: Python never
    removes a C++ QRadioButton.

  What has no ritual
  ------------------

  8 of the 20 functions Qt declares: 3 private; 2 takes or gives a type that
  cannot be passed yet; 2 forbidden; 1 a template.

  What to expect
  --------------

  - The C++ QRadioButton is created at the first use, not by
    'QRadioButton(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QRadioButton.
  - Qt tells when it has removed the C++ QRadioButton. Every call on the cute
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
    Calls Qt's 'QString QRadioButton::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qradiobutton.html#tr

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
    #  QString QRadioButton::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN12QRadioButton2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QRadioButton'

  #  A C++ QRadioButton Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QRadioButton'

  #  The functions Qt calls itself that QRadioButton is the first to declare.
  #  A class of a program built on it can write one anew, and Qt then calls
  #  that. For each name: the key C++ knows the function by, what it gives,
  #  and what it takes.
  __virtual_functions__ = {
      'initStyleOption': (
          ('_ZNK12QRadioButton15initStyleOptionEP18QStyleOptionButton',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtWidgets:QStyleOptionButton'),
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
    Calls Qt's 'const QMetaObject *QRadioButton::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qradiobutton.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QRadioButton::metaObject() const
    address = self.uglySide.call('ritual_ZNK12QRadioButton10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def sizeHint(self) -> QSize:
    """
    Calls Qt's 'QSize QRadioButton::sizeHint() const'.

    Qt's own words: https://doc.qt.io/qt-6/qradiobutton.html#sizeHint

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QRadioButton::sizeHint() const
    ritual = 'ritual_ZNK12QRadioButton8sizeHintEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK12QRadioButton8sizeHintEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def minimumSizeHint(self) -> QSize:
    """
    Calls Qt's 'QSize QRadioButton::minimumSizeHint() const'.

    Qt's own words: https://doc.qt.io/qt-6/qradiobutton.html#minimumSizeHint

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QRadioButton::minimumSizeHint() const
    ritual = 'ritual_ZNK12QRadioButton15minimumSizeHintEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK12QRadioButton15minimumSizeHintEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  @overload(QPoint)
  def hitButton(self, a0: QPoint) -> bool:
    """
    Calls Qt's 'bool QRadioButton::hitButton(const QPoint &a0) const'.

    Qt's own words: https://doc.qt.io/qt-6/qradiobutton.html#hitButton

    Parameters
    ----------

    a0 : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  bool QRadioButton::hitButton(const QPoint &a0) const
    return self.uglySide.call(
        'ritual_own_ZNK12QRadioButton9hitButtonERK6QPoint',
        self._valueOf(a0),
    )

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

  @overload()
  @overload(QWidget)
  @overload(NoneType)
  def __init__(self, parent: Optional[QWidget] = None) -> None:
    """
    Notes what was given, for Qt's 'QRadioButton::QRadioButton(QWidget
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qradiobutton.html#QRadioButton

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QRadioButton::QRadioButton(QWidget *parent)
    self._noteCreation(QRadioButton, lambda: Rituals.call(
        'ritual_ZN12QRadioButtonC1EP7QWidget', self._addressOf(parent),
    ))

  @overload(str)
  @overload(str, QWidget)
  @overload(str, NoneType)
  def __init__(self, text: str, parent: Optional[QWidget] = None) -> None:
    """
    Notes what was given, for Qt's 'QRadioButton::QRadioButton(const QString
    &text, QWidget *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qradiobutton.html#QRadioButton

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QRadioButton::QRadioButton(const QString &text, QWidget *parent)
    self._noteCreation(QRadioButton, lambda: Rituals.call(
        'ritual_ZN12QRadioButtonC1ERK7QStringP7QWidget',
        text, self._addressOf(parent),
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

  @overload(QEvent)
  @overload(NoneType)
  def event(self, e: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QRadioButton::event(QEvent *e)'.

    Qt's own words: https://doc.qt.io/qt-6/qradiobutton.html#event

    Parameters
    ----------

    e : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QRadioButton::event(QEvent *e)
    return self.uglySide.call(
        'ritual_own_ZN12QRadioButton5eventEP6QEvent', self._addressOf(e),
    )

  @overload(QPaintEvent)
  @overload(NoneType)
  def paintEvent(self, a0: Optional[QPaintEvent]) -> None:
    """
    Calls Qt's 'void QRadioButton::paintEvent(QPaintEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qradiobutton.html#paintEvent

    Parameters
    ----------

    a0 : Optional[QPaintEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QRadioButton::paintEvent(QPaintEvent *a0)
    self.uglySide.call(
        'ritual_own_ZN12QRadioButton10paintEventEP11QPaintEvent',
        self._addressOf(a0),
    )

  @overload(QMouseEvent)
  @overload(NoneType)
  def mouseMoveEvent(self, a0: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QRadioButton::mouseMoveEvent(QMouseEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qradiobutton.html#mouseMoveEvent

    Parameters
    ----------

    a0 : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QRadioButton::mouseMoveEvent(QMouseEvent *a0)
    self.uglySide.call(
        'ritual_own_ZN12QRadioButton14mouseMoveEventEP11QMouseEvent',
        self._addressOf(a0),
    )

  @overload(QStyleOptionButton)
  @overload(NoneType)
  def initStyleOption(self, button: Optional[QStyleOptionButton]) -> None:
    """
    Calls Qt's 'void QRadioButton::initStyleOption(QStyleOptionButton
    *button) const'.

    Qt's own words: https://doc.qt.io/qt-6/qradiobutton.html#initStyleOption

    Parameters
    ----------

    button : Optional[QStyleOptionButton]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QRadioButton::initStyleOption(QStyleOptionButton *button) const
    self.uglySide.call(
        'ritual_own_ZNK12QRadioButton15initStyleOptionEP18QStyleOptionButto'
        'n',
        self._addressOf(button),
    )
