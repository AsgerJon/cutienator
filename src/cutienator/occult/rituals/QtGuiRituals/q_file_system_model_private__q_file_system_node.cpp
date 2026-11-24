//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qfilesystemmodel_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if QT_CONFIG(filesystemmodel)
#if QT_CONFIG(filesystemmodel)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qfilesystemmodel_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qtimezone.h>
#include <QtCore/qdatetime.h>
#include <QtCore/qfileinfo.h>
#include <QtGui/qicon.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qfileinfogatherer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QFileSystemModelPrivate::QFileSystemNode::QFileSystemNode(const QString
//      &filename, QFileSystemNode *p)
extern "C" Q_DECL_EXPORT
QFileSystemModelPrivate::QFileSystemNode *ritual_ZN23QFileSystemModelPrivate15QFileSystemNodeC1ERK7QStringPS0_(
    const QString *filename,
    QFileSystemModelPrivate::QFileSystemNode *p) {
  return new QFileSystemModelPrivate::QFileSystemNode(*filename, p);
}

//  QFileSystemModelPrivate::QFileSystemNode::~QFileSystemNode()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QFileSystemModelPrivate15QFileSystemNodeD1Ev(
    QFileSystemModelPrivate::QFileSystemNode *self) {
  delete self;
}

//  qint64 QFileSystemModelPrivate::QFileSystemNode::size() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK23QFileSystemModelPrivate15QFileSystemNode4sizeEv(
    const QFileSystemModelPrivate::QFileSystemNode *self) {
  return self->size();
}

//  QString QFileSystemModelPrivate::QFileSystemNode::type() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK23QFileSystemModelPrivate15QFileSystemNode4typeEv(
    const QFileSystemModelPrivate::QFileSystemNode *self) {
  return new QString(self->type());
}

//  QDateTime QFileSystemModelPrivate::QFileSystemNode::lastModified(const
//      QTimeZone &tz) const
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZNK23QFileSystemModelPrivate15QFileSystemNode12lastModifiedERK9QTimeZone(
    const QFileSystemModelPrivate::QFileSystemNode *self,
    const QTimeZone *tz) {
  return new QDateTime(self->lastModified(*tz));
}

//  bool QFileSystemModelPrivate::QFileSystemNode::isReadable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QFileSystemModelPrivate15QFileSystemNode10isReadableEv(
    const QFileSystemModelPrivate::QFileSystemNode *self) {
  return self->isReadable();
}

//  bool QFileSystemModelPrivate::QFileSystemNode::isWritable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QFileSystemModelPrivate15QFileSystemNode10isWritableEv(
    const QFileSystemModelPrivate::QFileSystemNode *self) {
  return self->isWritable();
}

//  bool QFileSystemModelPrivate::QFileSystemNode::isExecutable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QFileSystemModelPrivate15QFileSystemNode12isExecutableEv(
    const QFileSystemModelPrivate::QFileSystemNode *self) {
  return self->isExecutable();
}

//  bool QFileSystemModelPrivate::QFileSystemNode::isDir() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QFileSystemModelPrivate15QFileSystemNode5isDirEv(
    const QFileSystemModelPrivate::QFileSystemNode *self) {
  return self->isDir();
}

//  QFileInfo QFileSystemModelPrivate::QFileSystemNode::fileInfo() const
extern "C" Q_DECL_EXPORT
QFileInfo *ritual_ZNK23QFileSystemModelPrivate15QFileSystemNode8fileInfoEv(
    const QFileSystemModelPrivate::QFileSystemNode *self) {
  return new QFileInfo(self->fileInfo());
}

//  bool QFileSystemModelPrivate::QFileSystemNode::isFile() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QFileSystemModelPrivate15QFileSystemNode6isFileEv(
    const QFileSystemModelPrivate::QFileSystemNode *self) {
  return self->isFile();
}

//  bool QFileSystemModelPrivate::QFileSystemNode::isSystem() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QFileSystemModelPrivate15QFileSystemNode8isSystemEv(
    const QFileSystemModelPrivate::QFileSystemNode *self) {
  return self->isSystem();
}

//  bool QFileSystemModelPrivate::QFileSystemNode::isHidden() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QFileSystemModelPrivate15QFileSystemNode8isHiddenEv(
    const QFileSystemModelPrivate::QFileSystemNode *self) {
  return self->isHidden();
}

//  bool QFileSystemModelPrivate::QFileSystemNode::isSymLink(bool
//      ignoreNtfsSymLinks) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QFileSystemModelPrivate15QFileSystemNode9isSymLinkEb(
    const QFileSystemModelPrivate::QFileSystemNode *self,
    bool ignoreNtfsSymLinks) {
  return self->isSymLink(ignoreNtfsSymLinks);
}

