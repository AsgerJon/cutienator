//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickinputmethod_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuick/qtquickglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#if QT_CONFIG(im)
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickinputmethod_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>
#include <QtGui/qtransform.h>
#include <QtCore/qlocale.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QQuickInputMethod that Python can take functions over in. Every QQuickInputMethod
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickInputMethodCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickInputMethodCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickInputMethodCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickInputMethodCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickInputMethodCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickInputMethodCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickInputMethodCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickInputMethod : public QQuickInputMethod {
public:
  using QQuickInputMethod::QQuickInputMethod;
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
      CuteQQuickInputMethodCall0 call = reinterpret_cast<CuteQQuickInputMethodCall0>(taken[0]);
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
      CuteQQuickInputMethodCall1 call = reinterpret_cast<CuteQQuickInputMethodCall1>(taken[1]);
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
      CuteQQuickInputMethodCall2 call = reinterpret_cast<CuteQQuickInputMethodCall2>(taken[2]);
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
      CuteQQuickInputMethodCall3 call = reinterpret_cast<CuteQQuickInputMethodCall3>(taken[3]);
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
      CuteQQuickInputMethodCall4 call = reinterpret_cast<CuteQQuickInputMethodCall4>(taken[4]);
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
      CuteQQuickInputMethodCall5 call = reinterpret_cast<CuteQQuickInputMethodCall5>(taken[5]);
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
      CuteQQuickInputMethodCall6 call = reinterpret_cast<CuteQQuickInputMethodCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickInputMethod::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QQuickInputMethod10metaObjectEv(
    const QQuickInputMethod *self) {
  return self->metaObject();
}

//  void *QQuickInputMethod::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN17QQuickInputMethod11qt_metacastEPKc(
    QQuickInputMethod *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickInputMethod::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN17QQuickInputMethod11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickInputMethod *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickInputMethod::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QQuickInputMethod2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickInputMethod::tr(s, c, n));
}

//  void QQuickInputMethod::qt_qmlMarker_singleton()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickInputMethod22qt_qmlMarker_singletonEv(
    QQuickInputMethod *self) {
  self->qt_qmlMarker_singleton();
}

//  QQuickInputMethod::QQuickInputMethod(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickInputMethod *ritual_ZN17QQuickInputMethodC1EP7QObject(
    QObject *parent) {
  return new CuteQQuickInputMethod(parent);
}

//  QRectF QQuickInputMethod::anchorRectangle() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK17QQuickInputMethod15anchorRectangleEv(
    const QQuickInputMethod *self) {
  return new QRectF(self->anchorRectangle());
}

//  QRectF QQuickInputMethod::cursorRectangle() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK17QQuickInputMethod15cursorRectangleEv(
    const QQuickInputMethod *self) {
  return new QRectF(self->cursorRectangle());
}

//  Qt::LayoutDirection QQuickInputMethod::inputDirection() const
extern "C" Q_DECL_EXPORT
Qt::LayoutDirection ritual_ZNK17QQuickInputMethod14inputDirectionEv(
    const QQuickInputMethod *self) {
  return self->inputDirection();
}

//  QRectF QQuickInputMethod::inputItemClipRectangle() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK17QQuickInputMethod22inputItemClipRectangleEv(
    const QQuickInputMethod *self) {
  return new QRectF(self->inputItemClipRectangle());
}

//  QRectF QQuickInputMethod::inputItemRectangle() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK17QQuickInputMethod18inputItemRectangleEv(
    const QQuickInputMethod *self) {
  return new QRectF(self->inputItemRectangle());
}

//  void QQuickInputMethod::setInputItemRectangle(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickInputMethod21setInputItemRectangleERK6QRectF(
    QQuickInputMethod *self,
    const QRectF *rect) {
  self->setInputItemRectangle(*rect);
}

//  QTransform QQuickInputMethod::inputItemTransform() const
extern "C" Q_DECL_EXPORT
QTransform *ritual_ZNK17QQuickInputMethod18inputItemTransformEv(
    const QQuickInputMethod *self) {
  return new QTransform(self->inputItemTransform());
}

