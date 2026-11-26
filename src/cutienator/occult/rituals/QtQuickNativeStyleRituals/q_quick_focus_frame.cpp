//  Written by hand on 2026-11-25 from
//  QtQuickNativeStyle/6.12.0/QtQuickNativeStyle/private/qquickfocusframe_p.h,
//  Qt 6.12.0, from Qt's source. Kept as it is when the generator runs
//  again.
//  Qt builds QuickNativeStyle for macOS and Windows only, so the whole
//  file stands under that. The class is abstract: its one virtual
//  function 'createFocusFrame' is private and pure, so Qt has no
//  function of its own for it and there is no 'own_' ritual. Without a
//  Python function taken for it, it gives a null pointer. The
//  destructor is the implicit one, written as 'delete self'.
//  Not written: 'qt_metacast', the private static 'm_focusFrame' and
//  the static 'Invalid' of the description. No file of QtWidgets is
//  included, as 'QStyle' would then be ambiguous in the headers of
//  this part.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if defined(Q_OS_MACOS) || defined(Q_OS_WIN)
#include <QtQuickNativeStyle/qtquicknativestyleexports.h>
#include <QtQuickNativeStyle/6.12.0/QtQuickNativeStyle/private/qquickfocusframe_p.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QQuickFocusFrame that Python can take functions over in. Every
//  QQuickFocusFrame Python makes is one. Each function below asks the
//  Python function handed over for it, and runs Qt's own without one.
typedef QQuickItem *(*CuteQQuickFocusFrameCall0)(const void *, QQmlContext *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickFocusFrameCall1)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickFocusFrameCall2)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickFocusFrameCall3)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickFocusFrameCall4)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickFocusFrameCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickFocusFrameCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickFocusFrameCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickFocusFrame : public QQuickFocusFrame {
public:
  using QQuickFocusFrame::QQuickFocusFrame;
  void *taken[8] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN16QQuickFocusFrame16createFocusFrameEP11QQmlContext")) {
      taken[0] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  QQuickItem *QQuickFocusFrame::createFocusFrame(QQmlContext *context)
  QQuickItem *createFocusFrame(QQmlContext *context) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickFocusFrameCall0 call = reinterpret_cast<CuteQQuickFocusFrameCall0>(taken[0]);
      QQuickItem *given = call(this, context, &handled);
      if (handled) return given;
    }
    return {};
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickFocusFrameCall1 call = reinterpret_cast<CuteQQuickFocusFrameCall1>(taken[1]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickFocusFrameCall2 call = reinterpret_cast<CuteQQuickFocusFrameCall2>(taken[2]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickFocusFrameCall3 call = reinterpret_cast<CuteQQuickFocusFrameCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickFocusFrameCall4 call = reinterpret_cast<CuteQQuickFocusFrameCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickFocusFrameCall5 call = reinterpret_cast<CuteQQuickFocusFrameCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickFocusFrameCall6 call = reinterpret_cast<CuteQQuickFocusFrameCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickFocusFrameCall7 call = reinterpret_cast<CuteQQuickFocusFrameCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickFocusFrame::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16QQuickFocusFrame10metaObjectEv(
    const QQuickFocusFrame *self) {
  return self->metaObject();
}

//  QString QQuickFocusFrame::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QQuickFocusFrame2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickFocusFrame::tr(s, c, n));
}

//  QQuickFocusFrame::QQuickFocusFrame()
extern "C" Q_DECL_EXPORT
QQuickFocusFrame *ritual_ZN16QQuickFocusFrameC1Ev() {
  return new CuteQQuickFocusFrame();
}

//  QQuickFocusFrame::~QQuickFocusFrame()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickFocusFrameD1Ev(QQuickFocusFrame *self) {
  delete self;
}

//  QQuickItem *QQuickFocusFrame::createFocusFrame(QQmlContext *context)
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZN16QQuickFocusFrame16createFocusFrameEP11QQmlContext(
    QQuickFocusFrame *self,
    QQmlContext *context) {
  return self->createFocusFrame(context);
}

//  void QQuickFocusFrame::moveToItem(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickFocusFrame10moveToItemEP10QQuickItem(
    QQuickFocusFrame *self,
    QQuickItem *item) {
  self->moveToItem(item);
}

//  QQuickFocusFrameDescription QQuickFocusFrame::getDescriptionForItem(
//      QQuickItem *focusItem) const
extern "C" Q_DECL_EXPORT
QQuickFocusFrameDescription *ritual_ZNK16QQuickFocusFrame21getDescriptionForItemEP10QQuickItem(
    const QQuickFocusFrame *self,
    QQuickItem *focusItem) {
  return new QQuickFocusFrameDescription(
      self->getDescriptionForItem(focusItem));
}

//  a Python function taken by a CuteQQuickFocusFrame, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickFocusFrame(
    QQuickFocusFrame *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickFocusFrame *>(self)->take(key, call);
}

#endif  // defined(Q_OS_MACOS) || defined(Q_OS_WIN)
