"""
QGraphicsTransform binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qgraphicstransform.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QMatrix4x4
  from . import QGraphicsTransformPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMatrix4x4 = WAIT['QMatrix4x4']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QGraphicsTransform(QObject):
  """
  The cute side of Qt's QGraphicsTransform: a plain Python object standing in
  front of one C++ QGraphicsTransform.

  It is built on the cute 'QObject', as Qt's QGraphicsTransform is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QGraphicsTransform that has a ritual and that Python
  can call so far, 5 names in all: 'metaObject', 'tr', 'applyTo', 'update',
  'd_func'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QGraphicsTransform::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QGraphicsTransform::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QGraphicsTransform::~QGraphicsTransform()': the destructor: Python
    never removes a C++ QGraphicsTransform.
  - Qt's 'QGraphicsTransform::QGraphicsTransform(QGraphicsTransformPrivate
    &p, QObject *parent)': takes a type Python has no way to hand over yet.
  - Qt's 'const QGraphicsTransformPrivate *QGraphicsTransform::d_func()
    const': takes in Python what 'QGraphicsTransformPrivate
    *QGraphicsTransform::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 13 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QGraphicsTransform is created at the first use, not by
    'QGraphicsTransform(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGraphicsTransform.
  - Qt tells when it has removed the C++ QGraphicsTransform. Every call on
    the cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QGraphicsTransform::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicstransform.html#tr

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
    #  QString QGraphicsTransform::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN18QGraphicsTransform2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGraphicsTransform'

  #  A C++ QGraphicsTransform Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QGraphicsTransform'

  #  The functions Qt calls itself that QGraphicsTransform is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'applyTo': (
          ('_ZNK18QGraphicsTransform7applyToEP10QMatrix4x4',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QMatrix4x4'),
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
    Calls Qt's 'const QMetaObject *QGraphicsTransform::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicstransform.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QGraphicsTransform::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK18QGraphicsTransform10metaObjectEv',
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

  @overload()
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QGraphicsTransform::QGraphicsTransform(QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicstransform.html#QGraphicsTransform

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QGraphicsTransform::QGraphicsTransform(QObject *parent)
    self._noteCreation(QGraphicsTransform, lambda: Rituals.call(
        'ritual_ZN18QGraphicsTransformC1EP7QObject',
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

  @overload(QMatrix4x4)
  @overload(NoneType)
  def applyTo(self, matrix: Optional[QMatrix4x4]) -> None:
    """
    Calls Qt's 'void QGraphicsTransform::applyTo(QMatrix4x4 *matrix) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicstransform.html#applyTo

    Parameters
    ----------

    matrix : Optional[QMatrix4x4]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsTransform::applyTo(QMatrix4x4 *matrix) const
    self.uglySide.call(
        'ritual_ZNK18QGraphicsTransform7applyToEP10QMatrix4x4',
        self._addressOf(matrix),
    )

  def update(self) -> None:
    """
    Calls Qt's 'void QGraphicsTransform::update()'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicstransform.html#update
    """
    #  void QGraphicsTransform::update()
    self.uglySide.call('ritual_ZN18QGraphicsTransform6updateEv')

  def d_func(self) -> Optional[QGraphicsTransformPrivate]:
    """
    Calls Qt's 'QGraphicsTransformPrivate *QGraphicsTransform::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicstransform.html#d_func

    Returns
    -------

    Optional[QGraphicsTransformPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGraphicsTransformPrivate *QGraphicsTransform::d_func()
    address = self.uglySide.call('ritual_ZN18QGraphicsTransform6d_funcEv')
    from . import QGraphicsTransformPrivate
    return QGraphicsTransformPrivate._cuteAt(address)


#  Qt's 'QList<QGraphicsTransform *>': the list of QGraphicsTransform, which
#  'QList[QGraphicsTransform]' gives. It is made here, so that there is one
#  as soon as there can be a QGraphicsTransform.
QList.createKind(
    QGraphicsTransform, 'address',
    make='ritual_list_make_QGraphicsTransform_ptr',
    add='ritual_list_add_QGraphicsTransform_ptr',
    size='ritual_list_size_QGraphicsTransform_ptr',
    at='ritual_list_at_QGraphicsTransform_ptr',
    drop='ritual_list_drop_QGraphicsTransform_ptr',
)
