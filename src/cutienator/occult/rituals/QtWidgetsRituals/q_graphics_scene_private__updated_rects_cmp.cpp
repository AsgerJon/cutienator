//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qgraphicsscene_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(graphicsview)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qgraphicsscene_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>

//  bool QGraphicsScenePrivate::UpdatedRectsCmp::operator()(const QRectF &a,
//      const QRectF &b) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QGraphicsScenePrivate15UpdatedRectsCmpclERK6QRectFS3_(
    const QGraphicsScenePrivate::UpdatedRectsCmp *self,
    const QRectF *a,
    const QRectF *b) {
  return self->operator()(*a, *b);
}

//  QGraphicsScenePrivate::UpdatedRectsCmp::~UpdatedRectsCmp()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QGraphicsScenePrivate15UpdatedRectsCmpD1Ev(
    QGraphicsScenePrivate::UpdatedRectsCmp *self) {
  delete self;
}

#endif  // QT_CONFIG(graphicsview)
