//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qabstractspinbox.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qabstractspinbox.h>
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
#include <QtCore/qvariant.h>

//  const QMetaObject *QAbstractSpinBox::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16QAbstractSpinBox10metaObjectEv(
    const QAbstractSpinBox *self) {
  return self->metaObject();
}

//  QString QAbstractSpinBox::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QAbstractSpinBox2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QAbstractSpinBox::tr(s, c, n));
}

//  QAbstractSpinBox::QAbstractSpinBox(QWidget *parent)
extern "C" Q_DECL_EXPORT
QAbstractSpinBox *ritual_ZN16QAbstractSpinBoxC1EP7QWidget(QWidget *parent) {
  return new QAbstractSpinBox(parent);
}

//  QAbstractSpinBox::~QAbstractSpinBox()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QAbstractSpinBoxD1Ev(QAbstractSpinBox *self) {
  delete self;
}

//  ButtonSymbols QAbstractSpinBox::buttonSymbols() const
extern "C" Q_DECL_EXPORT
QAbstractSpinBox::ButtonSymbols ritual_ZNK16QAbstractSpinBox13buttonSymbolsEv(
    const QAbstractSpinBox *self) {
  return self->buttonSymbols();
}

//  void QAbstractSpinBox::setButtonSymbols(ButtonSymbols bs)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QAbstractSpinBox16setButtonSymbolsENS_13ButtonSymbolsE(
    QAbstractSpinBox *self,
    QAbstractSpinBox::ButtonSymbols bs) {
  self->setButtonSymbols(bs);
}

//  void QAbstractSpinBox::setCorrectionMode(CorrectionMode cm)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QAbstractSpinBox17setCorrectionModeENS_14CorrectionModeE(
    QAbstractSpinBox *self,
    QAbstractSpinBox::CorrectionMode cm) {
  self->setCorrectionMode(cm);
}

//  CorrectionMode QAbstractSpinBox::correctionMode() const
extern "C" Q_DECL_EXPORT
QAbstractSpinBox::CorrectionMode ritual_ZNK16QAbstractSpinBox14correctionModeEv(
    const QAbstractSpinBox *self) {
  return self->correctionMode();
}

//  bool QAbstractSpinBox::hasAcceptableInput() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QAbstractSpinBox18hasAcceptableInputEv(
    const QAbstractSpinBox *self) {
  return self->hasAcceptableInput();
}

//  QString QAbstractSpinBox::text() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK16QAbstractSpinBox4textEv(const QAbstractSpinBox *self) {
  return new QString(self->text());
}

//  QString QAbstractSpinBox::specialValueText() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK16QAbstractSpinBox16specialValueTextEv(
    const QAbstractSpinBox *self) {
  return new QString(self->specialValueText());
}

//  void QAbstractSpinBox::setSpecialValueText(const QString &txt)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QAbstractSpinBox19setSpecialValueTextERK7QString(
    QAbstractSpinBox *self,
    const QString *txt) {
  self->setSpecialValueText(*txt);
}

//  bool QAbstractSpinBox::wrapping() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QAbstractSpinBox8wrappingEv(const QAbstractSpinBox *self) {
  return self->wrapping();
}

//  void QAbstractSpinBox::setWrapping(bool w)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QAbstractSpinBox11setWrappingEb(
    QAbstractSpinBox *self,
    bool w) {
  self->setWrapping(w);
}

//  void QAbstractSpinBox::setReadOnly(bool r)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QAbstractSpinBox11setReadOnlyEb(
    QAbstractSpinBox *self,
    bool r) {
  self->setReadOnly(r);
}

//  bool QAbstractSpinBox::isReadOnly() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QAbstractSpinBox10isReadOnlyEv(
    const QAbstractSpinBox *self) {
  return self->isReadOnly();
}

//  void QAbstractSpinBox::setKeyboardTracking(bool kt)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QAbstractSpinBox19setKeyboardTrackingEb(
    QAbstractSpinBox *self,
    bool kt) {
  self->setKeyboardTracking(kt);
}

