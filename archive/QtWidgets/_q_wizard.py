"""
QWizard binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qwizard.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import Qt
from . import QDialog, QWidget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QEvent, QMetaObject, QSize, QVariant
  from ..QtGui import QPaintEvent, QPixmap, QResizeEvent
  from . import QAbstractButton, QWizardPage
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAbstractButton = WAIT['QAbstractButton']
  QEvent = WAIT['QEvent']
  QPaintEvent = WAIT['QPaintEvent']
  QPixmap = WAIT['QPixmap']
  QResizeEvent = WAIT['QResizeEvent']
  QVariant = WAIT['QVariant']
  QWizardPage = WAIT['QWizardPage']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QWizard(QDialog):
  """
  The cute side of Qt's QWizard: a plain Python object standing in front of
  one C++ QWizard.

  It is built on the cute 'QDialog', as Qt's QWizard is built on Qt's
  QDialog, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QWizard that has a ritual and that Python can call
  so far, 46 names in all: 'metaObject', 'tr', 'addPage', 'setPage',
  'removePage', 'page', 'hasVisitedPage', 'setStartId', 'startId',
  'currentPage', 'currentId', 'validateCurrentPage', 'nextId', 'setField',
  'field', 'setWizardStyle', 'wizardStyle', 'setOption', 'testOption',
  'setOptions', 'options', 'setButtonText', 'buttonText', 'setButton',
  'button', 'setTitleFormat', 'titleFormat', 'setSubTitleFormat',
  'subTitleFormat', 'setPixmap', 'pixmap', 'setSideWidget', 'sideWidget',
  'setDefaultProperty', 'setVisible', 'sizeHint', 'back', 'next',
  'setCurrentId', 'restart', 'event', 'resizeEvent', 'paintEvent', 'done',
  'initializePage', 'cleanupPage'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QWizard::~QWizard()': the destructor: Python never removes a C++
    QWizard.

  What has no ritual
  ------------------

  16 of the 64 functions Qt declares: 7 takes or gives a type that cannot be
  passed yet; 5 a signal; 2 forbidden; 1 a template; 1 declared and nowhere
  to be found.

  What to expect
  --------------

  - The C++ QWizard is created at the first use, not by 'QWizard(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QWizard.
  - Qt tells when it has removed the C++ QWizard. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  """

  #  The enums Qt writes inside QWizard, each a class in here as in C++, and
  #  the names Qt has for the combinations of its flags enums.

  class WizardButton(CuteNum):
    """
    The enum 'QWizard::WizardButton' of Qt, with the 13 names Qt gives in it.
    """

    BackButton = Kee[int](0)
    NextButton = Kee[int](1)
    CommitButton = Kee[int](2)
    FinishButton = Kee[int](3)
    CancelButton = Kee[int](4)
    HelpButton = Kee[int](5)
    CustomButton1 = Kee[int](6)
    CustomButton2 = Kee[int](7)
    CustomButton3 = Kee[int](8)
    Stretch = Kee[int](9)
    NoButton = Kee[int](-1)
    NStandardButtons = Kee[int](6)
    NButtons = Kee[int](9)

  class WizardOption(CuteFlags):
    """
    The flags enum 'QWizard::WizardOption' of Qt, with the 18 names Qt gives
    in it. Qt names the type of its combinations 'QWizard::WizardOptions'.
    """

    IndependentPages = 0x1
    IgnoreSubTitles = 0x2
    ExtendedWatermarkPixmap = 0x4
    NoDefaultButton = 0x8
    NoBackButtonOnStartPage = 0x10
    NoBackButtonOnLastPage = 0x20
    DisabledBackButtonOnLastPage = 0x40
    HaveNextButtonOnLastPage = 0x80
    HaveFinishButtonOnEarlyPages = 0x100
    NoCancelButton = 0x200
    CancelButtonOnLeft = 0x400
    HaveHelpButton = 0x800
    HelpButtonOnRight = 0x1000
    HaveCustomButton1 = 0x2000
    HaveCustomButton2 = 0x4000
    HaveCustomButton3 = 0x8000
    NoCancelButtonOnLastPage = 0x10000
    StretchBanner = 0x20000

  WizardOptions = WizardOption

  class WizardPixmap(CuteNum):
    """
    The enum 'QWizard::WizardPixmap' of Qt, with the 5 names Qt gives in it.
    """

    WatermarkPixmap = Kee[int](0)
    LogoPixmap = Kee[int](1)
    BannerPixmap = Kee[int](2)
    BackgroundPixmap = Kee[int](3)
    NPixmaps = Kee[int](4)

  class WizardStyle(CuteNum):
    """
    The enum 'QWizard::WizardStyle' of Qt, with the 5 names Qt gives in it.
    """

    ClassicStyle = Kee[int](0)
    ModernStyle = Kee[int](1)
    MacStyle = Kee[int](2)
    AeroStyle = Kee[int](3)
    NStyles = Kee[int](4)

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
    Calls Qt's 'QString QWizard::tr(const char *s, const char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qwizard.html#tr

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
    #  QString QWizard::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN7QWizard2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWizard'

  #  A C++ QWizard Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QWizard'

  #  The functions Qt calls itself that QWizard is the first to declare. A
  #  class of a program built on it can write one anew, and Qt then calls
  #  that. For each name: the key C++ knows the function by, what it gives,
  #  and what it takes.
  __virtual_functions__ = {
      'validateCurrentPage': (
          ('_ZN7QWizard19validateCurrentPageEv',
           ('bool', 'number', ''),
           ()),
      ),
      'nextId': (
          ('_ZNK7QWizard6nextIdEv',
           ('int', 'number', ''),
           ()),
      ),
      'initializePage': (
          ('_ZN7QWizard14initializePageEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'cleanupPage': (
          ('_ZN7QWizard11cleanupPageEi',
           ('nothing', 'nothing', ''),
           (
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

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QWizard::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwizard.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QWizard::metaObject() const
    address = self.uglySide.call('ritual_ZNK7QWizard10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload(int)
  def page(self, id: int) -> Optional[QWizardPage]:
    """
    Calls Qt's 'QWizardPage *QWizard::page(int id) const'.

    Qt's own words: https://doc.qt.io/qt-6/qwizard.html#page

    Parameters
    ----------

    id : int
      Passed on as it is.

    Returns
    -------

    Optional[QWizardPage]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWizardPage *QWizard::page(int id) const
    address = self.uglySide.call('ritual_ZNK7QWizard4pageEi', id)
    from . import QWizardPage
    return QWizardPage._cuteAt(address)

  @overload(int)
  def hasVisitedPage(self, id: int) -> bool:
    """
    Calls Qt's 'bool QWizard::hasVisitedPage(int id) const'.

    Qt's own words: https://doc.qt.io/qt-6/qwizard.html#hasVisitedPage

    Parameters
    ----------

    id : int
      Passed on as it is.
    """
    #  bool QWizard::hasVisitedPage(int id) const
    return self.uglySide.call('ritual_ZNK7QWizard14hasVisitedPageEi', id)

  def startId(self) -> int:
    """
    Calls Qt's 'int QWizard::startId() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwizard.html#startId
    """
    #  int QWizard::startId() const
    return self.uglySide.call('ritual_ZNK7QWizard7startIdEv')

  def currentPage(self) -> Optional[QWizardPage]:
    """
    Calls Qt's 'QWizardPage *QWizard::currentPage() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwizard.html#currentPage

    Returns
    -------

    Optional[QWizardPage]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWizardPage *QWizard::currentPage() const
    address = self.uglySide.call('ritual_ZNK7QWizard11currentPageEv')
    from . import QWizardPage
    return QWizardPage._cuteAt(address)

  def currentId(self) -> int:
    """
    Calls Qt's 'int QWizard::currentId() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwizard.html#currentId
    """
    #  int QWizard::currentId() const
    return self.uglySide.call('ritual_ZNK7QWizard9currentIdEv')

  def nextId(self) -> int:
    """
    Calls Qt's 'int QWizard::nextId() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwizard.html#nextId
    """
    #  int QWizard::nextId() const
    ritual = 'ritual_ZNK7QWizard6nextIdEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK7QWizard6nextIdEv'
    return self.uglySide.call(ritual)

  @overload(str)
  def field(self, name: str) -> QVariant:
    """
    Calls Qt's 'QVariant QWizard::field(const QString &name) const'.

    Qt's own words: https://doc.qt.io/qt-6/qwizard.html#field

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QWizard::field(const QString &name) const
    address = self.uglySide.call('ritual_ZNK7QWizard5fieldERK7QString', name)
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def wizardStyle(self) -> WizardStyle:
    """
    Calls Qt's 'WizardStyle QWizard::wizardStyle() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwizard.html#wizardStyle

    Returns
    -------

    WizardStyle
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'WizardStyle(number)'
      gives.
    """
    #  WizardStyle QWizard::wizardStyle() const
    return QWizard.WizardStyle(self.uglySide.call(
        'ritual_ZNK7QWizard11wizardStyleEv',
    ))

  @overload(WizardOption)
  def testOption(self, option: WizardOption) -> bool:
    """
    Calls Qt's 'bool QWizard::testOption(WizardOption option) const'.

    Qt's own words: https://doc.qt.io/qt-6/qwizard.html#testOption

    Parameters
    ----------

    option : WizardOption
      Passed on as its number.
    """
    #  bool QWizard::testOption(WizardOption option) const
    return self.uglySide.call(
        'ritual_ZNK7QWizard10testOptionENS_12WizardOptionE', option.value,
    )

  def options(self) -> WizardOptions:
    """
    Calls Qt's 'WizardOptions QWizard::options() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwizard.html#options

    Returns
    -------

    WizardOptions
      The value standing for the combination Qt gave back.
    """
    #  WizardOptions QWizard::options() const
    return QWizard.WizardOptions(self.uglySide.call(
        'ritual_ZNK7QWizard7optionsEv',
    ))

  @overload(WizardButton)
  def buttonText(self, which: WizardButton) -> str:
    """
    Calls Qt's 'QString QWizard::buttonText(WizardButton which) const'.

    Qt's own words: https://doc.qt.io/qt-6/qwizard.html#buttonText

    Parameters
    ----------

    which : WizardButton
      Passed on as its number.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWizard::buttonText(WizardButton which) const
    return self.uglySide.call(
        'ritual_ZNK7QWizard10buttonTextENS_12WizardButtonE', which.value,
    )

  @overload(WizardButton)
  def button(self, which: WizardButton) -> Optional[QAbstractButton]:
    """
    Calls Qt's 'QAbstractButton *QWizard::button(WizardButton which) const'.

    Qt's own words: https://doc.qt.io/qt-6/qwizard.html#button

    Parameters
    ----------

    which : WizardButton
      Passed on as its number.

    Returns
    -------

    Optional[QAbstractButton]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractButton *QWizard::button(WizardButton which) const
    address = self.uglySide.call(
        'ritual_ZNK7QWizard6buttonENS_12WizardButtonE', which.value,
    )
    from . import QAbstractButton
    return QAbstractButton._cuteAt(address)

  def titleFormat(self) -> Qt.TextFormat:
    """
    Calls Qt's 'Qt::TextFormat QWizard::titleFormat() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwizard.html#titleFormat

    Returns
    -------

    Qt.TextFormat
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.TextFormat(number)'
      gives.
    """
    #  Qt::TextFormat QWizard::titleFormat() const
    return Qt.TextFormat(self.uglySide.call(
        'ritual_ZNK7QWizard11titleFormatEv',
    ))

  def subTitleFormat(self) -> Qt.TextFormat:
    """
    Calls Qt's 'Qt::TextFormat QWizard::subTitleFormat() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwizard.html#subTitleFormat

    Returns
    -------

    Qt.TextFormat
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.TextFormat(number)'
      gives.
    """
    #  Qt::TextFormat QWizard::subTitleFormat() const
    return Qt.TextFormat(self.uglySide.call(
        'ritual_ZNK7QWizard14subTitleFormatEv',
    ))

  @overload(WizardPixmap)
  def pixmap(self, which: WizardPixmap) -> QPixmap:
    """
    Calls Qt's 'QPixmap QWizard::pixmap(WizardPixmap which) const'.

    Qt's own words: https://doc.qt.io/qt-6/qwizard.html#pixmap

    Parameters
    ----------

    which : WizardPixmap
      Passed on as its number.

    Returns
    -------

    QPixmap
      A new cute QPixmap around the copy Qt gave back. Python owns it.
    """
    #  QPixmap QWizard::pixmap(WizardPixmap which) const
    address = self.uglySide.call(
        'ritual_ZNK7QWizard6pixmapENS_12WizardPixmapE', which.value,
    )
    from ..QtGui import QPixmap
    return QPixmap._cuteOwning(address)

  def sideWidget(self) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget *QWizard::sideWidget() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwizard.html#sideWidget

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *QWizard::sideWidget() const
    address = self.uglySide.call('ritual_ZNK7QWizard10sideWidgetEv')
    return QWidget._cuteAt(address)

  def sizeHint(self) -> QSize:
    """
    Calls Qt's 'QSize QWizard::sizeHint() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwizard.html#sizeHint

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QWizard::sizeHint() const
    ritual = 'ritual_ZNK7QWizard8sizeHintEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK7QWizard8sizeHintEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int, QWizardPage)
  @overload(int, NoneType)
  def setPage(self, id: int, page: Optional[QWizardPage]) -> None:
    """
    Calls Qt's 'void QWizard::setPage(int id, QWizardPage *page)'.

    Qt's own words: https://doc.qt.io/qt-6/qwizard.html#setPage

    Parameters
    ----------

    id : int
      Passed on as it is.

    page : Optional[QWizardPage]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWizard::setPage(int id, QWizardPage *page)
    self.uglySide.call(
        'ritual_ZN7QWizard7setPageEiP11QWizardPage',
        id, self._addressOf(page),
    )

  @overload(int)
  def setStartId(self, id: int) -> None:
    """
    Calls Qt's 'void QWizard::setStartId(int id)'.

    Qt's own words: https://doc.qt.io/qt-6/qwizard.html#setStartId

    Parameters
    ----------

    id : int
      Passed on as it is.
    """
    #  void QWizard::setStartId(int id)
    self.uglySide.call('ritual_ZN7QWizard10setStartIdEi', id)

  @overload(str, QVariant)
  def setField(self, name: str, value: QVariant) -> None:
    """
    Calls Qt's 'void QWizard::setField(const QString &name, const QVariant
    &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qwizard.html#setField

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QWizard::setField(const QString &name, const QVariant &value)
    self.uglySide.call(
        'ritual_ZN7QWizard8setFieldERK7QStringRK8QVariant',
        name, self._valueOf(value),
    )

  @overload(WizardStyle)
  def setWizardStyle(self, style: WizardStyle) -> None:
    """
    Calls Qt's 'void QWizard::setWizardStyle(WizardStyle style)'.

    Qt's own words: https://doc.qt.io/qt-6/qwizard.html#setWizardStyle

    Parameters
    ----------

    style : WizardStyle
      Passed on as its number.
    """
    #  void QWizard::setWizardStyle(WizardStyle style)
    self.uglySide.call(
        'ritual_ZN7QWizard14setWizardStyleENS_11WizardStyleE', style.value,
    )

  @overload(WizardOption)
  @overload(WizardOption, bool)
  def setOption(self, option: WizardOption, on: bool = True) -> None:
    """
    Calls Qt's 'void QWizard::setOption(WizardOption option, bool on)'.

    Qt's own words: https://doc.qt.io/qt-6/qwizard.html#setOption

    Parameters
    ----------

    option : WizardOption
      Passed on as its number.

    on : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QWizard::setOption(WizardOption option, bool on)
    self.uglySide.call(
        'ritual_ZN7QWizard9setOptionENS_12WizardOptionEb', option.value, on,
    )

  @overload(WizardOptions)
  def setOptions(self, options: WizardOptions) -> None:
    """
    Calls Qt's 'void QWizard::setOptions(WizardOptions options)'.

    Qt's own words: https://doc.qt.io/qt-6/qwizard.html#setOptions

    Parameters
    ----------

    options : WizardOptions
      Passed on as its number.
    """
    #  void QWizard::setOptions(WizardOptions options)
    self.uglySide.call(
        'ritual_ZN7QWizard10setOptionsE6QFlagsINS_12WizardOptionEE',
        options.value,
    )

  @overload(WizardButton, str)
  def setButtonText(self, which: WizardButton, text: str) -> None:
    """
    Calls Qt's 'void QWizard::setButtonText(WizardButton which, const QString
    &text)'.

    Qt's own words: https://doc.qt.io/qt-6/qwizard.html#setButtonText

    Parameters
    ----------

    which : WizardButton
      Passed on as its number.

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QWizard::setButtonText(WizardButton which, const QString &text)
    self.uglySide.call(
        'ritual_ZN7QWizard13setButtonTextENS_12WizardButtonERK7QString',
        which.value, text,
    )

  @overload(WizardButton, QAbstractButton)
  @overload(WizardButton, NoneType)
  def setButton(
      self,
      which: WizardButton,
      button: Optional[QAbstractButton],
  ) -> None:
    """
    Calls Qt's 'void QWizard::setButton(WizardButton which, QAbstractButton
    *button)'.

    Qt's own words: https://doc.qt.io/qt-6/qwizard.html#setButton

    Parameters
    ----------

    which : WizardButton
      Passed on as its number.

    button : Optional[QAbstractButton]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWizard::setButton(WizardButton which, QAbstractButton *button)
    self.uglySide.call(
        'ritual_ZN7QWizard9setButtonENS_12WizardButtonEP15QAbstractButton',
        which.value, self._addressOf(button),
    )

  @overload(Qt.TextFormat)
  def setTitleFormat(self, format: Qt.TextFormat) -> None:
    """
    Calls Qt's 'void QWizard::setTitleFormat(Qt::TextFormat format)'.

    Qt's own words: https://doc.qt.io/qt-6/qwizard.html#setTitleFormat

    Parameters
    ----------

    format : Qt.TextFormat
      Passed on as its number.
    """
    #  void QWizard::setTitleFormat(Qt::TextFormat format)
    self.uglySide.call(
        'ritual_ZN7QWizard14setTitleFormatEN2Qt10TextFormatE', format.value,
    )

  @overload(Qt.TextFormat)
  def setSubTitleFormat(self, format: Qt.TextFormat) -> None:
    """
    Calls Qt's 'void QWizard::setSubTitleFormat(Qt::TextFormat format)'.

    Qt's own words: https://doc.qt.io/qt-6/qwizard.html#setSubTitleFormat

    Parameters
    ----------

    format : Qt.TextFormat
      Passed on as its number.
    """
    #  void QWizard::setSubTitleFormat(Qt::TextFormat format)
    self.uglySide.call(
        'ritual_ZN7QWizard17setSubTitleFormatEN2Qt10TextFormatE',
        format.value,
    )

  @overload(WizardPixmap, QPixmap)
  def setPixmap(self, which: WizardPixmap, pixmap: QPixmap) -> None:
    """
    Calls Qt's 'void QWizard::setPixmap(WizardPixmap which, const QPixmap
    &pixmap)'.

    Qt's own words: https://doc.qt.io/qt-6/qwizard.html#setPixmap

    Parameters
    ----------

    which : WizardPixmap
      Passed on as its number.

    pixmap : QPixmap
      Passed on as a value: Qt reads the C++ QPixmap, which stays Python's
      own.
    """
    #  void QWizard::setPixmap(WizardPixmap which, const QPixmap &pixmap)
    self.uglySide.call(
        'ritual_ZN7QWizard9setPixmapENS_12WizardPixmapERK7QPixmap',
        which.value, self._valueOf(pixmap),
    )

  @overload(QWidget)
  @overload(NoneType)
  def setSideWidget(self, widget: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void QWizard::setSideWidget(QWidget *widget)'.

    Qt's own words: https://doc.qt.io/qt-6/qwizard.html#setSideWidget

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWizard::setSideWidget(QWidget *widget)
    self.uglySide.call(
        'ritual_ZN7QWizard13setSideWidgetEP7QWidget',
        self._addressOf(widget),
    )

  @overload(str, str, str)
  @overload(str, str, NoneType)
  @overload(str, NoneType, str)
  @overload(str, NoneType, NoneType)
  @overload(NoneType, str, str)
  @overload(NoneType, str, NoneType)
  @overload(NoneType, NoneType, str)
  @overload(NoneType, NoneType, NoneType)
  def setDefaultProperty(
      self,
      className: Optional[str],
      property: Optional[str],
      changedSignal: Optional[str],
  ) -> None:
    """
    Calls Qt's 'void QWizard::setDefaultProperty(const char *className, const
    char *property, const char *changedSignal)'.

    Qt's own words: https://doc.qt.io/qt-6/qwizard.html#setDefaultProperty

    Parameters
    ----------

    className : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    property : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    changedSignal : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.
    """
    #  void QWizard::setDefaultProperty(const char *className, const char
    #      *property, const char *changedSignal)
    self.uglySide.call(
        'ritual_ZN7QWizard18setDefaultPropertyEPKcS1_S1_',
        self._bytesOf(className), self._bytesOf(property),
        self._bytesOf(changedSignal),
    )

  @overload(bool)
  def setVisible(self, visible: bool) -> None:
    """
    Calls Qt's 'void QWizard::setVisible(bool visible)'.

    Qt's own words: https://doc.qt.io/qt-6/qwizard.html#setVisible

    Parameters
    ----------

    visible : bool
      Passed on as it is.
    """
    #  void QWizard::setVisible(bool visible)
    ritual = 'ritual_ZN7QWizard10setVisibleEb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN7QWizard10setVisibleEb'
    self.uglySide.call(ritual, visible)

  @overload(int)
  def setCurrentId(self, id: int) -> None:
    """
    Calls Qt's 'void QWizard::setCurrentId(int id)'.

    Qt's own words: https://doc.qt.io/qt-6/qwizard.html#setCurrentId

    Parameters
    ----------

    id : int
      Passed on as it is.
    """
    #  void QWizard::setCurrentId(int id)
    self.uglySide.call('ritual_ZN7QWizard12setCurrentIdEi', id)

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
  @overload(QWidget, Qt.WindowFlags)
  @overload(NoneType, Qt.WindowFlags)
  def __init__(
      self,
      parent: Optional[QWidget] = None,
      flags: Qt.WindowFlags = Qt.WindowFlags(),
  ) -> None:
    """
    Notes what was given, for Qt's 'QWizard::QWizard(QWidget *parent,
    Qt::WindowFlags flags)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qwizard.html#QWizard

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    flags : Qt.WindowFlags
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.WindowFlags().
    """
    #  QWizard::QWizard(QWidget *parent, Qt::WindowFlags flags)
    self._noteCreation(QWizard, lambda: Rituals.call(
        'ritual_ZN7QWizardC1EP7QWidget6QFlagsIN2Qt10WindowTypeEE',
        self._addressOf(parent), flags.value,
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

  @overload(QWizardPage)
  @overload(NoneType)
  def addPage(self, page: Optional[QWizardPage]) -> int:
    """
    Calls Qt's 'int QWizard::addPage(QWizardPage *page)'.

    Qt's own words: https://doc.qt.io/qt-6/qwizard.html#addPage

    Parameters
    ----------

    page : Optional[QWizardPage]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  int QWizard::addPage(QWizardPage *page)
    return self.uglySide.call(
        'ritual_ZN7QWizard7addPageEP11QWizardPage', self._addressOf(page),
    )

  @overload(int)
  def removePage(self, id: int) -> None:
    """
    Calls Qt's 'void QWizard::removePage(int id)'.

    Qt's own words: https://doc.qt.io/qt-6/qwizard.html#removePage

    Parameters
    ----------

    id : int
      Passed on as it is.
    """
    #  void QWizard::removePage(int id)
    self.uglySide.call('ritual_ZN7QWizard10removePageEi', id)

  def validateCurrentPage(self) -> bool:
    """
    Calls Qt's 'bool QWizard::validateCurrentPage()'.

    Qt's own words: https://doc.qt.io/qt-6/qwizard.html#validateCurrentPage
    """
    #  bool QWizard::validateCurrentPage()
    ritual = 'ritual_ZN7QWizard19validateCurrentPageEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN7QWizard19validateCurrentPageEv'
    return self.uglySide.call(ritual)

  def back(self) -> None:
    """
    Calls Qt's 'void QWizard::back()'.

    Qt's own words: https://doc.qt.io/qt-6/qwizard.html#back
    """
    #  void QWizard::back()
    self.uglySide.call('ritual_ZN7QWizard4backEv')

  def next(self) -> None:
    """
    Calls Qt's 'void QWizard::next()'.

    Qt's own words: https://doc.qt.io/qt-6/qwizard.html#next
    """
    #  void QWizard::next()
    self.uglySide.call('ritual_ZN7QWizard4nextEv')

  def restart(self) -> None:
    """
    Calls Qt's 'void QWizard::restart()'.

    Qt's own words: https://doc.qt.io/qt-6/qwizard.html#restart
    """
    #  void QWizard::restart()
    self.uglySide.call('ritual_ZN7QWizard7restartEv')

  @overload(QEvent)
  @overload(NoneType)
  def event(self, event: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QWizard::event(QEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qwizard.html#event

    Parameters
    ----------

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QWizard::event(QEvent *event)
    ritual = 'ritual_ZN7QWizard5eventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN7QWizard5eventEP6QEvent'
    return self.uglySide.call(ritual, self._addressOf(event))

  @overload(QResizeEvent)
  @overload(NoneType)
  def resizeEvent(self, event: Optional[QResizeEvent]) -> None:
    """
    Calls Qt's 'void QWizard::resizeEvent(QResizeEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qwizard.html#resizeEvent

    Parameters
    ----------

    event : Optional[QResizeEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWizard::resizeEvent(QResizeEvent *event)
    ritual = 'ritual_ZN7QWizard11resizeEventEP12QResizeEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN7QWizard11resizeEventEP12QResizeEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QPaintEvent)
  @overload(NoneType)
  def paintEvent(self, event: Optional[QPaintEvent]) -> None:
    """
    Calls Qt's 'void QWizard::paintEvent(QPaintEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qwizard.html#paintEvent

    Parameters
    ----------

    event : Optional[QPaintEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWizard::paintEvent(QPaintEvent *event)
    ritual = 'ritual_ZN7QWizard10paintEventEP11QPaintEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN7QWizard10paintEventEP11QPaintEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(int)
  def done(self, result: int) -> None:
    """
    Calls Qt's 'void QWizard::done(int result)'.

    Qt's own words: https://doc.qt.io/qt-6/qwizard.html#done

    Parameters
    ----------

    result : int
      Passed on as it is.
    """
    #  void QWizard::done(int result)
    ritual = 'ritual_ZN7QWizard4doneEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN7QWizard4doneEi'
    self.uglySide.call(ritual, result)

  @overload(int)
  def initializePage(self, id: int) -> None:
    """
    Calls Qt's 'void QWizard::initializePage(int id)'.

    Qt's own words: https://doc.qt.io/qt-6/qwizard.html#initializePage

    Parameters
    ----------

    id : int
      Passed on as it is.
    """
    #  void QWizard::initializePage(int id)
    ritual = 'ritual_ZN7QWizard14initializePageEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN7QWizard14initializePageEi'
    self.uglySide.call(ritual, id)

  @overload(int)
  def cleanupPage(self, id: int) -> None:
    """
    Calls Qt's 'void QWizard::cleanupPage(int id)'.

    Qt's own words: https://doc.qt.io/qt-6/qwizard.html#cleanupPage

    Parameters
    ----------

    id : int
      Passed on as it is.
    """
    #  void QWizard::cleanupPage(int id)
    ritual = 'ritual_ZN7QWizard11cleanupPageEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN7QWizard11cleanupPageEi'
    self.uglySide.call(ritual, id)
