//  Written by dev_tooling.RitualGenerator from the records of QtQuickControl
//  s2BasicStyleImpl/6.12.0/QtQuickControls2BasicStyleImpl/private/qquickbasi
//  cprogressbar_p.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtQuickControls2BasicStyleImpl/QtQuickControls2BasicStyleImpl>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickControls2BasicStyleImpl/6.12.0/QtQuickControls2BasicStyleImpl/private/qquickbasicprogressbar_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qcolor.h>
#include <QtQuick/QtQuick>
#include <QtQuick/qquickitem.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickControls2BasicStyleImpl/private/qquickbasicprogressbar_p.h>
#include <QtCore/qeasingcurve.h>
#include <QtQuick/private/qquickitem_p.h>
#include <QtQuick/private/qsgadaptationlayer_p.h>
#include <QtQuickControls2Impl/private/qquickanimatednode_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quickcontrols/basic/impl/qquickbasicprogressbar.cpp, line 14, as local:qquickbasicprogressbar.cpp:Blocks
static const int Blocks = 4;

//  from ../qtdeclarative/src/quickcontrols/basic/impl/qquickbasicprogressbar.cpp, line 15, as local:qquickbasicprogressbar.cpp:BlockWidth
static const int BlockWidth = 16;

//  from ../qtdeclarative/src/quickcontrols/basic/impl/qquickbasicprogressbar.cpp, line 16, as local:qquickbasicprogressbar.cpp:BlockRestingSpacing
static const int BlockRestingSpacing = 4;

//  from ../qtdeclarative/src/quickcontrols/basic/impl/qquickbasicprogressbar.cpp, line 18, as local:qquickbasicprogressbar.cpp:BlockSpan
static const int BlockSpan = Blocks * (BlockWidth + BlockRestingSpacing) - BlockRestingSpacing;

//  from ../qtdeclarative/src/quickcontrols/basic/impl/qquickbasicprogressbar.cpp, line 19, as local:qquickbasicprogressbar.cpp:QbpbTotalDuration
static const int QbpbTotalDuration = 4000;

//  from ../qtdeclarative/src/quickcontrols/basic/impl/qquickbasicprogressbar.cpp, line 20, as local:qquickbasicprogressbar.cpp:SecondPhaseStart
static const int SecondPhaseStart = QbpbTotalDuration * 0.4;

//  from ../qtdeclarative/src/quickcontrols/basic/impl/qquickbasicprogressbar.cpp, line 39, as local:qquickbasicprogressbar.cpp:QQuickBasicProgressBarNode
class QQuickBasicProgressBarNode : public QQuickAnimatedNode
{
public:
    QQuickBasicProgressBarNode(QQuickBasicProgressBar *item);

    void updateCurrentTime(int time) override;
    void sync(QQuickItem *item) override;

private:
    bool m_indeterminate = false;
    qreal m_pixelsPerSecond = 0;
};

//  from ../qtdeclarative/src/quickcontrols/basic/impl/qquickbasicprogressbar.cpp, line 52, as local:qquickbasicprogressbar.cpp:QQuickBasicProgressBarNode::QQuickBasicProgressBarNode
inline QQuickBasicProgressBarNode::QQuickBasicProgressBarNode(QQuickBasicProgressBar *item)
    : QQuickAnimatedNode(item),
      m_pixelsPerSecond(item->width())
{
    setLoopCount(Infinite);
    setDuration(QbpbTotalDuration);
}

//  from ../qtdeclarative/src/quickcontrols/basic/impl/qquickbasicprogressbar.cpp, line 231, as _ZN22QQuickBasicProgressBar10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE
inline void QQuickBasicProgressBar::itemChange(QQuickItem::ItemChange change, const QQuickItem::ItemChangeData &data)
{
    QQuickItem::itemChange(change, data);
    if (change == ItemVisibleHasChanged)
        update();
}

//  from ../qtdeclarative/src/quickcontrols/basic/impl/qquickbasicprogressbar.cpp, line 202, as _ZNK22QQuickBasicProgressBar15isIndeterminateEv
inline bool QQuickBasicProgressBar::isIndeterminate() const
{
    return m_indeterminate;
}

//  from ../qtdeclarative/src/quickcontrols/basic/impl/qquickbasicprogressbar.cpp, line 207, as _ZN22QQuickBasicProgressBar16setIndeterminateEb
inline void QQuickBasicProgressBar::setIndeterminate(bool indeterminate)
{
    if (indeterminate == m_indeterminate)
        return;

    m_indeterminate = indeterminate;
    setClip(m_indeterminate);
    update();
}

