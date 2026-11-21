//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qpainter.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qpainter.h>
#include <QtCore/qpoint.h>
#include <QtCore/qrect.h>

//  PixmapFragment QPainter::PixmapFragment::create(const QPointF &pos, const
//      QRectF &sourceRect, qreal scaleX, qreal scaleY, qreal rotation, qreal
//      opacity)
extern "C" Q_DECL_EXPORT
QPainter::PixmapFragment *ritual_ZN8QPainter14PixmapFragment6createERK7QPointFRK6QRectFdddd(
    const QPointF *pos,
    const QRectF *sourceRect,
    qreal scaleX,
    qreal scaleY,
    qreal rotation,
    qreal opacity) {
  return new QPainter::PixmapFragment(
      QPainter::PixmapFragment::create(
          *pos,
          *sourceRect,
          scaleX,
          scaleY,
          rotation,
          opacity));
}

//  QPainter::PixmapFragment::~PixmapFragment()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter14PixmapFragmentD1Ev(QPainter::PixmapFragment *self) {
  delete self;
}