//  bool QAbstractSpinBox::keyboardTracking() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QAbstractSpinBox16keyboardTrackingEv(
    const QAbstractSpinBox *self) {
  return self->keyboardTracking();
}

//  void QAbstractSpinBox::setAlignment(Qt::Alignment flag)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QAbstractSpinBox12setAlignmentE6QFlagsIN2Qt13AlignmentFlagEE(
    QAbstractSpinBox *self,
    int flag) {
  self->setAlignment(QFlags<Qt::AlignmentFlag>::fromInt(flag));
}

//  Qt::Alignment QAbstractSpinBox::alignment() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QAbstractSpinBox9alignmentEv(const QAbstractSpinBox *self) {
  return static_cast<int>(self->alignment().toInt());
}

//  void QAbstractSpinBox::setFrame(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QAbstractSpinBox8setFrameEb(
    QAbstractSpinBox *self,
    bool a0) {
  self->setFrame(a0);
}

//  bool QAbstractSpinBox::hasFrame() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QAbstractSpinBox8hasFrameEv(const QAbstractSpinBox *self) {
  return self->hasFrame();
}

//  void QAbstractSpinBox::setAccelerated(bool on)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QAbstractSpinBox14setAcceleratedEb(
    QAbstractSpinBox *self,
    bool on) {
  self->setAccelerated(on);
}

//  bool QAbstractSpinBox::isAccelerated() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QAbstractSpinBox13isAcceleratedEv(
    const QAbstractSpinBox *self) {
  return self->isAccelerated();
}

//  void QAbstractSpinBox::setGroupSeparatorShown(bool shown)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QAbstractSpinBox22setGroupSeparatorShownEb(
    QAbstractSpinBox *self,
    bool shown) {
  self->setGroupSeparatorShown(shown);
}

//  bool QAbstractSpinBox::isGroupSeparatorShown() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QAbstractSpinBox21isGroupSeparatorShownEv(
    const QAbstractSpinBox *self) {
  return self->isGroupSeparatorShown();
}

//  QSize QAbstractSpinBox::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK16QAbstractSpinBox8sizeHintEv(
    const QAbstractSpinBox *self) {
  return new QSize(self->sizeHint());
}

//  QSize QAbstractSpinBox::minimumSizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK16QAbstractSpinBox15minimumSizeHintEv(
    const QAbstractSpinBox *self) {
  return new QSize(self->minimumSizeHint());
}

//  void QAbstractSpinBox::interpretText()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QAbstractSpinBox13interpretTextEv(QAbstractSpinBox *self) {
  self->interpretText();
}

//  bool QAbstractSpinBox::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QAbstractSpinBox5eventEP6QEvent(
    QAbstractSpinBox *self,
    QEvent *event) {
  return self->event(event);
}

//  QVariant QAbstractSpinBox::inputMethodQuery(Qt::InputMethodQuery a0)
//      const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK16QAbstractSpinBox16inputMethodQueryEN2Qt16InputMethodQueryE(
    const QAbstractSpinBox *self,
    Qt::InputMethodQuery a0) {
  return new QVariant(self->inputMethodQuery(a0));
}

//  void QAbstractSpinBox::stepBy(int steps)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QAbstractSpinBox6stepByEi(
    QAbstractSpinBox *self,
    int steps) {
  self->stepBy(steps);
}

//  void QAbstractSpinBox::stepUp()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QAbstractSpinBox6stepUpEv(QAbstractSpinBox *self) {
  self->stepUp();
}

//  void QAbstractSpinBox::stepDown()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QAbstractSpinBox8stepDownEv(QAbstractSpinBox *self) {
  self->stepDown();
}

//  void QAbstractSpinBox::selectAll()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QAbstractSpinBox9selectAllEv(QAbstractSpinBox *self) {
  self->selectAll();
}

//  void QAbstractSpinBox::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QAbstractSpinBox5clearEv(QAbstractSpinBox *self) {
  self->clear();
}
