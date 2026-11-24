//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsgrendernode_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgrendernode_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QSGRenderNodePrivate::QSGRenderNodePrivate()
extern "C" Q_DECL_EXPORT
QSGRenderNodePrivate *ritual_ZN20QSGRenderNodePrivateC1Ev() {
  return new QSGRenderNodePrivate();
}

//  QSGRenderNodePrivate *QSGRenderNodePrivate::get(QSGRenderNode *node)
extern "C" Q_DECL_EXPORT
QSGRenderNodePrivate *ritual_ZN20QSGRenderNodePrivate3getEP13QSGRenderNode(
    QSGRenderNode *node) {
  return QSGRenderNodePrivate::get(node);
}

//  QSGRenderNodePrivate::~QSGRenderNodePrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QSGRenderNodePrivateD1Ev(QSGRenderNodePrivate *self) {
  delete self;
}
