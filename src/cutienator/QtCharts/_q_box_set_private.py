"""
QBoxSetPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCharts/6.12.0/QtCharts/private/qboxset_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QBoxSetPrivate to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from . import QBoxSet
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QBoxSet = WAIT['QBoxSet']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QBoxSetPrivate(QObject):
  """
  The cute side of Qt's QBoxSetPrivate: a plain Python object standing in
  front of one C++ QBoxSetPrivate.

  It is built on the cute 'QObject', as Qt's QBoxSetPrivate is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QBoxSetPrivate that has a ritual and that Python can
  call so far, 9 names in all: 'metaObject', 'tr', 'append', 'clear',
  'setValue', 'value', 'restructuredBox', 'updatedBox', 'updatedLayout'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QBoxSetPrivate::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QBoxSetPrivate::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QBoxSetPrivate::~QBoxSetPrivate()': the destructor: Python never
    removes a C++ QBoxSetPrivate.
  - Qt's 'bool QBoxSetPrivate::append(const QList<qreal> &values)': takes a
    type Python has no way to hand over yet.

  What has no ritual
  ------------------

  3 of the 17 functions Qt declares: 2 not a gap; 1 cannot be called and
  cannot be called through the meta-object and cannot be copied.

  What to expect
  --------------

  - The C++ QBoxSetPrivate is created at the first use, not by
    'QBoxSetPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QBoxSetPrivate.
  - Qt tells when it has removed the C++ QBoxSetPrivate. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QBoxSetPrivate that has no cute function yet, 'remove',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
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
    Calls Qt's 'QString QBoxSetPrivate::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qboxsetprivate.html#tr

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
    #  QString QBoxSetPrivate::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN14QBoxSetPrivate2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QBoxSetPrivate'

  #  A C++ QBoxSetPrivate Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QBoxSetPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QBoxSetPrivate::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qboxsetprivate.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QBoxSetPrivate::metaObject() const
    address = self.uglySide.call('ritual_ZNK14QBoxSetPrivate10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int, float)
  def setValue(self, index: int, value: float) -> None:
    """
    Calls Qt's 'void QBoxSetPrivate::setValue(const int index, const qreal
    value)'.

    Qt's own words: https://doc.qt.io/qt-6/qboxsetprivate.html#setValue

    Parameters
    ----------

    index : int
      Passed on as it is.

    value : float
      Passed on as it is.
    """
    #  void QBoxSetPrivate::setValue(const int index, const qreal value)
    self.uglySide.call('ritual_ZN14QBoxSetPrivate8setValueEid', index, value)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str, QBoxSet)
  @overload(str, NoneType)
  def __init__(self, label: str, parent: Optional[QBoxSet]) -> None:
    """
    Notes what was given, for Qt's 'QBoxSetPrivate::QBoxSetPrivate(const
    QString label, QBoxSet *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qboxsetprivate.html#QBoxSetPrivate

    Parameters
    ----------

    label : str
      Passed on as it is: a QString is made of it for the call.

    parent : Optional[QBoxSet]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QBoxSetPrivate::QBoxSetPrivate(const QString label, QBoxSet *parent)
    self._noteCreation(QBoxSetPrivate, lambda: Rituals.call(
        'ritual_ZN14QBoxSetPrivateC1E7QStringP7QBoxSet',
        label, self._addressOf(parent),
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

  @overload(float)
  def append(self, value: float) -> bool:
    """
    Calls Qt's 'bool QBoxSetPrivate::append(qreal value)'.

    Qt's own words: https://doc.qt.io/qt-6/qboxsetprivate.html#append

    Parameters
    ----------

    value : float
      Passed on as it is.
    """
    #  bool QBoxSetPrivate::append(qreal value)
    return self.uglySide.call('ritual_ZN14QBoxSetPrivate6appendEd', value)

  def clear(self) -> None:
    """
    Calls Qt's 'void QBoxSetPrivate::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qboxsetprivate.html#clear
    """
    #  void QBoxSetPrivate::clear()
    self.uglySide.call('ritual_ZN14QBoxSetPrivate5clearEv')

  @overload(int)
  def value(self, index: int) -> float:
    """
    Calls Qt's 'qreal QBoxSetPrivate::value(const int index)'.

    Qt's own words: https://doc.qt.io/qt-6/qboxsetprivate.html#value

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  qreal QBoxSetPrivate::value(const int index)
    return self.uglySide.call('ritual_ZN14QBoxSetPrivate5valueEi', index)

  def restructuredBox(self) -> None:
    """
    Calls Qt's 'void QBoxSetPrivate::restructuredBox()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qboxsetprivate.html#restructuredBox
    """
    #  void QBoxSetPrivate::restructuredBox()
    self.uglySide.call('ritual_ZN14QBoxSetPrivate15restructuredBoxEv')

  def updatedBox(self) -> None:
    """
    Calls Qt's 'void QBoxSetPrivate::updatedBox()'.

    Qt's own words: https://doc.qt.io/qt-6/qboxsetprivate.html#updatedBox
    """
    #  void QBoxSetPrivate::updatedBox()
    self.uglySide.call('ritual_ZN14QBoxSetPrivate10updatedBoxEv')

  def updatedLayout(self) -> None:
    """
    Calls Qt's 'void QBoxSetPrivate::updatedLayout()'.

    Qt's own words: https://doc.qt.io/qt-6/qboxsetprivate.html#updatedLayout
    """
    #  void QBoxSetPrivate::updatedLayout()
    self.uglySide.call('ritual_ZN14QBoxSetPrivate13updatedLayoutEv')

  @staticmethod
  def remove(*__, **_) -> Never:
    """
    Qt's 'int QBoxSetPrivate::remove(const int index, const int count)':
    cannot be called and cannot be called through the meta-object and cannot
    be copied: no header file has its code, Qt's source does not mark it or
    its class for use from outside Qt or writes it 'inline' or nowhere, and
    it is no signal, slot or invokable function giving back nothing, of a
    class built on QObject, and Qt's source has no code for it that could be
    told from the rest.
    """
    raise NotImplementedError(
        "'QBoxSetPrivate.remove' has no cute function yet. Qt's 'int "
        "QBoxSetPrivate::remove(const int index, const int count)': cannot "
        "be called and cannot be called through the meta-object and cannot "
        "be copied: no header file has its code, Qt's source does not mark "
        "it or its class for use from outside Qt or writes it 'inline' or "
        "nowhere, and it is no signal, slot or invokable function giving "
        "back nothing, of a class built on QObject, and Qt's source has no "
        "code for it that could be told from the rest.")
