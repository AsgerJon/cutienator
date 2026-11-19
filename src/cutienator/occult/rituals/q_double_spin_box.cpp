//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qspinbox.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qspinbox.h>
#include <QtCore/qstring.h>

//  const QMetaObject *QDoubleSpinBox::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK14QDoubleSpinBox10metaObjectEv(
    const QDoubleSpinBox *self) {
  return self->metaObject();
}

//  QString QDoubleSpinBox::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN14QDoubleSpinBox2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QDoubleSpinBox::tr(s, c, n));
}

//  QDoubleSpinBox::QDoubleSpinBox(QWidget *parent)
extern "C" Q_DECL_EXPORT
QDoubleSpinBox *ritual_ZN14QDoubleSpinBoxC1EP7QWidget(QWidget *parent) {
  return new QDoubleSpinBox(parent);
}

//  QDoubleSpinBox::~QDoubleSpinBox()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QDoubleSpinBoxD1Ev(QDoubleSpinBox *self) {
  delete self;
}

//  double QDoubleSpinBox::value() const
extern "C" Q_DECL_EXPORT
double ritual_ZNK14QDoubleSpinBox5valueEv(const QDoubleSpinBox *self) {
  return self->value();
}

//  QString QDoubleSpinBox::prefix() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QDoubleSpinBox6prefixEv(const QDoubleSpinBox *self) {
  return new QString(self->prefix());
}

//  void QDoubleSpinBox::setPrefix(const QString &prefix)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QDoubleSpinBox9setPrefixERK7QString(
    QDoubleSpinBox *self,
    const QString *prefix) {
  self->setPrefix(*prefix);
}

//  QString QDoubleSpinBox::suffix() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QDoubleSpinBox6suffixEv(const QDoubleSpinBox *self) {
  return new QString(self->suffix());
}

//  void QDoubleSpinBox::setSuffix(const QString &suffix)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QDoubleSpinBox9setSuffixERK7QString(
    QDoubleSpinBox *self,
    const QString *suffix) {
  self->setSuffix(*suffix);
}

//  QString QDoubleSpinBox::cleanText() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QDoubleSpinBox9cleanTextEv(const QDoubleSpinBox *self) {
  return new QString(self->cleanText());
}

//  double QDoubleSpinBox::singleStep() const
extern "C" Q_DECL_EXPORT
double ritual_ZNK14QDoubleSpinBox10singleStepEv(const QDoubleSpinBox *self) {
  return self->singleStep();
}

//  void QDoubleSpinBox::setSingleStep(double val)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QDoubleSpinBox13setSingleStepEd(
    QDoubleSpinBox *self,
    double val) {
  self->setSingleStep(val);
}

//  double QDoubleSpinBox::minimum() const
extern "C" Q_DECL_EXPORT
double ritual_ZNK14QDoubleSpinBox7minimumEv(const QDoubleSpinBox *self) {
  return self->minimum();
}

//  void QDoubleSpinBox::setMinimum(double min)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QDoubleSpinBox10setMinimumEd(
    QDoubleSpinBox *self,
    double min) {
  self->setMinimum(min);
}

//  double QDoubleSpinBox::maximum() const
extern "C" Q_DECL_EXPORT
double ritual_ZNK14QDoubleSpinBox7maximumEv(const QDoubleSpinBox *self) {
  return self->maximum();
}

//  void QDoubleSpinBox::setMaximum(double max)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QDoubleSpinBox10setMaximumEd(
    QDoubleSpinBox *self,
    double max) {
  self->setMaximum(max);
}

//  void QDoubleSpinBox::setRange(double min, double max)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QDoubleSpinBox8setRangeEdd(
    QDoubleSpinBox *self,
    double min,
    double max) {
  self->setRange(min, max);
}

//  StepType QDoubleSpinBox::stepType() const
extern "C" Q_DECL_EXPORT
QAbstractSpinBox::StepType ritual_ZNK14QDoubleSpinBox8stepTypeEv(
    const QDoubleSpinBox *self) {
  return self->stepType();
}

//  void QDoubleSpinBox::setStepType(StepType stepType)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QDoubleSpinBox11setStepTypeEN16QAbstractSpinBox8StepTypeE(
    QDoubleSpinBox *self,
    QAbstractSpinBox::StepType stepType) {
  self->setStepType(stepType);
}

//  int QDoubleSpinBox::decimals() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QDoubleSpinBox8decimalsEv(const QDoubleSpinBox *self) {
  return self->decimals();
}

//  void QDoubleSpinBox::setDecimals(int prec)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QDoubleSpinBox11setDecimalsEi(
    QDoubleSpinBox *self,
    int prec) {
  self->setDecimals(prec);
}

//  double QDoubleSpinBox::valueFromText(const QString &text) const
extern "C" Q_DECL_EXPORT
double ritual_ZNK14QDoubleSpinBox13valueFromTextERK7QString(
    const QDoubleSpinBox *self,
    const QString *text) {
  return self->valueFromText(*text);
}

//  QString QDoubleSpinBox::textFromValue(double val) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QDoubleSpinBox13textFromValueEd(
    const QDoubleSpinBox *self,
    double val) {
  return new QString(self->textFromValue(val));
}

//  void QDoubleSpinBox::setValue(double val)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QDoubleSpinBox8setValueEd(QDoubleSpinBox *self, double val) {
  self->setValue(val);
}
