//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qstringhash_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qstringhash_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qhashedstring_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qlatin1stringview.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qhashedstring_p.h"
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

//  const QString &QStringHashBase::toQString(const QString &s)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QStringHashBase9toQStringERK7QString(const QString *s) {
  return new QString(QStringHashBase::toQString(*s));
}

//  const QString &QStringHashBase::toQString(const QHashedString &s)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QStringHashBase9toQStringERK13QHashedString(
    const QHashedString *s) {
  return new QString(QStringHashBase::toQString(*s));
}

//  QString QStringHashBase::toQString(const QV4::String *s)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QStringHashBase9toQStringEPKN3QV46StringE(
    const QV4::String *s) {
  return new QString(QStringHashBase::toQString(s));
}

//  QString QStringHashBase::toQString(const QHashedStringRef &s)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QStringHashBase9toQStringERK16QHashedStringRef(
    const QHashedStringRef *s) {
  return new QString(QStringHashBase::toQString(*s));
}

//  QString QStringHashBase::toQString(const QLatin1String &s)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QStringHashBase9toQStringERK13QLatin1String(
    const QLatin1String *s) {
  return new QString(QStringHashBase::toQString(*s));
}

//  QString QStringHashBase::toQString(const QHashedCStringRef &s)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QStringHashBase9toQStringERK17QHashedCStringRef(
    const QHashedCStringRef *s) {
  return new QString(QStringHashBase::toQString(*s));
}

//  quint32 QStringHashBase::hashOf(const QHashedStringRef &s)
extern "C" Q_DECL_EXPORT
quint32 ritual_ZN15QStringHashBase6hashOfERK16QHashedStringRef(
    const QHashedStringRef *s) {
  return QStringHashBase::hashOf(*s);
}

//  quint32 QStringHashBase::hashOf(QV4::String *s)
extern "C" Q_DECL_EXPORT
quint32 ritual_ZN15QStringHashBase6hashOfEPN3QV46StringE(QV4::String *s) {
  return QStringHashBase::hashOf(s);
}

//  quint32 QStringHashBase::hashOf(const QV4::String *s)
extern "C" Q_DECL_EXPORT
quint32 ritual_ZN15QStringHashBase6hashOfEPKN3QV46StringE(
    const QV4::String *s) {
  return QStringHashBase::hashOf(s);
}

//  QStringHashBase::~QStringHashBase()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QStringHashBaseD1Ev(QStringHashBase *self) {
  delete self;
}
