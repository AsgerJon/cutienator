//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qprogressbar.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qprogressbar.h>
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>

//  const QMetaObject *QProgressBar::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK12QProgressBar10metaObjectEv(
    const QProgressBar *self) {
  return self->metaObject();
}

//  QString QProgressBar::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN12QProgressBar2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QProgressBar::tr(s, c, n));
}

//  QProgressBar::QProgressBar(QWidget *parent)
extern "C" Q_DECL_EXPORT
QProgressBar *ritual_ZN12QProgressBarC1EP7QWidget(QWidget *parent) {
  return new QProgressBar(parent);
}

//  QProgressBar::~QProgressBar()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QProgressBarD1Ev(QProgressBar *self) {
  delete self;
}

//  int QProgressBar::minimum() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QProgressBar7minimumEv(const QProgressBar *self) {
  return self->minimum();
}

//  int QProgressBar::maximum() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QProgressBar7maximumEv(const QProgressBar *self) {
  return self->maximum();
}

//  int QProgressBar::value() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QProgressBar5valueEv(const QProgressBar *self) {
  return self->value();
}

//  QString QProgressBar::text() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK12QProgressBar4textEv(const QProgressBar *self) {
  return new QString(self->text());
}

//  void QProgressBar::setTextVisible(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QProgressBar14setTextVisibleEb(
    QProgressBar *self,
    bool visible) {
  self->setTextVisible(visible);
}

//  bool QProgressBar::isTextVisible() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QProgressBar13isTextVisibleEv(const QProgressBar *self) {
  return self->isTextVisible();
}

//  Qt::Alignment QProgressBar::alignment() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QProgressBar9alignmentEv(const QProgressBar *self) {
  return static_cast<int>(self->alignment().toInt());
}

//  void QProgressBar::setAlignment(Qt::Alignment alignment)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QProgressBar12setAlignmentE6QFlagsIN2Qt13AlignmentFlagEE(
    QProgressBar *self,
    int alignment) {
  self->setAlignment(QFlags<Qt::AlignmentFlag>::fromInt(alignment));
}

//  QSize QProgressBar::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK12QProgressBar8sizeHintEv(const QProgressBar *self) {
  return new QSize(self->sizeHint());
}

//  QSize QProgressBar::minimumSizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK12QProgressBar15minimumSizeHintEv(
    const QProgressBar *self) {
  return new QSize(self->minimumSizeHint());
}

//  Qt::Orientation QProgressBar::orientation() const
extern "C" Q_DECL_EXPORT
Qt::Orientation ritual_ZNK12QProgressBar11orientationEv(
    const QProgressBar *self) {
  return self->orientation();
}

//  void QProgressBar::setInvertedAppearance(bool invert)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QProgressBar21setInvertedAppearanceEb(
    QProgressBar *self,
    bool invert) {
  self->setInvertedAppearance(invert);
}

//  bool QProgressBar::invertedAppearance() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QProgressBar18invertedAppearanceEv(
    const QProgressBar *self) {
  return self->invertedAppearance();
}

//  void QProgressBar::setTextDirection(QProgressBar::Direction
//      textDirection)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QProgressBar16setTextDirectionENS_9DirectionE(
    QProgressBar *self,
    QProgressBar::Direction textDirection) {
  self->setTextDirection(textDirection);
}

//  QProgressBar::Direction QProgressBar::textDirection() const
extern "C" Q_DECL_EXPORT
QProgressBar::Direction ritual_ZNK12QProgressBar13textDirectionEv(
    const QProgressBar *self) {
  return self->textDirection();
}

//  void QProgressBar::setFormat(const QString &format)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QProgressBar9setFormatERK7QString(
    QProgressBar *self,
    const QString *format) {
  self->setFormat(*format);
}

//  void QProgressBar::resetFormat()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QProgressBar11resetFormatEv(QProgressBar *self) {
  self->resetFormat();
}

//  QString QProgressBar::format() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK12QProgressBar6formatEv(const QProgressBar *self) {
  return new QString(self->format());
}

//  void QProgressBar::reset()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QProgressBar5resetEv(QProgressBar *self) {
  self->reset();
}

//  void QProgressBar::setRange(int minimum, int maximum)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QProgressBar8setRangeEii(
    QProgressBar *self,
    int minimum,
    int maximum) {
  self->setRange(minimum, maximum);
}

//  void QProgressBar::setMinimum(int minimum)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QProgressBar10setMinimumEi(QProgressBar *self, int minimum) {
  self->setMinimum(minimum);
}

//  void QProgressBar::setMaximum(int maximum)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QProgressBar10setMaximumEi(QProgressBar *self, int maximum) {
  self->setMaximum(maximum);
}

//  void QProgressBar::setValue(int value)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QProgressBar8setValueEi(QProgressBar *self, int value) {
  self->setValue(value);
}

//  void QProgressBar::setOrientation(Qt::Orientation a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QProgressBar14setOrientationEN2Qt11OrientationE(
    QProgressBar *self,
    Qt::Orientation a0) {
  self->setOrientation(a0);
}
