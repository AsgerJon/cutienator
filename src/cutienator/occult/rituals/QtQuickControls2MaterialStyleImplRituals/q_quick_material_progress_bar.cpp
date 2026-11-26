//  Written by dev_tooling.RitualGenerator from the records of QtQuickControl
//  s2MaterialStyleImpl/6.12.0/QtQuickControls2MaterialStyleImpl/private/qqui
//  ckmaterialprogressbar_p.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtQuickControls2MaterialStyleImpl/QtQuickControls2MaterialStyleImpl>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickControls2MaterialStyleImpl/6.12.0/QtQuickControls2MaterialStyleImpl/private/qquickmaterialprogressbar_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qcolor.h>
#include <QtQuick/QtQuick>
#include <QtQuick/qquickitem.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickControls2MaterialStyleImpl/private/qquickmaterialprogressbar_p.h>
#include <QtCore/qmath.h>
#include <QtCore/qeasingcurve.h>
#include <QtQuick/private/qquickitem_p.h>
#include <QtQuick/private/qsgadaptationlayer_p.h>
#include <QtQuick/qsgrectanglenode.h>
#include <QtQuick/qsgimagenode.h>
#include <QtQuick/qquickwindow.h>
#include <QtQuickControls2Impl/private/qquickanimatednode_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quickcontrols/material/impl/qquickmaterialprogressbar.cpp, line 18, as local:qquickmaterialprogressbar.cpp:PauseDuration
static const int PauseDuration = 520;

//  from ../qtdeclarative/src/quickcontrols/material/impl/qquickmaterialprogressbar.cpp, line 19, as local:qquickmaterialprogressbar.cpp:SlideDuration
static const int SlideDuration = 1240;

//  from ../qtdeclarative/src/quickcontrols/material/impl/qquickmaterialprogressbar.cpp, line 20, as local:qquickmaterialprogressbar.cpp:QmpbTotalDuration
static const int QmpbTotalDuration = SlideDuration + PauseDuration;

//  from ../qtdeclarative/src/quickcontrols/material/impl/qquickmaterialprogressbar.cpp, line 22, as local:qquickmaterialprogressbar.cpp:QQuickMaterialProgressBarNode
class QQuickMaterialProgressBarNode : public QQuickAnimatedNode
{
public:
    QQuickMaterialProgressBarNode(QQuickMaterialProgressBar *item);

    void updateCurrentTime(int time) override;
    void sync(QQuickItem *item) override;

private:
    void moveNode(QSGTransformNode *node, const QRectF &geometry, qreal progress);

    bool m_indeterminate = false;
    QEasingCurve m_easing = QEasingCurve::OutCubic;
};

//  from ../qtdeclarative/src/quickcontrols/material/impl/qquickmaterialprogressbar.cpp, line 37, as local:qquickmaterialprogressbar.cpp:QQuickMaterialProgressBarNode::QQuickMaterialProgressBarNode
inline QQuickMaterialProgressBarNode::QQuickMaterialProgressBarNode(QQuickMaterialProgressBar *item)
    : QQuickAnimatedNode(item)
{
    setLoopCount(Infinite);
    setDuration(QmpbTotalDuration);
}

//  from ../qtdeclarative/src/quickcontrols/material/impl/qquickmaterialprogressbar.cpp, line 44, as local:qquickmaterialprogressbar.cpp:QQuickMaterialProgressBarNode::updateCurrentTime
inline void QQuickMaterialProgressBarNode::updateCurrentTime(int time)
{
    QSGRectangleNode *geometryNode = static_cast<QSGRectangleNode *>(firstChild());
    Q_ASSERT(geometryNode->type() == QSGNode::GeometryNodeType);
    const QRectF geometry = geometryNode->rect();

    QSGTransformNode *firstNode = static_cast<QSGTransformNode *>(geometryNode->firstChild());
    if (firstNode) {
        Q_ASSERT(firstNode->type() == QSGNode::TransformNodeType);

        const qreal progress = qMin<qreal>(1.0, static_cast<qreal>(time) / SlideDuration);
        moveNode(static_cast<QSGTransformNode *>(firstNode), geometry, progress);
    }

    QSGTransformNode *secondNode = static_cast<QSGTransformNode *>(geometryNode->lastChild());
    if (secondNode) {
        Q_ASSERT(secondNode->type() == QSGNode::TransformNodeType);

        const qreal progress = qMax<qreal>(0.0, static_cast<qreal>(time - PauseDuration) / SlideDuration);
        moveNode(static_cast<QSGTransformNode *>(secondNode), geometry, progress);
    }
}

