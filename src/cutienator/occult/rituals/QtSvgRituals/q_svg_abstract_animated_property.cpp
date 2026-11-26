//  Written by dev_tooling.RitualGenerator from the records of
//  QtSvg/6.12.0/QtSvg/private/qsvganimatedproperty_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtSvg/6.12.0/QtSvg/private/qtsvgglobal_p.h>
#include <QtSvg/QtSvg>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSvg/6.12.0/QtSvg/private/qsvganimatedproperty_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qstringview.h>
#include <QtCore/qvariant.h>
#include <QtCore/qlist.h>
#include <cstring>
#include <QtCore/QList>

//  A QSvgAbstractAnimatedProperty that Python can take functions over in. Every QSvgAbstractAnimatedProperty
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQSvgAbstractAnimatedPropertyCall0)(const void *, uint, qreal, int *);
class CuteQSvgAbstractAnimatedProperty : public QSvgAbstractAnimatedProperty {
public:
  using QSvgAbstractAnimatedProperty::QSvgAbstractAnimatedProperty;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK28QSvgAbstractAnimatedProperty11interpolateEjd")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  void QSvgAbstractAnimatedProperty::interpolate(uint index, qreal t)
  //      const
  void interpolate(uint index, qreal t) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQSvgAbstractAnimatedPropertyCall0 call = reinterpret_cast<CuteQSvgAbstractAnimatedPropertyCall0>(taken[0]);
      call(this, index, t, &handled);
      if (handled) return;
    }
  }
};

//  QSvgAbstractAnimatedProperty::QSvgAbstractAnimatedProperty(const QString
//      &name, Type type)
extern "C" Q_DECL_EXPORT
QSvgAbstractAnimatedProperty *ritual_ZN28QSvgAbstractAnimatedPropertyC1ERK7QStringNS_4TypeE(
    const QString *name,
    QSvgAbstractAnimatedProperty::Type type) {
  return new CuteQSvgAbstractAnimatedProperty(*name, type);
}

//  QSvgAbstractAnimatedProperty::~QSvgAbstractAnimatedProperty()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QSvgAbstractAnimatedPropertyD1Ev(
    QSvgAbstractAnimatedProperty *self) {
  delete self;
}

//  void QSvgAbstractAnimatedProperty::setKeyFrames(const QList<qreal>
//      &keyFrames)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QSvgAbstractAnimatedProperty12setKeyFramesERK5QListIdE(
    QSvgAbstractAnimatedProperty *self,
    const QList<qreal> *keyFrames) {
  self->setKeyFrames(*keyFrames);
}

//  void QSvgAbstractAnimatedProperty::appendKeyFrame(qreal keyFrame)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QSvgAbstractAnimatedProperty14appendKeyFrameEd(
    QSvgAbstractAnimatedProperty *self,
    qreal keyFrame) {
  self->appendKeyFrame(keyFrame);
}

//  QList<qreal> QSvgAbstractAnimatedProperty::keyFrames() const
extern "C" Q_DECL_EXPORT
QList<qreal> *ritual_ZNK28QSvgAbstractAnimatedProperty9keyFramesEv(
    const QSvgAbstractAnimatedProperty *self) {
  return new QList<qreal>(self->keyFrames());
}

//  const QSvgEasingInterface
//      *QSvgAbstractAnimatedProperty::easingAt(unsigned int i) const
extern "C" Q_DECL_EXPORT
const QSvgEasingInterface *ritual_ZNK28QSvgAbstractAnimatedProperty8easingAtEj(
    const QSvgAbstractAnimatedProperty *self,
    unsigned int i) {
  return self->easingAt(i);
}

//  void QSvgAbstractAnimatedProperty::setPropertyName(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QSvgAbstractAnimatedProperty15setPropertyNameERK7QString(
    QSvgAbstractAnimatedProperty *self,
    const QString *name) {
  self->setPropertyName(*name);
}

//  QStringView QSvgAbstractAnimatedProperty::propertyName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK28QSvgAbstractAnimatedProperty12propertyNameEv(
    const QSvgAbstractAnimatedProperty *self) {
  return new QString(self->propertyName().toString());
}

//  Type QSvgAbstractAnimatedProperty::type() const
extern "C" Q_DECL_EXPORT
QSvgAbstractAnimatedProperty::Type ritual_ZNK28QSvgAbstractAnimatedProperty4typeEv(
    const QSvgAbstractAnimatedProperty *self) {
  return self->type();
}

//  QVariant QSvgAbstractAnimatedProperty::interpolatedValue() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK28QSvgAbstractAnimatedProperty17interpolatedValueEv(
    const QSvgAbstractAnimatedProperty *self) {
  return new QVariant(self->interpolatedValue());
}

//  void QSvgAbstractAnimatedProperty::interpolate(uint index, qreal t) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK28QSvgAbstractAnimatedProperty11interpolateEjd(
    const QSvgAbstractAnimatedProperty *self,
    uint index,
    qreal t) {
  self->interpolate(index, t);
}

//  QSvgAbstractAnimatedProperty
//      *QSvgAbstractAnimatedProperty::createAnimatedProperty(const QString
//      &name)
extern "C" Q_DECL_EXPORT
QSvgAbstractAnimatedProperty *ritual_ZN28QSvgAbstractAnimatedProperty22createAnimatedPropertyERK7QString(
    const QString *name) {
  return QSvgAbstractAnimatedProperty::createAnimatedProperty(*name);
}

//  a Python function taken by a CuteQSvgAbstractAnimatedProperty, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSvgAbstractAnimatedProperty(
    QSvgAbstractAnimatedProperty *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSvgAbstractAnimatedProperty *>(self)->take(key, call);
}

//  QList<QSvgAbstractAnimatedProperty *>::QList()
extern "C" Q_DECL_EXPORT
QList<QSvgAbstractAnimatedProperty *> *ritual_list_make_QSvgAbstractAnimatedProperty_ptr() {
  return new QList<QSvgAbstractAnimatedProperty *>();
}

//  void QList<QSvgAbstractAnimatedProperty *>::append(const
//      QSvgAbstractAnimatedProperty * &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QSvgAbstractAnimatedProperty_ptr(
    QList<QSvgAbstractAnimatedProperty *> *self,
    QSvgAbstractAnimatedProperty *element) {
  self->append(element);
}

//  qsizetype QList<QSvgAbstractAnimatedProperty *>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QSvgAbstractAnimatedProperty_ptr(
    const QList<QSvgAbstractAnimatedProperty *> *self) {
  return self->size();
}

//  const QSvgAbstractAnimatedProperty * &QList<QSvgAbstractAnimatedProperty
//      *>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QSvgAbstractAnimatedProperty *ritual_list_at_QSvgAbstractAnimatedProperty_ptr(
    const QList<QSvgAbstractAnimatedProperty *> *self,
    long long index) {
  return self->at(index);
}

//  QList<QSvgAbstractAnimatedProperty *>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QSvgAbstractAnimatedProperty_ptr(
    QList<QSvgAbstractAnimatedProperty *> *self) {
  delete self;
}

//  a QList<qreal> a ritual of QSvgAbstractAnimatedProperty gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QSvgAbstractAnimatedProperty__QList_qreal(
    QList<qreal> *self) {
  delete self;
}
