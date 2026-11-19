//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qfile.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qfile.h>
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>

//  const QMetaObject *QFile::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK5QFile10metaObjectEv(const QFile *self) {
  return self->metaObject();
}

//  QString QFile::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN5QFile2trEPKcS1_i(const char *s, const char *c, int n) {
  return new QString(QFile::tr(s, c, n));
}

//  QFile::QFile()
extern "C" Q_DECL_EXPORT
QFile *ritual_ZN5QFileC1Ev() {
  return new QFile();
}

//  QFile::QFile(const QString &name)
extern "C" Q_DECL_EXPORT
QFile *ritual_ZN5QFileC1ERK7QString(const QString *name) {
  return new QFile(*name);
}

//  QFile::QFile(QObject *parent)
extern "C" Q_DECL_EXPORT
QFile *ritual_ZN5QFileC1EP7QObject(QObject *parent) {
  return new QFile(parent);
}

//  QFile::QFile(const QString &name, QObject *parent)
extern "C" Q_DECL_EXPORT
QFile *ritual_ZN5QFileC1ERK7QStringP7QObject(
    const QString *name,
    QObject *parent) {
  return new QFile(*name, parent);
}

//  QFile::~QFile()
extern "C" Q_DECL_EXPORT
void ritual_ZN5QFileD1Ev(QFile *self) {
  delete self;
}

//  QString QFile::fileName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK5QFile8fileNameEv(const QFile *self) {
  return new QString(self->fileName());
}

//  void QFile::setFileName(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN5QFile11setFileNameERK7QString(
    QFile *self,
    const QString *name) {
  self->setFileName(*name);
}

//  QByteArray QFile::encodeName(const QString &fileName)
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN5QFile10encodeNameERK7QString(const QString *fileName) {
  return new QByteArray(QFile::encodeName(*fileName));
}

//  QString QFile::decodeName(const QByteArray &localFileName)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN5QFile10decodeNameERK10QByteArray(
    const QByteArray *localFileName) {
  return new QString(QFile::decodeName(*localFileName));
}

//  QString QFile::decodeName(const char *localFileName)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN5QFile10decodeNameEPKc(const char *localFileName) {
  return new QString(QFile::decodeName(localFileName));
}

//  bool QFile::exists() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK5QFile6existsEv(const QFile *self) {
  return self->exists();
}

//  bool QFile::exists(const QString &fileName)
extern "C" Q_DECL_EXPORT
bool ritual_ZN5QFile6existsERK7QString(const QString *fileName) {
  return QFile::exists(*fileName);
}

//  QString QFile::symLinkTarget() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK5QFile13symLinkTargetEv(const QFile *self) {
  return new QString(self->symLinkTarget());
}

//  QString QFile::symLinkTarget(const QString &fileName)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN5QFile13symLinkTargetERK7QString(const QString *fileName) {
  return new QString(QFile::symLinkTarget(*fileName));
}

//  bool QFile::remove()
extern "C" Q_DECL_EXPORT
bool ritual_ZN5QFile6removeEv(QFile *self) {
  return self->remove();
}

//  bool QFile::remove(const QString &fileName)
extern "C" Q_DECL_EXPORT
bool ritual_ZN5QFile6removeERK7QString(const QString *fileName) {
  return QFile::remove(*fileName);
}

//  bool QFile::supportsMoveToTrash()
extern "C" Q_DECL_EXPORT
bool ritual_ZN5QFile19supportsMoveToTrashEv() {
  return QFile::supportsMoveToTrash();
}

//  bool QFile::moveToTrash()
extern "C" Q_DECL_EXPORT
bool ritual_ZN5QFile11moveToTrashEv(QFile *self) {
  return self->moveToTrash();
}

//  bool QFile::moveToTrash(const QString &fileName, QString *pathInTrash)
extern "C" Q_DECL_EXPORT
bool ritual_ZN5QFile11moveToTrashERK7QStringPS0_(
    const QString *fileName,
    QString *pathInTrash) {
  return QFile::moveToTrash(*fileName, pathInTrash);
}

//  bool QFile::rename(const QString &newName)
extern "C" Q_DECL_EXPORT
bool ritual_ZN5QFile6renameERK7QString(QFile *self, const QString *newName) {
  return self->rename(*newName);
}

