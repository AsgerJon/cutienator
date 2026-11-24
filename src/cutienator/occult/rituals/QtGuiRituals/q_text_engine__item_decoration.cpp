//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qtextengine_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qtextengine_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qpen.h>

//  QTextEngine::ItemDecoration::ItemDecoration()
extern "C" Q_DECL_EXPORT
QTextEngine::ItemDecoration *ritual_ZN11QTextEngine14ItemDecorationC1Ev() {
  return new QTextEngine::ItemDecoration();
}

//  QTextEngine::ItemDecoration::ItemDecoration(qreal x1, qreal x2, qreal y,
//      const QPen &pen)
extern "C" Q_DECL_EXPORT
QTextEngine::ItemDecoration *ritual_ZN11QTextEngine14ItemDecorationC1EdddRK4QPen(
    qreal x1,
    qreal x2,
    qreal y,
    const QPen *pen) {
  return new QTextEngine::ItemDecoration(x1, x2, y, *pen);
}

//  QTextEngine::ItemDecoration::~ItemDecoration()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTextEngine14ItemDecorationD1Ev(
    QTextEngine::ItemDecoration *self) {
  delete self;
}
