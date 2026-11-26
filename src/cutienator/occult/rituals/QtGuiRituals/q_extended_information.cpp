//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qfileinfogatherer_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if QT_CONFIG(filesystemmodel)
#if QT_CONFIG(filesystemmodel)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qfileinfogatherer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qfileinfo.h>
#include <QtCore/qtimezone.h>
#include <QtCore/qdatetime.h>
#include <QtCore/QFile>

//  QExtendedInformation::QExtendedInformation()
extern "C" Q_DECL_EXPORT
QExtendedInformation *ritual_ZN20QExtendedInformationC1Ev() {
  return new QExtendedInformation();
}

//  QExtendedInformation::QExtendedInformation(const QFileInfo &info)
extern "C" Q_DECL_EXPORT
QExtendedInformation *ritual_ZN20QExtendedInformationC1ERK9QFileInfo(
    const QFileInfo *info) {
  return new QExtendedInformation(*info);
}

//  bool QExtendedInformation::isDir()
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QExtendedInformation5isDirEv(QExtendedInformation *self) {
  return self->isDir();
}

//  bool QExtendedInformation::isFile()
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QExtendedInformation6isFileEv(QExtendedInformation *self) {
  return self->isFile();
}

//  bool QExtendedInformation::isSystem()
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QExtendedInformation8isSystemEv(QExtendedInformation *self) {
  return self->isSystem();
}

//  bool QExtendedInformation::operator==(const QExtendedInformation
//      &fileInfo) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QExtendedInformationeqERKS_(
    const QExtendedInformation *self,
    const QExtendedInformation *fileInfo) {
  return self->operator==(*fileInfo);
}

#if !defined(QT_NO_FSFILEENGINE)
//  bool QExtendedInformation::isCaseSensitive() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QExtendedInformation15isCaseSensitiveEv(
    const QExtendedInformation *self) {
  return self->isCaseSensitive();
}
#endif  // !defined(QT_NO_FSFILEENGINE)

//  QFile::Permissions QExtendedInformation::permissions() const
extern "C" Q_DECL_EXPORT
QFile::Permissions *ritual_ZNK20QExtendedInformation11permissionsEv(
    const QExtendedInformation *self) {
  return new QFile::Permissions(self->permissions());
}

//  Type QExtendedInformation::type() const
extern "C" Q_DECL_EXPORT
QExtendedInformation::Type ritual_ZNK20QExtendedInformation4typeEv(
    const QExtendedInformation *self) {
  return self->type();
}

//  bool QExtendedInformation::isSymLink(bool ignoreNtfsSymLinks) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QExtendedInformation9isSymLinkEb(
    const QExtendedInformation *self,
    bool ignoreNtfsSymLinks) {
  return self->isSymLink(ignoreNtfsSymLinks);
}

//  bool QExtendedInformation::isHidden() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QExtendedInformation8isHiddenEv(
    const QExtendedInformation *self) {
  return self->isHidden();
}

//  QFileInfo QExtendedInformation::fileInfo() const
extern "C" Q_DECL_EXPORT
QFileInfo *ritual_ZNK20QExtendedInformation8fileInfoEv(
    const QExtendedInformation *self) {
  return new QFileInfo(self->fileInfo());
}

//  QDateTime QExtendedInformation::lastModified(const QTimeZone &tz) const
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZNK20QExtendedInformation12lastModifiedERK9QTimeZone(
    const QExtendedInformation *self,
    const QTimeZone *tz) {
  return new QDateTime(self->lastModified(*tz));
}

//  qint64 QExtendedInformation::size() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK20QExtendedInformation4sizeEv(
    const QExtendedInformation *self) {
  return self->size();
}

//  QExtendedInformation::~QExtendedInformation()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QExtendedInformationD1Ev(QExtendedInformation *self) {
  delete self;
}

//  a QFile::Permissions a ritual of QExtendedInformation gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QExtendedInformation__QFile_Permissions(
    QFile::Permissions *self) {
  delete self;
}

#endif  // QT_CONFIG(filesystemmodel)
#endif  // QT_CONFIG(filesystemmodel)
