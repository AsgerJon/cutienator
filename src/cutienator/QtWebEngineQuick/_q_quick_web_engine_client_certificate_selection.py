"""
QQuickWebEngineClientCertificateSelection binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWebEngineQuick/6.12.0/QtWebEngineQuick/private/qquickwebengineclientcertificateselection_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickWebEngineClientCertificateSelection to be private: it
#  declares the class in a header it calls private. cutienator does not care.
#  Qt hands objects of the class out all the same, and a class we are handed
#  is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QUrl
  from . import QQuickWebEngineClientCertificateOption
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickWebEngineClientCertificateOption = WAIT['QQuickWebEngineClientCertificateOption']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickWebEngineClientCertificateSelection(QObject):
  """
  The cute side of Qt's QQuickWebEngineClientCertificateSelection: a plain
  Python object standing in front of one C++
  QQuickWebEngineClientCertificateSelection.

  It is built on the cute 'QObject', as Qt's
  QQuickWebEngineClientCertificateSelection is built on Qt's QObject, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickWebEngineClientCertificateSelection that has a
  ritual and that Python can call so far, 5 names in all: 'metaObject', 'tr',
  'host', 'select', 'selectNone'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickWebEngineClientCertificateSelection::qt_metacast(const
    char *a0)': one of Qt's own inner workings.
  - Qt's 'int
    QQuickWebEngineClientCertificateSelection::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'void
    QQuickWebEngineClientCertificateSelection::qt_qmlMarker_uncreatable()':
    one of Qt's own inner workings.
  - Qt's 'QQmlListProperty<QQuickWebEngineClientCertificateOption>
    QQuickWebEngineClientCertificateSelection::certificates()': gives a type
    Python has no way to take yet.
  - Qt's 'qsizetype
    QQuickWebEngineClientCertificateSelection::certificates_count(
    QQmlListProperty<QQuickWebEngineClientCertificateOption> *p)': names
    'QQmlListProperty<QQuickWebEngineClientCertificateOption>', which has no
    cute class yet.
  - Qt's 'QQuickWebEngineClientCertificateOption
    *QQuickWebEngineClientCertificateSelection::certificates_at(
    QQmlListProperty<QQuickWebEngineClientCertificateOption> *p, qsizetype
    idx)': names 'QQmlListProperty<QQuickWebEngineClientCertificateOption>',
    which has no cute class yet.
  - Qt's 'QQuickWebEngineClientCertificateSelection::
    QQuickWebEngineClientCertificateSelection(
    QSharedPointer<QtWebEngineCore::ClientCertSelectController> a0)': takes a
    type Python has no way to hand over yet.

  What has no ritual
  ------------------

  2 of the 16 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickWebEngineClientCertificateSelection is created at the first
    use, not by 'QQuickWebEngineClientCertificateSelection(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickWebEngineClientCertificateSelection.
  - Qt tells when it has removed the C++
    QQuickWebEngineClientCertificateSelection. Every call on the cute object,
    and every use of it as an argument, then raises 'RuntimeError', and
    nothing reaches C++.
  - Each name of Qt's QQuickWebEngineClientCertificateSelection that has no
    cute function yet, 'certificates', 'certificates_at',
    'certificates_count', holds a function that raises 'NotImplementedError',
    and its docstring says why.
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
    Calls Qt's 'QString QQuickWebEngineClientCertificateSelection::tr(const
    char *s, const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineclientcertificateselection.html#tr

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
    #  QString QQuickWebEngineClientCertificateSelection::tr(const char *s,
    #      const char *c, int n)
    return Rituals.call(
        'ritual_ZN41QQuickWebEngineClientCertificateSelection2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickWebEngineClientCertificateSelection'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject
    *QQuickWebEngineClientCertificateSelection::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineclientcertificateselection.html

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject
    #      *QQuickWebEngineClientCertificateSelection::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK41QQuickWebEngineClientCertificateSelection10metaObjectE'
        'v',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def host(self) -> QUrl:
    """
    Calls Qt's 'QUrl QQuickWebEngineClientCertificateSelection::host()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineclientcertificateselection.html

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QQuickWebEngineClientCertificateSelection::host() const
    address = self.uglySide.call(
        'ritual_ZNK41QQuickWebEngineClientCertificateSelection4hostEv',
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

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
    'QQuickWebEngineClientCertificateSelection::
    QQuickWebEngineClientCertificateSelection()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineclientcertificateselection.html
    """
    #  QQuickWebEngineClientCertificateSelection::
    #      QQuickWebEngineClientCertificateSelection()
    self._noteCreation(
        QQuickWebEngineClientCertificateSelection, lambda: Rituals.call(
            'ritual_ZN41QQuickWebEngineClientCertificateSelectionC1Ev',
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

  @overload(int)
  def select(self, idx: int) -> None:
    """
    Calls Qt's 'void QQuickWebEngineClientCertificateSelection::select(int
    idx)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineclientcertificateselection.html

    Parameters
    ----------

    idx : int
      Passed on as it is.
    """
    #  void QQuickWebEngineClientCertificateSelection::select(int idx)
    self.uglySide.call(
        'ritual_ZN41QQuickWebEngineClientCertificateSelection6selectEi', idx,
    )

  @overload(QQuickWebEngineClientCertificateOption)
  @overload(NoneType)
  def select(
      self,
      certificate: Optional[QQuickWebEngineClientCertificateOption],
  ) -> None:
    """
    Calls Qt's 'void QQuickWebEngineClientCertificateSelection::select(const
    QQuickWebEngineClientCertificateOption *certificate)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineclientcertificateselection.html

    Parameters
    ----------

    certificate : Optional[QQuickWebEngineClientCertificateOption]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickWebEngineClientCertificateSelection::select(const
    #      QQuickWebEngineClientCertificateOption *certificate)
    self.uglySide.call(
        'ritual_ZN41QQuickWebEngineClientCertificateSelection6selectEPK38QQ'
        'uickWebEngineClientCertificateOption',
        self._addressOf(certificate),
    )

  def selectNone(self) -> None:
    """
    Calls Qt's 'void
    QQuickWebEngineClientCertificateSelection::selectNone()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineclientcertificateselection.html
    """
    #  void QQuickWebEngineClientCertificateSelection::selectNone()
    self.uglySide.call(
        'ritual_ZN41QQuickWebEngineClientCertificateSelection10selectNoneEv',
    )

  @staticmethod
  def certificates(*__, **_) -> Never:
    """
    Qt's 'QQmlListProperty<QQuickWebEngineClientCertificateOption>
    QQuickWebEngineClientCertificateSelection::certificates()': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQuickWebEngineClientCertificateSelection.certificates' has no "
        "cute function yet. Qt's "
        "'QQmlListProperty<QQuickWebEngineClientCertificateOption> "
        "QQuickWebEngineClientCertificateSelection::certificates()': gives "
        "a type Python has no way to take yet.")

  @staticmethod
  def certificates_at(*__, **_) -> Never:
    """
    Qt's 'QQuickWebEngineClientCertificateOption
    *QQuickWebEngineClientCertificateSelection::certificates_at(
    QQmlListProperty<QQuickWebEngineClientCertificateOption> *p, qsizetype
    idx)': names 'QQmlListProperty<QQuickWebEngineClientCertificateOption>',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQuickWebEngineClientCertificateSelection.certificates_at' has no "
        "cute function yet. Qt's 'QQuickWebEngineClientCertificateOption "
        "*QQuickWebEngineClientCertificateSelection::certificates_at(QQmlLis"
        "tProperty<QQuickWebEngineClientCertificateOption> *p, qsizetype "
        "idx)': names "
        "'QQmlListProperty<QQuickWebEngineClientCertificateOption>', which "
        "has no cute class yet.")

  @staticmethod
  def certificates_count(*__, **_) -> Never:
    """
    Qt's 'qsizetype
    QQuickWebEngineClientCertificateSelection::certificates_count(
    QQmlListProperty<QQuickWebEngineClientCertificateOption> *p)': names
    'QQmlListProperty<QQuickWebEngineClientCertificateOption>', which has no
    cute class yet.
    """
    raise NotImplementedError(
        "'QQuickWebEngineClientCertificateSelection.certificates_count' has "
        "no cute function yet. Qt's 'qsizetype "
        "QQuickWebEngineClientCertificateSelection::certificates_count(QQmlL"
        "istProperty<QQuickWebEngineClientCertificateOption> *p)': names "
        "'QQmlListProperty<QQuickWebEngineClientCertificateOption>', which "
        "has no cute class yet.")