//  bool QFileSystemModelPrivate::QFileSystemNode::caseSensitive() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QFileSystemModelPrivate15QFileSystemNode13caseSensitiveEv(
    const QFileSystemModelPrivate::QFileSystemNode *self) {
  return self->caseSensitive();
}

//  QIcon QFileSystemModelPrivate::QFileSystemNode::icon() const
extern "C" Q_DECL_EXPORT
QIcon *ritual_ZNK23QFileSystemModelPrivate15QFileSystemNode4iconEv(
    const QFileSystemModelPrivate::QFileSystemNode *self) {
  return new QIcon(self->icon());
}

//  bool QFileSystemModelPrivate::QFileSystemNode::operator>(const QString
//      &name) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QFileSystemModelPrivate15QFileSystemNodegtERK7QString(
    const QFileSystemModelPrivate::QFileSystemNode *self,
    const QString *name) {
  return self->operator>(*name);
}

//  bool QFileSystemModelPrivate::QFileSystemNode::operator<(const QString
//      &name) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QFileSystemModelPrivate15QFileSystemNodeltERK7QString(
    const QFileSystemModelPrivate::QFileSystemNode *self,
    const QString *name) {
  return self->operator<(*name);
}

//  bool QFileSystemModelPrivate::QFileSystemNode::operator!=(const
//      QExtendedInformation &fileInfo) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QFileSystemModelPrivate15QFileSystemNodeneERK20QExtendedInformation(
    const QFileSystemModelPrivate::QFileSystemNode *self,
    const QExtendedInformation *fileInfo) {
  return self->operator!=(*fileInfo);
}

//  bool QFileSystemModelPrivate::QFileSystemNode::operator==(const QString
//      &name) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QFileSystemModelPrivate15QFileSystemNodeeqERK7QString(
    const QFileSystemModelPrivate::QFileSystemNode *self,
    const QString *name) {
  return self->operator==(*name);
}

//  bool QFileSystemModelPrivate::QFileSystemNode::operator==(const
//      QExtendedInformation &fileInfo) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QFileSystemModelPrivate15QFileSystemNodeeqERK20QExtendedInformation(
    const QFileSystemModelPrivate::QFileSystemNode *self,
    const QExtendedInformation *fileInfo) {
  return self->operator==(*fileInfo);
}

//  bool QFileSystemModelPrivate::QFileSystemNode::hasInformation() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QFileSystemModelPrivate15QFileSystemNode14hasInformationEv(
    const QFileSystemModelPrivate::QFileSystemNode *self) {
  return self->hasInformation();
}

//  void QFileSystemModelPrivate::QFileSystemNode::populate(const
//      QExtendedInformation &fileInfo)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QFileSystemModelPrivate15QFileSystemNode8populateERK20QExtendedInformation(
    QFileSystemModelPrivate::QFileSystemNode *self,
    const QExtendedInformation *fileInfo) {
  self->populate(*fileInfo);
}

//  int QFileSystemModelPrivate::QFileSystemNode::visibleLocation(const
//      QString &childName)
extern "C" Q_DECL_EXPORT
int ritual_ZN23QFileSystemModelPrivate15QFileSystemNode15visibleLocationERK7QString(
    QFileSystemModelPrivate::QFileSystemNode *self,
    const QString *childName) {
  return self->visibleLocation(*childName);
}

//  void QFileSystemModelPrivate::QFileSystemNode::updateIcon(QAbstractFileIc
//      onProvider *iconProvider, const QString &path)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QFileSystemModelPrivate15QFileSystemNode10updateIconEP25QAbstractFileIconProviderRK7QString(
    QFileSystemModelPrivate::QFileSystemNode *self,
    QAbstractFileIconProvider *iconProvider,
    const QString *path) {
  self->updateIcon(iconProvider, *path);
}

//  void QFileSystemModelPrivate::QFileSystemNode::retranslateStrings(QAbstra
//      ctFileIconProvider *iconProvider, const QString &path)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QFileSystemModelPrivate15QFileSystemNode18retranslateStringsEP25QAbstractFileIconProviderRK7QString(
    QFileSystemModelPrivate::QFileSystemNode *self,
    QAbstractFileIconProvider *iconProvider,
    const QString *path) {
  self->retranslateStrings(iconProvider, *path);
}

#endif  // QT_CONFIG(filesystemmodel)
#endif  // QT_CONFIG(filesystemmodel)
