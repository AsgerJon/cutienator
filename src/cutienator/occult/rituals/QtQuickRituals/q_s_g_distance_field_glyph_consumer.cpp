//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsgadaptationlayer_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgadaptationlayer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QSGDistanceFieldGlyphConsumer::~QSGDistanceFieldGlyphConsumer()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QSGDistanceFieldGlyphConsumerD1Ev(
    QSGDistanceFieldGlyphConsumer *self) {
  delete self;
}

//  void QSGDistanceFieldGlyphConsumer::invalidateGlyphs(const QList<quint32>
//      &glyphs)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QSGDistanceFieldGlyphConsumer16invalidateGlyphsERK5QListIjE(
    QSGDistanceFieldGlyphConsumer *self,
    const QList<quint32> *glyphs) {
  self->invalidateGlyphs(*glyphs);
}
