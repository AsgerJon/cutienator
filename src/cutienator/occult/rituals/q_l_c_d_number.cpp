//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qlcdnumber.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qlcdnumber.h>
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>

//  const QMetaObject *QLCDNumber::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10QLCDNumber10metaObjectEv(
    const QLCDNumber *self) {
  return self->metaObject();
}

//  QString QLCDNumber::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10QLCDNumber2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QLCDNumber::tr(s, c, n));
}

//  QLCDNumber::QLCDNumber(QWidget *parent)
extern "C" Q_DECL_EXPORT
QLCDNumber *ritual_ZN10QLCDNumberC1EP7QWidget(QWidget *parent) {
  return new QLCDNumber(parent);
}

//  QLCDNumber::QLCDNumber(uint numDigits, QWidget *parent)
extern "C" Q_DECL_EXPORT
QLCDNumber *ritual_ZN10QLCDNumberC1EjP7QWidget(
    uint numDigits,
    QWidget *parent) {
  return new QLCDNumber(numDigits, parent);
}

//  QLCDNumber::~QLCDNumber()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QLCDNumberD1Ev(QLCDNumber *self) {
  delete self;
}

//  bool QLCDNumber::smallDecimalPoint() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QLCDNumber17smallDecimalPointEv(const QLCDNumber *self) {
  return self->smallDecimalPoint();
}

//  int QLCDNumber::digitCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QLCDNumber10digitCountEv(const QLCDNumber *self) {
  return self->digitCount();
}

//  void QLCDNumber::setDigitCount(int nDigits)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QLCDNumber13setDigitCountEi(QLCDNumber *self, int nDigits) {
  self->setDigitCount(nDigits);
}

//  bool QLCDNumber::checkOverflow(double num) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QLCDNumber13checkOverflowEd(
    const QLCDNumber *self,
    double num) {
  return self->checkOverflow(num);
}

//  bool QLCDNumber::checkOverflow(int num) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QLCDNumber13checkOverflowEi(
    const QLCDNumber *self,
    int num) {
  return self->checkOverflow(num);
}

//  Mode QLCDNumber::mode() const
extern "C" Q_DECL_EXPORT
QLCDNumber::Mode ritual_ZNK10QLCDNumber4modeEv(const QLCDNumber *self) {
  return self->mode();
}

//  void QLCDNumber::setMode(Mode a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QLCDNumber7setModeENS_4ModeE(
    QLCDNumber *self,
    QLCDNumber::Mode a0) {
  self->setMode(a0);
}

//  SegmentStyle QLCDNumber::segmentStyle() const
extern "C" Q_DECL_EXPORT
QLCDNumber::SegmentStyle ritual_ZNK10QLCDNumber12segmentStyleEv(
    const QLCDNumber *self) {
  return self->segmentStyle();
}

//  void QLCDNumber::setSegmentStyle(SegmentStyle a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QLCDNumber15setSegmentStyleENS_12SegmentStyleE(
    QLCDNumber *self,
    QLCDNumber::SegmentStyle a0) {
  self->setSegmentStyle(a0);
}

//  double QLCDNumber::value() const
extern "C" Q_DECL_EXPORT
double ritual_ZNK10QLCDNumber5valueEv(const QLCDNumber *self) {
  return self->value();
}

//  int QLCDNumber::intValue() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QLCDNumber8intValueEv(const QLCDNumber *self) {
  return self->intValue();
}

//  QSize QLCDNumber::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK10QLCDNumber8sizeHintEv(const QLCDNumber *self) {
  return new QSize(self->sizeHint());
}

//  void QLCDNumber::display(const QString &str)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QLCDNumber7displayERK7QString(
    QLCDNumber *self,
    const QString *str) {
  self->display(*str);
}

//  void QLCDNumber::display(int num)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QLCDNumber7displayEi(QLCDNumber *self, int num) {
  self->display(num);
}

//  void QLCDNumber::display(double num)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QLCDNumber7displayEd(QLCDNumber *self, double num) {
  self->display(num);
}

//  void QLCDNumber::setHexMode()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QLCDNumber10setHexModeEv(QLCDNumber *self) {
  self->setHexMode();
}

//  void QLCDNumber::setDecMode()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QLCDNumber10setDecModeEv(QLCDNumber *self) {
  self->setDecMode();
}

//  void QLCDNumber::setOctMode()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QLCDNumber10setOctModeEv(QLCDNumber *self) {
  self->setOctMode();
}

//  void QLCDNumber::setBinMode()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QLCDNumber10setBinModeEv(QLCDNumber *self) {
  self->setBinMode();
}

//  void QLCDNumber::setSmallDecimalPoint(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QLCDNumber20setSmallDecimalPointEb(
    QLCDNumber *self,
    bool a0) {
  self->setSmallDecimalPoint(a0);
}
