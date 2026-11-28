"""
QHelpContentWidget binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtHelp/qhelpcontentwidget.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtWidgets import QTreeView

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QModelIndex, QUrl
  from . import QHelpContentModel
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QHelpContentModel = WAIT['QHelpContentModel']
  QModelIndex = WAIT['QModelIndex']
  QUrl = WAIT['QUrl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QHelpContentWidget(QTreeView):
  """
  The cute side of Qt's QHelpContentWidget: a plain Python object standing in
  front of one C++ QHelpContentWidget.

  It is built on the cute 'QTreeView', as Qt's QHelpContentWidget is built on
  Qt's QTreeView, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QHelpContentWidget that has a ritual and that Python
  can call so far, 6 names in all: 'metaObject', 'tr', 'indexOf',
  'linkActivated', 'showLink', 'searchContentItem'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QHelpContentWidget::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QHelpContentWidget::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  2 of the 11 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QHelpContentWidget is created at the first use, not by
    'QHelpContentWidget(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QHelpContentWidget.
  - Qt tells when it has removed the C++ QHelpContentWidget. Every call on
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
    Calls Qt's 'QString QHelpContentWidget::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qhelpcontentwidget.html#tr

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
    #  QString QHelpContentWidget::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN18QHelpContentWidget2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QHelpContentWidget'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QHelpContentWidget::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhelpcontentwidget.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QHelpContentWidget::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK18QHelpContentWidget10metaObjectEv',
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
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QHelpContentWidget::QHelpContentWidget()', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpcontentwidget.html#QHelpContentWidget
    """
    #  QHelpContentWidget::QHelpContentWidget()
    self._noteCreation(QHelpContentWidget, lambda: Rituals.call(
        'ritual_ZN18QHelpContentWidgetC1Ev',
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

  @overload(QUrl)
  def indexOf(self, link: QUrl) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QHelpContentWidget::indexOf(const QUrl &link)'.

    Qt's own words: https://doc.qt.io/qt-6/qhelpcontentwidget.html#indexOf

    Parameters
    ----------

    link : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    Returns
    -------

    QModelIndex
      A new cute QModelIndex around the copy Qt gave back. Python owns it.
    """
    #  QModelIndex QHelpContentWidget::indexOf(const QUrl &link)
    address = self.uglySide.call(
        'ritual_ZN18QHelpContentWidget7indexOfERK4QUrl', self._valueOf(link),
    )
    from ..QtCore import QModelIndex
    return QModelIndex._cuteOwning(address)

  @overload(QUrl)
  def linkActivated(self, link: QUrl) -> None:
    """
    Calls Qt's 'void QHelpContentWidget::linkActivated(const QUrl &link)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpcontentwidget.html#linkActivated

    Parameters
    ----------

    link : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QHelpContentWidget::linkActivated(const QUrl &link)
    self.uglySide.call(
        'ritual_ZN18QHelpContentWidget13linkActivatedERK4QUrl',
        self._valueOf(link),
    )

  @overload(QModelIndex)
  def showLink(self, index: QModelIndex) -> None:
    """
    Calls Qt's 'void QHelpContentWidget::showLink(const QModelIndex &index)'.

    Qt's own words: https://doc.qt.io/qt-6/qhelpcontentwidget.html#showLink

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  void QHelpContentWidget::showLink(const QModelIndex &index)
    self.uglySide.call(
        'ritual_ZN18QHelpContentWidget8showLinkERK11QModelIndex',
        self._valueOf(index),
    )

  @overload(QHelpContentModel, QModelIndex, str)
  @overload(NoneType, QModelIndex, str)
  def searchContentItem(
      self,
      model: Optional[QHelpContentModel],
      parent: QModelIndex,
      path: str,
  ) -> bool:
    """
    Calls Qt's 'bool QHelpContentWidget::searchContentItem(QHelpContentModel
    *model, const QModelIndex &parent, const QString &path)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpcontentwidget.html#searchContentItem

    Parameters
    ----------

    model : Optional[QHelpContentModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    path : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QHelpContentWidget::searchContentItem(QHelpContentModel *model,
    #      const QModelIndex &parent, const QString &path)
    return self.uglySide.call(
        'ritual_ZN18QHelpContentWidget17searchContentItemEP17QHelpContentMo'
        'delRK11QModelIndexRK7QString',
        self._addressOf(model), self._valueOf(parent), path,
    )