//  from ../qtdeclarative/src/quickcontrols/basic/impl/qquickbasicprogressbar.cpp, line 188, as _ZNK22QQuickBasicProgressBar8progressEv
inline qreal QQuickBasicProgressBar::progress() const
{
    return m_progress;
}

//  from ../qtdeclarative/src/quickcontrols/basic/impl/qquickbasicprogressbar.cpp, line 193, as _ZN22QQuickBasicProgressBar11setProgressEd
inline void QQuickBasicProgressBar::setProgress(qreal progress)
{
    if (progress == m_progress)
        return;

    m_progress = progress;
    update();
}

//  from ../qtdeclarative/src/quickcontrols/basic/impl/qquickbasicprogressbar.cpp, line 217, as _ZNK22QQuickBasicProgressBar5colorEv
inline QColor QQuickBasicProgressBar::color() const
{
    return m_color;
}

//  from ../qtdeclarative/src/quickcontrols/basic/impl/qquickbasicprogressbar.cpp, line 222, as _ZN22QQuickBasicProgressBar8setColorERK6QColor
inline void QQuickBasicProgressBar::setColor(const QColor &color)
{
    if (color == m_color)
        return;

    m_color = color;
    update();
}
//  -----------------------------------------------------------------------

//  Only a class built on QQuickBasicProgressBar may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickBasicProgressBar : QQuickBasicProgressBar {
  using QQuickBasicProgressBar::itemChange;
};

//  const QMetaObject *QQuickBasicProgressBar::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK22QQuickBasicProgressBar10metaObjectEv(
    const QQuickBasicProgressBar *self) {
  return self->metaObject();
}

//  void *QQuickBasicProgressBar::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN22QQuickBasicProgressBar11qt_metacastEPKc(
    QQuickBasicProgressBar *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickBasicProgressBar::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN22QQuickBasicProgressBar11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickBasicProgressBar *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  bool QQuickBasicProgressBar::isIndeterminate() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QQuickBasicProgressBar15isIndeterminateEv(
    const QQuickBasicProgressBar *self) {
  return self->isIndeterminate();
}

//  void QQuickBasicProgressBar::setIndeterminate(bool indeterminate)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickBasicProgressBar16setIndeterminateEb(
    QQuickBasicProgressBar *self,
    bool indeterminate) {
  self->setIndeterminate(indeterminate);
}

//  qreal QQuickBasicProgressBar::progress() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK22QQuickBasicProgressBar8progressEv(
    const QQuickBasicProgressBar *self) {
  return self->progress();
}

//  void QQuickBasicProgressBar::setProgress(qreal progress)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickBasicProgressBar11setProgressEd(
    QQuickBasicProgressBar *self,
    qreal progress) {
  self->setProgress(progress);
}

//  QColor QQuickBasicProgressBar::color() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK22QQuickBasicProgressBar5colorEv(
    const QQuickBasicProgressBar *self) {
  return new QColor(self->color());
}

//  void QQuickBasicProgressBar::setColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickBasicProgressBar8setColorERK6QColor(
    QQuickBasicProgressBar *self,
    const QColor *color) {
  self->setColor(*color);
}

//  void QQuickBasicProgressBar::itemChange(ItemChange change, const
//      ItemChangeData &data)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickBasicProgressBar10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE(
    QQuickBasicProgressBar *self,
    QQuickItem::ItemChange change,
    const QQuickItem::ItemChangeData *data) {
  self->itemChange(change, *data);
}

//  QSGNode *QQuickBasicProgressBar::updatePaintNode(QSGNode *oldNode,
//      UpdatePaintNodeData *a1)
extern "C" Q_DECL_EXPORT
QSGNode *ritual_ZN22QQuickBasicProgressBar15updatePaintNodeEP7QSGNodePN10QQuickItem19UpdatePaintNodeDataE(
    QQuickBasicProgressBar *self,
    QSGNode *oldNode,
    QQuickItem::UpdatePaintNodeData *a1) {
  return self->updatePaintNode(oldNode, a1);
}

//  void QQuickBasicProgressBar::itemChange(ItemChange change, const
//      ItemChangeData &data)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QQuickBasicProgressBar10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE(
    QQuickBasicProgressBar *self,
    QQuickItem::ItemChange change,
    const QQuickItem::ItemChangeData *data) {
  static_cast<OwnQQuickBasicProgressBar *>(self)->OwnQQuickBasicProgressBar::itemChange(
      change,
      *data);
}
