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

//  QQmlPropertyCacheVector::QQmlPropertyCacheVector(QQmlPropertyCacheVector
//      &&a0)
extern "C" Q_DECL_EXPORT
QQmlPropertyCacheVector *ritual_ZN23QQmlPropertyCacheVectorC1EOS_(
    QQmlPropertyCacheVector *a0) {
  return new QQmlPropertyCacheVector(std::move(*a0));
}

//  QQmlPropertyCacheVector
//      &QQmlPropertyCacheVector::operator=(QQmlPropertyCacheVector &&a0)
extern "C" Q_DECL_EXPORT
QQmlPropertyCacheVector *ritual_ZN23QQmlPropertyCacheVectoraSEOS_(
    QQmlPropertyCacheVector *self,
    QQmlPropertyCacheVector *a0) {
  return &(self->operator=(std::move(*a0)));
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

//  void QQmlPropertyCacheVector::appendOwn(const QQmlPropertyCache::Ptr
//      &cache)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQmlPropertyCacheVector9appendOwnERK14QQmlRefPointerI17QQmlPropertyCacheE(
    QQmlPropertyCacheVector *self,
    const QQmlPropertyCache::Ptr *cache) {
  self->appendOwn(*cache);
}

//  QQmlPropertyCache::ConstPtr QQmlPropertyCacheVector::at(int index) const
extern "C" Q_DECL_EXPORT
QQmlPropertyCache::ConstPtr *ritual_ZNK23QQmlPropertyCacheVector2atEi(
    const QQmlPropertyCacheVector *self,
    int index) {
  return new QQmlPropertyCache::ConstPtr(self->at(index));
}

//  QQmlPropertyCache::Ptr QQmlPropertyCacheVector::ownAt(int index) const
extern "C" Q_DECL_EXPORT
QQmlPropertyCache::Ptr *ritual_ZNK23QQmlPropertyCacheVector5ownAtEi(
    const QQmlPropertyCacheVector *self,
    int index) {
  return new QQmlPropertyCache::Ptr(self->ownAt(index));
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

//  void QQmlPropertyCacheVector::setOwn(int index, const
//      QQmlPropertyCache::Ptr &replacement)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQmlPropertyCacheVector6setOwnEiRK14QQmlRefPointerI17QQmlPropertyCacheE(
    QQmlPropertyCacheVector *self,
    int index,
    const QQmlPropertyCache::Ptr *replacement) {
  self->setOwn(index, *replacement);
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

//  a QQmlPropertyCache::Ptr a ritual of QQmlPropertyCacheVector gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQmlPropertyCacheVector__QQmlPropertyCache_Ptr(
    QQmlPropertyCache::Ptr *self) {
  delete self;
}
