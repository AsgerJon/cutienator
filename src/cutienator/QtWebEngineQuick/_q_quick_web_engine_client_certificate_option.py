"""
QQuickWebEngineClientCertificateOption binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWebEngineQuick/6.12.0/QtWebEngineQuick/private/qquickwebengineclientcertificateselection_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickWebEngineClientCertificateOption to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QDateTime, QMetaObject
  from . import QQuickWebEngineClientCertificateSelection
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickWebEngineClientCertificateSelection = WAIT['QQuickWebEngineClientCertificateSelection']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickWebEngineClientCertificateOption(QObject):
  """
  The cute side of Qt's QQuickWebEngineClientCertificateOption: a plain
  Python object standing in front of one C++
  QQuickWebEngineClientCertificateOption.

  It is built on the cute 'QObject', as Qt's
  QQuickWebEngineClientCertificateOption is built on Qt's QObject, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickWebEngineClientCertificateOption that has a
  ritual and that Python can call so far, 8 names in all: 'metaObject', 'tr',
  'issuer', 'subject', 'effectiveDate', 'expiryDate', 'isSelfSigned',
  'select'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickWebEngineClientCertificateOption::qt_metacast(const
    char *a0)': one of Qt's own inner workings.
  - Qt's 'int
    QQuickWebEngineClientCertificateOption::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'void
    QQuickWebEngineClientCertificateOption::qt_qmlMarker_uncreatable()': one
    of Qt's own inner workings.

  What has no ritual
  ------------------

  2 of the 14 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickWebEngineClientCertificateOption is created at the first
    use, not by 'QQuickWebEngineClientCertificateOption(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickWebEngineClientCertificateOption.
  - Qt tells when it has removed the C++
    QQuickWebEngineClientCertificateOption. Every call on the cute object,
    and every use of it as an argument, then raises 'RuntimeError', and
    nothing reaches C++.
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
    Calls Qt's 'QString QQuickWebEngineClientCertificateOption::tr(const char
    *s, const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineclientcertificateoption.html#tr

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
    #  QString QQuickWebEngineClientCertificateOption::tr(const char *s,
    #      const char *c, int n)
    return Rituals.call(
        'ritual_ZN38QQuickWebEngineClientCertificateOption2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickWebEngineClientCertificateOption'

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
    *QQuickWebEngineClientCertificateOption::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineclientcertificateoption.html

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject
    #      *QQuickWebEngineClientCertificateOption::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK38QQuickWebEngineClientCertificateOption10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def issuer(self) -> str:
    """
    Calls Qt's 'QString QQuickWebEngineClientCertificateOption::issuer()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineclientcertificateoption.html#issuer

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickWebEngineClientCertificateOption::issuer() const
    return self.uglySide.call(
        'ritual_ZNK38QQuickWebEngineClientCertificateOption6issuerEv',
    )

  def subject(self) -> str:
    """
    Calls Qt's 'QString QQuickWebEngineClientCertificateOption::subject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineclientcertificateoption.html

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickWebEngineClientCertificateOption::subject() const
    return self.uglySide.call(
        'ritual_ZNK38QQuickWebEngineClientCertificateOption7subjectEv',
    )

  def effectiveDate(self) -> QDateTime:
    """
    Calls Qt's 'QDateTime
    QQuickWebEngineClientCertificateOption::effectiveDate() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineclientcertificateoption.html

    Returns
    -------

    QDateTime
      A new cute QDateTime around the copy Qt gave back. Python owns it.
    """
    #  QDateTime QQuickWebEngineClientCertificateOption::effectiveDate()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK38QQuickWebEngineClientCertificateOption13effectiveDateE'
        'v',
    )
    from ..QtCore import QDateTime
    return QDateTime._cuteOwning(address)

  def expiryDate(self) -> QDateTime:
    """
    Calls Qt's 'QDateTime
    QQuickWebEngineClientCertificateOption::expiryDate() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineclientcertificateoption.html

    Returns
    -------

    QDateTime
      A new cute QDateTime around the copy Qt gave back. Python owns it.
    """
    #  QDateTime QQuickWebEngineClientCertificateOption::expiryDate() const
    address = self.uglySide.call(
        'ritual_ZNK38QQuickWebEngineClientCertificateOption10expiryDateEv',
    )
    from ..QtCore import QDateTime
    return QDateTime._cuteOwning(address)

  def isSelfSigned(self) -> bool:
    """
    Calls Qt's 'bool QQuickWebEngineClientCertificateOption::isSelfSigned()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineclientcertificateoption.html
    """
    #  bool QQuickWebEngineClientCertificateOption::isSelfSigned() const
    return self.uglySide.call(
        'ritual_ZNK38QQuickWebEngineClientCertificateOption12isSelfSignedEv',
    )

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

  @overload(QQuickWebEngineClientCertificateSelection, int)
  @overload(NoneType, int)
  def __init__(
      self,
      selection: Optional[QQuickWebEngineClientCertificateSelection],
      index: int,
  ) -> None:
    """
    Notes what was given, for Qt's 'QQuickWebEngineClientCertificateOption::
    QQuickWebEngineClientCertificateOption(
    QQuickWebEngineClientCertificateSelection *selection, int index)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineclientcertificateoption.html

    Parameters
    ----------

    selection : Optional[QQuickWebEngineClientCertificateSelection]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    index : int
      Passed on as it is.
    """
    #  QQuickWebEngineClientCertificateOption::
    #      QQuickWebEngineClientCertificateOption(
    #      QQuickWebEngineClientCertificateSelection *selection, int index)
    self._noteCreation(
        QQuickWebEngineClientCertificateOption, lambda: Rituals.call(
            'ritual_ZN38QQuickWebEngineClientCertificateOptionC1EP41QQuickW'
            'ebEngineClientCertificateSelectioni',
            self._addressOf(selection), index,
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

  def select(self) -> None:
    """
    Calls Qt's 'void QQuickWebEngineClientCertificateOption::select()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineclientcertificateoption.html#select
    """
    #  void QQuickWebEngineClientCertificateOption::select()
    self.uglySide.call(
        'ritual_ZN38QQuickWebEngineClientCertificateOption6selectEv',
    )
