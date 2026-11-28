"""
QFormDataPartBuilder binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/qformdatabuilder.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QByteArrayView, QIODevice
  from . import QHttpHeaders
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QByteArrayView = WAIT['QByteArrayView']
  QHttpHeaders = WAIT['QHttpHeaders']
  QIODevice = WAIT['QIODevice']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QFormDataPartBuilder(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QFormDataPartBuilder: a plain Python object standing
  in front of one C++ QFormDataPartBuilder.

  C++ hands a QFormDataPartBuilder around as a copy, so every C++
  QFormDataPartBuilder behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QFormDataPartBuilder that has a ritual and that
  Python can call so far, 4 names in all: 'setBody', 'setBodyDevice',
  'setHeaders', 'setBodyHelper'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QFormDataPartBuilder::QFormDataPartBuilder(QFormDataBuilderPrivate
    *qfdb, qsizetype idx)': names 'QFormDataBuilderPrivate', which has no
    cute class yet.
  - Qt's 'void QFormDataPartBuilder::swap(QFormDataPartBuilder &other)':
    takes a type Python has no way to hand over yet.
  - Qt's 'QFormDataPartBuilder::~QFormDataPartBuilder()': the destructor:
    Python removes its C++ QFormDataPartBuilder by it, and has no other use
    for it.

  What has no ritual
  ------------------

  3 of the 11 functions Qt declares: 2 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 1 a template.

  What to expect
  --------------

  - The C++ QFormDataPartBuilder is created at the first use, not by
    'QFormDataPartBuilder(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QFormDataPartBuilder back gives a copy the ritual
    made for Python, in a new cute QFormDataPartBuilder.
  - Each name of Qt's QFormDataPartBuilder that has no cute function yet,
    'd_func', 'swap', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QFormDataPartBuilder'

  #  Qt's '~QFormDataPartBuilder()'. Naming it makes this a value class:
  #  Python owns every C++ QFormDataPartBuilder behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN20QFormDataPartBuilderD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QByteArrayView)
  @overload(QByteArrayView, str)
  @overload(QByteArrayView, str, str)
  def setBody(
      self,
      data: QByteArrayView,
      fileName: str = '',
      mimeType: str = '',
  ) -> QFormDataPartBuilder:
    """
    Calls Qt's 'QFormDataPartBuilder
    QFormDataPartBuilder::setBody(QByteArrayView data, QAnyStringView
    fileName, QAnyStringView mimeType)'.

    Qt's own words: https://doc.qt.io/qt-6/qformdatapartbuilder.html#setBody

    Parameters
    ----------

    data : QByteArrayView
      Passed on as a value: Qt reads the C++ QByteArrayView, which stays
      Python's own.

    fileName : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    mimeType : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    Returns
    -------

    QFormDataPartBuilder
      A new cute QFormDataPartBuilder around the copy Qt gave back. Python
      owns it.
    """
    #  QFormDataPartBuilder QFormDataPartBuilder::setBody(QByteArrayView
    #      data, QAnyStringView fileName, QAnyStringView mimeType)
    address = self.uglySide.call(
        'ritual_ZN20QFormDataPartBuilder7setBodyE14QByteArrayView14QAnyStri'
        'ngViewS1_',
        self._valueOf(data), fileName, mimeType,
    )
    return QFormDataPartBuilder._cuteOwning(address)

  @overload(QIODevice)
  @overload(NoneType)
  @overload(QIODevice, str)
  @overload(NoneType, str)
  @overload(QIODevice, str, str)
  @overload(NoneType, str, str)
  def setBodyDevice(
      self,
      body: Optional[QIODevice],
      fileName: str = '',
      mimeType: str = '',
  ) -> QFormDataPartBuilder:
    """
    Calls Qt's 'QFormDataPartBuilder
    QFormDataPartBuilder::setBodyDevice(QIODevice *body, QAnyStringView
    fileName, QAnyStringView mimeType)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qformdatapartbuilder.html#setBodyDevice

    Parameters
    ----------

    body : Optional[QIODevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    fileName : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    mimeType : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    Returns
    -------

    QFormDataPartBuilder
      A new cute QFormDataPartBuilder around the copy Qt gave back. Python
      owns it.
    """
    #  QFormDataPartBuilder QFormDataPartBuilder::setBodyDevice(QIODevice
    #      *body, QAnyStringView fileName, QAnyStringView mimeType)
    address = self.uglySide.call(
        'ritual_ZN20QFormDataPartBuilder13setBodyDeviceEP9QIODevice14QAnySt'
        'ringViewS2_',
        self._addressOf(body), fileName, mimeType,
    )
    return QFormDataPartBuilder._cuteOwning(address)

  @overload(QHttpHeaders)
  def setHeaders(self, headers: QHttpHeaders) -> QFormDataPartBuilder:
    """
    Calls Qt's 'QFormDataPartBuilder QFormDataPartBuilder::setHeaders(const
    QHttpHeaders &headers)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qformdatapartbuilder.html#setHeaders

    Parameters
    ----------

    headers : QHttpHeaders
      Passed on as a value: Qt reads the C++ QHttpHeaders, which stays
      Python's own.

    Returns
    -------

    QFormDataPartBuilder
      A new cute QFormDataPartBuilder around the copy Qt gave back. Python
      owns it.
    """
    #  QFormDataPartBuilder QFormDataPartBuilder::setHeaders(const
    #      QHttpHeaders &headers)
    address = self.uglySide.call(
        'ritual_ZN20QFormDataPartBuilder10setHeadersERK12QHttpHeaders',
        self._valueOf(headers),
    )
    return QFormDataPartBuilder._cuteOwning(address)

  @overload(QByteArray, str, str)
  def setBodyHelper(
      self,
      data: QByteArray,
      fileName: str,
      mimeType: str,
  ) -> QFormDataPartBuilder:
    """
    Calls Qt's 'QFormDataPartBuilder
    QFormDataPartBuilder::setBodyHelper(const QByteArray &data,
    QAnyStringView fileName, QAnyStringView mimeType)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qformdatapartbuilder.html#setBodyHelper

    Parameters
    ----------

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    fileName : str
      Passed on as it is: a QString is made of it for the call.

    mimeType : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QFormDataPartBuilder
      A new cute QFormDataPartBuilder around the copy Qt gave back. Python
      owns it.
    """
    #  QFormDataPartBuilder QFormDataPartBuilder::setBodyHelper(const
    #      QByteArray &data, QAnyStringView fileName, QAnyStringView
    #      mimeType)
    address = self.uglySide.call(
        'ritual_ZN20QFormDataPartBuilder13setBodyHelperERK10QByteArray14QAn'
        'yStringViewS3_',
        self._valueOf(data), fileName, mimeType,
    )
    return QFormDataPartBuilder._cuteOwning(address)

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
    'QFormDataPartBuilder::QFormDataPartBuilder()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qformdatapartbuilder.html#QFormDataPartBuilder
    """
    #  QFormDataPartBuilder::QFormDataPartBuilder()
    self._noteCreation(QFormDataPartBuilder, lambda: Rituals.call(
        'ritual_ZN20QFormDataPartBuilderC1Ev',
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
  def d_func(*__, **_) -> Never:
    """
    - Qt's 'const QFormDataPartBuilderPrivate *QFormDataPartBuilder::d_func()
      const': Qt's library has no name for it, and its code in Qt's source
      does not compile apart from its file: member access into incomplete
      type 'QFormDataBuilderPrivate'.
    - Qt's 'QFormDataPartBuilderPrivate *QFormDataPartBuilder::d_func()':
      Qt's library has no name for it, and its code in Qt's source does not
      compile apart from its file: expected '{' or ','.
    """
    raise NotImplementedError(
        "'QFormDataPartBuilder.d_func' has no cute function yet. Qt's "
        "'const QFormDataPartBuilderPrivate *QFormDataPartBuilder::d_func() "
        "const': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: member access into "
        "incomplete type 'QFormDataBuilderPrivate'. Qt's "
        "'QFormDataPartBuilderPrivate *QFormDataPartBuilder::d_func()': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: expected '{' or ','.")

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QFormDataPartBuilder::swap(QFormDataPartBuilder &other)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QFormDataPartBuilder.swap' has no cute function yet. Qt's 'void "
        "QFormDataPartBuilder::swap(QFormDataPartBuilder &other)': takes a "
        "type Python has no way to hand over yet.")
