"""
QQmlSettingsLabs binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLabsSettings/6.12.0/QtLabsSettings/private/qqmlsettings_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQmlSettingsLabs to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from ..QtQml import QQmlParserStatus

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QTimerEvent, QVariant
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QTimerEvent = WAIT['QTimerEvent']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlSettingsLabs(QObject, QQmlParserStatus):
  """
  The cute side of Qt's QQmlSettingsLabs: a plain Python object standing in
  front of one C++ QQmlSettingsLabs.

  It is built on the cute 'QObject', as Qt's QQmlSettingsLabs is built on
  Qt's QObject, and has everything that class has. It is built on the cute
  'QQmlParserStatus' as well, as Qt's QQmlSettingsLabs is built on Qt's
  QQmlParserStatus too, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQmlSettingsLabs that has a ritual and that Python
  can call so far, 12 names in all: 'metaObject', 'tr', 'category',
  'setCategory', 'fileName', 'setFileName', 'value', 'setValue', 'sync',
  'timerEvent', 'classBegin', 'componentComplete'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQmlSettingsLabs::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQmlSettingsLabs::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QQmlSettingsLabs::~QQmlSettingsLabs()': the destructor: Python
    never removes a C++ QQmlSettingsLabs.
  - Qt's 'QQmlSettingsLabsPrivate *QQmlSettingsLabs::d_func()': gives
    'QQmlSettingsLabsPrivate', which has no cute class yet.
  - Qt's 'const QQmlSettingsLabsPrivate *QQmlSettingsLabs::d_func() const':
    gives 'QQmlSettingsLabsPrivate', which has no cute class yet.

  What has no ritual
  ------------------

  4 of the 22 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQmlSettingsLabs is created at the first use, not by
    'QQmlSettingsLabs(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlSettingsLabs.
  - Qt tells when it has removed the C++ QQmlSettingsLabs. Every call on the
    cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QQmlSettingsLabs::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlsettingslabs.html#tr

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
    #  QString QQmlSettingsLabs::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN16QQmlSettingsLabs2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlSettingsLabs'

  #  Qt's QQmlSettingsLabs is built on more than one class. The part of a C++
  #  QQmlSettingsLabs that belongs to a class after the first begins
  #  somewhere inside the object, and the ritual named for that class gives
  #  where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QQmlParserStatus': 'ritual_cast_QQmlSettingsLabs_QQmlParserStatus',
  }

  #  A C++ QQmlSettingsLabs Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQmlSettingsLabs'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQmlSettingsLabs::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlsettingslabs.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQmlSettingsLabs::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK16QQmlSettingsLabs10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def category(self) -> str:
    """
    Calls Qt's 'QString QQmlSettingsLabs::category() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlsettingslabs.html#category

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlSettingsLabs::category() const
    return self.uglySide.call('ritual_ZNK16QQmlSettingsLabs8categoryEv')

  def fileName(self) -> str:
    """
    Calls Qt's 'QString QQmlSettingsLabs::fileName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlsettingslabs.html#fileName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlSettingsLabs::fileName() const
    return self.uglySide.call('ritual_ZNK16QQmlSettingsLabs8fileNameEv')

  @overload(str)
  @overload(str, QVariant)
  def value(
      self,
      key: str,
      defaultValue: Optional[QVariant] = None,
  ) -> QVariant:
    """
    Calls Qt's 'QVariant QQmlSettingsLabs::value(const QString &key, const
    QVariant &defaultValue) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlsettingslabs.html#value

    Parameters
    ----------

    key : str
      Passed on as it is: a QString is made of it for the call.

    defaultValue : Optional[QVariant]
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own. May be left out, as in Qt: a new 'QVariant()' is then passed on.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QQmlSettingsLabs::value(const QString &key, const QVariant
    #      &defaultValue) const
    if defaultValue is None:
      from ..QtCore import QVariant
      defaultValue = QVariant()
    address = self.uglySide.call(
        'ritual_ZNK16QQmlSettingsLabs5valueERK7QStringRK8QVariant',
        key, self._valueOf(defaultValue),
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setCategory(self, category: str) -> None:
    """
    Calls Qt's 'void QQmlSettingsLabs::setCategory(const QString &category)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlsettingslabs.html#setCategory

    Parameters
    ----------

    category : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQmlSettingsLabs::setCategory(const QString &category)
    self.uglySide.call(
        'ritual_ZN16QQmlSettingsLabs11setCategoryERK7QString', category,
    )

  @overload(str)
  def setFileName(self, fileName: str) -> None:
    """
    Calls Qt's 'void QQmlSettingsLabs::setFileName(const QString &fileName)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlsettingslabs.html#setFileName

    Parameters
    ----------

    fileName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQmlSettingsLabs::setFileName(const QString &fileName)
    self.uglySide.call(
        'ritual_ZN16QQmlSettingsLabs11setFileNameERK7QString', fileName,
    )

  @overload(str, QVariant)
  def setValue(self, key: str, value: QVariant) -> None:
    """
    Calls Qt's 'void QQmlSettingsLabs::setValue(const QString &key, const
    QVariant &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlsettingslabs.html#setValue

    Parameters
    ----------

    key : str
      Passed on as it is: a QString is made of it for the call.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QQmlSettingsLabs::setValue(const QString &key, const QVariant
    #      &value)
    self.uglySide.call(
        'ritual_ZN16QQmlSettingsLabs8setValueERK7QStringRK8QVariant',
        key, self._valueOf(value),
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
    'QQmlSettingsLabs::QQmlSettingsLabs(QObject *parent)', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsettingslabs.html#QQmlSettingsLabs

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQmlSettingsLabs::QQmlSettingsLabs(QObject *parent)
    self._noteCreation(QQmlSettingsLabs, lambda: Rituals.call(
        'ritual_ZN16QQmlSettingsLabsC1EP7QObject',
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

  def sync(self) -> None:
    """
    Calls Qt's 'void QQmlSettingsLabs::sync()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlsettingslabs.html#sync
    """
    #  void QQmlSettingsLabs::sync()
    self.uglySide.call('ritual_ZN16QQmlSettingsLabs4syncEv')

  @overload(QTimerEvent)
  @overload(NoneType)
  def timerEvent(self, event: Optional[QTimerEvent]) -> None:
    """
    Calls Qt's 'void QQmlSettingsLabs::timerEvent(QTimerEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlsettingslabs.html#timerEvent

    Parameters
    ----------

    event : Optional[QTimerEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlSettingsLabs::timerEvent(QTimerEvent *event)
    ritual = 'ritual_ZN16QQmlSettingsLabs10timerEventEP11QTimerEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QQmlSettingsLabs10timerEventEP11QTimerEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  def classBegin(self) -> None:
    """
    Calls Qt's 'void QQmlSettingsLabs::classBegin()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlsettingslabs.html#classBegin
    """
    #  void QQmlSettingsLabs::classBegin()
    ritual = 'ritual_ZN16QQmlSettingsLabs10classBeginEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QQmlSettingsLabs10classBeginEv'
    self.uglySide.call(ritual)

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQmlSettingsLabs::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsettingslabs.html#componentComplete
    """
    #  void QQmlSettingsLabs::componentComplete()
    ritual = 'ritual_ZN16QQmlSettingsLabs17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QQmlSettingsLabs17componentCompleteEv'
    self.uglySide.call(ritual)
