//  Written by dev_tooling.RitualGenerator from the records of
//  QtDataVisualization/qtouch3dinputhandler.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtGui/qtguiglobal.h>
#include <QtDataVisualization/qtouch3dinputhandler.h>
#include <QtCore/qstring.h>
#include <QtCore/qpoint.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QTouch3DInputHandler that Python can take functions over in. Every QTouch3DInputHandler
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQTouch3DInputHandlerCall0)(const void *, QTouchEvent *, int *);
typedef void (*CuteQTouch3DInputHandlerCall1)(const void *, QMouseEvent *, const QPoint *, int *);
typedef void (*CuteQTouch3DInputHandlerCall2)(const void *, QMouseEvent *, const QPoint *, int *);
typedef void (*CuteQTouch3DInputHandlerCall3)(const void *, QMouseEvent *, const QPoint *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQTouch3DInputHandlerCall4)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQTouch3DInputHandlerCall5)(const void *, QMouseEvent *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQTouch3DInputHandlerCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQTouch3DInputHandlerCall7)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQTouch3DInputHandlerCall8)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQTouch3DInputHandlerCall9)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQTouch3DInputHandlerCall10)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQTouch3DInputHandlerCall11)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQTouch3DInputHandlerCall12)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQTouch3DInputHandler : public QTouch3DInputHandler {
public:
  using QTouch3DInputHandler::QTouch3DInputHandler;
  void *taken[13] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN23QAbstract3DInputHandler10touchEventEP11QTouchEvent")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN23QAbstract3DInputHandler15mousePressEventEP11QMouseEventRK6QPoint")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN23QAbstract3DInputHandler17mouseReleaseEventEP11QMouseEventRK6QPoint")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN23QAbstract3DInputHandler14mouseMoveEventEP11QMouseEventRK6QPoint")) {
      taken[3] = call;
      return true;
    }
#if QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN23QAbstract3DInputHandler10wheelEventEP11QWheelEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN23QAbstract3DInputHandler21mouseDoubleClickEventEP11QMouseEvent")) {
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

  //  void QTouch3DInputHandler::touchEvent(QTouchEvent *event)
  void touchEvent(QTouchEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQTouch3DInputHandlerCall0 call = reinterpret_cast<CuteQTouch3DInputHandlerCall0>(taken[0]);
      call(this, event, &handled);
      if (handled) return;
    }
    QTouch3DInputHandler::touchEvent(event);
  }

  //  void Q3DInputHandler::mousePressEvent(QMouseEvent *event, const
  //      QPoint &mousePos)
  void mousePressEvent(QMouseEvent *event, const QPoint &mousePos) override {
    if (taken[1]) {
      int handled = 0;
      CuteQTouch3DInputHandlerCall1 call = reinterpret_cast<CuteQTouch3DInputHandlerCall1>(taken[1]);
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
    if (taken[2]) {
      int handled = 0;
      CuteQTouch3DInputHandlerCall2 call = reinterpret_cast<CuteQTouch3DInputHandlerCall2>(taken[2]);
      call(this, event, &mousePos, &handled);
      if (handled) return;
    }
    Q3DInputHandler::mouseReleaseEvent(event, mousePos);
  }

  //  void Q3DInputHandler::mouseMoveEvent(QMouseEvent *event, const QPoint
  //      &mousePos)
  void mouseMoveEvent(QMouseEvent *event, const QPoint &mousePos) override {
    if (taken[3]) {
      int handled = 0;
      CuteQTouch3DInputHandlerCall3 call = reinterpret_cast<CuteQTouch3DInputHandlerCall3>(taken[3]);
      call(this, event, &mousePos, &handled);
      if (handled) return;
    }
    Q3DInputHandler::mouseMoveEvent(event, mousePos);
  }

#if QT_CONFIG(wheelevent)
  //  void Q3DInputHandler::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQTouch3DInputHandlerCall4 call = reinterpret_cast<CuteQTouch3DInputHandlerCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    Q3DInputHandler::wheelEvent(event);
  }
#endif  // QT_CONFIG(wheelevent)

  //  void QAbstract3DInputHandler::mouseDoubleClickEvent(QMouseEvent
  //      *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQTouch3DInputHandlerCall5 call = reinterpret_cast<CuteQTouch3DInputHandlerCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstract3DInputHandler::mouseDoubleClickEvent(event);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQTouch3DInputHandlerCall6 call = reinterpret_cast<CuteQTouch3DInputHandlerCall6>(taken[6]);
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
      CuteQTouch3DInputHandlerCall7 call = reinterpret_cast<CuteQTouch3DInputHandlerCall7>(taken[7]);
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
      CuteQTouch3DInputHandlerCall8 call = reinterpret_cast<CuteQTouch3DInputHandlerCall8>(taken[8]);
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
      CuteQTouch3DInputHandlerCall9 call = reinterpret_cast<CuteQTouch3DInputHandlerCall9>(taken[9]);
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
      CuteQTouch3DInputHandlerCall10 call = reinterpret_cast<CuteQTouch3DInputHandlerCall10>(taken[10]);
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
      CuteQTouch3DInputHandlerCall11 call = reinterpret_cast<CuteQTouch3DInputHandlerCall11>(taken[11]);
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
      CuteQTouch3DInputHandlerCall12 call = reinterpret_cast<CuteQTouch3DInputHandlerCall12>(taken[12]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QTouch3DInputHandler::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK20QTouch3DInputHandler10metaObjectEv(
    const QTouch3DInputHandler *self) {
  return self->metaObject();
}

//  void *QTouch3DInputHandler::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN20QTouch3DInputHandler11qt_metacastEPKc(
    QTouch3DInputHandler *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QTouch3DInputHandler::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN20QTouch3DInputHandler11qt_metacallEN11QMetaObject4CallEiPPv(
    QTouch3DInputHandler *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QTouch3DInputHandler::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN20QTouch3DInputHandler2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QTouch3DInputHandler::tr(s, c, n));
}

//  QTouch3DInputHandler::QTouch3DInputHandler(QObject *parent)
extern "C" Q_DECL_EXPORT
QTouch3DInputHandler *ritual_ZN20QTouch3DInputHandlerC1EP7QObject(
    QObject *parent) {
  return new CuteQTouch3DInputHandler(parent);
}

//  QTouch3DInputHandler::~QTouch3DInputHandler()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QTouch3DInputHandlerD1Ev(QTouch3DInputHandler *self) {
  delete self;
}

//  void QTouch3DInputHandler::touchEvent(QTouchEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QTouch3DInputHandler10touchEventEP11QTouchEvent(
    QTouch3DInputHandler *self,
    QTouchEvent *event) {
  self->touchEvent(event);
}

//  a Python function taken by a CuteQTouch3DInputHandler, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QTouch3DInputHandler(
    QTouch3DInputHandler *self,
    const char *key,
    void *call) {
  return static_cast<CuteQTouch3DInputHandler *>(self)->take(key, call);
}

//  void QTouch3DInputHandler::touchEvent(QTouchEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QTouch3DInputHandler10touchEventEP11QTouchEvent(
    QTouch3DInputHandler *self,
    QTouchEvent *event) {
  self->QTouch3DInputHandler::touchEvent(event);
}
