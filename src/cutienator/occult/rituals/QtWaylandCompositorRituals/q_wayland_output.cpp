//  Written by dev_tooling.RitualGenerator from the records of
//  QtWaylandCompositor/qwaylandoutput.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtWaylandCompositor/qwaylandoutput.h>
#include <QtCore/qstring.h>
#include <QtCore/qpoint.h>
#include <QtWaylandCompositor/qwaylandoutputmode.h>
#include <QtCore/qrect.h>
#include <QtCore/qsize.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  Only a class built on QWaylandOutput may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQWaylandOutput : QWaylandOutput {
  using QWaylandOutput::event;
  using QWaylandOutput::initialize;
};

//  A QWaylandOutput that Python can take functions over in. Every QWaylandOutput
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQWaylandOutputCall0)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQWaylandOutputCall1)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQWaylandOutputCall2)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQWaylandOutputCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWaylandOutputCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWaylandOutputCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWaylandOutputCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWaylandOutputCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWaylandOutputCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQWaylandOutput : public QWaylandOutput {
public:
  using QWaylandOutput::QWaylandOutput;
  void *taken[9] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN14QWaylandOutput6updateEv")) {
      taken[0] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN14QWaylandOutput10initializeEv")) {
      taken[2] = call;
      return true;
    }
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

  //  void QWaylandOutput::update()
  void update() override {
    if (taken[0]) {
      int handled = 0;
      CuteQWaylandOutputCall0 call = reinterpret_cast<CuteQWaylandOutputCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QWaylandOutput::update();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QWaylandOutput::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQWaylandOutputCall1 call = reinterpret_cast<CuteQWaylandOutputCall1>(taken[1]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QWaylandOutput::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  void QWaylandOutput::initialize()
  void initialize() override {
    if (taken[2]) {
      int handled = 0;
      CuteQWaylandOutputCall2 call = reinterpret_cast<CuteQWaylandOutputCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QWaylandOutput::initialize();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQWaylandOutputCall3 call = reinterpret_cast<CuteQWaylandOutputCall3>(taken[3]);
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
      CuteQWaylandOutputCall4 call = reinterpret_cast<CuteQWaylandOutputCall4>(taken[4]);
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
      CuteQWaylandOutputCall5 call = reinterpret_cast<CuteQWaylandOutputCall5>(taken[5]);
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
      CuteQWaylandOutputCall6 call = reinterpret_cast<CuteQWaylandOutputCall6>(taken[6]);
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
      CuteQWaylandOutputCall7 call = reinterpret_cast<CuteQWaylandOutputCall7>(taken[7]);
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
      CuteQWaylandOutputCall8 call = reinterpret_cast<CuteQWaylandOutputCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QWaylandOutput::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK14QWaylandOutput10metaObjectEv(
    const QWaylandOutput *self) {
  return self->metaObject();
}

//  void *QWaylandOutput::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN14QWaylandOutput11qt_metacastEPKc(
    QWaylandOutput *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QWaylandOutput::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN14QWaylandOutput11qt_metacallEN11QMetaObject4CallEiPPv(
    QWaylandOutput *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QWaylandOutput::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN14QWaylandOutput2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QWaylandOutput::tr(s, c, n));
}

//  QWaylandOutputPrivate *QWaylandOutput::d_func()
extern "C" Q_DECL_EXPORT
QWaylandOutputPrivate *ritual_ZN14QWaylandOutput6d_funcEv(
    QWaylandOutput *self) {
  return self->d_func();
}

//  const QWaylandOutputPrivate *QWaylandOutput::d_func() const
extern "C" Q_DECL_EXPORT
const QWaylandOutputPrivate *ritual_ZNK14QWaylandOutput6d_funcEv(
    const QWaylandOutput *self) {
  return self->d_func();
}

//  void QWaylandOutput::qt_qmlMarker_uncreatable()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWaylandOutput24qt_qmlMarker_uncreatableEv(
    QWaylandOutput *self) {
  self->qt_qmlMarker_uncreatable();
}

//  QWaylandOutput::QWaylandOutput()
extern "C" Q_DECL_EXPORT
QWaylandOutput *ritual_ZN14QWaylandOutputC1Ev() {
  return new CuteQWaylandOutput();
}

//  QWaylandOutput::QWaylandOutput(QWaylandCompositor *compositor, QWindow
//      *window)
extern "C" Q_DECL_EXPORT
QWaylandOutput *ritual_ZN14QWaylandOutputC1EP18QWaylandCompositorP7QWindow(
    QWaylandCompositor *compositor,
    QWindow *window) {
  return new CuteQWaylandOutput(compositor, window);
}

//  QWaylandOutput::~QWaylandOutput()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWaylandOutputD1Ev(QWaylandOutput *self) {
  delete self;
}

//  QWaylandOutput *QWaylandOutput::fromResource(wl_resource *resource)
extern "C" Q_DECL_EXPORT
QWaylandOutput *ritual_ZN14QWaylandOutput12fromResourceEP11wl_resource(
    wl_resource *resource) {
  return QWaylandOutput::fromResource(resource);
}

//  struct ::wl_resource *QWaylandOutput::resourceForClient(QWaylandClient
//      *client) const
extern "C" Q_DECL_EXPORT
struct ::wl_resource *ritual_ZNK14QWaylandOutput17resourceForClientEP14QWaylandClient(
    const QWaylandOutput *self,
    QWaylandClient *client) {
  return self->resourceForClient(client);
}

//  QWaylandCompositor *QWaylandOutput::compositor() const
extern "C" Q_DECL_EXPORT
QWaylandCompositor *ritual_ZNK14QWaylandOutput10compositorEv(
    const QWaylandOutput *self) {
  return self->compositor();
}

//  void QWaylandOutput::setCompositor(QWaylandCompositor *compositor)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWaylandOutput13setCompositorEP18QWaylandCompositor(
    QWaylandOutput *self,
    QWaylandCompositor *compositor) {
  self->setCompositor(compositor);
}

//  QWindow *QWaylandOutput::window() const
extern "C" Q_DECL_EXPORT
QWindow *ritual_ZNK14QWaylandOutput6windowEv(const QWaylandOutput *self) {
  return self->window();
}

//  void QWaylandOutput::setWindow(QWindow *window)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWaylandOutput9setWindowEP7QWindow(
    QWaylandOutput *self,
    QWindow *window) {
  self->setWindow(window);
}

