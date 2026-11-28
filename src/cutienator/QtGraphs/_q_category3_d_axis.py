"""
QCategory3DAxis binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGraphs/qcategory3daxis.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtCore import QObject, QStringList
from . import QAbstract3DAxis

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from . import QCategory3DAxisPrivate

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QCategory3DAxis(QAbstract3DAxis):
  """
  The cute side of Qt's QCategory3DAxis: a plain Python object standing in
  front of one C++ QCategory3DAxis.

  It is built on the cute 'QAbstract3DAxis', as Qt's QCategory3DAxis is built
  on Qt's QAbstract3DAxis, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QCategory3DAxis that has a ritual and that Python
  can call so far, 7 names in all: 'metaObject', 'tr', 'd_func', 'setLabels',
  'labels', 'rowLabelsChanged', 'columnLabelsChanged'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QCategory3DAxis::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QCategory3DAxis::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'const QCategory3DAxisPrivate *QCategory3DAxis::d_func() const':
    takes in Python what 'QCategory3DAxisPrivate *QCategory3DAxis::d_func()'
    takes.
  - Qt's 'QCategory3DAxis::~QCategory3DAxis()': the destructor: Python never
    removes a C++ QCategory3DAxis.

  What has no ritual
  ------------------

  4 of the 16 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QCategory3DAxis is created at the first use, not by
    'QCategory3DAxis(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QCategory3DAxis.
  - Qt tells when it has removed the C++ QCategory3DAxis. Every call on the
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
    Calls Qt's 'QString QCategory3DAxis::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qcategory3daxis.html#tr

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
    #  QString QCategory3DAxis::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN15QCategory3DAxis2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCategory3DAxis'
  #  The part of Qt it is of, as another part has a class of its name too.
  __qt_part__ = 'QtGraphs'

  #  A C++ QCategory3DAxis Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QCategory3DAxis'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QCategory3DAxis::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcategory3daxis.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QCategory3DAxis::metaObject() const
    address = self.uglySide.call('ritual_ZNK15QCategory3DAxis10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def labels(self) -> QStringList:
    """
    Calls Qt's 'QStringList QCategory3DAxis::labels() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcategory3daxis.html#labels

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QCategory3DAxis::labels() const
    address = self.uglySide.call('ritual_ZNK15QCategory3DAxis6labelsEv')
    return QStringList._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QStringList)
  def setLabels(self, labels: QStringList) -> None:
    """
    Calls Qt's 'void QCategory3DAxis::setLabels(const QStringList &labels)'.

    Qt's own words: https://doc.qt.io/qt-6/qcategory3daxis.html#setLabels

    Parameters
    ----------

    labels : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QCategory3DAxis::setLabels(const QStringList &labels)
    self.uglySide.call(
        'ritual_ZN15QCategory3DAxis9setLabelsERK5QListI7QStringE',
        self._valueOf(labels),
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
    Notes what was given, for Qt's 'QCategory3DAxis::QCategory3DAxis(QObject
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcategory3daxis.html#QCategory3DAxis

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QCategory3DAxis::QCategory3DAxis(QObject *parent)
    self._noteCreation(QCategory3DAxis, lambda: Rituals.call(
        'ritual_ZN15QCategory3DAxisC1EP7QObject',
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

  def d_func(self) -> Optional[QCategory3DAxisPrivate]:
    """
    Calls Qt's 'QCategory3DAxisPrivate *QCategory3DAxis::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qcategory3daxis.html#d_func

    Returns
    -------

    Optional[QCategory3DAxisPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCategory3DAxisPrivate *QCategory3DAxis::d_func()
    address = self.uglySide.call('ritual_ZN15QCategory3DAxis6d_funcEv')
    from . import QCategory3DAxisPrivate
    return QCategory3DAxisPrivate._cuteAt(address)

  def rowLabelsChanged(self) -> None:
    """
    Calls Qt's 'void QCategory3DAxis::rowLabelsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcategory3daxis.html#rowLabelsChanged
    """
    #  void QCategory3DAxis::rowLabelsChanged()
    self.uglySide.call('ritual_ZN15QCategory3DAxis16rowLabelsChangedEv')

  def columnLabelsChanged(self) -> None:
    """
    Calls Qt's 'void QCategory3DAxis::columnLabelsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcategory3daxis.html#columnLabelsChanged
    """
    #  void QCategory3DAxis::columnLabelsChanged()
    self.uglySide.call('ritual_ZN15QCategory3DAxis19columnLabelsChangedEv')
