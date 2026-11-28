"""
QWebEngineFrame binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWebEngineCore/qwebengineframe.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QSizeF, QUrl
  from ..QtQml import QJSValue
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QJSValue = WAIT['QJSValue']


class QWebEngineFrame(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QWebEngineFrame: a plain Python object standing in
  front of one C++ QWebEngineFrame.

  C++ hands a QWebEngineFrame around as a copy, so every C++ QWebEngineFrame
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QWebEngineFrame that has a ritual and that Python
  can call so far, 11 names in all: 'isValid', 'name', 'htmlName',
  'children', 'url', 'size', 'isMainFrame', 'runJavaScript', 'printToPdf',
  '__eq__', '__ne__'. It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QWebEngineFrame &QWebEngineFrame::operator=(const QWebEngineFrame
    &other)': assignment: Python binds a name and has no operator for it.
  - Qt's 'QWebEngineFrame::QWebEngineFrame(QWebEngineFrame &&other)': takes a
    type Python has no way to hand over yet.
  - Qt's 'QWebEngineFrame &QWebEngineFrame::operator=(QWebEngineFrame
    &&other)': assignment: Python binds a name and has no operator for it.
  - Qt's 'QWebEngineFrame::~QWebEngineFrame()': the destructor: Python
    removes its C++ QWebEngineFrame by it, and has no other use for it.
  - Qt's 'void QWebEngineFrame::printToPdf(const std::function<void (const
    QByteArray &)> &callback)': takes a type Python has no way to hand over
    yet.
  - Qt's 'void QWebEngineFrame::runJavaScriptImpl(const QString
    &scriptSource, quint32 worldId, QtPrivate::QSlotObjectBase *callback)':
    names 'QtPrivate::QSlotObjectBase', which has no cute class yet.
  - Qt's 'QWebEngineFrame::QWebEngineFrame(QWeakPointer<QtWebEngineCore::
    WebContentsAdapter> adapter, quint64 id)': takes a type Python has no way
    to hand over yet.

  What has no ritual
  ------------------

  5 of the 28 functions Qt declares: 3 not a gap; 2 a template.

  What to expect
  --------------

  - The C++ QWebEngineFrame is created at the first use, not by
    'QWebEngineFrame(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QWebEngineFrame back gives a copy the ritual made for
    Python, in a new cute QWebEngineFrame.
  - Each name of Qt's QWebEngineFrame that has no cute function yet,
    'runJavaScriptImpl', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWebEngineFrame'

  #  Qt's '~QWebEngineFrame()'. Naming it makes this a value class: Python
  #  owns every C++ QWebEngineFrame behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN15QWebEngineFrameD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QWebEngineFrame::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebengineframe.html#isValid
    """
    #  bool QWebEngineFrame::isValid() const
    return self.uglySide.call('ritual_ZNK15QWebEngineFrame7isValidEv')

  def name(self) -> str:
    """
    Calls Qt's 'QString QWebEngineFrame::name() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebengineframe.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWebEngineFrame::name() const
    return self.uglySide.call('ritual_ZNK15QWebEngineFrame4nameEv')

  def htmlName(self) -> str:
    """
    Calls Qt's 'QString QWebEngineFrame::htmlName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebengineframe.html#htmlName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWebEngineFrame::htmlName() const
    return self.uglySide.call('ritual_ZNK15QWebEngineFrame8htmlNameEv')

  def children(self) -> QList[QWebEngineFrame]:
    """
    Calls Qt's 'QList<QWebEngineFrame> QWebEngineFrame::children() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebengineframe.html#children

    Returns
    -------

    QList[QWebEngineFrame]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QWebEngineFrame> QWebEngineFrame::children() const
    address = self.uglySide.call('ritual_ZNK15QWebEngineFrame8childrenEv')
    return QList[QWebEngineFrame]._cuteOwning(address)

  def url(self) -> QUrl:
    """
    Calls Qt's 'QUrl QWebEngineFrame::url() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebengineframe.html#url

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QWebEngineFrame::url() const
    address = self.uglySide.call('ritual_ZNK15QWebEngineFrame3urlEv')
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def size(self) -> QSizeF:
    """
    Calls Qt's 'QSizeF QWebEngineFrame::size() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebengineframe.html#size

    Returns
    -------

    QSizeF
      A new cute QSizeF around the copy Qt gave back. Python owns it.
    """
    #  QSizeF QWebEngineFrame::size() const
    address = self.uglySide.call('ritual_ZNK15QWebEngineFrame4sizeEv')
    from ..QtCore import QSizeF
    return QSizeF._cuteOwning(address)

  def isMainFrame(self) -> bool:
    """
    Calls Qt's 'bool QWebEngineFrame::isMainFrame() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebengineframe.html#isMainFrame
    """
    #  bool QWebEngineFrame::isMainFrame() const
    return self.uglySide.call('ritual_ZNK15QWebEngineFrame11isMainFrameEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, rhs: QWebEngineFrame) -> bool:
    """
    Calls Qt's 'bool operator==(const QWebEngineFrame &lhs, const
    QWebEngineFrame &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebengineframe.html#operator==

    Parameters
    ----------

    rhs : QWebEngineFrame
      Passed on as a value: Qt reads the C++ QWebEngineFrame, which stays
      Python's own.
    """
    #  bool operator==(const QWebEngineFrame &lhs, const QWebEngineFrame
    #      &rhs)
    return Rituals.call(
        'ritual_ZeqRK15QWebEngineFrameS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __ne__(self, rhs: QWebEngineFrame) -> bool:
    """
    Calls Qt's 'bool operator!=(const QWebEngineFrame &lhs, const
    QWebEngineFrame &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebengineframe.html#operator!=

    Parameters
    ----------

    rhs : QWebEngineFrame
      Passed on as a value: Qt reads the C++ QWebEngineFrame, which stays
      Python's own.
    """
    #  bool operator!=(const QWebEngineFrame &lhs, const QWebEngineFrame
    #      &rhs)
    return Rituals.call(
        'ritual_ZneRK15QWebEngineFrameS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __ne__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QWebEngineFrame::QWebEngineFrame()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineframe.html#QWebEngineFrame
    """
    #  QWebEngineFrame::QWebEngineFrame()
    self._noteCreation(QWebEngineFrame, lambda: Rituals.call(
        'ritual_ZN15QWebEngineFrameC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QWebEngineFrame) -> None:
    """
    Notes what was given, for Qt's 'QWebEngineFrame::QWebEngineFrame(const
    QWebEngineFrame &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineframe.html#QWebEngineFrame

    Parameters
    ----------

    other : QWebEngineFrame
      Passed on as a value: Qt reads the C++ QWebEngineFrame, which stays
      Python's own.
    """
    #  QWebEngineFrame::QWebEngineFrame(const QWebEngineFrame &other)
    self._noteCreation(QWebEngineFrame, lambda: Rituals.call(
        'ritual_ZN15QWebEngineFrameC1ERKS_', self._valueOf(other),
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
  @overload(str, int)
  def runJavaScript(self, script: str, worldId: int = 0) -> None:
    """
    Calls Qt's 'void QWebEngineFrame::runJavaScript(const QString &script,
    quint32 worldId)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebengineframe.html#runJavaScript

    Parameters
    ----------

    script : str
      Passed on as it is: a QString is made of it for the call.

    worldId : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  void QWebEngineFrame::runJavaScript(const QString &script, quint32
    #      worldId)
    self.uglySide.call(
        'ritual_ZN15QWebEngineFrame13runJavaScriptERK7QStringj',
        script, worldId,
    )

  @overload(str, QJSValue)
  def runJavaScript(self, script: str, callback: QJSValue) -> None:
    """
    Calls Qt's 'void QWebEngineFrame::runJavaScript(const QString &script,
    const QJSValue &callback)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebengineframe.html#runJavaScript

    Parameters
    ----------

    script : str
      Passed on as it is: a QString is made of it for the call.

    callback : QJSValue
      Passed on as a value: Qt reads the C++ QJSValue, which stays Python's
      own.
    """
    #  void QWebEngineFrame::runJavaScript(const QString &script, const
    #      QJSValue &callback)
    self.uglySide.call(
        'ritual_ZN15QWebEngineFrame13runJavaScriptERK7QStringRK8QJSValue',
        script, self._valueOf(callback),
    )

  @overload(str, int, QJSValue)
  def runJavaScript(
      self,
      script: str,
      worldId: int,
      callback: QJSValue,
  ) -> None:
    """
    Calls Qt's 'void QWebEngineFrame::runJavaScript(const QString &script,
    quint32 worldId, const QJSValue &callback)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebengineframe.html#runJavaScript

    Parameters
    ----------

    script : str
      Passed on as it is: a QString is made of it for the call.

    worldId : int
      Passed on as it is.

    callback : QJSValue
      Passed on as a value: Qt reads the C++ QJSValue, which stays Python's
      own.
    """
    #  void QWebEngineFrame::runJavaScript(const QString &script, quint32
    #      worldId, const QJSValue &callback)
    self.uglySide.call(
        'ritual_ZN15QWebEngineFrame13runJavaScriptERK7QStringjRK8QJSValue',
        script, worldId, self._valueOf(callback),
    )

  @overload(str)
  def printToPdf(self, filePath: str) -> None:
    """
    Calls Qt's 'void QWebEngineFrame::printToPdf(const QString &filePath)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebengineframe.html#printToPdf

    Parameters
    ----------

    filePath : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QWebEngineFrame::printToPdf(const QString &filePath)
    self.uglySide.call(
        'ritual_ZN15QWebEngineFrame10printToPdfERK7QString', filePath,
    )

  @overload(QJSValue)
  def printToPdf(self, callback: QJSValue) -> None:
    """
    Calls Qt's 'void QWebEngineFrame::printToPdf(const QJSValue &callback)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebengineframe.html#printToPdf

    Parameters
    ----------

    callback : QJSValue
      Passed on as a value: Qt reads the C++ QJSValue, which stays Python's
      own.
    """
    #  void QWebEngineFrame::printToPdf(const QJSValue &callback)
    self.uglySide.call(
        'ritual_ZN15QWebEngineFrame10printToPdfERK8QJSValue',
        self._valueOf(callback),
    )

  @staticmethod
  def runJavaScriptImpl(*__, **_) -> Never:
    """
    Qt's 'void QWebEngineFrame::runJavaScriptImpl(const QString
    &scriptSource, quint32 worldId, QtPrivate::QSlotObjectBase *callback)':
    names 'QtPrivate::QSlotObjectBase', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QWebEngineFrame.runJavaScriptImpl' has no cute function yet. Qt's "
        "'void QWebEngineFrame::runJavaScriptImpl(const QString "
        "&scriptSource, quint32 worldId, QtPrivate::QSlotObjectBase "
        "*callback)': names 'QtPrivate::QSlotObjectBase', which has no cute "
        "class yet.")


#  Qt's 'QList<QWebEngineFrame>': the list of QWebEngineFrame, which
#  'QList[QWebEngineFrame]' gives. It is made here, so that there is one as
#  soon as there can be a QWebEngineFrame.
QList.createKind(
    QWebEngineFrame, 'value',
    make='ritual_list_make_QWebEngineFrame',
    add='ritual_list_add_QWebEngineFrame',
    size='ritual_list_size_QWebEngineFrame',
    at='ritual_list_at_QWebEngineFrame',
    drop='ritual_list_drop_QWebEngineFrame',
)
