"""
QQuickLabsPlatformDialog binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLabsPlatform/6.12.0/QtLabsPlatform/private/qquicklabsplatformdialog_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickLabsPlatformDialog to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..QtCore import Qt

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QPlatformDialogHelper, QWindow
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPlatformDialogHelper = WAIT['QPlatformDialogHelper']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickLabsPlatformDialog(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuickLabsPlatformDialog: a plain Python object
  standing in front of one C++ QQuickLabsPlatformDialog.

  What exists
  -----------

  Every function of Qt's QQuickLabsPlatformDialog that has a ritual and that
  Python can call so far, 29 names in all: 'metaObject', 'handle',
  'parentWindow', 'title', 'flags', 'modality', 'isVisible', 'result',
  'open', 'close', 'accept', 'reject', 'done', 'accepted', 'rejected',
  'parentWindowChanged', 'titleChanged', 'flagsChanged', 'modalityChanged',
  'visibleChanged', 'resultChanged', 'classBegin', 'componentComplete',
  'destroy', 'useNativeDialog', 'onCreate', 'onShow', 'onHide',
  'findParentWindow'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickLabsPlatformDialog::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QQuickLabsPlatformDialog::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuickLabsPlatformDialog::qt_qmlMarker_uncreatable()': one of
    Qt's own inner workings.
  - Qt's 'QQuickLabsPlatformDialog::~QQuickLabsPlatformDialog()': the
    destructor: Python never removes a C++ QQuickLabsPlatformDialog.
  - Qt's 'QQmlListProperty<QObject> QQuickLabsPlatformDialog::data()': gives
    a type Python has no way to take yet.

  What has no ritual
  ------------------

  11 of the 45 functions Qt declares: 8 leans on 'QQuickLabsPlatformDialog; 2
  not a gap; 1 Qt's library has no name for it, and its code in Qt's source
  does not compile apart from its file.

  What to expect
  --------------

  - The C++ QQuickLabsPlatformDialog is created at the first use, not by
    'QQuickLabsPlatformDialog(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickLabsPlatformDialog.
  - Qt tells when it has removed the C++ QQuickLabsPlatformDialog. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickLabsPlatformDialog that has no cute function yet,
    '__init__', 'create', 'data', 'setFlags', 'setModality',
    'setParentWindow', 'setResult', 'setTitle', 'setVisible', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QQuickLabsPlatformDialog, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class StandardCode(CuteNum):
    """
    The enum 'QQuickLabsPlatformDialog::StandardCode' of Qt, with the 2 names
    Qt gives in it.
    """

    Rejected = Kee[int](0)
    Accepted = Kee[int](1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickLabsPlatformDialog'

  #  A C++ QQuickLabsPlatformDialog Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickLabsPlatformDialog'

  #  The functions Qt calls itself that QQuickLabsPlatformDialog is the first
  #  to declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'accept': (
          ('_ZN24QQuickLabsPlatformDialog6acceptEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'reject': (
          ('_ZN24QQuickLabsPlatformDialog6rejectEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'done': (
          ('_ZN24QQuickLabsPlatformDialog4doneEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'useNativeDialog': (
          ('_ZNK24QQuickLabsPlatformDialog15useNativeDialogEv',
           ('bool', 'number', ''),
           ()),
      ),
      'onCreate': (
          ('_ZN24QQuickLabsPlatformDialog8onCreateEP21QPlatformDialogHelper',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QPlatformDialogHelper'),
           )),
      ),
      'onShow': (
          ('_ZN24QQuickLabsPlatformDialog6onShowEP21QPlatformDialogHelper',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QPlatformDialogHelper'),
           )),
      ),
      'onHide': (
          ('_ZN24QQuickLabsPlatformDialog6onHideEP21QPlatformDialogHelper',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QPlatformDialogHelper'),
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
    Calls Qt's 'const QMetaObject *QQuickLabsPlatformDialog::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformdialog.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickLabsPlatformDialog::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK24QQuickLabsPlatformDialog10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def handle(self) -> Optional[QPlatformDialogHelper]:
    """
    Calls Qt's 'QPlatformDialogHelper *QQuickLabsPlatformDialog::handle()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformdialog.html#handle

    Returns
    -------

    Optional[QPlatformDialogHelper]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlatformDialogHelper *QQuickLabsPlatformDialog::handle() const
    address = self.uglySide.call(
        'ritual_ZNK24QQuickLabsPlatformDialog6handleEv',
    )
    from ..QtGui import QPlatformDialogHelper
    return QPlatformDialogHelper._cuteAt(address)

  def parentWindow(self) -> Optional[QWindow]:
    """
    Calls Qt's 'QWindow *QQuickLabsPlatformDialog::parentWindow() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformdialog.html#parentWindow

    Returns
    -------

    Optional[QWindow]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWindow *QQuickLabsPlatformDialog::parentWindow() const
    address = self.uglySide.call(
        'ritual_ZNK24QQuickLabsPlatformDialog12parentWindowEv',
    )
    from ..QtGui import QWindow
    return QWindow._cuteAt(address)

  def title(self) -> str:
    """
    Calls Qt's 'QString QQuickLabsPlatformDialog::title() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformdialog.html#title

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickLabsPlatformDialog::title() const
    return self.uglySide.call('ritual_ZNK24QQuickLabsPlatformDialog5titleEv')

  def flags(self) -> Qt.WindowFlags:
    """
    Calls Qt's 'Qt::WindowFlags QQuickLabsPlatformDialog::flags() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformdialog.html#flags

    Returns
    -------

    Qt.WindowFlags
      The value standing for the combination Qt gave back.
    """
    #  Qt::WindowFlags QQuickLabsPlatformDialog::flags() const
    return Qt.WindowFlags(self.uglySide.call(
        'ritual_ZNK24QQuickLabsPlatformDialog5flagsEv',
    ))

  def modality(self) -> Qt.WindowModality:
    """
    Calls Qt's 'Qt::WindowModality QQuickLabsPlatformDialog::modality()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformdialog.html#modality

    Returns
    -------

    Qt.WindowModality
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt.WindowModality(number)' gives.
    """
    #  Qt::WindowModality QQuickLabsPlatformDialog::modality() const
    return Qt.WindowModality(self.uglySide.call(
        'ritual_ZNK24QQuickLabsPlatformDialog8modalityEv',
    ))

  def isVisible(self) -> bool:
    """
    Calls Qt's 'bool QQuickLabsPlatformDialog::isVisible() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformdialog.html#isVisible
    """
    #  bool QQuickLabsPlatformDialog::isVisible() const
    return self.uglySide.call(
        'ritual_ZNK24QQuickLabsPlatformDialog9isVisibleEv',
    )

  def result(self) -> int:
    """
    Calls Qt's 'int QQuickLabsPlatformDialog::result() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformdialog.html#result
    """
    #  int QQuickLabsPlatformDialog::result() const
    return self.uglySide.call(
        'ritual_ZNK24QQuickLabsPlatformDialog6resultEv',
    )

  def useNativeDialog(self) -> bool:
    """
    Calls Qt's 'bool QQuickLabsPlatformDialog::useNativeDialog() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformdialog.html#useNativeDialog
    """
    #  bool QQuickLabsPlatformDialog::useNativeDialog() const
    ritual = 'ritual_ZNK24QQuickLabsPlatformDialog15useNativeDialogEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK24QQuickLabsPlatformDialog15useNativeDialogEv'
    return self.uglySide.call(ritual)

  def findParentWindow(self) -> Optional[QWindow]:
    """
    Calls Qt's 'QWindow *QQuickLabsPlatformDialog::findParentWindow() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformdialog.html#findParentWindow

    Returns
    -------

    Optional[QWindow]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWindow *QQuickLabsPlatformDialog::findParentWindow() const
    address = self.uglySide.call(
        'ritual_ZNK24QQuickLabsPlatformDialog16findParentWindowEv',
    )
    from ..QtGui import QWindow
    return QWindow._cuteAt(address)

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
    Qt's 'QQuickLabsPlatformDialog::QQuickLabsPlatformDialog(QPlatformTheme::
    DialogType type, QObject *parent)': leans on
    'QQuickLabsPlatformDialog::qt_metacall(QMetaObject::Call, int, void**)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickLabsPlatformDialog.__init__' has no cute function yet. Qt's "
        "'QQuickLabsPlatformDialog::QQuickLabsPlatformDialog(QPlatformTheme:"
        ":DialogType type, QObject *parent)': leans on "
        "'QQuickLabsPlatformDialog::qt_metacall(QMetaObject::Call, int, "
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

  def open(self) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformDialog::open()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicklabsplatformdialog.html#open
    """
    #  void QQuickLabsPlatformDialog::open()
    self.uglySide.call('ritual_ZN24QQuickLabsPlatformDialog4openEv')

  def close(self) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformDialog::close()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformdialog.html#close
    """
    #  void QQuickLabsPlatformDialog::close()
    self.uglySide.call('ritual_ZN24QQuickLabsPlatformDialog5closeEv')

  def accept(self) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformDialog::accept()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformdialog.html#accept
    """
    #  void QQuickLabsPlatformDialog::accept()
    ritual = 'ritual_ZN24QQuickLabsPlatformDialog6acceptEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN24QQuickLabsPlatformDialog6acceptEv'
    self.uglySide.call(ritual)

  def reject(self) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformDialog::reject()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformdialog.html#reject
    """
    #  void QQuickLabsPlatformDialog::reject()
    ritual = 'ritual_ZN24QQuickLabsPlatformDialog6rejectEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN24QQuickLabsPlatformDialog6rejectEv'
    self.uglySide.call(ritual)

  @overload(int)
  def done(self, result: int) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformDialog::done(int result)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicklabsplatformdialog.html#done

    Parameters
    ----------

    result : int
      Passed on as it is.
    """
    #  void QQuickLabsPlatformDialog::done(int result)
    self.uglySide.call('ritual_ZN24QQuickLabsPlatformDialog4doneEi', result)

  def accepted(self) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformDialog::accepted()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformdialog.html#accepted
    """
    #  void QQuickLabsPlatformDialog::accepted()
    self.uglySide.call('ritual_ZN24QQuickLabsPlatformDialog8acceptedEv')

  def rejected(self) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformDialog::rejected()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformdialog.html#rejected
    """
    #  void QQuickLabsPlatformDialog::rejected()
    self.uglySide.call('ritual_ZN24QQuickLabsPlatformDialog8rejectedEv')

  def parentWindowChanged(self) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformDialog::parentWindowChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformdialog.html#parentWindowChanged
    """
    #  void QQuickLabsPlatformDialog::parentWindowChanged()
    self.uglySide.call(
        'ritual_ZN24QQuickLabsPlatformDialog19parentWindowChangedEv',
    )

  def titleChanged(self) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformDialog::titleChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformdialog.html#titleChanged
    """
    #  void QQuickLabsPlatformDialog::titleChanged()
    self.uglySide.call('ritual_ZN24QQuickLabsPlatformDialog12titleChangedEv')

  def flagsChanged(self) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformDialog::flagsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformdialog.html#flagsChanged
    """
    #  void QQuickLabsPlatformDialog::flagsChanged()
    self.uglySide.call('ritual_ZN24QQuickLabsPlatformDialog12flagsChangedEv')

  def modalityChanged(self) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformDialog::modalityChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformdialog.html#modalityChanged
    """
    #  void QQuickLabsPlatformDialog::modalityChanged()
    self.uglySide.call(
        'ritual_ZN24QQuickLabsPlatformDialog15modalityChangedEv',
    )

  def visibleChanged(self) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformDialog::visibleChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformdialog.html#visibleChanged
    """
    #  void QQuickLabsPlatformDialog::visibleChanged()
    self.uglySide.call(
        'ritual_ZN24QQuickLabsPlatformDialog14visibleChangedEv',
    )

  def resultChanged(self) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformDialog::resultChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformdialog.html#resultChanged
    """
    #  void QQuickLabsPlatformDialog::resultChanged()
    self.uglySide.call(
        'ritual_ZN24QQuickLabsPlatformDialog13resultChangedEv',
    )

  def classBegin(self) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformDialog::classBegin()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformdialog.html#classBegin
    """
    #  void QQuickLabsPlatformDialog::classBegin()
    ritual = 'ritual_ZN24QQuickLabsPlatformDialog10classBeginEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN24QQuickLabsPlatformDialog10classBeginEv'
    self.uglySide.call(ritual)

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformDialog::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformdialog.html#componentComplete
    """
    #  void QQuickLabsPlatformDialog::componentComplete()
    self.uglySide.call(
        'ritual_ZN24QQuickLabsPlatformDialog17componentCompleteEv',
    )

  def destroy(self) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformDialog::destroy()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformdialog.html#destroy
    """
    #  void QQuickLabsPlatformDialog::destroy()
    self.uglySide.call('ritual_ZN24QQuickLabsPlatformDialog7destroyEv')

  @overload(QPlatformDialogHelper)
  @overload(NoneType)
  def onCreate(self, dialog: Optional[QPlatformDialogHelper]) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformDialog::onCreate(QPlatformDialogHelper
    *dialog)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformdialog.html#onCreate

    Parameters
    ----------

    dialog : Optional[QPlatformDialogHelper]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickLabsPlatformDialog::onCreate(QPlatformDialogHelper *dialog)
    ritual = (
        'ritual_ZN24QQuickLabsPlatformDialog8onCreateEP21QPlatformDialogHel'
        'per')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN24QQuickLabsPlatformDialog8onCreateEP21QPlatformDia'
          'logHelper')
    self.uglySide.call(ritual, self._addressOf(dialog))

  @overload(QPlatformDialogHelper)
  @overload(NoneType)
  def onShow(self, dialog: Optional[QPlatformDialogHelper]) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformDialog::onShow(QPlatformDialogHelper
    *dialog)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformdialog.html#onShow

    Parameters
    ----------

    dialog : Optional[QPlatformDialogHelper]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickLabsPlatformDialog::onShow(QPlatformDialogHelper *dialog)
    ritual = (
        'ritual_ZN24QQuickLabsPlatformDialog6onShowEP21QPlatformDialogHelpe'
        'r')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN24QQuickLabsPlatformDialog6onShowEP21QPlatformDialo'
          'gHelper')
    self.uglySide.call(ritual, self._addressOf(dialog))

  @overload(QPlatformDialogHelper)
  @overload(NoneType)
  def onHide(self, dialog: Optional[QPlatformDialogHelper]) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformDialog::onHide(QPlatformDialogHelper
    *dialog)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformdialog.html#onHide

    Parameters
    ----------

    dialog : Optional[QPlatformDialogHelper]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickLabsPlatformDialog::onHide(QPlatformDialogHelper *dialog)
    ritual = (
        'ritual_ZN24QQuickLabsPlatformDialog6onHideEP21QPlatformDialogHelpe'
        'r')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN24QQuickLabsPlatformDialog6onHideEP21QPlatformDialo'
          'gHelper')
    self.uglySide.call(ritual, self._addressOf(dialog))

  @staticmethod
  def create(*__, **_) -> Never:
    """
    Qt's 'bool QQuickLabsPlatformDialog::create()': Qt's library has no name
    for it, and its code in Qt's source does not compile apart from its file:
    use of undeclared identifier 'QWidgetPlatform'.
    """
    raise NotImplementedError(
        "'QQuickLabsPlatformDialog.create' has no cute function yet. Qt's "
        "'bool QQuickLabsPlatformDialog::create()': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: use of undeclared identifier 'QWidgetPlatform'.")

  @staticmethod
  def data(*__, **_) -> Never:
    """
    Qt's 'QQmlListProperty<QObject> QQuickLabsPlatformDialog::data()': gives
    a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQuickLabsPlatformDialog.data' has no cute function yet. Qt's "
        "'QQmlListProperty<QObject> QQuickLabsPlatformDialog::data()': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def setFlags(*__, **_) -> Never:
    """
    Qt's 'void QQuickLabsPlatformDialog::setFlags(Qt::WindowFlags flags)':
    leans on 'QQuickLabsPlatformDialog::flagsChanged()', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QQuickLabsPlatformDialog.setFlags' has no cute function yet. Qt's "
        "'void QQuickLabsPlatformDialog::setFlags(Qt::WindowFlags flags)': "
        "leans on 'QQuickLabsPlatformDialog::flagsChanged()', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def setModality(*__, **_) -> Never:
    """
    Qt's 'void QQuickLabsPlatformDialog::setModality(Qt::WindowModality
    modality)': leans on 'QQuickLabsPlatformDialog::modalityChanged()', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QQuickLabsPlatformDialog.setModality' has no cute function yet. "
        "Qt's 'void "
        "QQuickLabsPlatformDialog::setModality(Qt::WindowModality "
        "modality)': leans on "
        "'QQuickLabsPlatformDialog::modalityChanged()', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def setParentWindow(*__, **_) -> Never:
    """
    Qt's 'void QQuickLabsPlatformDialog::setParentWindow(QWindow *window)':
    leans on 'QQuickLabsPlatformDialog::parentWindowChanged()', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QQuickLabsPlatformDialog.setParentWindow' has no cute function "
        "yet. Qt's 'void QQuickLabsPlatformDialog::setParentWindow(QWindow "
        "*window)': leans on "
        "'QQuickLabsPlatformDialog::parentWindowChanged()', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def setResult(*__, **_) -> Never:
    """
    Qt's 'void QQuickLabsPlatformDialog::setResult(int result)': leans on
    'QQuickLabsPlatformDialog::resultChanged()', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickLabsPlatformDialog.setResult' has no cute function yet. "
        "Qt's 'void QQuickLabsPlatformDialog::setResult(int result)': leans "
        "on 'QQuickLabsPlatformDialog::resultChanged()', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def setTitle(*__, **_) -> Never:
    """
    Qt's 'void QQuickLabsPlatformDialog::setTitle(const QString &title)':
    leans on 'QQuickLabsPlatformDialog::titleChanged()', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QQuickLabsPlatformDialog.setTitle' has no cute function yet. Qt's "
        "'void QQuickLabsPlatformDialog::setTitle(const QString &title)': "
        "leans on 'QQuickLabsPlatformDialog::titleChanged()', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def setVisible(*__, **_) -> Never:
    """
    Qt's 'void QQuickLabsPlatformDialog::setVisible(bool visible)': leans on
    'QQuickLabsPlatformDialog::visibleChanged()', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickLabsPlatformDialog.setVisible' has no cute function yet. "
        "Qt's 'void QQuickLabsPlatformDialog::setVisible(bool visible)': "
        "leans on 'QQuickLabsPlatformDialog::visibleChanged()', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")
