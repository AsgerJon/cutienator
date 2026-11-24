//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qsystemsemaphore.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qglobal.h>
#if QT_CONFIG(systemsemaphore)
#include <QtCore/qsystemsemaphore.h>
#include <QtCore/qstring.h>
#include <QtCore/qtipccommon.h>

//  QString QSystemSemaphore::tr(const char *sourceText, const char
//      *disambiguation, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QSystemSemaphore2trEPKcS1_i(
    const char *sourceText,
    const char *disambiguation,
    int n) {
  return new QString(QSystemSemaphore::tr(sourceText, disambiguation, n));
}

//  QSystemSemaphore::QSystemSemaphore(const QNativeIpcKey &key, int
//      initialValue, AccessMode a2)
extern "C" Q_DECL_EXPORT
QSystemSemaphore *ritual_ZN16QSystemSemaphoreC1ERK13QNativeIpcKeyiNS_10AccessModeE(
    const QNativeIpcKey *key,
    int initialValue,
    QSystemSemaphore::AccessMode a2) {
  return new QSystemSemaphore(*key, initialValue, a2);
}

//  QSystemSemaphore::~QSystemSemaphore()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSystemSemaphoreD1Ev(QSystemSemaphore *self) {
  delete self;
}

//  void QSystemSemaphore::setNativeKey(const QNativeIpcKey &key, int
//      initialValue, AccessMode a2)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSystemSemaphore12setNativeKeyERK13QNativeIpcKeyiNS_10AccessModeE(
    QSystemSemaphore *self,
    const QNativeIpcKey *key,
    int initialValue,
    QSystemSemaphore::AccessMode a2) {
  self->setNativeKey(*key, initialValue, a2);
}

//  void QSystemSemaphore::setNativeKey(const QString &key, int initialValue,
//      AccessMode mode, QNativeIpcKey::Type type)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSystemSemaphore12setNativeKeyERK7QStringiNS_10AccessModeEN13QNativeIpcKey4TypeE(
    QSystemSemaphore *self,
    const QString *key,
    int initialValue,
    QSystemSemaphore::AccessMode mode,
    QNativeIpcKey::Type type) {
  self->setNativeKey(*key, initialValue, mode, type);
}

//  QNativeIpcKey QSystemSemaphore::nativeIpcKey() const
extern "C" Q_DECL_EXPORT
QNativeIpcKey *ritual_ZNK16QSystemSemaphore12nativeIpcKeyEv(
    const QSystemSemaphore *self) {
  return new QNativeIpcKey(self->nativeIpcKey());
}

//  QSystemSemaphore::QSystemSemaphore(const QString &key, int initialValue,
//      AccessMode mode)
extern "C" Q_DECL_EXPORT
QSystemSemaphore *ritual_ZN16QSystemSemaphoreC1ERK7QStringiNS_10AccessModeE(
    const QString *key,
    int initialValue,
    QSystemSemaphore::AccessMode mode) {
  return new QSystemSemaphore(*key, initialValue, mode);
}

//  void QSystemSemaphore::setKey(const QString &key, int initialValue,
//      AccessMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSystemSemaphore6setKeyERK7QStringiNS_10AccessModeE(
    QSystemSemaphore *self,
    const QString *key,
    int initialValue,
    QSystemSemaphore::AccessMode mode) {
  self->setKey(*key, initialValue, mode);
}

//  QString QSystemSemaphore::key() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK16QSystemSemaphore3keyEv(const QSystemSemaphore *self) {
  return new QString(self->key());
}

//  bool QSystemSemaphore::acquire()
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QSystemSemaphore7acquireEv(QSystemSemaphore *self) {
  return self->acquire();
}

//  bool QSystemSemaphore::release(int n)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QSystemSemaphore7releaseEi(QSystemSemaphore *self, int n) {
  return self->release(n);
}

//  SystemSemaphoreError QSystemSemaphore::error() const
extern "C" Q_DECL_EXPORT
QSystemSemaphore::SystemSemaphoreError ritual_ZNK16QSystemSemaphore5errorEv(
    const QSystemSemaphore *self) {
  return self->error();
}

//  QString QSystemSemaphore::errorString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK16QSystemSemaphore11errorStringEv(
    const QSystemSemaphore *self) {
  return new QString(self->errorString());
}

//  bool QSystemSemaphore::isKeyTypeSupported(QNativeIpcKey::Type type)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QSystemSemaphore18isKeyTypeSupportedEN13QNativeIpcKey4TypeE(
    QNativeIpcKey::Type type) {
  return QSystemSemaphore::isKeyTypeSupported(type);
}

//  QNativeIpcKey QSystemSemaphore::platformSafeKey(const QString &key,
//      QNativeIpcKey::Type type)
extern "C" Q_DECL_EXPORT
QNativeIpcKey *ritual_ZN16QSystemSemaphore15platformSafeKeyERK7QStringN13QNativeIpcKey4TypeE(
    const QString *key,
    QNativeIpcKey::Type type) {
  return new QNativeIpcKey(QSystemSemaphore::platformSafeKey(*key, type));
}

//  QNativeIpcKey QSystemSemaphore::legacyNativeKey(const QString &key,
//      QNativeIpcKey::Type type)
extern "C" Q_DECL_EXPORT
QNativeIpcKey *ritual_ZN16QSystemSemaphore15legacyNativeKeyERK7QStringN13QNativeIpcKey4TypeE(
    const QString *key,
    QNativeIpcKey::Type type) {
  return new QNativeIpcKey(QSystemSemaphore::legacyNativeKey(*key, type));
}

#endif  // QT_CONFIG(systemsemaphore)
