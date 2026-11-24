//  Written by dev_tooling.RitualGenerator from the records of
//  QtWaylandCompositor/qwaylandcompositor.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtWaylandCompositor/qwaylandcompositor.h>
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>
#include <QtWaylandCompositor/qwaylandclient.h>
#include <QtWaylandCompositor/qwaylandsurface.h>
#include <QtWaylandCompositor/qwaylandoutput.h>
#include <QtWaylandCompositor/qwaylandbufferref.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  Only a class built on QWaylandCompositor may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQWaylandCompositor : QWaylandCompositor {
  using QWaylandCompositor::retainedSelectionReceived;
  using QWaylandCompositor::createSeat;
  using QWaylandCompositor::createPointerDevice;
  using QWaylandCompositor::createKeyboardDevice;
  using QWaylandCompositor::createTouchDevice;
};

//  A QWaylandCompositor that Python can take functions over in. Every QWaylandCompositor
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQWaylandCompositorCall0)(const void *, int *);
typedef void (*CuteQWaylandCompositorCall1)(const void *, QWaylandSurfaceGrabber *, const QWaylandBufferRef *, int *);
typedef void (*CuteQWaylandCompositorCall2)(const void *, QMimeData *, int *);
typedef void * (*CuteQWaylandCompositorCall3)(const void *, int *);
typedef void * (*CuteQWaylandCompositorCall4)(const void *, QWaylandSeat *, int *);
typedef void * (*CuteQWaylandCompositorCall5)(const void *, QWaylandSeat *, int *);
typedef void * (*CuteQWaylandCompositorCall6)(const void *, QWaylandSeat *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQWaylandCompositorCall7)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQWaylandCompositorCall8)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWaylandCompositorCall9)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWaylandCompositorCall10)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWaylandCompositorCall11)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWaylandCompositorCall12)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWaylandCompositorCall13)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQWaylandCompositor : public QWaylandCompositor {
public:
  using QWaylandCompositor::QWaylandCompositor;
  void *taken[14] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN18QWaylandCompositor6createEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QWaylandCompositor11grabSurfaceEP22QWaylandSurfaceGrabberRK17QWaylandBufferRef")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QWaylandCompositor25retainedSelectionReceivedEP9QMimeData")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QWaylandCompositor10createSeatEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QWaylandCompositor19createPointerDeviceEP12QWaylandSeat")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QWaylandCompositor20createKeyboardDeviceEP12QWaylandSeat")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QWaylandCompositor17createTouchDeviceEP12QWaylandSeat")) {
      taken[6] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[13] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void QWaylandCompositor::create()
  void create() override {
    if (taken[0]) {
      int handled = 0;
      CuteQWaylandCompositorCall0 call = reinterpret_cast<CuteQWaylandCompositorCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QWaylandCompositor::create();
  }

  //  void QWaylandCompositor::grabSurface(QWaylandSurfaceGrabber *grabber,
  //      const QWaylandBufferRef &buffer)
  void grabSurface(
      QWaylandSurfaceGrabber *grabber,
      const QWaylandBufferRef &buffer) override {
    if (taken[1]) {
      int handled = 0;
      CuteQWaylandCompositorCall1 call = reinterpret_cast<CuteQWaylandCompositorCall1>(taken[1]);
      call(this, grabber, &buffer, &handled);
      if (handled) return;
    }
    QWaylandCompositor::grabSurface(grabber, buffer);
  }

  //  void QWaylandCompositor::retainedSelectionReceived(QMimeData
  //      *mimeData)
  void retainedSelectionReceived(QMimeData *mimeData) override {
    if (taken[2]) {
      int handled = 0;
      CuteQWaylandCompositorCall2 call = reinterpret_cast<CuteQWaylandCompositorCall2>(taken[2]);
      call(this, mimeData, &handled);
      if (handled) return;
    }
    QWaylandCompositor::retainedSelectionReceived(mimeData);
  }

  //  QWaylandSeat *QWaylandCompositor::createSeat()
  QWaylandSeat *createSeat() override {
    if (taken[3]) {
      int handled = 0;
      CuteQWaylandCompositorCall3 call = reinterpret_cast<CuteQWaylandCompositorCall3>(taken[3]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QWaylandSeat *>(given);
    }
    return QWaylandCompositor::createSeat();
  }

  //  QWaylandPointer *QWaylandCompositor::createPointerDevice(QWaylandSeat
  //      *seat)
  QWaylandPointer *createPointerDevice(QWaylandSeat *seat) override {
    if (taken[4]) {
      int handled = 0;
      CuteQWaylandCompositorCall4 call = reinterpret_cast<CuteQWaylandCompositorCall4>(taken[4]);
      void * given = call(this, seat, &handled);
      if (handled) return static_cast<QWaylandPointer *>(given);
    }
    return QWaylandCompositor::createPointerDevice(seat);
  }

  //  QWaylandKeyboard
  //      *QWaylandCompositor::createKeyboardDevice(QWaylandSeat *seat)
  QWaylandKeyboard *createKeyboardDevice(QWaylandSeat *seat) override {
    if (taken[5]) {
      int handled = 0;
      CuteQWaylandCompositorCall5 call = reinterpret_cast<CuteQWaylandCompositorCall5>(taken[5]);
      void * given = call(this, seat, &handled);
      if (handled) return static_cast<QWaylandKeyboard *>(given);
    }
    return QWaylandCompositor::createKeyboardDevice(seat);
  }

  //  QWaylandTouch *QWaylandCompositor::createTouchDevice(QWaylandSeat
  //      *seat)
  QWaylandTouch *createTouchDevice(QWaylandSeat *seat) override {
    if (taken[6]) {
      int handled = 0;
      CuteQWaylandCompositorCall6 call = reinterpret_cast<CuteQWaylandCompositorCall6>(taken[6]);
      void * given = call(this, seat, &handled);
      if (handled) return static_cast<QWaylandTouch *>(given);
    }
    return QWaylandCompositor::createTouchDevice(seat);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQWaylandCompositorCall7 call = reinterpret_cast<CuteQWaylandCompositorCall7>(taken[7]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQWaylandCompositorCall8 call = reinterpret_cast<CuteQWaylandCompositorCall8>(taken[8]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQWaylandCompositorCall9 call = reinterpret_cast<CuteQWaylandCompositorCall9>(taken[9]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQWaylandCompositorCall10 call = reinterpret_cast<CuteQWaylandCompositorCall10>(taken[10]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQWaylandCompositorCall11 call = reinterpret_cast<CuteQWaylandCompositorCall11>(taken[11]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[12]) {
      int handled = 0;
      CuteQWaylandCompositorCall12 call = reinterpret_cast<CuteQWaylandCompositorCall12>(taken[12]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[13]) {
      int handled = 0;
      CuteQWaylandCompositorCall13 call = reinterpret_cast<CuteQWaylandCompositorCall13>(taken[13]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QWaylandCompositor::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18QWaylandCompositor10metaObjectEv(
    const QWaylandCompositor *self) {
  return self->metaObject();
}

//  QString QWaylandCompositor::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18QWaylandCompositor2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QWaylandCompositor::tr(s, c, n));
}

//  void QWaylandCompositor::qt_qmlMarker_uncreatable()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWaylandCompositor24qt_qmlMarker_uncreatableEv(
    QWaylandCompositor *self) {
  self->qt_qmlMarker_uncreatable();
}

//  QWaylandCompositor::QWaylandCompositor(QObject *parent)
extern "C" Q_DECL_EXPORT
QWaylandCompositor *ritual_ZN18QWaylandCompositorC1EP7QObject(
    QObject *parent) {
  return new CuteQWaylandCompositor(parent);
}

//  QWaylandCompositor::~QWaylandCompositor()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWaylandCompositorD1Ev(QWaylandCompositor *self) {
  delete self;
}

//  void QWaylandCompositor::create()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWaylandCompositor6createEv(QWaylandCompositor *self) {
  self->create();
}

//  bool QWaylandCompositor::isCreated() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QWaylandCompositor9isCreatedEv(
    const QWaylandCompositor *self) {
  return self->isCreated();
}

//  void QWaylandCompositor::setSocketName(const QByteArray &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWaylandCompositor13setSocketNameERK10QByteArray(
    QWaylandCompositor *self,
    const QByteArray *name) {
  self->setSocketName(*name);
}

//  QByteArray QWaylandCompositor::socketName() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK18QWaylandCompositor10socketNameEv(
    const QWaylandCompositor *self) {
  return new QByteArray(self->socketName());
}

//  void QWaylandCompositor::addSocketDescriptor(int fd)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWaylandCompositor19addSocketDescriptorEi(
    QWaylandCompositor *self,
    int fd) {
  self->addSocketDescriptor(fd);
}

//  QList<QWaylandClient *> QWaylandCompositor::clients() const
extern "C" Q_DECL_EXPORT
QList<QWaylandClient *> *ritual_ZNK18QWaylandCompositor7clientsEv(
    const QWaylandCompositor *self) {
  return new QList<QWaylandClient *>(self->clients());
}

//  void QWaylandCompositor::destroyClientForSurface(QWaylandSurface
//      *surface)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWaylandCompositor23destroyClientForSurfaceEP15QWaylandSurface(
    QWaylandCompositor *self,
    QWaylandSurface *surface) {
  self->destroyClientForSurface(surface);
}

//  void QWaylandCompositor::destroyClient(QWaylandClient *client)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWaylandCompositor13destroyClientEP14QWaylandClient(
    QWaylandCompositor *self,
    QWaylandClient *client) {
  self->destroyClient(client);
}

