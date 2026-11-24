//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qfilesystemmetadata_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qfilesystemmetadata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qdatetime.h>

//  QFileSystemMetaData::QFileSystemMetaData()
extern "C" Q_DECL_EXPORT
QFileSystemMetaData *ritual_ZN19QFileSystemMetaDataC1Ev() {
  return new QFileSystemMetaData();
}

//  bool QFileSystemMetaData::hasFlags(MetaDataFlags flags) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QFileSystemMetaData8hasFlagsE6QFlagsINS_12MetaDataFlagEE(
    const QFileSystemMetaData *self,
    int flags) {
  return self->hasFlags(
      QFlags<QFileSystemMetaData::MetaDataFlag>::fromInt(flags));
}

//  MetaDataFlags QFileSystemMetaData::missingFlags(MetaDataFlags flags)
extern "C" Q_DECL_EXPORT
int ritual_ZN19QFileSystemMetaData12missingFlagsE6QFlagsINS_12MetaDataFlagEE(
    QFileSystemMetaData *self,
    int flags) {
  return static_cast<int>(
      self->missingFlags(
          QFlags<QFileSystemMetaData::MetaDataFlag>::fromInt(flags)).toInt());
}

//  void QFileSystemMetaData::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QFileSystemMetaData5clearEv(QFileSystemMetaData *self) {
  self->clear();
}

//  void QFileSystemMetaData::clearFlags(MetaDataFlags flags)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QFileSystemMetaData10clearFlagsE6QFlagsINS_12MetaDataFlagEE(
    QFileSystemMetaData *self,
    int flags) {
  self->clearFlags(
      QFlags<QFileSystemMetaData::MetaDataFlag>::fromInt(flags));
}

//  bool QFileSystemMetaData::exists() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QFileSystemMetaData6existsEv(
    const QFileSystemMetaData *self) {
  return self->exists();
}

//  bool QFileSystemMetaData::isLink() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QFileSystemMetaData6isLinkEv(
    const QFileSystemMetaData *self) {
  return self->isLink();
}

//  bool QFileSystemMetaData::isFile() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QFileSystemMetaData6isFileEv(
    const QFileSystemMetaData *self) {
  return self->isFile();
}

//  bool QFileSystemMetaData::isDirectory() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QFileSystemMetaData11isDirectoryEv(
    const QFileSystemMetaData *self) {
  return self->isDirectory();
}

//  bool QFileSystemMetaData::isBundle() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QFileSystemMetaData8isBundleEv(
    const QFileSystemMetaData *self) {
  return self->isBundle();
}

//  bool QFileSystemMetaData::isAlias() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QFileSystemMetaData7isAliasEv(
    const QFileSystemMetaData *self) {
  return self->isAlias();
}

//  bool QFileSystemMetaData::isLegacyLink() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QFileSystemMetaData12isLegacyLinkEv(
    const QFileSystemMetaData *self) {
  return self->isLegacyLink();
}

//  bool QFileSystemMetaData::isSequential() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QFileSystemMetaData12isSequentialEv(
    const QFileSystemMetaData *self) {
  return self->isSequential();
}

//  bool QFileSystemMetaData::isHidden() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QFileSystemMetaData8isHiddenEv(
    const QFileSystemMetaData *self) {
  return self->isHidden();
}

//  bool QFileSystemMetaData::wasDeleted() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QFileSystemMetaData10wasDeletedEv(
    const QFileSystemMetaData *self) {
  return self->wasDeleted();
}

#if !(defined(Q_OS_WIN))
//  bool QFileSystemMetaData::isLnkFile() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QFileSystemMetaData9isLnkFileEv(
    const QFileSystemMetaData *self) {
  return self->isLnkFile();
}
#endif  // !(defined(Q_OS_WIN))

#if !(defined(Q_OS_WIN))
//  bool QFileSystemMetaData::isJunction() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QFileSystemMetaData10isJunctionEv(
    const QFileSystemMetaData *self) {
  return self->isJunction();
}
#endif  // !(defined(Q_OS_WIN))

//  qint64 QFileSystemMetaData::size() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK19QFileSystemMetaData4sizeEv(
    const QFileSystemMetaData *self) {
  return self->size();
}

//  void QFileSystemMetaData::setPermissions(QFile::Permissions permissions)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QFileSystemMetaData14setPermissionsE6QFlagsIN11QFileDevice10PermissionEE(
    QFileSystemMetaData *self,
    int permissions) {
  self->setPermissions(
      QFlags<QFileDevice::Permission>::fromInt(permissions));
}

//  QDateTime QFileSystemMetaData::accessTime() const
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZNK19QFileSystemMetaData10accessTimeEv(
    const QFileSystemMetaData *self) {
  return new QDateTime(self->accessTime());
}

//  QDateTime QFileSystemMetaData::birthTime() const
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZNK19QFileSystemMetaData9birthTimeEv(
    const QFileSystemMetaData *self) {
  return new QDateTime(self->birthTime());
}

//  QDateTime QFileSystemMetaData::metadataChangeTime() const
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZNK19QFileSystemMetaData18metadataChangeTimeEv(
    const QFileSystemMetaData *self) {
  return new QDateTime(self->metadataChangeTime());
}

//  QDateTime QFileSystemMetaData::modificationTime() const
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZNK19QFileSystemMetaData16modificationTimeEv(
    const QFileSystemMetaData *self) {
  return new QDateTime(self->modificationTime());
}

//  uint QFileSystemMetaData::userId() const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK19QFileSystemMetaData6userIdEv(
    const QFileSystemMetaData *self) {
  return self->userId();
}

//  uint QFileSystemMetaData::groupId() const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK19QFileSystemMetaData7groupIdEv(
    const QFileSystemMetaData *self) {
  return self->groupId();
}

//  uint QFileSystemMetaData::ownerId(QAbstractFileEngine::FileOwner owner)
//      const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK19QFileSystemMetaData7ownerIdEN19QAbstractFileEngine9FileOwnerE(
    const QFileSystemMetaData *self,
    QAbstractFileEngine::FileOwner owner) {
  return self->ownerId(owner);
}

//  bool QFileSystemMetaData::isReadable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QFileSystemMetaData10isReadableEv(
    const QFileSystemMetaData *self) {
  return self->isReadable();
}

//  bool QFileSystemMetaData::isWritable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QFileSystemMetaData10isWritableEv(
    const QFileSystemMetaData *self) {
  return self->isWritable();
}

//  bool QFileSystemMetaData::isExecutable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QFileSystemMetaData12isExecutableEv(
    const QFileSystemMetaData *self) {
  return self->isExecutable();
}

//  QFileSystemMetaData::~QFileSystemMetaData()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QFileSystemMetaDataD1Ev(QFileSystemMetaData *self) {
  delete self;
}
