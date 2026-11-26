//  Written by dev_tooling.RitualGenerator from the records of
//  QtDataVisualization/qabstract3dinputhandler.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtDataVisualization/qabstract3dinputhandler.h>
#include <QtCore/qstring.h>
#include <QtCore/qpoint.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QAbstract3DInputHandler that Python can take functions over in. Every QAbstract3DInputHandler
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQAbstract3DInputHandlerCall0)(const void *, QMouseEvent *, int *);
typedef void (*CuteQAbstract3DInputHandlerCall1)(const void *, QTouchEvent *, int *);
typedef void (*CuteQAbstract3DInputHandlerCall2)(const void *, QMouseEvent *, const QPoint *, int *);
typedef void (*CuteQAbstract3DInputHandlerCall3)(const void *, QMouseEvent *, const QPoint *, int *);
typedef void (*CuteQAbstract3DInputHandlerCall4)(const void *, QMouseEvent *, const QPoint *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQAbstract3DInputHandlerCall5)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAbstract3DInputHandlerCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAbstract3DInputHandlerCall7)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstract3DInputHandlerCall8)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstract3DInputHandlerCall9)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstract3DInputHandlerCall10)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstract3DInputHandlerCall11)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstract3DInputHandlerCall12)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQAbstract3DInputHandler : public QAbstract3DInputHandler {
public:
  using QAbstract3DInputHandler::QAbstract3DInputHandler;
  void *taken[13] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN23QAbstract3DInputHandler21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN23QAbstract3DInputHandler10touchEventEP11QTouchEvent")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN23QAbstract3DInputHandler15mousePressEventEP11QMouseEventRK6QPoint")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN23QAbstract3DInputHandler17mouseReleaseEventEP11QMouseEventRK6QPoint")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN23QAbstract3DInputHandler14mouseMoveEventEP11QMouseEventRK6QPoint")) {
      taken[4] = call;
      return true;
    }
#if QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN23QAbstract3DInputHandler10wheelEventEP11QWheelEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(wheelevent)
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

  //  void QAbstract3DInputHandler::mouseDoubleClickEvent(QMouseEvent
  //      *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQAbstract3DInputHandlerCall0 call = reinterpret_cast<CuteQAbstract3DInputHandlerCall0>(taken[0]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstract3DInputHandler::mouseDoubleClickEvent(event);
  }

  //  void QAbstract3DInputHandler::touchEvent(QTouchEvent *event)
  void touchEvent(QTouchEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQAbstract3DInputHandlerCall1 call = reinterpret_cast<CuteQAbstract3DInputHandlerCall1>(taken[1]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstract3DInputHandler::touchEvent(event);
  }

  //  void QAbstract3DInputHandler::mousePressEvent(QMouseEvent *event,
  //      const QPoint &mousePos)
  void mousePressEvent(QMouseEvent *event, const QPoint &mousePos) override {
    if (taken[2]) {
      int handled = 0;
      CuteQAbstract3DInputHandlerCall2 call = reinterpret_cast<CuteQAbstract3DInputHandlerCall2>(taken[2]);
      call(this, event, &mousePos, &handled);
      if (handled) return;
    }
    QAbstract3DInputHandler::mousePressEvent(event, mousePos);
  }

  //  void QAbstract3DInputHandler::mouseReleaseEvent(QMouseEvent *event,
  //      const QPoint &mousePos)
  void mouseReleaseEvent(
      QMouseEvent *event,
      const QPoint &mousePos) override {
    if (taken[3]) {
      int handled = 0;
      CuteQAbstract3DInputHandlerCall3 call = reinterpret_cast<CuteQAbstract3DInputHandlerCall3>(taken[3]);
      call(this, event, &mousePos, &handled);
      if (handled) return;
    }
    QAbstract3DInputHandler::mouseReleaseEvent(event, mousePos);
  }

  //  void QAbstract3DInputHandler::mouseMoveEvent(QMouseEvent *event,
  //      const QPoint &mousePos)
  void mouseMoveEvent(QMouseEvent *event, const QPoint &mousePos) override {
    if (taken[4]) {
      int handled = 0;
      CuteQAbstract3DInputHandlerCall4 call = reinterpret_cast<CuteQAbstract3DInputHandlerCall4>(taken[4]);
      call(this, event, &mousePos, &handled);
      if (handled) return;
    }
    QAbstract3DInputHandler::mouseMoveEvent(event, mousePos);
  }

#if QT_CONFIG(wheelevent)
  //  void QAbstract3DInputHandler::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQAbstract3DInputHandlerCall5 call = reinterpret_cast<CuteQAbstract3DInputHandlerCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstract3DInputHandler::wheelEvent(event);
  }
