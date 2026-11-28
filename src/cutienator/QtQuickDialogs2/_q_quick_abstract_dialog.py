"""
QQuickAbstractDialog binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickDialogs2/6.12.0/QtQuickDialogs2/private/qquickabstractdialog_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickAbstractDialog to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QObject
from ..QtQml import QQmlParserStatus
from ..QtQuickTemplates2 import QQuickPopup

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QPlatformDialogHelper, QWindow
  from ..QtQuick import QQuickItem
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPlatformDialogHelper = WAIT['QPlatformDialogHelper']
  QWindow = WAIT['QWindow']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickAbstractDialog(QObject, QQmlParserStatus):
  """
  The cute side of Qt's QQuickAbstractDialog: a plain Python object standing
  in front of one C++ QQuickAbstractDialog.

  It is built on the cute 'QObject', as Qt's QQuickAbstractDialog is built on
  Qt's QObject, and has everything that class has. It is built on the cute
  'QQmlParserStatus' as well, as Qt's QQuickAbstractDialog is built on Qt's
  QQmlParserStatus too, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickAbstractDialog that has a ritual and that
  Python can call so far, 44 names in all: 'metaObject', 'tr', 'handle',
  'parentWindow', 'setParentWindow', 'resetParentWindow', 'title',
  'setTitle', 'flags', 'setFlags', 'modality', 'setModality', 'isVisible',
  'setVisible', 'result', 'setResult', 'popupType', 'setPopupType',
  'resetPopupType', 'open', 'close', 'accept', 'reject', 'done', 'accepted',
  'rejected', 'parentWindowChanged', 'titleChanged', 'flagsChanged',
  'modalityChanged', 'visibleChanged', 'resultChanged', 'popupTypeChanged',
  'classBegin', 'componentComplete', 'destroy', 'useNativeDialog',
  'onCreate', 'onShow', 'onHide', 'dialogCode', 'findParentItem',
  'windowForOpen', 'deferredOpen'. None can be made from Python: one comes
  out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickAbstractDialog::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuickAbstractDialog::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuickAbstractDialog::qt_qmlMarker_anonymous()': one of Qt's
    own inner workings.
  - Qt's 'QQuickAbstractDialog::QQuickAbstractDialog(QQuickDialogType type,
    QObject *parent)': names the enum 'QQuickDialogType', whose class cannot
    be named here.
  - Qt's 'QQuickAbstractDialog::~QQuickAbstractDialog()': the destructor:
    Python never removes a C++ QQuickAbstractDialog.
  - Qt's 'QQmlListProperty<QObject> QQuickAbstractDialog::data()': gives a
    type Python has no way to take yet.
  - Qt's 'bool QQuickAbstractDialog::create(CreateOptions a0)': names the
    enum 'QQuickAbstractDialog::CreateOptions', whose class cannot be named
    here.

  What has no ritual
  ------------------

  2 of the 53 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickAbstractDialog is created at the first use, not by
    'QQuickAbstractDialog(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickAbstractDialog.
  - Qt tells when it has removed the C++ QQuickAbstractDialog. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickAbstractDialog that has no cute function yet,
    '__init__', 'create', 'data', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QQuickAbstractDialog, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class StandardCode(CuteNum):
    """
    The enum 'QQuickAbstractDialog::StandardCode' of Qt, with the 2 names Qt
    gives in it.
    """

    Rejected = Kee[int](0)
    Accepted = Kee[int](1)

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
    Calls Qt's 'QString QQuickAbstractDialog::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickabstractdialog.html#tr

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
    #  QString QQuickAbstractDialog::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN20QQuickAbstractDialog2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickAbstractDialog'

  #  Qt's QQuickAbstractDialog is built on more than one class. The part of a
  #  C++ QQuickAbstractDialog that belongs to a class after the first begins
  #  somewhere inside the object, and the ritual named for that class gives
  #  where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QQmlParserStatus':
          'ritual_cast_QQuickAbstractDialog_QQmlParserStatus',
  }

  #  A C++ QQuickAbstractDialog Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickAbstractDialog'

  #  The functions Qt calls itself that QQuickAbstractDialog is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'accept': (
          ('_ZN20QQuickAbstractDialog6acceptEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'reject': (
          ('_ZN20QQuickAbstractDialog6rejectEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'done': (
          ('_ZN20QQuickAbstractDialog4doneEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'useNativeDialog': (
          ('_ZNK20QQuickAbstractDialog15useNativeDialogEv',
           ('bool', 'number', ''),
           ()),
      ),
      'onCreate': (
          ('_ZN20QQuickAbstractDialog8onCreateEP21QPlatformDialogHelper',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QPlatformDialogHelper'),
           )),
      ),
      'onShow': (
          ('_ZN20QQuickAbstractDialog6onShowEP21QPlatformDialogHelper',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QPlatformDialogHelper'),
           )),
      ),
      'onHide': (
          ('_ZN20QQuickAbstractDialog6onHideEP21QPlatformDialogHelper',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QPlatformDialogHelper'),
           )),
      ),
      'dialogCode': (
          ('_ZNK20QQuickAbstractDialog10dialogCodeEv',
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
    Calls Qt's 'const QMetaObject *QQuickAbstractDialog::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractdialog.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickAbstractDialog::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK20QQuickAbstractDialog10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def handle(self) -> Optional[QPlatformDialogHelper]:
    """
    Calls Qt's 'QPlatformDialogHelper *QQuickAbstractDialog::handle() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickabstractdialog.html#handle

    Returns
    -------

    Optional[QPlatformDialogHelper]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlatformDialogHelper *QQuickAbstractDialog::handle() const
    address = self.uglySide.call('ritual_ZNK20QQuickAbstractDialog6handleEv')
    from ..QtGui import QPlatformDialogHelper
    return QPlatformDialogHelper._cuteAt(address)

  def parentWindow(self) -> Optional[QWindow]:
    """
    Calls Qt's 'QWindow *QQuickAbstractDialog::parentWindow() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractdialog.html#parentWindow

    Returns
    -------

    Optional[QWindow]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWindow *QQuickAbstractDialog::parentWindow() const
    address = self.uglySide.call(
        'ritual_ZNK20QQuickAbstractDialog12parentWindowEv',
    )
    from ..QtGui import QWindow
    return QWindow._cuteAt(address)

  def title(self) -> str:
    """
    Calls Qt's 'QString QQuickAbstractDialog::title() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickabstractdialog.html#title

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickAbstractDialog::title() const
    return self.uglySide.call('ritual_ZNK20QQuickAbstractDialog5titleEv')

  def flags(self) -> Qt.WindowFlags:
    """
    Calls Qt's 'Qt::WindowFlags QQuickAbstractDialog::flags() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickabstractdialog.html#flags

    Returns
    -------

    Qt.WindowFlags
      The value standing for the combination Qt gave back.
    """
    #  Qt::WindowFlags QQuickAbstractDialog::flags() const
    return Qt.WindowFlags(self.uglySide.call(
        'ritual_ZNK20QQuickAbstractDialog5flagsEv',
    ))

  def modality(self) -> Qt.WindowModality:
    """
    Calls Qt's 'Qt::WindowModality QQuickAbstractDialog::modality() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickabstractdialog.html#modality

    Returns
    -------

    Qt.WindowModality
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt.WindowModality(number)' gives.
    """
    #  Qt::WindowModality QQuickAbstractDialog::modality() const
    return Qt.WindowModality(self.uglySide.call(
        'ritual_ZNK20QQuickAbstractDialog8modalityEv',
    ))

  def isVisible(self) -> bool:
    """
    Calls Qt's 'bool QQuickAbstractDialog::isVisible() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractdialog.html#isVisible
    """
    #  bool QQuickAbstractDialog::isVisible() const
    return self.uglySide.call('ritual_ZNK20QQuickAbstractDialog9isVisibleEv')

  def result(self) -> int:
    """
    Calls Qt's 'int QQuickAbstractDialog::result() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickabstractdialog.html#result
    """
    #  int QQuickAbstractDialog::result() const
    return self.uglySide.call('ritual_ZNK20QQuickAbstractDialog6resultEv')

  def popupType(self) -> QQuickPopup.PopupType:
    """
    Calls Qt's 'QQuickPopup::PopupType QQuickAbstractDialog::popupType()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractdialog.html#popupType

    Returns
    -------

    QQuickPopup.PopupType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QQuickPopup.PopupType(number)' gives.
    """
    #  QQuickPopup::PopupType QQuickAbstractDialog::popupType() const
    return QQuickPopup.PopupType(self.uglySide.call(
        'ritual_ZNK20QQuickAbstractDialog9popupTypeEv',
    ))

  def useNativeDialog(self) -> bool:
    """
    Calls Qt's 'bool QQuickAbstractDialog::useNativeDialog() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractdialog.html#useNativeDialog
    """
    #  bool QQuickAbstractDialog::useNativeDialog() const
    ritual = 'ritual_ZNK20QQuickAbstractDialog15useNativeDialogEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QQuickAbstractDialog15useNativeDialogEv'
    return self.uglySide.call(ritual)

  def dialogCode(self) -> int:
    """
    Calls Qt's 'int QQuickAbstractDialog::dialogCode() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractdialog.html#dialogCode
    """
    #  int QQuickAbstractDialog::dialogCode() const
    ritual = 'ritual_ZNK20QQuickAbstractDialog10dialogCodeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QQuickAbstractDialog10dialogCodeEv'
    return self.uglySide.call(ritual)

  def findParentItem(self) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickAbstractDialog::findParentItem() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractdialog.html#findParentItem

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickAbstractDialog::findParentItem() const
    address = self.uglySide.call(
        'ritual_ZNK20QQuickAbstractDialog14findParentItemEv',
    )
    from ..QtQuick import QQuickItem
    return QQuickItem._cuteAt(address)

  def windowForOpen(self) -> Optional[QWindow]:
    """
    Calls Qt's 'QWindow *QQuickAbstractDialog::windowForOpen() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractdialog.html#windowForOpen

    Returns
    -------

    Optional[QWindow]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWindow *QQuickAbstractDialog::windowForOpen() const
    address = self.uglySide.call(
        'ritual_ZNK20QQuickAbstractDialog13windowForOpenEv',
    )
    from ..QtGui import QWindow
    return QWindow._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QWindow)
  @overload(NoneType)
  def setParentWindow(self, window: Optional[QWindow]) -> None:
    """
    Calls Qt's 'void QQuickAbstractDialog::setParentWindow(QWindow *window)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractdialog.html#setParentWindow

    Parameters
    ----------

    window : Optional[QWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickAbstractDialog::setParentWindow(QWindow *window)
    self.uglySide.call(
        'ritual_ZN20QQuickAbstractDialog15setParentWindowEP7QWindow',
        self._addressOf(window),
    )

  @overload(str)
  def setTitle(self, title: str) -> None:
    """
    Calls Qt's 'void QQuickAbstractDialog::setTitle(const QString &title)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickabstractdialog.html#setTitle

    Parameters
    ----------

    title : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickAbstractDialog::setTitle(const QString &title)
    self.uglySide.call(
        'ritual_ZN20QQuickAbstractDialog8setTitleERK7QString', title,
    )

  @overload(Qt.WindowFlags)
  def setFlags(self, flags: Qt.WindowFlags) -> None:
    """
    Calls Qt's 'void QQuickAbstractDialog::setFlags(Qt::WindowFlags flags)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickabstractdialog.html#setFlags

    Parameters
    ----------

    flags : Qt.WindowFlags
      Passed on as its number.
    """
    #  void QQuickAbstractDialog::setFlags(Qt::WindowFlags flags)
    self.uglySide.call(
        'ritual_ZN20QQuickAbstractDialog8setFlagsE6QFlagsIN2Qt10WindowTypeE'
        'E',
        flags.value,
    )

  @overload(Qt.WindowModality)
  def setModality(self, modality: Qt.WindowModality) -> None:
    """
    Calls Qt's 'void QQuickAbstractDialog::setModality(Qt::WindowModality
    modality)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractdialog.html#setModality

    Parameters
    ----------

    modality : Qt.WindowModality
      Passed on as its number.
    """
    #  void QQuickAbstractDialog::setModality(Qt::WindowModality modality)
    self.uglySide.call(
        'ritual_ZN20QQuickAbstractDialog11setModalityEN2Qt14WindowModalityE',
        modality.value,
    )

  @overload(bool)
  def setVisible(self, visible: bool) -> None:
    """
    Calls Qt's 'void QQuickAbstractDialog::setVisible(bool visible)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractdialog.html#setVisible

    Parameters
    ----------

    visible : bool
      Passed on as it is.
    """
    #  void QQuickAbstractDialog::setVisible(bool visible)
    self.uglySide.call(
        'ritual_ZN20QQuickAbstractDialog10setVisibleEb', visible,
    )

  @overload(int)
  def setResult(self, result: int) -> None:
    """
    Calls Qt's 'void QQuickAbstractDialog::setResult(int result)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractdialog.html#setResult

    Parameters
    ----------

    result : int
      Passed on as it is.
    """
    #  void QQuickAbstractDialog::setResult(int result)
    self.uglySide.call('ritual_ZN20QQuickAbstractDialog9setResultEi', result)

  @overload(QQuickPopup.PopupType)
  def setPopupType(self, popupType: QQuickPopup.PopupType) -> None:
    """
    Calls Qt's 'void
    QQuickAbstractDialog::setPopupType(QQuickPopup::PopupType popupType)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractdialog.html#setPopupType

    Parameters
    ----------

    popupType : QQuickPopup.PopupType
      Passed on as its number.
    """
    #  void QQuickAbstractDialog::setPopupType(QQuickPopup::PopupType
    #      popupType)
    self.uglySide.call(
        'ritual_ZN20QQuickAbstractDialog12setPopupTypeEN11QQuickPopup9Popup'
        'TypeE',
        popupType.value,
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QQuickAbstractDialog::QQuickAbstractDialog(QQuickDialogType type,
    QObject *parent)': names the enum 'QQuickDialogType', whose class cannot
    be named here.
    """
    raise NotImplementedError(
        "'QQuickAbstractDialog.__init__' has no cute function yet. Qt's "
        "'QQuickAbstractDialog::QQuickAbstractDialog(QQuickDialogType type, "
        "QObject *parent)': names the enum 'QQuickDialogType', whose class "
        "cannot be named here.")

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

  def resetParentWindow(self) -> None:
    """
    Calls Qt's 'void QQuickAbstractDialog::resetParentWindow()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractdialog.html#resetParentWindow
    """
    #  void QQuickAbstractDialog::resetParentWindow()
    self.uglySide.call(
        'ritual_ZN20QQuickAbstractDialog17resetParentWindowEv',
    )

  def resetPopupType(self) -> None:
    """
    Calls Qt's 'void QQuickAbstractDialog::resetPopupType()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractdialog.html#resetPopupType
    """
    #  void QQuickAbstractDialog::resetPopupType()
    self.uglySide.call('ritual_ZN20QQuickAbstractDialog14resetPopupTypeEv')

  def open(self) -> None:
    """
    Calls Qt's 'void QQuickAbstractDialog::open()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickabstractdialog.html#open
    """
    #  void QQuickAbstractDialog::open()
    self.uglySide.call('ritual_ZN20QQuickAbstractDialog4openEv')

  def close(self) -> None:
    """
    Calls Qt's 'void QQuickAbstractDialog::close()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickabstractdialog.html#close
    """
    #  void QQuickAbstractDialog::close()
    self.uglySide.call('ritual_ZN20QQuickAbstractDialog5closeEv')

  def accept(self) -> None:
    """
    Calls Qt's 'void QQuickAbstractDialog::accept()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickabstractdialog.html#accept
    """
    #  void QQuickAbstractDialog::accept()
    ritual = 'ritual_ZN20QQuickAbstractDialog6acceptEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QQuickAbstractDialog6acceptEv'
    self.uglySide.call(ritual)

  def reject(self) -> None:
    """
    Calls Qt's 'void QQuickAbstractDialog::reject()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickabstractdialog.html#reject
    """
    #  void QQuickAbstractDialog::reject()
    ritual = 'ritual_ZN20QQuickAbstractDialog6rejectEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QQuickAbstractDialog6rejectEv'
    self.uglySide.call(ritual)

  @overload(int)
  def done(self, result: int) -> None:
    """
    Calls Qt's 'void QQuickAbstractDialog::done(int result)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickabstractdialog.html#done

    Parameters
    ----------

    result : int
      Passed on as it is.
    """
    #  void QQuickAbstractDialog::done(int result)
    ritual = 'ritual_ZN20QQuickAbstractDialog4doneEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QQuickAbstractDialog4doneEi'
    self.uglySide.call(ritual, result)

  def accepted(self) -> None:
    """
    Calls Qt's 'void QQuickAbstractDialog::accepted()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickabstractdialog.html#accepted
    """
    #  void QQuickAbstractDialog::accepted()
    self.uglySide.call('ritual_ZN20QQuickAbstractDialog8acceptedEv')

  def rejected(self) -> None:
    """
    Calls Qt's 'void QQuickAbstractDialog::rejected()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickabstractdialog.html#rejected
    """
    #  void QQuickAbstractDialog::rejected()
    self.uglySide.call('ritual_ZN20QQuickAbstractDialog8rejectedEv')

  def parentWindowChanged(self) -> None:
    """
    Calls Qt's 'void QQuickAbstractDialog::parentWindowChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractdialog.html#parentWindowChanged
    """
    #  void QQuickAbstractDialog::parentWindowChanged()
    self.uglySide.call(
        'ritual_ZN20QQuickAbstractDialog19parentWindowChangedEv',
    )

  def titleChanged(self) -> None:
    """
    Calls Qt's 'void QQuickAbstractDialog::titleChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractdialog.html#titleChanged
    """
    #  void QQuickAbstractDialog::titleChanged()
    self.uglySide.call('ritual_ZN20QQuickAbstractDialog12titleChangedEv')

  def flagsChanged(self) -> None:
    """
    Calls Qt's 'void QQuickAbstractDialog::flagsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractdialog.html#flagsChanged
    """
    #  void QQuickAbstractDialog::flagsChanged()
    self.uglySide.call('ritual_ZN20QQuickAbstractDialog12flagsChangedEv')

  def modalityChanged(self) -> None:
    """
    Calls Qt's 'void QQuickAbstractDialog::modalityChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractdialog.html#modalityChanged
    """
    #  void QQuickAbstractDialog::modalityChanged()
    self.uglySide.call('ritual_ZN20QQuickAbstractDialog15modalityChangedEv')

  def visibleChanged(self) -> None:
    """
    Calls Qt's 'void QQuickAbstractDialog::visibleChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractdialog.html#visibleChanged
    """
    #  void QQuickAbstractDialog::visibleChanged()
    self.uglySide.call('ritual_ZN20QQuickAbstractDialog14visibleChangedEv')

  def resultChanged(self) -> None:
    """
    Calls Qt's 'void QQuickAbstractDialog::resultChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractdialog.html#resultChanged
    """
    #  void QQuickAbstractDialog::resultChanged()
    self.uglySide.call('ritual_ZN20QQuickAbstractDialog13resultChangedEv')

  def popupTypeChanged(self) -> None:
    """
    Calls Qt's 'void QQuickAbstractDialog::popupTypeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractdialog.html#popupTypeChanged
    """
    #  void QQuickAbstractDialog::popupTypeChanged()
    self.uglySide.call('ritual_ZN20QQuickAbstractDialog16popupTypeChangedEv')

  def classBegin(self) -> None:
    """
    Calls Qt's 'void QQuickAbstractDialog::classBegin()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractdialog.html#classBegin
    """
    #  void QQuickAbstractDialog::classBegin()
    ritual = 'ritual_ZN20QQuickAbstractDialog10classBeginEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QQuickAbstractDialog10classBeginEv'
    self.uglySide.call(ritual)

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQuickAbstractDialog::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractdialog.html#componentComplete
    """
    #  void QQuickAbstractDialog::componentComplete()
    ritual = 'ritual_ZN20QQuickAbstractDialog17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QQuickAbstractDialog17componentCompleteEv'
    self.uglySide.call(ritual)

  def destroy(self) -> None:
    """
    Calls Qt's 'void QQuickAbstractDialog::destroy()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickabstractdialog.html#destroy
    """
    #  void QQuickAbstractDialog::destroy()
    self.uglySide.call('ritual_ZN20QQuickAbstractDialog7destroyEv')

  @overload(QPlatformDialogHelper)
  @overload(NoneType)
  def onCreate(self, dialog: Optional[QPlatformDialogHelper]) -> None:
    """
    Calls Qt's 'void QQuickAbstractDialog::onCreate(QPlatformDialogHelper
    *dialog)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickabstractdialog.html#onCreate

    Parameters
    ----------

    dialog : Optional[QPlatformDialogHelper]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickAbstractDialog::onCreate(QPlatformDialogHelper *dialog)
    ritual = (
        'ritual_ZN20QQuickAbstractDialog8onCreateEP21QPlatformDialogHelper')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QQuickAbstractDialog8onCreateEP21QPlatformDialogH'
          'elper')
    self.uglySide.call(ritual, self._addressOf(dialog))

  @overload(QPlatformDialogHelper)
  @overload(NoneType)
  def onShow(self, dialog: Optional[QPlatformDialogHelper]) -> None:
    """
    Calls Qt's 'void QQuickAbstractDialog::onShow(QPlatformDialogHelper
    *dialog)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickabstractdialog.html#onShow

    Parameters
    ----------

    dialog : Optional[QPlatformDialogHelper]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickAbstractDialog::onShow(QPlatformDialogHelper *dialog)
    ritual = (
        'ritual_ZN20QQuickAbstractDialog6onShowEP21QPlatformDialogHelper')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QQuickAbstractDialog6onShowEP21QPlatformDialogHel'
          'per')
    self.uglySide.call(ritual, self._addressOf(dialog))

  @overload(QPlatformDialogHelper)
  @overload(NoneType)
  def onHide(self, dialog: Optional[QPlatformDialogHelper]) -> None:
    """
    Calls Qt's 'void QQuickAbstractDialog::onHide(QPlatformDialogHelper
    *dialog)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickabstractdialog.html#onHide

    Parameters
    ----------

    dialog : Optional[QPlatformDialogHelper]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickAbstractDialog::onHide(QPlatformDialogHelper *dialog)
    ritual = (
        'ritual_ZN20QQuickAbstractDialog6onHideEP21QPlatformDialogHelper')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QQuickAbstractDialog6onHideEP21QPlatformDialogHel'
          'per')
    self.uglySide.call(ritual, self._addressOf(dialog))

  @overload(QWindow)
  @overload(NoneType)
  def deferredOpen(self, window: Optional[QWindow]) -> None:
    """
    Calls Qt's 'void QQuickAbstractDialog::deferredOpen(QWindow *window)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractdialog.html#deferredOpen

    Parameters
    ----------

    window : Optional[QWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickAbstractDialog::deferredOpen(QWindow *window)
    self.uglySide.call(
        'ritual_ZN20QQuickAbstractDialog12deferredOpenEP7QWindow',
        self._addressOf(window),
    )

  @staticmethod
  def create(*__, **_) -> Never:
    """
    Qt's 'bool QQuickAbstractDialog::create(CreateOptions a0)': names the
    enum 'QQuickAbstractDialog::CreateOptions', whose class cannot be named
    here.
    """
    raise NotImplementedError(
        "'QQuickAbstractDialog.create' has no cute function yet. Qt's 'bool "
        "QQuickAbstractDialog::create(CreateOptions a0)': names the enum "
        "'QQuickAbstractDialog::CreateOptions', whose class cannot be named "
        "here.")

  @staticmethod
  def data(*__, **_) -> Never:
    """
    Qt's 'QQmlListProperty<QObject> QQuickAbstractDialog::data()': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQuickAbstractDialog.data' has no cute function yet. Qt's "
        "'QQmlListProperty<QObject> QQuickAbstractDialog::data()': gives a "
        "type Python has no way to take yet.")