//  QString QWaylandOutput::manufacturer() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QWaylandOutput12manufacturerEv(
    const QWaylandOutput *self) {
  return new QString(self->manufacturer());
}

//  void QWaylandOutput::setManufacturer(const QString &manufacturer)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWaylandOutput15setManufacturerERK7QString(
    QWaylandOutput *self,
    const QString *manufacturer) {
  self->setManufacturer(*manufacturer);
}

//  QString QWaylandOutput::model() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QWaylandOutput5modelEv(const QWaylandOutput *self) {
  return new QString(self->model());
}

//  void QWaylandOutput::setModel(const QString &model)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWaylandOutput8setModelERK7QString(
    QWaylandOutput *self,
    const QString *model) {
  self->setModel(*model);
}

//  QPoint QWaylandOutput::position() const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK14QWaylandOutput8positionEv(const QWaylandOutput *self) {
  return new QPoint(self->position());
}

//  void QWaylandOutput::setPosition(const QPoint &pt)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWaylandOutput11setPositionERK6QPoint(
    QWaylandOutput *self,
    const QPoint *pt) {
  self->setPosition(*pt);
}

//  QList<QWaylandOutputMode> QWaylandOutput::modes() const
extern "C" Q_DECL_EXPORT
QList<QWaylandOutputMode> *ritual_ZNK14QWaylandOutput5modesEv(
    const QWaylandOutput *self) {
  return new QList<QWaylandOutputMode>(self->modes());
}

//  void QWaylandOutput::addMode(const QWaylandOutputMode &mode, bool
//      preferred)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWaylandOutput7addModeERK18QWaylandOutputModeb(
    QWaylandOutput *self,
    const QWaylandOutputMode *mode,
    bool preferred) {
  self->addMode(*mode, preferred);
}

//  QWaylandOutputMode QWaylandOutput::currentMode() const
extern "C" Q_DECL_EXPORT
QWaylandOutputMode *ritual_ZNK14QWaylandOutput11currentModeEv(
    const QWaylandOutput *self) {
  return new QWaylandOutputMode(self->currentMode());
}

//  void QWaylandOutput::setCurrentMode(const QWaylandOutputMode &mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWaylandOutput14setCurrentModeERK18QWaylandOutputMode(
    QWaylandOutput *self,
    const QWaylandOutputMode *mode) {
  self->setCurrentMode(*mode);
}

