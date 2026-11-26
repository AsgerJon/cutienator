//  Written by dev_tooling.RitualGenerator from the records of QtQuickControl
//  s2UniversalStyleImpl/6.12.0/QtQuickControls2UniversalStyleImpl/private/qq
//  uickuniversalbusyindicator_p.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtQuickControls2UniversalStyleImpl/QtQuickControls2UniversalStyleImpl>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickControls2UniversalStyleImpl/6.12.0/QtQuickControls2UniversalStyleImpl/private/qquickuniversalbusyindicator_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qcolor.h>
#include <QtQuick/QtQuick>
#include <QtQuick/qquickitem.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickControls2UniversalStyleImpl/private/qquickuniversalbusyindicator_p.h>
#include <QtCore/qmath.h>
#include <QtCore/qeasingcurve.h>
#include <QtQuick/private/qquickitem_p.h>
#include <QtQuick/private/qsgadaptationlayer_p.h>
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

//  from ../qtdeclarative/src/quickcontrols/universal/impl/qquickuniversalbusyindicator.cpp, line 15, as local:qquickuniversalbusyindicator.cpp:PhaseCount
static const int PhaseCount = 6;

//  from ../qtdeclarative/src/quickcontrols/universal/impl/qquickuniversalbusyindicator.cpp, line 19, as local:qquickuniversalbusyindicator.cpp:QQuickUniversalBusyIndicatorNode
class QQuickUniversalBusyIndicatorNode : public QQuickAnimatedNode
{
public:
    QQuickUniversalBusyIndicatorNode(QQuickUniversalBusyIndicator *item);

    void updateCurrentTime(int time) override;
    void sync(QQuickItem *item) override;

private:
    struct Phase {
        Phase() = default;
        Phase(int d, qreal f, qreal t, QEasingCurve::Type c) : duration(d), from(f), to(t), curve(c) { }
        int duration = 0;
        qreal from = 0;
        qreal to = 0;
        QEasingCurve curve = QEasingCurve::Linear;
    };

    Phase m_phases[PhaseCount];
};

//  from ../qtdeclarative/src/quickcontrols/universal/impl/qquickuniversalbusyindicator.cpp, line 195, as _ZN28QQuickUniversalBusyIndicator10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE
inline void QQuickUniversalBusyIndicator::itemChange(QQuickItem::ItemChange change, const QQuickItem::ItemChangeData &data)
{
    QQuickItem::itemChange(change, data);
    if (change == ItemVisibleHasChanged)
        update();
}

//  from ../qtdeclarative/src/quickcontrols/universal/impl/qquickuniversalbusyindicator.cpp, line 162, as _ZNK28QQuickUniversalBusyIndicator5countEv
inline int QQuickUniversalBusyIndicator::count() const
{
    return m_count;
}

//  from ../qtdeclarative/src/quickcontrols/universal/impl/qquickuniversalbusyindicator.cpp, line 167, as _ZN28QQuickUniversalBusyIndicator8setCountEi
inline void QQuickUniversalBusyIndicator::setCount(int count)
{
    if (m_count == count)
        return;

    m_count = count;
    update();
}

//  from ../qtdeclarative/src/quickcontrols/universal/impl/qquickuniversalbusyindicator.cpp, line 176, as _ZNK28QQuickUniversalBusyIndicator5colorEv
inline QColor QQuickUniversalBusyIndicator::color() const
{
    return m_color;
}

//  from ../qtdeclarative/src/quickcontrols/universal/impl/qquickuniversalbusyindicator.cpp, line 181, as _ZN28QQuickUniversalBusyIndicator8setColorERK6QColor
inline void QQuickUniversalBusyIndicator::setColor(const QColor &color)
{
    if (m_color == color)
        return;

    m_color = color;
    update();
}

//  from ../qtdeclarative/src/quickcontrols/universal/impl/qquickuniversalbusyindicator.cpp, line 190, as _ZNK28QQuickUniversalBusyIndicator7elapsedEv
inline int QQuickUniversalBusyIndicator::elapsed() const
{
    return m_elapsed;
}
//  -----------------------------------------------------------------------

//  Only a class built on QQuickUniversalBusyIndicator may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickUniversalBusyIndicator : QQuickUniversalBusyIndicator {
  using QQuickUniversalBusyIndicator::itemChange;
};

//  const QMetaObject *QQuickUniversalBusyIndicator::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK28QQuickUniversalBusyIndicator10metaObjectEv(
    const QQuickUniversalBusyIndicator *self) {
  return self->metaObject();
}

//  void *QQuickUniversalBusyIndicator::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN28QQuickUniversalBusyIndicator11qt_metacastEPKc(
    QQuickUniversalBusyIndicator *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickUniversalBusyIndicator::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN28QQuickUniversalBusyIndicator11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickUniversalBusyIndicator *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  int QQuickUniversalBusyIndicator::count() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK28QQuickUniversalBusyIndicator5countEv(
    const QQuickUniversalBusyIndicator *self) {
  return self->count();
}

//  void QQuickUniversalBusyIndicator::setCount(int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickUniversalBusyIndicator8setCountEi(
    QQuickUniversalBusyIndicator *self,
    int count) {
  self->setCount(count);
}

//  QColor QQuickUniversalBusyIndicator::color() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK28QQuickUniversalBusyIndicator5colorEv(
    const QQuickUniversalBusyIndicator *self) {
  return new QColor(self->color());
}

//  void QQuickUniversalBusyIndicator::setColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickUniversalBusyIndicator8setColorERK6QColor(
    QQuickUniversalBusyIndicator *self,
    const QColor *color) {
  self->setColor(*color);
}

//  int QQuickUniversalBusyIndicator::elapsed() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK28QQuickUniversalBusyIndicator7elapsedEv(
    const QQuickUniversalBusyIndicator *self) {
  return self->elapsed();
}

//  void QQuickUniversalBusyIndicator::itemChange(ItemChange change, const
//      ItemChangeData &data)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickUniversalBusyIndicator10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE(
    QQuickUniversalBusyIndicator *self,
    QQuickItem::ItemChange change,
    const QQuickItem::ItemChangeData *data) {
  self->itemChange(change, *data);
}

//  QSGNode *QQuickUniversalBusyIndicator::updatePaintNode(QSGNode *oldNode,
//      UpdatePaintNodeData *a1)
extern "C" Q_DECL_EXPORT
QSGNode *ritual_ZN28QQuickUniversalBusyIndicator15updatePaintNodeEP7QSGNodePN10QQuickItem19UpdatePaintNodeDataE(
    QQuickUniversalBusyIndicator *self,
    QSGNode *oldNode,
    QQuickItem::UpdatePaintNodeData *a1) {
  return self->updatePaintNode(oldNode, a1);
}

//  void QQuickUniversalBusyIndicator::itemChange(ItemChange change, const
//      ItemChangeData &data)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN28QQuickUniversalBusyIndicator10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE(
    QQuickUniversalBusyIndicator *self,
    QQuickItem::ItemChange change,
    const QQuickItem::ItemChangeData *data) {
  static_cast<OwnQQuickUniversalBusyIndicator *>(self)->OwnQQuickUniversalBusyIndicator::itemChange(
      change,
      *data);
}
