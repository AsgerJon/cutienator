//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qtipccommon.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qglobal.h>
#if QT_CONFIG(sharedmemory) || QT_CONFIG(systemsemaphore)
#include <QtCore/qtipccommon.h>
#include <QtCore/qstring.h>

//  Type QNativeIpcKey::legacyDefaultTypeForOs()
extern "C" Q_DECL_EXPORT
QNativeIpcKey::Type ritual_ZN13QNativeIpcKey22legacyDefaultTypeForOsEv() {
  return QNativeIpcKey::legacyDefaultTypeForOs();
}

//  QNativeIpcKey::QNativeIpcKey()
extern "C" Q_DECL_EXPORT
QNativeIpcKey *ritual_ZN13QNativeIpcKeyC1Ev() {
  return new QNativeIpcKey();
}

//  QNativeIpcKey::QNativeIpcKey(Type type)
extern "C" Q_DECL_EXPORT
QNativeIpcKey *ritual_ZN13QNativeIpcKeyC1ENS_4TypeE(
    QNativeIpcKey::Type type) {
  return new QNativeIpcKey(type);
}

//  QNativeIpcKey::QNativeIpcKey(const QString &k, Type type)
extern "C" Q_DECL_EXPORT
QNativeIpcKey *ritual_ZN13QNativeIpcKeyC1ERK7QStringNS_4TypeE(
    const QString *k,
    QNativeIpcKey::Type type) {
  return new QNativeIpcKey(*k, type);
}

//  QNativeIpcKey::QNativeIpcKey(const QNativeIpcKey &other)
extern "C" Q_DECL_EXPORT
QNativeIpcKey *ritual_ZN13QNativeIpcKeyC1ERKS_(const QNativeIpcKey *other) {
  return new QNativeIpcKey(*other);
}

//  QNativeIpcKey::~QNativeIpcKey()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QNativeIpcKeyD1Ev(QNativeIpcKey *self) {
  delete self;
}

//  bool QNativeIpcKey::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QNativeIpcKey7isEmptyEv(const QNativeIpcKey *self) {
  return self->isEmpty();
}

//  bool QNativeIpcKey::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QNativeIpcKey7isValidEv(const QNativeIpcKey *self) {
  return self->isValid();
}

//  Type QNativeIpcKey::type() const
extern "C" Q_DECL_EXPORT
QNativeIpcKey::Type ritual_ZNK13QNativeIpcKey4typeEv(
    const QNativeIpcKey *self) {
  return self->type();
}

//  void QNativeIpcKey::setType(Type type)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QNativeIpcKey7setTypeENS_4TypeE(
    QNativeIpcKey *self,
    QNativeIpcKey::Type type) {
  self->setType(type);
}

//  QString QNativeIpcKey::nativeKey() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK13QNativeIpcKey9nativeKeyEv(const QNativeIpcKey *self) {
  return new QString(self->nativeKey());
}

//  void QNativeIpcKey::setNativeKey(const QString &newKey)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QNativeIpcKey12setNativeKeyERK7QString(
    QNativeIpcKey *self,
    const QString *newKey) {
  self->setNativeKey(*newKey);
}

//  QString QNativeIpcKey::toString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK13QNativeIpcKey8toStringEv(const QNativeIpcKey *self) {
  return new QString(self->toString());
}

//  QNativeIpcKey QNativeIpcKey::fromString(const QString &string)
extern "C" Q_DECL_EXPORT
QNativeIpcKey *ritual_ZN13QNativeIpcKey10fromStringERK7QString(
    const QString *string) {
  return new QNativeIpcKey(QNativeIpcKey::fromString(*string));
}

//  bool QNativeIpcKey::isSlowPath() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QNativeIpcKey10isSlowPathEv(const QNativeIpcKey *self) {
  return self->isSlowPath();
}

//  void QNativeIpcKey::copy_internal(const QNativeIpcKey &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QNativeIpcKey13copy_internalERKS_(
    QNativeIpcKey *self,
    const QNativeIpcKey *other) {
  self->copy_internal(*other);
}

//  void QNativeIpcKey::destroy_internal()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QNativeIpcKey16destroy_internalEv(QNativeIpcKey *self) {
  self->destroy_internal();
}

//  void QNativeIpcKey::setType_internal(Type a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QNativeIpcKey16setType_internalENS_4TypeE(
    QNativeIpcKey *self,
    QNativeIpcKey::Type a0) {
  self->setType_internal(a0);
}

//  void QNativeIpcKey::setNativeKey_internal(const QString &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QNativeIpcKey21setNativeKey_internalERK7QString(
    QNativeIpcKey *self,
    const QString *a0) {
  self->setNativeKey_internal(*a0);
}

//  int QNativeIpcKey::compare_internal(const QNativeIpcKey &lhs, const
//      QNativeIpcKey &rhs)
extern "C" Q_DECL_EXPORT
int ritual_ZN13QNativeIpcKey16compare_internalERKS_S1_(
    const QNativeIpcKey *lhs,
    const QNativeIpcKey *rhs) {
  return QNativeIpcKey::compare_internal(*lhs, *rhs);
}

//  bool operator==(const QNativeIpcKey &lhs, const QNativeIpcKey &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK13QNativeIpcKeyS1_(
    const QNativeIpcKey *lhs,
    const QNativeIpcKey *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QNativeIpcKey &lhs, const QNativeIpcKey &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK13QNativeIpcKeyS1_(
    const QNativeIpcKey *lhs,
    const QNativeIpcKey *rhs) {
  return operator!=(*lhs, *rhs);
}

#endif  // QT_CONFIG(sharedmemory) || QT_CONFIG(systemsemaphore)
