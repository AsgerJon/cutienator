//  Written by dev_tooling.RitualGenerator from the records of
//  QtGraphs/q3dscene.h, Qt 6.12.0. Changes made here are lost.
#include <QtGraphs/qgraphsglobal.h>
#if !(!QT_CONFIG(graphs_3d_bars3d) && !QT_CONFIG(graphs_3d_scatter3d) && !QT_CONFIG(graphs_3d_surface3d))
#include <QtGraphs/QtGraphs>
#include <QtGraphs/q3dscene.h>
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

//  QString Q3DScene::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN8Q3DScene2trEPKcS1_i(const char *s, const char *c, int n) {
  return new QString(Q3DScene::tr(s, c, n));
}

//  Q3DScenePrivate *Q3DScene::d_func()
extern "C" Q_DECL_EXPORT
Q3DScenePrivate *ritual_ZN8Q3DScene6d_funcEv(Q3DScene *self) {
  return self->d_func();
}

//  const Q3DScenePrivate *Q3DScene::d_func() const
extern "C" Q_DECL_EXPORT
const Q3DScenePrivate *ritual_ZNK8Q3DScene6d_funcEv(const Q3DScene *self) {
  return self->d_func();
}

//  void Q3DScene::qt_qmlMarker_uncreatable()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Q3DScene24qt_qmlMarker_uncreatableEv(Q3DScene *self) {
  self->qt_qmlMarker_uncreatable();
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

//  void Q3DScene::setPrimarySubViewport(QRect primarySubViewport)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Q3DScene21setPrimarySubViewportE5QRect(
    Q3DScene *self,
    const QRect *primarySubViewport) {
  self->setPrimarySubViewport(*primarySubViewport);
}

//  bool Q3DScene::isPointInPrimarySubView(QPoint point)
extern "C" Q_DECL_EXPORT
bool ritual_ZN8Q3DScene23isPointInPrimarySubViewE6QPoint(
    Q3DScene *self,
    const QPoint *point) {
  return self->isPointInPrimarySubView(*point);
}

//  QRect Q3DScene::secondarySubViewport() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK8Q3DScene20secondarySubViewportEv(const Q3DScene *self) {
  return new QRect(self->secondarySubViewport());
}

//  void Q3DScene::setSecondarySubViewport(QRect secondarySubViewport)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Q3DScene23setSecondarySubViewportE5QRect(
    Q3DScene *self,
    const QRect *secondarySubViewport) {
  self->setSecondarySubViewport(*secondarySubViewport);
}

//  bool Q3DScene::isPointInSecondarySubView(QPoint point)
extern "C" Q_DECL_EXPORT
bool ritual_ZN8Q3DScene25isPointInSecondarySubViewE6QPoint(
    Q3DScene *self,
    const QPoint *point) {
  return self->isPointInSecondarySubView(*point);
}

//  void Q3DScene::setSelectionQueryPosition(QPoint point)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Q3DScene25setSelectionQueryPositionE6QPoint(
    Q3DScene *self,
    const QPoint *point) {
  self->setSelectionQueryPosition(*point);
}

//  QPoint Q3DScene::selectionQueryPosition() const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK8Q3DScene22selectionQueryPositionEv(const Q3DScene *self) {
  return new QPoint(self->selectionQueryPosition());
}

//  void Q3DScene::setGraphPositionQuery(QPoint point)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Q3DScene21setGraphPositionQueryE6QPoint(
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

//  qreal Q3DScene::devicePixelRatio() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK8Q3DScene16devicePixelRatioEv(const Q3DScene *self) {
  return self->devicePixelRatio();
}

//  void Q3DScene::setDevicePixelRatio(qreal pixelRatio)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Q3DScene19setDevicePixelRatioEd(
    Q3DScene *self,
    qreal pixelRatio) {
  self->setDevicePixelRatio(pixelRatio);
}

//  QPoint Q3DScene::invalidSelectionPoint() const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK8Q3DScene21invalidSelectionPointEv(const Q3DScene *self) {
  return new QPoint(self->invalidSelectionPoint());
}

//  a Python function taken by a CuteQ3DScene, for the function named by the
//      key
extern "C" Q_DECL_EXPORT
bool ritual_take_Q3DScene(Q3DScene *self, const char *key, void *call) {
  return static_cast<CuteQ3DScene *>(self)->take(key, call);
}

#endif  // !(!QT_CONFIG(graphs_3d_bars3d) && !QT_CONFIG(graphs_3d_scatter3d) && !QT_CONFIG(graphs_3d_surface3d))
