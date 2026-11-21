//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qcommandlinkbutton.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qcommandlinkbutton.h>
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>

//  const QMetaObject *QCommandLinkButton::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18QCommandLinkButton10metaObjectEv(
    const QCommandLinkButton *self) {
  return self->metaObject();
}

//  QString QCommandLinkButton::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18QCommandLinkButton2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QCommandLinkButton::tr(s, c, n));
}

//  QCommandLinkButton::QCommandLinkButton(QWidget *parent)
extern "C" Q_DECL_EXPORT
QCommandLinkButton *ritual_ZN18QCommandLinkButtonC1EP7QWidget(
    QWidget *parent) {
  return new QCommandLinkButton(parent);
}

//  QCommandLinkButton::QCommandLinkButton(const QString &text, QWidget
//      *parent)
extern "C" Q_DECL_EXPORT
QCommandLinkButton *ritual_ZN18QCommandLinkButtonC1ERK7QStringP7QWidget(
    const QString *text,
    QWidget *parent) {
  return new QCommandLinkButton(*text, parent);
}

//  QCommandLinkButton::QCommandLinkButton(const QString &text, const QString
//      &description, QWidget *parent)
extern "C" Q_DECL_EXPORT
QCommandLinkButton *ritual_ZN18QCommandLinkButtonC1ERK7QStringS2_P7QWidget(
    const QString *text,
    const QString *description,
    QWidget *parent) {
  return new QCommandLinkButton(*text, *description, parent);
}

//  QCommandLinkButton::~QCommandLinkButton()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QCommandLinkButtonD1Ev(QCommandLinkButton *self) {
  delete self;
}

//  QString QCommandLinkButton::description() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18QCommandLinkButton11descriptionEv(
    const QCommandLinkButton *self) {
  return new QString(self->description());
}

//  void QCommandLinkButton::setDescription(const QString &description)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QCommandLinkButton14setDescriptionERK7QString(
    QCommandLinkButton *self,
    const QString *description) {
  self->setDescription(*description);
}

//  QSize QCommandLinkButton::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK18QCommandLinkButton8sizeHintEv(
    const QCommandLinkButton *self) {
  return new QSize(self->sizeHint());
}

//  int QCommandLinkButton::heightForWidth(int a0) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QCommandLinkButton14heightForWidthEi(
    const QCommandLinkButton *self,
    int a0) {
  return self->heightForWidth(a0);
}

//  QSize QCommandLinkButton::minimumSizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK18QCommandLinkButton15minimumSizeHintEv(
    const QCommandLinkButton *self) {
  return new QSize(self->minimumSizeHint());
}

//  void QCommandLinkButton::initStyleOption(QStyleOptionButton *option)
//      const
extern "C" Q_DECL_EXPORT
void ritual_ZNK18QCommandLinkButton15initStyleOptionEP18QStyleOptionButton(
    const QCommandLinkButton *self,
    QStyleOptionButton *option) {
  self->initStyleOption(option);
}