//  QList<QWaylandSurface *> QWaylandCompositor::surfaces() const
extern "C" Q_DECL_EXPORT
QList<QWaylandSurface *> *ritual_ZNK18QWaylandCompositor8surfacesEv(
    const QWaylandCompositor *self) {
  return new QList<QWaylandSurface *>(self->surfaces());
}

//  QList<QWaylandSurface *>
//      QWaylandCompositor::surfacesForClient(QWaylandClient *client) const
extern "C" Q_DECL_EXPORT
QList<QWaylandSurface *> *ritual_ZNK18QWaylandCompositor17surfacesForClientEP14QWaylandClient(
    const QWaylandCompositor *self,
    QWaylandClient *client) {
  return new QList<QWaylandSurface *>(self->surfacesForClient(client));
}

//  QWaylandOutput *QWaylandCompositor::outputFor(QWindow *window) const
extern "C" Q_DECL_EXPORT
QWaylandOutput *ritual_ZNK18QWaylandCompositor9outputForEP7QWindow(
    const QWaylandCompositor *self,
    QWindow *window) {
  return self->outputFor(window);
}

//  QWaylandOutput *QWaylandCompositor::defaultOutput() const
extern "C" Q_DECL_EXPORT
QWaylandOutput *ritual_ZNK18QWaylandCompositor13defaultOutputEv(
    const QWaylandCompositor *self) {
  return self->defaultOutput();
}

