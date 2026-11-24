//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsgbatchrenderer_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgbatchrenderer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/qsgnode.h>
#include <QtQuick/private/qsgnode_p.h>
#include <QtQuick/private/qsgrenderer_p.h>
#include <QtQuick/private/qsgnodeupdater_p.h>
#include <QtQuick/qsgmaterial.h>
#include <algorithm>
#include "limits.h"
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quick/scenegraph/coreapi/qsgnode.cpp, line 360, as _ZN14QSGNodePrivate15mutabilityGroupEPK7QSGNode
inline quint8 QSGNodePrivate::mutabilityGroup(const QSGNode *node)
{
    return !node->d_ptr.isNull()
               ? node->d_ptr->m_mutabilityGroup
               : 0;
}
//  -----------------------------------------------------------------------

//  QSGBatchRenderer::Element::Element()
extern "C" Q_DECL_EXPORT
QSGBatchRenderer::Element *ritual_ZN16QSGBatchRenderer7ElementC1Ev() {
  return new QSGBatchRenderer::Element();
}

//  void QSGBatchRenderer::Element::setNode(QSGGeometryNode *n)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGBatchRenderer7Element7setNodeEP15QSGGeometryNode(
    QSGBatchRenderer::Element *self,
    QSGGeometryNode *n) {
  self->setNode(n);
}

//  QSGBatchRenderer::Element::~Element()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGBatchRenderer7ElementD1Ev(
    QSGBatchRenderer::Element *self) {
  delete self;
}
