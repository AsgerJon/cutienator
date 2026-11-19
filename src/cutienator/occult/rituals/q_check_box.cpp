//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qcheckbox.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qcheckbox.h>
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>

//  const QMetaObject *QCheckBox::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK9QCheckBox10metaObjectEv(
    const QCheckBox *self) {
  return self->metaObject();
}

//  QString QCheckBox::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN9QCheckBox2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QCheckBox::tr(s, c, n));
}

//  QCheckBox::QCheckBox(QWidget *parent)
extern "C" Q_DECL_EXPORT
QCheckBox *ritual_ZN9QCheckBoxC1EP7QWidget(QWidget *parent) {
  return new QCheckBox(parent);
}

//  QCheckBox::QCheckBox(const QString &text, QWidget *parent)
extern "C" Q_DECL_EXPORT
QCheckBox *ritual_ZN9QCheckBoxC1ERK7QStringP7QWidget(
    const QString *text,
    QWidget *parent) {
  return new QCheckBox(*text, parent);
}

//  QCheckBox::~QCheckBox()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QCheckBoxD1Ev(QCheckBox *self) {
  delete self;
}

//  QSize QCheckBox::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK9QCheckBox8sizeHintEv(const QCheckBox *self) {
  return new QSize(self->sizeHint());
}

//  QSize QCheckBox::minimumSizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK9QCheckBox15minimumSizeHintEv(const QCheckBox *self) {
  return new QSize(self->minimumSizeHint());
}

//  void QCheckBox::setTristate(bool y)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QCheckBox11setTristateEb(QCheckBox *self, bool y) {
  self->setTristate(y);
}

//  bool QCheckBox::isTristate() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QCheckBox10isTristateEv(const QCheckBox *self) {
  return self->isTristate();
}

//  Qt::CheckState QCheckBox::checkState() const
extern "C" Q_DECL_EXPORT
Qt::CheckState ritual_ZNK9QCheckBox10checkStateEv(const QCheckBox *self) {
  return self->checkState();
}

//  void QCheckBox::setCheckState(Qt::CheckState state)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QCheckBox13setCheckStateEN2Qt10CheckStateE(
    QCheckBox *self,
    Qt::CheckState state) {
  self->setCheckState(state);
}
