//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qbrush.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qbrush.h>
#include <QtGui/qcolor.h>
#include <QtCore/qlist.h>
#include <QtGui/QGradientStops>

//  QGradient::QGradient()
extern "C" Q_DECL_EXPORT
QGradient *ritual_ZN9QGradientC1Ev() {
  return new QGradient();
}

//  QGradient::QGradient(Preset a0)
extern "C" Q_DECL_EXPORT
QGradient *ritual_ZN9QGradientC1ENS_6PresetE(QGradient::Preset a0) {
  return new QGradient(a0);
}

//  QGradient::~QGradient()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QGradientD1Ev(QGradient *self) {
  delete self;
}

//  Type QGradient::type() const
extern "C" Q_DECL_EXPORT
QGradient::Type ritual_ZNK9QGradient4typeEv(const QGradient *self) {
  return self->type();
}

//  void QGradient::setSpread(Spread spread)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QGradient9setSpreadENS_6SpreadE(
    QGradient *self,
    QGradient::Spread spread) {
  self->setSpread(spread);
}

//  Spread QGradient::spread() const
extern "C" Q_DECL_EXPORT
QGradient::Spread ritual_ZNK9QGradient6spreadEv(const QGradient *self) {
  return self->spread();
}

//  void QGradient::setColorAt(qreal pos, const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QGradient10setColorAtEdRK6QColor(
    QGradient *self,
    qreal pos,
    const QColor *color) {
  self->setColorAt(pos, *color);
}

//  void QGradient::setStops(const QGradientStops &stops)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QGradient8setStopsERK5QListISt4pairId6QColorEE(
    QGradient *self,
    const QGradientStops *stops) {
  self->setStops(*stops);
}

//  QGradientStops QGradient::stops() const
extern "C" Q_DECL_EXPORT
QGradientStops *ritual_ZNK9QGradient5stopsEv(const QGradient *self) {
  return new QGradientStops(self->stops());
}

//  CoordinateMode QGradient::coordinateMode() const
extern "C" Q_DECL_EXPORT
QGradient::CoordinateMode ritual_ZNK9QGradient14coordinateModeEv(
    const QGradient *self) {
  return self->coordinateMode();
}

//  void QGradient::setCoordinateMode(CoordinateMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QGradient17setCoordinateModeENS_14CoordinateModeE(
    QGradient *self,
    QGradient::CoordinateMode mode) {
  self->setCoordinateMode(mode);
}

//  InterpolationMode QGradient::interpolationMode() const
extern "C" Q_DECL_EXPORT
QGradient::InterpolationMode ritual_ZNK9QGradient17interpolationModeEv(
    const QGradient *self) {
  return self->interpolationMode();
}

//  void QGradient::setInterpolationMode(InterpolationMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QGradient20setInterpolationModeENS_17InterpolationModeE(
    QGradient *self,
    QGradient::InterpolationMode mode) {
  self->setInterpolationMode(mode);
}

//  bool QGradient::operator==(const QGradient &gradient) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QGradienteqERKS_(
    const QGradient *self,
    const QGradient *gradient) {
  return self->operator==(*gradient);
}

//  bool QGradient::operator!=(const QGradient &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QGradientneERKS_(
    const QGradient *self,
    const QGradient *other) {
  return self->operator!=(*other);
}

//  QList<QGradient>::QList()
extern "C" Q_DECL_EXPORT
QList<QGradient> *ritual_list_make_QGradient() {
  return new QList<QGradient>();
}

//  void QList<QGradient>::append(const QGradient &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QGradient(
    QList<QGradient> *self,
    const QGradient *element) {
  self->append(*element);
}

//  qsizetype QList<QGradient>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QGradient(const QList<QGradient> *self) {
  return self->size();
}

//  const QGradient &QList<QGradient>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QGradient *ritual_list_at_QGradient(
    const QList<QGradient> *self,
    long long index) {
  return new QGradient(self->at(index));
}

//  QList<QGradient>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QGradient(QList<QGradient> *self) {
  delete self;
}

//  a QGradientStops a ritual of QGradient gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QGradient__QGradientStops(QGradientStops *self) {
  delete self;
}
