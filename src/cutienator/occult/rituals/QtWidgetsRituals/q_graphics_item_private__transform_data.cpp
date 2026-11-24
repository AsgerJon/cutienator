//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qgraphicsitem_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(graphicsview)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qgraphicsitem_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qtransform.h>

//  QGraphicsItemPrivate::TransformData::TransformData()
extern "C" Q_DECL_EXPORT
QGraphicsItemPrivate::TransformData *ritual_ZN20QGraphicsItemPrivate13TransformDataC1Ev() {
  return new QGraphicsItemPrivate::TransformData();
}

//  QTransform
//      QGraphicsItemPrivate::TransformData::computedFullTransform(QTransform
//      *postmultiplyTransform) const
extern "C" Q_DECL_EXPORT
QTransform *ritual_ZNK20QGraphicsItemPrivate13TransformData21computedFullTransformEP10QTransform(
    const QGraphicsItemPrivate::TransformData *self,
    QTransform *postmultiplyTransform) {
  return new QTransform(self->computedFullTransform(postmultiplyTransform));
}

//  QGraphicsItemPrivate::TransformData::~TransformData()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QGraphicsItemPrivate13TransformDataD1Ev(
    QGraphicsItemPrivate::TransformData *self) {
  delete self;
}

#endif  // QT_CONFIG(graphicsview)
