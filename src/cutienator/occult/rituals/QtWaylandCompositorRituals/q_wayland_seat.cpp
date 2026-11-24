//  Written by dev_tooling.RitualGenerator from the records of
//  QtWaylandCompositor/qwaylandseat.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtGui/qtguiglobal.h>
#include <QtWaylandCompositor/qwaylandseat.h>
#include <QtCore/qstring.h>
#include <QtCore/qpoint.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QWaylandSeat that Python can take functions over in. Every QWaylandSeat
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQWaylandSeatCall0)(const void *, int *);
typedef bool (*CuteQWaylandSeatCall1)(const void *, QInputEvent *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQWaylandSeatCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQWaylandSeatCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWaylandSeatCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWaylandSeatCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWaylandSeatCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWaylandSeatCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWaylandSeatCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQWaylandSeat : public QWaylandSeat {
public:
  using QWaylandSeat::QWaylandSeat;
  void *taken[9] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN12QWaylandSeat10initializeEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QWaylandSeat7isOwnerEP11QInputEvent")) {
      taken[1] = call;
      return true;
    }
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

  //  void QWaylandSeat::initialize()
  void initialize() override {
    if (taken[0]) {
      int handled = 0;
      CuteQWaylandSeatCall0 call = reinterpret_cast<CuteQWaylandSeatCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QWaylandSeat::initialize();
  }

  //  bool QWaylandSeat::isOwner(QInputEvent *inputEvent) const
  bool isOwner(QInputEvent *inputEvent) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQWaylandSeatCall1 call = reinterpret_cast<CuteQWaylandSeatCall1>(taken[1]);
      bool given = call(this, inputEvent, &handled);
      if (handled) return given;
    }
    return QWaylandSeat::isOwner(inputEvent);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQWaylandSeatCall2 call = reinterpret_cast<CuteQWaylandSeatCall2>(taken[2]);
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
      CuteQWaylandSeatCall3 call = reinterpret_cast<CuteQWaylandSeatCall3>(taken[3]);
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
      CuteQWaylandSeatCall4 call = reinterpret_cast<CuteQWaylandSeatCall4>(taken[4]);
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
      CuteQWaylandSeatCall5 call = reinterpret_cast<CuteQWaylandSeatCall5>(taken[5]);
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
      CuteQWaylandSeatCall6 call = reinterpret_cast<CuteQWaylandSeatCall6>(taken[6]);
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
      CuteQWaylandSeatCall7 call = reinterpret_cast<CuteQWaylandSeatCall7>(taken[7]);
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
      CuteQWaylandSeatCall8 call = reinterpret_cast<CuteQWaylandSeatCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QWaylandSeat::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK12QWaylandSeat10metaObjectEv(
    const QWaylandSeat *self) {
  return self->metaObject();
}

//  QString QWaylandSeat::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN12QWaylandSeat2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QWaylandSeat::tr(s, c, n));
}

//  void QWaylandSeat::qt_qmlMarker_uncreatable()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QWaylandSeat24qt_qmlMarker_uncreatableEv(
    QWaylandSeat *self) {
  self->qt_qmlMarker_uncreatable();
}

//  QWaylandSeat::QWaylandSeat(QWaylandCompositor *compositor,
//      CapabilityFlags capabilityFlags)
extern "C" Q_DECL_EXPORT
QWaylandSeat *ritual_ZN12QWaylandSeatC1EP18QWaylandCompositor6QFlagsINS_14CapabilityFlagEE(
    QWaylandCompositor *compositor,
    int capabilityFlags) {
  return new CuteQWaylandSeat(
      compositor,
      QFlags<QWaylandSeat::CapabilityFlag>::fromInt(capabilityFlags));
}

//  QWaylandSeat::~QWaylandSeat()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QWaylandSeatD1Ev(QWaylandSeat *self) {
  delete self;
}

//  void QWaylandSeat::initialize()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QWaylandSeat10initializeEv(QWaylandSeat *self) {
  self->initialize();
}

//  bool QWaylandSeat::isInitialized() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QWaylandSeat13isInitializedEv(const QWaylandSeat *self) {
  return self->isInitialized();
}

//  void QWaylandSeat::sendMousePressEvent(Qt::MouseButton button)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QWaylandSeat19sendMousePressEventEN2Qt11MouseButtonE(
    QWaylandSeat *self,
    Qt::MouseButton button) {
  self->sendMousePressEvent(button);
}

//  void QWaylandSeat::sendMouseReleaseEvent(Qt::MouseButton button)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QWaylandSeat21sendMouseReleaseEventEN2Qt11MouseButtonE(
    QWaylandSeat *self,
    Qt::MouseButton button) {
  self->sendMouseReleaseEvent(button);
}

