"""
qdesigner_internal::TextPropertyEditor binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/textpropertyeditor_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means qdesigner_internal::TextPropertyEditor to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QObject
from ..QtWidgets import QWidget
from . import qdesigner_internal

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QSize
  from ..QtGui import QResizeEvent
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QResizeEvent = WAIT['QResizeEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class TextPropertyEditor(QWidget):
  """
  The cute side of Qt's qdesigner_internal::TextPropertyEditor: a plain
  Python object standing in front of one C++
  qdesigner_internal::TextPropertyEditor.

  It is built on the cute 'QWidget', as Qt's
  qdesigner_internal::TextPropertyEditor is built on Qt's QWidget, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's qdesigner_internal::TextPropertyEditor that has a
  ritual and that Python can call so far, 26 names in all: 'metaObject',
  'tr', 'textPropertyValidationMode', 'setTextPropertyValidationMode',
  'updateMode', 'setUpdateMode', 'text', 'sizeHint', 'minimumSizeHint',
  'setAlignment', 'hasAcceptableInput', 'installEventFilter',
  'stringToEditorString', 'editorStringToString', 'multiLine', 'textChanged',
  'editingFinished', 'setText', 'selectAll', 'clear', 'resizeEvent',
  'slotTextChanged', 'slotTextEdited', 'slotEditingFinished',
  'setRegularExpressionValidator', 'markIntermediateState'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *qdesigner_internal::TextPropertyEditor::qt_metacast(const
    char *a0)': one of Qt's own inner workings.
  - Qt's 'int
    qdesigner_internal::TextPropertyEditor::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'qdesigner_internal::TextPropertyEditor::~TextPropertyEditor()': the
    destructor: Python never removes a C++
    qdesigner_internal::TextPropertyEditor.

  What has no ritual
  ------------------

  2 of the 32 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ qdesigner_internal::TextPropertyEditor is created at the first
    use, not by 'qdesigner_internal::TextPropertyEditor(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ qdesigner_internal::TextPropertyEditor.
  - Qt tells when it has removed the C++
    qdesigner_internal::TextPropertyEditor. Every call on the cute object,
    and every use of it as an argument, then raises 'RuntimeError', and
    nothing reaches C++.
  """

  #  The enums Qt writes inside qdesigner_internal::TextPropertyEditor, each
  #  a class in here as in C++, and the names Qt has for the combinations of
  #  its flags enums.

  class EmbeddingMode(CuteNum):
    """
    The enum 'qdesigner_internal::TextPropertyEditor::EmbeddingMode' of Qt,
    with the 3 names Qt gives in it.
    """

    EmbeddingNone = Kee[int](0)
    EmbeddingTreeView = Kee[int](1)
    EmbeddingInPlace = Kee[int](2)

  class UpdateMode(CuteNum):
    """
    The enum 'qdesigner_internal::TextPropertyEditor::UpdateMode' of Qt, with
    the 2 names Qt gives in it.
    """

    UpdateAsYouType = Kee[int](0)
    UpdateOnFinished = Kee[int](1)

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
    Calls Qt's 'QString qdesigner_internal::TextPropertyEditor::tr(const char
    *s, const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-textpropertyeditor.html#tr

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
    #  QString qdesigner_internal::TextPropertyEditor::tr(const char *s,
    #      const char *c, int n)
    return Rituals.call(
        'ritual_ZN18qdesigner_internal18TextPropertyEditor2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(str)
  @overload(str, qdesigner_internal.TextPropertyValidationMode)
  def stringToEditorString(
      s: str,
      validationMode: qdesigner_internal.TextPropertyValidationMode = (
          qdesigner_internal.TextPropertyValidationMode.ValidationMultiLine),
  ) -> str:
    """
    Calls Qt's 'QString
    qdesigner_internal::TextPropertyEditor::stringToEditorString(const
    QString &s, TextPropertyValidationMode validationMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-textpropertyeditor.html

    Parameters
    ----------

    s : str
      Passed on as it is: a QString is made of it for the call.

    validationMode : qdesigner_internal.TextPropertyValidationMode
      Passed on as its number. May be left out, as in Qt: it is then
      qdesigner_internal.TextPropertyValidationMode.ValidationMultiLine.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString
    #      qdesigner_internal::TextPropertyEditor::stringToEditorString(const
    #      QString &s, TextPropertyValidationMode validationMode)
    return Rituals.call(
        'ritual_ZN18qdesigner_internal18TextPropertyEditor20stringToEditorS'
        'tringERK7QStringNS_26TextPropertyValidationModeE',
        s, validationMode.value,
    )

  @staticmethod
  @overload(str)
  @overload(str, qdesigner_internal.TextPropertyValidationMode)
  def editorStringToString(
      s: str,
      validationMode: qdesigner_internal.TextPropertyValidationMode = (
          qdesigner_internal.TextPropertyValidationMode.ValidationMultiLine),
  ) -> str:
    """
    Calls Qt's 'QString
    qdesigner_internal::TextPropertyEditor::editorStringToString(const
    QString &s, TextPropertyValidationMode validationMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-textpropertyeditor.html

    Parameters
    ----------

    s : str
      Passed on as it is: a QString is made of it for the call.

    validationMode : qdesigner_internal.TextPropertyValidationMode
      Passed on as its number. May be left out, as in Qt: it is then
      qdesigner_internal.TextPropertyValidationMode.ValidationMultiLine.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString
    #      qdesigner_internal::TextPropertyEditor::editorStringToString(const
    #      QString &s, TextPropertyValidationMode validationMode)
    return Rituals.call(
        'ritual_ZN18qdesigner_internal18TextPropertyEditor20editorStringToS'
        'tringERK7QStringNS_26TextPropertyValidationModeE',
        s, validationMode.value,
    )

  @staticmethod
  @overload(qdesigner_internal.TextPropertyValidationMode)
  def multiLine(
      validationMode: qdesigner_internal.TextPropertyValidationMode,
  ) -> bool:
    """
    Calls Qt's 'bool qdesigner_internal::TextPropertyEditor::multiLine(
    TextPropertyValidationMode validationMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-textpropertyeditor.html

    Parameters
    ----------

    validationMode : qdesigner_internal.TextPropertyValidationMode
      Passed on as its number.
    """
    #  bool qdesigner_internal::TextPropertyEditor::multiLine(
    #      TextPropertyValidationMode validationMode)
    return Rituals.call(
        'ritual_ZN18qdesigner_internal18TextPropertyEditor9multiLineENS_26T'
        'extPropertyValidationModeE',
        validationMode.value,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'qdesigner_internal::TextPropertyEditor'

  #  A C++ qdesigner_internal::TextPropertyEditor Python makes is of a C++
  #  class of ours, in which Python can take functions over. This ritual
  #  hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_qdesigner_internal_TextPropertyEditor'

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
    *qdesigner_internal::TextPropertyEditor::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-textpropertyeditor.html

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject
    #      *qdesigner_internal::TextPropertyEditor::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal18TextPropertyEditor10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def textPropertyValidationMode(
      self,
  ) -> qdesigner_internal.TextPropertyValidationMode:
    """
    Calls Qt's 'TextPropertyValidationMode
    qdesigner_internal::TextPropertyEditor::textPropertyValidationMode()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-textpropertyeditor.html

    Returns
    -------

    qdesigner_internal.TextPropertyValidationMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'qdesigner_internal.TextPropertyValidationMode(number)' gives.
    """
    #  TextPropertyValidationMode qdesigner_internal::TextPropertyEditor::
    #      textPropertyValidationMode() const
    return qdesigner_internal.TextPropertyValidationMode(self.uglySide.call(
        'ritual_ZNK18qdesigner_internal18TextPropertyEditor26textPropertyVa'
        'lidationModeEv',
    ))

  def updateMode(self) -> UpdateMode:
    """
    Calls Qt's 'UpdateMode
    qdesigner_internal::TextPropertyEditor::updateMode() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-textpropertyeditor.html

    Returns
    -------

    UpdateMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'UpdateMode(number)'
      gives.
    """
    #  UpdateMode qdesigner_internal::TextPropertyEditor::updateMode() const
    return TextPropertyEditor.UpdateMode(self.uglySide.call(
        'ritual_ZNK18qdesigner_internal18TextPropertyEditor10updateModeEv',
    ))

  def text(self) -> str:
    """
    Calls Qt's 'QString qdesigner_internal::TextPropertyEditor::text()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-textpropertyeditor.html#text

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString qdesigner_internal::TextPropertyEditor::text() const
    return self.uglySide.call(
        'ritual_ZNK18qdesigner_internal18TextPropertyEditor4textEv',
    )

  def sizeHint(self) -> QSize:
    """
    Calls Qt's 'QSize qdesigner_internal::TextPropertyEditor::sizeHint()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-textpropertyeditor.html

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize qdesigner_internal::TextPropertyEditor::sizeHint() const
    ritual = 'ritual_ZNK18qdesigner_internal18TextPropertyEditor8sizeHintEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK18qdesigner_internal18TextPropertyEditor8sizeHintE'
          'v')
    address = self.uglySide.call(ritual)
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def minimumSizeHint(self) -> QSize:
    """
    Calls Qt's 'QSize
    qdesigner_internal::TextPropertyEditor::minimumSizeHint() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-textpropertyeditor.html

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize qdesigner_internal::TextPropertyEditor::minimumSizeHint() const
    ritual = (
        'ritual_ZNK18qdesigner_internal18TextPropertyEditor15minimumSizeHin'
        'tEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK18qdesigner_internal18TextPropertyEditor15minimumS'
          'izeHintEv')
    address = self.uglySide.call(ritual)
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def hasAcceptableInput(self) -> bool:
    """
    Calls Qt's 'bool
    qdesigner_internal::TextPropertyEditor::hasAcceptableInput() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-textpropertyeditor.html
    """
    #  bool qdesigner_internal::TextPropertyEditor::hasAcceptableInput()
    #      const
    return self.uglySide.call(
        'ritual_ZNK18qdesigner_internal18TextPropertyEditor18hasAcceptableI'
        'nputEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(qdesigner_internal.TextPropertyValidationMode)
  def setTextPropertyValidationMode(
      self,
      vm: qdesigner_internal.TextPropertyValidationMode,
  ) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::TextPropertyEditor::setTextPropertyValidationMode(
    TextPropertyValidationMode vm)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-textpropertyeditor.html

    Parameters
    ----------

    vm : qdesigner_internal.TextPropertyValidationMode
      Passed on as its number.
    """
    #  void qdesigner_internal::TextPropertyEditor::
    #      setTextPropertyValidationMode(TextPropertyValidationMode vm)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal18TextPropertyEditor29setTextProperty'
        'ValidationModeENS_26TextPropertyValidationModeE',
        vm.value,
    )

  @overload(UpdateMode)
  def setUpdateMode(self, um: UpdateMode) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::TextPropertyEditor::setUpdateMode(UpdateMode um)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-textpropertyeditor.html

    Parameters
    ----------

    um : UpdateMode
      Passed on as its number.
    """
    #  void qdesigner_internal::TextPropertyEditor::setUpdateMode(UpdateMode
    #      um)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal18TextPropertyEditor13setUpdateModeEN'
        'S0_10UpdateModeE',
        um.value,
    )

  @overload(Qt.Alignment)
  def setAlignment(self, alignment: Qt.Alignment) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::TextPropertyEditor::setAlignment(Qt::Alignment
    alignment)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-textpropertyeditor.html

    Parameters
    ----------

    alignment : Qt.Alignment
      Passed on as its number.
    """
    #  void
    #      qdesigner_internal::TextPropertyEditor::setAlignment(Qt::Alignment
    #      alignment)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal18TextPropertyEditor12setAlignmentE6Q'
        'FlagsIN2Qt13AlignmentFlagEE',
        alignment.value,
    )

  @overload(str)
  def setText(self, text: str) -> None:
    """
    Calls Qt's 'void qdesigner_internal::TextPropertyEditor::setText(const
    QString &text)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-textpropertyeditor.html#setText

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void qdesigner_internal::TextPropertyEditor::setText(const QString
    #      &text)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal18TextPropertyEditor7setTextERK7QStri'
        'ng',
        text,
    )

  @overload(str)
  def setRegularExpressionValidator(self, pattern: str) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::TextPropertyEditor::setRegularExpressionValidator(
    const QString &pattern)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-textpropertyeditor.html

    Parameters
    ----------

    pattern : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void qdesigner_internal::TextPropertyEditor::
    #      setRegularExpressionValidator(const QString &pattern)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal18TextPropertyEditor29setRegularExpre'
        'ssionValidatorERK7QString',
        pattern,
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
  @overload(QWidget, EmbeddingMode)
  @overload(NoneType, EmbeddingMode)
  @overload(
      QWidget, EmbeddingMode, qdesigner_internal.TextPropertyValidationMode,
  )
  @overload(
      NoneType, EmbeddingMode, qdesigner_internal.TextPropertyValidationMode,
  )
  def __init__(
      self,
      parent: Optional[QWidget] = None,
      embeddingMode: EmbeddingMode = EmbeddingMode.EmbeddingNone,
      validationMode: qdesigner_internal.TextPropertyValidationMode = (
          qdesigner_internal.TextPropertyValidationMode.ValidationMultiLine),
  ) -> None:
    """
    Notes what was given, for Qt's
    'qdesigner_internal::TextPropertyEditor::TextPropertyEditor(QWidget
    *parent, EmbeddingMode embeddingMode, TextPropertyValidationMode
    validationMode)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-textpropertyeditor.html

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    embeddingMode : EmbeddingMode
      Passed on as its number. May be left out, as in Qt: it is then
      EmbeddingMode.EmbeddingNone.

    validationMode : qdesigner_internal.TextPropertyValidationMode
      Passed on as its number. May be left out, as in Qt: it is then
      qdesigner_internal.TextPropertyValidationMode.ValidationMultiLine.
    """
    #  qdesigner_internal::TextPropertyEditor::TextPropertyEditor(QWidget
    #      *parent, EmbeddingMode embeddingMode, TextPropertyValidationMode
    #      validationMode)
    self._noteCreation(TextPropertyEditor, lambda: Rituals.call(
        'ritual_ZN18qdesigner_internal18TextPropertyEditorC1EP7QWidgetNS0_1'
        '3EmbeddingModeENS_26TextPropertyValidationModeE',
        self._addressOf(parent), embeddingMode.value, validationMode.value,
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

  @overload(QObject)
  @overload(NoneType)
  def installEventFilter(self, filterObject: Optional[QObject]) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::TextPropertyEditor::installEventFilter(QObject
    *filterObject)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-textpropertyeditor.html

    Parameters
    ----------

    filterObject : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void
    #      qdesigner_internal::TextPropertyEditor::installEventFilter(QObject
    #      *filterObject)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal18TextPropertyEditor18installEventFil'
        'terEP7QObject',
        self._addressOf(filterObject, 'QObject'),
    )

  @overload(str)
  def textChanged(self, text: str) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::TextPropertyEditor::textChanged(const QString
    &text)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-textpropertyeditor.html

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void qdesigner_internal::TextPropertyEditor::textChanged(const QString
    #      &text)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal18TextPropertyEditor11textChangedERK7'
        'QString',
        text,
    )

  def editingFinished(self) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::TextPropertyEditor::editingFinished()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-textpropertyeditor.html
    """
    #  void qdesigner_internal::TextPropertyEditor::editingFinished()
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal18TextPropertyEditor15editingFinished'
        'Ev',
    )

  def selectAll(self) -> None:
    """
    Calls Qt's 'void qdesigner_internal::TextPropertyEditor::selectAll()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-textpropertyeditor.html
    """
    #  void qdesigner_internal::TextPropertyEditor::selectAll()
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal18TextPropertyEditor9selectAllEv',
    )

  def clear(self) -> None:
    """
    Calls Qt's 'void qdesigner_internal::TextPropertyEditor::clear()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-textpropertyeditor.html#clear
    """
    #  void qdesigner_internal::TextPropertyEditor::clear()
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal18TextPropertyEditor5clearEv',
    )

  @overload(QResizeEvent)
  @overload(NoneType)
  def resizeEvent(self, event: Optional[QResizeEvent]) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::TextPropertyEditor::resizeEvent(QResizeEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-textpropertyeditor.html

    Parameters
    ----------

    event : Optional[QResizeEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void qdesigner_internal::TextPropertyEditor::resizeEvent(QResizeEvent
    #      *event)
    ritual = (
        'ritual_ZN18qdesigner_internal18TextPropertyEditor11resizeEventEP12'
        'QResizeEvent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18qdesigner_internal18TextPropertyEditor11resizeEve'
          'ntEP12QResizeEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(str)
  def slotTextChanged(self, text: str) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::TextPropertyEditor::slotTextChanged(const QString
    &text)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-textpropertyeditor.html

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void qdesigner_internal::TextPropertyEditor::slotTextChanged(const
    #      QString &text)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal18TextPropertyEditor15slotTextChanged'
        'ERK7QString',
        text,
    )

  def slotTextEdited(self) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::TextPropertyEditor::slotTextEdited()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-textpropertyeditor.html
    """
    #  void qdesigner_internal::TextPropertyEditor::slotTextEdited()
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal18TextPropertyEditor14slotTextEditedE'
        'v',
    )

  def slotEditingFinished(self) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::TextPropertyEditor::slotEditingFinished()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-textpropertyeditor.html
    """
    #  void qdesigner_internal::TextPropertyEditor::slotEditingFinished()
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal18TextPropertyEditor19slotEditingFini'
        'shedEv',
    )

  def markIntermediateState(self) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::TextPropertyEditor::markIntermediateState()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-textpropertyeditor.html
    """
    #  void qdesigner_internal::TextPropertyEditor::markIntermediateState()
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal18TextPropertyEditor21markIntermediat'
        'eStateEv',
    )
