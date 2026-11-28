"""
QQmlTableModelColumn binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLabsQmlModels/6.12.0/QtLabsQmlModels/private/qqmltablemodelcolumn_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQmlTableModelColumn to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QHash

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QObject
  from ..QtQml import QJSValue
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QJSValue = WAIT['QJSValue']
  QObject = WAIT['QObject']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlTableModelColumn(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlTableModelColumn: a plain Python object standing
  in front of one C++ QQmlTableModelColumn.

  What exists
  -----------

  Every function of Qt's QQmlTableModelColumn that has a ritual and that
  Python can call so far, 47 names in all: 'metaObject', 'tr', 'display',
  'setDisplay', 'decoration', 'setDecoration', 'edit', 'setEdit', 'toolTip',
  'setToolTip', 'statusTip', 'setStatusTip', 'whatsThis', 'setWhatsThis',
  'font', 'setFont', 'textAlignment', 'setTextAlignment', 'background',
  'setBackground', 'foreground', 'setForeground', 'checkState',
  'setCheckState', 'accessibleText', 'setAccessibleText',
  'accessibleDescription', 'setAccessibleDescription', 'sizeHint',
  'setSizeHint', 'getterAtRole', 'getters', 'indexChanged', 'displayChanged',
  'decorationChanged', 'editChanged', 'toolTipChanged', 'statusTipChanged',
  'whatsThisChanged', 'fontChanged', 'textAlignmentChanged',
  'backgroundChanged', 'foregroundChanged', 'checkStateChanged',
  'accessibleTextChanged', 'accessibleDescriptionChanged', 'sizeHintChanged'.
  It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQmlTableModelColumn::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQmlTableModelColumn::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QQmlTableModelColumn::~QQmlTableModelColumn()': the destructor:
    Python never removes a C++ QQmlTableModelColumn.
  - Qt's 'const QHash<int, QString>
    QQmlTableModelColumn::supportedRoleNames()': gives a type Python has no
    way to take yet.

  What has no ritual
  ------------------

  2 of the 54 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQmlTableModelColumn is created at the first use, not by
    'QQmlTableModelColumn(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlTableModelColumn.
  - Qt tells when it has removed the C++ QQmlTableModelColumn. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQmlTableModelColumn that has no cute function yet,
    'supportedRoleNames', holds a function that raises 'NotImplementedError',
    and its docstring says why.
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
    Calls Qt's 'QString QQmlTableModelColumn::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltablemodelcolumn.html#tr

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
    #  QString QQmlTableModelColumn::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN20QQmlTableModelColumn2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlTableModelColumn'

  #  A C++ QQmlTableModelColumn Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQmlTableModelColumn'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQmlTableModelColumn::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltablemodelcolumn.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQmlTableModelColumn::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK20QQmlTableModelColumn10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def display(self) -> QJSValue:
    """
    Calls Qt's 'QJSValue QQmlTableModelColumn::display() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltablemodelcolumn.html#display

    Returns
    -------

    QJSValue
      A new cute QJSValue around the copy Qt gave back. Python owns it.
    """
    #  QJSValue QQmlTableModelColumn::display() const
    address = self.uglySide.call(
        'ritual_ZNK20QQmlTableModelColumn7displayEv',
    )
    from ..QtQml import QJSValue
    return QJSValue._cuteOwning(address)

  def decoration(self) -> QJSValue:
    """
    Calls Qt's 'QJSValue QQmlTableModelColumn::decoration() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltablemodelcolumn.html#decoration

    Returns
    -------

    QJSValue
      A new cute QJSValue around the copy Qt gave back. Python owns it.
    """
    #  QJSValue QQmlTableModelColumn::decoration() const
    address = self.uglySide.call(
        'ritual_ZNK20QQmlTableModelColumn10decorationEv',
    )
    from ..QtQml import QJSValue
    return QJSValue._cuteOwning(address)

  def edit(self) -> QJSValue:
    """
    Calls Qt's 'QJSValue QQmlTableModelColumn::edit() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltablemodelcolumn.html#edit

    Returns
    -------

    QJSValue
      A new cute QJSValue around the copy Qt gave back. Python owns it.
    """
    #  QJSValue QQmlTableModelColumn::edit() const
    address = self.uglySide.call('ritual_ZNK20QQmlTableModelColumn4editEv')
    from ..QtQml import QJSValue
    return QJSValue._cuteOwning(address)

  def toolTip(self) -> QJSValue:
    """
    Calls Qt's 'QJSValue QQmlTableModelColumn::toolTip() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltablemodelcolumn.html#toolTip

    Returns
    -------

    QJSValue
      A new cute QJSValue around the copy Qt gave back. Python owns it.
    """
    #  QJSValue QQmlTableModelColumn::toolTip() const
    address = self.uglySide.call(
        'ritual_ZNK20QQmlTableModelColumn7toolTipEv',
    )
    from ..QtQml import QJSValue
    return QJSValue._cuteOwning(address)

  def statusTip(self) -> QJSValue:
    """
    Calls Qt's 'QJSValue QQmlTableModelColumn::statusTip() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltablemodelcolumn.html#statusTip

    Returns
    -------

    QJSValue
      A new cute QJSValue around the copy Qt gave back. Python owns it.
    """
    #  QJSValue QQmlTableModelColumn::statusTip() const
    address = self.uglySide.call(
        'ritual_ZNK20QQmlTableModelColumn9statusTipEv',
    )
    from ..QtQml import QJSValue
    return QJSValue._cuteOwning(address)

  def whatsThis(self) -> QJSValue:
    """
    Calls Qt's 'QJSValue QQmlTableModelColumn::whatsThis() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltablemodelcolumn.html#whatsThis

    Returns
    -------

    QJSValue
      A new cute QJSValue around the copy Qt gave back. Python owns it.
    """
    #  QJSValue QQmlTableModelColumn::whatsThis() const
    address = self.uglySide.call(
        'ritual_ZNK20QQmlTableModelColumn9whatsThisEv',
    )
    from ..QtQml import QJSValue
    return QJSValue._cuteOwning(address)

  def font(self) -> QJSValue:
    """
    Calls Qt's 'QJSValue QQmlTableModelColumn::font() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltablemodelcolumn.html#font

    Returns
    -------

    QJSValue
      A new cute QJSValue around the copy Qt gave back. Python owns it.
    """
    #  QJSValue QQmlTableModelColumn::font() const
    address = self.uglySide.call('ritual_ZNK20QQmlTableModelColumn4fontEv')
    from ..QtQml import QJSValue
    return QJSValue._cuteOwning(address)

  def textAlignment(self) -> QJSValue:
    """
    Calls Qt's 'QJSValue QQmlTableModelColumn::textAlignment() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltablemodelcolumn.html#textAlignment

    Returns
    -------

    QJSValue
      A new cute QJSValue around the copy Qt gave back. Python owns it.
    """
    #  QJSValue QQmlTableModelColumn::textAlignment() const
    address = self.uglySide.call(
        'ritual_ZNK20QQmlTableModelColumn13textAlignmentEv',
    )
    from ..QtQml import QJSValue
    return QJSValue._cuteOwning(address)

  def background(self) -> QJSValue:
    """
    Calls Qt's 'QJSValue QQmlTableModelColumn::background() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltablemodelcolumn.html#background

    Returns
    -------

    QJSValue
      A new cute QJSValue around the copy Qt gave back. Python owns it.
    """
    #  QJSValue QQmlTableModelColumn::background() const
    address = self.uglySide.call(
        'ritual_ZNK20QQmlTableModelColumn10backgroundEv',
    )
    from ..QtQml import QJSValue
    return QJSValue._cuteOwning(address)

  def foreground(self) -> QJSValue:
    """
    Calls Qt's 'QJSValue QQmlTableModelColumn::foreground() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltablemodelcolumn.html#foreground

    Returns
    -------

    QJSValue
      A new cute QJSValue around the copy Qt gave back. Python owns it.
    """
    #  QJSValue QQmlTableModelColumn::foreground() const
    address = self.uglySide.call(
        'ritual_ZNK20QQmlTableModelColumn10foregroundEv',
    )
    from ..QtQml import QJSValue
    return QJSValue._cuteOwning(address)

  def checkState(self) -> QJSValue:
    """
    Calls Qt's 'QJSValue QQmlTableModelColumn::checkState() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltablemodelcolumn.html#checkState

    Returns
    -------

    QJSValue
      A new cute QJSValue around the copy Qt gave back. Python owns it.
    """
    #  QJSValue QQmlTableModelColumn::checkState() const
    address = self.uglySide.call(
        'ritual_ZNK20QQmlTableModelColumn10checkStateEv',
    )
    from ..QtQml import QJSValue
    return QJSValue._cuteOwning(address)

  def accessibleText(self) -> QJSValue:
    """
    Calls Qt's 'QJSValue QQmlTableModelColumn::accessibleText() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltablemodelcolumn.html#accessibleText

    Returns
    -------

    QJSValue
      A new cute QJSValue around the copy Qt gave back. Python owns it.
    """
    #  QJSValue QQmlTableModelColumn::accessibleText() const
    address = self.uglySide.call(
        'ritual_ZNK20QQmlTableModelColumn14accessibleTextEv',
    )
    from ..QtQml import QJSValue
    return QJSValue._cuteOwning(address)

  def accessibleDescription(self) -> QJSValue:
    """
    Calls Qt's 'QJSValue QQmlTableModelColumn::accessibleDescription()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltablemodelcolumn.html#accessibleDescription

    Returns
    -------

    QJSValue
      A new cute QJSValue around the copy Qt gave back. Python owns it.
    """
    #  QJSValue QQmlTableModelColumn::accessibleDescription() const
    address = self.uglySide.call(
        'ritual_ZNK20QQmlTableModelColumn21accessibleDescriptionEv',
    )
    from ..QtQml import QJSValue
    return QJSValue._cuteOwning(address)

  def sizeHint(self) -> QJSValue:
    """
    Calls Qt's 'QJSValue QQmlTableModelColumn::sizeHint() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltablemodelcolumn.html#sizeHint

    Returns
    -------

    QJSValue
      A new cute QJSValue around the copy Qt gave back. Python owns it.
    """
    #  QJSValue QQmlTableModelColumn::sizeHint() const
    address = self.uglySide.call(
        'ritual_ZNK20QQmlTableModelColumn8sizeHintEv',
    )
    from ..QtQml import QJSValue
    return QJSValue._cuteOwning(address)

  def getters(self) -> QHash[str, QJSValue]:
    """
    Calls Qt's 'const QHash<QString, QJSValue>
    QQmlTableModelColumn::getters() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltablemodelcolumn.html#getters

    Returns
    -------

    QHash[str, QJSValue]
      A new cute map around the copy Qt gave back. Python owns it.
    """
    #  const QHash<QString, QJSValue> QQmlTableModelColumn::getters() const
    address = self.uglySide.call(
        'ritual_ZNK20QQmlTableModelColumn7gettersEv',
    )
    from ..QtQml import QJSValue
    return QHash[str, QJSValue]._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QJSValue)
  def setDisplay(self, stringOrFunction: QJSValue) -> None:
    """
    Calls Qt's 'void QQmlTableModelColumn::setDisplay(const QJSValue
    &stringOrFunction)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltablemodelcolumn.html#setDisplay

    Parameters
    ----------

    stringOrFunction : QJSValue
      Passed on as a value: Qt reads the C++ QJSValue, which stays Python's
      own.
    """
    #  void QQmlTableModelColumn::setDisplay(const QJSValue
    #      &stringOrFunction)
    self.uglySide.call(
        'ritual_ZN20QQmlTableModelColumn10setDisplayERK8QJSValue',
        self._valueOf(stringOrFunction),
    )

  @overload(QJSValue)
  def setDecoration(self, stringOrFunction: QJSValue) -> None:
    """
    Calls Qt's 'void QQmlTableModelColumn::setDecoration(const QJSValue
    &stringOrFunction)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltablemodelcolumn.html#setDecoration

    Parameters
    ----------

    stringOrFunction : QJSValue
      Passed on as a value: Qt reads the C++ QJSValue, which stays Python's
      own.
    """
    #  void QQmlTableModelColumn::setDecoration(const QJSValue
    #      &stringOrFunction)
    self.uglySide.call(
        'ritual_ZN20QQmlTableModelColumn13setDecorationERK8QJSValue',
        self._valueOf(stringOrFunction),
    )

  @overload(QJSValue)
  def setEdit(self, stringOrFunction: QJSValue) -> None:
    """
    Calls Qt's 'void QQmlTableModelColumn::setEdit(const QJSValue
    &stringOrFunction)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltablemodelcolumn.html#setEdit

    Parameters
    ----------

    stringOrFunction : QJSValue
      Passed on as a value: Qt reads the C++ QJSValue, which stays Python's
      own.
    """
    #  void QQmlTableModelColumn::setEdit(const QJSValue &stringOrFunction)
    self.uglySide.call(
        'ritual_ZN20QQmlTableModelColumn7setEditERK8QJSValue',
        self._valueOf(stringOrFunction),
    )

  @overload(QJSValue)
  def setToolTip(self, stringOrFunction: QJSValue) -> None:
    """
    Calls Qt's 'void QQmlTableModelColumn::setToolTip(const QJSValue
    &stringOrFunction)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltablemodelcolumn.html#setToolTip

    Parameters
    ----------

    stringOrFunction : QJSValue
      Passed on as a value: Qt reads the C++ QJSValue, which stays Python's
      own.
    """
    #  void QQmlTableModelColumn::setToolTip(const QJSValue
    #      &stringOrFunction)
    self.uglySide.call(
        'ritual_ZN20QQmlTableModelColumn10setToolTipERK8QJSValue',
        self._valueOf(stringOrFunction),
    )

  @overload(QJSValue)
  def setStatusTip(self, stringOrFunction: QJSValue) -> None:
    """
    Calls Qt's 'void QQmlTableModelColumn::setStatusTip(const QJSValue
    &stringOrFunction)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltablemodelcolumn.html#setStatusTip

    Parameters
    ----------

    stringOrFunction : QJSValue
      Passed on as a value: Qt reads the C++ QJSValue, which stays Python's
      own.
    """
    #  void QQmlTableModelColumn::setStatusTip(const QJSValue
    #      &stringOrFunction)
    self.uglySide.call(
        'ritual_ZN20QQmlTableModelColumn12setStatusTipERK8QJSValue',
        self._valueOf(stringOrFunction),
    )

  @overload(QJSValue)
  def setWhatsThis(self, stringOrFunction: QJSValue) -> None:
    """
    Calls Qt's 'void QQmlTableModelColumn::setWhatsThis(const QJSValue
    &stringOrFunction)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltablemodelcolumn.html#setWhatsThis

    Parameters
    ----------

    stringOrFunction : QJSValue
      Passed on as a value: Qt reads the C++ QJSValue, which stays Python's
      own.
    """
    #  void QQmlTableModelColumn::setWhatsThis(const QJSValue
    #      &stringOrFunction)
    self.uglySide.call(
        'ritual_ZN20QQmlTableModelColumn12setWhatsThisERK8QJSValue',
        self._valueOf(stringOrFunction),
    )

  @overload(QJSValue)
  def setFont(self, stringOrFunction: QJSValue) -> None:
    """
    Calls Qt's 'void QQmlTableModelColumn::setFont(const QJSValue
    &stringOrFunction)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltablemodelcolumn.html#setFont

    Parameters
    ----------

    stringOrFunction : QJSValue
      Passed on as a value: Qt reads the C++ QJSValue, which stays Python's
      own.
    """
    #  void QQmlTableModelColumn::setFont(const QJSValue &stringOrFunction)
    self.uglySide.call(
        'ritual_ZN20QQmlTableModelColumn7setFontERK8QJSValue',
        self._valueOf(stringOrFunction),
    )

  @overload(QJSValue)
  def setTextAlignment(self, stringOrFunction: QJSValue) -> None:
    """
    Calls Qt's 'void QQmlTableModelColumn::setTextAlignment(const QJSValue
    &stringOrFunction)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltablemodelcolumn.html#setTextAlignment

    Parameters
    ----------

    stringOrFunction : QJSValue
      Passed on as a value: Qt reads the C++ QJSValue, which stays Python's
      own.
    """
    #  void QQmlTableModelColumn::setTextAlignment(const QJSValue
    #      &stringOrFunction)
    self.uglySide.call(
        'ritual_ZN20QQmlTableModelColumn16setTextAlignmentERK8QJSValue',
        self._valueOf(stringOrFunction),
    )

  @overload(QJSValue)
  def setBackground(self, stringOrFunction: QJSValue) -> None:
    """
    Calls Qt's 'void QQmlTableModelColumn::setBackground(const QJSValue
    &stringOrFunction)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltablemodelcolumn.html#setBackground

    Parameters
    ----------

    stringOrFunction : QJSValue
      Passed on as a value: Qt reads the C++ QJSValue, which stays Python's
      own.
    """
    #  void QQmlTableModelColumn::setBackground(const QJSValue
    #      &stringOrFunction)
    self.uglySide.call(
        'ritual_ZN20QQmlTableModelColumn13setBackgroundERK8QJSValue',
        self._valueOf(stringOrFunction),
    )

  @overload(QJSValue)
  def setForeground(self, stringOrFunction: QJSValue) -> None:
    """
    Calls Qt's 'void QQmlTableModelColumn::setForeground(const QJSValue
    &stringOrFunction)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltablemodelcolumn.html#setForeground

    Parameters
    ----------

    stringOrFunction : QJSValue
      Passed on as a value: Qt reads the C++ QJSValue, which stays Python's
      own.
    """
    #  void QQmlTableModelColumn::setForeground(const QJSValue
    #      &stringOrFunction)
    self.uglySide.call(
        'ritual_ZN20QQmlTableModelColumn13setForegroundERK8QJSValue',
        self._valueOf(stringOrFunction),
    )

  @overload(QJSValue)
  def setCheckState(self, stringOrFunction: QJSValue) -> None:
    """
    Calls Qt's 'void QQmlTableModelColumn::setCheckState(const QJSValue
    &stringOrFunction)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltablemodelcolumn.html#setCheckState

    Parameters
    ----------

    stringOrFunction : QJSValue
      Passed on as a value: Qt reads the C++ QJSValue, which stays Python's
      own.
    """
    #  void QQmlTableModelColumn::setCheckState(const QJSValue
    #      &stringOrFunction)
    self.uglySide.call(
        'ritual_ZN20QQmlTableModelColumn13setCheckStateERK8QJSValue',
        self._valueOf(stringOrFunction),
    )

  @overload(QJSValue)
  def setAccessibleText(self, stringOrFunction: QJSValue) -> None:
    """
    Calls Qt's 'void QQmlTableModelColumn::setAccessibleText(const QJSValue
    &stringOrFunction)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltablemodelcolumn.html#setAccessibleText

    Parameters
    ----------

    stringOrFunction : QJSValue
      Passed on as a value: Qt reads the C++ QJSValue, which stays Python's
      own.
    """
    #  void QQmlTableModelColumn::setAccessibleText(const QJSValue
    #      &stringOrFunction)
    self.uglySide.call(
        'ritual_ZN20QQmlTableModelColumn17setAccessibleTextERK8QJSValue',
        self._valueOf(stringOrFunction),
    )

  @overload(QJSValue)
  def setAccessibleDescription(self, stringOrFunction: QJSValue) -> None:
    """
    Calls Qt's 'void QQmlTableModelColumn::setAccessibleDescription(const
    QJSValue &stringOrFunction)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltablemodelcolumn.html#setAccessibleDescription

    Parameters
    ----------

    stringOrFunction : QJSValue
      Passed on as a value: Qt reads the C++ QJSValue, which stays Python's
      own.
    """
    #  void QQmlTableModelColumn::setAccessibleDescription(const QJSValue
    #      &stringOrFunction)
    self.uglySide.call(
        'ritual_ZN20QQmlTableModelColumn24setAccessibleDescriptionERK8QJSVa'
        'lue',
        self._valueOf(stringOrFunction),
    )

  @overload(QJSValue)
  def setSizeHint(self, stringOrFunction: QJSValue) -> None:
    """
    Calls Qt's 'void QQmlTableModelColumn::setSizeHint(const QJSValue
    &stringOrFunction)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltablemodelcolumn.html#setSizeHint

    Parameters
    ----------

    stringOrFunction : QJSValue
      Passed on as a value: Qt reads the C++ QJSValue, which stays Python's
      own.
    """
    #  void QQmlTableModelColumn::setSizeHint(const QJSValue
    #      &stringOrFunction)
    self.uglySide.call(
        'ritual_ZN20QQmlTableModelColumn11setSizeHintERK8QJSValue',
        self._valueOf(stringOrFunction),
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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QQmlTableModelColumn::QQmlTableModelColumn(QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltablemodelcolumn.html#QQmlTableModelColumn

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQmlTableModelColumn::QQmlTableModelColumn(QObject *parent)
    self._noteCreation(QQmlTableModelColumn, lambda: Rituals.call(
        'ritual_ZN20QQmlTableModelColumnC1EP7QObject',
        self._addressOf(parent, 'QObject'),
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

  @overload(str)
  def getterAtRole(self, roleName: str) -> QJSValue:
    """
    Calls Qt's 'QJSValue QQmlTableModelColumn::getterAtRole(const QString
    &roleName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltablemodelcolumn.html#getterAtRole

    Parameters
    ----------

    roleName : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QJSValue
      A new cute QJSValue around the copy Qt gave back. Python owns it.
    """
    #  QJSValue QQmlTableModelColumn::getterAtRole(const QString &roleName)
    address = self.uglySide.call(
        'ritual_ZN20QQmlTableModelColumn12getterAtRoleERK7QString', roleName,
    )
    from ..QtQml import QJSValue
    return QJSValue._cuteOwning(address)

  def indexChanged(self) -> None:
    """
    Calls Qt's 'void QQmlTableModelColumn::indexChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltablemodelcolumn.html#indexChanged
    """
    #  void QQmlTableModelColumn::indexChanged()
    self.uglySide.call('ritual_ZN20QQmlTableModelColumn12indexChangedEv')

  def displayChanged(self) -> None:
    """
    Calls Qt's 'void QQmlTableModelColumn::displayChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltablemodelcolumn.html#displayChanged
    """
    #  void QQmlTableModelColumn::displayChanged()
    self.uglySide.call('ritual_ZN20QQmlTableModelColumn14displayChangedEv')

  def decorationChanged(self) -> None:
    """
    Calls Qt's 'void QQmlTableModelColumn::decorationChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltablemodelcolumn.html#decorationChanged
    """
    #  void QQmlTableModelColumn::decorationChanged()
    self.uglySide.call(
        'ritual_ZN20QQmlTableModelColumn17decorationChangedEv',
    )

  def editChanged(self) -> None:
    """
    Calls Qt's 'void QQmlTableModelColumn::editChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltablemodelcolumn.html#editChanged
    """
    #  void QQmlTableModelColumn::editChanged()
    self.uglySide.call('ritual_ZN20QQmlTableModelColumn11editChangedEv')

  def toolTipChanged(self) -> None:
    """
    Calls Qt's 'void QQmlTableModelColumn::toolTipChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltablemodelcolumn.html#toolTipChanged
    """
    #  void QQmlTableModelColumn::toolTipChanged()
    self.uglySide.call('ritual_ZN20QQmlTableModelColumn14toolTipChangedEv')

  def statusTipChanged(self) -> None:
    """
    Calls Qt's 'void QQmlTableModelColumn::statusTipChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltablemodelcolumn.html#statusTipChanged
    """
    #  void QQmlTableModelColumn::statusTipChanged()
    self.uglySide.call('ritual_ZN20QQmlTableModelColumn16statusTipChangedEv')

  def whatsThisChanged(self) -> None:
    """
    Calls Qt's 'void QQmlTableModelColumn::whatsThisChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltablemodelcolumn.html#whatsThisChanged
    """
    #  void QQmlTableModelColumn::whatsThisChanged()
    self.uglySide.call('ritual_ZN20QQmlTableModelColumn16whatsThisChangedEv')

  def fontChanged(self) -> None:
    """
    Calls Qt's 'void QQmlTableModelColumn::fontChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltablemodelcolumn.html#fontChanged
    """
    #  void QQmlTableModelColumn::fontChanged()
    self.uglySide.call('ritual_ZN20QQmlTableModelColumn11fontChangedEv')

  def textAlignmentChanged(self) -> None:
    """
    Calls Qt's 'void QQmlTableModelColumn::textAlignmentChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltablemodelcolumn.html#textAlignmentChanged
    """
    #  void QQmlTableModelColumn::textAlignmentChanged()
    self.uglySide.call(
        'ritual_ZN20QQmlTableModelColumn20textAlignmentChangedEv',
    )

  def backgroundChanged(self) -> None:
    """
    Calls Qt's 'void QQmlTableModelColumn::backgroundChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltablemodelcolumn.html#backgroundChanged
    """
    #  void QQmlTableModelColumn::backgroundChanged()
    self.uglySide.call(
        'ritual_ZN20QQmlTableModelColumn17backgroundChangedEv',
    )

  def foregroundChanged(self) -> None:
    """
    Calls Qt's 'void QQmlTableModelColumn::foregroundChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltablemodelcolumn.html#foregroundChanged
    """
    #  void QQmlTableModelColumn::foregroundChanged()
    self.uglySide.call(
        'ritual_ZN20QQmlTableModelColumn17foregroundChangedEv',
    )

  def checkStateChanged(self) -> None:
    """
    Calls Qt's 'void QQmlTableModelColumn::checkStateChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltablemodelcolumn.html#checkStateChanged
    """
    #  void QQmlTableModelColumn::checkStateChanged()
    self.uglySide.call(
        'ritual_ZN20QQmlTableModelColumn17checkStateChangedEv',
    )

  def accessibleTextChanged(self) -> None:
    """
    Calls Qt's 'void QQmlTableModelColumn::accessibleTextChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltablemodelcolumn.html#accessibleTextChanged
    """
    #  void QQmlTableModelColumn::accessibleTextChanged()
    self.uglySide.call(
        'ritual_ZN20QQmlTableModelColumn21accessibleTextChangedEv',
    )

  def accessibleDescriptionChanged(self) -> None:
    """
    Calls Qt's 'void QQmlTableModelColumn::accessibleDescriptionChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltablemodelcolumn.html
    """
    #  void QQmlTableModelColumn::accessibleDescriptionChanged()
    self.uglySide.call(
        'ritual_ZN20QQmlTableModelColumn28accessibleDescriptionChangedEv',
    )

  def sizeHintChanged(self) -> None:
    """
    Calls Qt's 'void QQmlTableModelColumn::sizeHintChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltablemodelcolumn.html#sizeHintChanged
    """
    #  void QQmlTableModelColumn::sizeHintChanged()
    self.uglySide.call('ritual_ZN20QQmlTableModelColumn15sizeHintChangedEv')

  @staticmethod
  def supportedRoleNames(*__, **_) -> Never:
    """
    Qt's 'const QHash<int, QString>
    QQmlTableModelColumn::supportedRoleNames()': gives a type Python has no
    way to take yet.
    """
    raise NotImplementedError(
        "'QQmlTableModelColumn.supportedRoleNames' has no cute function "
        "yet. Qt's 'const QHash<int, QString> "
        "QQmlTableModelColumn::supportedRoleNames()': gives a type Python "
        "has no way to take yet.")
