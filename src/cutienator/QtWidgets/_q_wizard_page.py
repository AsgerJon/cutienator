"""
QWizardPage binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qwizard.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QWidget, QWizard

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QPixmap
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPixmap = WAIT['QPixmap']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QWizardPage(QWidget):
  """
  The cute side of Qt's QWizardPage: a plain Python object standing in front
  of one C++ QWizardPage.

  It is built on the cute 'QWidget', as Qt's QWizardPage is built on Qt's
  QWidget, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QWizardPage that has a ritual and that Python can
  call so far, 19 names in all: 'metaObject', 'tr', 'setTitle', 'title',
  'setSubTitle', 'subTitle', 'setPixmap', 'pixmap', 'setFinalPage',
  'isFinalPage', 'setCommitPage', 'isCommitPage', 'setButtonText',
  'buttonText', 'initializePage', 'cleanupPage', 'validatePage',
  'isComplete', 'nextId'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QWizardPage::~QWizardPage()': the destructor: Python never removes
    a C++ QWizardPage.

  What has no ritual
  ------------------

  13 of the 34 functions Qt declares: 4 protected; 3 private; 2 takes or
  gives a type that cannot be passed yet; 2 forbidden; 1 a template; 1 a
  signal.

  What to expect
  --------------

  - The C++ QWizardPage is created at the first use, not by
    'QWizardPage(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QWizardPage.
  - Qt tells when it has removed the C++ QWizardPage. Every call on the cute
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
    Calls Qt's 'QString QWizardPage::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qwizardpage.html#tr

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
    #  QString QWizardPage::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN11QWizardPage2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWizardPage'

  #  A C++ QWizardPage Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QWizardPage'

  #  The functions Qt calls itself that QWizardPage is the first to declare.
  #  A class of a program built on it can write one anew, and Qt then calls
  #  that. For each name: the key C++ knows the function by, what it gives,
  #  and what it takes.
  __virtual_functions__ = {
      'initializePage': (
          ('_ZN11QWizardPage14initializePageEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'cleanupPage': (
          ('_ZN11QWizardPage11cleanupPageEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'validatePage': (
          ('_ZN11QWizardPage12validatePageEv',
           ('bool', 'number', ''),
           ()),
      ),
      'isComplete': (
          ('_ZNK11QWizardPage10isCompleteEv',
           ('bool', 'number', ''),
           ()),
      ),
      'nextId': (
          ('_ZNK11QWizardPage6nextIdEv',
           ('int', 'number', ''),
           ()),
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
    Calls Qt's 'const QMetaObject *QWizardPage::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwizardpage.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QWizardPage::metaObject() const
    address = self.uglySide.call('ritual_ZNK11QWizardPage10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def title(self) -> str:
    """
    Calls Qt's 'QString QWizardPage::title() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwizardpage.html#title

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWizardPage::title() const
    return self.uglySide.call('ritual_ZNK11QWizardPage5titleEv')

  def subTitle(self) -> str:
    """
    Calls Qt's 'QString QWizardPage::subTitle() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwizardpage.html#subTitle

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWizardPage::subTitle() const
    return self.uglySide.call('ritual_ZNK11QWizardPage8subTitleEv')

  @overload(QWizard.WizardPixmap)
  def pixmap(self, which: QWizard.WizardPixmap) -> QPixmap:
    """
    Calls Qt's 'QPixmap QWizardPage::pixmap(QWizard::WizardPixmap which)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qwizardpage.html#pixmap

    Parameters
    ----------

    which : QWizard.WizardPixmap
      Passed on as its number.

    Returns
    -------

    QPixmap
      A new cute QPixmap around the copy Qt gave back. Python owns it.
    """
    #  QPixmap QWizardPage::pixmap(QWizard::WizardPixmap which) const
    address = self.uglySide.call(
        'ritual_ZNK11QWizardPage6pixmapEN7QWizard12WizardPixmapE',
        which.value,
    )
    from ..QtGui import QPixmap
    return QPixmap._cuteOwning(address)

  def isFinalPage(self) -> bool:
    """
    Calls Qt's 'bool QWizardPage::isFinalPage() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwizardpage.html#isFinalPage
    """
    #  bool QWizardPage::isFinalPage() const
    return self.uglySide.call('ritual_ZNK11QWizardPage11isFinalPageEv')

  def isCommitPage(self) -> bool:
    """
    Calls Qt's 'bool QWizardPage::isCommitPage() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwizardpage.html#isCommitPage
    """
    #  bool QWizardPage::isCommitPage() const
    return self.uglySide.call('ritual_ZNK11QWizardPage12isCommitPageEv')

  @overload(QWizard.WizardButton)
  def buttonText(self, which: QWizard.WizardButton) -> str:
    """
    Calls Qt's 'QString QWizardPage::buttonText(QWizard::WizardButton which)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qwizardpage.html#buttonText

    Parameters
    ----------

    which : QWizard.WizardButton
      Passed on as its number.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWizardPage::buttonText(QWizard::WizardButton which) const
    return self.uglySide.call(
        'ritual_ZNK11QWizardPage10buttonTextEN7QWizard12WizardButtonE',
        which.value,
    )

  def isComplete(self) -> bool:
    """
    Calls Qt's 'bool QWizardPage::isComplete() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwizardpage.html#isComplete
    """
    #  bool QWizardPage::isComplete() const
    ritual = 'ritual_ZNK11QWizardPage10isCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QWizardPage10isCompleteEv'
    return self.uglySide.call(ritual)

  def nextId(self) -> int:
    """
    Calls Qt's 'int QWizardPage::nextId() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwizardpage.html#nextId
    """
    #  int QWizardPage::nextId() const
    ritual = 'ritual_ZNK11QWizardPage6nextIdEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QWizardPage6nextIdEv'
    return self.uglySide.call(ritual)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setTitle(self, title: str) -> None:
    """
    Calls Qt's 'void QWizardPage::setTitle(const QString &title)'.

    Qt's own words: https://doc.qt.io/qt-6/qwizardpage.html#setTitle

    Parameters
    ----------

    title : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QWizardPage::setTitle(const QString &title)
    self.uglySide.call('ritual_ZN11QWizardPage8setTitleERK7QString', title)

  @overload(str)
  def setSubTitle(self, subTitle: str) -> None:
    """
    Calls Qt's 'void QWizardPage::setSubTitle(const QString &subTitle)'.

    Qt's own words: https://doc.qt.io/qt-6/qwizardpage.html#setSubTitle

    Parameters
    ----------

    subTitle : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QWizardPage::setSubTitle(const QString &subTitle)
    self.uglySide.call(
        'ritual_ZN11QWizardPage11setSubTitleERK7QString', subTitle,
    )

  @overload(QWizard.WizardPixmap, QPixmap)
  def setPixmap(self, which: QWizard.WizardPixmap, pixmap: QPixmap) -> None:
    """
    Calls Qt's 'void QWizardPage::setPixmap(QWizard::WizardPixmap which,
    const QPixmap &pixmap)'.

    Qt's own words: https://doc.qt.io/qt-6/qwizardpage.html#setPixmap

    Parameters
    ----------

    which : QWizard.WizardPixmap
      Passed on as its number.

    pixmap : QPixmap
      Passed on as a value: Qt reads the C++ QPixmap, which stays Python's
      own.
    """
    #  void QWizardPage::setPixmap(QWizard::WizardPixmap which, const QPixmap
    #      &pixmap)
    self.uglySide.call(
        'ritual_ZN11QWizardPage9setPixmapEN7QWizard12WizardPixmapERK7QPixma'
        'p',
        which.value, self._valueOf(pixmap),
    )

  @overload(bool)
  def setFinalPage(self, finalPage: bool) -> None:
    """
    Calls Qt's 'void QWizardPage::setFinalPage(bool finalPage)'.

    Qt's own words: https://doc.qt.io/qt-6/qwizardpage.html#setFinalPage

    Parameters
    ----------

    finalPage : bool
      Passed on as it is.
    """
    #  void QWizardPage::setFinalPage(bool finalPage)
    self.uglySide.call('ritual_ZN11QWizardPage12setFinalPageEb', finalPage)

  @overload(bool)
  def setCommitPage(self, commitPage: bool) -> None:
    """
    Calls Qt's 'void QWizardPage::setCommitPage(bool commitPage)'.

    Qt's own words: https://doc.qt.io/qt-6/qwizardpage.html#setCommitPage

    Parameters
    ----------

    commitPage : bool
      Passed on as it is.
    """
    #  void QWizardPage::setCommitPage(bool commitPage)
    self.uglySide.call('ritual_ZN11QWizardPage13setCommitPageEb', commitPage)

  @overload(QWizard.WizardButton, str)
  def setButtonText(self, which: QWizard.WizardButton, text: str) -> None:
    """
    Calls Qt's 'void QWizardPage::setButtonText(QWizard::WizardButton which,
    const QString &text)'.

    Qt's own words: https://doc.qt.io/qt-6/qwizardpage.html#setButtonText

    Parameters
    ----------

    which : QWizard.WizardButton
      Passed on as its number.

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QWizardPage::setButtonText(QWizard::WizardButton which, const
    #      QString &text)
    self.uglySide.call(
        'ritual_ZN11QWizardPage13setButtonTextEN7QWizard12WizardButtonERK7Q'
        'String',
        which.value, text,
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
    Notes what was given, for Qt's 'QWizardPage::QWizardPage(QWidget
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qwizardpage.html#QWizardPage

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QWizardPage::QWizardPage(QWidget *parent)
    self._noteCreation(QWizardPage, lambda: Rituals.call(
        'ritual_ZN11QWizardPageC1EP7QWidget', self._addressOf(parent),
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

  def initializePage(self) -> None:
    """
    Calls Qt's 'void QWizardPage::initializePage()'.

    Qt's own words: https://doc.qt.io/qt-6/qwizardpage.html#initializePage
    """
    #  void QWizardPage::initializePage()
    ritual = 'ritual_ZN11QWizardPage14initializePageEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QWizardPage14initializePageEv'
    self.uglySide.call(ritual)

  def cleanupPage(self) -> None:
    """
    Calls Qt's 'void QWizardPage::cleanupPage()'.

    Qt's own words: https://doc.qt.io/qt-6/qwizardpage.html#cleanupPage
    """
    #  void QWizardPage::cleanupPage()
    ritual = 'ritual_ZN11QWizardPage11cleanupPageEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QWizardPage11cleanupPageEv'
    self.uglySide.call(ritual)

  def validatePage(self) -> bool:
    """
    Calls Qt's 'bool QWizardPage::validatePage()'.

    Qt's own words: https://doc.qt.io/qt-6/qwizardpage.html#validatePage
    """
    #  bool QWizardPage::validatePage()
    ritual = 'ritual_ZN11QWizardPage12validatePageEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QWizardPage12validatePageEv'
    return self.uglySide.call(ritual)
