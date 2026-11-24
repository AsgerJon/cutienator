//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickanimatedsprite_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick/qtquickglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#if QT_CONFIG(quick_sprite)
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickanimatedsprite_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#include <QtQuick/qquickitem.h>

//  Only a class built on QQuickAnimatedSprite may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickAnimatedSprite : QQuickAnimatedSprite {
  using QQuickAnimatedSprite::componentComplete;
  using QQuickAnimatedSprite::updatePaintNode;
  using QQuickAnimatedSprite::itemChange;
};

//  const QMetaObject *QQuickAnimatedSprite::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK20QQuickAnimatedSprite10metaObjectEv(
    const QQuickAnimatedSprite *self) {
  return self->metaObject();
}

//  QString QQuickAnimatedSprite::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN20QQuickAnimatedSprite2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickAnimatedSprite::tr(s, c, n));
}

//  QQuickAnimatedSprite::QQuickAnimatedSprite(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickAnimatedSprite *ritual_ZN20QQuickAnimatedSpriteC1EP10QQuickItem(
    QQuickItem *parent) {
  return new QQuickAnimatedSprite(parent);
}

//  bool QQuickAnimatedSprite::running() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QQuickAnimatedSprite7runningEv(
    const QQuickAnimatedSprite *self) {
  return self->running();
}

//  bool QQuickAnimatedSprite::interpolate() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QQuickAnimatedSprite11interpolateEv(
    const QQuickAnimatedSprite *self) {
  return self->interpolate();
}

//  QUrl QQuickAnimatedSprite::source() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK20QQuickAnimatedSprite6sourceEv(
    const QQuickAnimatedSprite *self) {
  return new QUrl(self->source());
}

//  bool QQuickAnimatedSprite::reverse() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QQuickAnimatedSprite7reverseEv(
    const QQuickAnimatedSprite *self) {
  return self->reverse();
}

//  bool QQuickAnimatedSprite::frameSync() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QQuickAnimatedSprite9frameSyncEv(
    const QQuickAnimatedSprite *self) {
  return self->frameSync();
}

//  int QQuickAnimatedSprite::frameCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QQuickAnimatedSprite10frameCountEv(
    const QQuickAnimatedSprite *self) {
  return self->frameCount();
}

//  int QQuickAnimatedSprite::frameHeight() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QQuickAnimatedSprite11frameHeightEv(
    const QQuickAnimatedSprite *self) {
  return self->frameHeight();
}

//  int QQuickAnimatedSprite::frameWidth() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QQuickAnimatedSprite10frameWidthEv(
    const QQuickAnimatedSprite *self) {
  return self->frameWidth();
}

//  int QQuickAnimatedSprite::frameX() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QQuickAnimatedSprite6frameXEv(
    const QQuickAnimatedSprite *self) {
  return self->frameX();
}

//  int QQuickAnimatedSprite::frameY() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QQuickAnimatedSprite6frameYEv(
    const QQuickAnimatedSprite *self) {
  return self->frameY();
}

//  qreal QQuickAnimatedSprite::frameRate() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK20QQuickAnimatedSprite9frameRateEv(
    const QQuickAnimatedSprite *self) {
  return self->frameRate();
}

//  int QQuickAnimatedSprite::frameDuration() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QQuickAnimatedSprite13frameDurationEv(
    const QQuickAnimatedSprite *self) {
  return self->frameDuration();
}

//  int QQuickAnimatedSprite::loops() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QQuickAnimatedSprite5loopsEv(
    const QQuickAnimatedSprite *self) {
  return self->loops();
}

//  bool QQuickAnimatedSprite::paused() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QQuickAnimatedSprite6pausedEv(
    const QQuickAnimatedSprite *self) {
  return self->paused();
}

//  int QQuickAnimatedSprite::currentFrame() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QQuickAnimatedSprite12currentFrameEv(
    const QQuickAnimatedSprite *self) {
  return self->currentFrame();
}

//  FinishBehavior QQuickAnimatedSprite::finishBehavior() const
extern "C" Q_DECL_EXPORT
QQuickAnimatedSprite::FinishBehavior ritual_ZNK20QQuickAnimatedSprite14finishBehaviorEv(
    const QQuickAnimatedSprite *self) {
  return self->finishBehavior();
}

//  void QQuickAnimatedSprite::setFinishBehavior(FinishBehavior arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickAnimatedSprite17setFinishBehaviorENS_14FinishBehaviorE(
    QQuickAnimatedSprite *self,
    QQuickAnimatedSprite::FinishBehavior arg) {
  self->setFinishBehavior(arg);
}