//  void QWaylandSeat::sendMouseMoveEvent(QWaylandView *surface, const
//      QPointF &localPos, const QPointF &outputSpacePos)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QWaylandSeat18sendMouseMoveEventEP12QWaylandViewRK7QPointFS4_(
    QWaylandSeat *self,
    QWaylandView *surface,
    const QPointF *localPos,
    const QPointF *outputSpacePos) {
  self->sendMouseMoveEvent(surface, *localPos, *outputSpacePos);
}

//  void QWaylandSeat::sendMouseWheelEvent(Qt::Orientation orientation, int
//      delta)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QWaylandSeat19sendMouseWheelEventEN2Qt11OrientationEi(
    QWaylandSeat *self,
    Qt::Orientation orientation,
    int delta) {
  self->sendMouseWheelEvent(orientation, delta);
}

//  void QWaylandSeat::sendKeyPressEvent(uint code)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QWaylandSeat17sendKeyPressEventEj(
    QWaylandSeat *self,
    uint code) {
  self->sendKeyPressEvent(code);
}

//  void QWaylandSeat::sendKeyReleaseEvent(uint code)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QWaylandSeat19sendKeyReleaseEventEj(
    QWaylandSeat *self,
    uint code) {
  self->sendKeyReleaseEvent(code);
}

//  void QWaylandSeat::sendFullKeyEvent(QKeyEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QWaylandSeat16sendFullKeyEventEP9QKeyEvent(
    QWaylandSeat *self,
    QKeyEvent *event) {
  self->sendFullKeyEvent(event);
}

//  void QWaylandSeat::sendKeyEvent(int qtKey, bool pressed)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QWaylandSeat12sendKeyEventEib(
    QWaylandSeat *self,
    int qtKey,
    bool pressed) {
  self->sendKeyEvent(qtKey, pressed);
}

//  void QWaylandSeat::sendUnicodeKeyPressEvent(uint unicode)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QWaylandSeat24sendUnicodeKeyPressEventEj(
    QWaylandSeat *self,
    uint unicode) {
  self->sendUnicodeKeyPressEvent(unicode);
}

//  void QWaylandSeat::sendUnicodeKeyReleaseEvent(uint unicode)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QWaylandSeat26sendUnicodeKeyReleaseEventEj(
    QWaylandSeat *self,
    uint unicode) {
  self->sendUnicodeKeyReleaseEvent(unicode);
}

//  uint QWaylandSeat::sendTouchPointEvent(QWaylandSurface *surface, int id,
//      const QPointF &point, Qt::TouchPointState state)
extern "C" Q_DECL_EXPORT
uint ritual_ZN12QWaylandSeat19sendTouchPointEventEP15QWaylandSurfaceiRK7QPointFN2Qt15TouchPointStateE(
    QWaylandSeat *self,
    QWaylandSurface *surface,
    int id,
    const QPointF *point,
    Qt::TouchPointState state) {
  return self->sendTouchPointEvent(surface, id, *point, state);
}

//  uint QWaylandSeat::sendTouchPointPressed(QWaylandSurface *surface, int
//      id, const QPointF &position)
extern "C" Q_DECL_EXPORT
uint ritual_ZN12QWaylandSeat21sendTouchPointPressedEP15QWaylandSurfaceiRK7QPointF(
    QWaylandSeat *self,
    QWaylandSurface *surface,
    int id,
    const QPointF *position) {
  return self->sendTouchPointPressed(surface, id, *position);
}

//  uint QWaylandSeat::sendTouchPointReleased(QWaylandSurface *surface, int
//      id, const QPointF &position)
extern "C" Q_DECL_EXPORT
uint ritual_ZN12QWaylandSeat22sendTouchPointReleasedEP15QWaylandSurfaceiRK7QPointF(
    QWaylandSeat *self,
    QWaylandSurface *surface,
    int id,
    const QPointF *position) {
  return self->sendTouchPointReleased(surface, id, *position);
}

//  uint QWaylandSeat::sendTouchPointMoved(QWaylandSurface *surface, int id,
//      const QPointF &position)
extern "C" Q_DECL_EXPORT
uint ritual_ZN12QWaylandSeat19sendTouchPointMovedEP15QWaylandSurfaceiRK7QPointF(
    QWaylandSeat *self,
    QWaylandSurface *surface,
    int id,
    const QPointF *position) {
  return self->sendTouchPointMoved(surface, id, *position);
}

//  void QWaylandSeat::sendTouchFrameEvent(QWaylandClient *client)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QWaylandSeat19sendTouchFrameEventEP14QWaylandClient(
    QWaylandSeat *self,
    QWaylandClient *client) {
  self->sendTouchFrameEvent(client);
}

//  void QWaylandSeat::sendTouchCancelEvent(QWaylandClient *client)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QWaylandSeat20sendTouchCancelEventEP14QWaylandClient(
    QWaylandSeat *self,
    QWaylandClient *client) {
  self->sendTouchCancelEvent(client);
}

