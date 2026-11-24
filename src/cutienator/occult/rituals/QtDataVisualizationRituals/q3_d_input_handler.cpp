//  Written by dev_tooling.RitualGenerator from the records of
//  QtDataVisualization/q3dinputhandler.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtGui/qtguiglobal.h>
#include <QtDataVisualization/q3dinputhandler.h>
#include <QtCore/qstring.h>
#include <QtCore/qpoint.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A Q3DInputHandler that Python can take functions over in. Every Q3DInputHandler
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQ3DInputHandlerCall0)(const void *, QMouseEvent *, const QPoint *, int *);
typedef void (*CuteQ3DInputHandlerCall1)(const void *, QMouseEvent *, const QPoint *, int *);
typedef void (*CuteQ3DInputHandlerCall2)(const void *, QMouseEvent *, const QPoint *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQ3DInputHandlerCall3)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQ3DInputHandlerCall4)(const void *, QMouseEvent *, int *);
typedef void (*CuteQ3DInputHandlerCall5)(const void *, QTouchEvent *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQ3DInputHandlerCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQ3DInputHandlerCall7)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQ3DInputHandlerCall8)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQ3DInputHandlerCall9)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQ3DInputHandlerCall10)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQ3DInputHandlerCall11)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQ3DInputHandlerCall12)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQ3DInputHandler : public Q3DInputHandler {
public:
  using Q3DInputHandler::Q3DInputHandler;
  void *taken[13] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN23QAbstract3DInputHandler15mousePressEventEP11QMouseEventRK6QPoint")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN23QAbstract3DInputHandler17mouseReleaseEventEP11QMouseEventRK6QPoint")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN23QAbstract3DInputHandler14mouseMoveEventEP11QMouseEventRK6QPoint")) {
      taken[2] = call;
      return true;
    }
#if QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN23QAbstract3DInputHandler10wheelEventEP11QWheelEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN23QAbstract3DInputHandler21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN23QAbstract3DInputHandler10touchEventEP11QTouchEvent")) {
      taken[5] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void Q3DInputHandler::mousePressEvent(QMouseEvent *event, const
  //      QPoint &mousePos)
  void mousePressEvent(QMouseEvent *event, const QPoint &mousePos) override {
    if (taken[0]) {
      int handled = 0;
      CuteQ3DInputHandlerCall0 call = reinterpret_cast<CuteQ3DInputHandlerCall0>(taken[0]);
      call(this, event, &mousePos, &handled);
      if (handled) return;
    }
    Q3DInputHandler::mousePressEvent(event, mousePos);
  }

  //  void Q3DInputHandler::mouseReleaseEvent(QMouseEvent *event, const
  //      QPoint &mousePos)
  void mouseReleaseEvent(
      QMouseEvent *event,
      const QPoint &mousePos) override {
    if (taken[1]) {
      int handled = 0;
      CuteQ3DInputHandlerCall1 call = reinterpret_cast<CuteQ3DInputHandlerCall1>(taken[1]);
      call(this, event, &mousePos, &handled);
      if (handled) return;
    }
    Q3DInputHandler::mouseReleaseEvent(event, mousePos);
  }

  //  void Q3DInputHandler::mouseMoveEvent(QMouseEvent *event, const QPoint
  //      &mousePos)
  void mouseMoveEvent(QMouseEvent *event, const QPoint &mousePos) override {
    if (taken[2]) {
      int handled = 0;
      CuteQ3DInputHandlerCall2 call = reinterpret_cast<CuteQ3DInputHandlerCall2>(taken[2]);
      call(this, event, &mousePos, &handled);
      if (handled) return;
    }
    Q3DInputHandler::mouseMoveEvent(event, mousePos);
  }

#if QT_CONFIG(wheelevent)
  //  void Q3DInputHandler::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQ3DInputHandlerCall3 call = reinterpret_cast<CuteQ3DInputHandlerCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    Q3DInputHandler::wheelEvent(event);
  }
