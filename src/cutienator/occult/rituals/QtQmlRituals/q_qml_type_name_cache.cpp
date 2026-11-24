//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmltypenamecache_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmltypenamecache_p.h>
#include <QtQml/6.12.0/QtQml/private/qhashedstring_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qurl.h>
#include <QtCore/qstring.h>

//  QQmlTypeNameCache::~QQmlTypeNameCache()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlTypeNameCacheD1Ev(QQmlTypeNameCache *self) {
  delete self;
}

//  bool QQmlTypeNameCache::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QQmlTypeNameCache7isEmptyEv(const QQmlTypeNameCache *self) {
  return self->isEmpty();
}

//  void QQmlTypeNameCache::add(const QHashedString &name, int sciptIndex,
//      const QHashedString &nameSpace)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlTypeNameCache3addERK13QHashedStringiS2_(
    QQmlTypeNameCache *self,
    const QHashedString *name,
    int sciptIndex,
    const QHashedString *nameSpace) {
  self->add(*name, sciptIndex, *nameSpace);
}

//  void QQmlTypeNameCache::add(const QHashedString &name, const QUrl &url,
//      const QHashedString &nameSpace)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlTypeNameCache3addERK13QHashedStringRK4QUrlS2_(
    QQmlTypeNameCache *self,
    const QHashedString *name,
    const QUrl *url,
    const QHashedString *nameSpace) {
  self->add(*name, *url, *nameSpace);
}

//  QHashedStringRef QQmlTypeNameCache::toHashedStringRef(const
//      QHashedStringRef &key)
extern "C" Q_DECL_EXPORT
QHashedStringRef *ritual_ZN17QQmlTypeNameCache17toHashedStringRefERK16QHashedStringRef(
    const QHashedStringRef *key) {
  return new QHashedStringRef(QQmlTypeNameCache::toHashedStringRef(*key));
}

//  QHashedStringRef QQmlTypeNameCache::toHashedStringRef(const QV4::String
//      *key)
extern "C" Q_DECL_EXPORT
QHashedStringRef *ritual_ZN17QQmlTypeNameCache17toHashedStringRefEPKN3QV46StringE(
    const QV4::String *key) {
  return new QHashedStringRef(QQmlTypeNameCache::toHashedStringRef(key));
}

//  QString QQmlTypeNameCache::toQString(const QHashedStringRef &key)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QQmlTypeNameCache9toQStringERK16QHashedStringRef(
    const QHashedStringRef *key) {
  return new QString(QQmlTypeNameCache::toQString(*key));
}

//  QString QQmlTypeNameCache::toQString(const QV4::String *key)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QQmlTypeNameCache9toQStringEPKN3QV46StringE(
    const QV4::String *key) {
  return new QString(QQmlTypeNameCache::toQString(key));
}
