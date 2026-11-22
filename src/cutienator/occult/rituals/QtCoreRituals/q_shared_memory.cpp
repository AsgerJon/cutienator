//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qsharedmemory.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qsharedmemory.h>
#include <QtCore/qstring.h>
#include <QtCore/qtipccommon.h>

//  const QMetaObject *QSharedMemory::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13QSharedMemory10metaObjectEv(
    const QSharedMemory *self) {
  return self->metaObject();
}

//  QString QSharedMemory::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13QSharedMemory2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QSharedMemory::tr(s, c, n));
}

//  QSharedMemory::QSharedMemory(QObject *parent)
extern "C" Q_DECL_EXPORT
QSharedMemory *ritual_ZN13QSharedMemoryC1EP7QObject(QObject *parent) {
  return new QSharedMemory(parent);
}

//  QSharedMemory::QSharedMemory(const QNativeIpcKey &key, QObject *parent)
extern "C" Q_DECL_EXPORT
QSharedMemory *ritual_ZN13QSharedMemoryC1ERK13QNativeIpcKeyP7QObject(
    const QNativeIpcKey *key,
    QObject *parent) {
  return new QSharedMemory(*key, parent);
}

//  QSharedMemory::~QSharedMemory()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSharedMemoryD1Ev(QSharedMemory *self) {
  delete self;
}

//  QSharedMemory::QSharedMemory(const QString &key, QObject *parent)
extern "C" Q_DECL_EXPORT
QSharedMemory *ritual_ZN13QSharedMemoryC1ERK7QStringP7QObject(
    const QString *key,
    QObject *parent) {
  return new QSharedMemory(*key, parent);
}

//  void QSharedMemory::setKey(const QString &key)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSharedMemory6setKeyERK7QString(
    QSharedMemory *self,
    const QString *key) {
  self->setKey(*key);
}

//  QString QSharedMemory::key() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK13QSharedMemory3keyEv(const QSharedMemory *self) {
  return new QString(self->key());
}

//  void QSharedMemory::setNativeKey(const QNativeIpcKey &key)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSharedMemory12setNativeKeyERK13QNativeIpcKey(
    QSharedMemory *self,
    const QNativeIpcKey *key) {
  self->setNativeKey(*key);
}

//  void QSharedMemory::setNativeKey(const QString &key, QNativeIpcKey::Type
//      type)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSharedMemory12setNativeKeyERK7QStringN13QNativeIpcKey4TypeE(
    QSharedMemory *self,
    const QString *key,
    QNativeIpcKey::Type type) {
  self->setNativeKey(*key, type);
}

//  QString QSharedMemory::nativeKey() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK13QSharedMemory9nativeKeyEv(const QSharedMemory *self) {
  return new QString(self->nativeKey());
}

//  QNativeIpcKey QSharedMemory::nativeIpcKey() const
extern "C" Q_DECL_EXPORT
QNativeIpcKey *ritual_ZNK13QSharedMemory12nativeIpcKeyEv(
    const QSharedMemory *self) {
  return new QNativeIpcKey(self->nativeIpcKey());
}

//  bool QSharedMemory::create(qsizetype size, AccessMode mode)
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QSharedMemory6createExNS_10AccessModeE(
    QSharedMemory *self,
    qsizetype size,
    QSharedMemory::AccessMode mode) {
  return self->create(size, mode);
}

//  qsizetype QSharedMemory::size() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK13QSharedMemory4sizeEv(const QSharedMemory *self) {
  return self->size();
}

//  bool QSharedMemory::attach(AccessMode mode)
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QSharedMemory6attachENS_10AccessModeE(
    QSharedMemory *self,
    QSharedMemory::AccessMode mode) {
  return self->attach(mode);
}

//  bool QSharedMemory::isAttached() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QSharedMemory10isAttachedEv(const QSharedMemory *self) {
  return self->isAttached();
}

//  bool QSharedMemory::detach()
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QSharedMemory6detachEv(QSharedMemory *self) {
  return self->detach();
}

//  bool QSharedMemory::lock()
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QSharedMemory4lockEv(QSharedMemory *self) {
  return self->lock();
}

//  bool QSharedMemory::unlock()
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QSharedMemory6unlockEv(QSharedMemory *self) {
  return self->unlock();
}

//  SharedMemoryError QSharedMemory::error() const
extern "C" Q_DECL_EXPORT
QSharedMemory::SharedMemoryError ritual_ZNK13QSharedMemory5errorEv(
    const QSharedMemory *self) {
  return self->error();
}

//  QString QSharedMemory::errorString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK13QSharedMemory11errorStringEv(
    const QSharedMemory *self) {
  return new QString(self->errorString());
}

//  bool QSharedMemory::isKeyTypeSupported(QNativeIpcKey::Type type)
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QSharedMemory18isKeyTypeSupportedEN13QNativeIpcKey4TypeE(
    QNativeIpcKey::Type type) {
  return QSharedMemory::isKeyTypeSupported(type);
}

//  QNativeIpcKey QSharedMemory::platformSafeKey(const QString &key,
//      QNativeIpcKey::Type type)
extern "C" Q_DECL_EXPORT
QNativeIpcKey *ritual_ZN13QSharedMemory15platformSafeKeyERK7QStringN13QNativeIpcKey4TypeE(
    const QString *key,
    QNativeIpcKey::Type type) {
  return new QNativeIpcKey(QSharedMemory::platformSafeKey(*key, type));
}

//  QNativeIpcKey QSharedMemory::legacyNativeKey(const QString &key,
//      QNativeIpcKey::Type type)
extern "C" Q_DECL_EXPORT
QNativeIpcKey *ritual_ZN13QSharedMemory15legacyNativeKeyERK7QStringN13QNativeIpcKey4TypeE(
    const QString *key,
    QNativeIpcKey::Type type) {
  return new QNativeIpcKey(QSharedMemory::legacyNativeKey(*key, type));
}
