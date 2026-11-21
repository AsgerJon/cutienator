//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qerrormessage.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qerrormessage.h>
#include <QtCore/qstring.h>

//  const QMetaObject *QErrorMessage::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13QErrorMessage10metaObjectEv(
    const QErrorMessage *self) {
  return self->metaObject();
}

//  QString QErrorMessage::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13QErrorMessage2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QErrorMessage::tr(s, c, n));
}

//  QErrorMessage::QErrorMessage(QWidget *parent)
extern "C" Q_DECL_EXPORT
QErrorMessage *ritual_ZN13QErrorMessageC1EP7QWidget(QWidget *parent) {
  return new QErrorMessage(parent);
}

//  QErrorMessage::~QErrorMessage()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QErrorMessageD1Ev(QErrorMessage *self) {
  delete self;
}

//  QErrorMessage *QErrorMessage::qtHandler()
extern "C" Q_DECL_EXPORT
QErrorMessage *ritual_ZN13QErrorMessage9qtHandlerEv() {
  return QErrorMessage::qtHandler();
}

//  void QErrorMessage::showMessage(const QString &message)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QErrorMessage11showMessageERK7QString(
    QErrorMessage *self,
    const QString *message) {
  self->showMessage(*message);
}

//  void QErrorMessage::showMessage(const QString &message, const QString
//      &type)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QErrorMessage11showMessageERK7QStringS2_(
    QErrorMessage *self,
    const QString *message,
    const QString *type) {
  self->showMessage(*message, *type);
}
