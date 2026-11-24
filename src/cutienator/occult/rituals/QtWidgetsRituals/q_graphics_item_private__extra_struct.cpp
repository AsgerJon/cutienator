//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qgraphicsitem_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qgraphicsitem_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qvariant.h>

//  QGraphicsItemPrivate::ExtraStruct::ExtraStruct()
extern "C" Q_DECL_EXPORT
QGraphicsItemPrivate::ExtraStruct *ritual_ZN20QGraphicsItemPrivate11ExtraStructC1Ev() {
  return new QGraphicsItemPrivate::ExtraStruct();
}

//  QGraphicsItemPrivate::ExtraStruct::ExtraStruct(Extra type, const QVariant
//      &value)
extern "C" Q_DECL_EXPORT
QGraphicsItemPrivate::ExtraStruct *ritual_ZN20QGraphicsItemPrivate11ExtraStructC1ENS_5ExtraERK8QVariant(
    QGraphicsItemPrivate::Extra type,
    const QVariant *value) {
  return new QGraphicsItemPrivate::ExtraStruct(type, *value);
}

//  bool QGraphicsItemPrivate::ExtraStruct::operator<(Extra extra) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QGraphicsItemPrivate11ExtraStructltENS_5ExtraE(
    const QGraphicsItemPrivate::ExtraStruct *self,
    QGraphicsItemPrivate::Extra extra) {
  return self->operator<(extra);
}

//  QGraphicsItemPrivate::ExtraStruct::~ExtraStruct()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QGraphicsItemPrivate11ExtraStructD1Ev(
    QGraphicsItemPrivate::ExtraStruct *self) {
  delete self;
}

#endif  // QT_CONFIG(graphicsview)
#endif  // QT_CONFIG(graphicsview)
