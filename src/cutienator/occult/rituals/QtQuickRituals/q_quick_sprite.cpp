//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquicksprite_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQuick/qtquickglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#if QT_CONFIG(quick_sprite)
#if QT_CONFIG(quick_sprite)
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquicksprite_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QQuickSprite that Python can take functions over in. Every QQuickSprite
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(quick_sprite)
typedef int (*CuteQQuickSpriteCall0)(const void *, int *);
#endif  // QT_CONFIG(quick_sprite)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickSpriteCall1)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickSpriteCall2)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickSpriteCall3)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickSpriteCall4)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickSpriteCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickSpriteCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickSpriteCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickSprite : public QQuickSprite {
public:
  using QQuickSprite::QQuickSprite;
  void *taken[8] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(quick_sprite)
    if (!std::strcmp(key, "_ZNK21QQuickStochasticState14variedDurationEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_sprite)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if QT_CONFIG(quick_sprite)
  //  int QQuickSprite::variedDuration() const
  int variedDuration() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickSpriteCall0 call = reinterpret_cast<CuteQQuickSpriteCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickSprite::variedDuration();
  }
#endif  // QT_CONFIG(quick_sprite)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickSpriteCall1 call = reinterpret_cast<CuteQQuickSpriteCall1>(taken[1]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickSpriteCall2 call = reinterpret_cast<CuteQQuickSpriteCall2>(taken[2]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickSpriteCall3 call = reinterpret_cast<CuteQQuickSpriteCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickSpriteCall4 call = reinterpret_cast<CuteQQuickSpriteCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickSpriteCall5 call = reinterpret_cast<CuteQQuickSpriteCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickSpriteCall6 call = reinterpret_cast<CuteQQuickSpriteCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickSpriteCall7 call = reinterpret_cast<CuteQQuickSpriteCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickSprite::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK12QQuickSprite10metaObjectEv(
    const QQuickSprite *self) {
  return self->metaObject();
}

//  void *QQuickSprite::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN12QQuickSprite11qt_metacastEPKc(
    QQuickSprite *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickSprite::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN12QQuickSprite11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickSprite *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickSprite::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN12QQuickSprite2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickSprite::tr(s, c, n));
}

//  QQuickSprite::QQuickSprite(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickSprite *ritual_ZN12QQuickSpriteC1EP7QObject(QObject *parent) {
  return new CuteQQuickSprite(parent);
}

//  QQuickSprite::~QQuickSprite()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickSpriteD1Ev(QQuickSprite *self) {
  delete self;
}

//  QUrl QQuickSprite::source() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK12QQuickSprite6sourceEv(const QQuickSprite *self) {
  return new QUrl(self->source());
}

//  int QQuickSprite::frameHeight() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QQuickSprite11frameHeightEv(const QQuickSprite *self) {
  return self->frameHeight();
}

//  int QQuickSprite::frameWidth() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QQuickSprite10frameWidthEv(const QQuickSprite *self) {
  return self->frameWidth();
}

//  bool QQuickSprite::reverse() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QQuickSprite7reverseEv(const QQuickSprite *self) {
  return self->reverse();
}

//  int QQuickSprite::frames() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QQuickSprite6framesEv(const QQuickSprite *self) {
  return self->frames();
}

//  int QQuickSprite::frameCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QQuickSprite10frameCountEv(const QQuickSprite *self) {
  return self->frameCount();
}

//  int QQuickSprite::frameX() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QQuickSprite6frameXEv(const QQuickSprite *self) {
  return self->frameX();
}

//  int QQuickSprite::frameY() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QQuickSprite6frameYEv(const QQuickSprite *self) {
  return self->frameY();
}

//  void QQuickSprite::resetFrameRate()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickSprite14resetFrameRateEv(QQuickSprite *self) {
  self->resetFrameRate();
}

//  qreal QQuickSprite::frameRate() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK12QQuickSprite9frameRateEv(const QQuickSprite *self) {
  return self->frameRate();
}

//  qreal QQuickSprite::frameRateVariation() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK12QQuickSprite18frameRateVariationEv(
    const QQuickSprite *self) {
  return self->frameRateVariation();
}

//  void QQuickSprite::resetFrameDuration()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickSprite18resetFrameDurationEv(QQuickSprite *self) {
  self->resetFrameDuration();
}

//  int QQuickSprite::frameDuration() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QQuickSprite13frameDurationEv(const QQuickSprite *self) {
  return self->frameDuration();
}

//  int QQuickSprite::frameDurationVariation() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QQuickSprite22frameDurationVariationEv(
    const QQuickSprite *self) {
  return self->frameDurationVariation();
}

//  int QQuickSprite::variedDuration() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QQuickSprite14variedDurationEv(const QQuickSprite *self) {
  return self->variedDuration();
}

//  bool QQuickSprite::frameSync() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QQuickSprite9frameSyncEv(const QQuickSprite *self) {
  return self->frameSync();
}

//  void QQuickSprite::setDevicePixelRatio(qreal dpr)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickSprite19setDevicePixelRatioEd(
    QQuickSprite *self,
    qreal dpr) {
  self->setDevicePixelRatio(dpr);
}

//  qreal QQuickSprite::devicePixelRatio() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK12QQuickSprite16devicePixelRatioEv(
    const QQuickSprite *self) {
  return self->devicePixelRatio();
}

//  void QQuickSprite::sourceChanged(QUrl arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickSprite13sourceChangedE4QUrl(
    QQuickSprite *self,
    const QUrl *arg) {
  self->sourceChanged(*arg);
}

//  void QQuickSprite::frameHeightChanged(int arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickSprite18frameHeightChangedEi(
    QQuickSprite *self,
    int arg) {
  self->frameHeightChanged(arg);
}

