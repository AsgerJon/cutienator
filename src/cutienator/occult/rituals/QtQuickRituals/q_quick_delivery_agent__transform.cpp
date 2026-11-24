//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickdeliveryagent_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickdeliveryagent_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qpoint.h>
#include <cstring>

//  A QQuickDeliveryAgent::Transform that Python can take functions over in. Every QQuickDeliveryAgent::Transform
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QPointF * (*CuteQQuickDeliveryAgent_TransformCall0)(const void *, const QPointF *, int *);
class CuteQQuickDeliveryAgent_Transform : public QQuickDeliveryAgent::Transform {
public:
  using QQuickDeliveryAgent::Transform::Transform;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN19QQuickDeliveryAgent9Transform3mapERK7QPointF")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  QPointF QQuickDeliveryAgent::Transform::map(const QPointF &point)
  QPointF map(const QPointF &point) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickDeliveryAgent_TransformCall0 call = reinterpret_cast<CuteQQuickDeliveryAgent_TransformCall0>(taken[0]);
      const QPointF * given = call(this, &point, &handled);
      if (handled && given) return *given;
    }
    return {};
  }
};

//  QQuickDeliveryAgent::Transform::~Transform()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickDeliveryAgent9TransformD1Ev(
    QQuickDeliveryAgent::Transform *self) {
  delete self;
}

//  QPointF QQuickDeliveryAgent::Transform::map(const QPointF &point)
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZN19QQuickDeliveryAgent9Transform3mapERK7QPointF(
    QQuickDeliveryAgent::Transform *self,
    const QPointF *point) {
  return new QPointF(self->map(*point));
}

//  a Python function taken by a CuteQQuickDeliveryAgent_Transform, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickDeliveryAgent_Transform(
    QQuickDeliveryAgent::Transform *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickDeliveryAgent_Transform *>(self)->take(key, call);
}