//  void QWaylandSeat::sendFullTouchEvent(QWaylandSurface *surface,
//      QTouchEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QWaylandSeat18sendFullTouchEventEP15QWaylandSurfaceP11QTouchEvent(
    QWaylandSeat *self,
    QWaylandSurface *surface,
    QTouchEvent *event) {
  self->sendFullTouchEvent(surface, event);
}

//  QWaylandPointer *QWaylandSeat::pointer() const
extern "C" Q_DECL_EXPORT
QWaylandPointer *ritual_ZNK12QWaylandSeat7pointerEv(
    const QWaylandSeat *self) {
  return self->pointer();
}

//  QWaylandView *QWaylandSeat::mouseFocus() const
extern "C" Q_DECL_EXPORT
QWaylandView *ritual_ZNK12QWaylandSeat10mouseFocusEv(
    const QWaylandSeat *self) {
  return self->mouseFocus();
}

//  void QWaylandSeat::setMouseFocus(QWaylandView *view)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QWaylandSeat13setMouseFocusEP12QWaylandView(
    QWaylandSeat *self,
    QWaylandView *view) {
  self->setMouseFocus(view);
}

//  QWaylandKeyboard *QWaylandSeat::keyboard() const
extern "C" Q_DECL_EXPORT
QWaylandKeyboard *ritual_ZNK12QWaylandSeat8keyboardEv(
    const QWaylandSeat *self) {
  return self->keyboard();
}

//  QWaylandSurface *QWaylandSeat::keyboardFocus() const
extern "C" Q_DECL_EXPORT
QWaylandSurface *ritual_ZNK12QWaylandSeat13keyboardFocusEv(
    const QWaylandSeat *self) {
  return self->keyboardFocus();
}

//  bool QWaylandSeat::setKeyboardFocus(QWaylandSurface *surface)
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QWaylandSeat16setKeyboardFocusEP15QWaylandSurface(
    QWaylandSeat *self,
    QWaylandSurface *surface) {
  return self->setKeyboardFocus(surface);
}

//  QWaylandKeymap *QWaylandSeat::keymap()
extern "C" Q_DECL_EXPORT
QWaylandKeymap *ritual_ZN12QWaylandSeat6keymapEv(QWaylandSeat *self) {
  return self->keymap();
}

//  QWaylandTouch *QWaylandSeat::touch() const
extern "C" Q_DECL_EXPORT
QWaylandTouch *ritual_ZNK12QWaylandSeat5touchEv(const QWaylandSeat *self) {
  return self->touch();
}

//  QWaylandCompositor *QWaylandSeat::compositor() const
extern "C" Q_DECL_EXPORT
QWaylandCompositor *ritual_ZNK12QWaylandSeat10compositorEv(
    const QWaylandSeat *self) {
  return self->compositor();
}

#if QT_CONFIG(draganddrop)
//  QWaylandDrag *QWaylandSeat::drag() const
extern "C" Q_DECL_EXPORT
QWaylandDrag *ritual_ZNK12QWaylandSeat4dragEv(const QWaylandSeat *self) {
  return self->drag();
}
#endif  // QT_CONFIG(draganddrop)

//  QWaylandSeat::CapabilityFlags QWaylandSeat::capabilities() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QWaylandSeat12capabilitiesEv(const QWaylandSeat *self) {
  return static_cast<int>(self->capabilities().toInt());
}

//  bool QWaylandSeat::isOwner(QInputEvent *inputEvent) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QWaylandSeat7isOwnerEP11QInputEvent(
    const QWaylandSeat *self,
    QInputEvent *inputEvent) {
  return self->isOwner(inputEvent);
}

//  void QWaylandSeat::sendUnicodeKeyEvent(uint unicode, QEvent::Type type)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QWaylandSeat19sendUnicodeKeyEventEjN6QEvent4TypeE(
    QWaylandSeat *self,
    uint unicode,
    QEvent::Type type) {
  self->sendUnicodeKeyEvent(unicode, type);
}

//  void QWaylandSeat::handleMouseFocusDestroyed()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QWaylandSeat25handleMouseFocusDestroyedEv(
    QWaylandSeat *self) {
  self->handleMouseFocusDestroyed();
}

//  a Python function taken by a CuteQWaylandSeat, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QWaylandSeat(
    QWaylandSeat *self,
    const char *key,
    void *call) {
  return static_cast<CuteQWaylandSeat *>(self)->take(key, call);
}

//  void QWaylandSeat::initialize()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QWaylandSeat10initializeEv(QWaylandSeat *self) {
  self->QWaylandSeat::initialize();
}

//  bool QWaylandSeat::isOwner(QInputEvent *inputEvent) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK12QWaylandSeat7isOwnerEP11QInputEvent(
    const QWaylandSeat *self,
    QInputEvent *inputEvent) {
  return self->QWaylandSeat::isOwner(inputEvent);
}