//  void QWaylandCompositor::setDefaultOutput(QWaylandOutput *output)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWaylandCompositor16setDefaultOutputEP14QWaylandOutput(
    QWaylandCompositor *self,
    QWaylandOutput *output) {
  self->setDefaultOutput(output);
}

//  QList<QWaylandOutput *> QWaylandCompositor::outputs() const
extern "C" Q_DECL_EXPORT
QList<QWaylandOutput *> *ritual_ZNK18QWaylandCompositor7outputsEv(
    const QWaylandCompositor *self) {
  return new QList<QWaylandOutput *>(self->outputs());
}

//  uint QWaylandCompositor::currentTimeMsecs() const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK18QWaylandCompositor16currentTimeMsecsEv(
    const QWaylandCompositor *self) {
  return self->currentTimeMsecs();
}

//  void QWaylandCompositor::setRetainedSelectionEnabled(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWaylandCompositor27setRetainedSelectionEnabledEb(
    QWaylandCompositor *self,
    bool enabled) {
  self->setRetainedSelectionEnabled(enabled);
}

//  bool QWaylandCompositor::retainedSelectionEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QWaylandCompositor24retainedSelectionEnabledEv(
    const QWaylandCompositor *self) {
  return self->retainedSelectionEnabled();
}

//  void QWaylandCompositor::overrideSelection(const QMimeData *data)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWaylandCompositor17overrideSelectionEPK9QMimeData(
    QWaylandCompositor *self,
    const QMimeData *data) {
  self->overrideSelection(data);
}

