"""
Qt3DRender::QFilterKey binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/qfilterkey.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore
from . import Qt3DRender

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QVariant
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QFilterKey(Qt3DCore.QNode):
  """
  The cute side of Qt's Qt3DRender::QFilterKey: a plain Python object
  standing in front of one C++ Qt3DRender::QFilterKey.

  It is built on the cute 'Qt3DCore::QNode', as Qt's Qt3DRender::QFilterKey
  is built on Qt's Qt3DCore::QNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::QFilterKey that has a ritual and that
  Python can call so far, 9 names in all: 'metaObject', 'tr', 'value',
  'name', 'setValue', 'setName', 'nameChanged', 'valueChanged', 'd_func'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DRender::QFilterKey::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int Qt3DRender::QFilterKey::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DRender::QFilterKey::~QFilterKey()': the destructor: Python
    never removes a C++ Qt3DRender::QFilterKey.
  - Qt's 'const QFilterKeyPrivate *Qt3DRender::QFilterKey::d_func() const':
    takes in Python what 'QFilterKeyPrivate
    *Qt3DRender::QFilterKey::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 16 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DRender::QFilterKey is created at the first use, not by
    'Qt3DRender::QFilterKey(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::QFilterKey.
  - Qt tells when it has removed the C++ Qt3DRender::QFilterKey. Every call
    on the cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString Qt3DRender::QFilterKey::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-qfilterkey.html#tr

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
    #  QString Qt3DRender::QFilterKey::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN10Qt3DRender10QFilterKey2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::QFilterKey'

  #  A C++ Qt3DRender::QFilterKey Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DRender_QFilterKey'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *Qt3DRender::QFilterKey::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qfilterkey.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DRender::QFilterKey::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender10QFilterKey10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def value(self) -> QVariant:
    """
    Calls Qt's 'QVariant Qt3DRender::QFilterKey::value() const'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-qfilterkey.html#value

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant Qt3DRender::QFilterKey::value() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender10QFilterKey5valueEv',
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def name(self) -> str:
    """
    Calls Qt's 'QString Qt3DRender::QFilterKey::name() const'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-qfilterkey.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString Qt3DRender::QFilterKey::name() const
    return self.uglySide.call('ritual_ZNK10Qt3DRender10QFilterKey4nameEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QVariant)
  def setValue(self, value: QVariant) -> None:
    """
    Calls Qt's 'void Qt3DRender::QFilterKey::setValue(const QVariant
    &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qfilterkey.html#setValue

    Parameters
    ----------

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void Qt3DRender::QFilterKey::setValue(const QVariant &value)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender10QFilterKey8setValueERK8QVariant',
        self._valueOf(value),
    )

  @overload(str)
  def setName(self, customType: str) -> None:
    """
    Calls Qt's 'void Qt3DRender::QFilterKey::setName(const QString
    &customType)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-qfilterkey.html#setName

    Parameters
    ----------

    customType : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void Qt3DRender::QFilterKey::setName(const QString &customType)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender10QFilterKey7setNameERK7QString', customType,
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
  @overload(Qt3DCore.QNode)
  @overload(NoneType)
  def __init__(self, parent: Optional[Qt3DCore.QNode] = None) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DRender::QFilterKey::QFilterKey(Qt3DCore::QNode *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qfilterkey.html#QFilterKey

    Parameters
    ----------

    parent : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DRender::QFilterKey::QFilterKey(Qt3DCore::QNode *parent)
    self._noteCreation(QFilterKey, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender10QFilterKeyC1EPN8Qt3DCore5QNodeE',
        self._addressOf(parent),
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
  def nameChanged(self, name: str) -> None:
    """
    Calls Qt's 'void Qt3DRender::QFilterKey::nameChanged(const QString
    &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qfilterkey.html#nameChanged

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void Qt3DRender::QFilterKey::nameChanged(const QString &name)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender10QFilterKey11nameChangedERK7QString', name,
    )

  @overload(QVariant)
  def valueChanged(self, value: QVariant) -> None:
    """
    Calls Qt's 'void Qt3DRender::QFilterKey::valueChanged(const QVariant
    &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qfilterkey.html#valueChanged

    Parameters
    ----------

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void Qt3DRender::QFilterKey::valueChanged(const QVariant &value)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender10QFilterKey12valueChangedERK8QVariant',
        self._valueOf(value),
    )

  def d_func(self) -> Optional[Qt3DRender.QFilterKeyPrivate]:
    """
    Calls Qt's 'QFilterKeyPrivate *Qt3DRender::QFilterKey::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-qfilterkey.html#d_func

    Returns
    -------

    Optional[Qt3DRender.QFilterKeyPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QFilterKeyPrivate *Qt3DRender::QFilterKey::d_func()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DRender10QFilterKey6d_funcEv',
    )
    return Qt3DRender.QFilterKeyPrivate._cuteAt(address)
