//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/qpa/qplatformwindow_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if QT_CONFIG(wayland)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/qpa/qplatformwindow_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmargins.h>
#include <QtCore/qrect.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QNativeInterface::Private::QWaylandWindow that Python can take functions over in. Every QNativeInterface::Private::QWaylandWindow
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(wayland)
typedef void (*CuteQNativeInterface_Private_QWaylandWindowCall0)(const void *, const QMargins *, int *);
#endif  // QT_CONFIG(wayland)
#if QT_CONFIG(wayland)
typedef void (*CuteQNativeInterface_Private_QWaylandWindowCall1)(const void *, uint, int *);
#endif  // QT_CONFIG(wayland)
#if QT_CONFIG(wayland)
typedef void (*CuteQNativeInterface_Private_QWaylandWindowCall2)(const void *, const QString *, int *);
#endif  // QT_CONFIG(wayland)
#if QT_CONFIG(wayland)
typedef void (*CuteQNativeInterface_Private_QWaylandWindowCall3)(const void *, int, int *);
#endif  // QT_CONFIG(wayland)
#if QT_CONFIG(wayland)
typedef void (*CuteQNativeInterface_Private_QWaylandWindowCall4)(const void *, const QRect *, int *);
#endif  // QT_CONFIG(wayland)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQNativeInterface_Private_QWaylandWindowCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQNativeInterface_Private_QWaylandWindowCall6)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNativeInterface_Private_QWaylandWindowCall7)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNativeInterface_Private_QWaylandWindowCall8)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNativeInterface_Private_QWaylandWindowCall9)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNativeInterface_Private_QWaylandWindowCall10)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNativeInterface_Private_QWaylandWindowCall11)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQNativeInterface_Private_QWaylandWindow : public QNativeInterface::Private::QWaylandWindow {
public:
  using QNativeInterface::Private::QWaylandWindow::QWaylandWindow;
  void *taken[12] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(wayland)
    if (!std::strcmp(key, "_ZN16QNativeInterface7Private14QWaylandWindow16setCustomMarginsERK8QMargins")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(wayland)
#if QT_CONFIG(wayland)
    if (!std::strcmp(key, "_ZN16QNativeInterface7Private14QWaylandWindow25requestXdgActivationTokenEj")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(wayland)
#if QT_CONFIG(wayland)
    if (!std::strcmp(key, "_ZN16QNativeInterface7Private14QWaylandWindow19setSessionRestoreIdERK7QString")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(wayland)
#if QT_CONFIG(wayland)
    if (!std::strcmp(key, "_ZN16QNativeInterface7Private14QWaylandWindow21setExtendedWindowTypeENS1_10WindowTypeE")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(wayland)
#if QT_CONFIG(wayland)
    if (!std::strcmp(key, "_ZN16QNativeInterface7Private14QWaylandWindow24setParentControlGeometryERK5QRect")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(wayland)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if QT_CONFIG(wayland)
  //  void
  //      QNativeInterface::Private::QWaylandWindow::setCustomMargins(const
  //      QMargins &margins)
  void setCustomMargins(const QMargins &margins) override {
    if (taken[0]) {
      int handled = 0;
      CuteQNativeInterface_Private_QWaylandWindowCall0 call = reinterpret_cast<CuteQNativeInterface_Private_QWaylandWindowCall0>(taken[0]);
      call(this, &margins, &handled);
      if (handled) return;
    }
  }
#endif  // QT_CONFIG(wayland)

#if QT_CONFIG(wayland)
  //  void QNativeInterface::Private::QWaylandWindow::requestXdgActivationT
  //      oken(uint serial)
  void requestXdgActivationToken(uint serial) override {
    if (taken[1]) {
      int handled = 0;
      CuteQNativeInterface_Private_QWaylandWindowCall1 call = reinterpret_cast<CuteQNativeInterface_Private_QWaylandWindowCall1>(taken[1]);
      call(this, serial, &handled);
      if (handled) return;
    }
  }
#endif  // QT_CONFIG(wayland)

#if QT_CONFIG(wayland)
  //  void
  //      QNativeInterface::Private::QWaylandWindow::setSessionRestoreId(co
  //      nst QString &role)
  void setSessionRestoreId(const QString &role) override {
    if (taken[2]) {
      int handled = 0;
      CuteQNativeInterface_Private_QWaylandWindowCall2 call = reinterpret_cast<CuteQNativeInterface_Private_QWaylandWindowCall2>(taken[2]);
      call(this, &role, &handled);
      if (handled) return;
    }
  }
#endif  // QT_CONFIG(wayland)

#if QT_CONFIG(wayland)
  //  void QNativeInterface::Private::QWaylandWindow::setExtendedWindowType
  //      (WindowType windowType)
  void setExtendedWindowType(
      QNativeInterface::Private::QWaylandWindow::WindowType windowType) override {
    if (taken[3]) {
      int handled = 0;
      CuteQNativeInterface_Private_QWaylandWindowCall3 call = reinterpret_cast<CuteQNativeInterface_Private_QWaylandWindowCall3>(taken[3]);
      call(this, static_cast<int>(windowType), &handled);
      if (handled) return;
    }
  }
#endif  // QT_CONFIG(wayland)

#if QT_CONFIG(wayland)
  //  void QNativeInterface::Private::QWaylandWindow::setParentControlGeome
  //      try(const QRect &parentAnchor)
  void setParentControlGeometry(const QRect &parentAnchor) override {
    if (taken[4]) {
      int handled = 0;
      CuteQNativeInterface_Private_QWaylandWindowCall4 call = reinterpret_cast<CuteQNativeInterface_Private_QWaylandWindowCall4>(taken[4]);
      call(this, &parentAnchor, &handled);
      if (handled) return;
    }
  }
#endif  // QT_CONFIG(wayland)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQNativeInterface_Private_QWaylandWindowCall5 call = reinterpret_cast<CuteQNativeInterface_Private_QWaylandWindowCall5>(taken[5]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQNativeInterface_Private_QWaylandWindowCall6 call = reinterpret_cast<CuteQNativeInterface_Private_QWaylandWindowCall6>(taken[6]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQNativeInterface_Private_QWaylandWindowCall7 call = reinterpret_cast<CuteQNativeInterface_Private_QWaylandWindowCall7>(taken[7]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQNativeInterface_Private_QWaylandWindowCall8 call = reinterpret_cast<CuteQNativeInterface_Private_QWaylandWindowCall8>(taken[8]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQNativeInterface_Private_QWaylandWindowCall9 call = reinterpret_cast<CuteQNativeInterface_Private_QWaylandWindowCall9>(taken[9]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[10]) {
      int handled = 0;
      CuteQNativeInterface_Private_QWaylandWindowCall10 call = reinterpret_cast<CuteQNativeInterface_Private_QWaylandWindowCall10>(taken[10]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[11]) {
      int handled = 0;
      CuteQNativeInterface_Private_QWaylandWindowCall11 call = reinterpret_cast<CuteQNativeInterface_Private_QWaylandWindowCall11>(taken[11]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject
//      *QNativeInterface::Private::QWaylandWindow::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16QNativeInterface7Private14QWaylandWindow10metaObjectEv(
    const QNativeInterface::Private::QWaylandWindow *self) {
  return self->metaObject();
}

//  QString QNativeInterface::Private::QWaylandWindow::tr(const char *s,
//      const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QNativeInterface7Private14QWaylandWindow2trEPKcS3_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QNativeInterface::Private::QWaylandWindow::tr(s, c, n));
}

//  QNativeInterface::Private::QWaylandWindow::~QWaylandWindow()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QNativeInterface7Private14QWaylandWindowD1Ev(
    QNativeInterface::Private::QWaylandWindow *self) {
  delete self;
}

//  void QNativeInterface::Private::QWaylandWindow::setCustomMargins(const
//      QMargins &margins)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QNativeInterface7Private14QWaylandWindow16setCustomMarginsERK8QMargins(
    QNativeInterface::Private::QWaylandWindow *self,
    const QMargins *margins) {
  self->setCustomMargins(*margins);
}

//  void
//      QNativeInterface::Private::QWaylandWindow::requestXdgActivationToken(
//      uint serial)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QNativeInterface7Private14QWaylandWindow25requestXdgActivationTokenEj(
    QNativeInterface::Private::QWaylandWindow *self,
    uint serial) {
  self->requestXdgActivationToken(serial);
}

//  void QNativeInterface::Private::QWaylandWindow::setSessionRestoreId(const
//      QString &role)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QNativeInterface7Private14QWaylandWindow19setSessionRestoreIdERK7QString(
    QNativeInterface::Private::QWaylandWindow *self,
    const QString *role) {
  self->setSessionRestoreId(*role);
}

//  void QNativeInterface::Private::QWaylandWindow::setExtendedWindowType(Win
//      dowType windowType)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QNativeInterface7Private14QWaylandWindow21setExtendedWindowTypeENS1_10WindowTypeE(
    QNativeInterface::Private::QWaylandWindow *self,
    QNativeInterface::Private::QWaylandWindow::WindowType windowType) {
  self->setExtendedWindowType(windowType);
}

//  void
//      QNativeInterface::Private::QWaylandWindow::setParentControlGeometry(c
//      onst QRect &parentAnchor)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QNativeInterface7Private14QWaylandWindow24setParentControlGeometryERK5QRect(
    QNativeInterface::Private::QWaylandWindow *self,
    const QRect *parentAnchor) {
  self->setParentControlGeometry(*parentAnchor);
}

//  a Python function taken by a CuteQNativeInterface_Private_QWaylandWindow,
//      for the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QNativeInterface_Private_QWaylandWindow(
    QNativeInterface::Private::QWaylandWindow *self,
    const char *key,
    void *call) {
  return static_cast<CuteQNativeInterface_Private_QWaylandWindow *>(self)->take(key, call);
}

#endif  // QT_CONFIG(wayland)