//  QWaylandSeat *QWaylandCompositor::defaultSeat() const
extern "C" Q_DECL_EXPORT
QWaylandSeat *ritual_ZNK18QWaylandCompositor11defaultSeatEv(
    const QWaylandCompositor *self) {
  return self->defaultSeat();
}

//  QWaylandSeat *QWaylandCompositor::seatFor(QInputEvent *inputEvent)
extern "C" Q_DECL_EXPORT
QWaylandSeat *ritual_ZN18QWaylandCompositor7seatForEP11QInputEvent(
    QWaylandCompositor *self,
    QInputEvent *inputEvent) {
  return self->seatFor(inputEvent);
}

//  bool QWaylandCompositor::useHardwareIntegrationExtension() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QWaylandCompositor31useHardwareIntegrationExtensionEv(
    const QWaylandCompositor *self) {
  return self->useHardwareIntegrationExtension();
}

//  void QWaylandCompositor::setUseHardwareIntegrationExtension(bool use)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWaylandCompositor34setUseHardwareIntegrationExtensionEb(
    QWaylandCompositor *self,
    bool use) {
  self->setUseHardwareIntegrationExtension(use);
}

//  void QWaylandCompositor::grabSurface(QWaylandSurfaceGrabber *grabber,
//      const QWaylandBufferRef &buffer)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWaylandCompositor11grabSurfaceEP22QWaylandSurfaceGrabberRK17QWaylandBufferRef(
    QWaylandCompositor *self,
    QWaylandSurfaceGrabber *grabber,
    const QWaylandBufferRef *buffer) {
  self->grabSurface(grabber, *buffer);
}

//  void QWaylandCompositor::processWaylandEvents()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWaylandCompositor20processWaylandEventsEv(
    QWaylandCompositor *self) {
  self->processWaylandEvents();
}

//  void QWaylandCompositor::applicationStateChanged(Qt::ApplicationState
//      state)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWaylandCompositor23applicationStateChangedEN2Qt16ApplicationStateE(
    QWaylandCompositor *self,
    Qt::ApplicationState state) {
  self->applicationStateChanged(state);
}

//  void QWaylandCompositor::retainedSelectionReceived(QMimeData *mimeData)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWaylandCompositor25retainedSelectionReceivedEP9QMimeData(
    QWaylandCompositor *self,
    QMimeData *mimeData) {
  self->retainedSelectionReceived(mimeData);
}

//  QWaylandSeat *QWaylandCompositor::createSeat()
extern "C" Q_DECL_EXPORT
QWaylandSeat *ritual_ZN18QWaylandCompositor10createSeatEv(
    QWaylandCompositor *self) {
  return self->createSeat();
}

//  QWaylandPointer *QWaylandCompositor::createPointerDevice(QWaylandSeat
//      *seat)
extern "C" Q_DECL_EXPORT
QWaylandPointer *ritual_ZN18QWaylandCompositor19createPointerDeviceEP12QWaylandSeat(
    QWaylandCompositor *self,
    QWaylandSeat *seat) {
  return self->createPointerDevice(seat);
}

