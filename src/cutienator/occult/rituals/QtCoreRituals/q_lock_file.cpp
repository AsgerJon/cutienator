//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qlockfile.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qlockfile.h>
#include <QtCore/qstring.h>

//  QLockFile::QLockFile(const QString &fileName)
extern "C" Q_DECL_EXPORT
QLockFile *ritual_ZN9QLockFileC1ERK7QString(const QString *fileName) {
  return new QLockFile(*fileName);
}

//  QLockFile::~QLockFile()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QLockFileD1Ev(QLockFile *self) {
  delete self;
}

//  QString QLockFile::fileName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QLockFile8fileNameEv(const QLockFile *self) {
  return new QString(self->fileName());
}

//  bool QLockFile::lock()
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QLockFile4lockEv(QLockFile *self) {
  return self->lock();
}

//  bool QLockFile::tryLock(int timeout)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QLockFile7tryLockEi(QLockFile *self, int timeout) {
  return self->tryLock(timeout);
}

//  void QLockFile::unlock()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QLockFile6unlockEv(QLockFile *self) {
  self->unlock();
}

//  void QLockFile::setStaleLockTime(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QLockFile16setStaleLockTimeEi(QLockFile *self, int a0) {
  self->setStaleLockTime(a0);
}

//  int QLockFile::staleLockTime() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QLockFile13staleLockTimeEv(const QLockFile *self) {
  return self->staleLockTime();
}

//  bool QLockFile::isLocked() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QLockFile8isLockedEv(const QLockFile *self) {
  return self->isLocked();
}

//  bool QLockFile::getLockInfo(qint64 *pid, QString *hostname, QString
//      *appname) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QLockFile11getLockInfoEPxP7QStringS2_(
    const QLockFile *self,
    qint64 *pid,
    QString *hostname,
    QString *appname) {
  return self->getLockInfo(pid, hostname, appname);
}

//  bool QLockFile::removeStaleLockFile()
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QLockFile19removeStaleLockFileEv(QLockFile *self) {
  return self->removeStaleLockFile();
}

//  LockError QLockFile::error() const
extern "C" Q_DECL_EXPORT
QLockFile::LockError ritual_ZNK9QLockFile5errorEv(const QLockFile *self) {
  return self->error();
}

//  QLockFilePrivate *QLockFile::d_func()
extern "C" Q_DECL_EXPORT
QLockFilePrivate *ritual_ZN9QLockFile6d_funcEv(QLockFile *self) {
  return self->d_func();
}

//  const QLockFilePrivate *QLockFile::d_func() const
extern "C" Q_DECL_EXPORT
const QLockFilePrivate *ritual_ZNK9QLockFile6d_funcEv(
    const QLockFile *self) {
  return self->d_func();
}