//  void QQuickSprite::frameWidthChanged(int arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickSprite17frameWidthChangedEi(
    QQuickSprite *self,
    int arg) {
  self->frameWidthChanged(arg);
}

//  void QQuickSprite::reverseChanged(bool arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickSprite14reverseChangedEb(
    QQuickSprite *self,
    bool arg) {
  self->reverseChanged(arg);
}

//  void QQuickSprite::frameCountChanged(int arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickSprite17frameCountChangedEi(
    QQuickSprite *self,
    int arg) {
  self->frameCountChanged(arg);
}

//  void QQuickSprite::frameXChanged(int arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickSprite13frameXChangedEi(QQuickSprite *self, int arg) {
  self->frameXChanged(arg);
}

//  void QQuickSprite::frameYChanged(int arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickSprite13frameYChangedEi(QQuickSprite *self, int arg) {
  self->frameYChanged(arg);
}

//  void QQuickSprite::frameRateChanged(qreal arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickSprite16frameRateChangedEd(
    QQuickSprite *self,
    qreal arg) {
  self->frameRateChanged(arg);
}

//  void QQuickSprite::frameRateVariationChanged(qreal arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickSprite25frameRateVariationChangedEd(
    QQuickSprite *self,
    qreal arg) {
  self->frameRateVariationChanged(arg);
}

//  void QQuickSprite::frameDurationChanged(int arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickSprite20frameDurationChangedEi(
    QQuickSprite *self,
    int arg) {
  self->frameDurationChanged(arg);
}

//  void QQuickSprite::frameDurationVariationChanged(int arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickSprite29frameDurationVariationChangedEi(
    QQuickSprite *self,
    int arg) {
  self->frameDurationVariationChanged(arg);
}

//  void QQuickSprite::frameSyncChanged(bool arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickSprite16frameSyncChangedEb(
    QQuickSprite *self,
    bool arg) {
  self->frameSyncChanged(arg);
}

//  void QQuickSprite::setSource(QUrl arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickSprite9setSourceE4QUrl(
    QQuickSprite *self,
    const QUrl *arg) {
  self->setSource(*arg);
}

//  void QQuickSprite::setFrameHeight(int arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickSprite14setFrameHeightEi(QQuickSprite *self, int arg) {
  self->setFrameHeight(arg);
}

//  void QQuickSprite::setFrameWidth(int arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickSprite13setFrameWidthEi(QQuickSprite *self, int arg) {
  self->setFrameWidth(arg);
}

//  void QQuickSprite::setReverse(bool arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickSprite10setReverseEb(QQuickSprite *self, bool arg) {
  self->setReverse(arg);
}

//  void QQuickSprite::setFrames(int arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickSprite9setFramesEi(QQuickSprite *self, int arg) {
  self->setFrames(arg);
}

//  void QQuickSprite::setFrameCount(int arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickSprite13setFrameCountEi(QQuickSprite *self, int arg) {
  self->setFrameCount(arg);
}

//  void QQuickSprite::setFrameX(int arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickSprite9setFrameXEi(QQuickSprite *self, int arg) {
  self->setFrameX(arg);
}

//  void QQuickSprite::setFrameY(int arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickSprite9setFrameYEi(QQuickSprite *self, int arg) {
  self->setFrameY(arg);
}

//  void QQuickSprite::setFrameRate(qreal arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickSprite12setFrameRateEd(QQuickSprite *self, qreal arg) {
  self->setFrameRate(arg);
}

//  void QQuickSprite::setFrameRateVariation(qreal arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickSprite21setFrameRateVariationEd(
    QQuickSprite *self,
    qreal arg) {
  self->setFrameRateVariation(arg);
}

//  void QQuickSprite::setFrameDuration(int arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickSprite16setFrameDurationEi(
    QQuickSprite *self,
    int arg) {
  self->setFrameDuration(arg);
}

//  void QQuickSprite::setFrameDurationVariation(int arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickSprite25setFrameDurationVariationEi(
    QQuickSprite *self,
    int arg) {
  self->setFrameDurationVariation(arg);
}

//  void QQuickSprite::setFrameSync(bool arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickSprite12setFrameSyncEb(QQuickSprite *self, bool arg) {
  self->setFrameSync(arg);
}

//  void QQuickSprite::startImageLoading()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickSprite17startImageLoadingEv(QQuickSprite *self) {
  self->startImageLoading();
}

//  a Python function taken by a CuteQQuickSprite, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickSprite(
    QQuickSprite *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickSprite *>(self)->take(key, call);
}

//  int QQuickSprite::variedDuration() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK12QQuickSprite14variedDurationEv(
    const QQuickSprite *self) {
  return self->QQuickSprite::variedDuration();
}

//  QList<QQuickSprite *>::QList()
extern "C" Q_DECL_EXPORT
QList<QQuickSprite *> *ritual_list_make_QQuickSprite_ptr() {
  return new QList<QQuickSprite *>();
}

//  void QList<QQuickSprite *>::append(const QQuickSprite * &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QQuickSprite_ptr(
    QList<QQuickSprite *> *self,
    QQuickSprite *element) {
  self->append(element);
}

//  qsizetype QList<QQuickSprite *>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QQuickSprite_ptr(
    const QList<QQuickSprite *> *self) {
  return self->size();
}

//  const QQuickSprite * &QList<QQuickSprite *>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QQuickSprite *ritual_list_at_QQuickSprite_ptr(
    const QList<QQuickSprite *> *self,
    long long index) {
  return self->at(index);
}

//  QList<QQuickSprite *>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QQuickSprite_ptr(QList<QQuickSprite *> *self) {
  delete self;
}

#endif  // QT_CONFIG(quick_sprite)
#endif  // QT_CONFIG(quick_sprite)