//  QWaylandKeyboard *QWaylandCompositor::createKeyboardDevice(QWaylandSeat
//      *seat)
extern "C" Q_DECL_EXPORT
QWaylandKeyboard *ritual_ZN18QWaylandCompositor20createKeyboardDeviceEP12QWaylandSeat(
    QWaylandCompositor *self,
    QWaylandSeat *seat) {
  return self->createKeyboardDevice(seat);
}

//  QWaylandTouch *QWaylandCompositor::createTouchDevice(QWaylandSeat *seat)
extern "C" Q_DECL_EXPORT
QWaylandTouch *ritual_ZN18QWaylandCompositor17createTouchDeviceEP12QWaylandSeat(
    QWaylandCompositor *self,
    QWaylandSeat *seat) {
  return self->createTouchDevice(seat);
}

//  a Python function taken by a CuteQWaylandCompositor, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QWaylandCompositor(
    QWaylandCompositor *self,
    const char *key,
    void *call) {
  return static_cast<CuteQWaylandCompositor *>(self)->take(key, call);
}

//  void QWaylandCompositor::create()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QWaylandCompositor6createEv(QWaylandCompositor *self) {
  self->QWaylandCompositor::create();
}

//  void QWaylandCompositor::grabSurface(QWaylandSurfaceGrabber *grabber,
//      const QWaylandBufferRef &buffer)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QWaylandCompositor11grabSurfaceEP22QWaylandSurfaceGrabberRK17QWaylandBufferRef(
    QWaylandCompositor *self,
    QWaylandSurfaceGrabber *grabber,
    const QWaylandBufferRef *buffer) {
  self->QWaylandCompositor::grabSurface(grabber, *buffer);
}

//  void QWaylandCompositor::retainedSelectionReceived(QMimeData *mimeData)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QWaylandCompositor25retainedSelectionReceivedEP9QMimeData(
    QWaylandCompositor *self,
    QMimeData *mimeData) {
  static_cast<OwnQWaylandCompositor *>(self)->OwnQWaylandCompositor::retainedSelectionReceived(
      mimeData);
}

//  QWaylandSeat *QWaylandCompositor::createSeat()
extern "C" Q_DECL_EXPORT
QWaylandSeat *ritual_own_ZN18QWaylandCompositor10createSeatEv(
    QWaylandCompositor *self) {
  return static_cast<OwnQWaylandCompositor *>(self)->OwnQWaylandCompositor::createSeat();
}

//  QWaylandPointer *QWaylandCompositor::createPointerDevice(QWaylandSeat
//      *seat)
extern "C" Q_DECL_EXPORT
QWaylandPointer *ritual_own_ZN18QWaylandCompositor19createPointerDeviceEP12QWaylandSeat(
    QWaylandCompositor *self,
    QWaylandSeat *seat) {
  return static_cast<OwnQWaylandCompositor *>(self)->OwnQWaylandCompositor::createPointerDevice(
      seat);
}

//  QWaylandKeyboard *QWaylandCompositor::createKeyboardDevice(QWaylandSeat
//      *seat)
extern "C" Q_DECL_EXPORT
QWaylandKeyboard *ritual_own_ZN18QWaylandCompositor20createKeyboardDeviceEP12QWaylandSeat(
    QWaylandCompositor *self,
    QWaylandSeat *seat) {
  return static_cast<OwnQWaylandCompositor *>(self)->OwnQWaylandCompositor::createKeyboardDevice(
      seat);
}

//  QWaylandTouch *QWaylandCompositor::createTouchDevice(QWaylandSeat *seat)
extern "C" Q_DECL_EXPORT
QWaylandTouch *ritual_own_ZN18QWaylandCompositor17createTouchDeviceEP12QWaylandSeat(
    QWaylandCompositor *self,
    QWaylandSeat *seat) {
  return static_cast<OwnQWaylandCompositor *>(self)->OwnQWaylandCompositor::createTouchDevice(
      seat);
}
