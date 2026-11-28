"""
QVirtualKeyboardAbstractInputMethod binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtVirtualKeyboard/qvirtualkeyboardabstractinputmethod.h, Qt 6.12.0.
#  Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QMap, QObject
from . import QVirtualKeyboardInputEngine, QVirtualKeyboardSelectionListModel

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QVariant
  from . import QVirtualKeyboardAbstractInputMethodPrivate
  from . import QVirtualKeyboardInputContext, QVirtualKeyboardTrace
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QVariant = WAIT['QVariant']
  QVirtualKeyboardTrace = WAIT['QVirtualKeyboardTrace']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QVirtualKeyboardAbstractInputMethod(QObject):
  """
  The cute side of Qt's QVirtualKeyboardAbstractInputMethod: a plain Python
  object standing in front of one C++ QVirtualKeyboardAbstractInputMethod.

  It is built on the cute 'QObject', as Qt's
  QVirtualKeyboardAbstractInputMethod is built on Qt's QObject, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QVirtualKeyboardAbstractInputMethod that has a
  ritual and that Python can call so far, 22 names in all: 'metaObject',
  'tr', 'd_func', 'inputContext', 'inputEngine', 'setInputMode',
  'setTextCase', 'keyEvent', 'selectionListItemCount', 'selectionListData',
  'selectionListItemSelected', 'selectionListRemoveItem', 'traceBegin',
  'traceEnd', 'clickPreeditText', 'selectionListChanged',
  'selectionListActiveItemChanged', 'selectionListsChanged', 'reset',
  'update', 'clearInputMode', 'setInputEngine'. None can be made from Python:
  one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QVirtualKeyboardAbstractInputMethod::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int
    QVirtualKeyboardAbstractInputMethod::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'const QVirtualKeyboardAbstractInputMethodPrivate
    *QVirtualKeyboardAbstractInputMethod::d_func() const': takes in Python
    what 'QVirtualKeyboardAbstractInputMethodPrivate
    *QVirtualKeyboardAbstractInputMethod::d_func()' takes.
  - Qt's 'void
    QVirtualKeyboardAbstractInputMethod::qt_qmlMarker_anonymous()': one of
    Qt's own inner workings.
  - Qt's 'QVirtualKeyboardAbstractInputMethod::
    ~QVirtualKeyboardAbstractInputMethod()': the destructor: Python never
    removes a C++ QVirtualKeyboardAbstractInputMethod.
  - Qt's 'QList<QVirtualKeyboardInputEngine::InputMode>
    QVirtualKeyboardAbstractInputMethod::inputModes(const QString &locale)':
    gives a type Python has no way to take yet.
  - Qt's 'QList<QVirtualKeyboardSelectionListModel::Type>
    QVirtualKeyboardAbstractInputMethod::selectionLists()': gives a type
    Python has no way to take yet.
  - Qt's 'QList<QVirtualKeyboardInputEngine::PatternRecognitionMode>
    QVirtualKeyboardAbstractInputMethod::patternRecognitionModes() const':
    gives a type Python has no way to take yet.
  - Qt's 'bool QVirtualKeyboardAbstractInputMethod::reselect(int
    cursorPosition, const QVirtualKeyboardInputEngine::ReselectFlags
    &reselectFlags)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  4 of the 35 functions Qt declares: 2 not a gap; 2 the class is abstract, so
  C++ cannot make one, and the C++ class of ours does not fill in every
  function it leaves open.

  What to expect
  --------------

  - The C++ QVirtualKeyboardAbstractInputMethod is created at the first use,
    not by 'QVirtualKeyboardAbstractInputMethod(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QVirtualKeyboardAbstractInputMethod.
  - Qt tells when it has removed the C++ QVirtualKeyboardAbstractInputMethod.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QVirtualKeyboardAbstractInputMethod that has no cute
    function yet, '__init__', 'inputModes', 'patternRecognitionModes',
    'reselect', 'selectionLists', holds a function that raises
    'NotImplementedError', and its docstring says why.
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
    Calls Qt's 'QString QVirtualKeyboardAbstractInputMethod::tr(const char
    *s, const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardabstractinputmethod.html#tr

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
    #  QString QVirtualKeyboardAbstractInputMethod::tr(const char *s, const
    #      char *c, int n)
    return Rituals.call(
        'ritual_ZN35QVirtualKeyboardAbstractInputMethod2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QVirtualKeyboardAbstractInputMethod'

  #  A C++ QVirtualKeyboardAbstractInputMethod Python makes is of a C++ class
  #  of ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QVirtualKeyboardAbstractInputMethod'

  #  The functions Qt calls itself that QVirtualKeyboardAbstractInputMethod
  #  is the first to declare and that cannot be handed to Python yet, each as
  #  Qt declares it. A class of a program that writes one of them anew is
  #  refused, since Qt would never call what it wrote; see
  #  'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'inputModes': (
          'QList<QVirtualKeyboardInputEngine::InputMode> '
          'QVirtualKeyboardAbstractInputMethod::inputModes(const QString &)',
      ),
      'selectionLists': (
          'QList<QVirtualKeyboardSelectionListModel::Type> '
          'QVirtualKeyboardAbstractInputMethod::selectionLists()',
      ),
      'patternRecognitionModes': (
          'QList<QVirtualKeyboardInputEngine::PatternRecognitionMode> '
          'QVirtualKeyboardAbstractInputMethod::patternRecognitionModes() '
          'const',
      ),
      'traceBegin': (
          'QVirtualKeyboardTrace '
          '*QVirtualKeyboardAbstractInputMethod::traceBegin(int, '
          'QVirtualKeyboardInputEngine::PatternRecognitionMode, const '
          'QVariantMap &, const QVariantMap &)',
      ),
      'reselect': (
          'bool QVirtualKeyboardAbstractInputMethod::reselect(int, const '
          'QVirtualKeyboardInputEngine::ReselectFlags &)',
      ),
  }

  #  The functions Qt calls itself that QVirtualKeyboardAbstractInputMethod
  #  is the first to declare. A class of a program built on it can write one
  #  anew, and Qt then calls that. For each name: the key C++ knows the
  #  function by, what it gives, and what it takes.
  __virtual_functions__ = {
      'setInputMode': (
          ('_ZN35QVirtualKeyboardAbstractInputMethod12setInputModeERK7QStri'
           'ngN27QVirtualKeyboardInputEngine9InputModeE',
           ('bool', 'number', ''),
           (
               ('address', 'text', ''),
               ('int', 'enum',
                'QtVirtualKeyboard:QVirtualKeyboardInputEngine.InputMode'),
           )),
      ),
      'setTextCase': (
          ('_ZN35QVirtualKeyboardAbstractInputMethod11setTextCaseEN27QVirtu'
           'alKeyboardInputEngine8TextCaseE',
           ('bool', 'number', ''),
           (
               ('int', 'enum',
                'QtVirtualKeyboard:QVirtualKeyboardInputEngine.TextCase'),
           )),
      ),
      'keyEvent': (
          ('_ZN35QVirtualKeyboardAbstractInputMethod8keyEventEN2Qt3KeyERK7Q'
           'String6QFlagsINS0_16KeyboardModifierEE',
           ('bool', 'number', ''),
           (
               ('int', 'enum', 'QtCore:Qt.Key'),
               ('address', 'text', ''),
               ('int', 'flags', 'QtCore:Qt.KeyboardModifier'),
           )),
      ),
      'selectionListItemCount': (
          ('_ZN35QVirtualKeyboardAbstractInputMethod22selectionListItemCoun'
           'tEN34QVirtualKeyboardSelectionListModel4TypeE',
           ('int', 'number', ''),
           (
               ('int', 'enum',
                'QtVirtualKeyboard:QVirtualKeyboardSelectionListModel.Type'),
           )),
      ),
      'selectionListData': (
          ('_ZN35QVirtualKeyboardAbstractInputMethod17selectionListDataEN34'
           'QVirtualKeyboardSelectionListModel4TypeEiNS0_4RoleE',
           ('address', 'value', 'QtCore:QVariant'),
           (
               ('int', 'enum',
                'QtVirtualKeyboard:QVirtualKeyboardSelectionListModel.Type'),
               ('int', 'number', ''),
               ('int', 'enum',
                'QtVirtualKeyboard:QVirtualKeyboardSelectionListModel.Role'),
           )),
      ),
      'selectionListItemSelected': (
          ('_ZN35QVirtualKeyboardAbstractInputMethod25selectionListItemSele'
           'ctedEN34QVirtualKeyboardSelectionListModel4TypeEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'enum',
                'QtVirtualKeyboard:QVirtualKeyboardSelectionListModel.Type'),
               ('int', 'number', ''),
           )),
      ),
      'selectionListRemoveItem': (
          ('_ZN35QVirtualKeyboardAbstractInputMethod23selectionListRemoveIt'
           'emEN34QVirtualKeyboardSelectionListModel4TypeEi',
           ('bool', 'number', ''),
           (
               ('int', 'enum',
                'QtVirtualKeyboard:QVirtualKeyboardSelectionListModel.Type'),
               ('int', 'number', ''),
           )),
      ),
      'traceEnd': (
          ('_ZN35QVirtualKeyboardAbstractInputMethod8traceEndEP21QVirtualKe'
           'yboardTrace',
           ('bool', 'number', ''),
           (
               ('address', 'address',
                'QtVirtualKeyboard:QVirtualKeyboardTrace'),
           )),
      ),
      'clickPreeditText': (
          ('_ZN35QVirtualKeyboardAbstractInputMethod16clickPreeditTextEi',
           ('bool', 'number', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'reset': (
          ('_ZN35QVirtualKeyboardAbstractInputMethod5resetEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'update': (
          ('_ZN35QVirtualKeyboardAbstractInputMethod6updateEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'clearInputMode': (
          ('_ZN35QVirtualKeyboardAbstractInputMethod14clearInputModeEv',
           ('nothing', 'nothing', ''),
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
    Calls Qt's 'const QMetaObject
    *QVirtualKeyboardAbstractInputMethod::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardabstractinputmethod.html

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QVirtualKeyboardAbstractInputMethod::metaObject()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK35QVirtualKeyboardAbstractInputMethod10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def inputContext(self) -> Optional[QVirtualKeyboardInputContext]:
    """
    Calls Qt's 'QVirtualKeyboardInputContext
    *QVirtualKeyboardAbstractInputMethod::inputContext() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardabstractinputmethod.html

    Returns
    -------

    Optional[QVirtualKeyboardInputContext]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QVirtualKeyboardInputContext
    #      *QVirtualKeyboardAbstractInputMethod::inputContext() const
    address = self.uglySide.call(
        'ritual_ZNK35QVirtualKeyboardAbstractInputMethod12inputContextEv',
    )
    from . import QVirtualKeyboardInputContext
    return QVirtualKeyboardInputContext._cuteAt(address)

  def inputEngine(self) -> Optional[QVirtualKeyboardInputEngine]:
    """
    Calls Qt's 'QVirtualKeyboardInputEngine
    *QVirtualKeyboardAbstractInputMethod::inputEngine() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardabstractinputmethod.html

    Returns
    -------

    Optional[QVirtualKeyboardInputEngine]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QVirtualKeyboardInputEngine
    #      *QVirtualKeyboardAbstractInputMethod::inputEngine() const
    address = self.uglySide.call(
        'ritual_ZNK35QVirtualKeyboardAbstractInputMethod11inputEngineEv',
    )
    return QVirtualKeyboardInputEngine._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str, QVirtualKeyboardInputEngine.InputMode)
  def setInputMode(
      self,
      locale: str,
      inputMode: QVirtualKeyboardInputEngine.InputMode,
  ) -> bool:
    """
    Calls Qt's 'bool QVirtualKeyboardAbstractInputMethod::setInputMode(const
    QString &locale, QVirtualKeyboardInputEngine::InputMode inputMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardabstractinputmethod.html

    Parameters
    ----------

    locale : str
      Passed on as it is: a QString is made of it for the call.

    inputMode : QVirtualKeyboardInputEngine.InputMode
      Passed on as its number.
    """
    #  bool QVirtualKeyboardAbstractInputMethod::setInputMode(const QString
    #      &locale, QVirtualKeyboardInputEngine::InputMode inputMode)
    return self.uglySide.call(
        'ritual_ZN35QVirtualKeyboardAbstractInputMethod12setInputModeERK7QS'
        'tringN27QVirtualKeyboardInputEngine9InputModeE',
        locale, inputMode.value,
    )

  @overload(QVirtualKeyboardInputEngine.TextCase)
  def setTextCase(
      self,
      textCase: QVirtualKeyboardInputEngine.TextCase,
  ) -> bool:
    """
    Calls Qt's 'bool QVirtualKeyboardAbstractInputMethod::setTextCase(
    QVirtualKeyboardInputEngine::TextCase textCase)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardabstractinputmethod.html

    Parameters
    ----------

    textCase : QVirtualKeyboardInputEngine.TextCase
      Passed on as its number.
    """
    #  bool QVirtualKeyboardAbstractInputMethod::setTextCase(
    #      QVirtualKeyboardInputEngine::TextCase textCase)
    return self.uglySide.call(
        'ritual_ZN35QVirtualKeyboardAbstractInputMethod11setTextCaseEN27QVi'
        'rtualKeyboardInputEngine8TextCaseE',
        textCase.value,
    )

  @overload(QVirtualKeyboardInputEngine)
  @overload(NoneType)
  def setInputEngine(
      self,
      inputEngine: Optional[QVirtualKeyboardInputEngine],
  ) -> None:
    """
    Calls Qt's 'void QVirtualKeyboardAbstractInputMethod::setInputEngine(
    QVirtualKeyboardInputEngine *inputEngine)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardabstractinputmethod.html

    Parameters
    ----------

    inputEngine : Optional[QVirtualKeyboardInputEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QVirtualKeyboardAbstractInputMethod::setInputEngine(
    #      QVirtualKeyboardInputEngine *inputEngine)
    self.uglySide.call(
        'ritual_ZN35QVirtualKeyboardAbstractInputMethod14setInputEngineEP27'
        'QVirtualKeyboardInputEngine',
        self._addressOf(inputEngine),
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
    - Qt's 'QVirtualKeyboardAbstractInputMethod::
      QVirtualKeyboardAbstractInputMethod(
      QVirtualKeyboardAbstractInputMethodPrivate &dd, QObject *parent)': the
      class is abstract, so C++ cannot make one, and the C++ class of ours
      does not fill in every function it leaves open.
    - Qt's 'QVirtualKeyboardAbstractInputMethod::
      QVirtualKeyboardAbstractInputMethod(QObject *parent)': the class is
      abstract, so C++ cannot make one, and the C++ class of ours does not
      fill in every function it leaves open.
    """
    raise NotImplementedError(
        "'QVirtualKeyboardAbstractInputMethod.__init__' has no cute "
        "function yet. Qt's "
        "'QVirtualKeyboardAbstractInputMethod::QVirtualKeyboardAbstractInput"
        "Method(QVirtualKeyboardAbstractInputMethodPrivate &dd, QObject "
        "*parent)': the class is abstract, so C++ cannot make one, and the "
        "C++ class of ours does not fill in every function it leaves open. "
        "Qt's "
        "'QVirtualKeyboardAbstractInputMethod::QVirtualKeyboardAbstractInput"
        "Method(QObject *parent)': the class is abstract, so C++ cannot "
        "make one, and the C++ class of ours does not fill in every "
        "function it leaves open.")

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

  def d_func(self) -> Optional[QVirtualKeyboardAbstractInputMethodPrivate]:
    """
    Calls Qt's 'QVirtualKeyboardAbstractInputMethodPrivate
    *QVirtualKeyboardAbstractInputMethod::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardabstractinputmethod.html#d_func

    Returns
    -------

    Optional[QVirtualKeyboardAbstractInputMethodPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QVirtualKeyboardAbstractInputMethodPrivate
    #      *QVirtualKeyboardAbstractInputMethod::d_func()
    address = self.uglySide.call(
        'ritual_ZN35QVirtualKeyboardAbstractInputMethod6d_funcEv',
    )
    from . import QVirtualKeyboardAbstractInputMethodPrivate
    return QVirtualKeyboardAbstractInputMethodPrivate._cuteAt(address)

  @overload(Qt.Key, str, Qt.KeyboardModifiers)
  def keyEvent(
      self,
      key: Qt.Key,
      text: str,
      modifiers: Qt.KeyboardModifiers,
  ) -> bool:
    """
    Calls Qt's 'bool QVirtualKeyboardAbstractInputMethod::keyEvent(Qt::Key
    key, const QString &text, Qt::KeyboardModifiers modifiers)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardabstractinputmethod.html#keyEvent

    Parameters
    ----------

    key : Qt.Key
      Passed on as its number.

    text : str
      Passed on as it is: a QString is made of it for the call.

    modifiers : Qt.KeyboardModifiers
      Passed on as its number.
    """
    #  bool QVirtualKeyboardAbstractInputMethod::keyEvent(Qt::Key key, const
    #      QString &text, Qt::KeyboardModifiers modifiers)
    return self.uglySide.call(
        'ritual_ZN35QVirtualKeyboardAbstractInputMethod8keyEventEN2Qt3KeyER'
        'K7QString6QFlagsINS0_16KeyboardModifierEE',
        key.value, text, modifiers.value,
    )

  @overload(QVirtualKeyboardSelectionListModel.Type)
  def selectionListItemCount(
      self,
      type: QVirtualKeyboardSelectionListModel.Type,
  ) -> int:
    """
    Calls Qt's 'int
    QVirtualKeyboardAbstractInputMethod::selectionListItemCount(
    QVirtualKeyboardSelectionListModel::Type type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardabstractinputmethod.html

    Parameters
    ----------

    type : QVirtualKeyboardSelectionListModel.Type
      Passed on as its number.
    """
    #  int QVirtualKeyboardAbstractInputMethod::selectionListItemCount(
    #      QVirtualKeyboardSelectionListModel::Type type)
    ritual = (
        'ritual_ZN35QVirtualKeyboardAbstractInputMethod22selectionListItemC'
        'ountEN34QVirtualKeyboardSelectionListModel4TypeE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN35QVirtualKeyboardAbstractInputMethod22selectionLis'
          'tItemCountEN34QVirtualKeyboardSelectionListModel4TypeE')
    return self.uglySide.call(ritual, type.value)

  @overload(
      QVirtualKeyboardSelectionListModel.Type, int,
      QVirtualKeyboardSelectionListModel.Role,
  )
  def selectionListData(
      self,
      type: QVirtualKeyboardSelectionListModel.Type,
      index: int,
      role: QVirtualKeyboardSelectionListModel.Role,
  ) -> QVariant:
    """
    Calls Qt's 'QVariant
    QVirtualKeyboardAbstractInputMethod::selectionListData(
    QVirtualKeyboardSelectionListModel::Type type, int index,
    QVirtualKeyboardSelectionListModel::Role role)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardabstractinputmethod.html

    Parameters
    ----------

    type : QVirtualKeyboardSelectionListModel.Type
      Passed on as its number.

    index : int
      Passed on as it is.

    role : QVirtualKeyboardSelectionListModel.Role
      Passed on as its number.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QVirtualKeyboardAbstractInputMethod::selectionListData(
    #      QVirtualKeyboardSelectionListModel::Type type, int index,
    #      QVirtualKeyboardSelectionListModel::Role role)
    ritual = (
        'ritual_ZN35QVirtualKeyboardAbstractInputMethod17selectionListDataE'
        'N34QVirtualKeyboardSelectionListModel4TypeEiNS0_4RoleE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN35QVirtualKeyboardAbstractInputMethod17selectionLis'
          'tDataEN34QVirtualKeyboardSelectionListModel4TypeEiNS0_4RoleE')
    address = self.uglySide.call(ritual, type.value, index, role.value)
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(QVirtualKeyboardSelectionListModel.Type, int)
  def selectionListItemSelected(
      self,
      type: QVirtualKeyboardSelectionListModel.Type,
      index: int,
  ) -> None:
    """
    Calls Qt's 'void
    QVirtualKeyboardAbstractInputMethod::selectionListItemSelected(
    QVirtualKeyboardSelectionListModel::Type type, int index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardabstractinputmethod.html

    Parameters
    ----------

    type : QVirtualKeyboardSelectionListModel.Type
      Passed on as its number.

    index : int
      Passed on as it is.
    """
    #  void QVirtualKeyboardAbstractInputMethod::selectionListItemSelected(
    #      QVirtualKeyboardSelectionListModel::Type type, int index)
    ritual = (
        'ritual_ZN35QVirtualKeyboardAbstractInputMethod25selectionListItemS'
        'electedEN34QVirtualKeyboardSelectionListModel4TypeEi')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN35QVirtualKeyboardAbstractInputMethod25selectionLis'
          'tItemSelectedEN34QVirtualKeyboardSelectionListModel4TypeEi')
    self.uglySide.call(ritual, type.value, index)

  @overload(QVirtualKeyboardSelectionListModel.Type, int)
  def selectionListRemoveItem(
      self,
      type: QVirtualKeyboardSelectionListModel.Type,
      index: int,
  ) -> bool:
    """
    Calls Qt's 'bool
    QVirtualKeyboardAbstractInputMethod::selectionListRemoveItem(
    QVirtualKeyboardSelectionListModel::Type type, int index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardabstractinputmethod.html

    Parameters
    ----------

    type : QVirtualKeyboardSelectionListModel.Type
      Passed on as its number.

    index : int
      Passed on as it is.
    """
    #  bool QVirtualKeyboardAbstractInputMethod::selectionListRemoveItem(
    #      QVirtualKeyboardSelectionListModel::Type type, int index)
    ritual = (
        'ritual_ZN35QVirtualKeyboardAbstractInputMethod23selectionListRemov'
        'eItemEN34QVirtualKeyboardSelectionListModel4TypeEi')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN35QVirtualKeyboardAbstractInputMethod23selectionLis'
          'tRemoveItemEN34QVirtualKeyboardSelectionListModel4TypeEi')
    return self.uglySide.call(ritual, type.value, index)

  @overload(
      int, QVirtualKeyboardInputEngine.PatternRecognitionMode, QMap[str,
      QVariant], QMap[str, QVariant],
  )
  def traceBegin(
      self,
      traceId: int,
      patternRecognitionMode: QVirtualKeyboardInputEngine.PatternRecognitionMode,
      traceCaptureDeviceInfo: QMap[str, QVariant],
      traceScreenInfo: QMap[str, QVariant],
  ) -> Optional[QVirtualKeyboardTrace]:
    """
    Calls Qt's 'QVirtualKeyboardTrace
    *QVirtualKeyboardAbstractInputMethod::traceBegin(int traceId,
    QVirtualKeyboardInputEngine::PatternRecognitionMode
    patternRecognitionMode, const QVariantMap &traceCaptureDeviceInfo, const
    QVariantMap &traceScreenInfo)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardabstractinputmethod.html

    Parameters
    ----------

    traceId : int
      Passed on as it is.

    patternRecognitionMode : QVirtualKeyboardInputEngine.PatternRecognitionMode
      Passed on as its number.

    traceCaptureDeviceInfo : QMap[str, QVariant]
      Passed on as a map of Qt: Qt reads the C++ map, which stays Python's
      own. A dict of Python is made into one first, and refused when a key or
      a value does not fit.

    traceScreenInfo : QMap[str, QVariant]
      Passed on as a map of Qt: Qt reads the C++ map, which stays Python's
      own. A dict of Python is made into one first, and refused when a key or
      a value does not fit.

    Returns
    -------

    Optional[QVirtualKeyboardTrace]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QVirtualKeyboardTrace
    #      *QVirtualKeyboardAbstractInputMethod::traceBegin(int traceId,
    #      QVirtualKeyboardInputEngine::PatternRecognitionMode
    #      patternRecognitionMode, const QVariantMap &traceCaptureDeviceInfo,
    #      const QVariantMap &traceScreenInfo)
    address = self.uglySide.call(
        'ritual_ZN35QVirtualKeyboardAbstractInputMethod10traceBeginEiN27QVi'
        'rtualKeyboardInputEngine22PatternRecognitionModeERK4QMapI7QString8'
        'QVariantES7_',
        traceId, patternRecognitionMode.value,
        self._valueOf(traceCaptureDeviceInfo),
        self._valueOf(traceScreenInfo),
    )
    from . import QVirtualKeyboardTrace
    return QVirtualKeyboardTrace._cuteAt(address)

  @overload(QVirtualKeyboardTrace)
  @overload(NoneType)
  def traceEnd(self, trace: Optional[QVirtualKeyboardTrace]) -> bool:
    """
    Calls Qt's 'bool
    QVirtualKeyboardAbstractInputMethod::traceEnd(QVirtualKeyboardTrace
    *trace)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardabstractinputmethod.html#traceEnd

    Parameters
    ----------

    trace : Optional[QVirtualKeyboardTrace]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QVirtualKeyboardAbstractInputMethod::traceEnd(
    #      QVirtualKeyboardTrace *trace)
    ritual = (
        'ritual_ZN35QVirtualKeyboardAbstractInputMethod8traceEndEP21QVirtua'
        'lKeyboardTrace')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN35QVirtualKeyboardAbstractInputMethod8traceEndEP21Q'
          'VirtualKeyboardTrace')
    return self.uglySide.call(ritual, self._addressOf(trace))

  @overload(int)
  def clickPreeditText(self, cursorPosition: int) -> bool:
    """
    Calls Qt's 'bool
    QVirtualKeyboardAbstractInputMethod::clickPreeditText(int
    cursorPosition)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardabstractinputmethod.html

    Parameters
    ----------

    cursorPosition : int
      Passed on as it is.
    """
    #  bool QVirtualKeyboardAbstractInputMethod::clickPreeditText(int
    #      cursorPosition)
    ritual = (
        'ritual_ZN35QVirtualKeyboardAbstractInputMethod16clickPreeditTextEi')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN35QVirtualKeyboardAbstractInputMethod16clickPreedit'
          'TextEi')
    return self.uglySide.call(ritual, cursorPosition)

  @overload(QVirtualKeyboardSelectionListModel.Type)
  def selectionListChanged(
      self,
      type: QVirtualKeyboardSelectionListModel.Type,
  ) -> None:
    """
    Calls Qt's 'void
    QVirtualKeyboardAbstractInputMethod::selectionListChanged(
    QVirtualKeyboardSelectionListModel::Type type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardabstractinputmethod.html

    Parameters
    ----------

    type : QVirtualKeyboardSelectionListModel.Type
      Passed on as its number.
    """
    #  void QVirtualKeyboardAbstractInputMethod::selectionListChanged(
    #      QVirtualKeyboardSelectionListModel::Type type)
    self.uglySide.call(
        'ritual_ZN35QVirtualKeyboardAbstractInputMethod20selectionListChang'
        'edEN34QVirtualKeyboardSelectionListModel4TypeE',
        type.value,
    )

  @overload(QVirtualKeyboardSelectionListModel.Type, int)
  def selectionListActiveItemChanged(
      self,
      type: QVirtualKeyboardSelectionListModel.Type,
      index: int,
  ) -> None:
    """
    Calls Qt's 'void
    QVirtualKeyboardAbstractInputMethod::selectionListActiveItemChanged(
    QVirtualKeyboardSelectionListModel::Type type, int index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardabstractinputmethod.html

    Parameters
    ----------

    type : QVirtualKeyboardSelectionListModel.Type
      Passed on as its number.

    index : int
      Passed on as it is.
    """
    #  void QVirtualKeyboardAbstractInputMethod::
    #      selectionListActiveItemChanged(
    #      QVirtualKeyboardSelectionListModel::Type type, int index)
    self.uglySide.call(
        'ritual_ZN35QVirtualKeyboardAbstractInputMethod30selectionListActiv'
        'eItemChangedEN34QVirtualKeyboardSelectionListModel4TypeEi',
        type.value, index,
    )

  def selectionListsChanged(self) -> None:
    """
    Calls Qt's 'void
    QVirtualKeyboardAbstractInputMethod::selectionListsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardabstractinputmethod.html
    """
    #  void QVirtualKeyboardAbstractInputMethod::selectionListsChanged()
    self.uglySide.call(
        'ritual_ZN35QVirtualKeyboardAbstractInputMethod21selectionListsChan'
        'gedEv',
    )

  def reset(self) -> None:
    """
    Calls Qt's 'void QVirtualKeyboardAbstractInputMethod::reset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardabstractinputmethod.html#reset
    """
    #  void QVirtualKeyboardAbstractInputMethod::reset()
    ritual = 'ritual_ZN35QVirtualKeyboardAbstractInputMethod5resetEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN35QVirtualKeyboardAbstractInputMethod5resetEv'
    self.uglySide.call(ritual)

  def update(self) -> None:
    """
    Calls Qt's 'void QVirtualKeyboardAbstractInputMethod::update()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardabstractinputmethod.html#update
    """
    #  void QVirtualKeyboardAbstractInputMethod::update()
    ritual = 'ritual_ZN35QVirtualKeyboardAbstractInputMethod6updateEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN35QVirtualKeyboardAbstractInputMethod6updateEv'
    self.uglySide.call(ritual)

  def clearInputMode(self) -> None:
    """
    Calls Qt's 'void QVirtualKeyboardAbstractInputMethod::clearInputMode()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardabstractinputmethod.html
    """
    #  void QVirtualKeyboardAbstractInputMethod::clearInputMode()
    ritual = (
        'ritual_ZN35QVirtualKeyboardAbstractInputMethod14clearInputModeEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN35QVirtualKeyboardAbstractInputMethod14clearInputMo'
          'deEv')
    self.uglySide.call(ritual)

  @staticmethod
  def inputModes(*__, **_) -> Never:
    """
    Qt's 'QList<QVirtualKeyboardInputEngine::InputMode>
    QVirtualKeyboardAbstractInputMethod::inputModes(const QString &locale)':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QVirtualKeyboardAbstractInputMethod.inputModes' has no cute "
        "function yet. Qt's 'QList<QVirtualKeyboardInputEngine::InputMode> "
        "QVirtualKeyboardAbstractInputMethod::inputModes(const QString "
        "&locale)': gives a type Python has no way to take yet.")

  @staticmethod
  def patternRecognitionModes(*__, **_) -> Never:
    """
    Qt's 'QList<QVirtualKeyboardInputEngine::PatternRecognitionMode>
    QVirtualKeyboardAbstractInputMethod::patternRecognitionModes() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QVirtualKeyboardAbstractInputMethod.patternRecognitionModes' has "
        "no cute function yet. Qt's "
        "'QList<QVirtualKeyboardInputEngine::PatternRecognitionMode> "
        "QVirtualKeyboardAbstractInputMethod::patternRecognitionModes() "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def reselect(*__, **_) -> Never:
    """
    Qt's 'bool QVirtualKeyboardAbstractInputMethod::reselect(int
    cursorPosition, const QVirtualKeyboardInputEngine::ReselectFlags
    &reselectFlags)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QVirtualKeyboardAbstractInputMethod.reselect' has no cute "
        "function yet. Qt's 'bool "
        "QVirtualKeyboardAbstractInputMethod::reselect(int cursorPosition, "
        "const QVirtualKeyboardInputEngine::ReselectFlags &reselectFlags)': "
        "takes a type Python has no way to hand over yet.")

  @staticmethod
  def selectionLists(*__, **_) -> Never:
    """
    Qt's 'QList<QVirtualKeyboardSelectionListModel::Type>
    QVirtualKeyboardAbstractInputMethod::selectionLists()': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QVirtualKeyboardAbstractInputMethod.selectionLists' has no cute "
        "function yet. Qt's "
        "'QList<QVirtualKeyboardSelectionListModel::Type> "
        "QVirtualKeyboardAbstractInputMethod::selectionLists()': gives a "
        "type Python has no way to take yet.")