//  void QQuickAnimatedSprite::start()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickAnimatedSprite5startEv(QQuickAnimatedSprite *self) {
  self->start();
}

//  void QQuickAnimatedSprite::stop()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickAnimatedSprite4stopEv(QQuickAnimatedSprite *self) {
  self->stop();
}

//  void QQuickAnimatedSprite::restart()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickAnimatedSprite7restartEv(QQuickAnimatedSprite *self) {
  self->restart();
}

//  void QQuickAnimatedSprite::advance(int frames)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickAnimatedSprite7advanceEi(
    QQuickAnimatedSprite *self,
    int frames) {
  self->advance(frames);
}

//  void QQuickAnimatedSprite::pause()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickAnimatedSprite5pauseEv(QQuickAnimatedSprite *self) {
  self->pause();
}

//  void QQuickAnimatedSprite::resume()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickAnimatedSprite6resumeEv(QQuickAnimatedSprite *self) {
  self->resume();
}

//  void QQuickAnimatedSprite::setRunning(bool arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickAnimatedSprite10setRunningEb(
    QQuickAnimatedSprite *self,
    bool arg) {
  self->setRunning(arg);
}

//  void QQuickAnimatedSprite::setPaused(bool arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickAnimatedSprite9setPausedEb(
    QQuickAnimatedSprite *self,
    bool arg) {
  self->setPaused(arg);
}

//  void QQuickAnimatedSprite::setInterpolate(bool arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickAnimatedSprite14setInterpolateEb(
    QQuickAnimatedSprite *self,
    bool arg) {
  self->setInterpolate(arg);
}

//  void QQuickAnimatedSprite::setSource(const QUrl &arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickAnimatedSprite9setSourceERK4QUrl(
    QQuickAnimatedSprite *self,
    const QUrl *arg) {
  self->setSource(*arg);
}

//  void QQuickAnimatedSprite::setReverse(bool arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickAnimatedSprite10setReverseEb(
    QQuickAnimatedSprite *self,
    bool arg) {
  self->setReverse(arg);
}

//  void QQuickAnimatedSprite::setFrameSync(bool arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickAnimatedSprite12setFrameSyncEb(
    QQuickAnimatedSprite *self,
    bool arg) {
  self->setFrameSync(arg);
}

//  void QQuickAnimatedSprite::setFrameCount(int arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickAnimatedSprite13setFrameCountEi(
    QQuickAnimatedSprite *self,
    int arg) {
  self->setFrameCount(arg);
}

//  void QQuickAnimatedSprite::setFrameHeight(int arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickAnimatedSprite14setFrameHeightEi(
    QQuickAnimatedSprite *self,
    int arg) {
  self->setFrameHeight(arg);
}

//  void QQuickAnimatedSprite::setFrameWidth(int arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickAnimatedSprite13setFrameWidthEi(
    QQuickAnimatedSprite *self,
    int arg) {
  self->setFrameWidth(arg);
}

//  void QQuickAnimatedSprite::setFrameX(int arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickAnimatedSprite9setFrameXEi(
    QQuickAnimatedSprite *self,
    int arg) {
  self->setFrameX(arg);
}

//  void QQuickAnimatedSprite::setFrameY(int arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickAnimatedSprite9setFrameYEi(
    QQuickAnimatedSprite *self,
    int arg) {
  self->setFrameY(arg);
}

//  void QQuickAnimatedSprite::setFrameRate(qreal arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickAnimatedSprite12setFrameRateEd(
    QQuickAnimatedSprite *self,
    qreal arg) {
  self->setFrameRate(arg);
}

//  void QQuickAnimatedSprite::setFrameDuration(int arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickAnimatedSprite16setFrameDurationEi(
    QQuickAnimatedSprite *self,
    int arg) {
  self->setFrameDuration(arg);
}

//  void QQuickAnimatedSprite::resetFrameRate()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickAnimatedSprite14resetFrameRateEv(
    QQuickAnimatedSprite *self) {
  self->resetFrameRate();
}

//  void QQuickAnimatedSprite::resetFrameDuration()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickAnimatedSprite18resetFrameDurationEv(
    QQuickAnimatedSprite *self) {
  self->resetFrameDuration();
}

//  void QQuickAnimatedSprite::setLoops(int arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickAnimatedSprite8setLoopsEi(
    QQuickAnimatedSprite *self,
    int arg) {
  self->setLoops(arg);
}

//  void QQuickAnimatedSprite::setCurrentFrame(int arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickAnimatedSprite15setCurrentFrameEi(
    QQuickAnimatedSprite *self,
    int arg) {
  self->setCurrentFrame(arg);
}

