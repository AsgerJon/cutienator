//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickspriteengine_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/qtquickglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#if QT_CONFIG(quick_sprite)
#if QT_CONFIG(quick_sprite)
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickspriteengine_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#if QT_CONFIG(quick_sprite)
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquicksprite_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#endif
#include <QtGui/qimage.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>
#include <QtQml/QQmlListProperty>

//  A QQuickSpriteEngine that Python can take functions over in. Every QQuickSpriteEngine
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(quick_sprite)
typedef void (*CuteQQuickSpriteEngineCall0)(const void *, int, int *);
#endif  // QT_CONFIG(quick_sprite)
#if QT_CONFIG(quick_sprite)
typedef void (*CuteQQuickSpriteEngineCall1)(const void *, int, int *);
#endif  // QT_CONFIG(quick_sprite)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickSpriteEngineCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickSpriteEngineCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickSpriteEngineCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickSpriteEngineCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickSpriteEngineCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickSpriteEngineCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickSpriteEngineCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickSpriteEngine : public QQuickSpriteEngine {
public:
  using QQuickSpriteEngine::QQuickSpriteEngine;
  void *taken[9] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(quick_sprite)
    if (!std::strcmp(key, "_ZN22QQuickStochasticEngine7restartEi")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_sprite)
#if QT_CONFIG(quick_sprite)
    if (!std::strcmp(key, "_ZN22QQuickStochasticEngine7advanceEi")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_sprite)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if QT_CONFIG(quick_sprite)
  //  void QQuickSpriteEngine::restart(int index)
  void restart(int index) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickSpriteEngineCall0 call = reinterpret_cast<CuteQQuickSpriteEngineCall0>(taken[0]);
      call(this, index, &handled);
      if (handled) return;
    }
    QQuickSpriteEngine::restart(index);
  }
#endif  // QT_CONFIG(quick_sprite)

#if QT_CONFIG(quick_sprite)
  //  void QQuickSpriteEngine::advance(int index)
  void advance(int index) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickSpriteEngineCall1 call = reinterpret_cast<CuteQQuickSpriteEngineCall1>(taken[1]);
      call(this, index, &handled);
      if (handled) return;
    }
    QQuickSpriteEngine::advance(index);
  }
#endif  // QT_CONFIG(quick_sprite)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickSpriteEngineCall2 call = reinterpret_cast<CuteQQuickSpriteEngineCall2>(taken[2]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickSpriteEngineCall3 call = reinterpret_cast<CuteQQuickSpriteEngineCall3>(taken[3]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickSpriteEngineCall4 call = reinterpret_cast<CuteQQuickSpriteEngineCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickSpriteEngineCall5 call = reinterpret_cast<CuteQQuickSpriteEngineCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickSpriteEngineCall6 call = reinterpret_cast<CuteQQuickSpriteEngineCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickSpriteEngineCall7 call = reinterpret_cast<CuteQQuickSpriteEngineCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickSpriteEngineCall8 call = reinterpret_cast<CuteQQuickSpriteEngineCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickSpriteEngine::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18QQuickSpriteEngine10metaObjectEv(
    const QQuickSpriteEngine *self) {
  return self->metaObject();
}

//  void *QQuickSpriteEngine::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN18QQuickSpriteEngine11qt_metacastEPKc(
    QQuickSpriteEngine *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickSpriteEngine::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN18QQuickSpriteEngine11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickSpriteEngine *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickSpriteEngine::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18QQuickSpriteEngine2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickSpriteEngine::tr(s, c, n));
}

//  QQuickSpriteEngine::QQuickSpriteEngine(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickSpriteEngine *ritual_ZN18QQuickSpriteEngineC1EP7QObject(
    QObject *parent) {
  return new CuteQQuickSpriteEngine(parent);
}

//  QQuickSpriteEngine::QQuickSpriteEngine(const QList<QQuickSprite *>
//      &sprites, QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickSpriteEngine *ritual_ZN18QQuickSpriteEngineC1ERK5QListIP12QQuickSpriteEP7QObject(
    const QList<QQuickSprite *> *sprites,
    QObject *parent) {
  return new CuteQQuickSpriteEngine(*sprites, parent);
}

//  QQuickSpriteEngine::~QQuickSpriteEngine()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickSpriteEngineD1Ev(QQuickSpriteEngine *self) {
  delete self;
}

//  QQmlListProperty<QQuickSprite> QQuickSpriteEngine::sprites()
extern "C" Q_DECL_EXPORT
QQmlListProperty<QQuickSprite> *ritual_ZN18QQuickSpriteEngine7spritesEv(
    QQuickSpriteEngine *self) {
  return new QQmlListProperty<QQuickSprite>(self->sprites());
}

//  QQuickSprite *QQuickSpriteEngine::sprite(int sprite) const
extern "C" Q_DECL_EXPORT
QQuickSprite *ritual_ZNK18QQuickSpriteEngine6spriteEi(
    const QQuickSpriteEngine *self,
    int sprite) {
  return self->sprite(sprite);
}

//  int QQuickSpriteEngine::spriteState(int sprite) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QQuickSpriteEngine11spriteStateEi(
    const QQuickSpriteEngine *self,
    int sprite) {
  return self->spriteState(sprite);
}