#endif  // QT_CONFIG(wheelevent)

  //  void QAbstract3DInputHandler::mouseDoubleClickEvent(QMouseEvent
  //      *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQ3DInputHandlerCall4 call = reinterpret_cast<CuteQ3DInputHandlerCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstract3DInputHandler::mouseDoubleClickEvent(event);
  }

  //  void QAbstract3DInputHandler::touchEvent(QTouchEvent *event)
  void touchEvent(QTouchEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQ3DInputHandlerCall5 call = reinterpret_cast<CuteQ3DInputHandlerCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstract3DInputHandler::touchEvent(event);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQ3DInputHandlerCall6 call = reinterpret_cast<CuteQ3DInputHandlerCall6>(taken[6]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQ3DInputHandlerCall7 call = reinterpret_cast<CuteQ3DInputHandlerCall7>(taken[7]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQ3DInputHandlerCall8 call = reinterpret_cast<CuteQ3DInputHandlerCall8>(taken[8]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQ3DInputHandlerCall9 call = reinterpret_cast<CuteQ3DInputHandlerCall9>(taken[9]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQ3DInputHandlerCall10 call = reinterpret_cast<CuteQ3DInputHandlerCall10>(taken[10]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[11]) {
      int handled = 0;
      CuteQ3DInputHandlerCall11 call = reinterpret_cast<CuteQ3DInputHandlerCall11>(taken[11]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[12]) {
      int handled = 0;
      CuteQ3DInputHandlerCall12 call = reinterpret_cast<CuteQ3DInputHandlerCall12>(taken[12]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Q3DInputHandler::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15Q3DInputHandler10metaObjectEv(
    const Q3DInputHandler *self) {
  return self->metaObject();
}

//  QString Q3DInputHandler::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15Q3DInputHandler2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Q3DInputHandler::tr(s, c, n));
}

//  Q3DInputHandler::Q3DInputHandler(QObject *parent)
extern "C" Q_DECL_EXPORT
Q3DInputHandler *ritual_ZN15Q3DInputHandlerC1EP7QObject(QObject *parent) {
  return new CuteQ3DInputHandler(parent);
}

//  Q3DInputHandler::~Q3DInputHandler()
extern "C" Q_DECL_EXPORT
void ritual_ZN15Q3DInputHandlerD1Ev(Q3DInputHandler *self) {
  delete self;
}

//  void Q3DInputHandler::setRotationEnabled(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN15Q3DInputHandler18setRotationEnabledEb(
    Q3DInputHandler *self,
    bool enable) {
  self->setRotationEnabled(enable);
}

//  bool Q3DInputHandler::isRotationEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15Q3DInputHandler17isRotationEnabledEv(
    const Q3DInputHandler *self) {
  return self->isRotationEnabled();
}

//  void Q3DInputHandler::setZoomEnabled(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN15Q3DInputHandler14setZoomEnabledEb(
    Q3DInputHandler *self,
    bool enable) {
  self->setZoomEnabled(enable);
}

//  bool Q3DInputHandler::isZoomEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15Q3DInputHandler13isZoomEnabledEv(
    const Q3DInputHandler *self) {
  return self->isZoomEnabled();
}

//  void Q3DInputHandler::setSelectionEnabled(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN15Q3DInputHandler19setSelectionEnabledEb(
    Q3DInputHandler *self,
    bool enable) {
  self->setSelectionEnabled(enable);
}

//  bool Q3DInputHandler::isSelectionEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15Q3DInputHandler18isSelectionEnabledEv(
    const Q3DInputHandler *self) {
  return self->isSelectionEnabled();
}

//  void Q3DInputHandler::setZoomAtTargetEnabled(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN15Q3DInputHandler22setZoomAtTargetEnabledEb(
    Q3DInputHandler *self,
    bool enable) {
  self->setZoomAtTargetEnabled(enable);
}

//  bool Q3DInputHandler::isZoomAtTargetEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15Q3DInputHandler21isZoomAtTargetEnabledEv(
    const Q3DInputHandler *self) {
  return self->isZoomAtTargetEnabled();
}

//  void Q3DInputHandler::mousePressEvent(QMouseEvent *event, const QPoint
//      &mousePos)
extern "C" Q_DECL_EXPORT
void ritual_ZN15Q3DInputHandler15mousePressEventEP11QMouseEventRK6QPoint(
    Q3DInputHandler *self,
    QMouseEvent *event,
    const QPoint *mousePos) {
  self->mousePressEvent(event, *mousePos);
}

//  void Q3DInputHandler::mouseReleaseEvent(QMouseEvent *event, const QPoint
//      &mousePos)
extern "C" Q_DECL_EXPORT
void ritual_ZN15Q3DInputHandler17mouseReleaseEventEP11QMouseEventRK6QPoint(
    Q3DInputHandler *self,
    QMouseEvent *event,
    const QPoint *mousePos) {
  self->mouseReleaseEvent(event, *mousePos);
}

//  void Q3DInputHandler::mouseMoveEvent(QMouseEvent *event, const QPoint
//      &mousePos)
extern "C" Q_DECL_EXPORT
void ritual_ZN15Q3DInputHandler14mouseMoveEventEP11QMouseEventRK6QPoint(
    Q3DInputHandler *self,
    QMouseEvent *event,
    const QPoint *mousePos) {
  self->mouseMoveEvent(event, *mousePos);
}

#if QT_CONFIG(wheelevent)
//  void Q3DInputHandler::wheelEvent(QWheelEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN15Q3DInputHandler10wheelEventEP11QWheelEvent(
    Q3DInputHandler *self,
    QWheelEvent *event) {
  self->wheelEvent(event);
}
#endif  // QT_CONFIG(wheelevent)

//  a Python function taken by a CuteQ3DInputHandler, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Q3DInputHandler(
    Q3DInputHandler *self,
    const char *key,
    void *call) {
  return static_cast<CuteQ3DInputHandler *>(self)->take(key, call);
}

//  void Q3DInputHandler::mousePressEvent(QMouseEvent *event, const QPoint
//      &mousePos)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15Q3DInputHandler15mousePressEventEP11QMouseEventRK6QPoint(
    Q3DInputHandler *self,
    QMouseEvent *event,
    const QPoint *mousePos) {
  self->Q3DInputHandler::mousePressEvent(event, *mousePos);
}

//  void Q3DInputHandler::mouseReleaseEvent(QMouseEvent *event, const QPoint
//      &mousePos)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15Q3DInputHandler17mouseReleaseEventEP11QMouseEventRK6QPoint(
    Q3DInputHandler *self,
    QMouseEvent *event,
    const QPoint *mousePos) {
  self->Q3DInputHandler::mouseReleaseEvent(event, *mousePos);
}

//  void Q3DInputHandler::mouseMoveEvent(QMouseEvent *event, const QPoint
//      &mousePos)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15Q3DInputHandler14mouseMoveEventEP11QMouseEventRK6QPoint(
    Q3DInputHandler *self,
    QMouseEvent *event,
    const QPoint *mousePos) {
  self->Q3DInputHandler::mouseMoveEvent(event, *mousePos);
}

#if QT_CONFIG(wheelevent)
//  void Q3DInputHandler::wheelEvent(QWheelEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15Q3DInputHandler10wheelEventEP11QWheelEvent(
    Q3DInputHandler *self,
    QWheelEvent *event) {
  self->Q3DInputHandler::wheelEvent(event);
}
#endif  // QT_CONFIG(wheelevent)
