"""
QDesignerPropertyEditorInterface binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/abstractpropertyeditor.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QObject
from ..QtWidgets import QWidget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QVariant
  from . import QDesignerFormEditorInterface
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDesignerPropertyEditorInterface(QWidget):
  """
  The cute side of Qt's QDesignerPropertyEditorInterface: a plain Python
  object standing in front of one C++ QDesignerPropertyEditorInterface.

  It is built on the cute 'QWidget', as Qt's QDesignerPropertyEditorInterface
  is built on Qt's QWidget, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QDesignerPropertyEditorInterface that has a ritual
  and that Python can call so far, 10 names in all: 'metaObject', 'tr',
  'core', 'isReadOnly', 'object', 'currentPropertyName', 'propertyChanged',
  'setObject', 'setPropertyValue', 'setReadOnly'. It can be made from Python,
  in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QDesignerPropertyEditorInterface::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int QDesignerPropertyEditorInterface::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's
    'QDesignerPropertyEditorInterface::~QDesignerPropertyEditorInterface()':
    the destructor: Python never removes a C++
    QDesignerPropertyEditorInterface.

  What has no ritual
  ------------------

  2 of the 16 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QDesignerPropertyEditorInterface is created at the first use, not
    by 'QDesignerPropertyEditorInterface(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDesignerPropertyEditorInterface.
  - Qt tells when it has removed the C++ QDesignerPropertyEditorInterface.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
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
    Calls Qt's 'QString QDesignerPropertyEditorInterface::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerpropertyeditorinterface.html#tr

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
    #  QString QDesignerPropertyEditorInterface::tr(const char *s, const char
    #      *c, int n)
    return Rituals.call(
        'ritual_ZN32QDesignerPropertyEditorInterface2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDesignerPropertyEditorInterface'

  #  A C++ QDesignerPropertyEditorInterface Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QDesignerPropertyEditorInterface'

  #  The functions Qt calls itself that QDesignerPropertyEditorInterface is
  #  the first to declare. A class of a program built on it can write one
  #  anew, and Qt then calls that. For each name: the key C++ knows the
  #  function by, what it gives, and what it takes.
  __virtual_functions__ = {
      'core': (
          ('_ZNK32QDesignerPropertyEditorInterface4coreEv',
           ('address', 'address', 'QtDesigner:QDesignerFormEditorInterface'),
           ()),
      ),
      'isReadOnly': (
          ('_ZNK32QDesignerPropertyEditorInterface10isReadOnlyEv',
           ('bool', 'number', ''),
           ()),
      ),
      'object': (
          ('_ZNK32QDesignerPropertyEditorInterface6objectEv',
           ('address', 'address', 'QtCore:QObject'),
           ()),
      ),
      'currentPropertyName': (
          ('_ZNK32QDesignerPropertyEditorInterface19currentPropertyNameEv',
           ('address', 'text', ''),
           ()),
      ),
      'setObject': (
          ('_ZN32QDesignerPropertyEditorInterface9setObjectEP7QObject',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtCore:QObject'),
           )),
      ),
      'setPropertyValue': (
          ('_ZN32QDesignerPropertyEditorInterface16setPropertyValueERK7QStr'
           'ingRK8QVariantb',
           ('nothing', 'nothing', ''),
           (
               ('address', 'text', ''),
               ('address', 'value', 'QtCore:QVariant'),
               ('bool', 'number', ''),
           )),
      ),
      'setReadOnly': (
          ('_ZN32QDesignerPropertyEditorInterface11setReadOnlyEb',
           ('nothing', 'nothing', ''),
           (
               ('bool', 'number', ''),
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
    Calls Qt's 'const QMetaObject
    *QDesignerPropertyEditorInterface::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerpropertyeditorinterface.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QDesignerPropertyEditorInterface::metaObject()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK32QDesignerPropertyEditorInterface10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def core(self) -> Optional[QDesignerFormEditorInterface]:
    """
    Calls Qt's 'QDesignerFormEditorInterface
    *QDesignerPropertyEditorInterface::core() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerpropertyeditorinterface.html#core

    Returns
    -------

    Optional[QDesignerFormEditorInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDesignerFormEditorInterface *QDesignerPropertyEditorInterface::core()
    #      const
    ritual = 'ritual_ZNK32QDesignerPropertyEditorInterface4coreEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK32QDesignerPropertyEditorInterface4coreEv'
    address = self.uglySide.call(ritual)
    from . import QDesignerFormEditorInterface
    return QDesignerFormEditorInterface._cuteAt(address)

  def isReadOnly(self) -> bool:
    """
    Calls Qt's 'bool QDesignerPropertyEditorInterface::isReadOnly() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerpropertyeditorinterface.html#isReadOnly
    """
    #  bool QDesignerPropertyEditorInterface::isReadOnly() const
    return self.uglySide.call(
        'ritual_ZNK32QDesignerPropertyEditorInterface10isReadOnlyEv',
    )

  def object(self) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QDesignerPropertyEditorInterface::object() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerpropertyeditorinterface.html#object

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QDesignerPropertyEditorInterface::object() const
    address = self.uglySide.call(
        'ritual_ZNK32QDesignerPropertyEditorInterface6objectEv',
    )
    return QObject._cuteAt(address)

  def currentPropertyName(self) -> str:
    """
    Calls Qt's 'QString
    QDesignerPropertyEditorInterface::currentPropertyName() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerpropertyeditorinterface.html

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDesignerPropertyEditorInterface::currentPropertyName() const
    return self.uglySide.call(
        'ritual_ZNK32QDesignerPropertyEditorInterface19currentPropertyNameE'
        'v',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QObject)
  @overload(NoneType)
  def setObject(self, object: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QDesignerPropertyEditorInterface::setObject(QObject
    *object)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerpropertyeditorinterface.html#setObject

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDesignerPropertyEditorInterface::setObject(QObject *object)
    self.uglySide.call(
        'ritual_ZN32QDesignerPropertyEditorInterface9setObjectEP7QObject',
        self._addressOf(object, 'QObject'),
    )

  @overload(str, QVariant)
  @overload(str, QVariant, bool)
  def setPropertyValue(
      self,
      name: str,
      value: QVariant,
      changed: bool = True,
  ) -> None:
    """
    Calls Qt's 'void QDesignerPropertyEditorInterface::setPropertyValue(const
    QString &name, const QVariant &value, bool changed)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerpropertyeditorinterface.html

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    changed : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QDesignerPropertyEditorInterface::setPropertyValue(const QString
    #      &name, const QVariant &value, bool changed)
    self.uglySide.call(
        'ritual_ZN32QDesignerPropertyEditorInterface16setPropertyValueERK7Q'
        'StringRK8QVariantb',
        name, self._valueOf(value), changed,
    )

  @overload(bool)
  def setReadOnly(self, readOnly: bool) -> None:
    """
    Calls Qt's 'void QDesignerPropertyEditorInterface::setReadOnly(bool
    readOnly)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerpropertyeditorinterface.html#setReadOnly

    Parameters
    ----------

    readOnly : bool
      Passed on as it is.
    """
    #  void QDesignerPropertyEditorInterface::setReadOnly(bool readOnly)
    self.uglySide.call(
        'ritual_ZN32QDesignerPropertyEditorInterface11setReadOnlyEb',
        readOnly,
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

  @overload(QWidget)
  @overload(NoneType)
  @overload(QWidget, Qt.WindowFlags)
  @overload(NoneType, Qt.WindowFlags)
  def __init__(
      self,
      parent: Optional[QWidget],
      flags: Qt.WindowFlags = Qt.WindowFlags(),
  ) -> None:
    """
    Notes what was given, for Qt's
    'QDesignerPropertyEditorInterface::QDesignerPropertyEditorInterface(
    QWidget *parent, Qt::WindowFlags flags)', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerpropertyeditorinterface.html

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    flags : Qt.WindowFlags
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.WindowFlags().
    """
    #  QDesignerPropertyEditorInterface::
    #      QDesignerPropertyEditorInterface(QWidget *parent, Qt::WindowFlags
    #      flags)
    self._noteCreation(
        QDesignerPropertyEditorInterface, lambda: Rituals.call(
            'ritual_ZN32QDesignerPropertyEditorInterfaceC1EP7QWidget6QFlags'
            'IN2Qt10WindowTypeEE',
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

  @overload(str, QVariant)
  def propertyChanged(self, name: str, value: QVariant) -> None:
    """
    Calls Qt's 'void QDesignerPropertyEditorInterface::propertyChanged(const
    QString &name, const QVariant &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerpropertyeditorinterface.html

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QDesignerPropertyEditorInterface::propertyChanged(const QString
    #      &name, const QVariant &value)
    self.uglySide.call(
        'ritual_ZN32QDesignerPropertyEditorInterface15propertyChangedERK7QS'
        'tringRK8QVariant',
        name, self._valueOf(value),
    )
