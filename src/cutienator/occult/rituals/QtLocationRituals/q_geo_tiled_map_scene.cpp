//  Written by dev_tooling.RitualGenerator from the records of
//  QtLocation/6.12.0/QtLocation/private/qgeotiledmapscene_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtLocation/6.12.0/QtLocation/private/qlocationglobal_p.h>
#include <QtLocation/QtLocation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/6.12.0/QtLocation/private/qgeotiledmapscene_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/6.12.0/QtLocation/private/qgeocameradata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QGeoTiledMapScene that Python can take functions over in. Every QGeoTiledMapScene
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQGeoTiledMapSceneCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQGeoTiledMapSceneCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGeoTiledMapSceneCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGeoTiledMapSceneCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGeoTiledMapSceneCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGeoTiledMapSceneCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGeoTiledMapSceneCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQGeoTiledMapScene : public QGeoTiledMapScene {
public:
  using QGeoTiledMapScene::QGeoTiledMapScene;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQGeoTiledMapSceneCall0 call = reinterpret_cast<CuteQGeoTiledMapSceneCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQGeoTiledMapSceneCall1 call = reinterpret_cast<CuteQGeoTiledMapSceneCall1>(taken[1]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQGeoTiledMapSceneCall2 call = reinterpret_cast<CuteQGeoTiledMapSceneCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQGeoTiledMapSceneCall3 call = reinterpret_cast<CuteQGeoTiledMapSceneCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQGeoTiledMapSceneCall4 call = reinterpret_cast<CuteQGeoTiledMapSceneCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[5]) {
      int handled = 0;
      CuteQGeoTiledMapSceneCall5 call = reinterpret_cast<CuteQGeoTiledMapSceneCall5>(taken[5]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQGeoTiledMapSceneCall6 call = reinterpret_cast<CuteQGeoTiledMapSceneCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QGeoTiledMapScene::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QGeoTiledMapScene10metaObjectEv(
    const QGeoTiledMapScene *self) {
  return self->metaObject();
}

//  QString QGeoTiledMapScene::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QGeoTiledMapScene2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QGeoTiledMapScene::tr(s, c, n));
}

//  QGeoTiledMapScenePrivate *QGeoTiledMapScene::d_func()
extern "C" Q_DECL_EXPORT
QGeoTiledMapScenePrivate *ritual_ZN17QGeoTiledMapScene6d_funcEv(
    QGeoTiledMapScene *self) {
  return self->d_func();
}

//  const QGeoTiledMapScenePrivate *QGeoTiledMapScene::d_func() const
extern "C" Q_DECL_EXPORT
const QGeoTiledMapScenePrivate *ritual_ZNK17QGeoTiledMapScene6d_funcEv(
    const QGeoTiledMapScene *self) {
  return self->d_func();
}

//  QGeoTiledMapScene::QGeoTiledMapScene(QObject *parent)
extern "C" Q_DECL_EXPORT
QGeoTiledMapScene *ritual_ZN17QGeoTiledMapSceneC1EP7QObject(
    QObject *parent) {
  return new CuteQGeoTiledMapScene(parent);
}

//  QGeoTiledMapScene::~QGeoTiledMapScene()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGeoTiledMapSceneD1Ev(QGeoTiledMapScene *self) {
  delete self;
}

//  void QGeoTiledMapScene::setScreenSize(const QSize &size)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGeoTiledMapScene13setScreenSizeERK5QSize(
    QGeoTiledMapScene *self,
    const QSize *size) {
  self->setScreenSize(*size);
}

//  void QGeoTiledMapScene::setTileSize(int tileSize)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGeoTiledMapScene11setTileSizeEi(
    QGeoTiledMapScene *self,
    int tileSize) {
  self->setTileSize(tileSize);
}

//  void QGeoTiledMapScene::setCameraData(const QGeoCameraData &cameraData)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGeoTiledMapScene13setCameraDataERK14QGeoCameraData(
    QGeoTiledMapScene *self,
    const QGeoCameraData *cameraData) {
  self->setCameraData(*cameraData);
}

//  void QGeoTiledMapScene::setVisibleArea(const QRectF &visibleArea)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGeoTiledMapScene14setVisibleAreaERK6QRectF(
    QGeoTiledMapScene *self,
    const QRectF *visibleArea) {
  self->setVisibleArea(*visibleArea);
}

//  QSGNode *QGeoTiledMapScene::updateSceneGraph(QSGNode *oldNode,
//      QQuickWindow *window)
extern "C" Q_DECL_EXPORT
QSGNode *ritual_ZN17QGeoTiledMapScene16updateSceneGraphEP7QSGNodeP12QQuickWindow(
    QGeoTiledMapScene *self,
    QSGNode *oldNode,
    QQuickWindow *window) {
  return self->updateSceneGraph(oldNode, window);
}

//  void QGeoTiledMapScene::clearTexturedTiles()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGeoTiledMapScene18clearTexturedTilesEv(
    QGeoTiledMapScene *self) {
  self->clearTexturedTiles();
}

//  void QGeoTiledMapScene::updateSceneParameters()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGeoTiledMapScene21updateSceneParametersEv(
    QGeoTiledMapScene *self) {
  self->updateSceneParameters();
}

//  a Python function taken by a CuteQGeoTiledMapScene, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QGeoTiledMapScene(
    QGeoTiledMapScene *self,
    const char *key,
    void *call) {
  return static_cast<CuteQGeoTiledMapScene *>(self)->take(key, call);
}
