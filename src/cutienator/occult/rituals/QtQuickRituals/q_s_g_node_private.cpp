//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsgnode_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgnode_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
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

//  from ../qtdeclarative/src/quick/scenegraph/coreapi/qsgnode.cpp, line 372, as _ZN14QSGNodePrivate27setMutabilityGroupOfSubtreeEP7QSGNodeh
inline void QSGNodePrivate::setMutabilityGroupOfSubtree(QSGNode *node, quint8 group)
{
    Q_ASSERT((group & 0xf) == group);

    const quint8 currentMutabilityGroup = mutabilityGroup(node);
    if (currentMutabilityGroup != group) {
        if (node->d_ptr.isNull())
            node->d_ptr.reset(new QSGNodePrivate());
        node->d_ptr->m_mutabilityGroup = group;
        node->markDirty(QSGNode::DirtyGeometry);
    }

    for (int i = 0; i < node->childCount(); ++i)
        QSGNodePrivate::setMutabilityGroupOfSubtree(node->childAtIndex(i), group);
}
//  -----------------------------------------------------------------------

//  QSGNodePrivate::QSGNodePrivate()
extern "C" Q_DECL_EXPORT
QSGNodePrivate *ritual_ZN14QSGNodePrivateC1Ev() {
  return new QSGNodePrivate();
}

//  QSGNodePrivate::~QSGNodePrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSGNodePrivateD1Ev(QSGNodePrivate *self) {
  delete self;
}

//  quint8 QSGNodePrivate::mutabilityGroup(const QSGNode *node)
extern "C" Q_DECL_EXPORT
quint8 ritual_ZN14QSGNodePrivate15mutabilityGroupEPK7QSGNode(
    const QSGNode *node) {
  return QSGNodePrivate::mutabilityGroup(node);
}

//  void QSGNodePrivate::setMutabilityGroupOfSubtree(QSGNode *node, quint8
//      mutabilityGroup)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSGNodePrivate27setMutabilityGroupOfSubtreeEP7QSGNodeh(
    QSGNode *node,
    quint8 mutabilityGroup) {
  QSGNodePrivate::setMutabilityGroupOfSubtree(node, mutabilityGroup);
}

#if defined(QSG_RUNTIME_DESCRIPTION)
//  void QSGNodePrivate::setDescription(QSGNode *node, const QString
//      &description)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSGNodePrivate14setDescriptionEP7QSGNodeRK7QString(
    QSGNode *node,
    const QString *description) {
  QSGNodePrivate::setDescription(node, *description);
}
#endif  // defined(QSG_RUNTIME_DESCRIPTION)

#if defined(QSG_RUNTIME_DESCRIPTION)
//  QString QSGNodePrivate::description(const QSGNode *node)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN14QSGNodePrivate11descriptionEPK7QSGNode(
    const QSGNode *node) {
  return new QString(QSGNodePrivate::description(node));
}
#endif  // defined(QSG_RUNTIME_DESCRIPTION)
