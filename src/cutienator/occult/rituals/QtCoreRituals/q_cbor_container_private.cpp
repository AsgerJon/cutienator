//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qcborvalue_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qcborvalue_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qlatin1stringview.h>
#include <QtCore/qstringview.h>
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qanystringview.h>
#include <QtCore/qcborvalue.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qcborvalue.h>
#include <QtCore/private/qcborvalue_p.h>
#include <QtCore/qdatastream.h>
#include <QtCore/qcborarray.h>
#include <QtCore/qcbormap.h>
#if QT_CONFIG(cborstreamreader)
#include <QtCore/qcborstreamreader.h>
#endif
#if QT_CONFIG(cborstreamwriter)
#include <QtCore/qcborstreamwriter.h>
#endif
#include <QtCore/qdebug.h>
#include <QtCore/qendian.h>
#include <QtCore/qlocale.h>
#include <QtCore/qdatetime.h>
#include <QtCore/qtimezone.h>
#include <QtCore/private/qnumeric_p.h>
#include <QtCore/private/qsimd_p.h>
#include <new>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/corelib/serialization/qcborvalue.cpp, line 1108, as _ZN21QCborContainerPrivate20appendNonAsciiStringE11QStringView
inline void QCborContainerPrivate::appendNonAsciiString(QStringView s)
{
    appendByteData(reinterpret_cast<const char *>(s.utf16()), s.size() * 2,
                   QCborValue::String, QtCbor::Element::StringIsUtf16);
}
//  -----------------------------------------------------------------------

//  QCborContainerPrivate::QCborContainerPrivate()
extern "C" Q_DECL_EXPORT
QCborContainerPrivate *ritual_ZN21QCborContainerPrivateC1Ev() {
  return new QCborContainerPrivate();
}

//  qptrdiff QCborContainerPrivate::addByteData(const char *block, qsizetype
//      len)
extern "C" Q_DECL_EXPORT
qptrdiff ritual_ZN21QCborContainerPrivate11addByteDataEPKcx(
    QCborContainerPrivate *self,
    const char *block,
    qsizetype len) {
  return self->addByteData(block, len);
}

//  const QtCbor::ByteData *QCborContainerPrivate::byteData(QtCbor::Element
//      e) const
extern "C" Q_DECL_EXPORT
const QtCbor::ByteData *ritual_ZNK21QCborContainerPrivate8byteDataEN6QtCbor7ElementE(
    const QCborContainerPrivate *self,
    const QtCbor::Element *e) {
  return self->byteData(*e);
}

//  const QtCbor::ByteData *QCborContainerPrivate::byteData(qsizetype idx)
//      const
extern "C" Q_DECL_EXPORT
const QtCbor::ByteData *ritual_ZNK21QCborContainerPrivate8byteDataEx(
    const QCborContainerPrivate *self,
    qsizetype idx) {
  return self->byteData(idx);
}

//  QCborContainerPrivate *QCborContainerPrivate::containerAt(qsizetype idx,
//      QCborValue::Type type) const
extern "C" Q_DECL_EXPORT
QCborContainerPrivate *ritual_ZNK21QCborContainerPrivate11containerAtExN10QCborValue4TypeE(
    const QCborContainerPrivate *self,
    qsizetype idx,
    QCborValue::Type type) {
  return self->containerAt(idx, type);
}

//  void QCborContainerPrivate::append(QtCbor::Undefined a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QCborContainerPrivate6appendEN6QtCbor9UndefinedE(
    QCborContainerPrivate *self,
    const QtCbor::Undefined *a0) {
  self->append(*a0);
}

//  void QCborContainerPrivate::append(qint64 value)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QCborContainerPrivate6appendEx(
    QCborContainerPrivate *self,
    qint64 value) {
  self->append(value);
}

//  void QCborContainerPrivate::append(QCborTag tag)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QCborContainerPrivate6appendE8QCborTag(
    QCborContainerPrivate *self,
    QCborTag tag) {
  self->append(tag);
}