//  void QQuickInputMethod::setInputItemTransform(const QTransform
//      &transform)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickInputMethod21setInputItemTransformERK10QTransform(
    QQuickInputMethod *self,
    const QTransform *transform) {
  self->setInputItemTransform(*transform);
}

//  bool QQuickInputMethod::isAnimating() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QQuickInputMethod11isAnimatingEv(
    const QQuickInputMethod *self) {
  return self->isAnimating();
}

//  bool QQuickInputMethod::isVisible() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QQuickInputMethod9isVisibleEv(
    const QQuickInputMethod *self) {
  return self->isVisible();
}

//  void QQuickInputMethod::setVisible(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickInputMethod10setVisibleEb(
    QQuickInputMethod *self,
    bool visible) {
  self->setVisible(visible);
}

//  QRectF QQuickInputMethod::keyboardRectangle() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK17QQuickInputMethod17keyboardRectangleEv(
    const QQuickInputMethod *self) {
  return new QRectF(self->keyboardRectangle());
}

//  QLocale QQuickInputMethod::locale() const
extern "C" Q_DECL_EXPORT
QLocale *ritual_ZNK17QQuickInputMethod6localeEv(
    const QQuickInputMethod *self) {
  return new QLocale(self->locale());
}

//  void QQuickInputMethod::anchorRectangleChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickInputMethod22anchorRectangleChangedEv(
    QQuickInputMethod *self) {
  self->anchorRectangleChanged();
}

//  void QQuickInputMethod::animatingChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickInputMethod16animatingChangedEv(
    QQuickInputMethod *self) {
  self->animatingChanged();
}

//  void QQuickInputMethod::cursorRectangleChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickInputMethod22cursorRectangleChangedEv(
    QQuickInputMethod *self) {
  self->cursorRectangleChanged();
}

//  void QQuickInputMethod::inputDirectionChanged(Qt::LayoutDirection
//      newDirection)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickInputMethod21inputDirectionChangedEN2Qt15LayoutDirectionE(
    QQuickInputMethod *self,
    Qt::LayoutDirection newDirection) {
  self->inputDirectionChanged(newDirection);
}

//  void QQuickInputMethod::inputItemClipRectangleChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickInputMethod29inputItemClipRectangleChangedEv(
    QQuickInputMethod *self) {
  self->inputItemClipRectangleChanged();
}

//  void QQuickInputMethod::keyboardRectangleChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickInputMethod24keyboardRectangleChangedEv(
    QQuickInputMethod *self) {
  self->keyboardRectangleChanged();
}

//  void QQuickInputMethod::localeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickInputMethod13localeChangedEv(QQuickInputMethod *self) {
  self->localeChanged();
}

//  void QQuickInputMethod::visibleChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickInputMethod14visibleChangedEv(
    QQuickInputMethod *self) {
  self->visibleChanged();
}

//  void QQuickInputMethod::commit()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickInputMethod6commitEv(QQuickInputMethod *self) {
  self->commit();
}

//  void QQuickInputMethod::hide()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickInputMethod4hideEv(QQuickInputMethod *self) {
  self->hide();
}

//  void QQuickInputMethod::invokeAction(QInputMethod::Action a, int
//      cursorPosition)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickInputMethod12invokeActionEN12QInputMethod6ActionEi(
    QQuickInputMethod *self,
    QInputMethod::Action a,
    int cursorPosition) {
  self->invokeAction(a, cursorPosition);
}

//  void QQuickInputMethod::reset()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickInputMethod5resetEv(QQuickInputMethod *self) {
  self->reset();
}

//  void QQuickInputMethod::show()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickInputMethod4showEv(QQuickInputMethod *self) {
  self->show();
}

//  void QQuickInputMethod::update(Qt::InputMethodQueries queries)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickInputMethod6updateE6QFlagsIN2Qt16InputMethodQueryEE(
    QQuickInputMethod *self,
    int queries) {
  self->update(QFlags<Qt::InputMethodQuery>::fromInt(queries));
}

//  a Python function taken by a CuteQQuickInputMethod, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickInputMethod(
    QQuickInputMethod *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickInputMethod *>(self)->take(key, call);
}

#endif  // QT_CONFIG(im)
