//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qradiobutton.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qradiobutton.h>
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>

//  const QMetaObject *QRadioButton::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK12QRadioButton10metaObjectEv(
    const QRadioButton *self) {
  return self->metaObject();
}

//  QString QRadioButton::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN12QRadioButton2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QRadioButton::tr(s, c, n));
}

//  QRadioButton::QRadioButton(QWidget *parent)
extern "C" Q_DECL_EXPORT
QRadioButton *ritual_ZN12QRadioButtonC1EP7QWidget(QWidget *parent) {
  return new QRadioButton(parent);
}

//  QRadioButton::QRadioButton(const QString &text, QWidget *parent)
extern "C" Q_DECL_EXPORT
QRadioButton *ritual_ZN12QRadioButtonC1ERK7QStringP7QWidget(
    const QString *text,
    QWidget *parent) {
  return new QRadioButton(*text, parent);
}

//  QRadioButton::~QRadioButton()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QRadioButtonD1Ev(QRadioButton *self) {
  delete self;
}

//  QSize QRadioButton::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK12QRadioButton8sizeHintEv(const QRadioButton *self) {
  return new QSize(self->sizeHint());
}

//  QSize QRadioButton::minimumSizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK12QRadioButton15minimumSizeHintEv(
    const QRadioButton *self) {
  return new QSize(self->minimumSizeHint());
}
