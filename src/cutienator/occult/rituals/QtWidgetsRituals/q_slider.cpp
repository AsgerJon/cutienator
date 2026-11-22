//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qslider.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qslider.h>
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>

//  const QMetaObject *QSlider::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK7QSlider10metaObjectEv(const QSlider *self) {
  return self->metaObject();
}

//  QString QSlider::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QSlider2trEPKcS1_i(const char *s, const char *c, int n) {
  return new QString(QSlider::tr(s, c, n));
}

//  QSlider::QSlider(QWidget *parent)
extern "C" Q_DECL_EXPORT
QSlider *ritual_ZN7QSliderC1EP7QWidget(QWidget *parent) {
  return new QSlider(parent);
}

//  QSlider::QSlider(Qt::Orientation orientation, QWidget *parent)
extern "C" Q_DECL_EXPORT
QSlider *ritual_ZN7QSliderC1EN2Qt11OrientationEP7QWidget(
    Qt::Orientation orientation,
    QWidget *parent) {
  return new QSlider(orientation, parent);
}

//  QSlider::~QSlider()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QSliderD1Ev(QSlider *self) {
  delete self;
}

//  QSize QSlider::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK7QSlider8sizeHintEv(const QSlider *self) {
  return new QSize(self->sizeHint());
}

//  QSize QSlider::minimumSizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK7QSlider15minimumSizeHintEv(const QSlider *self) {
  return new QSize(self->minimumSizeHint());
}

//  void QSlider::setTickPosition(TickPosition position)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QSlider15setTickPositionENS_12TickPositionE(
    QSlider *self,
    QSlider::TickPosition position) {
  self->setTickPosition(position);
}

//  TickPosition QSlider::tickPosition() const
extern "C" Q_DECL_EXPORT
QSlider::TickPosition ritual_ZNK7QSlider12tickPositionEv(
    const QSlider *self) {
  return self->tickPosition();
}

//  void QSlider::setTickInterval(int ti)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QSlider15setTickIntervalEi(QSlider *self, int ti) {
  self->setTickInterval(ti);
}

//  int QSlider::tickInterval() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK7QSlider12tickIntervalEv(const QSlider *self) {
  return self->tickInterval();
}

//  bool QSlider::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN7QSlider5eventEP6QEvent(QSlider *self, QEvent *event) {
  return self->event(event);
}
