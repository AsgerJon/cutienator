//  Written by dev_tooling.RitualGenerator from the records of
//  QtDataVisualization/q3dscene.h, Qt 6.12.0. Changes made here are lost.
#include <QtDataVisualization/q3dscene.h>
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A Q3DScene that Python can take functions over in. Every Q3DScene
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQ3DSceneCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQ3DSceneCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQ3DSceneCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQ3DSceneCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQ3DSceneCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQ3DSceneCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQ3DSceneCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQ3DScene : public Q3DScene {
public:
  using Q3DScene::Q3DScene;
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
      CuteQ3DSceneCall0 call = reinterpret_cast<CuteQ3DSceneCall0>(taken[0]);
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
      CuteQ3DSceneCall1 call = reinterpret_cast<CuteQ3DSceneCall1>(taken[1]);
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
      CuteQ3DSceneCall2 call = reinterpret_cast<CuteQ3DSceneCall2>(taken[2]);
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
      CuteQ3DSceneCall3 call = reinterpret_cast<CuteQ3DSceneCall3>(taken[3]);
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
      CuteQ3DSceneCall4 call = reinterpret_cast<CuteQ3DSceneCall4>(taken[4]);
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
      CuteQ3DSceneCall5 call = reinterpret_cast<CuteQ3DSceneCall5>(taken[5]);
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
      CuteQ3DSceneCall6 call = reinterpret_cast<CuteQ3DSceneCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Q3DScene::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK8Q3DScene10metaObjectEv(const Q3DScene *self) {
  return self->metaObject();
}

//  void *Q3DScene::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN8Q3DScene11qt_metacastEPKc(Q3DScene *self, const char *a0) {
  return self->qt_metacast(a0);
}

//  int Q3DScene::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN8Q3DScene11qt_metacallEN11QMetaObject4CallEiPPv(
    Q3DScene *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Q3DScene::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN8Q3DScene2trEPKcS1_i(const char *s, const char *c, int n) {
  return new QString(Q3DScene::tr(s, c, n));
}

//  Q3DScene::Q3DScene(QObject *parent)
extern "C" Q_DECL_EXPORT
Q3DScene *ritual_ZN8Q3DSceneC1EP7QObject(QObject *parent) {
  return new CuteQ3DScene(parent);
}

//  Q3DScene::~Q3DScene()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Q3DSceneD1Ev(Q3DScene *self) {
  delete self;
}

//  QRect Q3DScene::viewport() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK8Q3DScene8viewportEv(const Q3DScene *self) {
  return new QRect(self->viewport());
}

//  QRect Q3DScene::primarySubViewport() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK8Q3DScene18primarySubViewportEv(const Q3DScene *self) {
  return new QRect(self->primarySubViewport());
}

//  void Q3DScene::setPrimarySubViewport(const QRect &primarySubViewport)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Q3DScene21setPrimarySubViewportERK5QRect(
    Q3DScene *self,
    const QRect *primarySubViewport) {
  self->setPrimarySubViewport(*primarySubViewport);
}

//  bool Q3DScene::isPointInPrimarySubView(const QPoint &point)
extern "C" Q_DECL_EXPORT
bool ritual_ZN8Q3DScene23isPointInPrimarySubViewERK6QPoint(
    Q3DScene *self,
    const QPoint *point) {
  return self->isPointInPrimarySubView(*point);
}

//  QRect Q3DScene::secondarySubViewport() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK8Q3DScene20secondarySubViewportEv(const Q3DScene *self) {
  return new QRect(self->secondarySubViewport());
}

//  void Q3DScene::setSecondarySubViewport(const QRect &secondarySubViewport)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Q3DScene23setSecondarySubViewportERK5QRect(
    Q3DScene *self,
    const QRect *secondarySubViewport) {
  self->setSecondarySubViewport(*secondarySubViewport);
}

//  bool Q3DScene::isPointInSecondarySubView(const QPoint &point)
extern "C" Q_DECL_EXPORT
bool ritual_ZN8Q3DScene25isPointInSecondarySubViewERK6QPoint(
    Q3DScene *self,
    const QPoint *point) {
  return self->isPointInSecondarySubView(*point);
}

//  void Q3DScene::setSelectionQueryPosition(const QPoint &point)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Q3DScene25setSelectionQueryPositionERK6QPoint(
    Q3DScene *self,
    const QPoint *point) {
  self->setSelectionQueryPosition(*point);
}

//  QPoint Q3DScene::selectionQueryPosition() const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK8Q3DScene22selectionQueryPositionEv(const Q3DScene *self) {
  return new QPoint(self->selectionQueryPosition());
}

//  QPoint Q3DScene::invalidSelectionPoint()
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZN8Q3DScene21invalidSelectionPointEv() {
  return new QPoint(Q3DScene::invalidSelectionPoint());
}

//  void Q3DScene::setGraphPositionQuery(const QPoint &point)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Q3DScene21setGraphPositionQueryERK6QPoint(
    Q3DScene *self,
    const QPoint *point) {
  self->setGraphPositionQuery(*point);
}

//  QPoint Q3DScene::graphPositionQuery() const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK8Q3DScene18graphPositionQueryEv(const Q3DScene *self) {
  return new QPoint(self->graphPositionQuery());
}

