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

//  A QQStyleKitShadowProperties that Python can take functions over in. Every QQStyleKitShadowProperties
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQStyleKitShadowPropertiesCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQStyleKitShadowPropertiesCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQStyleKitShadowPropertiesCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQStyleKitShadowPropertiesCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQStyleKitShadowPropertiesCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQStyleKitShadowPropertiesCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQStyleKitShadowPropertiesCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQStyleKitShadowProperties : public QQStyleKitShadowProperties {
public:
  using QQStyleKitShadowProperties::QQStyleKitShadowProperties;
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
      CuteQQStyleKitShadowPropertiesCall0 call = reinterpret_cast<CuteQQStyleKitShadowPropertiesCall0>(taken[0]);
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
      CuteQQStyleKitShadowPropertiesCall1 call = reinterpret_cast<CuteQQStyleKitShadowPropertiesCall1>(taken[1]);
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
      CuteQQStyleKitShadowPropertiesCall2 call = reinterpret_cast<CuteQQStyleKitShadowPropertiesCall2>(taken[2]);
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
      CuteQQStyleKitShadowPropertiesCall3 call = reinterpret_cast<CuteQQStyleKitShadowPropertiesCall3>(taken[3]);
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
      CuteQQStyleKitShadowPropertiesCall4 call = reinterpret_cast<CuteQQStyleKitShadowPropertiesCall4>(taken[4]);
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
      CuteQQStyleKitShadowPropertiesCall5 call = reinterpret_cast<CuteQQStyleKitShadowPropertiesCall5>(taken[5]);
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
      CuteQQStyleKitShadowPropertiesCall6 call = reinterpret_cast<CuteQQStyleKitShadowPropertiesCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQStyleKitShadowProperties::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK26QQStyleKitShadowProperties10metaObjectEv(
    const QQStyleKitShadowProperties *self) {
  return self->metaObject();
}

//  void *QQStyleKitShadowProperties::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN26QQStyleKitShadowProperties11qt_metacastEPKc(
    QQStyleKitShadowProperties *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQStyleKitShadowProperties::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN26QQStyleKitShadowProperties11qt_metacallEN11QMetaObject4CallEiPPv(
    QQStyleKitShadowProperties *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQStyleKitShadowProperties::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN26QQStyleKitShadowProperties2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQStyleKitShadowProperties::tr(s, c, n));
}

//  void QQStyleKitShadowProperties::qt_qmlMarker_uncreatable()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQStyleKitShadowProperties24qt_qmlMarker_uncreatableEv(
    QQStyleKitShadowProperties *self) {
  self->qt_qmlMarker_uncreatable();
}

//  QQStyleKitShadowProperties::QQStyleKitShadowProperties(QQSK::PropertyGrou
//      p group, QQStyleKitControlProperties *parent)
extern "C" Q_DECL_EXPORT
QQStyleKitShadowProperties *ritual_ZN26QQStyleKitShadowPropertiesC1EN4QQSK13PropertyGroupEP27QQStyleKitControlProperties(
    QQSK::PropertyGroup group,
    QQStyleKitControlProperties *parent) {
  return new CuteQQStyleKitShadowProperties(group, parent);
}

//  QColor QQStyleKitShadowProperties::color() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK26QQStyleKitShadowProperties5colorEv(
    const QQStyleKitShadowProperties *self) {
  return new QColor(self->color());
}

//  void QQStyleKitShadowProperties::setColor(QColor color)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQStyleKitShadowProperties8setColorE6QColor(
    QQStyleKitShadowProperties *self,
    const QColor *color) {
  self->setColor(*color);
}

//  qreal QQStyleKitShadowProperties::opacity() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK26QQStyleKitShadowProperties7opacityEv(
    const QQStyleKitShadowProperties *self) {
  return self->opacity();
}

//  void QQStyleKitShadowProperties::setOpacity(qreal opacity)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQStyleKitShadowProperties10setOpacityEd(
    QQStyleKitShadowProperties *self,
    qreal opacity) {
  self->setOpacity(opacity);
}

//  qreal QQStyleKitShadowProperties::scale() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK26QQStyleKitShadowProperties5scaleEv(
    const QQStyleKitShadowProperties *self) {
  return self->scale();
}

//  void QQStyleKitShadowProperties::setScale(qreal scale)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQStyleKitShadowProperties8setScaleEd(
    QQStyleKitShadowProperties *self,
    qreal scale) {
  self->setScale(scale);
}