//  bool QFile::rename(const QString &oldName, const QString &newName)
extern "C" Q_DECL_EXPORT
bool ritual_ZN5QFile6renameERK7QStringS2_(
    const QString *oldName,
    const QString *newName) {
  return QFile::rename(*oldName, *newName);
}

//  bool QFile::link(const QString &newName)
extern "C" Q_DECL_EXPORT
bool ritual_ZN5QFile4linkERK7QString(QFile *self, const QString *newName) {
  return self->link(*newName);
}

//  bool QFile::link(const QString &fileName, const QString &newName)
extern "C" Q_DECL_EXPORT
bool ritual_ZN5QFile4linkERK7QStringS2_(
    const QString *fileName,
    const QString *newName) {
  return QFile::link(*fileName, *newName);
}

//  bool QFile::open(OpenMode flags)
extern "C" Q_DECL_EXPORT
bool ritual_ZN5QFile4openE6QFlagsIN13QIODeviceBase12OpenModeFlagEE(
    QFile *self,
    int flags) {
  return self->open(QFlags<QIODeviceBase::OpenModeFlag>::fromInt(flags));
}

//  bool QFile::open(OpenMode flags, Permissions permissions)
extern "C" Q_DECL_EXPORT
bool ritual_ZN5QFile4openE6QFlagsIN13QIODeviceBase12OpenModeFlagEES0_IN11QFileDevice10PermissionEE(
    QFile *self,
    int flags,
    int permissions) {
  return self->open(
      QFlags<QIODeviceBase::OpenModeFlag>::fromInt(flags),
      QFlags<QFileDevice::Permission>::fromInt(permissions));
}

//  bool QFile::open(int fd, OpenMode ioFlags, FileHandleFlags handleFlags)
extern "C" Q_DECL_EXPORT
bool ritual_ZN5QFile4openEi6QFlagsIN13QIODeviceBase12OpenModeFlagEES0_IN11QFileDevice14FileHandleFlagEE(
    QFile *self,
    int fd,
    int ioFlags,
    int handleFlags) {
  return self->open(
      fd,
      QFlags<QIODeviceBase::OpenModeFlag>::fromInt(ioFlags),
      QFlags<QFileDevice::FileHandleFlag>::fromInt(handleFlags));
}

//  qint64 QFile::size() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK5QFile4sizeEv(const QFile *self) {
  return self->size();
}

//  bool QFile::resize(qint64 sz)
extern "C" Q_DECL_EXPORT
bool ritual_ZN5QFile6resizeEx(QFile *self, qint64 sz) {
  return self->resize(sz);
}

//  bool QFile::resize(const QString &filename, qint64 sz)
extern "C" Q_DECL_EXPORT
bool ritual_ZN5QFile6resizeERK7QStringx(const QString *filename, qint64 sz) {
  return QFile::resize(*filename, sz);
}

//  Permissions QFile::permissions() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK5QFile11permissionsEv(const QFile *self) {
  return static_cast<int>(self->permissions().toInt());
}

//  Permissions QFile::permissions(const QString &filename)
extern "C" Q_DECL_EXPORT
int ritual_ZN5QFile11permissionsERK7QString(const QString *filename) {
  return static_cast<int>(QFile::permissions(*filename).toInt());
}

//  bool QFile::setPermissions(Permissions permissionSpec)
extern "C" Q_DECL_EXPORT
bool ritual_ZN5QFile14setPermissionsE6QFlagsIN11QFileDevice10PermissionEE(
    QFile *self,
    int permissionSpec) {
  return self->setPermissions(
      QFlags<QFileDevice::Permission>::fromInt(permissionSpec));
}

//  bool QFile::setPermissions(const QString &filename, Permissions
//      permissionSpec)
extern "C" Q_DECL_EXPORT
bool ritual_ZN5QFile14setPermissionsERK7QString6QFlagsIN11QFileDevice10PermissionEE(
    const QString *filename,
    int permissionSpec) {
  return QFile::setPermissions(
      *filename,
      QFlags<QFileDevice::Permission>::fromInt(permissionSpec));
}