#endif  // QT_CONFIG(wheelevent)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQAbstract3DInputHandlerCall6 call = reinterpret_cast<CuteQAbstract3DInputHandlerCall6>(taken[6]);
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
      CuteQAbstract3DInputHandlerCall7 call = reinterpret_cast<CuteQAbstract3DInputHandlerCall7>(taken[7]);
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
      CuteQAbstract3DInputHandlerCall8 call = reinterpret_cast<CuteQAbstract3DInputHandlerCall8>(taken[8]);
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
      CuteQAbstract3DInputHandlerCall9 call = reinterpret_cast<CuteQAbstract3DInputHandlerCall9>(taken[9]);
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
      CuteQAbstract3DInputHandlerCall10 call = reinterpret_cast<CuteQAbstract3DInputHandlerCall10>(taken[10]);
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
      CuteQAbstract3DInputHandlerCall11 call = reinterpret_cast<CuteQAbstract3DInputHandlerCall11>(taken[11]);
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
      CuteQAbstract3DInputHandlerCall12 call = reinterpret_cast<CuteQAbstract3DInputHandlerCall12>(taken[12]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QAbstract3DInputHandler::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK23QAbstract3DInputHandler10metaObjectEv(
    const QAbstract3DInputHandler *self) {
  return self->metaObject();
}

//  void *QAbstract3DInputHandler::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN23QAbstract3DInputHandler11qt_metacastEPKc(
    QAbstract3DInputHandler *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QAbstract3DInputHandler::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN23QAbstract3DInputHandler11qt_metacallEN11QMetaObject4CallEiPPv(
    QAbstract3DInputHandler *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QAbstract3DInputHandler::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN23QAbstract3DInputHandler2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QAbstract3DInputHandler::tr(s, c, n));
}

//  QAbstract3DInputHandler::QAbstract3DInputHandler(QObject *parent)
extern "C" Q_DECL_EXPORT
QAbstract3DInputHandler *ritual_ZN23QAbstract3DInputHandlerC1EP7QObject(
    QObject *parent) {
  return new CuteQAbstract3DInputHandler(parent);
}

//  QAbstract3DInputHandler::~QAbstract3DInputHandler()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QAbstract3DInputHandlerD1Ev(QAbstract3DInputHandler *self) {
  delete self;
}

//  void QAbstract3DInputHandler::mouseDoubleClickEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QAbstract3DInputHandler21mouseDoubleClickEventEP11QMouseEvent(
    QAbstract3DInputHandler *self,
    QMouseEvent *event) {
  self->mouseDoubleClickEvent(event);
}

//  void QAbstract3DInputHandler::touchEvent(QTouchEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QAbstract3DInputHandler10touchEventEP11QTouchEvent(
    QAbstract3DInputHandler *self,
    QTouchEvent *event) {
  self->touchEvent(event);
}

//  void QAbstract3DInputHandler::mousePressEvent(QMouseEvent *event, const
//      QPoint &mousePos)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QAbstract3DInputHandler15mousePressEventEP11QMouseEventRK6QPoint(
    QAbstract3DInputHandler *self,
    QMouseEvent *event,
    const QPoint *mousePos) {
  self->mousePressEvent(event, *mousePos);
}

