//  Written by dev_tooling.RitualGenerator from the records of QtGui/qdrag.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
#include <QtGui/qdrag.h>
#include <QtCore/qstring.h>
#include <QtGui/qpixmap.h>
#include <QtCore/qpoint.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QDrag that Python can take functions over in. Every QDrag
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDragCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDragCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDragCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDragCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDragCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDragCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDragCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQDrag : public QDrag {
public:
  using QDrag::QDrag;
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
      CuteQDragCall0 call = reinterpret_cast<CuteQDragCall0>(taken[0]);
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
      CuteQDragCall1 call = reinterpret_cast<CuteQDragCall1>(taken[1]);
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
      CuteQDragCall2 call = reinterpret_cast<CuteQDragCall2>(taken[2]);
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
      CuteQDragCall3 call = reinterpret_cast<CuteQDragCall3>(taken[3]);
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
      CuteQDragCall4 call = reinterpret_cast<CuteQDragCall4>(taken[4]);
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
      CuteQDragCall5 call = reinterpret_cast<CuteQDragCall5>(taken[5]);
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
      CuteQDragCall6 call = reinterpret_cast<CuteQDragCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QDrag::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK5QDrag10metaObjectEv(const QDrag *self) {
  return self->metaObject();
}

//  QString QDrag::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN5QDrag2trEPKcS1_i(const char *s, const char *c, int n) {
  return new QString(QDrag::tr(s, c, n));
}

//  QDragPrivate *QDrag::d_func()
extern "C" Q_DECL_EXPORT
QDragPrivate *ritual_ZN5QDrag6d_funcEv(QDrag *self) {
  return self->d_func();
}

//  const QDragPrivate *QDrag::d_func() const
extern "C" Q_DECL_EXPORT
const QDragPrivate *ritual_ZNK5QDrag6d_funcEv(const QDrag *self) {
  return self->d_func();
}

//  QDrag::QDrag(QObject *dragSource)
extern "C" Q_DECL_EXPORT
QDrag *ritual_ZN5QDragC1EP7QObject(QObject *dragSource) {
  return new CuteQDrag(dragSource);
}

//  QDrag::~QDrag()
extern "C" Q_DECL_EXPORT
void ritual_ZN5QDragD1Ev(QDrag *self) {
  delete self;
}

//  void QDrag::setMimeData(QMimeData *data)
extern "C" Q_DECL_EXPORT
void ritual_ZN5QDrag11setMimeDataEP9QMimeData(QDrag *self, QMimeData *data) {
  self->setMimeData(data);
}

//  QMimeData *QDrag::mimeData() const
extern "C" Q_DECL_EXPORT
QMimeData *ritual_ZNK5QDrag8mimeDataEv(const QDrag *self) {
  return self->mimeData();
}

//  void QDrag::setPixmap(const QPixmap &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN5QDrag9setPixmapERK7QPixmap(QDrag *self, const QPixmap *a0) {
  self->setPixmap(*a0);
}

//  QPixmap QDrag::pixmap() const
extern "C" Q_DECL_EXPORT
QPixmap *ritual_ZNK5QDrag6pixmapEv(const QDrag *self) {
  return new QPixmap(self->pixmap());
}

//  void QDrag::setHotSpot(const QPoint &hotspot)
extern "C" Q_DECL_EXPORT
void ritual_ZN5QDrag10setHotSpotERK6QPoint(
    QDrag *self,
    const QPoint *hotspot) {
  self->setHotSpot(*hotspot);
}

//  QPoint QDrag::hotSpot() const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK5QDrag7hotSpotEv(const QDrag *self) {
  return new QPoint(self->hotSpot());
}

//  QObject *QDrag::source() const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK5QDrag6sourceEv(const QDrag *self) {
  return self->source();
}

//  QObject *QDrag::target() const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK5QDrag6targetEv(const QDrag *self) {
  return self->target();
}

//  Qt::DropAction QDrag::exec(Qt::DropActions supportedActions)
extern "C" Q_DECL_EXPORT
Qt::DropAction ritual_ZN5QDrag4execE6QFlagsIN2Qt10DropActionEE(
    QDrag *self,
    int supportedActions) {
  return self->exec(QFlags<Qt::DropAction>::fromInt(supportedActions));
}

//  Qt::DropAction QDrag::exec(Qt::DropActions supportedActions,
//      Qt::DropAction defaultAction)
extern "C" Q_DECL_EXPORT
Qt::DropAction ritual_ZN5QDrag4execE6QFlagsIN2Qt10DropActionEES2_(
    QDrag *self,
    int supportedActions,
    Qt::DropAction defaultAction) {
  return self->exec(
      QFlags<Qt::DropAction>::fromInt(supportedActions),
      defaultAction);
}

//  void QDrag::setDragCursor(const QPixmap &cursor, Qt::DropAction action)
extern "C" Q_DECL_EXPORT
void ritual_ZN5QDrag13setDragCursorERK7QPixmapN2Qt10DropActionE(
    QDrag *self,
    const QPixmap *cursor,
    Qt::DropAction action) {
  self->setDragCursor(*cursor, action);
}

//  QPixmap QDrag::dragCursor(Qt::DropAction action) const
extern "C" Q_DECL_EXPORT
QPixmap *ritual_ZNK5QDrag10dragCursorEN2Qt10DropActionE(
    const QDrag *self,
    Qt::DropAction action) {
  return new QPixmap(self->dragCursor(action));
}

//  Qt::DropActions QDrag::supportedActions() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK5QDrag16supportedActionsEv(const QDrag *self) {
  return static_cast<int>(self->supportedActions().toInt());
}

//  Qt::DropAction QDrag::defaultAction() const
extern "C" Q_DECL_EXPORT
Qt::DropAction ritual_ZNK5QDrag13defaultActionEv(const QDrag *self) {
  return self->defaultAction();
}

//  void QDrag::cancel()
extern "C" Q_DECL_EXPORT
void ritual_ZN5QDrag6cancelEv() {
  QDrag::cancel();
}

//  a Python function taken by a CuteQDrag, for the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDrag(QDrag *self, const char *key, void *call) {
  return static_cast<CuteQDrag *>(self)->take(key, call);
}

#endif  // QT_CONFIG(draganddrop)
#endif  // QT_CONFIG(draganddrop)
