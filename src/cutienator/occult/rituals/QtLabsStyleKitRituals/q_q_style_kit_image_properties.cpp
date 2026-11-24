//  Written by dev_tooling.RitualGenerator from the records of QtLabsStyleKit
//  /6.12.0/QtLabsStyleKit/private/qqstylekitcontrolproperties_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekitglobal_p.h>
#include <QtLabsStyleKit/QtLabsStyleKit>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekitcontrolproperties_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#include <QtGui/qcolor.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QQStyleKitImageProperties that Python can take functions over in. Every QQStyleKitImageProperties
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQStyleKitImagePropertiesCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQStyleKitImagePropertiesCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQStyleKitImagePropertiesCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQStyleKitImagePropertiesCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQStyleKitImagePropertiesCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQStyleKitImagePropertiesCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQStyleKitImagePropertiesCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQStyleKitImageProperties : public QQStyleKitImageProperties {
public:
  using QQStyleKitImageProperties::QQStyleKitImageProperties;
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
      CuteQQStyleKitImagePropertiesCall0 call = reinterpret_cast<CuteQQStyleKitImagePropertiesCall0>(taken[0]);
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
      CuteQQStyleKitImagePropertiesCall1 call = reinterpret_cast<CuteQQStyleKitImagePropertiesCall1>(taken[1]);
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
      CuteQQStyleKitImagePropertiesCall2 call = reinterpret_cast<CuteQQStyleKitImagePropertiesCall2>(taken[2]);
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
      CuteQQStyleKitImagePropertiesCall3 call = reinterpret_cast<CuteQQStyleKitImagePropertiesCall3>(taken[3]);
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
      CuteQQStyleKitImagePropertiesCall4 call = reinterpret_cast<CuteQQStyleKitImagePropertiesCall4>(taken[4]);
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
      CuteQQStyleKitImagePropertiesCall5 call = reinterpret_cast<CuteQQStyleKitImagePropertiesCall5>(taken[5]);
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
      CuteQQStyleKitImagePropertiesCall6 call = reinterpret_cast<CuteQQStyleKitImagePropertiesCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQStyleKitImageProperties::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK25QQStyleKitImageProperties10metaObjectEv(
    const QQStyleKitImageProperties *self) {
  return self->metaObject();
}

//  QString QQStyleKitImageProperties::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN25QQStyleKitImageProperties2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQStyleKitImageProperties::tr(s, c, n));
}

//  void QQStyleKitImageProperties::qt_qmlMarker_uncreatable()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQStyleKitImageProperties24qt_qmlMarker_uncreatableEv(
    QQStyleKitImageProperties *self) {
  self->qt_qmlMarker_uncreatable();
}

//  QQStyleKitImageProperties::QQStyleKitImageProperties(QQSK::PropertyGroup
//      group, QQStyleKitControlProperties *parent)
extern "C" Q_DECL_EXPORT
QQStyleKitImageProperties *ritual_ZN25QQStyleKitImagePropertiesC1EN4QQSK13PropertyGroupEP27QQStyleKitControlProperties(
    QQSK::PropertyGroup group,
    QQStyleKitControlProperties *parent) {
  return new CuteQQStyleKitImageProperties(group, parent);
}

//  QUrl QQStyleKitImageProperties::source() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK25QQStyleKitImageProperties6sourceEv(
    const QQStyleKitImageProperties *self) {
  return new QUrl(self->source());
}

//  void QQStyleKitImageProperties::setSource(const QUrl &source)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQStyleKitImageProperties9setSourceERK4QUrl(
    QQStyleKitImageProperties *self,
    const QUrl *source) {
  self->setSource(*source);
}

//  QColor QQStyleKitImageProperties::color() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK25QQStyleKitImageProperties5colorEv(
    const QQStyleKitImageProperties *self) {
  return new QColor(self->color());
}

//  void QQStyleKitImageProperties::setColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQStyleKitImageProperties8setColorERK6QColor(
    QQStyleKitImageProperties *self,
    const QColor *color) {
  self->setColor(*color);
}

//  QQuickImage::FillMode QQStyleKitImageProperties::fillMode() const
extern "C" Q_DECL_EXPORT
QQuickImage::FillMode ritual_ZNK25QQStyleKitImageProperties8fillModeEv(
    const QQStyleKitImageProperties *self) {
  return self->fillMode();
}

//  void QQStyleKitImageProperties::setFillMode(QQuickImage::FillMode
//      fillMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQStyleKitImageProperties11setFillModeEN11QQuickImage8FillModeE(
    QQStyleKitImageProperties *self,
    QQuickImage::FillMode fillMode) {
  self->setFillMode(fillMode);
}

//  a Python function taken by a CuteQQStyleKitImageProperties, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQStyleKitImageProperties(
    QQStyleKitImageProperties *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQStyleKitImageProperties *>(self)->take(key, call);
}