//  QRect QWaylandOutput::geometry() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK14QWaylandOutput8geometryEv(const QWaylandOutput *self) {
  return new QRect(self->geometry());
}

//  QRect QWaylandOutput::availableGeometry() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK14QWaylandOutput17availableGeometryEv(
    const QWaylandOutput *self) {
  return new QRect(self->availableGeometry());
}

//  void QWaylandOutput::setAvailableGeometry(const QRect &availableGeometry)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWaylandOutput20setAvailableGeometryERK5QRect(
    QWaylandOutput *self,
    const QRect *availableGeometry) {
  self->setAvailableGeometry(*availableGeometry);
}

//  QSize QWaylandOutput::physicalSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK14QWaylandOutput12physicalSizeEv(
    const QWaylandOutput *self) {
  return new QSize(self->physicalSize());
}

//  void QWaylandOutput::setPhysicalSize(const QSize &size)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWaylandOutput15setPhysicalSizeERK5QSize(
    QWaylandOutput *self,
    const QSize *size) {
  self->setPhysicalSize(*size);
}

//  Subpixel QWaylandOutput::subpixel() const
extern "C" Q_DECL_EXPORT
QWaylandOutput::Subpixel ritual_ZNK14QWaylandOutput8subpixelEv(
    const QWaylandOutput *self) {
  return self->subpixel();
}

//  void QWaylandOutput::setSubpixel(const Subpixel &subpixel)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWaylandOutput11setSubpixelERKNS_8SubpixelE(
    QWaylandOutput *self,
    const QWaylandOutput::Subpixel *subpixel) {
  self->setSubpixel(*subpixel);
}

//  Transform QWaylandOutput::transform() const
extern "C" Q_DECL_EXPORT
QWaylandOutput::Transform ritual_ZNK14QWaylandOutput9transformEv(
    const QWaylandOutput *self) {
  return self->transform();
}

//  void QWaylandOutput::setTransform(const Transform &transform)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWaylandOutput12setTransformERKNS_9TransformE(
    QWaylandOutput *self,
    const QWaylandOutput::Transform *transform) {
  self->setTransform(*transform);
}

//  int QWaylandOutput::scaleFactor() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QWaylandOutput11scaleFactorEv(const QWaylandOutput *self) {
  return self->scaleFactor();
}

//  void QWaylandOutput::setScaleFactor(int scale)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWaylandOutput14setScaleFactorEi(
    QWaylandOutput *self,
    int scale) {
  self->setScaleFactor(scale);
}

//  bool QWaylandOutput::sizeFollowsWindow() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QWaylandOutput17sizeFollowsWindowEv(
    const QWaylandOutput *self) {
  return self->sizeFollowsWindow();
}

//  void QWaylandOutput::setSizeFollowsWindow(bool follow)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWaylandOutput20setSizeFollowsWindowEb(
    QWaylandOutput *self,
    bool follow) {
  self->setSizeFollowsWindow(follow);
}

//  void QWaylandOutput::frameStarted()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWaylandOutput12frameStartedEv(QWaylandOutput *self) {
  self->frameStarted();
}

//  void QWaylandOutput::sendFrameCallbacks()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWaylandOutput18sendFrameCallbacksEv(QWaylandOutput *self) {
  self->sendFrameCallbacks();
}

//  void QWaylandOutput::surfaceEnter(QWaylandSurface *surface)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWaylandOutput12surfaceEnterEP15QWaylandSurface(
    QWaylandOutput *self,
    QWaylandSurface *surface) {
  self->surfaceEnter(surface);
}

//  void QWaylandOutput::surfaceLeave(QWaylandSurface *surface)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWaylandOutput12surfaceLeaveEP15QWaylandSurface(
    QWaylandOutput *self,
    QWaylandSurface *surface) {
  self->surfaceLeave(surface);
}

//  void QWaylandOutput::update()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWaylandOutput6updateEv(QWaylandOutput *self) {
  self->update();
}

//  void QWaylandOutput::compositorChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWaylandOutput17compositorChangedEv(QWaylandOutput *self) {
  self->compositorChanged();
}

//  void QWaylandOutput::windowChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWaylandOutput13windowChangedEv(QWaylandOutput *self) {
  self->windowChanged();
}

//  void QWaylandOutput::positionChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWaylandOutput15positionChangedEv(QWaylandOutput *self) {
  self->positionChanged();
}

