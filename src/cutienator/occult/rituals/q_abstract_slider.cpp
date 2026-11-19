//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qabstractslider.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qabstractslider.h>
#include <QtCore/qstring.h>

//  const QMetaObject *QAbstractSlider::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15QAbstractSlider10metaObjectEv(
    const QAbstractSlider *self) {
  return self->metaObject();
}

//  QString QAbstractSlider::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QAbstractSlider2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QAbstractSlider::tr(s, c, n));
}

//  QAbstractSlider::QAbstractSlider(QWidget *parent)
extern "C" Q_DECL_EXPORT
QAbstractSlider *ritual_ZN15QAbstractSliderC1EP7QWidget(QWidget *parent) {
  return new QAbstractSlider(parent);
}

//  QAbstractSlider::~QAbstractSlider()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstractSliderD1Ev(QAbstractSlider *self) {
  delete self;
}

//  Qt::Orientation QAbstractSlider::orientation() const
extern "C" Q_DECL_EXPORT
Qt::Orientation ritual_ZNK15QAbstractSlider11orientationEv(
    const QAbstractSlider *self) {
  return self->orientation();
}

//  void QAbstractSlider::setMinimum(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstractSlider10setMinimumEi(
    QAbstractSlider *self,
    int a0) {
  self->setMinimum(a0);
}

//  int QAbstractSlider::minimum() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QAbstractSlider7minimumEv(const QAbstractSlider *self) {
  return self->minimum();
}

//  void QAbstractSlider::setMaximum(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstractSlider10setMaximumEi(
    QAbstractSlider *self,
    int a0) {
  self->setMaximum(a0);
}

//  int QAbstractSlider::maximum() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QAbstractSlider7maximumEv(const QAbstractSlider *self) {
  return self->maximum();
}

//  void QAbstractSlider::setSingleStep(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstractSlider13setSingleStepEi(
    QAbstractSlider *self,
    int a0) {
  self->setSingleStep(a0);
}

//  int QAbstractSlider::singleStep() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QAbstractSlider10singleStepEv(const QAbstractSlider *self) {
  return self->singleStep();
}

//  void QAbstractSlider::setPageStep(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstractSlider11setPageStepEi(
    QAbstractSlider *self,
    int a0) {
  self->setPageStep(a0);
}

//  int QAbstractSlider::pageStep() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QAbstractSlider8pageStepEv(const QAbstractSlider *self) {
  return self->pageStep();
}

//  void QAbstractSlider::setTracking(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstractSlider11setTrackingEb(
    QAbstractSlider *self,
    bool enable) {
  self->setTracking(enable);
}

//  bool QAbstractSlider::hasTracking() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QAbstractSlider11hasTrackingEv(
    const QAbstractSlider *self) {
  return self->hasTracking();
}

//  void QAbstractSlider::setSliderDown(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstractSlider13setSliderDownEb(
    QAbstractSlider *self,
    bool a0) {
  self->setSliderDown(a0);
}

//  bool QAbstractSlider::isSliderDown() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QAbstractSlider12isSliderDownEv(
    const QAbstractSlider *self) {
  return self->isSliderDown();
}

//  void QAbstractSlider::setSliderPosition(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstractSlider17setSliderPositionEi(
    QAbstractSlider *self,
    int a0) {
  self->setSliderPosition(a0);
}

//  int QAbstractSlider::sliderPosition() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QAbstractSlider14sliderPositionEv(
    const QAbstractSlider *self) {
  return self->sliderPosition();
}

//  void QAbstractSlider::setInvertedAppearance(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstractSlider21setInvertedAppearanceEb(
    QAbstractSlider *self,
    bool a0) {
  self->setInvertedAppearance(a0);
}

//  bool QAbstractSlider::invertedAppearance() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QAbstractSlider18invertedAppearanceEv(
    const QAbstractSlider *self) {
  return self->invertedAppearance();
}

//  void QAbstractSlider::setInvertedControls(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstractSlider19setInvertedControlsEb(
    QAbstractSlider *self,
    bool a0) {
  self->setInvertedControls(a0);
}

//  bool QAbstractSlider::invertedControls() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QAbstractSlider16invertedControlsEv(
    const QAbstractSlider *self) {
  return self->invertedControls();
}

//  int QAbstractSlider::value() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QAbstractSlider5valueEv(const QAbstractSlider *self) {
  return self->value();
}

//  void QAbstractSlider::triggerAction(SliderAction action)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstractSlider13triggerActionENS_12SliderActionE(
    QAbstractSlider *self,
    QAbstractSlider::SliderAction action) {
  self->triggerAction(action);
}

//  void QAbstractSlider::setValue(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstractSlider8setValueEi(QAbstractSlider *self, int a0) {
  self->setValue(a0);
}

//  void QAbstractSlider::setOrientation(Qt::Orientation a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstractSlider14setOrientationEN2Qt11OrientationE(
    QAbstractSlider *self,
    Qt::Orientation a0) {
  self->setOrientation(a0);
}

//  void QAbstractSlider::setRange(int min, int max)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstractSlider8setRangeEii(
    QAbstractSlider *self,
    int min,
    int max) {
  self->setRange(min, max);
}