//  void QCborContainerPrivate::appendByteData(const char *data, qsizetype
//      len, QCborValue::Type type, QtCbor::Element::ValueFlags extraFlags)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QCborContainerPrivate14appendByteDataEPKcxN10QCborValue4TypeE6QFlagsIN6QtCbor7Element9ValueFlagEE(
    QCborContainerPrivate *self,
    const char *data,
    qsizetype len,
    QCborValue::Type type,
    int extraFlags) {
  self->appendByteData(
      data,
      len,
      type,
      QFlags<QtCbor::Element::ValueFlag>::fromInt(extraFlags));
}

//  void QCborContainerPrivate::appendAsciiString(const char *str, qsizetype
//      len)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QCborContainerPrivate17appendAsciiStringEPKcx(
    QCborContainerPrivate *self,
    const char *str,
    qsizetype len) {
  self->appendAsciiString(str, len);
}

//  void QCborContainerPrivate::appendUtf8String(const char *str, qsizetype
//      len)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QCborContainerPrivate16appendUtf8StringEPKcx(
    QCborContainerPrivate *self,
    const char *str,
    qsizetype len) {
  self->appendUtf8String(str, len);
}

//  void QCborContainerPrivate::append(QLatin1StringView s)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QCborContainerPrivate6appendE13QLatin1String(
    QCborContainerPrivate *self,
    const QLatin1String *s) {
  self->append(*s);
}

//  void QCborContainerPrivate::appendNonAsciiString(QStringView s)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QCborContainerPrivate20appendNonAsciiStringE11QStringView(
    QCborContainerPrivate *self,
    const QString *s) {
  self->appendNonAsciiString(QStringView(*s));
}

//  QByteArray QCborContainerPrivate::byteArrayAt(qsizetype idx) const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK21QCborContainerPrivate11byteArrayAtEx(
    const QCborContainerPrivate *self,
    qsizetype idx) {
  return new QByteArray(self->byteArrayAt(idx));
}

//  QString QCborContainerPrivate::stringAt(qsizetype idx) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK21QCborContainerPrivate8stringAtEx(
    const QCborContainerPrivate *self,
    qsizetype idx) {
  return new QString(self->stringAt(idx));
}

//  QAnyStringView QCborContainerPrivate::anyStringViewAt(qsizetype idx)
//      const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK21QCborContainerPrivate15anyStringViewAtEx(
    const QCborContainerPrivate *self,
    qsizetype idx) {
  return new QString(self->anyStringViewAt(idx).toString());
}

//  QCborValue QCborContainerPrivate::makeValue(QCborValue::Type type, qint64
//      n, QCborContainerPrivate *d, ContainerDisposition disp)
extern "C" Q_DECL_EXPORT
QCborValue *ritual_ZN21QCborContainerPrivate9makeValueEN10QCborValue4TypeExPS_NS_20ContainerDispositionE(
    QCborValue::Type type,
    qint64 n,
    QCborContainerPrivate *d,
    QCborContainerPrivate::ContainerDisposition disp) {
  return new QCborValue(QCborContainerPrivate::makeValue(type, n, d, disp));
}

//  QCborValue QCborContainerPrivate::valueAt(qsizetype idx) const
extern "C" Q_DECL_EXPORT
QCborValue *ritual_ZNK21QCborContainerPrivate7valueAtEx(
    const QCborContainerPrivate *self,
    qsizetype idx) {
  return new QCborValue(self->valueAt(idx));
}

//  QtCbor::Element QCborContainerPrivate::elementFromValue(const QCborValue
//      &value)
extern "C" Q_DECL_EXPORT
QtCbor::Element *ritual_ZN21QCborContainerPrivate16elementFromValueERK10QCborValue(
    const QCborValue *value) {
  return new QtCbor::Element(
      QCborContainerPrivate::elementFromValue(
          *value));
}