//  from ../qtdeclarative/src/quickcontrols/material/impl/qquickmaterialprogressbar.cpp, line 67, as local:qquickmaterialprogressbar.cpp:QQuickMaterialProgressBarNode::sync
inline void QQuickMaterialProgressBarNode::sync(QQuickItem *item)
{
    QQuickMaterialProgressBar *bar = static_cast<QQuickMaterialProgressBar *>(item);
    if (m_indeterminate != bar->isIndeterminate()) {
        m_indeterminate = bar->isIndeterminate();
        if (m_indeterminate)
            start();
        else
            stop();
    }

    QQuickItemPrivate *d = QQuickItemPrivate::get(item);

    QRectF bounds = item->boundingRect();
    bounds.setHeight(item->implicitHeight());
    bounds.moveTop((item->height() - bounds.height()) / 2.0);

    QSGRectangleNode *geometryNode = static_cast<QSGRectangleNode *>(firstChild());
    if (!geometryNode) {
        geometryNode = item->window()->createRectangleNode();
        geometryNode->setColor(Qt::transparent);
        appendChildNode(geometryNode);
    }
    geometryNode->setRect(bounds);

    const int count = m_indeterminate ? 2 : 1;
    const qreal w = m_indeterminate ? 0 : bar->progress() * item->width();
    const QRectF rect(0, bounds.y(), w, bounds.height());

    QSGNode *transformNode = geometryNode->firstChild();
    for (int i = 0; i < count; ++i) {
        if (!transformNode) {
            transformNode = new QSGTransformNode;
            geometryNode->appendChildNode(transformNode);

            QSGInternalRectangleNode *rectNode = d->sceneGraphContext()->createInternalRectangleNode();
            rectNode->setAntialiasing(true);
            transformNode->appendChildNode(rectNode);
        }
        Q_ASSERT(transformNode->type() == QSGNode::TransformNodeType);
        static_cast<QSGTransformNode *>(transformNode)->setMatrix(QMatrix4x4());

        QSGInternalRectangleNode *rectNode = static_cast<QSGInternalRectangleNode *>(transformNode->firstChild());
        Q_ASSERT(rectNode->type() == QSGNode::GeometryNodeType);

        rectNode->setRect(rect);
        rectNode->setColor(bar->color());
        rectNode->update();

        transformNode = transformNode->nextSibling();
    }

    while (transformNode) {
        QSGNode *nextSibling = transformNode->nextSibling();
        delete transformNode;
        transformNode = nextSibling;
    }
}

//  from ../qtdeclarative/src/quickcontrols/material/impl/qquickmaterialprogressbar.cpp, line 126, as local:qquickmaterialprogressbar.cpp:QQuickMaterialProgressBarNode::moveNode
inline void QQuickMaterialProgressBarNode::moveNode(QSGTransformNode *transformNode, const QRectF &geometry, qreal progress)
{
    const qreal value = m_easing.valueForProgress(progress);
    const qreal x = value * geometry.width();

    QMatrix4x4 matrix;
    matrix.translate(x, 0);
    transformNode->setMatrix(matrix);

    QSGInternalRectangleNode *rectNode = static_cast<QSGInternalRectangleNode *>(transformNode->firstChild());
    Q_ASSERT(rectNode->type() == QSGNode::GeometryNodeType);

    QRectF r = geometry;
    r.setWidth(value * (geometry.width() - x));
    rectNode->setRect(r);
    rectNode->update();
}

//  from ../qtdeclarative/src/quickcontrols/material/impl/qquickmaterialprogressbar.cpp, line 192, as _ZN25QQuickMaterialProgressBar10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE
inline void QQuickMaterialProgressBar::itemChange(QQuickItem::ItemChange change, const QQuickItem::ItemChangeData &data)
{
    QQuickItem::itemChange(change, data);
    if (change == ItemVisibleHasChanged)
        update();
}

//  from ../qtdeclarative/src/quickcontrols/material/impl/qquickmaterialprogressbar.cpp, line 150, as _ZNK25QQuickMaterialProgressBar5colorEv
inline QColor QQuickMaterialProgressBar::color() const
{
    return m_color;
}

//  from ../qtdeclarative/src/quickcontrols/material/impl/qquickmaterialprogressbar.cpp, line 155, as _ZN25QQuickMaterialProgressBar8setColorERK6QColor
inline void QQuickMaterialProgressBar::setColor(const QColor &color)
{
    if (color == m_color)
        return;

    m_color = color;
    update();
}

