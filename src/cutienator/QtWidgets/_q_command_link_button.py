"""
QCommandLinkButton binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qcommandlinkbutton.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QPushButton, QWidget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QEvent, QMetaObject, QSize
  from ..QtGui import QPaintEvent
  from . import QStyleOptionButton
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEvent = WAIT['QEvent']
  QPaintEvent = WAIT['QPaintEvent']
  QStyleOptionButton = WAIT['QStyleOptionButton']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QCommandLinkButton(QPushButton):
  """
  The cute side of Qt's QCommandLinkButton: a plain Python object standing in
  front of one C++ QCommandLinkButton.

  It is built on the cute 'QPushButton', as Qt's QCommandLinkButton is built
  on Qt's QPushButton, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QCommandLinkButton that has a ritual and that Python
  can call so far, 10 names in all: 'metaObject', 'tr', 'description',
  'setDescription', 'sizeHint', 'heightForWidth', 'minimumSizeHint',
  'initStyleOption', 'event', 'paintEvent'. It can be made from Python, in 3
  ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QCommandLinkButton::~QCommandLinkButton()': the destructor: Python
    never removes a C++ QCommandLinkButton.

  What has no ritual
  ------------------

  8 of the 22 functions Qt declares: 3 private; 2 takes or gives a type that
  cannot be passed yet; 2 forbidden; 1 a template.

  What to expect
  --------------

  - The C++ QCommandLinkButton is created at the first use, not by
    'QCommandLinkButton(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QCommandLinkButton.
  - Qt tells when it has removed the C++ QCommandLinkButton. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
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
    Calls Qt's 'QString QCommandLinkButton::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qcommandlinkbutton.html#tr

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
    #  QString QCommandLinkButton::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN18QCommandLinkButton2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCommandLinkButton'

  #  A C++ QCommandLinkButton Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QCommandLinkButton'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QCommandLinkButton::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcommandlinkbutton.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QCommandLinkButton::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK18QCommandLinkButton10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def description(self) -> str:
    """
    Calls Qt's 'QString QCommandLinkButton::description() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcommandlinkbutton.html#description

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QCommandLinkButton::description() const
    return self.uglySide.call(
        'ritual_ZNK18QCommandLinkButton11descriptionEv',
    )

  def sizeHint(self) -> QSize:
    """
    Calls Qt's 'QSize QCommandLinkButton::sizeHint() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcommandlinkbutton.html#sizeHint

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QCommandLinkButton::sizeHint() const
    ritual = 'ritual_ZNK18QCommandLinkButton8sizeHintEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK18QCommandLinkButton8sizeHintEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  @overload(int)
  def heightForWidth(self, a0: int) -> int:
    """
    Calls Qt's 'int QCommandLinkButton::heightForWidth(int a0) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcommandlinkbutton.html#heightForWidth

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  int QCommandLinkButton::heightForWidth(int a0) const
    ritual = 'ritual_ZNK18QCommandLinkButton14heightForWidthEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK18QCommandLinkButton14heightForWidthEi'
    return self.uglySide.call(ritual, a0)

  def minimumSizeHint(self) -> QSize:
    """
    Calls Qt's 'QSize QCommandLinkButton::minimumSizeHint() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcommandlinkbutton.html#minimumSizeHint

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QCommandLinkButton::minimumSizeHint() const
    ritual = 'ritual_ZNK18QCommandLinkButton15minimumSizeHintEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK18QCommandLinkButton15minimumSizeHintEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setDescription(self, description: str) -> None:
    """
    Calls Qt's 'void QCommandLinkButton::setDescription(const QString
    &description)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcommandlinkbutton.html#setDescription

    Parameters
    ----------

    description : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QCommandLinkButton::setDescription(const QString &description)
    self.uglySide.call(
        'ritual_ZN18QCommandLinkButton14setDescriptionERK7QString',
        description,
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
  @overload(QWidget)
  @overload(NoneType)
  def __init__(self, parent: Optional[QWidget] = None) -> None:
    """
    Notes what was given, for Qt's
    'QCommandLinkButton::QCommandLinkButton(QWidget *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcommandlinkbutton.html#QCommandLinkButton

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QCommandLinkButton::QCommandLinkButton(QWidget *parent)
    self._noteCreation(QCommandLinkButton, lambda: Rituals.call(
        'ritual_ZN18QCommandLinkButtonC1EP7QWidget', self._addressOf(parent),
    ))

  @overload(str)
  @overload(str, QWidget)
  @overload(str, NoneType)
  def __init__(self, text: str, parent: Optional[QWidget] = None) -> None:
    """
    Notes what was given, for Qt's
    'QCommandLinkButton::QCommandLinkButton(const QString &text, QWidget
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcommandlinkbutton.html#QCommandLinkButton

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QCommandLinkButton::QCommandLinkButton(const QString &text, QWidget
    #      *parent)
    self._noteCreation(QCommandLinkButton, lambda: Rituals.call(
        'ritual_ZN18QCommandLinkButtonC1ERK7QStringP7QWidget',
        text, self._addressOf(parent),
    ))

  @overload(str, str)
  @overload(str, str, QWidget)
  @overload(str, str, NoneType)
  def __init__(
      self,
      text: str,
      description: str,
      parent: Optional[QWidget] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QCommandLinkButton::QCommandLinkButton(const QString &text, const
    QString &description, QWidget *parent)', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcommandlinkbutton.html#QCommandLinkButton

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.

    description : str
      Passed on as it is: a QString is made of it for the call.

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QCommandLinkButton::QCommandLinkButton(const QString &text, const
    #      QString &description, QWidget *parent)
    self._noteCreation(QCommandLinkButton, lambda: Rituals.call(
        'ritual_ZN18QCommandLinkButtonC1ERK7QStringS2_P7QWidget',
        text, description, self._addressOf(parent),
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

  @overload(QStyleOptionButton)
  @overload(NoneType)
  def initStyleOption(self, option: Optional[QStyleOptionButton]) -> None:
    """
    Calls Qt's 'void QCommandLinkButton::initStyleOption(QStyleOptionButton
    *option) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcommandlinkbutton.html#initStyleOption

    Parameters
    ----------

    option : Optional[QStyleOptionButton]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QCommandLinkButton::initStyleOption(QStyleOptionButton *option)
    #      const
    ritual = (
        'ritual_ZNK18QCommandLinkButton15initStyleOptionEP18QStyleOptionBut'
        'ton')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK18QCommandLinkButton15initStyleOptionEP18QStyleOpt'
          'ionButton')
    self.uglySide.call(ritual, self._addressOf(option))

  @overload(QEvent)
  @overload(NoneType)
  def event(self, e: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QCommandLinkButton::event(QEvent *e)'.

    Qt's own words: https://doc.qt.io/qt-6/qcommandlinkbutton.html#event

    Parameters
    ----------

    e : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QCommandLinkButton::event(QEvent *e)
    return self.uglySide.call(
        'ritual_own_ZN18QCommandLinkButton5eventEP6QEvent',
        self._addressOf(e),
    )

  @overload(QPaintEvent)
  @overload(NoneType)
  def paintEvent(self, a0: Optional[QPaintEvent]) -> None:
    """
    Calls Qt's 'void QCommandLinkButton::paintEvent(QPaintEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qcommandlinkbutton.html#paintEvent

    Parameters
    ----------

    a0 : Optional[QPaintEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QCommandLinkButton::paintEvent(QPaintEvent *a0)
    self.uglySide.call(
        'ritual_own_ZN18QCommandLinkButton10paintEventEP11QPaintEvent',
        self._addressOf(a0),
    )