//  void QAbstract3DInputHandler::mouseReleaseEvent(QMouseEvent *event, const
//      QPoint &mousePos)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QAbstract3DInputHandler17mouseReleaseEventEP11QMouseEventRK6QPoint(
    QAbstract3DInputHandler *self,
    QMouseEvent *event,
    const QPoint *mousePos) {
  self->mouseReleaseEvent(event, *mousePos);
}

//  void QAbstract3DInputHandler::mouseMoveEvent(QMouseEvent *event, const
//      QPoint &mousePos)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QAbstract3DInputHandler14mouseMoveEventEP11QMouseEventRK6QPoint(
    QAbstract3DInputHandler *self,
    QMouseEvent *event,
    const QPoint *mousePos) {
  self->mouseMoveEvent(event, *mousePos);
}

#if QT_CONFIG(wheelevent)
//  void QAbstract3DInputHandler::wheelEvent(QWheelEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QAbstract3DInputHandler10wheelEventEP11QWheelEvent(
    QAbstract3DInputHandler *self,
    QWheelEvent *event) {
  self->wheelEvent(event);
}
#endif  // QT_CONFIG(wheelevent)

//  InputView QAbstract3DInputHandler::inputView() const
extern "C" Q_DECL_EXPORT
QAbstract3DInputHandler::InputView ritual_ZNK23QAbstract3DInputHandler9inputViewEv(
    const QAbstract3DInputHandler *self) {
  return self->inputView();
}

//  void QAbstract3DInputHandler::setInputView(InputView inputView)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QAbstract3DInputHandler12setInputViewENS_9InputViewE(
    QAbstract3DInputHandler *self,
    QAbstract3DInputHandler::InputView inputView) {
  self->setInputView(inputView);
}

//  QPoint QAbstract3DInputHandler::inputPosition() const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK23QAbstract3DInputHandler13inputPositionEv(
    const QAbstract3DInputHandler *self) {
  return new QPoint(self->inputPosition());
}

//  void QAbstract3DInputHandler::setInputPosition(const QPoint &position)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QAbstract3DInputHandler16setInputPositionERK6QPoint(
    QAbstract3DInputHandler *self,
    const QPoint *position) {
  self->setInputPosition(*position);
}

//  Q3DScene *QAbstract3DInputHandler::scene() const
extern "C" Q_DECL_EXPORT
Q3DScene *ritual_ZNK23QAbstract3DInputHandler5sceneEv(
    const QAbstract3DInputHandler *self) {
  return self->scene();
}

//  void QAbstract3DInputHandler::setScene(Q3DScene *scene)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QAbstract3DInputHandler8setSceneEP8Q3DScene(
    QAbstract3DInputHandler *self,
    Q3DScene *scene) {
  self->setScene(scene);
}

//  void QAbstract3DInputHandler::positionChanged(const QPoint &position)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QAbstract3DInputHandler15positionChangedERK6QPoint(
    QAbstract3DInputHandler *self,
    const QPoint *position) {
  self->positionChanged(*position);
}

//  void QAbstract3DInputHandler::inputViewChanged(QAbstract3DInputHandler::I
//      nputView view)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QAbstract3DInputHandler16inputViewChangedENS_9InputViewE(
    QAbstract3DInputHandler *self,
    QAbstract3DInputHandler::InputView view) {
  self->inputViewChanged(view);
}

//  void QAbstract3DInputHandler::sceneChanged(Q3DScene *scene)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QAbstract3DInputHandler12sceneChangedEP8Q3DScene(
    QAbstract3DInputHandler *self,
    Q3DScene *scene) {
  self->sceneChanged(scene);
}

//  void QAbstract3DInputHandler::setPrevDistance(int distance)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QAbstract3DInputHandler15setPrevDistanceEi(
    QAbstract3DInputHandler *self,
    int distance) {
  self->setPrevDistance(distance);
}

//  int QAbstract3DInputHandler::prevDistance() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK23QAbstract3DInputHandler12prevDistanceEv(
    const QAbstract3DInputHandler *self) {
  return self->prevDistance();
}

//  void QAbstract3DInputHandler::setPreviousInputPos(const QPoint &position)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QAbstract3DInputHandler19setPreviousInputPosERK6QPoint(
    QAbstract3DInputHandler *self,
    const QPoint *position) {
  self->setPreviousInputPos(*position);
}

