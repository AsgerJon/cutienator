//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljsimporter_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtQmlCompiler/QtQmlCompiler>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljsimporter_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qtyperevision.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlCompiler/private/qqmljsimporter_p.h>
#include <QtQmlCompiler/private/qqmljstypedescriptionreader_p.h>
#include <QtQmlCompiler/private/qqmljstypereader_p.h>
#include <QtQmlCompiler/private/qqmljsimportvisitor_p.h>
#include <QtQmlCompiler/private/qqmljslogger_p.h>
#include <QtQmlCompiler/private/qqmljsutils_p.h>
#include <QtQml/private/qqmlimportresolver_p.h>
#include <QtCore/qfileinfo.h>
#include <QtCore/qdiriterator.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from ../qtdeclarative/src/qmlcompiler/qqmljsimporter.cpp, line 26, as _ZN6QQmlJS6ImportC1E7QStringS1_13QTypeRevisionbb
inline QQmlJS::Import::Import(QString prefix, QString name, QTypeRevision version, bool isFile,
                       bool isDependency) :
      m_prefix(std::move(prefix)),
      m_name(std::move(name)),
      m_version(version),
      m_isFile(isFile),
      m_isDependency(isDependency)
{
}

//  from ../qtdeclarative/src/qmlcompiler/qqmljsimporter.cpp, line 36, as _ZNK6QQmlJS6Import7isValidEv
inline bool QQmlJS::Import::isValid() const
{
    return !m_name.isEmpty();
}
//  -----------------------------------------------------------------------

//  QQmlJS::Import::Import()
extern "C" Q_DECL_EXPORT
QQmlJS::Import *ritual_ZN6QQmlJS6ImportC1Ev() {
  return new QQmlJS::Import();
}

//  QQmlJS::Import::Import(QString prefix, QString name, QTypeRevision
//      version, bool isFile, bool isDependency)
extern "C" Q_DECL_EXPORT
QQmlJS::Import *ritual_ZN6QQmlJS6ImportC1E7QStringS1_13QTypeRevisionbb(
    const QString *prefix,
    const QString *name,
    const QTypeRevision *version,
    bool isFile,
    bool isDependency) {
  return new QQmlJS::Import(*prefix, *name, *version, isFile, isDependency);
}

//  bool QQmlJS::Import::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK6QQmlJS6Import7isValidEv(const QQmlJS::Import *self) {
  return self->isValid();
}

//  QString QQmlJS::Import::prefix() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK6QQmlJS6Import6prefixEv(const QQmlJS::Import *self) {
  return new QString(self->prefix());
}

//  QString QQmlJS::Import::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK6QQmlJS6Import4nameEv(const QQmlJS::Import *self) {
  return new QString(self->name());
}

//  QTypeRevision QQmlJS::Import::version() const
extern "C" Q_DECL_EXPORT
QTypeRevision *ritual_ZNK6QQmlJS6Import7versionEv(
    const QQmlJS::Import *self) {
  return new QTypeRevision(self->version());
}

//  bool QQmlJS::Import::isFile() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK6QQmlJS6Import6isFileEv(const QQmlJS::Import *self) {
  return self->isFile();
}

//  bool QQmlJS::Import::isDependency() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK6QQmlJS6Import12isDependencyEv(const QQmlJS::Import *self) {
  return self->isDependency();
}

//  bool operator==(const Import &a, const Import &b)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJSeqERKNS_6ImportES2_(
    const QQmlJS::Import *a,
    const QQmlJS::Import *b) {
  return operator==(*a, *b);
}

//  QQmlJS::Import::~Import()
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS6ImportD1Ev(QQmlJS::Import *self) {
  delete self;
}
