"""
qdesigner_internal::SignalSlotDialog binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/signalslotdialog_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means qdesigner_internal::SignalSlotDialog to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QObject, QStringList
from ..QtWidgets import QDialog, QWidget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from . import QDesignerDialogGuiInterface, QDesignerFormEditorInterface
  from . import QDesignerFormWindowInterface
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDesignerDialogGuiInterface = WAIT['QDesignerDialogGuiInterface']
  QDesignerFormEditorInterface = WAIT['QDesignerFormEditorInterface']
  QDesignerFormWindowInterface = WAIT['QDesignerFormWindowInterface']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class SignalSlotDialog(QDialog):
  """
  The cute side of Qt's qdesigner_internal::SignalSlotDialog: a plain Python
  object standing in front of one C++ qdesigner_internal::SignalSlotDialog.

  It is built on the cute 'QDialog', as Qt's
  qdesigner_internal::SignalSlotDialog is built on Qt's QDialog, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's qdesigner_internal::SignalSlotDialog that has a
  ritual and that Python can call so far, 5 names in all: 'metaObject', 'tr',
  'editMetaDataBase', 'editPromotedClass', 'fakeMethodsToMetaDataBase'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *qdesigner_internal::SignalSlotDialog::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int
    qdesigner_internal::SignalSlotDialog::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'qdesigner_internal::SignalSlotDialog::~SignalSlotDialog()': the
    destructor: Python never removes a C++
    qdesigner_internal::SignalSlotDialog.
  - Qt's 'DialogCode
    qdesigner_internal::SignalSlotDialog::showDialog(SignalSlotDialogData
    &slotData, SignalSlotDialogData &signalData)': takes a type Python has no
    way to hand over yet.
  - Qt's 'void
    qdesigner_internal::SignalSlotDialog::fakeMethodsFromMetaDataBase(
    QDesignerFormEditorInterface *core, QObject *o, QStringList &slotList,
    QStringList &signalList)': takes a type Python has no way to hand over
    yet.
  - Qt's 'void
    qdesigner_internal::SignalSlotDialog::existingMethodsFromMemberSheet(
    QDesignerFormEditorInterface *core, QObject *o, QStringList &slotList,
    QStringList &signalList)': takes a type Python has no way to hand over
    yet.
  - Qt's 'void qdesigner_internal::SignalSlotDialog::slotCheckSignature(const
    QString &signature, bool *ok)': takes a number to change where it is.

  What has no ritual
  ------------------

  2 of the 17 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ qdesigner_internal::SignalSlotDialog is created at the first use,
    not by 'qdesigner_internal::SignalSlotDialog(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ qdesigner_internal::SignalSlotDialog.
  - Qt tells when it has removed the C++
    qdesigner_internal::SignalSlotDialog. Every call on the cute object, and
    every use of it as an argument, then raises 'RuntimeError', and nothing
    reaches C++.
  - Each name of Qt's qdesigner_internal::SignalSlotDialog that has no cute
    function yet, 'existingMethodsFromMemberSheet',
    'fakeMethodsFromMetaDataBase', 'showDialog', 'slotCheckSignature', holds
    a function that raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside qdesigner_internal::SignalSlotDialog, each a
  #  class in here as in C++, and the names Qt has for the combinations of
  #  its flags enums.

  class FocusMode(CuteNum):
    """
    The enum 'qdesigner_internal::SignalSlotDialog::FocusMode' of Qt, with
    the 2 names Qt gives in it.
    """

    FocusSlots = Kee[int](0)
    FocusSignals = Kee[int](1)

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
    Calls Qt's 'QString qdesigner_internal::SignalSlotDialog::tr(const char
    *s, const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-signalslotdialog.html#tr

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
    #  QString qdesigner_internal::SignalSlotDialog::tr(const char *s, const
    #      char *c, int n)
    return Rituals.call(
        'ritual_ZN18qdesigner_internal16SignalSlotDialog2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(QDesignerFormWindowInterface, QObject)
  @overload(QDesignerFormWindowInterface, NoneType)
  @overload(NoneType, QObject)
  @overload(NoneType, NoneType)
  @overload(QDesignerFormWindowInterface, QObject, QWidget)
  @overload(QDesignerFormWindowInterface, QObject, NoneType)
  @overload(QDesignerFormWindowInterface, NoneType, QWidget)
  @overload(QDesignerFormWindowInterface, NoneType, NoneType)
  @overload(NoneType, QObject, QWidget)
  @overload(NoneType, QObject, NoneType)
  @overload(NoneType, NoneType, QWidget)
  @overload(NoneType, NoneType, NoneType)
  @overload(QDesignerFormWindowInterface, QObject, QWidget, FocusMode)
  @overload(QDesignerFormWindowInterface, QObject, NoneType, FocusMode)
  @overload(QDesignerFormWindowInterface, NoneType, QWidget, FocusMode)
  @overload(QDesignerFormWindowInterface, NoneType, NoneType, FocusMode)
  @overload(NoneType, QObject, QWidget, FocusMode)
  @overload(NoneType, QObject, NoneType, FocusMode)
  @overload(NoneType, NoneType, QWidget, FocusMode)
  @overload(NoneType, NoneType, NoneType, FocusMode)
  def editMetaDataBase(
      fw: Optional[QDesignerFormWindowInterface],
      object: Optional[QObject],
      parent: Optional[QWidget] = None,
      m: FocusMode = FocusMode.FocusSlots,
  ) -> bool:
    """
    Calls Qt's 'bool qdesigner_internal::SignalSlotDialog::editMetaDataBase(
    QDesignerFormWindowInterface *fw, QObject *object, QWidget *parent,
    FocusMode m)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-signalslotdialog.html

    Parameters
    ----------

    fw : Optional[QDesignerFormWindowInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    m : FocusMode
      Passed on as its number. May be left out, as in Qt: it is then
      FocusMode.FocusSlots.
    """
    #  bool qdesigner_internal::SignalSlotDialog::editMetaDataBase(
    #      QDesignerFormWindowInterface *fw, QObject *object, QWidget
    #      *parent, FocusMode m)
    return Rituals.call(
        'ritual_ZN18qdesigner_internal16SignalSlotDialog16editMetaDataBaseE'
        'P28QDesignerFormWindowInterfaceP7QObjectP7QWidgetNS0_9FocusModeE',
        CuteMixin._addressOf(fw), CuteMixin._addressOf(object, 'QObject'),
        CuteMixin._addressOf(parent), m.value,
    )

  @staticmethod
  @overload(QDesignerFormEditorInterface, str)
  @overload(NoneType, str)
  @overload(QDesignerFormEditorInterface, str, QWidget)
  @overload(QDesignerFormEditorInterface, str, NoneType)
  @overload(NoneType, str, QWidget)
  @overload(NoneType, str, NoneType)
  @overload(QDesignerFormEditorInterface, str, QWidget, FocusMode)
  @overload(QDesignerFormEditorInterface, str, NoneType, FocusMode)
  @overload(NoneType, str, QWidget, FocusMode)
  @overload(NoneType, str, NoneType, FocusMode)
  def editPromotedClass(
      core: Optional[QDesignerFormEditorInterface],
      promotedClassName: str,
      parent: Optional[QWidget] = None,
      m: FocusMode = FocusMode.FocusSlots,
  ) -> bool:
    """
    Calls Qt's 'bool qdesigner_internal::SignalSlotDialog::editPromotedClass(
    QDesignerFormEditorInterface *core, const QString &promotedClassName,
    QWidget *parent, FocusMode m)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-signalslotdialog.html

    Parameters
    ----------

    core : Optional[QDesignerFormEditorInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    promotedClassName : str
      Passed on as it is: a QString is made of it for the call.

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    m : FocusMode
      Passed on as its number. May be left out, as in Qt: it is then
      FocusMode.FocusSlots.
    """
    #  bool qdesigner_internal::SignalSlotDialog::editPromotedClass(
    #      QDesignerFormEditorInterface *core, const QString
    #      &promotedClassName, QWidget *parent, FocusMode m)
    return Rituals.call(
        'ritual_ZN18qdesigner_internal16SignalSlotDialog17editPromotedClass'
        'EP28QDesignerFormEditorInterfaceRK7QStringP7QWidgetNS0_9FocusModeE',
        CuteMixin._addressOf(core), promotedClassName,
        CuteMixin._addressOf(parent), m.value,
    )

  @staticmethod
  @overload(QDesignerFormEditorInterface, QObject)
  @overload(QDesignerFormEditorInterface, NoneType)
  @overload(NoneType, QObject)
  @overload(NoneType, NoneType)
  @overload(QDesignerFormEditorInterface, QObject, QWidget)
  @overload(QDesignerFormEditorInterface, QObject, NoneType)
  @overload(QDesignerFormEditorInterface, NoneType, QWidget)
  @overload(QDesignerFormEditorInterface, NoneType, NoneType)
  @overload(NoneType, QObject, QWidget)
  @overload(NoneType, QObject, NoneType)
  @overload(NoneType, NoneType, QWidget)
  @overload(NoneType, NoneType, NoneType)
  @overload(QDesignerFormEditorInterface, QObject, QWidget, FocusMode)
  @overload(QDesignerFormEditorInterface, QObject, NoneType, FocusMode)
  @overload(QDesignerFormEditorInterface, NoneType, QWidget, FocusMode)
  @overload(QDesignerFormEditorInterface, NoneType, NoneType, FocusMode)
  @overload(NoneType, QObject, QWidget, FocusMode)
  @overload(NoneType, QObject, NoneType, FocusMode)
  @overload(NoneType, NoneType, QWidget, FocusMode)
  @overload(NoneType, NoneType, NoneType, FocusMode)
  def editPromotedClass(
      core: Optional[QDesignerFormEditorInterface],
      baseObject: Optional[QObject],
      parent: Optional[QWidget] = None,
      m: FocusMode = FocusMode.FocusSlots,
  ) -> bool:
    """
    Calls Qt's 'bool qdesigner_internal::SignalSlotDialog::editPromotedClass(
    QDesignerFormEditorInterface *core, QObject *baseObject, QWidget *parent,
    FocusMode m)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-signalslotdialog.html

    Parameters
    ----------

    core : Optional[QDesignerFormEditorInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    baseObject : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    m : FocusMode
      Passed on as its number. May be left out, as in Qt: it is then
      FocusMode.FocusSlots.
    """
    #  bool qdesigner_internal::SignalSlotDialog::editPromotedClass(
    #      QDesignerFormEditorInterface *core, QObject *baseObject, QWidget
    #      *parent, FocusMode m)
    return Rituals.call(
        'ritual_ZN18qdesigner_internal16SignalSlotDialog17editPromotedClass'
        'EP28QDesignerFormEditorInterfaceP7QObjectP7QWidgetNS0_9FocusModeE',
        CuteMixin._addressOf(core), CuteMixin._addressOf(baseObject,
        'QObject'), CuteMixin._addressOf(parent), m.value,
    )

  @staticmethod
  @overload(QDesignerFormEditorInterface, str, QObject, QWidget, FocusMode)
  @overload(QDesignerFormEditorInterface, str, QObject, NoneType, FocusMode)
  @overload(QDesignerFormEditorInterface, str, NoneType, QWidget, FocusMode)
  @overload(QDesignerFormEditorInterface, str, NoneType, NoneType, FocusMode)
  @overload(NoneType, str, QObject, QWidget, FocusMode)
  @overload(NoneType, str, QObject, NoneType, FocusMode)
  @overload(NoneType, str, NoneType, QWidget, FocusMode)
  @overload(NoneType, str, NoneType, NoneType, FocusMode)
  def editPromotedClass(
      core: Optional[QDesignerFormEditorInterface],
      promotedClassName: str,
      baseObject: Optional[QObject],
      parent: Optional[QWidget],
      m: FocusMode,
  ) -> bool:
    """
    Calls Qt's 'bool qdesigner_internal::SignalSlotDialog::editPromotedClass(
    QDesignerFormEditorInterface *core, const QString &promotedClassName,
    QObject *baseObject, QWidget *parent, FocusMode m)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-signalslotdialog.html

    Parameters
    ----------

    core : Optional[QDesignerFormEditorInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    promotedClassName : str
      Passed on as it is: a QString is made of it for the call.

    baseObject : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    m : FocusMode
      Passed on as its number.
    """
    #  bool qdesigner_internal::SignalSlotDialog::editPromotedClass(
    #      QDesignerFormEditorInterface *core, const QString
    #      &promotedClassName, QObject *baseObject, QWidget *parent,
    #      FocusMode m)
    return Rituals.call(
        'ritual_ZN18qdesigner_internal16SignalSlotDialog17editPromotedClass'
        'EP28QDesignerFormEditorInterfaceRK7QStringP7QObjectP7QWidgetNS0_9F'
        'ocusModeE',
        CuteMixin._addressOf(core), promotedClassName,
        CuteMixin._addressOf(baseObject, 'QObject'),
        CuteMixin._addressOf(parent), m.value,
    )

  @staticmethod
  @overload(QDesignerFormEditorInterface, QObject, QStringList, QStringList)
  @overload(QDesignerFormEditorInterface, NoneType, QStringList, QStringList)
  @overload(NoneType, QObject, QStringList, QStringList)
  @overload(NoneType, NoneType, QStringList, QStringList)
  def fakeMethodsToMetaDataBase(
      core: Optional[QDesignerFormEditorInterface],
      o: Optional[QObject],
      slotList: QStringList,
      signalList: QStringList,
  ) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::SignalSlotDialog::fakeMethodsToMetaDataBase(
    QDesignerFormEditorInterface *core, QObject *o, const QStringList
    &slotList, const QStringList &signalList)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-signalslotdialog.html

    Parameters
    ----------

    core : Optional[QDesignerFormEditorInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    o : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    slotList : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    signalList : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void qdesigner_internal::SignalSlotDialog::fakeMethodsToMetaDataBase(
    #      QDesignerFormEditorInterface *core, QObject *o, const QStringList
    #      &slotList, const QStringList &signalList)
    Rituals.call(
        'ritual_ZN18qdesigner_internal16SignalSlotDialog25fakeMethodsToMeta'
        'DataBaseEP28QDesignerFormEditorInterfaceP7QObjectRK5QListI7QString'
        'ES9_',
        CuteMixin._addressOf(core), CuteMixin._addressOf(o, 'QObject'),
        CuteMixin._valueOf(slotList), CuteMixin._valueOf(signalList),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'qdesigner_internal::SignalSlotDialog'

  #  A C++ qdesigner_internal::SignalSlotDialog Python makes is of a C++
  #  class of ours, in which Python can take functions over. This ritual
  #  hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_qdesigner_internal_SignalSlotDialog'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject
    *qdesigner_internal::SignalSlotDialog::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-signalslotdialog.html

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *qdesigner_internal::SignalSlotDialog::metaObject()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal16SignalSlotDialog10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

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

  @overload(QDesignerDialogGuiInterface)
  @overload(NoneType)
  @overload(QDesignerDialogGuiInterface, QWidget)
  @overload(QDesignerDialogGuiInterface, NoneType)
  @overload(NoneType, QWidget)
  @overload(NoneType, NoneType)
  @overload(QDesignerDialogGuiInterface, QWidget, FocusMode)
  @overload(QDesignerDialogGuiInterface, NoneType, FocusMode)
  @overload(NoneType, QWidget, FocusMode)
  @overload(NoneType, NoneType, FocusMode)
  def __init__(
      self,
      dialogGui: Optional[QDesignerDialogGuiInterface],
      parent: Optional[QWidget] = None,
      m: FocusMode = FocusMode.FocusSlots,
  ) -> None:
    """
    Notes what was given, for Qt's
    'qdesigner_internal::SignalSlotDialog::SignalSlotDialog(
    QDesignerDialogGuiInterface *dialogGui, QWidget *parent, FocusMode m)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-signalslotdialog.html

    Parameters
    ----------

    dialogGui : Optional[QDesignerDialogGuiInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    m : FocusMode
      Passed on as its number. May be left out, as in Qt: it is then
      FocusMode.FocusSlots.
    """
    #  qdesigner_internal::SignalSlotDialog::SignalSlotDialog(
    #      QDesignerDialogGuiInterface *dialogGui, QWidget *parent, FocusMode
    #      m)
    self._noteCreation(SignalSlotDialog, lambda: Rituals.call(
        'ritual_ZN18qdesigner_internal16SignalSlotDialogC1EP27QDesignerDial'
        'ogGuiInterfaceP7QWidgetNS0_9FocusModeE',
        self._addressOf(dialogGui), self._addressOf(parent), m.value,
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
  def existingMethodsFromMemberSheet(*__, **_) -> Never:
    """
    Qt's 'void
    qdesigner_internal::SignalSlotDialog::existingMethodsFromMemberSheet(
    QDesignerFormEditorInterface *core, QObject *o, QStringList &slotList,
    QStringList &signalList)': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'qdesigner_internal.SignalSlotDialog.existingMethodsFromMemberSheet"
        "' has no cute function yet. Qt's 'void "
        "qdesigner_internal::SignalSlotDialog::existingMethodsFromMemberShee"
        "t(QDesignerFormEditorInterface *core, QObject *o, QStringList "
        "&slotList, QStringList &signalList)': takes a type Python has no "
        "way to hand over yet.")

  @staticmethod
  def fakeMethodsFromMetaDataBase(*__, **_) -> Never:
    """
    Qt's 'void
    qdesigner_internal::SignalSlotDialog::fakeMethodsFromMetaDataBase(
    QDesignerFormEditorInterface *core, QObject *o, QStringList &slotList,
    QStringList &signalList)': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'qdesigner_internal.SignalSlotDialog.fakeMethodsFromMetaDataBase' "
        "has no cute function yet. Qt's 'void "
        "qdesigner_internal::SignalSlotDialog::fakeMethodsFromMetaDataBase(Q"
        "DesignerFormEditorInterface *core, QObject *o, QStringList "
        "&slotList, QStringList &signalList)': takes a type Python has no "
        "way to hand over yet.")

  @staticmethod
  def showDialog(*__, **_) -> Never:
    """
    Qt's 'DialogCode
    qdesigner_internal::SignalSlotDialog::showDialog(SignalSlotDialogData
    &slotData, SignalSlotDialogData &signalData)': takes a type Python has no
    way to hand over yet.
    """
    raise NotImplementedError(
        "'qdesigner_internal.SignalSlotDialog.showDialog' has no cute "
        "function yet. Qt's 'DialogCode "
        "qdesigner_internal::SignalSlotDialog::showDialog(SignalSlotDialogDa"
        "ta &slotData, SignalSlotDialogData &signalData)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def slotCheckSignature(*__, **_) -> Never:
    """
    Qt's 'void qdesigner_internal::SignalSlotDialog::slotCheckSignature(const
    QString &signature, bool *ok)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'qdesigner_internal.SignalSlotDialog.slotCheckSignature' has no "
        "cute function yet. Qt's 'void "
        "qdesigner_internal::SignalSlotDialog::slotCheckSignature(const "
        "QString &signature, bool *ok)': takes a number to change where it "
        "is.")