//  void QWaylandOutput::geometryChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWaylandOutput15geometryChangedEv(QWaylandOutput *self) {
  self->geometryChanged();
}

//  void QWaylandOutput::modeAdded()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWaylandOutput9modeAddedEv(QWaylandOutput *self) {
  self->modeAdded();
}

//  void QWaylandOutput::currentModeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWaylandOutput18currentModeChangedEv(QWaylandOutput *self) {
  self->currentModeChanged();
}

//  void QWaylandOutput::availableGeometryChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWaylandOutput24availableGeometryChangedEv(
    QWaylandOutput *self) {
  self->availableGeometryChanged();
}

//  void QWaylandOutput::physicalSizeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWaylandOutput19physicalSizeChangedEv(QWaylandOutput *self) {
  self->physicalSizeChanged();
}

//  void QWaylandOutput::scaleFactorChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWaylandOutput18scaleFactorChangedEv(QWaylandOutput *self) {
  self->scaleFactorChanged();
}

//  void QWaylandOutput::subpixelChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWaylandOutput15subpixelChangedEv(QWaylandOutput *self) {
  self->subpixelChanged();
}

//  void QWaylandOutput::transformChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWaylandOutput16transformChangedEv(QWaylandOutput *self) {
  self->transformChanged();
}

//  void QWaylandOutput::sizeFollowsWindowChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWaylandOutput24sizeFollowsWindowChangedEv(
    QWaylandOutput *self) {
  self->sizeFollowsWindowChanged();
}

//  void QWaylandOutput::physicalSizeFollowsSizeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWaylandOutput30physicalSizeFollowsSizeChangedEv(
    QWaylandOutput *self) {
  self->physicalSizeFollowsSizeChanged();
}

//  void QWaylandOutput::manufacturerChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWaylandOutput19manufacturerChangedEv(QWaylandOutput *self) {
  self->manufacturerChanged();
}

//  void QWaylandOutput::modelChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWaylandOutput12modelChangedEv(QWaylandOutput *self) {
  self->modelChanged();
}

//  void QWaylandOutput::windowDestroyed()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWaylandOutput15windowDestroyedEv(QWaylandOutput *self) {
  self->windowDestroyed();
}

//  bool QWaylandOutput::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QWaylandOutput5eventEP6QEvent(
    QWaylandOutput *self,
    QEvent *event) {
  return self->event(event);
}

//  void QWaylandOutput::initialize()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWaylandOutput10initializeEv(QWaylandOutput *self) {
  self->initialize();
}

//  a Python function taken by a CuteQWaylandOutput, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QWaylandOutput(
    QWaylandOutput *self,
    const char *key,
    void *call) {
  return static_cast<CuteQWaylandOutput *>(self)->take(key, call);
}

//  void QWaylandOutput::update()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QWaylandOutput6updateEv(QWaylandOutput *self) {
  self->QWaylandOutput::update();
}

//  bool QWaylandOutput::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN14QWaylandOutput5eventEP6QEvent(
    QWaylandOutput *self,
    QEvent *event) {
  return static_cast<OwnQWaylandOutput *>(self)->OwnQWaylandOutput::event(
      event);
}

//  void QWaylandOutput::initialize()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QWaylandOutput10initializeEv(QWaylandOutput *self) {
  static_cast<OwnQWaylandOutput *>(self)->OwnQWaylandOutput::initialize();
}

//  QList<QWaylandOutput *>::QList()
extern "C" Q_DECL_EXPORT
QList<QWaylandOutput *> *ritual_list_make_QWaylandOutput_ptr() {
  return new QList<QWaylandOutput *>();
}

//  void QList<QWaylandOutput *>::append(const QWaylandOutput * &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QWaylandOutput_ptr(
    QList<QWaylandOutput *> *self,
    QWaylandOutput *element) {
  self->append(element);
}

//  qsizetype QList<QWaylandOutput *>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QWaylandOutput_ptr(
    const QList<QWaylandOutput *> *self) {
  return self->size();
}

//  const QWaylandOutput * &QList<QWaylandOutput *>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QWaylandOutput *ritual_list_at_QWaylandOutput_ptr(
    const QList<QWaylandOutput *> *self,
    long long index) {
  return self->at(index);
}

//  QList<QWaylandOutput *>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QWaylandOutput_ptr(QList<QWaylandOutput *> *self) {
  delete self;
}
