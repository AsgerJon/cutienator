"""
QWebEngineScript binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWebEngineCore/qwebenginescript.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QUrl
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QUrl = WAIT['QUrl']


class QWebEngineScript(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QWebEngineScript: a plain Python object standing in
  front of one C++ QWebEngineScript.

  C++ hands a QWebEngineScript around as a copy, so every C++
  QWebEngineScript behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QWebEngineScript that has a ritual and that Python
  can call so far, 14 names in all: 'name', 'setName', 'sourceUrl',
  'setSourceUrl', 'sourceCode', 'setSourceCode', 'injectionPoint',
  'setInjectionPoint', 'worldId', 'setWorldId', 'runsOnSubFrames',
  'setRunsOnSubFrames', '__eq__', '__ne__'. It can be made from Python, in 2
  ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QWebEngineScript::~QWebEngineScript()': the destructor: Python
    removes its C++ QWebEngineScript by it, and has no other use for it.
  - Qt's 'QWebEngineScript &QWebEngineScript::operator=(const
    QWebEngineScript &other)': assignment: Python binds a name and has no
    operator for it.
  - Qt's 'void QWebEngineScript::swap(QWebEngineScript &other)': takes a type
    Python has no way to hand over yet.
  - Qt's 'QWebEngineScript::QWebEngineScript(const
    QtWebEngineCore::UserScript &a0)': takes a type Python has no way to hand
    over yet.

  What has no ritual
  ------------------

  3 of the 23 functions Qt declares: 3 not a gap.

  What to expect
  --------------

  - The C++ QWebEngineScript is created at the first use, not by
    'QWebEngineScript(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QWebEngineScript back gives a copy the ritual made
    for Python, in a new cute QWebEngineScript.
  - Each name of Qt's QWebEngineScript that has no cute function yet, 'swap',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  #  The enums Qt writes inside QWebEngineScript, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class InjectionPoint(CuteNum):
    """
    The enum 'QWebEngineScript::InjectionPoint' of Qt, with the 3 names Qt
    gives in it.
    """

    Deferred = Kee[int](0)
    DocumentReady = Kee[int](1)
    DocumentCreation = Kee[int](2)

  class ScriptWorldId(CuteNum):
    """
    The enum 'QWebEngineScript::ScriptWorldId' of Qt, with the 3 names Qt
    gives in it.
    """

    MainWorld = Kee[int](0)
    ApplicationWorld = Kee[int](1)
    UserWorld = Kee[int](2)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWebEngineScript'

  #  Qt's '~QWebEngineScript()'. Naming it makes this a value class: Python
  #  owns every C++ QWebEngineScript behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN16QWebEngineScriptD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def name(self) -> str:
    """
    Calls Qt's 'QString QWebEngineScript::name() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebenginescript.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWebEngineScript::name() const
    return self.uglySide.call('ritual_ZNK16QWebEngineScript4nameEv')

  def sourceUrl(self) -> QUrl:
    """
    Calls Qt's 'QUrl QWebEngineScript::sourceUrl() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebenginescript.html#sourceUrl

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QWebEngineScript::sourceUrl() const
    address = self.uglySide.call('ritual_ZNK16QWebEngineScript9sourceUrlEv')
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def sourceCode(self) -> str:
    """
    Calls Qt's 'QString QWebEngineScript::sourceCode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebenginescript.html#sourceCode

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWebEngineScript::sourceCode() const
    return self.uglySide.call('ritual_ZNK16QWebEngineScript10sourceCodeEv')

  def injectionPoint(self) -> InjectionPoint:
    """
    Calls Qt's 'InjectionPoint QWebEngineScript::injectionPoint() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginescript.html#injectionPoint

    Returns
    -------

    InjectionPoint
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'InjectionPoint(number)'
      gives.
    """
    #  InjectionPoint QWebEngineScript::injectionPoint() const
    return QWebEngineScript.InjectionPoint(self.uglySide.call(
        'ritual_ZNK16QWebEngineScript14injectionPointEv',
    ))

  def worldId(self) -> int:
    """
    Calls Qt's 'quint32 QWebEngineScript::worldId() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebenginescript.html#worldId
    """
    #  quint32 QWebEngineScript::worldId() const
    return self.uglySide.call('ritual_ZNK16QWebEngineScript7worldIdEv')

  def runsOnSubFrames(self) -> bool:
    """
    Calls Qt's 'bool QWebEngineScript::runsOnSubFrames() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginescript.html#runsOnSubFrames
    """
    #  bool QWebEngineScript::runsOnSubFrames() const
    return self.uglySide.call(
        'ritual_ZNK16QWebEngineScript15runsOnSubFramesEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setName(self, a0: str) -> None:
    """
    Calls Qt's 'void QWebEngineScript::setName(const QString &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebenginescript.html#setName

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QWebEngineScript::setName(const QString &a0)
    self.uglySide.call('ritual_ZN16QWebEngineScript7setNameERK7QString', a0)

  @overload(QUrl)
  def setSourceUrl(self, url: QUrl) -> None:
    """
    Calls Qt's 'void QWebEngineScript::setSourceUrl(const QUrl &url)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebenginescript.html#setSourceUrl

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QWebEngineScript::setSourceUrl(const QUrl &url)
    self.uglySide.call(
        'ritual_ZN16QWebEngineScript12setSourceUrlERK4QUrl',
        self._valueOf(url),
    )

  @overload(str)
  def setSourceCode(self, a0: str) -> None:
    """
    Calls Qt's 'void QWebEngineScript::setSourceCode(const QString &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginescript.html#setSourceCode

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QWebEngineScript::setSourceCode(const QString &a0)
    self.uglySide.call(
        'ritual_ZN16QWebEngineScript13setSourceCodeERK7QString', a0,
    )

  @overload(InjectionPoint)
  def setInjectionPoint(self, a0: InjectionPoint) -> None:
    """
    Calls Qt's 'void QWebEngineScript::setInjectionPoint(InjectionPoint a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginescript.html#setInjectionPoint

    Parameters
    ----------

    a0 : InjectionPoint
      Passed on as its number.
    """
    #  void QWebEngineScript::setInjectionPoint(InjectionPoint a0)
    self.uglySide.call(
        'ritual_ZN16QWebEngineScript17setInjectionPointENS_14InjectionPoint'
        'E',
        a0.value,
    )

  @overload(int)
  def setWorldId(self, a0: int) -> None:
    """
    Calls Qt's 'void QWebEngineScript::setWorldId(quint32 a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebenginescript.html#setWorldId

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QWebEngineScript::setWorldId(quint32 a0)
    self.uglySide.call('ritual_ZN16QWebEngineScript10setWorldIdEj', a0)

  @overload(bool)
  def setRunsOnSubFrames(self, on: bool) -> None:
    """
    Calls Qt's 'void QWebEngineScript::setRunsOnSubFrames(bool on)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginescript.html#setRunsOnSubFrames

    Parameters
    ----------

    on : bool
      Passed on as it is.
    """
    #  void QWebEngineScript::setRunsOnSubFrames(bool on)
    self.uglySide.call(
        'ritual_ZN16QWebEngineScript18setRunsOnSubFramesEb', on,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, other: QWebEngineScript) -> bool:
    """
    Calls Qt's 'bool QWebEngineScript::operator==(const QWebEngineScript
    &other) const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebenginescript.html#operator==

    Parameters
    ----------

    other : QWebEngineScript
      Passed on as a value: Qt reads the C++ QWebEngineScript, which stays
      Python's own.
    """
    #  bool QWebEngineScript::operator==(const QWebEngineScript &other) const
    return self.uglySide.call(
        'ritual_ZNK16QWebEngineScripteqERKS_', self._valueOf(other),
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
  def __ne__(self, other: QWebEngineScript) -> bool:
    """
    Calls Qt's 'bool QWebEngineScript::operator!=(const QWebEngineScript
    &other) const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebenginescript.html#operator!=

    Parameters
    ----------

    other : QWebEngineScript
      Passed on as a value: Qt reads the C++ QWebEngineScript, which stays
      Python's own.
    """
    #  bool QWebEngineScript::operator!=(const QWebEngineScript &other) const
    return self.uglySide.call(
        'ritual_ZNK16QWebEngineScriptneERKS_', self._valueOf(other),
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
    Notes what was given, for Qt's 'QWebEngineScript::QWebEngineScript()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginescript.html#QWebEngineScript
    """
    #  QWebEngineScript::QWebEngineScript()
    self._noteCreation(QWebEngineScript, lambda: Rituals.call(
        'ritual_ZN16QWebEngineScriptC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QWebEngineScript) -> None:
    """
    Notes what was given, for Qt's 'QWebEngineScript::QWebEngineScript(const
    QWebEngineScript &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginescript.html#QWebEngineScript

    Parameters
    ----------

    other : QWebEngineScript
      Passed on as a value: Qt reads the C++ QWebEngineScript, which stays
      Python's own.
    """
    #  QWebEngineScript::QWebEngineScript(const QWebEngineScript &other)
    self._noteCreation(QWebEngineScript, lambda: Rituals.call(
        'ritual_ZN16QWebEngineScriptC1ERKS_', self._valueOf(other),
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

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QWebEngineScript::swap(QWebEngineScript &other)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QWebEngineScript.swap' has no cute function yet. Qt's 'void "
        "QWebEngineScript::swap(QWebEngineScript &other)': takes a type "
        "Python has no way to hand over yet.")


#  Qt's 'QList<QWebEngineScript>': the list of QWebEngineScript, which
#  'QList[QWebEngineScript]' gives. It is made here, so that there is one as
#  soon as there can be a QWebEngineScript.
QList.createKind(
    QWebEngineScript, 'value',
    make='ritual_list_make_QWebEngineScript',
    add='ritual_list_add_QWebEngineScript',
    size='ritual_list_size_QWebEngineScript',
    at='ritual_list_at_QWebEngineScript',
    drop='ritual_list_drop_QWebEngineScript',
)
