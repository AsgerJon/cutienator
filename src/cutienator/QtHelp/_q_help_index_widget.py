"""
QHelpIndexWidget binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtHelp/qhelpindexwidget.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList
from ..QtWidgets import QListView

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QModelIndex, QUrl
  from . import QHelpLink
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QHelpLink = WAIT['QHelpLink']
  QModelIndex = WAIT['QModelIndex']
  QUrl = WAIT['QUrl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QHelpIndexWidget(QListView):
  """
  The cute side of Qt's QHelpIndexWidget: a plain Python object standing in
  front of one C++ QHelpIndexWidget.

  It is built on the cute 'QListView', as Qt's QHelpIndexWidget is built on
  Qt's QListView, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QHelpIndexWidget that has a ritual and that Python
  can call so far, 8 names in all: 'metaObject', 'tr', 'linkActivated',
  'documentActivated', 'documentsActivated', 'filterIndices',
  'activateCurrentItem', 'showLink'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QHelpIndexWidget::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QHelpIndexWidget::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'void QHelpIndexWidget::linksActivated(const QMultiMap<QString,
    QUrl> &links, const QString &keyword)': takes a type Python has no way to
    hand over yet.

  What has no ritual
  ------------------

  2 of the 14 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QHelpIndexWidget is created at the first use, not by
    'QHelpIndexWidget(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QHelpIndexWidget.
  - Qt tells when it has removed the C++ QHelpIndexWidget. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QHelpIndexWidget that has no cute function yet,
    'linksActivated', holds a function that raises 'NotImplementedError', and
    its docstring says why.
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
    Calls Qt's 'QString QHelpIndexWidget::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qhelpindexwidget.html#tr

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
    #  QString QHelpIndexWidget::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN16QHelpIndexWidget2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QHelpIndexWidget'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QHelpIndexWidget::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhelpindexwidget.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QHelpIndexWidget::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK16QHelpIndexWidget10metaObjectEv',
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
    Notes what was given, for Qt's 'QHelpIndexWidget::QHelpIndexWidget()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpindexwidget.html#QHelpIndexWidget
    """
    #  QHelpIndexWidget::QHelpIndexWidget()
    self._noteCreation(QHelpIndexWidget, lambda: Rituals.call(
        'ritual_ZN16QHelpIndexWidgetC1Ev',
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

  @overload(QUrl, str)
  def linkActivated(self, link: QUrl, keyword: str) -> None:
    """
    Calls Qt's 'void QHelpIndexWidget::linkActivated(const QUrl &link, const
    QString &keyword)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpindexwidget.html#linkActivated

    Parameters
    ----------

    link : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    keyword : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QHelpIndexWidget::linkActivated(const QUrl &link, const QString
    #      &keyword)
    self.uglySide.call(
        'ritual_ZN16QHelpIndexWidget13linkActivatedERK4QUrlRK7QString',
        self._valueOf(link), keyword,
    )

  @overload(QHelpLink, str)
  def documentActivated(self, document: QHelpLink, keyword: str) -> None:
    """
    Calls Qt's 'void QHelpIndexWidget::documentActivated(const QHelpLink
    &document, const QString &keyword)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpindexwidget.html#documentActivated

    Parameters
    ----------

    document : QHelpLink
      Passed on as a value: Qt reads the C++ QHelpLink, which stays Python's
      own.

    keyword : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QHelpIndexWidget::documentActivated(const QHelpLink &document,
    #      const QString &keyword)
    self.uglySide.call(
        'ritual_ZN16QHelpIndexWidget17documentActivatedERK9QHelpLinkRK7QStr'
        'ing',
        self._valueOf(document), keyword,
    )

  @overload(QList[QHelpLink], str)
  def documentsActivated(
      self,
      documents: QList[QHelpLink],
      keyword: str,
  ) -> None:
    """
    Calls Qt's 'void QHelpIndexWidget::documentsActivated(const
    QList<QHelpLink> &documents, const QString &keyword)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpindexwidget.html#documentsActivated

    Parameters
    ----------

    documents : QList[QHelpLink]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    keyword : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QHelpIndexWidget::documentsActivated(const QList<QHelpLink>
    #      &documents, const QString &keyword)
    self.uglySide.call(
        'ritual_ZN16QHelpIndexWidget18documentsActivatedERK5QListI9QHelpLin'
        'kERK7QString',
        self._valueOf(documents), keyword,
    )

  @overload(str)
  @overload(str, str)
  def filterIndices(self, filter: str, wildcard: str = '') -> None:
    """
    Calls Qt's 'void QHelpIndexWidget::filterIndices(const QString &filter,
    const QString &wildcard)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpindexwidget.html#filterIndices

    Parameters
    ----------

    filter : str
      Passed on as it is: a QString is made of it for the call.

    wildcard : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.
    """
    #  void QHelpIndexWidget::filterIndices(const QString &filter, const
    #      QString &wildcard)
    self.uglySide.call(
        'ritual_ZN16QHelpIndexWidget13filterIndicesERK7QStringS2_',
        filter, wildcard,
    )

  def activateCurrentItem(self) -> None:
    """
    Calls Qt's 'void QHelpIndexWidget::activateCurrentItem()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpindexwidget.html#activateCurrentItem
    """
    #  void QHelpIndexWidget::activateCurrentItem()
    self.uglySide.call('ritual_ZN16QHelpIndexWidget19activateCurrentItemEv')

  @overload(QModelIndex)
  def showLink(self, index: QModelIndex) -> None:
    """
    Calls Qt's 'void QHelpIndexWidget::showLink(const QModelIndex &index)'.

    Qt's own words: https://doc.qt.io/qt-6/qhelpindexwidget.html#showLink

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  void QHelpIndexWidget::showLink(const QModelIndex &index)
    self.uglySide.call(
        'ritual_ZN16QHelpIndexWidget8showLinkERK11QModelIndex',
        self._valueOf(index),
    )

  @staticmethod
  def linksActivated(*__, **_) -> Never:
    """
    Qt's 'void QHelpIndexWidget::linksActivated(const QMultiMap<QString,
    QUrl> &links, const QString &keyword)': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QHelpIndexWidget.linksActivated' has no cute function yet. Qt's "
        "'void QHelpIndexWidget::linksActivated(const QMultiMap<QString, "
        "QUrl> &links, const QString &keyword)': takes a type Python has no "
        "way to hand over yet.")
