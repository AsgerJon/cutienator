//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qpixmapcache.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qpixmapcache.h>

//  QPixmapCache::Key::Key()
extern "C" Q_DECL_EXPORT
QPixmapCache::Key *ritual_ZN12QPixmapCache3KeyC1Ev() {
  return new QPixmapCache::Key();
}

//  QPixmapCache::Key::Key(const Key &other)
extern "C" Q_DECL_EXPORT
QPixmapCache::Key *ritual_ZN12QPixmapCache3KeyC1ERKS0_(
    const QPixmapCache::Key *other) {
  return new QPixmapCache::Key(*other);
}

//  QPixmapCache::Key::Key(Key &&other)
extern "C" Q_DECL_EXPORT
QPixmapCache::Key *ritual_ZN12QPixmapCache3KeyC1EOS0_(
    QPixmapCache::Key *other) {
  return new QPixmapCache::Key(std::move(*other));
}

//  Key &QPixmapCache::Key::operator=(Key &&other)
extern "C" Q_DECL_EXPORT
QPixmapCache::Key *ritual_ZN12QPixmapCache3KeyaSEOS0_(
    QPixmapCache::Key *self,
    QPixmapCache::Key *other) {
  return &(self->operator=(std::move(*other)));
}

//  QPixmapCache::Key::~Key()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QPixmapCache3KeyD1Ev(QPixmapCache::Key *self) {
  delete self;
}

//  bool QPixmapCache::Key::operator==(const Key &key) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QPixmapCache3KeyeqERKS0_(
    const QPixmapCache::Key *self,
    const QPixmapCache::Key *key) {
  return self->operator==(*key);
}

//  bool QPixmapCache::Key::operator!=(const Key &key) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QPixmapCache3KeyneERKS0_(
    const QPixmapCache::Key *self,
    const QPixmapCache::Key *key) {
  return self->operator!=(*key);
}

//  Key &QPixmapCache::Key::operator=(const Key &other)
extern "C" Q_DECL_EXPORT
QPixmapCache::Key *ritual_ZN12QPixmapCache3KeyaSERKS0_(
    QPixmapCache::Key *self,
    const QPixmapCache::Key *other) {
  return &(self->operator=(*other));
}

//  void QPixmapCache::Key::swap(Key &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QPixmapCache3Key4swapERS0_(
    QPixmapCache::Key *self,
    QPixmapCache::Key *other) {
  self->swap(*other);
}

//  bool QPixmapCache::Key::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QPixmapCache3Key7isValidEv(const QPixmapCache::Key *self) {
  return self->isValid();
}

//  size_t QPixmapCache::Key::hash(size_t seed) const
extern "C" Q_DECL_EXPORT
size_t ritual_ZNK12QPixmapCache3Key4hashEm(
    const QPixmapCache::Key *self,
    size_t seed) {
  return self->hash(seed);
}
