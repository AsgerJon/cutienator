//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsgdefaultrectanglenode_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgdefaultrectanglenode_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#include <QtGui/qcolor.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/private/qsgdefaultrectanglenode_p.h>
#include <QtQuick/qsgflatcolormaterial.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quick/scenegraph/util/qsgdefaultrectanglenode.cpp, line 12, as _ZN23QSGDefaultRectangleNodeC1Ev
inline QSGDefaultRectangleNode::QSGDefaultRectangleNode()
    : m_geometry(QSGGeometry::defaultAttributes_ColoredPoint2D(), 4)
{
    QSGGeometry::updateColoredRectGeometry(&m_geometry, QRectF());
    setMaterial(&m_material);
    setGeometry(&m_geometry);
    setColor(QColor(255, 255, 255));
#ifdef QSG_RUNTIME_DESCRIPTION
    qsgnode_set_description(this, QLatin1String("rectangle"));
#endif
}

//  from ../qtdeclarative/src/quick/scenegraph/util/qsgdefaultrectanglenode.cpp, line 24, as _ZN23QSGDefaultRectangleNode7setRectERK6QRectF
inline void QSGDefaultRectangleNode::setRect(const QRectF &rect)
{
    QSGGeometry::updateColoredRectGeometry(&m_geometry, rect);
    markDirty(QSGNode::DirtyGeometry);
}

//  from ../qtdeclarative/src/quick/scenegraph/util/qsgdefaultrectanglenode.cpp, line 30, as _ZNK23QSGDefaultRectangleNode4rectEv
inline QRectF QSGDefaultRectangleNode::rect() const
{
    const QSGGeometry::ColoredPoint2D *pts = m_geometry.vertexDataAsColoredPoint2D();
    return QRectF(pts[0].x,
                  pts[0].y,
                  pts[3].x - pts[0].x,
                  pts[3].y - pts[0].y);
}

//  from ../qtdeclarative/src/quick/scenegraph/util/qsgdefaultrectanglenode.cpp, line 39, as _ZN23QSGDefaultRectangleNode8setColorERK6QColor
inline void QSGDefaultRectangleNode::setColor(const QColor &color)
{
    if (color != m_color) {
        float r, g, b, a;
        color.getRgbF(&r, &g, &b, &a);
        QSGGeometry::ColoredPoint2D *pts = m_geometry.vertexDataAsColoredPoint2D();
        for (int i = 0; i < 4; ++i) {
            pts[i].r = uchar(qRound(r * a * 255));
            pts[i].g = uchar(qRound(g * a * 255));
            pts[i].b = uchar(qRound(b * a * 255));
            pts[i].a = uchar(qRound(a * 255));
        }
        markDirty(QSGNode::DirtyGeometry);
        m_color = color;
    }
}

//  from ../qtdeclarative/src/quick/scenegraph/util/qsgdefaultrectanglenode.cpp, line 56, as _ZNK23QSGDefaultRectangleNode5colorEv
inline QColor QSGDefaultRectangleNode::color() const
{
    return m_color;
}
//  -----------------------------------------------------------------------

//  QSGDefaultRectangleNode::QSGDefaultRectangleNode()
extern "C" Q_DECL_EXPORT
QSGDefaultRectangleNode *ritual_ZN23QSGDefaultRectangleNodeC1Ev() {
  return new QSGDefaultRectangleNode();
}

//  void QSGDefaultRectangleNode::setRect(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QSGDefaultRectangleNode7setRectERK6QRectF(
    QSGDefaultRectangleNode *self,
    const QRectF *rect) {
  self->setRect(*rect);
}

//  QRectF QSGDefaultRectangleNode::rect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK23QSGDefaultRectangleNode4rectEv(
    const QSGDefaultRectangleNode *self) {
  return new QRectF(self->rect());
}

//  void QSGDefaultRectangleNode::setColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QSGDefaultRectangleNode8setColorERK6QColor(
    QSGDefaultRectangleNode *self,
    const QColor *color) {
  self->setColor(*color);
}

//  QColor QSGDefaultRectangleNode::color() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK23QSGDefaultRectangleNode5colorEv(
    const QSGDefaultRectangleNode *self) {
  return new QColor(self->color());
}

//  void QSGDefaultRectangleNode::setRect(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QSGDefaultRectangleNode7setRectERK6QRectF(
    QSGDefaultRectangleNode *self,
    const QRectF *rect) {
  self->QSGDefaultRectangleNode::setRect(*rect);
}

//  QRectF QSGDefaultRectangleNode::rect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_own_ZNK23QSGDefaultRectangleNode4rectEv(
    const QSGDefaultRectangleNode *self) {
  return new QRectF(self->QSGDefaultRectangleNode::rect());
}

//  void QSGDefaultRectangleNode::setColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QSGDefaultRectangleNode8setColorERK6QColor(
    QSGDefaultRectangleNode *self,
    const QColor *color) {
  self->QSGDefaultRectangleNode::setColor(*color);
}

//  QColor QSGDefaultRectangleNode::color() const
extern "C" Q_DECL_EXPORT
QColor *ritual_own_ZNK23QSGDefaultRectangleNode5colorEv(
    const QSGDefaultRectangleNode *self) {
  return new QColor(self->QSGDefaultRectangleNode::color());
}
