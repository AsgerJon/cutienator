"""
QQmlDelegateChooser binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlModels/6.12.0/QtQmlModels/private/qqmldelegatecomponent_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQmlDelegateChooser to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtQml import QQmlComponent
from . import QQmlAbstractDelegateComponent

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from . import QQmlAdaptorModel
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQmlAdaptorModel = WAIT['QQmlAdaptorModel']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlDelegateChooser(QQmlAbstractDelegateComponent):
  """
  The cute side of Qt's QQmlDelegateChooser: a plain Python object standing
  in front of one C++ QQmlDelegateChooser.

  It is built on the cute 'QQmlAbstractDelegateComponent', as Qt's
  QQmlDelegateChooser is built on Qt's QQmlAbstractDelegateComponent, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QQmlDelegateChooser that has a ritual and that
  Python can call so far, 6 names in all: 'metaObject', 'tr', 'role',
  'setRole', 'delegate', 'roleChanged'. None can be made from Python: one
  comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQmlDelegateChooser::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQmlDelegateChooser::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QQmlListProperty<QQmlDelegateChoice>
    QQmlDelegateChooser::choices()': gives a type Python has no way to take
    yet.
  - Qt's 'void
    QQmlDelegateChooser::choices_append(QQmlListProperty<QQmlDelegateChoice>
    *a0, QQmlDelegateChoice *a1)': names
    'QQmlListProperty<QQmlDelegateChoice>', which has no cute class yet.
  - Qt's 'qsizetype
    QQmlDelegateChooser::choices_count(QQmlListProperty<QQmlDelegateChoice>
    *a0)': names 'QQmlListProperty<QQmlDelegateChoice>', which has no cute
    class yet.
  - Qt's 'QQmlDelegateChoice
    *QQmlDelegateChooser::choices_at(QQmlListProperty<QQmlDelegateChoice>
    *a0, qsizetype a1)': names 'QQmlListProperty<QQmlDelegateChoice>', which
    has no cute class yet.
  - Qt's 'void
    QQmlDelegateChooser::choices_clear(QQmlListProperty<QQmlDelegateChoice>
    *a0)': names 'QQmlListProperty<QQmlDelegateChoice>', which has no cute
    class yet.
  - Qt's 'void
    QQmlDelegateChooser::choices_replace(QQmlListProperty<QQmlDelegateChoice>
    *a0, qsizetype a1, QQmlDelegateChoice *a2)': names
    'QQmlListProperty<QQmlDelegateChoice>', which has no cute class yet.
  - Qt's 'void QQmlDelegateChooser::choices_removeLast(
    QQmlListProperty<QQmlDelegateChoice> *a0)': names
    'QQmlListProperty<QQmlDelegateChoice>', which has no cute class yet.

  What has no ritual
  ------------------

  2 of the 17 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQmlDelegateChooser is created at the first use, not by
    'QQmlDelegateChooser(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlDelegateChooser.
  - Qt tells when it has removed the C++ QQmlDelegateChooser. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQmlDelegateChooser that has no cute function yet,
    'choices', 'choices_append', 'choices_at', 'choices_clear',
    'choices_count', 'choices_removeLast', 'choices_replace', holds a
    function that raises 'NotImplementedError', and its docstring says why.
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
    Calls Qt's 'QString QQmlDelegateChooser::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldelegatechooser.html#tr

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
    #  QString QQmlDelegateChooser::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN19QQmlDelegateChooser2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlDelegateChooser'

  #  The functions Qt calls itself that QQmlDelegateChooser is the first to
  #  declare and that cannot be handed to Python yet, each as Qt declares it.
  #  A class of a program that writes one of them anew is refused, since Qt
  #  would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'choices': (
          'QQmlListProperty<QQmlDelegateChoice> '
          'QQmlDelegateChooser::choices()',
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
    Calls Qt's 'const QMetaObject *QQmlDelegateChooser::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatechooser.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQmlDelegateChooser::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK19QQmlDelegateChooser10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def role(self) -> str:
    """
    Calls Qt's 'QString QQmlDelegateChooser::role() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldelegatechooser.html#role

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlDelegateChooser::role() const
    return self.uglySide.call('ritual_ZNK19QQmlDelegateChooser4roleEv')

  @overload(QQmlAdaptorModel, int)
  @overload(NoneType, int)
  @overload(QQmlAdaptorModel, int, int)
  @overload(NoneType, int, int)
  def delegate(
      self,
      adaptorModel: Optional[QQmlAdaptorModel],
      row: int,
      column: int = -1,
  ) -> Optional[QQmlComponent]:
    """
    Calls Qt's 'QQmlComponent *QQmlDelegateChooser::delegate(QQmlAdaptorModel
    *adaptorModel, int row, int column) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldelegatechooser.html#delegate

    Parameters
    ----------

    adaptorModel : Optional[QQmlAdaptorModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    row : int
      Passed on as it is.

    column : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    Optional[QQmlComponent]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlComponent *QQmlDelegateChooser::delegate(QQmlAdaptorModel
    #      *adaptorModel, int row, int column) const
    ritual = 'ritual_ZNK19QQmlDelegateChooser8delegateEP16QQmlAdaptorModelii'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK19QQmlDelegateChooser8delegateEP16QQmlAdaptorModel'
          'ii')
    address = self.uglySide.call(
        ritual, self._addressOf(adaptorModel), row, column,
    )
    return QQmlComponent._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setRole(self, role: str) -> None:
    """
    Calls Qt's 'void QQmlDelegateChooser::setRole(const QString &role)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldelegatechooser.html#setRole

    Parameters
    ----------

    role : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQmlDelegateChooser::setRole(const QString &role)
    self.uglySide.call(
        'ritual_ZN19QQmlDelegateChooser7setRoleERK7QString', role,
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

  def roleChanged(self) -> None:
    """
    Calls Qt's 'void QQmlDelegateChooser::roleChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatechooser.html#roleChanged
    """
    #  void QQmlDelegateChooser::roleChanged()
    self.uglySide.call('ritual_ZN19QQmlDelegateChooser11roleChangedEv')

  @staticmethod
  def choices(*__, **_) -> Never:
    """
    Qt's 'QQmlListProperty<QQmlDelegateChoice>
    QQmlDelegateChooser::choices()': gives a type Python has no way to take
    yet.
    """
    raise NotImplementedError(
        "'QQmlDelegateChooser.choices' has no cute function yet. Qt's "
        "'QQmlListProperty<QQmlDelegateChoice> "
        "QQmlDelegateChooser::choices()': gives a type Python has no way to "
        "take yet.")

  @staticmethod
  def choices_append(*__, **_) -> Never:
    """
    Qt's 'void
    QQmlDelegateChooser::choices_append(QQmlListProperty<QQmlDelegateChoice>
    *a0, QQmlDelegateChoice *a1)': names
    'QQmlListProperty<QQmlDelegateChoice>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQmlDelegateChooser.choices_append' has no cute function yet. "
        "Qt's 'void "
        "QQmlDelegateChooser::choices_append(QQmlListProperty<QQmlDelegateCh"
        "oice> *a0, QQmlDelegateChoice *a1)': names "
        "'QQmlListProperty<QQmlDelegateChoice>', which has no cute class "
        "yet.")

  @staticmethod
  def choices_at(*__, **_) -> Never:
    """
    Qt's 'QQmlDelegateChoice
    *QQmlDelegateChooser::choices_at(QQmlListProperty<QQmlDelegateChoice>
    *a0, qsizetype a1)': names 'QQmlListProperty<QQmlDelegateChoice>', which
    has no cute class yet.
    """
    raise NotImplementedError(
        "'QQmlDelegateChooser.choices_at' has no cute function yet. Qt's "
        "'QQmlDelegateChoice "
        "*QQmlDelegateChooser::choices_at(QQmlListProperty<QQmlDelegateChoic"
        "e> *a0, qsizetype a1)': names "
        "'QQmlListProperty<QQmlDelegateChoice>', which has no cute class "
        "yet.")

  @staticmethod
  def choices_clear(*__, **_) -> Never:
    """
    Qt's 'void
    QQmlDelegateChooser::choices_clear(QQmlListProperty<QQmlDelegateChoice>
    *a0)': names 'QQmlListProperty<QQmlDelegateChoice>', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QQmlDelegateChooser.choices_clear' has no cute function yet. Qt's "
        "'void "
        "QQmlDelegateChooser::choices_clear(QQmlListProperty<QQmlDelegateCho"
        "ice> *a0)': names 'QQmlListProperty<QQmlDelegateChoice>', which "
        "has no cute class yet.")

  @staticmethod
  def choices_count(*__, **_) -> Never:
    """
    Qt's 'qsizetype
    QQmlDelegateChooser::choices_count(QQmlListProperty<QQmlDelegateChoice>
    *a0)': names 'QQmlListProperty<QQmlDelegateChoice>', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QQmlDelegateChooser.choices_count' has no cute function yet. Qt's "
        "'qsizetype "
        "QQmlDelegateChooser::choices_count(QQmlListProperty<QQmlDelegateCho"
        "ice> *a0)': names 'QQmlListProperty<QQmlDelegateChoice>', which "
        "has no cute class yet.")

  @staticmethod
  def choices_removeLast(*__, **_) -> Never:
    """
    Qt's 'void QQmlDelegateChooser::choices_removeLast(
    QQmlListProperty<QQmlDelegateChoice> *a0)': names
    'QQmlListProperty<QQmlDelegateChoice>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQmlDelegateChooser.choices_removeLast' has no cute function yet. "
        "Qt's 'void "
        "QQmlDelegateChooser::choices_removeLast(QQmlListProperty<QQmlDelega"
        "teChoice> *a0)': names 'QQmlListProperty<QQmlDelegateChoice>', "
        "which has no cute class yet.")

  @staticmethod
  def choices_replace(*__, **_) -> Never:
    """
    Qt's 'void
    QQmlDelegateChooser::choices_replace(QQmlListProperty<QQmlDelegateChoice>
    *a0, qsizetype a1, QQmlDelegateChoice *a2)': names
    'QQmlListProperty<QQmlDelegateChoice>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQmlDelegateChooser.choices_replace' has no cute function yet. "
        "Qt's 'void "
        "QQmlDelegateChooser::choices_replace(QQmlListProperty<QQmlDelegateC"
        "hoice> *a0, qsizetype a1, QQmlDelegateChoice *a2)': names "
        "'QQmlListProperty<QQmlDelegateChoice>', which has no cute class "
        "yet.")
