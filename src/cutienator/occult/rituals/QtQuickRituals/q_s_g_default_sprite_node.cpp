//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsgdefaultspritenode_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick/qtquickglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#if QT_CONFIG(quick_sprite)
#if QT_CONFIG(quick_sprite)
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgdefaultspritenode_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qsize.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/private/qsgdefaultspritenode_p.h>
#include <QtQuick/QSGMaterial>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quick/scenegraph/qsgdefaultspritenode.cpp, line 225, as _ZN20QSGDefaultSpriteNode7setSizeERK6QSizeF
inline void QSGDefaultSpriteNode::setSize(const QSizeF &size)
{
    if (m_size != size) {
        m_size = size;
        m_geometryDirty = true;
    }
}

//  from ../qtdeclarative/src/quick/scenegraph/qsgdefaultspritenode.cpp, line 239, as _ZN20QSGDefaultSpriteNode6updateEv
inline void QSGDefaultSpriteNode::update()
{
    if (m_geometryDirty) {
        updateGeometry();
        m_geometryDirty = false;
    }
}
//  -----------------------------------------------------------------------

//  void QSGDefaultSpriteNode::setSize(const QSizeF &size)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QSGDefaultSpriteNode7setSizeERK6QSizeF(
    QSGDefaultSpriteNode *self,
    const QSizeF *size) {
  self->setSize(*size);
}

//  void QSGDefaultSpriteNode::update()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QSGDefaultSpriteNode6updateEv(QSGDefaultSpriteNode *self) {
  self->update();
}

//  void QSGDefaultSpriteNode::setSize(const QSizeF &size)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QSGDefaultSpriteNode7setSizeERK6QSizeF(
    QSGDefaultSpriteNode *self,
    const QSizeF *size) {
  self->QSGDefaultSpriteNode::setSize(*size);
}

#endif  // QT_CONFIG(quick_sprite)
#endif  // QT_CONFIG(quick_sprite)