//  QPoint QAbstract3DInputHandler::previousInputPos() const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK23QAbstract3DInputHandler16previousInputPosEv(
    const QAbstract3DInputHandler *self) {
  return new QPoint(self->previousInputPos());
}

//  a Python function taken by a CuteQAbstract3DInputHandler, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAbstract3DInputHandler(
    QAbstract3DInputHandler *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAbstract3DInputHandler *>(self)->take(key, call);
}

//  void QAbstract3DInputHandler::mouseDoubleClickEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QAbstract3DInputHandler21mouseDoubleClickEventEP11QMouseEvent(
    QAbstract3DInputHandler *self,
    QMouseEvent *event) {
  self->QAbstract3DInputHandler::mouseDoubleClickEvent(event);
}

//  void QAbstract3DInputHandler::touchEvent(QTouchEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QAbstract3DInputHandler10touchEventEP11QTouchEvent(
    QAbstract3DInputHandler *self,
    QTouchEvent *event) {
  self->QAbstract3DInputHandler::touchEvent(event);
}

//  void QAbstract3DInputHandler::mousePressEvent(QMouseEvent *event, const
//      QPoint &mousePos)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QAbstract3DInputHandler15mousePressEventEP11QMouseEventRK6QPoint(
    QAbstract3DInputHandler *self,
    QMouseEvent *event,
    const QPoint *mousePos) {
  self->QAbstract3DInputHandler::mousePressEvent(event, *mousePos);
}

//  void QAbstract3DInputHandler::mouseReleaseEvent(QMouseEvent *event, const
//      QPoint &mousePos)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QAbstract3DInputHandler17mouseReleaseEventEP11QMouseEventRK6QPoint(
    QAbstract3DInputHandler *self,
    QMouseEvent *event,
    const QPoint *mousePos) {
  self->QAbstract3DInputHandler::mouseReleaseEvent(event, *mousePos);
}

//  void QAbstract3DInputHandler::mouseMoveEvent(QMouseEvent *event, const
//      QPoint &mousePos)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QAbstract3DInputHandler14mouseMoveEventEP11QMouseEventRK6QPoint(
    QAbstract3DInputHandler *self,
    QMouseEvent *event,
    const QPoint *mousePos) {
  self->QAbstract3DInputHandler::mouseMoveEvent(event, *mousePos);
}

#if QT_CONFIG(wheelevent)
//  void QAbstract3DInputHandler::wheelEvent(QWheelEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QAbstract3DInputHandler10wheelEventEP11QWheelEvent(
    QAbstract3DInputHandler *self,
    QWheelEvent *event) {
  self->QAbstract3DInputHandler::wheelEvent(event);
}
#endif  // QT_CONFIG(wheelevent)

//  QList<QAbstract3DInputHandler *>::QList()
extern "C" Q_DECL_EXPORT
QList<QAbstract3DInputHandler *> *ritual_list_make_QAbstract3DInputHandler_ptr() {
  return new QList<QAbstract3DInputHandler *>();
}

//  void QList<QAbstract3DInputHandler *>::append(const
//      QAbstract3DInputHandler * &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QAbstract3DInputHandler_ptr(
    QList<QAbstract3DInputHandler *> *self,
    QAbstract3DInputHandler *element) {
  self->append(element);
}

//  qsizetype QList<QAbstract3DInputHandler *>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QAbstract3DInputHandler_ptr(
    const QList<QAbstract3DInputHandler *> *self) {
  return self->size();
}

//  const QAbstract3DInputHandler * &QList<QAbstract3DInputHandler
//      *>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QAbstract3DInputHandler *ritual_list_at_QAbstract3DInputHandler_ptr(
    const QList<QAbstract3DInputHandler *> *self,
    long long index) {
  return self->at(index);
}

//  QList<QAbstract3DInputHandler *>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QAbstract3DInputHandler_ptr(
    QList<QAbstract3DInputHandler *> *self) {
  delete self;
}