//  int QQuickSpriteEngine::spriteStart(int sprite) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QQuickSpriteEngine11spriteStartEi(
    const QQuickSpriteEngine *self,
    int sprite) {
  return self->spriteStart(sprite);
}

//  int QQuickSpriteEngine::spriteFrames(int sprite) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QQuickSpriteEngine12spriteFramesEi(
    const QQuickSpriteEngine *self,
    int sprite) {
  return self->spriteFrames(sprite);
}

//  int QQuickSpriteEngine::spriteDuration(int sprite) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QQuickSpriteEngine14spriteDurationEi(
    const QQuickSpriteEngine *self,
    int sprite) {
  return self->spriteDuration(sprite);
}

//  int QQuickSpriteEngine::spriteX(int sprite) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QQuickSpriteEngine7spriteXEi(
    const QQuickSpriteEngine *self,
    int sprite) {
  return self->spriteX(sprite);
}

//  int QQuickSpriteEngine::spriteY(int sprite) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QQuickSpriteEngine7spriteYEi(
    const QQuickSpriteEngine *self,
    int sprite) {
  return self->spriteY(sprite);
}

//  int QQuickSpriteEngine::spriteWidth(int sprite) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QQuickSpriteEngine11spriteWidthEi(
    const QQuickSpriteEngine *self,
    int sprite) {
  return self->spriteWidth(sprite);
}

//  int QQuickSpriteEngine::spriteHeight(int sprite) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QQuickSpriteEngine12spriteHeightEi(
    const QQuickSpriteEngine *self,
    int sprite) {
  return self->spriteHeight(sprite);
}

//  int QQuickSpriteEngine::spriteCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QQuickSpriteEngine11spriteCountEv(
    const QQuickSpriteEngine *self) {
  return self->spriteCount();
}

//  int QQuickSpriteEngine::maxFrames() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QQuickSpriteEngine9maxFramesEv(
    const QQuickSpriteEngine *self) {
  return self->maxFrames();
}

//  void QQuickSpriteEngine::restart(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickSpriteEngine7restartEi(
    QQuickSpriteEngine *self,
    int index) {
  self->restart(index);
}

//  void QQuickSpriteEngine::advance(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickSpriteEngine7advanceEi(
    QQuickSpriteEngine *self,
    int index) {
  self->advance(index);
}

//  bool QQuickSpriteEngine::isNull() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QQuickSpriteEngine6isNullEv(
    const QQuickSpriteEngine *self) {
  return self->isNull();
}

//  bool QQuickSpriteEngine::isReady() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QQuickSpriteEngine7isReadyEv(
    const QQuickSpriteEngine *self) {
  return self->isReady();
}

//  bool QQuickSpriteEngine::isLoading() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QQuickSpriteEngine9isLoadingEv(
    const QQuickSpriteEngine *self) {
  return self->isLoading();
}

//  bool QQuickSpriteEngine::isError() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QQuickSpriteEngine7isErrorEv(
    const QQuickSpriteEngine *self) {
  return self->isError();
}

//  QQuickPixmap::Status QQuickSpriteEngine::status() const
extern "C" Q_DECL_EXPORT
QQuickPixmap::Status ritual_ZNK18QQuickSpriteEngine6statusEv(
    const QQuickSpriteEngine *self) {
  return self->status();
}

//  void QQuickSpriteEngine::startAssemblingImage()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickSpriteEngine20startAssemblingImageEv(
    QQuickSpriteEngine *self) {
  self->startAssemblingImage();
}

//  QImage QQuickSpriteEngine::assembledImage(int maxSize)
extern "C" Q_DECL_EXPORT
QImage *ritual_ZN18QQuickSpriteEngine14assembledImageEi(
    QQuickSpriteEngine *self,
    int maxSize) {
  return new QImage(self->assembledImage(maxSize));
}

//  int QQuickSpriteEngine::pseudospriteProgress(int a0, int a1, int *rd)
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QQuickSpriteEngine20pseudospriteProgressEiiPi(
    const QQuickSpriteEngine *self,
    int a0,
    int a1,
    int *rd) {
  return self->pseudospriteProgress(a0, a1, rd);
}

//  a Python function taken by a CuteQQuickSpriteEngine, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickSpriteEngine(
    QQuickSpriteEngine *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickSpriteEngine *>(self)->take(key, call);
}

//  void QQuickSpriteEngine::restart(int index)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QQuickSpriteEngine7restartEi(
    QQuickSpriteEngine *self,
    int index) {
  self->QQuickSpriteEngine::restart(index);
}

//  void QQuickSpriteEngine::advance(int index)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QQuickSpriteEngine7advanceEi(
    QQuickSpriteEngine *self,
    int index) {
  self->QQuickSpriteEngine::advance(index);
}

//  a QQmlListProperty<QQuickSprite> a ritual of QQuickSpriteEngine gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQuickSpriteEngine__QQmlListProperty_QQuickSprite(
    QQmlListProperty<QQuickSprite> *self) {
  delete self;
}

#endif  // QT_CONFIG(quick_sprite)
#endif  // QT_CONFIG(quick_sprite)
