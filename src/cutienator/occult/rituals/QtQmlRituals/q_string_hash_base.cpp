//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qstringhash_p.h, Qt 6.12.0. Edited by hand on
//  2026-11-25: added by hand, instances of templates of the class: 3. Kept
//  as it is when the generator runs again.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qstringhash_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qstringview.h>
#include <QtCore/qlatin1stringview.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qhashedstring_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/QString>
#include <QtCore/QStringView>
#include <QtCore/QLatin1StringView>
#include <QtCore/QLatin1String>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/private/qhashedstring_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
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

//  HashedForm<QString>::Type QStringHashBase::hashedString(const QString &s)
extern "C" Q_DECL_EXPORT
HashedForm<QString>::Type *ritual_ZN15QStringHashBase12hashedStringERK7QString(
    const QString *s) {
  return new HashedForm<QString>::Type(QStringHashBase::hashedString(*s));
}

//  HashedForm<QStringView>::Type QStringHashBase::hashedString(QStringView
//      s)
extern "C" Q_DECL_EXPORT
HashedForm<QStringView>::Type *ritual_ZN15QStringHashBase12hashedStringE11QStringView(
    const QString *s) {
  return new HashedForm<QStringView>::Type(
      QStringHashBase::hashedString(
          QStringView(*s)));
}

//  HashedForm<QV4::String *>::Type QStringHashBase::hashedString(QV4::String
//      *s)
extern "C" Q_DECL_EXPORT
HashedForm<QV4::String *>::Type *ritual_ZN15QStringHashBase12hashedStringEPN3QV46StringE(
    QV4::String *s) {
  return new HashedForm<QV4::String *>::Type(
      QStringHashBase::hashedString(
          s));
}

//  HashedForm<const QV4::String *>::Type QStringHashBase::hashedString(const
//      QV4::String *s)
extern "C" Q_DECL_EXPORT
HashedForm<const QV4::String *>::Type *ritual_ZN15QStringHashBase12hashedStringEPKN3QV46StringE(
    const QV4::String *s) {
  return new HashedForm<const QV4::String *>::Type(
      QStringHashBase::hashedString(
          s));
}

//  HashedForm<QLatin1StringView>::Type
//      QStringHashBase::hashedString(QLatin1StringView s)
extern "C" Q_DECL_EXPORT
HashedForm<QLatin1StringView>::Type *ritual_ZN15QStringHashBase12hashedStringE13QLatin1String(
    const QLatin1String *s) {
  return new HashedForm<QLatin1StringView>::Type(
      QStringHashBase::hashedString(
          *s));
}

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

//  a HashedForm<QString>::Type a ritual of QStringHashBase gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QStringHashBase__HashedForm_QString_Type(
    HashedForm<QString>::Type *self) {
  delete self;
}

//  a HashedForm<QStringView>::Type a ritual of QStringHashBase gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QStringHashBase__HashedForm_QStringView_Type(
    HashedForm<QStringView>::Type *self) {
  delete self;
}

//  a HashedForm<QV4::String *>::Type a ritual of QStringHashBase gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QStringHashBase__HashedForm_QV4_String_Type(
    HashedForm<QV4::String *>::Type *self) {
  delete self;
}

//  a HashedForm<const QV4::String *>::Type a ritual of QStringHashBase gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QStringHashBase__HashedForm_const_QV4_String_Type(
    HashedForm<const QV4::String *>::Type *self) {
  delete self;
}

//  a HashedForm<QLatin1StringView>::Type a ritual of QStringHashBase gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QStringHashBase__HashedForm_QLatin1StringView_Type(
    HashedForm<QLatin1StringView>::Type *self) {
  delete self;
}

//  static quint32 QStringHashBase::hashOf<QString>(const QString &key)
extern "C" Q_DECL_EXPORT
unsigned int ritual_ZN15QStringHashBase6hashOfI7QStringEEjRKT_(
    const QString *key) {
  return QStringHashBase::hashOf<QString>(*key);
}

//  static quint32 QStringHashBase::hashOf<QStringView>(
//      const QStringView &key)
extern "C" Q_DECL_EXPORT
unsigned int ritual_ZN15QStringHashBase6hashOfI11QStringViewEEjRKT_(
    const QStringView *key) {
  return QStringHashBase::hashOf<QStringView>(*key);
}

//  static quint32 QStringHashBase::hashOf<QLatin1StringView>(
//      const QLatin1StringView &key)
extern "C" Q_DECL_EXPORT
unsigned int ritual_ZN15QStringHashBase6hashOfI13QLatin1StringEEjRKT_(
    const QLatin1StringView *key) {
  return QStringHashBase::hashOf<QLatin1StringView>(*key);
}
