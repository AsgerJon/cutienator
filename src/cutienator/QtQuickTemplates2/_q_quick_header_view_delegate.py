"""
QQuickHeaderViewDelegate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickheaderviewdelegate_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickHeaderViewDelegate to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt
from ..QtQuick import QQuickItem
from . import QQuickTableViewDelegate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QVariant
  from . import QQuickHeaderViewBase
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickHeaderViewBase = WAIT['QQuickHeaderViewBase']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickHeaderViewDelegate(QQuickTableViewDelegate):
  """
  The cute side of Qt's QQuickHeaderViewDelegate: a plain Python object
  standing in front of one C++ QQuickHeaderViewDelegate.

  It is built on the cute 'QQuickTableViewDelegate', as Qt's
  QQuickHeaderViewDelegate is built on Qt's QQuickTableViewDelegate, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickHeaderViewDelegate that has a ritual and that
  Python can call so far, 10 names in all: 'metaObject', 'tr', 'headerView',
  'setHeaderView', 'orientation', 'model', 'setModel', 'headerViewChanged',
  'modelChanged', 'orientationChanged'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickHeaderViewDelegate::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QQuickHeaderViewDelegate::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickHeaderViewDelegatePrivate
    *QQuickHeaderViewDelegate::d_func()': gives
    'QQuickHeaderViewDelegatePrivate', which has no cute class yet.
  - Qt's 'const QQuickHeaderViewDelegatePrivate
    *QQuickHeaderViewDelegate::d_func() const': gives
    'QQuickHeaderViewDelegatePrivate', which has no cute class yet.

  What has no ritual
  ------------------

  4 of the 19 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickHeaderViewDelegate is created at the first use, not by
    'QQuickHeaderViewDelegate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickHeaderViewDelegate.
  - Qt tells when it has removed the C++ QQuickHeaderViewDelegate. Every call
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
    Calls Qt's 'QString QQuickHeaderViewDelegate::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickheaderviewdelegate.html#tr

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
    #  QString QQuickHeaderViewDelegate::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN24QQuickHeaderViewDelegate2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickHeaderViewDelegate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickHeaderViewDelegate::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickheaderviewdelegate.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickHeaderViewDelegate::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK24QQuickHeaderViewDelegate10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def headerView(self) -> Optional[QQuickHeaderViewBase]:
    """
    Calls Qt's 'QQuickHeaderViewBase *QQuickHeaderViewDelegate::headerView()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickheaderviewdelegate.html#headerView

    Returns
    -------

    Optional[QQuickHeaderViewBase]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickHeaderViewBase *QQuickHeaderViewDelegate::headerView() const
    address = self.uglySide.call(
        'ritual_ZNK24QQuickHeaderViewDelegate10headerViewEv',
    )
    from . import QQuickHeaderViewBase
    return QQuickHeaderViewBase._cuteAt(address)

  def orientation(self) -> Qt.Orientation:
    """
    Calls Qt's 'Qt::Orientation QQuickHeaderViewDelegate::orientation()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickheaderviewdelegate.html#orientation

    Returns
    -------

    Qt.Orientation
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.Orientation(number)'
      gives.
    """
    #  Qt::Orientation QQuickHeaderViewDelegate::orientation() const
    return Qt.Orientation(self.uglySide.call(
        'ritual_ZNK24QQuickHeaderViewDelegate11orientationEv',
    ))

  def model(self) -> QVariant:
    """
    Calls Qt's 'QVariant QQuickHeaderViewDelegate::model() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickheaderviewdelegate.html#model

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QQuickHeaderViewDelegate::model() const
    address = self.uglySide.call(
        'ritual_ZNK24QQuickHeaderViewDelegate5modelEv',
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QQuickHeaderViewBase)
  @overload(NoneType)
  def setHeaderView(
      self,
      headerView: Optional[QQuickHeaderViewBase],
  ) -> None:
    """
    Calls Qt's 'void
    QQuickHeaderViewDelegate::setHeaderView(QQuickHeaderViewBase
    *headerView)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickheaderviewdelegate.html#setHeaderView

    Parameters
    ----------

    headerView : Optional[QQuickHeaderViewBase]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickHeaderViewDelegate::setHeaderView(QQuickHeaderViewBase
    #      *headerView)
    self.uglySide.call(
        'ritual_ZN24QQuickHeaderViewDelegate13setHeaderViewEP20QQuickHeader'
        'ViewBase',
        self._addressOf(headerView),
    )

  @overload(QVariant)
  def setModel(self, model: QVariant) -> None:
    """
    Calls Qt's 'void QQuickHeaderViewDelegate::setModel(const QVariant
    &model)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickheaderviewdelegate.html#setModel

    Parameters
    ----------

    model : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QQuickHeaderViewDelegate::setModel(const QVariant &model)
    self.uglySide.call(
        'ritual_ZN24QQuickHeaderViewDelegate8setModelERK8QVariant',
        self._valueOf(model),
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
  @overload(QQuickItem)
  @overload(NoneType)
  def __init__(self, parent: Optional[QQuickItem] = None) -> None:
    """
    Notes what was given, for Qt's
    'QQuickHeaderViewDelegate::QQuickHeaderViewDelegate(QQuickItem *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickheaderviewdelegate.html

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickHeaderViewDelegate::QQuickHeaderViewDelegate(QQuickItem *parent)
    self._noteCreation(QQuickHeaderViewDelegate, lambda: Rituals.call(
        'ritual_ZN24QQuickHeaderViewDelegateC1EP10QQuickItem',
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

  def headerViewChanged(self) -> None:
    """
    Calls Qt's 'void QQuickHeaderViewDelegate::headerViewChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickheaderviewdelegate.html#headerViewChanged
    """
    #  void QQuickHeaderViewDelegate::headerViewChanged()
    self.uglySide.call(
        'ritual_ZN24QQuickHeaderViewDelegate17headerViewChangedEv',
    )

  def modelChanged(self) -> None:
    """
    Calls Qt's 'void QQuickHeaderViewDelegate::modelChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickheaderviewdelegate.html#modelChanged
    """
    #  void QQuickHeaderViewDelegate::modelChanged()
    self.uglySide.call('ritual_ZN24QQuickHeaderViewDelegate12modelChangedEv')

  def orientationChanged(self) -> None:
    """
    Calls Qt's 'void QQuickHeaderViewDelegate::orientationChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickheaderviewdelegate.html#orientationChanged
    """
    #  void QQuickHeaderViewDelegate::orientationChanged()
    self.uglySide.call(
        'ritual_ZN24QQuickHeaderViewDelegate18orientationChangedEv',
    )
