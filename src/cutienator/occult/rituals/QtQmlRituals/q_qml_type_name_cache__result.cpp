//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmltypenamecache_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmltypenamecache_p.h>
#include <QtQml/6.12.0/QtQml/private/qqmltype_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QQmlTypeNameCache::Result::Result()
extern "C" Q_DECL_EXPORT
QQmlTypeNameCache::Result *ritual_ZN17QQmlTypeNameCache6ResultC1Ev() {
  return new QQmlTypeNameCache::Result();
}

//  QQmlTypeNameCache::Result::Result(const QQmlImportRef *importNamespace)
extern "C" Q_DECL_EXPORT
QQmlTypeNameCache::Result *ritual_ZN17QQmlTypeNameCache6ResultC1EPK13QQmlImportRef(
    const QQmlImportRef *importNamespace) {
  return new QQmlTypeNameCache::Result(importNamespace);
}

//  QQmlTypeNameCache::Result::Result(const QQmlType &type)
extern "C" Q_DECL_EXPORT
QQmlTypeNameCache::Result *ritual_ZN17QQmlTypeNameCache6ResultC1ERK8QQmlType(
    const QQmlType *type) {
  return new QQmlTypeNameCache::Result(*type);
}

//  QQmlTypeNameCache::Result::Result(int scriptIndex)
extern "C" Q_DECL_EXPORT
QQmlTypeNameCache::Result *ritual_ZN17QQmlTypeNameCache6ResultC1Ei(
    int scriptIndex) {
  return new QQmlTypeNameCache::Result(scriptIndex);
}

//  bool QQmlTypeNameCache::Result::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QQmlTypeNameCache6Result7isValidEv(
    const QQmlTypeNameCache::Result *self) {
  return self->isValid();
}

//  QQmlTypeNameCache::Result::~Result()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlTypeNameCache6ResultD1Ev(
    QQmlTypeNameCache::Result *self) {
  delete self;
}
