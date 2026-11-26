//  Written by dev_tooling.RitualGenerator from the records of
//  QtSvg/6.12.0/QtSvg/private/qsvganimatedproperty_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtSvg/6.12.0/QtSvg/private/qtsvgglobal_p.h>
#include <QtSvg/QtSvg>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSvg/6.12.0/QtSvg/private/qsvganimatedproperty_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <cstring>
#include <QtCore/QList>

//  A QSvgAnimatedPropertyTransform that Python can take functions over in. Every QSvgAnimatedPropertyTransform
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQSvgAnimatedPropertyTransformCall0)(const void *, uint, qreal, int *);
class CuteQSvgAnimatedPropertyTransform : public QSvgAnimatedPropertyTransform {
public:
  using QSvgAnimatedPropertyTransform::QSvgAnimatedPropertyTransform;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK28QSvgAbstractAnimatedProperty11interpolateEjd")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  void QSvgAnimatedPropertyTransform::interpolate(uint index, qreal t)
  //      const
  void interpolate(uint index, qreal t) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQSvgAnimatedPropertyTransformCall0 call = reinterpret_cast<CuteQSvgAnimatedPropertyTransformCall0>(taken[0]);
      call(this, index, t, &handled);
      if (handled) return;
    }
    QSvgAnimatedPropertyTransform::interpolate(index, t);
  }
};

//  QSvgAnimatedPropertyTransform::QSvgAnimatedPropertyTransform(const
//      QString &name)
extern "C" Q_DECL_EXPORT
QSvgAnimatedPropertyTransform *ritual_ZN29QSvgAnimatedPropertyTransformC1ERK7QString(
    const QString *name) {
  return new CuteQSvgAnimatedPropertyTransform(*name);
}

//  QSvgAnimatedPropertyTransform::~QSvgAnimatedPropertyTransform()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QSvgAnimatedPropertyTransformD1Ev(
    QSvgAnimatedPropertyTransform *self) {
  delete self;
}

//  void QSvgAnimatedPropertyTransform::setTransformCount(quint32 count)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QSvgAnimatedPropertyTransform17setTransformCountEj(
    QSvgAnimatedPropertyTransform *self,
    quint32 count) {
  self->setTransformCount(count);
}

//  quint32 QSvgAnimatedPropertyTransform::transformCount() const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK29QSvgAnimatedPropertyTransform14transformCountEv(
    const QSvgAnimatedPropertyTransform *self) {
  return self->transformCount();
}

//  void QSvgAnimatedPropertyTransform::appendComponents(const
//      QList<TransformComponent> &components)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QSvgAnimatedPropertyTransform16appendComponentsERK5QListINS_18TransformComponentEE(
    QSvgAnimatedPropertyTransform *self,
    const QList<QSvgAnimatedPropertyTransform::TransformComponent> *components) {
  self->appendComponents(*components);
}

//  QList<TransformComponent> QSvgAnimatedPropertyTransform::components()
//      const
extern "C" Q_DECL_EXPORT
QList<QSvgAnimatedPropertyTransform::TransformComponent> *ritual_ZNK29QSvgAnimatedPropertyTransform10componentsEv(
    const QSvgAnimatedPropertyTransform *self) {
  return new QList<QSvgAnimatedPropertyTransform::TransformComponent>(
      self->components());
}

//  void QSvgAnimatedPropertyTransform::interpolate(uint index, qreal t)
//      const
extern "C" Q_DECL_EXPORT
void ritual_ZNK29QSvgAnimatedPropertyTransform11interpolateEjd(
    const QSvgAnimatedPropertyTransform *self,
    uint index,
    qreal t) {
  self->interpolate(index, t);
}

//  a Python function taken by a CuteQSvgAnimatedPropertyTransform, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSvgAnimatedPropertyTransform(
    QSvgAnimatedPropertyTransform *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSvgAnimatedPropertyTransform *>(self)->take(key, call);
}

//  void QSvgAnimatedPropertyTransform::interpolate(uint index, qreal t)
//      const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK29QSvgAnimatedPropertyTransform11interpolateEjd(
    const QSvgAnimatedPropertyTransform *self,
    uint index,
    qreal t) {
  self->QSvgAnimatedPropertyTransform::interpolate(index, t);
}

//  a QList<QSvgAnimatedPropertyTransform::TransformComponent> a ritual of
//      QSvgAnimatedPropertyTransform gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QSvgAnimatedPropertyTransform__QList_QSvgAnimatedPropertyTransform_TransformComponent(
    QList<QSvgAnimatedPropertyTransform::TransformComponent> *self) {
  delete self;
}