//  void Q3DScene::setSlicingActive(bool isSlicing)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Q3DScene16setSlicingActiveEb(Q3DScene *self, bool isSlicing) {
  self->setSlicingActive(isSlicing);
}

//  bool Q3DScene::isSlicingActive() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8Q3DScene15isSlicingActiveEv(const Q3DScene *self) {
  return self->isSlicingActive();
}

//  void Q3DScene::setSecondarySubviewOnTop(bool isSecondaryOnTop)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Q3DScene24setSecondarySubviewOnTopEb(
    Q3DScene *self,
    bool isSecondaryOnTop) {
  self->setSecondarySubviewOnTop(isSecondaryOnTop);
}

//  bool Q3DScene::isSecondarySubviewOnTop() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8Q3DScene23isSecondarySubviewOnTopEv(const Q3DScene *self) {
  return self->isSecondarySubviewOnTop();
}

//  Q3DCamera *Q3DScene::activeCamera() const
extern "C" Q_DECL_EXPORT
Q3DCamera *ritual_ZNK8Q3DScene12activeCameraEv(const Q3DScene *self) {
  return self->activeCamera();
}

//  void Q3DScene::setActiveCamera(Q3DCamera *camera)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Q3DScene15setActiveCameraEP9Q3DCamera(
    Q3DScene *self,
    Q3DCamera *camera) {
  self->setActiveCamera(camera);
}

//  Q3DLight *Q3DScene::activeLight() const
extern "C" Q_DECL_EXPORT
Q3DLight *ritual_ZNK8Q3DScene11activeLightEv(const Q3DScene *self) {
  return self->activeLight();
}

//  void Q3DScene::setActiveLight(Q3DLight *light)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Q3DScene14setActiveLightEP8Q3DLight(
    Q3DScene *self,
    Q3DLight *light) {
  self->setActiveLight(light);
}

//  float Q3DScene::devicePixelRatio() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK8Q3DScene16devicePixelRatioEv(const Q3DScene *self) {
  return self->devicePixelRatio();
}

//  void Q3DScene::setDevicePixelRatio(float pixelRatio)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Q3DScene19setDevicePixelRatioEf(
    Q3DScene *self,
    float pixelRatio) {
  self->setDevicePixelRatio(pixelRatio);
}

//  void Q3DScene::viewportChanged(const QRect &viewport)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Q3DScene15viewportChangedERK5QRect(
    Q3DScene *self,
    const QRect *viewport) {
  self->viewportChanged(*viewport);
}

//  void Q3DScene::primarySubViewportChanged(const QRect &subViewport)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Q3DScene25primarySubViewportChangedERK5QRect(
    Q3DScene *self,
    const QRect *subViewport) {
  self->primarySubViewportChanged(*subViewport);
}

//  void Q3DScene::secondarySubViewportChanged(const QRect &subViewport)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Q3DScene27secondarySubViewportChangedERK5QRect(
    Q3DScene *self,
    const QRect *subViewport) {
  self->secondarySubViewportChanged(*subViewport);
}

//  void Q3DScene::secondarySubviewOnTopChanged(bool isSecondaryOnTop)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Q3DScene28secondarySubviewOnTopChangedEb(
    Q3DScene *self,
    bool isSecondaryOnTop) {
  self->secondarySubviewOnTopChanged(isSecondaryOnTop);
}

//  void Q3DScene::slicingActiveChanged(bool isSlicingActive)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Q3DScene20slicingActiveChangedEb(
    Q3DScene *self,
    bool isSlicingActive) {
  self->slicingActiveChanged(isSlicingActive);
}

//  void Q3DScene::activeCameraChanged(Q3DCamera *camera)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Q3DScene19activeCameraChangedEP9Q3DCamera(
    Q3DScene *self,
    Q3DCamera *camera) {
  self->activeCameraChanged(camera);
}

//  void Q3DScene::activeLightChanged(Q3DLight *light)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Q3DScene18activeLightChangedEP8Q3DLight(
    Q3DScene *self,
    Q3DLight *light) {
  self->activeLightChanged(light);
}

//  void Q3DScene::devicePixelRatioChanged(float pixelRatio)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Q3DScene23devicePixelRatioChangedEf(
    Q3DScene *self,
    float pixelRatio) {
  self->devicePixelRatioChanged(pixelRatio);
}

//  void Q3DScene::selectionQueryPositionChanged(const QPoint &position)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Q3DScene29selectionQueryPositionChangedERK6QPoint(
    Q3DScene *self,
    const QPoint *position) {
  self->selectionQueryPositionChanged(*position);
}

//  void Q3DScene::graphPositionQueryChanged(const QPoint &position)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Q3DScene25graphPositionQueryChangedERK6QPoint(
    Q3DScene *self,
    const QPoint *position) {
  self->graphPositionQueryChanged(*position);
}

//  a Python function taken by a CuteQ3DScene, for the function named by the
//      key
extern "C" Q_DECL_EXPORT
bool ritual_take_Q3DScene(Q3DScene *self, const char *key, void *call) {
  return static_cast<CuteQ3DScene *>(self)->take(key, call);
}
