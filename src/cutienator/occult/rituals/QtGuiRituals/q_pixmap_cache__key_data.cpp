//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qpixmapcache_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qpixmapcache_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QPixmapCache::KeyData::KeyData()
extern "C" Q_DECL_EXPORT
QPixmapCache::KeyData *ritual_ZN12QPixmapCache7KeyDataC1Ev() {
  return new QPixmapCache::KeyData();
}

//  QPixmapCache::KeyData::KeyData(const KeyData &other)
extern "C" Q_DECL_EXPORT
QPixmapCache::KeyData *ritual_ZN12QPixmapCache7KeyDataC1ERKS0_(
    const QPixmapCache::KeyData *other) {
  return new QPixmapCache::KeyData(*other);
}

//  QPixmapCache::KeyData::~KeyData()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QPixmapCache7KeyDataD1Ev(QPixmapCache::KeyData *self) {
  delete self;
}
