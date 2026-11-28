"""
QPdfLinkModel binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtPdf/qpdflinkmodel.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QAbstractListModel, QHash, QObject
from . import QPdfDocument

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QByteArray, QMetaObject, QModelIndex, QPointF
  from ..QtCore import QVariant
  from . import QPdfLink, QPdfLinkModelPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QModelIndex = WAIT['QModelIndex']
  QPointF = WAIT['QPointF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPdfLinkModel(QAbstractListModel):
  """
  The cute side of Qt's QPdfLinkModel: a plain Python object standing in
  front of one C++ QPdfLinkModel.

  It is built on the cute 'QAbstractListModel', as Qt's QPdfLinkModel is
  built on Qt's QAbstractListModel, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QPdfLinkModel that has a ritual and that Python can
  call so far, 14 names in all: 'metaObject', 'tr', 'document', 'roleNames',
  'rowCount', 'data', 'page', 'linkAt', 'setDocument', 'setPage',
  'documentChanged', 'pageChanged', 'onStatusChanged', 'd_func'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QPdfLinkModel::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QPdfLinkModel::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QPdfLinkModel::~QPdfLinkModel()': the destructor: Python never
    removes a C++ QPdfLinkModel.
  - Qt's 'const QPdfLinkModelPrivate *QPdfLinkModel::d_func() const': takes
    in Python what 'QPdfLinkModelPrivate *QPdfLinkModel::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 21 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QPdfLinkModel is created at the first use, not by
    'QPdfLinkModel(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QPdfLinkModel.
  - Qt tells when it has removed the C++ QPdfLinkModel. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QPdfLinkModel, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class Role(CuteNum, scoped=True):
    """
    The enum 'QPdfLinkModel::Role' of Qt, with the 7 names Qt gives in it.
    C++ keeps these names inside the enum, so the class that holds the enum
    does not have them.
    """

    Link = Kee[int](256)
    Rectangle = Kee[int](257)
    Url = Kee[int](258)
    Page = Kee[int](259)
    Location = Kee[int](260)
    Zoom = Kee[int](261)
    NRoles = Kee[int](262)

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
    Calls Qt's 'QString QPdfLinkModel::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qpdflinkmodel.html#tr

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
    #  QString QPdfLinkModel::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN13QPdfLinkModel2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPdfLinkModel'

  #  A C++ QPdfLinkModel Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QPdfLinkModel'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QPdfLinkModel::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpdflinkmodel.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QPdfLinkModel::metaObject() const
    address = self.uglySide.call('ritual_ZNK13QPdfLinkModel10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def document(self) -> Optional[QPdfDocument]:
    """
    Calls Qt's 'QPdfDocument *QPdfLinkModel::document() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpdflinkmodel.html#document

    Returns
    -------

    Optional[QPdfDocument]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPdfDocument *QPdfLinkModel::document() const
    address = self.uglySide.call('ritual_ZNK13QPdfLinkModel8documentEv')
    return QPdfDocument._cuteAt(address)

  def roleNames(self) -> QHash[int, QByteArray]:
    """
    Calls Qt's 'QHash<int, QByteArray> QPdfLinkModel::roleNames() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpdflinkmodel.html#roleNames

    Returns
    -------

    QHash[int, QByteArray]
      A new cute map around the copy Qt gave back. Python owns it.
    """
    #  QHash<int, QByteArray> QPdfLinkModel::roleNames() const
    address = self.uglySide.call('ritual_ZNK13QPdfLinkModel9roleNamesEv')
    from ..QtCore import QByteArray
    return QHash[int, QByteArray]._cuteOwning(address)

  @overload(QModelIndex)
  def rowCount(self, parent: QModelIndex) -> int:
    """
    Calls Qt's 'int QPdfLinkModel::rowCount(const QModelIndex &parent)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qpdflinkmodel.html#rowCount

    Parameters
    ----------

    parent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  int QPdfLinkModel::rowCount(const QModelIndex &parent) const
    ritual = 'ritual_ZNK13QPdfLinkModel8rowCountERK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK13QPdfLinkModel8rowCountERK11QModelIndex'
    return self.uglySide.call(ritual, self._valueOf(parent))

  @overload(QModelIndex, int)
  def data(self, index: QModelIndex, role: int) -> QVariant:
    """
    Calls Qt's 'QVariant QPdfLinkModel::data(const QModelIndex &index, int
    role) const'.

    Qt's own words: https://doc.qt.io/qt-6/qpdflinkmodel.html#data

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    role : int
      Passed on as it is.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QPdfLinkModel::data(const QModelIndex &index, int role) const
    ritual = 'ritual_ZNK13QPdfLinkModel4dataERK11QModelIndexi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK13QPdfLinkModel4dataERK11QModelIndexi'
    address = self.uglySide.call(ritual, self._valueOf(index), role)
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def page(self) -> int:
    """
    Calls Qt's 'int QPdfLinkModel::page() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpdflinkmodel.html#page
    """
    #  int QPdfLinkModel::page() const
    return self.uglySide.call('ritual_ZNK13QPdfLinkModel4pageEv')

  @overload(QPointF)
  def linkAt(self, point: QPointF) -> QPdfLink:
    """
    Calls Qt's 'QPdfLink QPdfLinkModel::linkAt(QPointF point) const'.

    Qt's own words: https://doc.qt.io/qt-6/qpdflinkmodel.html#linkAt

    Parameters
    ----------

    point : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    Returns
    -------

    QPdfLink
      A new cute QPdfLink around the copy Qt gave back. Python owns it.
    """
    #  QPdfLink QPdfLinkModel::linkAt(QPointF point) const
    address = self.uglySide.call(
        'ritual_ZNK13QPdfLinkModel6linkAtE7QPointF',
        self._valueOf(point, 'QPointF'),
    )
    from . import QPdfLink
    return QPdfLink._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QPdfDocument)
  @overload(NoneType)
  def setDocument(self, document: Optional[QPdfDocument]) -> None:
    """
    Calls Qt's 'void QPdfLinkModel::setDocument(QPdfDocument *document)'.

    Qt's own words: https://doc.qt.io/qt-6/qpdflinkmodel.html#setDocument

    Parameters
    ----------

    document : Optional[QPdfDocument]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPdfLinkModel::setDocument(QPdfDocument *document)
    self.uglySide.call(
        'ritual_ZN13QPdfLinkModel11setDocumentEP12QPdfDocument',
        self._addressOf(document),
    )

  @overload(int)
  def setPage(self, page: int) -> None:
    """
    Calls Qt's 'void QPdfLinkModel::setPage(int page)'.

    Qt's own words: https://doc.qt.io/qt-6/qpdflinkmodel.html#setPage

    Parameters
    ----------

    page : int
      Passed on as it is.
    """
    #  void QPdfLinkModel::setPage(int page)
    self.uglySide.call('ritual_ZN13QPdfLinkModel7setPageEi', page)

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
    Notes what was given, for Qt's 'QPdfLinkModel::QPdfLinkModel(QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qpdflinkmodel.html#QPdfLinkModel

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QPdfLinkModel::QPdfLinkModel(QObject *parent)
    self._noteCreation(QPdfLinkModel, lambda: Rituals.call(
        'ritual_ZN13QPdfLinkModelC1EP7QObject',
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

  def documentChanged(self) -> None:
    """
    Calls Qt's 'void QPdfLinkModel::documentChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qpdflinkmodel.html#documentChanged
    """
    #  void QPdfLinkModel::documentChanged()
    self.uglySide.call('ritual_ZN13QPdfLinkModel15documentChangedEv')

  @overload(int)
  def pageChanged(self, page: int) -> None:
    """
    Calls Qt's 'void QPdfLinkModel::pageChanged(int page)'.

    Qt's own words: https://doc.qt.io/qt-6/qpdflinkmodel.html#pageChanged

    Parameters
    ----------

    page : int
      Passed on as it is.
    """
    #  void QPdfLinkModel::pageChanged(int page)
    self.uglySide.call('ritual_ZN13QPdfLinkModel11pageChangedEi', page)

  @overload(QPdfDocument.Status)
  def onStatusChanged(self, status: QPdfDocument.Status) -> None:
    """
    Calls Qt's 'void QPdfLinkModel::onStatusChanged(QPdfDocument::Status
    status)'.

    Qt's own words: https://doc.qt.io/qt-6/qpdflinkmodel.html#onStatusChanged

    Parameters
    ----------

    status : QPdfDocument.Status
      Passed on as its number.
    """
    #  void QPdfLinkModel::onStatusChanged(QPdfDocument::Status status)
    self.uglySide.call(
        'ritual_ZN13QPdfLinkModel15onStatusChangedEN12QPdfDocument6StatusE',
        status.value,
    )

  def d_func(self) -> Optional[QPdfLinkModelPrivate]:
    """
    Calls Qt's 'QPdfLinkModelPrivate *QPdfLinkModel::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qpdflinkmodel.html#d_func

    Returns
    -------

    Optional[QPdfLinkModelPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPdfLinkModelPrivate *QPdfLinkModel::d_func()
    address = self.uglySide.call('ritual_ZN13QPdfLinkModel6d_funcEv')
    from . import QPdfLinkModelPrivate
    return QPdfLinkModelPrivate._cuteAt(address)
