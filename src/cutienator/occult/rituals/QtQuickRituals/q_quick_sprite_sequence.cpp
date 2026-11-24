//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickspritesequence_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick/qtquickglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#if QT_CONFIG(quick_sprite)
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickspritesequence_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  Only a class built on QQuickSpriteSequence may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickSpriteSequence : QQuickSpriteSequence {
  using QQuickSpriteSequence::updatePaintNode;
};

//  const QMetaObject *QQuickSpriteSequence::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK20QQuickSpriteSequence10metaObjectEv(
    const QQuickSpriteSequence *self) {
  return self->metaObject();
}

//  QString QQuickSpriteSequence::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN20QQuickSpriteSequence2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickSpriteSequence::tr(s, c, n));
}

//  QQuickSpriteSequence::QQuickSpriteSequence(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickSpriteSequence *ritual_ZN20QQuickSpriteSequenceC1EP10QQuickItem(
    QQuickItem *parent) {
  return new QQuickSpriteSequence(parent);
}

//  bool QQuickSpriteSequence::running() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QQuickSpriteSequence7runningEv(
    const QQuickSpriteSequence *self) {
  return self->running();
}

//  bool QQuickSpriteSequence::interpolate() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QQuickSpriteSequence11interpolateEv(
    const QQuickSpriteSequence *self) {
  return self->interpolate();
}

//  QString QQuickSpriteSequence::goalSprite() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK20QQuickSpriteSequence10goalSpriteEv(
    const QQuickSpriteSequence *self) {
  return new QString(self->goalSprite());
}

//  QString QQuickSpriteSequence::currentSprite() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK20QQuickSpriteSequence13currentSpriteEv(
    const QQuickSpriteSequence *self) {
  return new QString(self->currentSprite());
}

//  void QQuickSpriteSequence::jumpTo(const QString &sprite)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickSpriteSequence6jumpToERK7QString(
    QQuickSpriteSequence *self,
    const QString *sprite) {
  self->jumpTo(*sprite);
}

//  void QQuickSpriteSequence::setGoalSprite(const QString &sprite)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickSpriteSequence13setGoalSpriteERK7QString(
    QQuickSpriteSequence *self,
    const QString *sprite) {
  self->setGoalSprite(*sprite);
}

//  void QQuickSpriteSequence::setRunning(bool arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickSpriteSequence10setRunningEb(
    QQuickSpriteSequence *self,
    bool arg) {
  self->setRunning(arg);
}

//  void QQuickSpriteSequence::setInterpolate(bool arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickSpriteSequence14setInterpolateEb(
    QQuickSpriteSequence *self,
    bool arg) {
  self->setInterpolate(arg);
}

//  void QQuickSpriteSequence::createEngine()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickSpriteSequence12createEngineEv(
    QQuickSpriteSequence *self) {
  self->createEngine();
}

//  void QQuickSpriteSequence::reset()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickSpriteSequence5resetEv(QQuickSpriteSequence *self) {
  self->reset();
}

//  QSGNode *QQuickSpriteSequence::updatePaintNode(QSGNode *a0,
//      UpdatePaintNodeData *a1)
extern "C" Q_DECL_EXPORT
QSGNode *ritual_ZN20QQuickSpriteSequence15updatePaintNodeEP7QSGNodePN10QQuickItem19UpdatePaintNodeDataE(
    QQuickSpriteSequence *self,
    QSGNode *a0,
    QQuickItem::UpdatePaintNodeData *a1) {
  return self->updatePaintNode(a0, a1);
}

//  void QQuickSpriteSequence::prepareNextFrame(QSGSpriteNode *node)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickSpriteSequence16prepareNextFrameEP13QSGSpriteNode(
    QQuickSpriteSequence *self,
    QSGSpriteNode *node) {
  self->prepareNextFrame(node);
}

//  QSGSpriteNode *QQuickSpriteSequence::initNode()
extern "C" Q_DECL_EXPORT
QSGSpriteNode *ritual_ZN20QQuickSpriteSequence8initNodeEv(
    QQuickSpriteSequence *self) {
  return self->initNode();
}

//  QQuickSpriteSequencePrivate *QQuickSpriteSequence::d_func()
extern "C" Q_DECL_EXPORT
QQuickSpriteSequencePrivate *ritual_ZN20QQuickSpriteSequence6d_funcEv(
    QQuickSpriteSequence *self) {
  return self->d_func();
}

//  const QQuickSpriteSequencePrivate *QQuickSpriteSequence::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickSpriteSequencePrivate *ritual_ZNK20QQuickSpriteSequence6d_funcEv(
    const QQuickSpriteSequence *self) {
  return self->d_func();
}

//  QSGNode *QQuickSpriteSequence::updatePaintNode(QSGNode *a0,
//      UpdatePaintNodeData *a1)
extern "C" Q_DECL_EXPORT
QSGNode *ritual_own_ZN20QQuickSpriteSequence15updatePaintNodeEP7QSGNodePN10QQuickItem19UpdatePaintNodeDataE(
    QQuickSpriteSequence *self,
    QSGNode *a0,
    QQuickItem::UpdatePaintNodeData *a1) {
  return static_cast<OwnQQuickSpriteSequence *>(self)->OwnQQuickSpriteSequence::updatePaintNode(
      a0,
      a1);
}

#endif  // QT_CONFIG(quick_sprite)
