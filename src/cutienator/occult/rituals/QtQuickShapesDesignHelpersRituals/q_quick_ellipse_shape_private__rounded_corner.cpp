//  Written by dev_tooling.RitualGenerator from the records of QtQuickShapesD
//  esignHelpers/6.12.0/QtQuickShapesDesignHelpers/private/qquickellipseshape
//  _p_p.h, Qt 6.12.0. Changes made here are lost.
#include <QtQuickShapesDesignHelpers/6.12.0/QtQuickShapesDesignHelpers/private/qquickshapesdesignhelpersglobal_p.h>
#include <QtQuickShapesDesignHelpers/QtQuickShapesDesignHelpers>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickShapesDesignHelpers/6.12.0/QtQuickShapesDesignHelpers/private/qquickellipseshape_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qvectornd.h>

//  void QQuickEllipseShapePrivate::RoundedCorner::update(qreal diff,
//      QVector2D a, QVector2D b, QVector2D c, qreal alpha, qreal radius)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickEllipseShapePrivate13RoundedCorner6updateEd9QVector2DS1_S1_dd(
    QQuickEllipseShapePrivate::RoundedCorner *self,
    qreal diff,
    const QVector2D *a,
    const QVector2D *b,
    const QVector2D *c,
    qreal alpha,
    qreal radius) {
  self->update(diff, *a, *b, *c, alpha, radius);
}

//  void QQuickEllipseShapePrivate::RoundedCorner::reset()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickEllipseShapePrivate13RoundedCorner5resetEv(
    QQuickEllipseShapePrivate::RoundedCorner *self) {
  self->reset();
}

//  QQuickEllipseShapePrivate::RoundedCorner::~RoundedCorner()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickEllipseShapePrivate13RoundedCornerD1Ev(
    QQuickEllipseShapePrivate::RoundedCorner *self) {
  delete self;
}
