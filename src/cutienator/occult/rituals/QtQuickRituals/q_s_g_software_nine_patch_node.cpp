//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsgsoftwarepublicnodes_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-26: added are 2 rituals that lean on what moc
//  writes for a class of the part Qt keeps to itself, whose ritual file
//  carries moc's output, drafted by a copy of the generator that lets those
//  names through. A copy of a meta-object is a second one: 'qobject_cast'
//  between it and Qt's own does not match. Kept as it is when the generator
//  runs again.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgsoftwarepublicnodes_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/private/qsgsoftwarepublicnodes_p.h>
#include <QtQuick/private/qsgsoftwarelayer_p.h>
#include <QtQuick/private/qsgsoftwarepixmaptexture_p.h>
#include <QtQuick/private/qsgsoftwareinternalimagenode_p.h>
#include <QtQuick/private/qsgplaintexture_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarepublicnodes.cpp, line 123, as _ZN24QSGSoftwareNinePatchNode10setTextureEP10QSGTexture
inline void QSGSoftwareNinePatchNode::setTexture(QSGTexture *texture)
{
    QSGSoftwarePixmapTexture *pt = qobject_cast<QSGSoftwarePixmapTexture*>(texture);
    if (!pt) {
        qWarning() << "Image used with invalid texture format.";
    } else {
        m_pixmap = pt->pixmap();
        markDirty(DirtyMaterial);
    }
    delete texture;
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarepublicnodes.cpp, line 135, as _ZN24QSGSoftwareNinePatchNode9setBoundsERK6QRectF
inline void QSGSoftwareNinePatchNode::setBounds(const QRectF &bounds)
{
    if (m_bounds == bounds)
        return;

    m_bounds = bounds;
    markDirty(DirtyGeometry);
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarepublicnodes.cpp, line 144, as _ZN24QSGSoftwareNinePatchNode19setDevicePixelRatioEd
inline void QSGSoftwareNinePatchNode::setDevicePixelRatio(qreal ratio)
{
    if (m_pixelRatio == ratio)
        return;

    m_pixelRatio = ratio;
    markDirty(DirtyGeometry);
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarepublicnodes.cpp, line 153, as _ZN24QSGSoftwareNinePatchNode10setPaddingEdddd
inline void QSGSoftwareNinePatchNode::setPadding(qreal left, qreal top, qreal right, qreal bottom)
{
    QMargins margins(qRound(left), qRound(top), qRound(right), qRound(bottom));
    if (m_margins == margins)
        return;

    m_margins = QMargins(qRound(left), qRound(top), qRound(right), qRound(bottom));
    markDirty(DirtyGeometry);
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarepublicnodes.cpp, line 163, as _ZN24QSGSoftwareNinePatchNode6updateEv
inline void QSGSoftwareNinePatchNode::update()
{
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarepublicnodes.cpp, line 117, as _ZN24QSGSoftwareNinePatchNodeC1Ev
inline QSGSoftwareNinePatchNode::QSGSoftwareNinePatchNode()
{
    setMaterial((QSGMaterial*)1);
    setGeometry((QSGGeometry*)1);
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarepublicnodes.cpp, line 179, as _ZNK24QSGSoftwareNinePatchNode6boundsEv
inline QRectF QSGSoftwareNinePatchNode::bounds() const
{
    return m_bounds;
}
//  -----------------------------------------------------------------------

//  QSGSoftwareNinePatchNode::QSGSoftwareNinePatchNode()
extern "C" Q_DECL_EXPORT
QSGSoftwareNinePatchNode *ritual_ZN24QSGSoftwareNinePatchNodeC1Ev() {
  return new QSGSoftwareNinePatchNode();
}

//  void QSGSoftwareNinePatchNode::setTexture(QSGTexture *texture)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QSGSoftwareNinePatchNode10setTextureEP10QSGTexture(
    QSGSoftwareNinePatchNode *self,
    QSGTexture *texture) {
  self->setTexture(texture);
}

//  void QSGSoftwareNinePatchNode::setBounds(const QRectF &bounds)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QSGSoftwareNinePatchNode9setBoundsERK6QRectF(
    QSGSoftwareNinePatchNode *self,
    const QRectF *bounds) {
  self->setBounds(*bounds);
}

//  void QSGSoftwareNinePatchNode::setDevicePixelRatio(qreal ratio)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QSGSoftwareNinePatchNode19setDevicePixelRatioEd(
    QSGSoftwareNinePatchNode *self,
    qreal ratio) {
  self->setDevicePixelRatio(ratio);
}

//  void QSGSoftwareNinePatchNode::setPadding(qreal left, qreal top, qreal
//      right, qreal bottom)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QSGSoftwareNinePatchNode10setPaddingEdddd(
    QSGSoftwareNinePatchNode *self,
    qreal left,
    qreal top,
    qreal right,
    qreal bottom) {
  self->setPadding(left, top, right, bottom);
}

//  void QSGSoftwareNinePatchNode::update()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QSGSoftwareNinePatchNode6updateEv(
    QSGSoftwareNinePatchNode *self) {
  self->update();
}

//  QRectF QSGSoftwareNinePatchNode::bounds() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK24QSGSoftwareNinePatchNode6boundsEv(
    const QSGSoftwareNinePatchNode *self) {
  return new QRectF(self->bounds());
}

//  bool QSGSoftwareNinePatchNode::isOpaque() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QSGSoftwareNinePatchNode8isOpaqueEv(
    const QSGSoftwareNinePatchNode *self) {
  return self->isOpaque();
}

//  void QSGSoftwareNinePatchNode::setTexture(QSGTexture *texture)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QSGSoftwareNinePatchNode10setTextureEP10QSGTexture(
    QSGSoftwareNinePatchNode *self,
    QSGTexture *texture) {
  self->QSGSoftwareNinePatchNode::setTexture(texture);
}

//  void QSGSoftwareNinePatchNode::setBounds(const QRectF &bounds)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QSGSoftwareNinePatchNode9setBoundsERK6QRectF(
    QSGSoftwareNinePatchNode *self,
    const QRectF *bounds) {
  self->QSGSoftwareNinePatchNode::setBounds(*bounds);
}

//  void QSGSoftwareNinePatchNode::setDevicePixelRatio(qreal ratio)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QSGSoftwareNinePatchNode19setDevicePixelRatioEd(
    QSGSoftwareNinePatchNode *self,
    qreal ratio) {
  self->QSGSoftwareNinePatchNode::setDevicePixelRatio(ratio);
}

//  void QSGSoftwareNinePatchNode::setPadding(qreal left, qreal top, qreal
//      right, qreal bottom)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QSGSoftwareNinePatchNode10setPaddingEdddd(
    QSGSoftwareNinePatchNode *self,
    qreal left,
    qreal top,
    qreal right,
    qreal bottom) {
  self->QSGSoftwareNinePatchNode::setPadding(left, top, right, bottom);
}

//  void QSGSoftwareNinePatchNode::update()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QSGSoftwareNinePatchNode6updateEv(
    QSGSoftwareNinePatchNode *self) {
  self->QSGSoftwareNinePatchNode::update();
}