//  qreal QQStyleKitShadowProperties::verticalOffset() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK26QQStyleKitShadowProperties14verticalOffsetEv(
    const QQStyleKitShadowProperties *self) {
  return self->verticalOffset();
}

//  void QQStyleKitShadowProperties::setVerticalOffset(qreal verticalOffset)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQStyleKitShadowProperties17setVerticalOffsetEd(
    QQStyleKitShadowProperties *self,
    qreal verticalOffset) {
  self->setVerticalOffset(verticalOffset);
}

//  qreal QQStyleKitShadowProperties::horizontalOffset() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK26QQStyleKitShadowProperties16horizontalOffsetEv(
    const QQStyleKitShadowProperties *self) {
  return self->horizontalOffset();
}

//  void QQStyleKitShadowProperties::setHorizontalOffset(qreal
//      horizontalOffset)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQStyleKitShadowProperties19setHorizontalOffsetEd(
    QQStyleKitShadowProperties *self,
    qreal horizontalOffset) {
  self->setHorizontalOffset(horizontalOffset);
}

//  qreal QQStyleKitShadowProperties::blur() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK26QQStyleKitShadowProperties4blurEv(
    const QQStyleKitShadowProperties *self) {
  return self->blur();
}

//  void QQStyleKitShadowProperties::setBlur(qreal blur)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQStyleKitShadowProperties7setBlurEd(
    QQStyleKitShadowProperties *self,
    qreal blur) {
  self->setBlur(blur);
}

//  bool QQStyleKitShadowProperties::visible() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK26QQStyleKitShadowProperties7visibleEv(
    const QQStyleKitShadowProperties *self) {
  return self->visible();
}

//  void QQStyleKitShadowProperties::setVisible(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQStyleKitShadowProperties10setVisibleEb(
    QQStyleKitShadowProperties *self,
    bool visible) {
  self->setVisible(visible);
}

//  QQmlComponent *QQStyleKitShadowProperties::delegate() const
extern "C" Q_DECL_EXPORT
QQmlComponent *ritual_ZNK26QQStyleKitShadowProperties8delegateEv(
    const QQStyleKitShadowProperties *self) {
  return self->delegate();
}

//  void QQStyleKitShadowProperties::setDelegate(QQmlComponent *delegate)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQStyleKitShadowProperties11setDelegateEP13QQmlComponent(
    QQStyleKitShadowProperties *self,
    QQmlComponent *delegate) {
  self->setDelegate(delegate);
}

//  void QQStyleKitShadowProperties::colorChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQStyleKitShadowProperties12colorChangedEv(
    QQStyleKitShadowProperties *self) {
  self->colorChanged();
}

//  void QQStyleKitShadowProperties::opacityChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQStyleKitShadowProperties14opacityChangedEv(
    QQStyleKitShadowProperties *self) {
  self->opacityChanged();
}

//  void QQStyleKitShadowProperties::scaleChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQStyleKitShadowProperties12scaleChangedEv(
    QQStyleKitShadowProperties *self) {
  self->scaleChanged();
}

//  void QQStyleKitShadowProperties::verticalOffsetChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQStyleKitShadowProperties21verticalOffsetChangedEv(
    QQStyleKitShadowProperties *self) {
  self->verticalOffsetChanged();
}

//  void QQStyleKitShadowProperties::horizontalOffsetChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQStyleKitShadowProperties23horizontalOffsetChangedEv(
    QQStyleKitShadowProperties *self) {
  self->horizontalOffsetChanged();
}

//  void QQStyleKitShadowProperties::blurChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQStyleKitShadowProperties11blurChangedEv(
    QQStyleKitShadowProperties *self) {
  self->blurChanged();
}

//  void QQStyleKitShadowProperties::visibleChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQStyleKitShadowProperties14visibleChangedEv(
    QQStyleKitShadowProperties *self) {
  self->visibleChanged();
}

//  void QQStyleKitShadowProperties::delegateChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQStyleKitShadowProperties15delegateChangedEv(
    QQStyleKitShadowProperties *self) {
  self->delegateChanged();
}

//  a Python function taken by a CuteQQStyleKitShadowProperties, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQStyleKitShadowProperties(
    QQStyleKitShadowProperties *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQStyleKitShadowProperties *>(self)->take(key, call);
}
