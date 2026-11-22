"""
QGroupBox binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qgroupbox.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt
from . import QWidget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QChildEvent, QEvent, QMetaObject, QSize
  from ..QtGui import QFocusEvent, QMouseEvent, QPaintEvent, QResizeEvent
  from . import QStyleOptionGroupBox
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QChildEvent = WAIT['QChildEvent']
  QEvent = WAIT['QEvent']
  QFocusEvent = WAIT['QFocusEvent']
  QMouseEvent = WAIT['QMouseEvent']
  QPaintEvent = WAIT['QPaintEvent']
  QResizeEvent = WAIT['QResizeEvent']
  QStyleOptionGroupBox = WAIT['QStyleOptionGroupBox']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QGroupBox(QWidget):
  """
  The cute side of Qt's QGroupBox: a plain Python object standing in front of
  one C++ QGroupBox.

  It is built on the cute 'QWidget', as Qt's QGroupBox is built on Qt's
  QWidget, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QGroupBox that has a ritual and that Python can call
  so far, 23 names in all: 'metaObject', 'tr', 'title', 'setTitle',
  'alignment', 'setAlignment', 'minimumSizeHint', 'isFlat', 'setFlat',
  'isCheckable', 'setCheckable', 'isChecked', 'setChecked', 'event',
  'childEvent', 'resizeEvent', 'paintEvent', 'focusInEvent', 'changeEvent',
  'mousePressEvent', 'mouseMoveEvent', 'mouseReleaseEvent',
  'initStyleOption'. It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QGroupBox::~QGroupBox()': the destructor: Python never removes a
    C++ QGroupBox.

  What has no ritual
  ------------------

  10 of the 36 functions Qt declares: 3 private; 2 takes or gives a type that
  cannot be passed yet; 2 a signal; 2 forbidden; 1 a template.

  What to expect
  --------------

  - The C++ QGroupBox is created at the first use, not by 'QGroupBox(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGroupBox.
  - Qt tells when it has removed the C++ QGroupBox. Every call on the cute
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
    Calls Qt's 'QString QGroupBox::tr(const char *s, const char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qgroupbox.html#tr

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
    #  QString QGroupBox::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN9QGroupBox2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGroupBox'

  #  A C++ QGroupBox Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QGroupBox'

  #  The functions Qt calls itself that QGroupBox is the first to declare. A
  #  class of a program built on it can write one anew, and Qt then calls
  #  that. For each name: the key C++ knows the function by, what it gives,
  #  and what it takes.
  __virtual_functions__ = {
      'initStyleOption': (
          ('_ZNK9QGroupBox15initStyleOptionEP20QStyleOptionGroupBox',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtWidgets:QStyleOptionGroupBox'),
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
    Calls Qt's 'const QMetaObject *QGroupBox::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgroupbox.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QGroupBox::metaObject() const
    address = self.uglySide.call('ritual_ZNK9QGroupBox10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def title(self) -> str:
    """
    Calls Qt's 'QString QGroupBox::title() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgroupbox.html#title

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QGroupBox::title() const
    return self.uglySide.call('ritual_ZNK9QGroupBox5titleEv')

  def alignment(self) -> Qt.Alignment:
    """
    Calls Qt's 'Qt::Alignment QGroupBox::alignment() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgroupbox.html#alignment

    Returns
    -------

    Qt.Alignment
      The value standing for the combination Qt gave back.
    """
    #  Qt::Alignment QGroupBox::alignment() const
    return Qt.Alignment(self.uglySide.call(
        'ritual_ZNK9QGroupBox9alignmentEv',
    ))

  def minimumSizeHint(self) -> QSize:
    """
    Calls Qt's 'QSize QGroupBox::minimumSizeHint() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgroupbox.html#minimumSizeHint

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QGroupBox::minimumSizeHint() const
    ritual = 'ritual_ZNK9QGroupBox15minimumSizeHintEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK9QGroupBox15minimumSizeHintEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def isFlat(self) -> bool:
    """
    Calls Qt's 'bool QGroupBox::isFlat() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgroupbox.html#isFlat
    """
    #  bool QGroupBox::isFlat() const
    return self.uglySide.call('ritual_ZNK9QGroupBox6isFlatEv')

  def isCheckable(self) -> bool:
    """
    Calls Qt's 'bool QGroupBox::isCheckable() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgroupbox.html#isCheckable
    """
    #  bool QGroupBox::isCheckable() const
    return self.uglySide.call('ritual_ZNK9QGroupBox11isCheckableEv')

  def isChecked(self) -> bool:
    """
    Calls Qt's 'bool QGroupBox::isChecked() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgroupbox.html#isChecked
    """
    #  bool QGroupBox::isChecked() const
    return self.uglySide.call('ritual_ZNK9QGroupBox9isCheckedEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setTitle(self, title: str) -> None:
    """
    Calls Qt's 'void QGroupBox::setTitle(const QString &title)'.

    Qt's own words: https://doc.qt.io/qt-6/qgroupbox.html#setTitle

    Parameters
    ----------

    title : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QGroupBox::setTitle(const QString &title)
    self.uglySide.call('ritual_ZN9QGroupBox8setTitleERK7QString', title)

  @overload(int)
  def setAlignment(self, alignment: int) -> None:
    """
    Calls Qt's 'void QGroupBox::setAlignment(int alignment)'.

    Qt's own words: https://doc.qt.io/qt-6/qgroupbox.html#setAlignment

    Parameters
    ----------

    alignment : int
      Passed on as it is.
    """
    #  void QGroupBox::setAlignment(int alignment)
    self.uglySide.call('ritual_ZN9QGroupBox12setAlignmentEi', alignment)

  @overload(bool)
  def setFlat(self, flat: bool) -> None:
    """
    Calls Qt's 'void QGroupBox::setFlat(bool flat)'.

    Qt's own words: https://doc.qt.io/qt-6/qgroupbox.html#setFlat

    Parameters
    ----------

    flat : bool
      Passed on as it is.
    """
    #  void QGroupBox::setFlat(bool flat)
    self.uglySide.call('ritual_ZN9QGroupBox7setFlatEb', flat)

  @overload(bool)
  def setCheckable(self, checkable: bool) -> None:
    """
    Calls Qt's 'void QGroupBox::setCheckable(bool checkable)'.

    Qt's own words: https://doc.qt.io/qt-6/qgroupbox.html#setCheckable

    Parameters
    ----------

    checkable : bool
      Passed on as it is.
    """
    #  void QGroupBox::setCheckable(bool checkable)
    self.uglySide.call('ritual_ZN9QGroupBox12setCheckableEb', checkable)

  @overload(bool)
  def setChecked(self, checked: bool) -> None:
    """
    Calls Qt's 'void QGroupBox::setChecked(bool checked)'.

    Qt's own words: https://doc.qt.io/qt-6/qgroupbox.html#setChecked

    Parameters
    ----------

    checked : bool
      Passed on as it is.
    """
    #  void QGroupBox::setChecked(bool checked)
    self.uglySide.call('ritual_ZN9QGroupBox10setCheckedEb', checked)

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
    Notes what was given, for Qt's 'QGroupBox::QGroupBox(QWidget *parent)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qgroupbox.html#QGroupBox

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QGroupBox::QGroupBox(QWidget *parent)
    self._noteCreation(QGroupBox, lambda: Rituals.call(
        'ritual_ZN9QGroupBoxC1EP7QWidget', self._addressOf(parent),
    ))

  @overload(str)
  @overload(str, QWidget)
  @overload(str, NoneType)
  def __init__(self, title: str, parent: Optional[QWidget] = None) -> None:
    """
    Notes what was given, for Qt's 'QGroupBox::QGroupBox(const QString
    &title, QWidget *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qgroupbox.html#QGroupBox

    Parameters
    ----------

    title : str
      Passed on as it is: a QString is made of it for the call.

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QGroupBox::QGroupBox(const QString &title, QWidget *parent)
    self._noteCreation(QGroupBox, lambda: Rituals.call(
        'ritual_ZN9QGroupBoxC1ERK7QStringP7QWidget',
        title, self._addressOf(parent),
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
  def event(self, event: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QGroupBox::event(QEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qgroupbox.html#event

    Parameters
    ----------

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QGroupBox::event(QEvent *event)
    return self.uglySide.call(
        'ritual_own_ZN9QGroupBox5eventEP6QEvent', self._addressOf(event),
    )

  @overload(QChildEvent)
  @overload(NoneType)
  def childEvent(self, event: Optional[QChildEvent]) -> None:
    """
    Calls Qt's 'void QGroupBox::childEvent(QChildEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qgroupbox.html#childEvent

    Parameters
    ----------

    event : Optional[QChildEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGroupBox::childEvent(QChildEvent *event)
    self.uglySide.call(
        'ritual_own_ZN9QGroupBox10childEventEP11QChildEvent',
        self._addressOf(event),
    )

  @overload(QResizeEvent)
  @overload(NoneType)
  def resizeEvent(self, event: Optional[QResizeEvent]) -> None:
    """
    Calls Qt's 'void QGroupBox::resizeEvent(QResizeEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qgroupbox.html#resizeEvent

    Parameters
    ----------

    event : Optional[QResizeEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGroupBox::resizeEvent(QResizeEvent *event)
    self.uglySide.call(
        'ritual_own_ZN9QGroupBox11resizeEventEP12QResizeEvent',
        self._addressOf(event),
    )

  @overload(QPaintEvent)
  @overload(NoneType)
  def paintEvent(self, event: Optional[QPaintEvent]) -> None:
    """
    Calls Qt's 'void QGroupBox::paintEvent(QPaintEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qgroupbox.html#paintEvent

    Parameters
    ----------

    event : Optional[QPaintEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGroupBox::paintEvent(QPaintEvent *event)
    self.uglySide.call(
        'ritual_own_ZN9QGroupBox10paintEventEP11QPaintEvent',
        self._addressOf(event),
    )

  @overload(QFocusEvent)
  @overload(NoneType)
  def focusInEvent(self, event: Optional[QFocusEvent]) -> None:
    """
    Calls Qt's 'void QGroupBox::focusInEvent(QFocusEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qgroupbox.html#focusInEvent

    Parameters
    ----------

    event : Optional[QFocusEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGroupBox::focusInEvent(QFocusEvent *event)
    self.uglySide.call(
        'ritual_own_ZN9QGroupBox12focusInEventEP11QFocusEvent',
        self._addressOf(event),
    )

  @overload(QEvent)
  @overload(NoneType)
  def changeEvent(self, event: Optional[QEvent]) -> None:
    """
    Calls Qt's 'void QGroupBox::changeEvent(QEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qgroupbox.html#changeEvent

    Parameters
    ----------

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGroupBox::changeEvent(QEvent *event)
    self.uglySide.call(
        'ritual_own_ZN9QGroupBox11changeEventEP6QEvent',
        self._addressOf(event),
    )

  @overload(QMouseEvent)
  @overload(NoneType)
  def mousePressEvent(self, event: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QGroupBox::mousePressEvent(QMouseEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qgroupbox.html#mousePressEvent

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGroupBox::mousePressEvent(QMouseEvent *event)
    self.uglySide.call(
        'ritual_own_ZN9QGroupBox15mousePressEventEP11QMouseEvent',
        self._addressOf(event),
    )

  @overload(QMouseEvent)
  @overload(NoneType)
  def mouseMoveEvent(self, event: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QGroupBox::mouseMoveEvent(QMouseEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qgroupbox.html#mouseMoveEvent

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGroupBox::mouseMoveEvent(QMouseEvent *event)
    self.uglySide.call(
        'ritual_own_ZN9QGroupBox14mouseMoveEventEP11QMouseEvent',
        self._addressOf(event),
    )

  @overload(QMouseEvent)
  @overload(NoneType)
  def mouseReleaseEvent(self, event: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QGroupBox::mouseReleaseEvent(QMouseEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qgroupbox.html#mouseReleaseEvent

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGroupBox::mouseReleaseEvent(QMouseEvent *event)
    self.uglySide.call(
        'ritual_own_ZN9QGroupBox17mouseReleaseEventEP11QMouseEvent',
        self._addressOf(event),
    )

  @overload(QStyleOptionGroupBox)
  @overload(NoneType)
  def initStyleOption(self, option: Optional[QStyleOptionGroupBox]) -> None:
    """
    Calls Qt's 'void QGroupBox::initStyleOption(QStyleOptionGroupBox *option)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qgroupbox.html#initStyleOption

    Parameters
    ----------

    option : Optional[QStyleOptionGroupBox]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGroupBox::initStyleOption(QStyleOptionGroupBox *option) const
    self.uglySide.call(
        'ritual_own_ZNK9QGroupBox15initStyleOptionEP20QStyleOptionGroupBox',
        self._addressOf(option),
    )
