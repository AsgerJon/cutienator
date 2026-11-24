//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickrangeslider_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickrangeslider_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QQuickRangeSliderNode that Python can take functions over in. Every QQuickRangeSliderNode
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickRangeSliderNodeCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickRangeSliderNodeCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickRangeSliderNodeCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickRangeSliderNodeCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickRangeSliderNodeCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickRangeSliderNodeCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickRangeSliderNodeCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickRangeSliderNode : public QQuickRangeSliderNode {
public:
  using QQuickRangeSliderNode::QQuickRangeSliderNode;
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
      CuteQQuickRangeSliderNodeCall0 call = reinterpret_cast<CuteQQuickRangeSliderNodeCall0>(taken[0]);
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
      CuteQQuickRangeSliderNodeCall1 call = reinterpret_cast<CuteQQuickRangeSliderNodeCall1>(taken[1]);
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
      CuteQQuickRangeSliderNodeCall2 call = reinterpret_cast<CuteQQuickRangeSliderNodeCall2>(taken[2]);
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
      CuteQQuickRangeSliderNodeCall3 call = reinterpret_cast<CuteQQuickRangeSliderNodeCall3>(taken[3]);
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
      CuteQQuickRangeSliderNodeCall4 call = reinterpret_cast<CuteQQuickRangeSliderNodeCall4>(taken[4]);
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
      CuteQQuickRangeSliderNodeCall5 call = reinterpret_cast<CuteQQuickRangeSliderNodeCall5>(taken[5]);
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
      CuteQQuickRangeSliderNodeCall6 call = reinterpret_cast<CuteQQuickRangeSliderNodeCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickRangeSliderNode::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK21QQuickRangeSliderNode10metaObjectEv(
    const QQuickRangeSliderNode *self) {
  return self->metaObject();
}

//  QString QQuickRangeSliderNode::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN21QQuickRangeSliderNode2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickRangeSliderNode::tr(s, c, n));
}

//  void QQuickRangeSliderNode::qt_qmlMarker_anonymous()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickRangeSliderNode22qt_qmlMarker_anonymousEv(
    QQuickRangeSliderNode *self) {
  self->qt_qmlMarker_anonymous();
}

//  QQuickRangeSliderNode::QQuickRangeSliderNode(qreal value,
//      QQuickRangeSlider *slider)
extern "C" Q_DECL_EXPORT
QQuickRangeSliderNode *ritual_ZN21QQuickRangeSliderNodeC1EdP17QQuickRangeSlider(
    qreal value,
    QQuickRangeSlider *slider) {
  return new CuteQQuickRangeSliderNode(value, slider);
}

//  QQuickRangeSliderNode::~QQuickRangeSliderNode()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickRangeSliderNodeD1Ev(QQuickRangeSliderNode *self) {
  delete self;
}

//  qreal QQuickRangeSliderNode::value() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK21QQuickRangeSliderNode5valueEv(
    const QQuickRangeSliderNode *self) {
  return self->value();
}

//  void QQuickRangeSliderNode::setValue(qreal value)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickRangeSliderNode8setValueEd(
    QQuickRangeSliderNode *self,
    qreal value) {
  self->setValue(value);
}

//  qreal QQuickRangeSliderNode::position() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK21QQuickRangeSliderNode8positionEv(
    const QQuickRangeSliderNode *self) {
  return self->position();
}

//  qreal QQuickRangeSliderNode::visualPosition() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK21QQuickRangeSliderNode14visualPositionEv(
    const QQuickRangeSliderNode *self) {
  return self->visualPosition();
}

//  QQuickItem *QQuickRangeSliderNode::handle() const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZNK21QQuickRangeSliderNode6handleEv(
    const QQuickRangeSliderNode *self) {
  return self->handle();
}

//  void QQuickRangeSliderNode::setHandle(QQuickItem *handle)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickRangeSliderNode9setHandleEP10QQuickItem(
    QQuickRangeSliderNode *self,
    QQuickItem *handle) {
  self->setHandle(handle);
}

//  bool QQuickRangeSliderNode::isPressed() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QQuickRangeSliderNode9isPressedEv(
    const QQuickRangeSliderNode *self) {
  return self->isPressed();
}

//  void QQuickRangeSliderNode::setPressed(bool pressed)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickRangeSliderNode10setPressedEb(
    QQuickRangeSliderNode *self,
    bool pressed) {
  self->setPressed(pressed);
}

//  bool QQuickRangeSliderNode::isHovered() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QQuickRangeSliderNode9isHoveredEv(
    const QQuickRangeSliderNode *self) {
  return self->isHovered();
}

//  void QQuickRangeSliderNode::setHovered(bool hovered)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickRangeSliderNode10setHoveredEb(
    QQuickRangeSliderNode *self,
    bool hovered) {
  self->setHovered(hovered);
}

//  qreal QQuickRangeSliderNode::implicitHandleWidth() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK21QQuickRangeSliderNode19implicitHandleWidthEv(
    const QQuickRangeSliderNode *self) {
  return self->implicitHandleWidth();
}

//  qreal QQuickRangeSliderNode::implicitHandleHeight() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK21QQuickRangeSliderNode20implicitHandleHeightEv(
    const QQuickRangeSliderNode *self) {
  return self->implicitHandleHeight();
}

//  void QQuickRangeSliderNode::increase()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickRangeSliderNode8increaseEv(
    QQuickRangeSliderNode *self) {
  self->increase();
}

//  void QQuickRangeSliderNode::decrease()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickRangeSliderNode8decreaseEv(
    QQuickRangeSliderNode *self) {
  self->decrease();
}

//  void QQuickRangeSliderNode::updateHandleCrossing()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickRangeSliderNode20updateHandleCrossingEv(
    QQuickRangeSliderNode *self) {
  self->updateHandleCrossing();
}

//  a Python function taken by a CuteQQuickRangeSliderNode, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickRangeSliderNode(
    QQuickRangeSliderNode *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickRangeSliderNode *>(self)->take(key, call);
}
