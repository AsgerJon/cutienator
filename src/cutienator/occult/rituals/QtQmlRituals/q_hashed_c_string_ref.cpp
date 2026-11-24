//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qhashedstring_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qhashedstring_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/private/qhashedstring_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qml/qml/ftw/qhashedstring.cpp, line 60, as _ZNK17QHashedCStringRef7toUtf16Ev
inline QString QHashedCStringRef::toUtf16() const
{
    if (m_length == 0)
        return QString();

    QString rv;
    rv.resize(m_length);
    writeUtf16((quint16*)rv.data());
    return rv;
}
//  -----------------------------------------------------------------------

//  QHashedCStringRef::QHashedCStringRef()
extern "C" Q_DECL_EXPORT
QHashedCStringRef *ritual_ZN17QHashedCStringRefC1Ev() {
  return new QHashedCStringRef();
}

//  QHashedCStringRef::QHashedCStringRef(const char *a0, int a1)
extern "C" Q_DECL_EXPORT
QHashedCStringRef *ritual_ZN17QHashedCStringRefC1EPKci(
    const char *a0,
    int a1) {
  return new QHashedCStringRef(a0, a1);
}

//  QHashedCStringRef::QHashedCStringRef(const char *a0, int a1, quint32 a2)
extern "C" Q_DECL_EXPORT
QHashedCStringRef *ritual_ZN17QHashedCStringRefC1EPKcij(
    const char *a0,
    int a1,
    quint32 a2) {
  return new QHashedCStringRef(a0, a1, a2);
}

//  QHashedCStringRef::QHashedCStringRef(const QHashedCStringRef &a0)
extern "C" Q_DECL_EXPORT
QHashedCStringRef *ritual_ZN17QHashedCStringRefC1ERKS_(
    const QHashedCStringRef *a0) {
  return new QHashedCStringRef(*a0);
}

//  quint32 QHashedCStringRef::hash() const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK17QHashedCStringRef4hashEv(const QHashedCStringRef *self) {
  return self->hash();
}

//  const char *QHashedCStringRef::constData() const
extern "C" Q_DECL_EXPORT
const char *ritual_ZNK17QHashedCStringRef9constDataEv(
    const QHashedCStringRef *self) {
  return self->constData();
}

//  int QHashedCStringRef::length() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QHashedCStringRef6lengthEv(const QHashedCStringRef *self) {
  return self->length();
}

//  QString QHashedCStringRef::toUtf16() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17QHashedCStringRef7toUtf16Ev(
    const QHashedCStringRef *self) {
  return new QString(self->toUtf16());
}

//  int QHashedCStringRef::utf16length() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QHashedCStringRef11utf16lengthEv(
    const QHashedCStringRef *self) {
  return self->utf16length();
}

//  void QHashedCStringRef::writeUtf16(QChar *a0) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK17QHashedCStringRef10writeUtf16EP5QChar(
    const QHashedCStringRef *self,
    QChar *a0) {
  self->writeUtf16(a0);
}

//  void QHashedCStringRef::writeUtf16(quint16 *a0) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK17QHashedCStringRef10writeUtf16EPt(
    const QHashedCStringRef *self,
    quint16 *a0) {
  self->writeUtf16(a0);
}

//  void QHashedCStringRef::computeHash() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK17QHashedCStringRef11computeHashEv(
    const QHashedCStringRef *self) {
  self->computeHash();
}

//  QHashedCStringRef::~QHashedCStringRef()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QHashedCStringRefD1Ev(QHashedCStringRef *self) {
  delete self;
}