//  void QQuickAnimatedSprite::createEngine()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickAnimatedSprite12createEngineEv(
    QQuickAnimatedSprite *self) {
  self->createEngine();
}

//  void QQuickAnimatedSprite::reset()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickAnimatedSprite5resetEv(QQuickAnimatedSprite *self) {
  self->reset();
}

//  void QQuickAnimatedSprite::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickAnimatedSprite17componentCompleteEv(
    QQuickAnimatedSprite *self) {
  self->componentComplete();
}

//  QSGNode *QQuickAnimatedSprite::updatePaintNode(QSGNode *a0,
//      UpdatePaintNodeData *a1)
extern "C" Q_DECL_EXPORT
QSGNode *ritual_ZN20QQuickAnimatedSprite15updatePaintNodeEP7QSGNodePN10QQuickItem19UpdatePaintNodeDataE(
    QQuickAnimatedSprite *self,
    QSGNode *a0,
    QQuickItem::UpdatePaintNodeData *a1) {
  return self->updatePaintNode(a0, a1);
}

//  void QQuickAnimatedSprite::itemChange(ItemChange a0, const ItemChangeData
//      &a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickAnimatedSprite10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE(
    QQuickAnimatedSprite *self,
    QQuickItem::ItemChange a0,
    const QQuickItem::ItemChangeData *a1) {
  self->itemChange(a0, *a1);
}

//  void QQuickAnimatedSprite::maybeUpdate()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickAnimatedSprite11maybeUpdateEv(
    QQuickAnimatedSprite *self) {
  self->maybeUpdate();
}

//  bool QQuickAnimatedSprite::isCurrentFrameChangedConnected()
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QQuickAnimatedSprite30isCurrentFrameChangedConnectedEv(
    QQuickAnimatedSprite *self) {
  return self->isCurrentFrameChangedConnected();
}

//  void QQuickAnimatedSprite::prepareNextFrame(QSGSpriteNode *node)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickAnimatedSprite16prepareNextFrameEP13QSGSpriteNode(
    QQuickAnimatedSprite *self,
    QSGSpriteNode *node) {
  self->prepareNextFrame(node);
}

//  void QQuickAnimatedSprite::reloadImage()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickAnimatedSprite11reloadImageEv(
    QQuickAnimatedSprite *self) {
  self->reloadImage();
}

//  QSGSpriteNode *QQuickAnimatedSprite::initNode()
extern "C" Q_DECL_EXPORT
QSGSpriteNode *ritual_ZN20QQuickAnimatedSprite8initNodeEv(
    QQuickAnimatedSprite *self) {
  return self->initNode();
}

//  QQuickAnimatedSpritePrivate *QQuickAnimatedSprite::d_func()
extern "C" Q_DECL_EXPORT
QQuickAnimatedSpritePrivate *ritual_ZN20QQuickAnimatedSprite6d_funcEv(
    QQuickAnimatedSprite *self) {
  return self->d_func();
}

//  const QQuickAnimatedSpritePrivate *QQuickAnimatedSprite::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickAnimatedSpritePrivate *ritual_ZNK20QQuickAnimatedSprite6d_funcEv(
    const QQuickAnimatedSprite *self) {
  return self->d_func();
}

//  void QQuickAnimatedSprite::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQuickAnimatedSprite17componentCompleteEv(
    QQuickAnimatedSprite *self) {
  static_cast<OwnQQuickAnimatedSprite *>(self)->OwnQQuickAnimatedSprite::componentComplete();
}

//  QSGNode *QQuickAnimatedSprite::updatePaintNode(QSGNode *a0,
//      UpdatePaintNodeData *a1)
extern "C" Q_DECL_EXPORT
QSGNode *ritual_own_ZN20QQuickAnimatedSprite15updatePaintNodeEP7QSGNodePN10QQuickItem19UpdatePaintNodeDataE(
    QQuickAnimatedSprite *self,
    QSGNode *a0,
    QQuickItem::UpdatePaintNodeData *a1) {
  return static_cast<OwnQQuickAnimatedSprite *>(self)->OwnQQuickAnimatedSprite::updatePaintNode(
      a0,
      a1);
}

//  void QQuickAnimatedSprite::itemChange(ItemChange a0, const ItemChangeData
//      &a1)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQuickAnimatedSprite10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE(
    QQuickAnimatedSprite *self,
    QQuickItem::ItemChange a0,
    const QQuickItem::ItemChangeData *a1) {
  static_cast<OwnQQuickAnimatedSprite *>(self)->OwnQQuickAnimatedSprite::itemChange(
      a0,
      *a1);
}

#endif  // QT_CONFIG(quick_sprite)
