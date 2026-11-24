//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmlpropertycachevector_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlpropertycachevector_p.h>
#include <QtQml/6.12.0/QtQml/private/qqmlpropertycache_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QQmlPropertyCacheVector::QQmlPropertyCacheVector()
extern "C" Q_DECL_EXPORT
QQmlPropertyCacheVector *ritual_ZN23QQmlPropertyCacheVectorC1Ev() {
  return new QQmlPropertyCacheVector();
}

//  QQmlPropertyCacheVector::~QQmlPropertyCacheVector()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQmlPropertyCacheVectorD1Ev(QQmlPropertyCacheVector *self) {
  delete self;
}

//  void QQmlPropertyCacheVector::resize(int size)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQmlPropertyCacheVector6resizeEi(
    QQmlPropertyCacheVector *self,
    int size) {
  self->resize(size);
}

//  int QQmlPropertyCacheVector::count() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK23QQmlPropertyCacheVector5countEv(
    const QQmlPropertyCacheVector *self) {
  return self->count();
}

//  bool QQmlPropertyCacheVector::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QQmlPropertyCacheVector7isEmptyEv(
    const QQmlPropertyCacheVector *self) {
  return self->isEmpty();
}

//  void QQmlPropertyCacheVector::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQmlPropertyCacheVector5clearEv(
    QQmlPropertyCacheVector *self) {
  self->clear();
}

//  void QQmlPropertyCacheVector::resetAndResize(int size)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQmlPropertyCacheVector14resetAndResizeEi(
    QQmlPropertyCacheVector *self,
    int size) {
  self->resetAndResize(size);
}

//  void QQmlPropertyCacheVector::append(const QQmlPropertyCache::ConstPtr
//      &cache)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQmlPropertyCacheVector6appendERKN17QQmlPropertyCache8ConstPtrE(
    QQmlPropertyCacheVector *self,
    const QQmlPropertyCache::ConstPtr *cache) {
  self->append(*cache);
}

//  QQmlPropertyCache::ConstPtr QQmlPropertyCacheVector::at(int index) const
extern "C" Q_DECL_EXPORT
QQmlPropertyCache::ConstPtr *ritual_ZNK23QQmlPropertyCacheVector2atEi(
    const QQmlPropertyCacheVector *self,
    int index) {
  return new QQmlPropertyCache::ConstPtr(self->at(index));
}

//  void QQmlPropertyCacheVector::set(int index, const
//      QQmlPropertyCache::ConstPtr &replacement)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQmlPropertyCacheVector3setEiRKN17QQmlPropertyCache8ConstPtrE(
    QQmlPropertyCacheVector *self,
    int index,
    const QQmlPropertyCache::ConstPtr *replacement) {
  self->set(index, *replacement);
}

//  void QQmlPropertyCacheVector::setNeedsVMEMetaObject(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQmlPropertyCacheVector21setNeedsVMEMetaObjectEi(
    QQmlPropertyCacheVector *self,
    int index) {
  self->setNeedsVMEMetaObject(index);
}

//  bool QQmlPropertyCacheVector::needsVMEMetaObject(int index) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QQmlPropertyCacheVector18needsVMEMetaObjectEi(
    const QQmlPropertyCacheVector *self,
    int index) {
  return self->needsVMEMetaObject(index);
}

//  void QQmlPropertyCacheVector::seal()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQmlPropertyCacheVector4sealEv(
    QQmlPropertyCacheVector *self) {
  self->seal();
}

//  void QQmlPropertyCacheVector::releaseElement(int i)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQmlPropertyCacheVector14releaseElementEi(
    QQmlPropertyCacheVector *self,
    int i) {
  self->releaseElement(i);
}
