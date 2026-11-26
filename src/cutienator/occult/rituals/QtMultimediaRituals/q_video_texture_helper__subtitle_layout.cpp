//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/6.12.0/QtMultimedia/private/qvideotexturehelper_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#include <QtMultimedia/QtMultimedia>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/6.12.0/QtMultimedia/private/qvideotexturehelper_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qsize.h>
#include <QtCore/qstring.h>
#include <QtCore/qpoint.h>
#include <QtGui/qimage.h>

//  bool QVideoTextureHelper::SubtitleLayout::update(const QSize &frameSize,
//      QString text)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QVideoTextureHelper14SubtitleLayout6updateERK5QSize7QString(
    QVideoTextureHelper::SubtitleLayout *self,
    const QSize *frameSize,
    const QString *text) {
  return self->update(*frameSize, *text);
}

//  void QVideoTextureHelper::SubtitleLayout::draw(QPainter *painter, const
//      QPointF &translate) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK19QVideoTextureHelper14SubtitleLayout4drawEP8QPainterRK7QPointF(
    const QVideoTextureHelper::SubtitleLayout *self,
    QPainter *painter,
    const QPointF *translate) {
  self->draw(painter, *translate);
}

//  QImage QVideoTextureHelper::SubtitleLayout::toImage() const
extern "C" Q_DECL_EXPORT
QImage *ritual_ZNK19QVideoTextureHelper14SubtitleLayout7toImageEv(
    const QVideoTextureHelper::SubtitleLayout *self) {
  return new QImage(self->toImage());
}