//  from ../qtdeclarative/src/quickcontrols/material/impl/qquickmaterialprogressbar.cpp, line 164, as _ZNK25QQuickMaterialProgressBar8progressEv
inline qreal QQuickMaterialProgressBar::progress() const
{
    return m_progress;
}

//  from ../qtdeclarative/src/quickcontrols/material/impl/qquickmaterialprogressbar.cpp, line 169, as _ZN25QQuickMaterialProgressBar11setProgressEd
inline void QQuickMaterialProgressBar::setProgress(qreal progress)
{
    if (progress == m_progress)
        return;

    m_progress = progress;
    update();
}

//  from ../qtdeclarative/src/quickcontrols/material/impl/qquickmaterialprogressbar.cpp, line 178, as _ZNK25QQuickMaterialProgressBar15isIndeterminateEv
inline bool QQuickMaterialProgressBar::isIndeterminate() const
{
    return m_indeterminate;
}

//  from ../qtdeclarative/src/quickcontrols/material/impl/qquickmaterialprogressbar.cpp, line 183, as _ZN25QQuickMaterialProgressBar16setIndeterminateEb
inline void QQuickMaterialProgressBar::setIndeterminate(bool indeterminate)
{
    if (indeterminate == m_indeterminate)
        return;

    m_indeterminate = indeterminate;
    update();
}
//  -----------------------------------------------------------------------

//  Only a class built on QQuickMaterialProgressBar may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickMaterialProgressBar : QQuickMaterialProgressBar {
  using QQuickMaterialProgressBar::itemChange;
};

//  const QMetaObject *QQuickMaterialProgressBar::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK25QQuickMaterialProgressBar10metaObjectEv(
    const QQuickMaterialProgressBar *self) {
  return self->metaObject();
}

//  void *QQuickMaterialProgressBar::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN25QQuickMaterialProgressBar11qt_metacastEPKc(
    QQuickMaterialProgressBar *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickMaterialProgressBar::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN25QQuickMaterialProgressBar11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickMaterialProgressBar *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QColor QQuickMaterialProgressBar::color() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK25QQuickMaterialProgressBar5colorEv(
    const QQuickMaterialProgressBar *self) {
  return new QColor(self->color());
}

//  void QQuickMaterialProgressBar::setColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickMaterialProgressBar8setColorERK6QColor(
    QQuickMaterialProgressBar *self,
    const QColor *color) {
  self->setColor(*color);
}

//  qreal QQuickMaterialProgressBar::progress() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK25QQuickMaterialProgressBar8progressEv(
    const QQuickMaterialProgressBar *self) {
  return self->progress();
}

//  void QQuickMaterialProgressBar::setProgress(qreal progress)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickMaterialProgressBar11setProgressEd(
    QQuickMaterialProgressBar *self,
    qreal progress) {
  self->setProgress(progress);
}

//  bool QQuickMaterialProgressBar::isIndeterminate() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK25QQuickMaterialProgressBar15isIndeterminateEv(
    const QQuickMaterialProgressBar *self) {
  return self->isIndeterminate();
}

//  void QQuickMaterialProgressBar::setIndeterminate(bool indeterminate)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickMaterialProgressBar16setIndeterminateEb(
    QQuickMaterialProgressBar *self,
    bool indeterminate) {
  self->setIndeterminate(indeterminate);
}

//  void QQuickMaterialProgressBar::itemChange(ItemChange change, const
//      ItemChangeData &data)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickMaterialProgressBar10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE(
    QQuickMaterialProgressBar *self,
    QQuickItem::ItemChange change,
    const QQuickItem::ItemChangeData *data) {
  self->itemChange(change, *data);
}

//  QSGNode *QQuickMaterialProgressBar::updatePaintNode(QSGNode *oldNode,
//      UpdatePaintNodeData *a1)
extern "C" Q_DECL_EXPORT
QSGNode *ritual_ZN25QQuickMaterialProgressBar15updatePaintNodeEP7QSGNodePN10QQuickItem19UpdatePaintNodeDataE(
    QQuickMaterialProgressBar *self,
    QSGNode *oldNode,
    QQuickItem::UpdatePaintNodeData *a1) {
  return self->updatePaintNode(oldNode, a1);
}

//  void QQuickMaterialProgressBar::itemChange(ItemChange change, const
//      ItemChangeData &data)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN25QQuickMaterialProgressBar10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE(
    QQuickMaterialProgressBar *self,
    QQuickItem::ItemChange change,
    const QQuickItem::ItemChangeData *data) {
  static_cast<OwnQQuickMaterialProgressBar *>(self)->OwnQQuickMaterialProgressBar::itemChange(
      change,
      *data);
}
