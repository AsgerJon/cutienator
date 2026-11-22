//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qspinbox.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qspinbox.h>
#include <QtCore/qstring.h>

//  const QMetaObject *QSpinBox::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK8QSpinBox10metaObjectEv(const QSpinBox *self) {
  return self->metaObject();
}

//  QString QSpinBox::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN8QSpinBox2trEPKcS1_i(const char *s, const char *c, int n) {
  return new QString(QSpinBox::tr(s, c, n));
}

//  QSpinBox::QSpinBox(QWidget *parent)
extern "C" Q_DECL_EXPORT
QSpinBox *ritual_ZN8QSpinBoxC1EP7QWidget(QWidget *parent) {
  return new QSpinBox(parent);
}

//  QSpinBox::~QSpinBox()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QSpinBoxD1Ev(QSpinBox *self) {
  delete self;
}

//  int QSpinBox::value() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK8QSpinBox5valueEv(const QSpinBox *self) {
  return self->value();
}

//  QString QSpinBox::prefix() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK8QSpinBox6prefixEv(const QSpinBox *self) {
  return new QString(self->prefix());
}

//  void QSpinBox::setPrefix(const QString &prefix)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QSpinBox9setPrefixERK7QString(
    QSpinBox *self,
    const QString *prefix) {
  self->setPrefix(*prefix);
}

//  QString QSpinBox::suffix() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK8QSpinBox6suffixEv(const QSpinBox *self) {
  return new QString(self->suffix());
}

//  void QSpinBox::setSuffix(const QString &suffix)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QSpinBox9setSuffixERK7QString(
    QSpinBox *self,
    const QString *suffix) {
  self->setSuffix(*suffix);
}

//  QString QSpinBox::cleanText() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK8QSpinBox9cleanTextEv(const QSpinBox *self) {
  return new QString(self->cleanText());
}

//  int QSpinBox::singleStep() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK8QSpinBox10singleStepEv(const QSpinBox *self) {
  return self->singleStep();
}

//  void QSpinBox::setSingleStep(int val)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QSpinBox13setSingleStepEi(QSpinBox *self, int val) {
  self->setSingleStep(val);
}

//  int QSpinBox::minimum() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK8QSpinBox7minimumEv(const QSpinBox *self) {
  return self->minimum();
}

//  void QSpinBox::setMinimum(int min)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QSpinBox10setMinimumEi(QSpinBox *self, int min) {
  self->setMinimum(min);
}

//  int QSpinBox::maximum() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK8QSpinBox7maximumEv(const QSpinBox *self) {
  return self->maximum();
}

//  void QSpinBox::setMaximum(int max)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QSpinBox10setMaximumEi(QSpinBox *self, int max) {
  self->setMaximum(max);
}

//  void QSpinBox::setRange(int min, int max)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QSpinBox8setRangeEii(QSpinBox *self, int min, int max) {
  self->setRange(min, max);
}

//  StepType QSpinBox::stepType() const
extern "C" Q_DECL_EXPORT
QAbstractSpinBox::StepType ritual_ZNK8QSpinBox8stepTypeEv(
    const QSpinBox *self) {
  return self->stepType();
}

//  void QSpinBox::setStepType(StepType stepType)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QSpinBox11setStepTypeEN16QAbstractSpinBox8StepTypeE(
    QSpinBox *self,
    QAbstractSpinBox::StepType stepType) {
  self->setStepType(stepType);
}

//  int QSpinBox::displayIntegerBase() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK8QSpinBox18displayIntegerBaseEv(const QSpinBox *self) {
  return self->displayIntegerBase();
}

//  void QSpinBox::setDisplayIntegerBase(int base)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QSpinBox21setDisplayIntegerBaseEi(QSpinBox *self, int base) {
  self->setDisplayIntegerBase(base);
}

//  void QSpinBox::setValue(int val)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QSpinBox8setValueEi(QSpinBox *self, int val) {
  self->setValue(val);
}
