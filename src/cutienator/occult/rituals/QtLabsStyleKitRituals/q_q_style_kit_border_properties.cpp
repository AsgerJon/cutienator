//  Written by dev_tooling.RitualGenerator from the records of QtLabsStyleKit
//  /6.12.0/QtLabsStyleKit/private/qqstylekitcontrolproperties_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekitglobal_p.h>
#include <QtLabsStyleKit/QtLabsStyleKit>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekitcontrolproperties_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qcolor.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QQStyleKitBorderProperties that Python can take functions over in. Every QQStyleKitBorderProperties
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQStyleKitBorderPropertiesCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQStyleKitBorderPropertiesCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQStyleKitBorderPropertiesCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQStyleKitBorderPropertiesCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQStyleKitBorderPropertiesCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQStyleKitBorderPropertiesCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQStyleKitBorderPropertiesCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQStyleKitBorderProperties : public QQStyleKitBorderProperties {
public:
  using QQStyleKitBorderProperties::QQStyleKitBorderProperties;
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
      CuteQQStyleKitBorderPropertiesCall0 call = reinterpret_cast<CuteQQStyleKitBorderPropertiesCall0>(taken[0]);
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
      CuteQQStyleKitBorderPropertiesCall1 call = reinterpret_cast<CuteQQStyleKitBorderPropertiesCall1>(taken[1]);
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
      CuteQQStyleKitBorderPropertiesCall2 call = reinterpret_cast<CuteQQStyleKitBorderPropertiesCall2>(taken[2]);
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
      CuteQQStyleKitBorderPropertiesCall3 call = reinterpret_cast<CuteQQStyleKitBorderPropertiesCall3>(taken[3]);
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
      CuteQQStyleKitBorderPropertiesCall4 call = reinterpret_cast<CuteQQStyleKitBorderPropertiesCall4>(taken[4]);
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
      CuteQQStyleKitBorderPropertiesCall5 call = reinterpret_cast<CuteQQStyleKitBorderPropertiesCall5>(taken[5]);
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
      CuteQQStyleKitBorderPropertiesCall6 call = reinterpret_cast<CuteQQStyleKitBorderPropertiesCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQStyleKitBorderProperties::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK26QQStyleKitBorderProperties10metaObjectEv(
    const QQStyleKitBorderProperties *self) {
  return self->metaObject();
}

//  QString QQStyleKitBorderProperties::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN26QQStyleKitBorderProperties2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQStyleKitBorderProperties::tr(s, c, n));
}

//  void QQStyleKitBorderProperties::qt_qmlMarker_uncreatable()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQStyleKitBorderProperties24qt_qmlMarker_uncreatableEv(
    QQStyleKitBorderProperties *self) {
  self->qt_qmlMarker_uncreatable();
}

//  QQStyleKitBorderProperties::QQStyleKitBorderProperties(QQSK::PropertyGrou
//      p group, QQStyleKitControlProperties *parent)
extern "C" Q_DECL_EXPORT
QQStyleKitBorderProperties *ritual_ZN26QQStyleKitBorderPropertiesC1EN4QQSK13PropertyGroupEP27QQStyleKitControlProperties(
    QQSK::PropertyGroup group,
    QQStyleKitControlProperties *parent) {
  return new CuteQQStyleKitBorderProperties(group, parent);
}

//  qreal QQStyleKitBorderProperties::width() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK26QQStyleKitBorderProperties5widthEv(
    const QQStyleKitBorderProperties *self) {
  return self->width();
}

//  void QQStyleKitBorderProperties::setWidth(qreal width)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQStyleKitBorderProperties8setWidthEd(
    QQStyleKitBorderProperties *self,
    qreal width) {
  self->setWidth(width);
}

//  QColor QQStyleKitBorderProperties::color() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK26QQStyleKitBorderProperties5colorEv(
    const QQStyleKitBorderProperties *self) {
  return new QColor(self->color());
}

//  void QQStyleKitBorderProperties::setColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQStyleKitBorderProperties8setColorERK6QColor(
    QQStyleKitBorderProperties *self,
    const QColor *color) {
  self->setColor(*color);
}

//  a Python function taken by a CuteQQStyleKitBorderProperties, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQStyleKitBorderProperties(
    QQStyleKitBorderProperties *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQStyleKitBorderProperties *>(self)->take(key, call);
}
