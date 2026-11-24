//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsgadaptationlayer_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgadaptationlayer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  bool QSGDistanceFieldGlyphCache::Texture::operator==(const Texture
//      &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK26QSGDistanceFieldGlyphCache7TextureeqERKS0_(
    const QSGDistanceFieldGlyphCache::Texture *self,
    const QSGDistanceFieldGlyphCache::Texture *other) {
  return self->operator==(*other);
}

//  QSGDistanceFieldGlyphCache::Texture::~Texture()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QSGDistanceFieldGlyphCache7TextureD1Ev(
    QSGDistanceFieldGlyphCache::Texture *self) {
  delete self;
}
