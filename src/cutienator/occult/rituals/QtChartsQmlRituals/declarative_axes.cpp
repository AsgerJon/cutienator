//  Written by dev_tooling.RitualGenerator from the records of
//  QtChartsQml/6.12.0/QtChartsQml/private/declarativeaxes_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtChartsQml/6.12.0/QtChartsQml/private/declarativechartglobal_p.h>
#include <QtChartsQml/QtChartsQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtChartsQml/6.12.0/QtChartsQml/private/declarativeaxes_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  const QMetaObject *DeclarativeAxes::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15DeclarativeAxes10metaObjectEv(
    const DeclarativeAxes *self) {
  return self->metaObject();
}

//  QString DeclarativeAxes::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15DeclarativeAxes2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(DeclarativeAxes::tr(s, c, n));
}

//  void DeclarativeAxes::qt_qmlMarker_uncreatable()
extern "C" Q_DECL_EXPORT
void ritual_ZN15DeclarativeAxes24qt_qmlMarker_uncreatableEv(
    DeclarativeAxes *self) {
  self->qt_qmlMarker_uncreatable();
}

//  DeclarativeAxes::DeclarativeAxes(QObject *parent)
extern "C" Q_DECL_EXPORT
DeclarativeAxes *ritual_ZN15DeclarativeAxesC1EP7QObject(QObject *parent) {
  return new DeclarativeAxes(parent);
}

//  QAbstractAxis *DeclarativeAxes::axisX()
extern "C" Q_DECL_EXPORT
QAbstractAxis *ritual_ZN15DeclarativeAxes5axisXEv(DeclarativeAxes *self) {
  return self->axisX();
}

//  void DeclarativeAxes::setAxisX(QAbstractAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN15DeclarativeAxes8setAxisXEP13QAbstractAxis(
    DeclarativeAxes *self,
    QAbstractAxis *axis) {
  self->setAxisX(axis);
}

//  QAbstractAxis *DeclarativeAxes::axisY()
extern "C" Q_DECL_EXPORT
QAbstractAxis *ritual_ZN15DeclarativeAxes5axisYEv(DeclarativeAxes *self) {
  return self->axisY();
}

//  void DeclarativeAxes::setAxisY(QAbstractAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN15DeclarativeAxes8setAxisYEP13QAbstractAxis(
    DeclarativeAxes *self,
    QAbstractAxis *axis) {
  self->setAxisY(axis);
}

//  QAbstractAxis *DeclarativeAxes::axisXTop()
extern "C" Q_DECL_EXPORT
QAbstractAxis *ritual_ZN15DeclarativeAxes8axisXTopEv(DeclarativeAxes *self) {
  return self->axisXTop();
}

//  void DeclarativeAxes::setAxisXTop(QAbstractAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN15DeclarativeAxes11setAxisXTopEP13QAbstractAxis(
    DeclarativeAxes *self,
    QAbstractAxis *axis) {
  self->setAxisXTop(axis);
}

//  QAbstractAxis *DeclarativeAxes::axisYRight()
extern "C" Q_DECL_EXPORT
QAbstractAxis *ritual_ZN15DeclarativeAxes10axisYRightEv(
    DeclarativeAxes *self) {
  return self->axisYRight();
}

//  void DeclarativeAxes::setAxisYRight(QAbstractAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN15DeclarativeAxes13setAxisYRightEP13QAbstractAxis(
    DeclarativeAxes *self,
    QAbstractAxis *axis) {
  self->setAxisYRight(axis);
}

//  void DeclarativeAxes::emitAxisXChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN15DeclarativeAxes16emitAxisXChangedEv(DeclarativeAxes *self) {
  self->emitAxisXChanged();
}

//  void DeclarativeAxes::emitAxisYChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN15DeclarativeAxes16emitAxisYChangedEv(DeclarativeAxes *self) {
  self->emitAxisYChanged();
}

//  void DeclarativeAxes::emitAxisXTopChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN15DeclarativeAxes19emitAxisXTopChangedEv(
    DeclarativeAxes *self) {
  self->emitAxisXTopChanged();
}

//  void DeclarativeAxes::emitAxisYRightChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN15DeclarativeAxes21emitAxisYRightChangedEv(
    DeclarativeAxes *self) {
  self->emitAxisYRightChanged();
}
